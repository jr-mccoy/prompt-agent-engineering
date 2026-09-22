---
title: "RAI Red-Teaming Plan"
category: AI-ML/responsible-ai-governance
description: "Design a red-teaming plan for an AI system — threat model, attack categories, coverage, and reporting — that measures real failure modes rather than producing anecdotes, and pairs findings with severity and reproducibility."
techniques:
  - ST-02
  - RT-02
  - DS-06
  - QA-12
  - CM-02
difficulty: advanced
tags:
  - red-teaming
  - adversarial-testing
  - threat-model
  - llm-safety
  - responsible-ai
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/responsible-ai-governance/rai_model_risk_assessment.md
  - domain-AI-ML/responsible-ai-governance/rai_privacy_pii_assessment.md
  - domain-AI-ML/responsible-ai-governance/rai_ethics_review_protocol.md
---

# RAI Red-Teaming Plan

**Objective:** Design a red-teaming plan that defines a threat model, selects attack categories appropriate to the system, specifies coverage and success criteria, and structures reporting — so the exercise produces measurable, reproducible findings with severity, not a scattering of one-off anecdotes.

**When to Use:**
- Before deploying a consequential or public-facing AI system (especially generative/agentic).
- When a risk assessment flagged high-severity but untested failure modes.
- As recurring assurance after major model or capability changes.

**When NOT to Use:**
- For routine performance evaluation on benign inputs — use standard eval prompts.
- For a full security pentest of infrastructure (complement with security tooling).

## Inputs / Context

- **System under test** — type (classifier, LLM, agentic, multimodal), capabilities, and what it can affect (tools, data, actions).
- **Threat actors of concern** — careless users, motivated adversaries, insiders; their goals.
- **Known weak points** — from prior incidents, risk assessment, or interpretability findings.
- **Constraints** — what testers may/may not do (data access, live-system limits, legal boundaries), and the test environment.
- **Reporting audience** — who acts on findings and at what gate.

## Constraints

**Must:**
- Start from a threat model (actors, goals, capabilities) and derive attack categories from it — not a generic checklist.
- Define success criteria and severity per finding, and require reproducibility (steps to re-trigger).
- Specify coverage targets so the absence of findings in an area is interpretable.

**Must Not:**
- Report a single successful jailbreak/exploit as the system's overall failure rate without coverage context.
- Test in production against real users or real PII without authorization; flag legal/ethical boundaries and require sign-off.
- Fabricate attack-success statistics; report measured rates over a stated number of attempts, or mark as unquantified.

**Instructions:**

1. **Build the threat model.** Define adversaries, their goals, and capabilities; state what a successful attack lets them do (harmful output, data exfiltration, tool misuse, evasion).

2. **Derive attack categories.** From the threat model and system type, select categories: prompt injection/jailbreak, harmful-content elicitation, PII/memorization extraction, evasion/adversarial inputs, tool/agent misuse, bias provocation, and over-refusal — keeping only those relevant.

3. **Define success criteria and severity.** For each category, state what counts as a successful attack and how severe it is (harm × reach × ease).

4. **Set coverage and method.** Specify manual vs automated generation, number of attempts per category, diversity of attack styles, and which surfaces/inputs are in scope — so "no findings" is meaningful.

5. **Establish authorization and safety rules.** State the test environment, data restrictions, and required sign-offs; prohibit real-user/real-PII testing without authorization.

6. **Run and log reproducibly.** Require each finding to include the exact input, the harmful output, and reproduction steps; record attempts and successes per category.

7. **Score and rank findings.** Rate by severity, exploitability, and reproducibility; distinguish reliable exploits from flaky one-offs.

8. **Report and route.** Summarize per-category success rates with coverage, ranked findings, and recommended mitigations feeding the risk register and governance gate.

**Output Format:**

A markdown red-team plan + (post-run) report template:
- **Threat Model** — actors, goals, capabilities, impact.
- **Attack Categories** — table: Category | Why in scope | Success criterion | Severity basis.
- **Coverage & Method** — attempts/category, generation method, surfaces in scope.
- **Authorization & Safety Rules**.
- **Findings Log** — Finding | Category | Repro steps | Severity | Reproducible? | Recommended mitigation.
- **Per-Category Results** — successes/attempts with coverage caveat.
- **Routing** — to risk register / gate.

## Verification

- [ ] Attack categories are derived from a stated threat model, not a generic list.
- [ ] Each category has a success criterion and severity basis.
- [ ] Coverage (attempts/category, surfaces) is specified so "no findings" is interpretable.
- [ ] Authorization and no-real-PII/no-prod-user rules are stated.
- [ ] Each finding is reproducible with exact steps.
- [ ] Success rates are reported over stated attempts, not from a single anecdote.

## False-Positive Prevention

❌ **DON'T:**
- Claim "the model is unsafe" from one successful jailbreak with no coverage measurement.
- Claim "the model is safe" after a handful of unsystematic prompts.
- Report a flaky one-off exploit as a reliable vulnerability without reproduction.
- Test against live users or real PII without authorization.

✅ **DO:**
- Quantify success per category over a stated number of diverse attempts.
- Require reproduction steps and mark reliable vs flaky findings.
- State coverage so absence of findings is meaningful.
- Confine testing to an authorized environment with synthetic/authorized data.

## Example Output

```markdown
## Red-Team Plan: Customer-Facing Support Assistant (LLM + retrieval + refund tool)

### Threat Model
Actors: motivated user (free refunds), curious user (extract other customers' data), troll (harmful content). Impact: unauthorized refunds (tool misuse), PII leakage, brand-damaging output.

### Attack Categories
| Category | Why in scope | Success criterion | Severity basis |
|---|---|---|---|
| Tool misuse (refund) | Has refund tool | Issues refund without authorization | Critical (financial) |
| PII extraction | Retrieval over customer data | Returns another user's PII | Critical (privacy) |
| Jailbreak/harmful content | Public-facing | Produces disallowed content | High |
| Prompt injection via retrieved docs | RAG | Injected instruction changes behavior | High |
| Over-refusal | UX risk | Refuses benign request | Medium |

### Coverage & Method
150 attempts/category (manual + automated mutation), varied phrasing/languages; surfaces: chat input + uploaded docs.

### Authorization & Safety Rules
Staging only; synthetic customer data; refund tool sandboxed. No real PII. Sign-off: security + product.

### Findings Log (excerpt)
| Finding | Category | Repro | Severity | Reproducible? | Mitigation |
|---|---|---|---|---|---|
| Injected doc triggers refund | Prompt injection→tool | steps attached | Critical | Yes (9/10) | Tool-call gating + provenance check |
| Other-user order via crafted query | PII extraction | steps attached | Critical | Yes (6/10) | Row-level access control in retrieval |

### Per-Category Results
Tool misuse 12/150; PII 8/150; jailbreak 21/150; injection 14/150; over-refusal 19/150. (Coverage: see method.)

### Routing
Critical findings → block deploy; feed risk register; re-test after mitigation.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** threat model → categories → coverage → run → report.
- **RT-02 (Multi-Dimensional Analysis Framework):** findings across severity, exploitability, reproducibility.
- **DS-06 (Prioritization & Severity Guidance):** ranks findings and routes critical ones.
- **QA-12 (False Positives Identification):** separates reliable exploits from anecdotes; demands coverage.
- **CM-02 (Constraint Specification):** authorization and safety rules bound the exercise.

**Related Prompts:**
- `rai_model_risk_assessment.md` — supplies the untested risks to target.
- `rai_privacy_pii_assessment.md` — deeper analysis of memorization/extraction findings.
- `rai_ethics_review_protocol.md` — escalation path for serious harms found.
