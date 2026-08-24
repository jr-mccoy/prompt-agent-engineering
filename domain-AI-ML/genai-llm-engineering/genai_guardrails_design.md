---
title: "LLM Guardrails Design"
category: AI-ML/genai-llm-engineering
description: "Design layered input/output guardrails for an LLM application — safety, PII, jailbreak, topical scope, and grounding — with explicit failure actions, measurable thresholds, and an evaluation set, without over-blocking legitimate use."
techniques:
  - ST-02
  - CM-02
  - DS-02
  - QA-12
  - DS-06
difficulty: advanced
tags:
  - guardrails
  - safety
  - pii
  - jailbreak
  - grounding
  - llm-security
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/genai-llm-engineering/genai_prompt_injection_defense.md
  - domain-software-engineering/analysis/security/security_llm_application_review.md
  - domain-AI-ML/genai-llm-engineering/genai_llm_observability_tracing.md
---

# LLM Guardrails Design

**Objective:** Design a layered guardrail system for an LLM application — input guards (PII, jailbreak, off-topic, injection) and output guards (safety, PII leakage, groundedness, format/policy) — each with an explicit detection method, failure action, and measurable threshold, evaluated on a labeled set so the guards catch real harms without strangling legitimate traffic.

**When to Use:**
- Putting an LLM feature in front of users and needing to bound what goes in and comes out.
- A compliance/safety review requires demonstrable input/output controls.
- An existing app over-blocks (false refusals) or under-blocks (leaks/unsafe output) and needs redesign.

**When NOT to Use:**
- The threat is specifically prompt injection / data exfiltration (use `genai_prompt_injection_defense.md`).
- You need a full application security review (use `domain-software-engineering/analysis/security/security_llm_application_review.md`).

## Inputs / Context

State the model + provider + version (some providers ship built-in safety filters; know what you're layering on). Provide what you can:
- **Application** — what it does, who uses it, what data it touches.
- **Risk surface** — what bad inputs/outputs would cause real harm (PII leak, unsafe advice, off-brand content, ungrounded claims).
- **Policy** — content policy, regulatory constraints, allowed/forbidden topics.
- **Constraints** — latency budget for guard checks, tolerance for false refusals vs missed harms.
- **Existing controls** — provider safety filters, auth, rate limits already in place.

## Constraints

**Must:**
- Place guards on both input and output; specify detection method and failure action (block, redact, regenerate, escalate) for each.
- Set measurable thresholds and evaluate each guard on a labeled set with both harmful and legitimate cases (false-positive vs false-negative tradeoff stated).
- Define the user-visible behavior on a block (clear refusal vs silent drop) and the logging/alerting path.

**Must Not:**
- Rely on a single prompt-level instruction ("don't say anything harmful") as the guardrail — guards must be enforced outside the model's discretion where stakes are real.
- Over-block by setting detectors so aggressive that legitimate use is refused, without measuring the false-refusal rate.
- Fabricate detector accuracy; require evaluation on the user's labeled set.

**Instructions:**

1. **Enumerate the risk surface.** List the concrete harms for this app (PII exposure, unsafe/illegal advice, off-topic/off-brand output, ungrounded claims, jailbreak compliance) and rank by severity × likelihood.

2. **Design input guards.** For each input risk: detection (classifier, regex/PII detector, allow/deny topic, injection scan — cross-link `genai_prompt_injection_defense.md`), the failure action, and the threshold. Specify how user input is delimited from system instructions.

3. **Design output guards.** For each output risk: safety/toxicity check, PII leakage scan, grounding/faithfulness check (does output stick to provided context?), policy/format validation. Specify regenerate-vs-block-vs-redact per guard.

4. **Define failure actions and UX.** State exactly what happens on each trip: refuse with a clear message, redact and continue, regenerate with a stricter prompt, or escalate to human. Avoid silent failures that confuse users.

5. **Set thresholds via the FP/FN tradeoff.** For each guard, choose a threshold based on the cost of a false refusal vs a missed harm, and state the chosen operating point explicitly.

6. **Build the evaluation set.** Assemble labeled harmful cases (per risk), benign-but-tricky cases (to measure over-blocking), and adversarial variants. Measure each guard's precision/recall and the end-to-end false-refusal rate.

7. **Wire in logging and monitoring.** Log every guard trip with reason, sample blocked traffic for review, alert on spikes, and feed confirmed misses/false-refusals back into the eval set. Cross-link `genai_llm_observability_tracing.md`.

8. **Plan defense in depth.** Note that no single guard is sufficient; specify the layering and what the system does if a guard service is unavailable (fail-closed vs fail-open per risk).

**Output Format:**

A markdown guardrails spec:
- **Risk Surface** — ranked harms (severity × likelihood)
- **Input Guards** — table: Risk | Detection | Threshold | Failure action
- **Output Guards** — table: Risk | Detection | Threshold | Failure action
- **Failure UX** — user-visible behavior per trip + fail-open/closed policy
- **Evaluation Plan** — labeled set composition + per-guard precision/recall + false-refusal rate
- **Monitoring** — logging, sampling, alerting, feedback loop

## Verification

- [ ] Guards exist on both input and output, each with detection + threshold + failure action.
- [ ] Thresholds are justified by an explicit false-refusal vs missed-harm tradeoff.
- [ ] Each guard has an evaluation plan with harmful AND benign-but-tricky cases.
- [ ] User-visible failure behavior and fail-open/closed policy are specified per risk.
- [ ] High-stakes guards are enforced outside the model's discretion, not by a prompt instruction alone.
- [ ] No detector accuracy is claimed without evaluation on the user's labeled set.

## False-Positive Prevention

❌ **DON'T:**
- Treat "I added a system-prompt rule" as a guardrail for high-stakes harms — the model can be talked out of it.
- Tune detectors only on harmful cases; without benign cases you can't see the false-refusal damage.
- Block silently — users who don't know why they were refused route around the system or churn.
- Assume provider safety filters cover your app-specific risks (PII schema, off-brand topics, grounding).

✅ **DO:**
- Enforce critical guards in code/services outside the model, and layer defense in depth.
- Measure both missed harms and false refusals on a labeled set, and pick the operating point deliberately.
- Give clear refusal messages and log every trip for review and feedback.
- Add app-specific guards (PII formats, topical scope, grounding) on top of any provider filters.

## Example Output

```markdown
## Guardrails: Customer Self-Service Assistant (model: <provider/model vX>)

### Risk Surface (ranked)
1. PII leakage in output (high sev x med likelihood)  2. Unsafe financial advice (high x low)
3. Off-topic/off-brand content (med x high)  4. Jailbreak -> policy bypass (high x med)

### Input Guards
| Risk | Detection | Threshold | Action |
|---|---|---|---|
| Injection | injection scanner (see genai_prompt_injection_defense) | flagged | strip + log |
| Off-topic | topic classifier | conf < 0.6 in-scope | refuse + clarify |
| PII in prompt | PII detector | any match | redact before storage |

### Output Guards
| Risk | Detection | Threshold | Action |
|---|---|---|---|
| PII leakage | PII scan on output | any match | redact + alert |
| Unsafe advice | safety classifier | score > T | block + canned referral |
| Ungrounded claim | faithfulness check vs context | unsupported | regenerate; if repeat, abstain |

### Failure UX
Blocks return a clear reason + next step. Output guards fail-closed (block on guard outage)
for PII/safety; topic guard fails-open (allow) to avoid over-refusal.

### Evaluation Plan
500 labeled inputs (200 benign-tricky, 200 harmful, 100 adversarial). Per-guard precision/recall;
end-to-end false-refusal rate target < 3% on benign-tricky.

### Monitoring
Log all trips with reason; sample 2% for review; alert on >2x trip-rate spike; weekly
false-refusal review feeds eval set.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** risk surface → input guards → output guards → eval → monitoring.
- **CM-02 (Constraint Specification):** each guard is a bounded constraint with a defined failure action.
- **DS-02 (Metric Specification):** thresholds and per-guard precision/recall make guards measurable.
- **QA-12 (False Positives Identification):** the false-refusal vs missed-harm tradeoff is central.
- **DS-06 (Prioritization & Severity Guidance):** risks ranked by severity × likelihood drive effort.

**Related Prompts:**
- `genai_prompt_injection_defense.md` — the deep dive on the injection guard referenced here.
- `domain-software-engineering/analysis/security/security_llm_application_review.md` — the full security review this complements.
- `genai_llm_observability_tracing.md` — wire guard trips into observability.
