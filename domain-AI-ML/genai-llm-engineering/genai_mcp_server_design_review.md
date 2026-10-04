---
title: "MCP Server Design Review — Primitive Inventory, Model-Facing Descriptions, Response Budgets, Recoverable Errors, Transport, Auth, and Versioning"
category: AI-ML/genai-llm-engineering
description: "Review a whole MCP server before or after release — the tool/resource/prompt inventory and its granularity, names and descriptions as the model's only selection signal, schemas, pagination and per-response token budgets, error shapes a model can recover from, stdio vs streamable-HTTP transport, authorization, versioning, and evidence from runs with real model clients — producing a severity-ranked findings list rather than a redesign."
techniques:
  - AG-37
  - IPC-02
  - IPC-03
  - IPC-04
  - AG-42
difficulty: advanced
tags:
  - mcp
  - mcp-server
  - tool-design
  - api-review
  - context-efficiency
  - agent-tooling
  - review-my-mcp-server
  - model-picks-wrong-tool
  - tool-output-too-big
updated: "2026-10-02"
related_prompts:
  - domain-AI-ML/genai-llm-engineering/genai_mcp_tool_interface_design.md
  - domain-AI-ML/genai-llm-engineering/genai_mcp_server_threat_model.md
  - domain-AI-ML/genai-llm-engineering/genai_context_window_strategy.md
---

# MCP Server Design Review

**Objective:** Review an existing or near-release Model Context Protocol server as a *product whose user is a model* — whether its set of tools, resources, and prompts is the right size and shape, whether a model with no other context can choose and call them correctly, whether responses fit a context budget, whether errors lead to a correct retry, and whether transport, authorization, and versioning hold up for clients you do not control — and return a severity-ranked findings list with the evidence behind each finding.

**When to Use:**
- An MCP server exists (often generated from an OpenAPI spec or a thin SDK wrapper) and models select the wrong tool, loop, or exhaust context.
- A server is about to be published to clients and models you do not control, and needs a release review.
- You inherited a server with dozens of tools and need to know which to merge, cut, or move to resources.
- Moving a local stdio server to a hosted streamable-HTTP deployment, which changes the auth and session story.

**When NOT to Use:**
- You are designing **one tool's** interface from scratch — use `domain-AI-ML/genai-llm-engineering/genai_mcp_tool_interface_design.md`; this prompt reviews the **whole server** and cites that one for per-tool fixes.
- The question is what an attacker can do through the server or client (poisoning, injection, token handling) — use `domain-AI-ML/genai-llm-engineering/genai_mcp_server_threat_model.md`; this review flags security-relevant design smells and hands them over.
- You are deciding how tools compose inside an agent's loop — use `domain-AI-ML/agentic-ai-systems/aiagent_tool_design.md`.

## Inputs / Context

- **The server's advertised surface** — the full tools/list, resources/list (and templates), and prompts/list output exactly as a client receives it, including descriptions and input/output schemas.
- **Underlying system** — what API, database, or service the server fronts, and which operations write or delete.
- **Target clients and models** — known host applications, or "unknown/public".
- **Transport and deployment** — stdio (local process) and/or streamable HTTP (hosted); who runs it, under whose identity.
- **Auth model** — how the server authenticates the user and what credential it uses downstream.
- **Response size samples** — typical and worst-case payloads per tool, in bytes or tokens.
- **Run evidence** (strongly preferred) — transcripts or logs of real model clients doing realistic tasks against the server.

## Constraints

**Must:**
- Review from the **model's seat first**: read only what a client receives (names, descriptions, schemas), never the source code, before judging selection and calling.
- Classify every capability as **tool** (model-invoked action or query), **resource** (application-selected context, addressable by URI), or **prompt** (user-selected template), and flag mis-assignments.
- Set an explicit **per-response token budget** and test every list-returning tool against its worst case.
- Distinguish **protocol errors** (malformed request, unknown tool) from **tool execution errors** returned as a result the model can read and act on.
- Ground every severity rating in evidence — a run transcript, a measured payload, or a schema defect — and label findings inferred without run evidence as `unverified`.
- Mark protocol details (transport names, auth requirements, result fields, pagination cursors, annotation semantics) `[verify against current MCP specification]` — the spec revises.

**Must Not:**
- Treat tool **annotations** (read-only, destructive, idempotent hints) as enforcement; they are untrusted hints to the client, so the review must check that the server itself enforces the behaviour they claim.
- Approve a 1:1 endpoint wrapper because each tool "works"; the review question is whether a model completes tasks, not whether each call succeeds in isolation.
- Accept unbounded list responses, or truncation without a marker the model can see.
- Hardcode a model name or a token limit as fact; budgets are stated as the user's choice.

**Instructions:**

1. **Reconstruct the task inventory.** List the 5–15 tasks a model will actually be asked to do through this server. Every later finding refers back to a task; a tool that serves no task is a cut candidate.

2. **Inventory the primitives.** Table every tool, resource, and prompt with: task served, read/write/delete, and primitive fit. Common mis-assignments: static reference data exposed as a tool (should be a resource), a multi-step workflow the user triggers exposed as five tools (should be a prompt or one task-level tool), and write operations exposed as resources.

3. **Judge granularity.** Flag (a) **endpoint mirroring** — a task needs 3+ chained calls where one task-level tool would do; (b) **overlap** — two tools whose distinction you cannot state in one sentence; (c) **sprawl** — tool count above what the target clients handle well (record the count; the threshold is the user's measurement, not a constant). Recommend merge, cut, or move-to-resource per row.

4. **Read names and descriptions as the only trigger signal (AG-37).** For each tool, the description must say what it does, when to use it, when *not* to (naming the confusable sibling), what it returns, and side effects. Flag internal jargon, missing "not this one" clauses, and descriptions that differ from actual behaviour. Check that tool names are unique and stable — clients may namespace or truncate them `[verify]`.

5. **Check schemas.** Required parameters minimal; every parameter has a format and an example; closed value sets are enums; IDs say where they come from ("customer_id from find_customer"). Where an output schema is declared, check that results actually conform.

6. **Set and test response budgets (AG-42, IPC-04).** Pick a per-call budget with the user (for example 2–4k tokens for routine calls). For each list-returning tool, scale-test mentally and with real data: what does the call return against the largest tenant, not the demo account? Require cursor pagination with a stated page size, a `has_more`/next-cursor signal, and a **total or remaining count** so a model can tell a short page from a truncated one. Strip fields that support no decision.

7. **Review error shapes (IPC-02).** Each tool's failures should come back as a readable result flagged as an error, with a fixed vocabulary — e.g. `invalid_argument`, `not_found`, `permission_denied`, `rate_limited`, `upstream_unavailable` — plus the offending value, a valid example, and a retryable/terminal flag. Flag stack traces, bare HTTP codes, and silent empty results that hide a failure.

8. **Review transport and session handling.** stdio: the server runs with the launching user's OS privileges — confirm it needs nothing more, and that it writes nothing but protocol messages to stdout. Streamable HTTP: confirm session handling, origin validation and localhost binding for local HTTP servers, timeouts for long operations, and progress notifications for slow tools `[verify against current MCP specification]`.

9. **Review authorization.** Per-user identity or a shared service credential? Does each downstream call act with the *user's* scope? Is the token the server received used only for this server and never forwarded downstream? Flag anything here as `security — see threat model` and hand it to `genai_mcp_server_threat_model.md` rather than resolving it in this review.

10. **Review versioning (IPC-03).** Clients cache tool lists and models learn names. Require: additive changes by default; renames ship as a new tool with the old one deprecated and still working; a declared server version; a changelog entry when any description changes, since a description change alters model behaviour as much as a code change does; and use of the list-changed notification when the surface changes at runtime.

11. **Weigh run evidence.** From real model-client transcripts, compute per task: first-call tool-selection accuracy, first-call argument validity, error-recovery rate, calls per completed task, and context consumed by tool results. Map each failure to a finding from steps 3–9. If no transcripts exist, the top recommendation is to produce them.

12. **Rank and hand off.** Severity: **Blocker** (data loss, cross-user data exposure, or a core task that cannot be completed), **Major** (wrong tool or context exhaustion on a common task), **Minor** (cost or clarity). Each finding names its fix and the prompt that owns the fix.

**Output Format:**

```
# MCP server review — [server]   Transport: [stdio | streamable HTTP | both]   Clients: [..]
## Task inventory
## Primitive inventory      | Name | Primitive | Task | R/W/D | Fit | Action (keep/merge/cut/move) |
## Description findings     | Tool | Problem | Rewrite (as the model will read it) |
## Schema findings
## Response budgets         | Tool | Worst case (tokens) | Budget | Pagination + count? | Action |
## Error shapes             | Tool | Current failure output | Required shape | Retryable? |
## Transport & sessions
## Authorization (handed to threat model)
## Versioning
## Run evidence             | Metric | Value | n | Source |
## Findings (ranked)        | # | Severity | Finding | Evidence | Fix | Owner prompt |
## Unverified items
```

## Verification

- [ ] Every tool, resource, and prompt in the advertised surface appears in the inventory with a task and a primitive-fit judgment.
- [ ] Descriptions were judged from the client's view, not the source code.
- [ ] Each list-returning tool has a measured or estimated worst case against a stated budget.
- [ ] Pagination includes a continuation signal and a count, not only a page.
- [ ] Error findings distinguish protocol errors from tool execution errors.
- [ ] Annotations are checked against enforced server behaviour, not taken at face value.
- [ ] Auth findings are handed to the threat model, not silently resolved.
- [ ] Every severity rating cites evidence; inferred findings are labelled `unverified`.
- [ ] Protocol specifics carry `[verify against current MCP specification]`.

## False-Positive Prevention

❌ **DON'T:**
- Call a server healthy because every tool passes its unit tests — a model can still pick the wrong one 30% of the time; only client runs show it.
- Count tools and stop — a 6-tool server with two indistinguishable tools is worse than a 12-tool server with crisp boundaries.
- Size responses against the demo tenant; the 40-row fixture becomes a 9,000-row production account.
- Read `destructiveHint: false` as proof a tool cannot delete anything — it is a claim the server makes about itself.
- Grade descriptions on grammar; grade them on whether they prevent the observed confusion.
- Recommend a full redesign when three description rewrites and one merge fix the measured failures.

✅ **DO:**
- Tie every finding to a task the model must complete.
- Quote the description exactly as the model reads it, then the rewrite.
- Require a count alongside every page so truncation is visible to the model.
- Treat a description change as a versioned, changelogged release.
- Separate what you measured from what you inferred.

## Example Output

```markdown
# MCP server review — tracker-mcp (issue tracker)   Transport: stdio now, streamable HTTP planned
Clients: two internal coding assistants + "any MCP client" after publication. Budget agreed: 3k tokens/call.

## Task inventory
T1 find an issue from partial text · T2 read one issue with comments · T3 list my open issues ·
T4 create an issue · T5 comment on an issue · T6 change status/assignee · T7 read team conventions

## Primitive inventory (31 tools, generated from the OpenAPI spec)
| Name                      | Primitive | Task | R/W/D | Fit | Action |
| get_issue / get_issue_v2  | tool      | T2   | R     | duplicate | merge → get_issue |
| list_issues, search_issues, query_issues | tool | T1,T3 | R | overlap | merge → search_issues(filters) |
| get_label_colors, get_workflow_schema | tool | — | R | static reference | move → resource tracker://conventions |
| bulk_delete_issues        | tool      | none | D     | no task needs it | cut from model surface |
| add_comment, edit_comment | tool      | T5   | W     | ok  | keep add_comment; cut edit_comment (no task) |
| ...19 admin endpoints     | tool      | none | R/W   | sprawl | cut |
Result: 31 → 7 tools + 1 resource.

## Description findings
| search_issues | "Searches issues using JQL-like syntax." | "Find issues by free text, assignee, or status. Use
  for 'find' and 'my open issues'. Returns id, title, status, assignee — NOT comments; call get_issue for
  those. Read-only." |

## Response budgets
| Tool          | Worst case            | Budget | Pagination + count? | Action |
| list_issues   | 500 issues ≈ 180 KB ≈ ~45k tokens (bytes/4, rough) | 3k | none | page 25, cursor, total_count |
| get_issue     | 1 issue + 212 comments ≈ 14k tokens | 3k | none | last 10 comments + comments_remaining: 202 |

## Error shapes
| create_issue | raw upstream stack trace (2.1 KB) | {error:"invalid_argument", field:"priority",
  received:"urgent", allowed:["p0","p1","p2","p3"], retryable:true} | yes |
| any          | HTTP 429 as text "Too Many Requests" | rate_limited + retry_after_s, retryable:true | yes |

## Transport & sessions
stdio build logs debug lines to stdout → corrupts the protocol stream under load (Blocker for stdio users).

## Authorization (handed to threat model)
One shared admin API key for all users; every caller can read every project. → genai_mcp_server_threat_model.md

## Versioning
No server version declared; get_issue_v2 shipped as a rename with get_issue silently changed. Adopt additive-only.

## Run evidence (40 scripted tasks × 2 clients, before fixes)
| First-call tool selection | 26/40 (65%) | most errors: list vs search vs query |
| Context exhausted mid-task | 6/40 | all via list_issues on the large project |
| Recovered from error unaided | 3/11 | stack-trace errors gave nothing to correct |

## Findings (ranked)
| 1 | Blocker | stdout logging breaks stdio | reproduced | log to stderr | — |
| 2 | Blocker | shared admin key → cross-project reads | config | per-user tokens | threat model |
| 3 | Major | 3 overlapping search tools | 14/40 wrong-tool | merge + rewrite | genai_mcp_tool_interface_design.md |
| 4 | Major | unbounded list_issues | 6/40 exhaustion | page + count | this review |
| 5 | Major | errors unrecoverable | 3/11 recovery | fixed vocabulary | this review |
| 6 | Minor | static data as tools | inventory | move to resource | this review |

## Unverified items
Annotation semantics and session-header behaviour for the HTTP move [verify against current MCP specification].
```

**Techniques Used:**
- **AG-37 (Description-as-Trigger Discipline):** tool descriptions are reviewed as the model's only selection signal, with explicit "not this one" clauses.
- **IPC-02 (Typed Status + Fixed Error Vocabulary):** tool failures are required to return an enumerated error code with a retryable flag, not prose or stack traces.
- **IPC-03 (Contract-Version Literal):** the server declares a version and treats renames and description changes as versioned contract changes.
- **IPC-04 (Count-and-Sequence Checksums):** every paginated result carries a total or remaining count so truncation is detectable by the model.
- **AG-42 (Tool-Call Scale Test):** list tools and chained-call patterns are tested against the largest real tenant, not the demo fixture.

**Related Prompts:**
- `genai_mcp_tool_interface_design.md` — designing one tool's interface; this review cites it for per-tool rewrites.
- `genai_mcp_server_threat_model.md` — the adversarial review that receives this review's auth and annotation findings.
- `genai_context_window_strategy.md` — the context budget that per-call response limits are carved from.
