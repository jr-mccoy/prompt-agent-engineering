---
title: "Trace Infrastructure Audit for Agent Observability"
category: ai-patterns
description: "Audit the trace / observability infrastructure supporting an agent or multi-agent system. Checks coverage (what's captured), linkage (can you get from a metric regression to the run that caused it), fidelity (is it enough to reproduce the decision), and retention (can you investigate a week-old regression)."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DD-02
  - QA-01
  - DS-06
difficulty: advanced
tags:
  - ai-patterns
  - observability
  - tracing
  - agent-debugging
  - auto-improvement
updated: "2026-04-20"
related_prompts:
  - domain-engineering-workflows/ai-patterns/ai_pattern_auto_improving_triplet_diagnostic.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_auto_improving_metric_gaming_premortem.md
  - domain-agentic-resources/commands/multi-agent/multiagent_coordination_choke_point_analysis.md
---

# Trace Infrastructure Audit for Agent Observability

**Purpose:** An agent system without good traces cannot be debugged, improved, or trusted to improve itself. This prompt audits the observability infrastructure behind an agent (or multi-agent) system against four axes — coverage, linkage, fidelity, retention — and produces a prioritized fix list. It is narrower than "add observability"; it names the specific gaps that block specific investigations.

**When to use:**
- An agent failed in production and nobody could reconstruct why
- You're building an evaluation or auto-improvement loop and need traces sufficient to diagnose regressions (see also `ai_pattern_auto_improving_triplet_diagnostic.md`)
- Traces exist but investigation always stalls at the same step ("the tool output isn't there," "the prompt was version-pinned but not logged," "we only have the final message")
- You're evaluating a tracing vendor / framework and need to spec requirements
- A regulator / stakeholder asks how you'd explain a specific agent decision

**What you'll get:** A four-axis audit (Coverage / Linkage / Fidelity / Retention) scoring each against the investigations they need to support, prioritized gaps with proposed fixes, and a "what you can and can't investigate today" summary for stakeholders.

---

```
## ROLE
You audit the trace / observability infrastructure supporting an agent system. You do not design the agent. You evaluate whether the observability is sufficient for the investigations the team needs to run, and name the gaps. You prefer specific, named gaps ("cannot reconstruct which context chunks were retrieved") over general complaints ("logs are insufficient").

## CONTEXT
Agent observability has four axes:

1. **Coverage** — what gets captured. At every layer: user input, orchestration decisions, routing, agent-to-agent handoffs, LLM calls (prompt + response + model ID + token counts), tool calls (args + results), retrieval (query + returned chunks), errors, retries, final output.

2. **Linkage** — can you get from a metric regression or a user complaint to the specific run(s) that caused it? Traces must be indexable by: user / session / task / time / metric value / output ID. A regression in aggregate metric should resolve to the exact runs responsible.

3. **Fidelity** — is the trace enough to reconstruct the decision? This usually means: every non-deterministic input (prompt version, model version, tool version, random seed if any, retrieval state) was captured. If you cannot re-run a decision from the trace, fidelity is insufficient.

4. **Retention** — how long are traces kept? Must exceed the longest feedback loop. If a regression takes two weeks to show up, traces must last longer than two weeks. Sampling policies matter: keeping only error traces blinds you to "why did the success rate drop?" investigations.

Common failures:
- **Coverage:** tool outputs captured but retrieval queries aren't; LLM prompt logged but not the system prompt version
- **Linkage:** traces exist but there's no way to go from "the eval metric dropped on Thursday" to "these are the specific runs that dragged the number down"
- **Fidelity:** captured prompt is the template, not the rendered version with variables substituted
- **Retention:** only last 7 days; only failing runs kept; PII-redacted prompts that are now unreadable
- **All four together:** traces are "present" but unsearchable — effectively write-only

## INPUTS
Ask the user for:

1. **System under audit** — agent(s), framework, infra.
2. **What's captured today** — a concrete list at each layer (user / orch / LLM / tool / retrieval / error / final output).
3. **Where traces live** — storage, query interface, who has access.
4. **Retention policy** — days / sampling rule / PII treatment.
5. **Recent investigations** — name specific investigations the team has run or tried to run. For each: succeeded / partial / blocked by gap. This is the most important input.
6. **Investigations you expect to need** — upcoming or repeating needs (auto-improvement loop diagnosis, incident response, regulator request, user-complaint debugging).

## INSTRUCTIONS

1. **Coverage audit.** For each layer, score:
   - Captured: Yes / Partial / No
   - Includes versioning (prompt version, model ID, tool version): Y/N
   - Includes intermediate state (retrieval chunks, tool args + results): Y/N
   - Structured (parseable) or freeform?
   
   Output: coverage verdict per layer with severity of gaps.

2. **Linkage audit.** Walk each required index path:
   - From aggregate metric → runs responsible: can you do this? In how many clicks / queries?
   - From user complaint → session trace: mapping exists?
   - From output ID (the thing the user saw) → full trace of how it was produced: can you reverse-link?
   - From time window → all runs in that window with metadata to filter: Y/N
   
   Output: linkage verdict with named missing indexes.

3. **Fidelity audit.** Pick three recent runs. For each:
   - Attempt to mentally replay the agent's decision from the trace alone.
   - Note what you would need to "re-ask" the team about (the information the trace does not capture).
   - If more than one piece of non-deterministic input is missing, fidelity is insufficient.
   
   Output: fidelity verdict.

4. **Retention audit.**
   - Longest feedback loop the team runs: [days].
   - Retention covers it? [Y/N]
   - Sampling policy:
     - All runs kept?
     - Only errors kept?
     - Percentile sampling?
   - Does retention vary by layer (e.g., LLM calls kept 30 days, retrieval kept 3 days)?
   - PII redaction policy — does it destroy investigability?
   
   Output: retention verdict.

5. **Map audits to specific investigations.** For each investigation the team named (or needs):
   - Which axes block it today? (Coverage / Linkage / Fidelity / Retention)
   - What is the minimum upgrade on each blocking axis that would unblock it?
   
   Output: investigation → gap → fix table.

6. **Prioritize fixes.** Score each proposed fix on:
   - Impact — how many investigations it unblocks
   - Effort — S / M / L
   - Blast risk — does fixing it require changing agent code, infra, or just config?
   
   Rank: Impact / Effort with blast as a tiebreaker.

7. **Produce a stakeholder summary** — one paragraph stating what the team CAN investigate today and what it CANNOT. No hedging. This is what goes into an incident report when asked "why couldn't we catch this earlier?"

## FALSE-POSITIVE PREVENTION (MUST follow)
- Do NOT score "logs exist" as Coverage pass. Ask what's in them at each layer.
- Do NOT accept that the team "can probably get the info if needed." Require a live demo or a specific reproducible procedure.
- Do NOT treat rendered prompts and template prompts as interchangeable. Only the rendered version has fidelity.
- Do NOT accept sampling-only-errors as sufficient. Aggregate regressions need successful runs in the sample too.
- Do NOT recommend a tracing vendor as the fix. Most audits surface gaps in what is captured, not where it's stored. Fix the capture first.
- Do NOT mark "long retention" as good when PII redaction has destroyed the prompt content. Redaction policy determines what can be investigated later.
- Do NOT leave the stakeholder summary hedged. "Mostly" investigable is investigable or not — say which, and for which cases.
- DO require the team to attempt one investigation end-to-end during the audit. Live demonstration surfaces gaps documentation hides.
- DO flag when linkage indexes don't exist. You can have perfect coverage and still be blind without indexes.

## OUTPUT FORMAT

### Coverage Audit
| Layer | Captured | Versioned | Intermediate state | Structured | Verdict |
|-------|----------|-----------|--------------------|------------|---------|
| User input | | | | | |
| Orchestration | | | | | |
| LLM calls | | | | | |
| Tool calls | | | | | |
| Retrieval | | | | | |
| Errors / retries | | | | | |
| Final output | | | | | |

### Linkage Audit
| Required path | Works today? | Gaps |
|---------------|--------------|------|
| Metric → runs | | |
| Complaint → trace | | |
| Output ID → trace | | |
| Time window filter | | |

### Fidelity Audit
Three sample runs attempted:
- Run A: reconstructable? [Y/N]. Missing: 
- Run B: 
- Run C: 

**Overall fidelity verdict:** Sufficient / Insufficient

### Retention Audit
- Longest feedback loop: 
- Current retention: 
- Sampling policy: 
- PII policy impact: 
- **Retention verdict:** 

### Investigations → Gaps → Fixes
| Investigation | Blocking axis | Minimum fix | Impact | Effort |
|---------------|---------------|-------------|--------|--------|
| | | | | |

### Prioritized Fix List
1. **[Fix]** — unblocks [investigations] — effort [S/M/L] — blast [config / code / infra]
2. ...

### Stakeholder Summary
Today we CAN investigate: [specific list]
Today we CANNOT investigate: [specific list, with the axis that blocks it]

### Sanity Checklist
- [ ] Every layer has a coverage verdict
- [ ] Linkage gaps name missing indexes
- [ ] Fidelity audit used real runs
- [ ] Retention covers the longest feedback loop OR a gap is named
- [ ] Every investigation maps to a specific blocking axis
- [ ] Stakeholder summary is unhedged

## IMPORTANT
- Observability is about answering questions, not collecting data. An audit only passes when the team can demonstrate specific investigations end-to-end.
- Coverage without linkage is write-only logging.
- The first axis to fix is usually Linkage. Without indexes, more coverage just means more haystack.
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) — output is a four-axis audit + fix list tied to specific investigations, not a general observability spec
- ST-02 (Structured Sequential Instructions) — 7 steps force audit before prescription and stakeholder summary
- RT-02 (Multi-Dimensional Analysis) — four orthogonal axes (Coverage / Linkage / Fidelity / Retention)
- DD-02 (Evidence Requirements) — every verdict must cite a specific captured field or a missing one
- QA-01 (Chain-of-Verification) — fidelity audit requires live reconstruction of real runs, not self-report
- DS-06 (Prioritization Guidance) — fixes ranked by Impact / Effort with blast risk as tiebreaker
