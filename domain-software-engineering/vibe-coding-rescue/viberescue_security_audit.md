---
title: "Security and Resilience Audit of AI-Generated Code"
category: software-engineering/vibe-coding-rescue
description: "Audit an AI-assisted codebase for the specific classes of security and resilience defects AI-generated code tends to produce — confidently-wrong auth, concat'd SQL, swallowed exceptions, optimistic happy paths, missing input validation — with evidence requirements and confidence labels."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-01
  - RT-07
  - RT-11
  - QA-01
difficulty: advanced
tags:
  - vibe-coding
  - security-audit
  - resilience
  - ai-code-review
  - defensive-security
updated: "2026-04-21"
related_prompts:
  - domain-software-engineering/vibe-coding-rescue/viberescue_wall_diagnosis.md
  - domain-software-engineering/vibe-coding-rescue/viberescue_engineer_handoff_briefing.md
  - domain-software-engineering/analysis/security/security_vulnerability_analysis.md
  - domain-software-engineering/analysis/security/security_sql_injection_analysis.md
  - domain-software-engineering/analysis/security/security_llm_application_review.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_agent_code_footgun_detector.md
---

# Security and Resilience Audit of AI-Generated Code

**Purpose:** AI-generated code has characteristic failure patterns different from human code: confidently plausible auth logic, string-concat SQL inside "helpful" migration scripts, broad try/except blocks that swallow errors, optimistic happy paths without edge-case handling, re-implemented crypto, input validation that checks the shape but not the semantics. This audit runs against those specific patterns, produces findings with confidence levels and evidence citations, and refuses to pattern-match without tracing actual data flow.

**When to use:**
- A codebase built largely with AI assistance is going to production, is in production, or is about to be handed to a new engineer (see `viberescue_engineer_handoff_briefing.md`).
- A security review is needed but the reviewer wants AI-specific patterns checked explicitly, not only the standard OWASP pass (which is also needed — see `security_vulnerability_analysis.md`).
- A team suspects their AI-generated code has "looks-right" bugs that a normal review misses.
- A defensive security effort before hardening or productionizing a side-project.

**Don't use when:** The codebase is safety-critical or operates in a regulated industry at a level requiring formal review. This audit complements, not replaces, such reviews.

**Audience:** The engineer or a trusted reviewer. Output is a findings report ready to hand to a remediator.

---

## Inputs Required

1. **Repo access.** Language, framework, rough LOC, entry points (HTTP routes, queue consumers, CLI, cron).
2. **Data sensitivity.** What data flows through: PII, financial, credentials, customer content, internal-only. Regulatory posture.
3. **Deployment posture.** Internet-facing / internal / local-only. Authentication used. Multi-tenant yes/no.
4. **AI-assistance history.** Rough fraction of code AI-assisted. Any areas the user explicitly wrote by hand (those can still be audited but the AI-specific-pattern risks change).
5. **Known areas of concern.** Any files or flows the user suspects.
6. **Tests and CI status.** Is there a test suite? Does it include auth / input-validation / data-isolation tests? Does CI block merges on anything?

---

## Instructions

### Step 1 — Establish scope and an evidence rule

Audit scope is the entry points (input 1) and every data path they reach — not "all files." For each file flagged, the finding must include a specific file path and line range. No findings without evidence.

### Step 2 — Run each of the AI-specific pattern categories

The categories below are where AI code goes wrong more often than hand-written code. For each, scan and collect findings.

#### 2.1 Confidently-wrong auth
- Hand-rolled auth middleware where a framework primitive exists.
- Role/permission checks that rely on string comparison of unverified inputs.
- Missing permission checks on routes that look similar to a protected route but aren't.
- Session / token validation that skips expiry or issuer checks because "the example didn't."
- Multi-tenant isolation based on a URL parameter without cross-check against authenticated tenant.

#### 2.2 SQL and query construction
- String concatenation or f-string interpolation into queries.
- ORM calls that reach `raw()` with user input.
- `LIKE` queries with unescaped user input.
- Query builders where user-supplied column/table names are interpolated.

#### 2.3 Swallowed and broad error handling
- `except Exception:` / `catch (Throwable)` / `catch(any)` with `pass` or a log and continue.
- Error handling that masks security-relevant failures (auth error becomes "something went wrong").
- Retries that suppress the underlying error forever.
- Errors caught and then the happy-path code runs anyway.

#### 2.4 Input validation holes
- Inputs validated for type / shape but not for semantic constraints (a valid UUID that's someone else's user; a valid integer that's out of expected range; a valid URL that's internal).
- Missing size limits / timeout limits on user-controlled inputs.
- Path / filename inputs without traversal protection.
- Redirect / forward targets built from user input without allow-list.

#### 2.5 Deserialization and data import
- Un-validated deserialization of user-provided data (pickle, YAML unsafe-load, JSON.parse with `eval`-equivalents).
- CSV / Excel / JSON ingestion that trusts the uploader.
- Template rendering that interpolates user input without escaping.

#### 2.6 Crypto / secrets
- Hand-rolled crypto; home-grown hashing for passwords; non-constant-time comparisons.
- Secrets in source, in configs, or echoed in logs.
- Hard-coded keys, tokens, salts, or "dev" credentials in prod paths.
- TLS / cert verification disabled.

#### 2.7 External calls / SSRF / webhooks
- HTTP clients that follow redirects with user-supplied URLs and no allow-list.
- Webhook receivers without signature verification.
- External calls inside a request handler without timeout or retry bound.
- LLM / AI prompts constructed with user input that flows back into code paths or tool calls without sanitization (`security_llm_application_review.md` applies).

#### 2.8 Optimistic happy paths (resilience)
- Code that assumes external services return 200.
- No handling for partial failures (some items succeed, some fail).
- Idempotency assumed where retries can double-apply (emails sent twice, payments double-charged).
- Missing dead-letter / manual-handling path for persistent failures.
- Correlated failure handling (all workers retry immediately → thundering herd).

#### 2.9 Tenant / data isolation
- Queries that accept a `tenant_id` from the request, not from the authenticated principal.
- Shared caches keyed only by object id without tenant scoping.
- Background jobs that lose tenant context and operate cross-tenant.

#### 2.10 Logging and PII
- Full request bodies, tokens, or credentials logged.
- PII logged at debug or info level.
- Error logs that include sensitive user content in a fixed format that downstream tools index.

### Step 3 — Distinguish the AI-specific failure shape

For each finding, note whether the pattern is especially likely to have come from AI generation. Signs:

- Style mismatch with surrounding code (a hand-rolled block in an ORM-heavy file).
- Over-elaborate naming for simple logic (classic AI signature in some tools).
- Comments that explain what the code does but not why (narration, not intent).
- Duplicate logic across files that looks cut-and-pasted.
- "Nearly-correct" idiom — the right function called with almost-right arguments.

Don't block findings on this signal; it's a prior, not a rule. But AI-specific shape raises confidence of the finding and suggests running a broader sweep for similar patterns.

### Step 4 — Verify each finding before reporting

For each candidate finding:

- **Trace the data flow.** Where does the input come from? Where does it reach? Is there sanitization or protection anywhere in the chain? Pattern-match without trace = no finding.
- **Check for framework-provided protection.** Does the ORM parameterize by default here? Is there middleware that already validates? If the framework protects, the finding is downgraded or removed.
- **Check the test coverage.** Is there a test that exercises this path? If yes and it passes, what's it actually asserting?
- **Confidence signal.** Assign High / Medium / Low per the PROMPT_QUALITY_STANDARDS guidance.

### Step 5 — Prioritize

Per finding, assign:

- **Severity:** Critical / High / Medium / Low / Informational. Critical = reachable from an unauthenticated external entry point with clear impact. High = reachable from authenticated external entry with impact. Medium = requires specific conditions or internal access. Low / Informational = hygiene.
- **Exploitability posture:** Is there a realistic attack path given the deployment (input 3)? Internal-only deployment downgrades some findings.
- **Blast radius:** Per-user / per-tenant / global / cross-tenant.

Output the top findings sorted by severity × exploitability × blast radius.

### Step 6 — Emit the "AI-generated patterns likely to repeat" section

Based on findings, list the patterns that appear repeatedly. This feeds directly into the rules file (`viberescue_rules_file_design.md`) as hard don'ts. Do not reuse these as separate per-instance findings; summarize.

### Step 7 — Suggest remediation per finding

Short: specific file/line change or referral to a framework primitive. Not "use parameterized queries"; "replace `f\"SELECT ... {user_id}\"` on line 42 with the ORM's filter or a parameterized query through `cursor.execute(sql, (user_id,))`."

### Step 8 — Dual-failure-prevention pass

Review the audit for two failure directions:

- **Harmful:** Missed a critical finding. Before delivering, ask: did every entry point get its auth / input-validation / data-isolation checks walked? If not, note the gap.
- **Unhelpful:** Flagged so many low/informational findings that the critical ones drown. Cap critical/high findings at 10 for the report body; move lower-severity to an appendix.

### Step 9 — Verify and output

Run the verification checklist.

---

## Constraints

### Must
- Every finding cites a specific file and line range.
- Every finding includes a traced data flow, framework-check, and confidence.
- Severity assigned per finding with exploitability and blast-radius context.
- Distinguish AI-specific patterns from generic ones; don't require the distinction for a finding to stand.
- Top findings sorted by risk, not by file order.
- Remediation is specific, not generic.

### Must Not
- Issue a finding on keyword match alone (`eval`, `exec`, `pickle`) without tracing reachability.
- Issue "you should review this area" as a finding. Either it's a finding with evidence or it's a scope gap.
- Omit verification when a finding looks obvious — the "obvious" findings are often framework-protected.
- Flood the report with low/informational findings at the expense of highs.
- Omit the "AI-patterns likely to repeat" section — it's the handle for prevention.

---

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Flag ORM `.raw()` calls without checking the arguments; raw SQL with parameterization is fine.
- Flag every `except Exception` as swallowed; check whether the exception is logged AND the happy path does NOT proceed.
- Claim SSRF without tracing that the URL is user-controlled and reaches a fetcher without allow-list.
- Flag an auth check as missing without tracing whether a middleware or decorator provides it upstream.
- Flag logging of "PII" when the logger redacts at a downstream sink. Trace the actual output.

✅ **DO:**
- Trace complete data flows from the entry point to the sensitive operation.
- Distinguish deployment posture (input 3) — an internal-only service has different severity calculus.
- Note when the codebase lacks tests that would catch a class of issue; that's itself a finding (Medium, usually).
- Call out framework primitives the code is reimplementing (hand-rolled auth when the framework has a decorator).
- Acknowledge when you can't reach a conclusion — "potential finding, needs runtime verification" is valid output.

---

## Dual-Failure Prevention (QA-20)

❌ **HARMFUL failure:** Confident finding that's framework-protected; team spends a day "fixing" non-issues while real issues sit. Or missed critical auth hole because it was in a file not reviewed.

❌ **UNHELPFUL failure:** Report is 80 "low / informational" findings and 0 concrete actions; reviewer throws up hands.

✅ **Quality check:** A senior security engineer can point to each Critical / High finding, see the traced data flow, and either confirm it's real or identify what's missing.

---

## Output Format

```markdown
# Security and Resilience Audit — [Repo]

## Summary
- Entry points audited: [list]
- Audit scope: [files / flows]
- Critical: [N] | High: [N] | Medium: [N] | Low: [N] | Informational: [N]

## Findings (sorted by risk)

### Finding 1: [Short title]
- **File / lines:** path/to/file.py:42–58
- **Category:** [from step 2's list]
- **Traced flow:** [entry → sanitization (none) → sensitive op]
- **Framework check:** [protection present / absent, why]
- **Tests:** [coverage present / absent]
- **Severity:** Critical | High | Medium | Low | Informational
- **Exploitability posture:** [internet-facing / internal-auth'd / internal-only]
- **Blast radius:** [per-user / per-tenant / global / cross-tenant]
- **AI-pattern shape:** [yes + why / neutral]
- **Confidence:** High | Medium | Low
- **Remediation:** [specific]

### Finding 2: …

## AI-Generated Patterns Likely to Repeat
- [Pattern + locations]  → rules-file hard don't recommendation
- [...]

## Scope Gaps
- [Areas not reached by this audit, with one-line reason]

## Low / Informational Findings (appendix)
- [Abbreviated list]

## Recommended Next Steps
- [3–6 bullets in remediation-priority order]
```

---

## Verification

- [ ] Every entry point was considered for auth / input-validation / data-isolation.
- [ ] Every finding has file + lines, traced flow, framework check, severity, confidence.
- [ ] No finding rests on keyword match without trace.
- [ ] AI-pattern repeat section present.
- [ ] Scope gaps acknowledged honestly.
- [ ] Low/Informational findings are appendixed, not in the top list.
- [ ] Remediation is specific to the file and the fix.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Produce a findings report with evidence and confidence, not a generic security pitch.
- **ST-02 (Structured Sequential Instructions):** Nine steps drive scope → categories → AI-pattern check → verify → prioritize → pattern-summary → remediate → dual-failure → verify.
- **CM-02 (Constraint Specification):** Must Not block forbids keyword-match findings and low-finding flooding.
- **DS-01 (Framework Application):** Ten AI-specific categories are the framework; the audit is scoped to them plus entry-point flow tracing.
- **RT-07 (Cascade Effect Analysis):** The "AI-generated patterns likely to repeat" section traces the cascade from individual findings to systemic prevention (rules file).
- **RT-11 (Error Recovery):** Scope gaps and honest non-conclusions are first-class outputs rather than silent omissions.
- **QA-01 (Self-Verification):** Verification checklist + confidence labels force per-finding grounding; dual-failure-prevention pass catches under- and over-reporting.
