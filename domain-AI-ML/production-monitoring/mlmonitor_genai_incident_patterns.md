---
title: "GenAI/LLM Incident Patterns & Runbooks"
category: AI-ML/production-monitoring
description: "A catalog of GenAI/LLM-specific production incident patterns with detection + response runbooks — hallucination/factuality spike, prompt-injection/jailbreak, RAG retrieval failure, output-safety violation, latency/timeout, and cost/token runaway — each with signals, immediate containment, diagnosis, and durable fix."
techniques:
  - ST-02
  - RT-10
  - DS-06
  - RT-09
  - QA-12
difficulty: advanced
tags:
  - genai
  - llm
  - hallucination
  - prompt-injection
  - rag-failure
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/production-monitoring/mlmonitor_incident_runbook_library.md
  - domain-AI-ML/agentic-ai-systems/aiagent_prompt_injection_untrusted_content_defense.md
  - domain-AI-ML/genai-llm-engineering/genai_llm_evaluation_design.md
---

# GenAI/LLM Incident Patterns & Runbooks

**Objective:** Produce a catalog of GenAI/LLM-specific production incident patterns — hallucination/factuality spikes, prompt-injection/jailbreak, RAG retrieval failure (stale/empty/wrong-doc), output-safety violations, latency/timeout, and cost/token runaway — each with detection signals, immediate containment, ML-aware diagnosis, and a durable fix, so an LLM-app responder can recognize and resolve failure modes that classic ML monitoring (accuracy/drift on a fixed label) does not surface.

**When to Use:**
- Running an LLM-backed product (chat, RAG, copilot, agent) and you need incident coverage for generative failure modes.
- After an LLM incident (a confidently wrong answer, a jailbreak, a cost spike) revealed missing playbooks.
- When standard ML runbooks don't fit because there is no ground-truth label per response.

**When NOT to Use:**
- For classic supervised-ML failure classes (drift, skew, pipeline) — use `mlmonitor_incident_runbook_library.md`.
- To design the prompt-injection defense itself — use `aiagent_prompt_injection_untrusted_content_defense.md`.
- To build the offline LLM evaluation/judge harness — use `genai_llm_evaluation_design.md`.

## Inputs / Context

- **Application shape** — chat / RAG / tool-using agent; user-facing vs internal; trust boundary (untrusted user input? untrusted retrieved/tool content?).
- **Signals available** — output-quality/judge scores, refusal/safety-filter rates, retrieval hit-rate and freshness, latency/token/cost telemetry, user reports/thumbs.
- **Guardrails in place** — input/output filters, grounding/citation checks, injection defenses, rate/cost limits.
- **Containment levers** — disable tool/feature, swap to safer prompt/model, tighten filter, cap tokens, kill switch.
- **Escalation map** — on-call, safety/trust owner, retrieval/data owner, cost owner.

## Constraints

**Must:**
- Treat each pattern as distinct with its own detection signals, containment, diagnosis, and durable fix.
- For factuality/hallucination, distinguish a model-generation failure from a RAG retrieval failure (the fix differs entirely).
- For prompt-injection/jailbreak, treat retrieved/tool content as untrusted, not just the user turn.
- Separate immediate containment (stop harm now) from durable fix (prevent recurrence).

**Must Not:**
- Invent incident events, judge scores, root causes, or cost/token figures; reconstruct from logs/telemetry and mark gaps "unknown / needs investigation."
- Attribute every wrong answer to "the model hallucinated" without checking retrieval, prompt, and context-window truncation first (single-root-cause oversimplification).
- Apply hindsight bias in diagnosis — judge guardrail decisions by what was detectable at the time.

**Instructions:**

1. **Enumerate the GenAI patterns.** Hallucination/factuality spike; prompt-injection/jailbreak; RAG retrieval failure (stale/empty/wrong-doc); output-safety violation; latency/timeout; cost/token runaway.

2. **Define detection signals per pattern.** Judge/factuality scores, citation-grounding rate, retrieval hit-rate and doc freshness, safety-filter trips, refusal-rate anomalies, p95 latency, tokens-per-request and spend, and user-report clustering.

3. **Specify immediate containment.** The fastest harm-reduction lever for each: disable the affected tool/feature, swap to a safer prompt/model, tighten the output filter, force grounding-or-refuse, cap tokens, throttle.

4. **Add ML-aware diagnosis.** For factuality: was the right document retrieved? was context truncated? is the prompt at fault, or generation? For injection: did untrusted content reach an instruction position? For cost runaway: a loop, a long-context blowup, or a retry storm?

5. **Define the durable fix.** Grounding/citation enforcement, retrieval freshness/index repair, injection isolation (untrusted-content sandboxing), output-safety rules, latency/token budgets and circuit breakers — pointing to the dedicated defense/eval prompts for design depth.

6. **Set escalation and severity.** Safety/trust owner for safety + injection; retrieval/data owner for RAG; cost owner for spend; severity by harm (safety > factual harm > cost).

7. **Index the patterns.** Symptom → pattern routing with disambiguation (a "wrong answer" could be hallucination OR retrieval failure OR truncation).

**Output Format:**

A markdown catalog:
- **Routing Index** — Symptom → candidate pattern(s) → disambiguation
- **Per-Pattern entries**, each: Pattern | Detection signals | Immediate containment | Diagnosis decision points | Durable fix | Escalation/severity
- **Cross-links** — to injection-defense and LLM-eval prompts for durable design

## Verification

- [ ] Each GenAI pattern is a distinct runbook with all four parts.
- [ ] Hallucination diagnosis checks retrieval and context truncation before blaming generation.
- [ ] Injection runbook treats retrieved/tool content as untrusted, not only user input.
- [ ] Immediate containment is separated from durable fix.
- [ ] Cost/latency patterns include budgets, circuit breakers, and loop detection.
- [ ] No invented judge scores or cost figures; gaps marked "unknown / needs investigation."

## False-Positive Prevention

❌ **DON'T:**
- Label every wrong answer "hallucination" when the retriever returned the wrong/stale doc or the context was truncated.
- Defend only the user turn against injection while a poisoned retrieved document carries the payload.
- Treat a cost spike as "more traffic" when it is an agent retry loop or runaway long-context calls.
- Close a safety-violation incident by deleting the bad output without fixing the filter gap.

✅ **DO:**
- Trace a factuality incident through retrieval → context → prompt → generation before assigning cause.
- Sandbox and de-instruct all untrusted content (user, retrieved, tool) per the injection-defense prompt.
- Diagnose cost runaway by token/loop telemetry and add a circuit breaker.
- Pair containment (filter/disable) with a durable fix and a detector so it recurs visibly, not silently.

## Example Output

```markdown
## GenAI Incident Patterns — Support RAG Assistant

### Routing Index
| Symptom | Candidate pattern(s) | Disambiguation |
|---|---|---|
| Confidently wrong answer | Hallucination, RAG-failure, truncation | Check retrieval hit + doc freshness + context length first |
| Assistant ignored its rules | Prompt-injection/jailbreak | Did untrusted user/retrieved content reach instruction position? |
| Spend doubled overnight | Cost/token runaway | Tokens/request, retry rate, context length |

### P1 — Hallucination / Factuality Spike
- **Detection:** judge factuality score drop; citation-grounding rate falls; user "that's wrong" cluster.
- **Containment:** force grounding-or-refuse; show citations; route low-grounding answers to fallback.
- **Diagnosis:** retrieval hit-rate normal? doc freshness ok? context truncated? → if retrieval healthy and context intact, generation fault.
- **Durable fix:** enforce cite-or-abstain; tune judge in `genai_llm_evaluation_design.md`.
- **Escalation/severity:** SEV-2 (factual harm), trust owner.

### P2 — Prompt-Injection / Jailbreak
- **Detection:** safety-filter trips; out-of-policy outputs; anomalous instruction-like spans in retrieved docs.
- **Containment:** disable affected tool; tighten output filter; quarantine suspect documents.
- **Diagnosis:** trace whether untrusted content reached an instruction position (user turn AND retrieved docs).
- **Durable fix:** untrusted-content isolation per `aiagent_prompt_injection_untrusted_content_defense.md`.
- **Escalation/severity:** SEV-1 if data exfil/safety, safety owner.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** every pattern follows detect → contain → diagnose → fix.
- **RT-10 (Troubleshooting Decision Tree):** routing index and per-pattern decision points.
- **DS-06 (Prioritization & Severity Guidance):** severity by harm class drives escalation.
- **RT-09 (Root Cause Explanation):** diagnosis resolves to the true generative/retrieval mechanism.
- **QA-12 (False Positives Identification):** blocks "blame the model" oversimplification and user-only injection defense.

**Related Prompts:**
- `mlmonitor_incident_runbook_library.md` — the classic-ML failure-class library this GenAI catalog complements.
- `aiagent_prompt_injection_untrusted_content_defense.md` — the durable injection defense the runbook points to.
- `genai_llm_evaluation_design.md` — the offline judge/eval harness behind factuality detection.
