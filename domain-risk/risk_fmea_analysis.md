---
title: "FMEA Analysis — Failure Modes and Effects for Non-Manufacturing Contexts"
category: risk/fmea
description: "Run a Failure Mode and Effects Analysis on a process or product. For each step or component, identify failure modes and rate severity, occurrence, and detectability (each 1–10), compute the Risk Priority Number (RPN = S × O × D), trace root cause, and recommend actions. Adapts the standard FMEA template for software systems, organizational processes, supply chains, and event operations, with detectability treated as a first-class lever, not an afterthought."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - DS-02
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - risk-management
  - fmea
  - failure-modes
  - rpn
  - process-analysis
updated: "2026-05-10"
reasoning:
  styles: [systems, causal, structural, probabilistic]
  stakes: variable
  horizon: weeks
  uncertainty: risk
  evidence_quality: moderate
  domain_complexity: cross_domain
  collaboration: small_team
  output_format: matrix_ranked_list
  user_role: [engineer, operator, pm, analyst, quality]
  mode: [audit, diagnose, plan]
related_prompts:
  - domain-risk/risk_register_builder.md
  - domain-risk/risk_dependency_chain_audit.md
  - domain-reasoning-craft/systems/systems_unintended_consequence_scan.md
---

# FMEA Analysis

**Objective:** Run a Failure Mode and Effects Analysis on a process or product. Decompose it into steps or components; for each, identify the ways it can fail (failure modes), the effect of each failure, and rate **severity (S, 1–10)**, **occurrence (O, 1–10)**, and **detectability (D, 1–10)**. Compute the **Risk Priority Number (RPN = S × O × D)**, trace the root cause of each high-RPN mode, and recommend actions that attack the right lever (severity, occurrence, or detectability). The template is the standard automotive/aerospace FMEA adapted so it works for software systems, organizational processes, supply chains, and event operations — domains where "occurrence" and "detection" mean process reliability and observability, not part defect rates.

**When to use:**
- A multi-step process or multi-component product needs systematic failure analysis before it goes live or scales.
- A recurring failure keeps surprising the team and you want to find where detection is weak.
- Designing a new operation (an event, a deployment pipeline, an onboarding flow) and you want failure-resistance built in.
- Prioritizing reliability work by impact rather than by whoever shouts loudest.

**When NOT to use:**
- You want a portfolio-level register of project risks with owners and review cadence — use `risk_register_builder.md`.
- You want to map single points of failure across dependencies — use `risk_dependency_chain_audit.md`.
- The system has no decomposable steps/components — FMEA needs a structure to walk.
- You're chasing unknown black-swan risks — use `risk_tail_risk_scan.md`.

**Audience:** Engineers, operators, quality and reliability owners, PMs, and analysts who own a process or product with discrete steps or components and need a defensible reliability prioritization.

---

## Inputs / Context

1. **The process or product.** What's being analyzed, and its purpose. One paragraph.
2. **Steps or components.** The decomposition: the ordered steps of the process, or the components of the product. If absent, the first task is to build it.
3. **Domain.** Software / organizational process / supply chain / event operation / other — this calibrates what S, O, D mean.
4. **Existing controls.** Current checks, monitors, reviews, or safeguards. These drive the detectability rating.
5. **What "severe" means here.** The worst realistic effect — customer harm, data loss, regulatory breach, event failure, revenue loss. Anchors the severity scale.

---

## Constraints

### Must
- Decompose the target into **steps (process) or components (product)** before analyzing. Walk every one.
- For each step/component, enumerate its **failure modes** (the specific ways it fails) and, for each, the **effect** (what the failure causes downstream).
- Rate each failure mode on three **1–10** scales using the anchors below:
  - **Severity (S):** how bad the effect is.
  - **Occurrence (O):** how often the failure mode is expected to happen.
  - **Detectability (D):** how *hard* it is to detect before the effect lands (1 = caught reliably, 10 = invisible until it's too late). Note the inversion: high D is bad.
- Compute **RPN = S × O × D** for each failure mode.
- For each high-RPN mode, identify the **root cause** (why the mode occurs), not just the mode itself.
- Recommend **actions** that target the specific weak lever: reduce severity (design-out, contain), reduce occurrence (prevent), or reduce detectability D (add detection). Detection-only fixes don't lower severity — say which lever each action moves.
- Produce a **ranked action list by RPN**, with a recomputed target RPN after the recommended action.

### Must Not
- Skip detectability or fold it into occurrence. A frequent-but-instantly-caught failure is very different from a rare-but-invisible one; D is what separates them.
- Stop at the failure mode without naming its effect and its root cause.
- Recommend "add monitoring" as a universal fix — monitoring lowers D, not S or O. Match the action to the lever.
- Use RPN as the only filter; a severity-9 or -10 mode warrants action even at modest RPN. Flag high-severity modes regardless of RPN.
- Rate by gut without the anchored scales; FMEA scores must be comparable across modes.

---

## Instructions

### Step 1 — Build or confirm the decomposition
List the ordered process steps or the product components. Each becomes a row group. If the user hasn't supplied one, construct it and confirm it covers the whole flow.

### Step 2 — Enumerate failure modes per step/component
For each step/component, ask "how can this fail?" List each distinct failure mode. Then for each mode, state the **effect** — what it causes downstream (to the user, the next step, the outcome).

### Step 3 — Rate severity (1–10)
Anchor to the domain's worst realistic effect:
- **1–2:** negligible — barely noticed.
- **3–4:** minor — small disruption, easily absorbed.
- **5–6:** moderate — noticeable degradation, requires intervention.
- **7–8:** major — objective threatened, customer/operation significantly harmed.
- **9–10:** severe/catastrophic — safety, legal, data-loss, or viability-threatening; 10 often implies no warning.

### Step 4 — Rate occurrence (1–10)
- **1–2:** remote — failure would be surprising.
- **3–4:** low — occasional, isolated.
- **5–6:** moderate — happens periodically.
- **7–8:** high — frequent.
- **9–10:** very high — near-inevitable given current design.

### Step 5 — Rate detectability (1–10, inverted)
Given existing controls, how likely is the failure to be caught *before* the effect lands?
- **1–2:** almost certainly caught (strong automated control / gate).
- **3–4:** likely caught.
- **5–6:** moderate chance — depends on attention.
- **7–8:** unlikely caught — weak or manual control.
- **9–10:** effectively undetectable until the effect occurs.

### Step 6 — Compute RPN and flag high-severity modes
RPN = S × O × D (1–1000). Separately flag every mode with **S ≥ 9** regardless of RPN — high-severity modes get attention even when O and D are low.

### Step 7 — Root cause for high-RPN and high-severity modes
For each prioritized mode, trace *why* it occurs. Don't stop at the proximate cause; go one or two levels deeper (a missing check is a symptom; why is the check missing?).

### Step 8 — Recommend actions by lever
For each prioritized mode, recommend an action and name the lever it moves:
- **Severity ↓:** design out the failure, or contain its blast radius so the effect is milder.
- **Occurrence ↓:** prevent the failure (better process, validation, redundancy).
- **Detectability ↓ (D smaller):** add detection so it's caught before the effect lands.
Estimate the **target RPN** after the action.

### Step 9 — Rank the action list
Order recommended actions by current RPN (with high-severity modes elevated). Show current RPN, lever, action, owner if known, and target RPN.

---

## False-Positive Prevention

1. **Detectability collapse.** Folding D into O or skipping it. A rare invisible failure (low O, high D) can be more dangerous than a frequent caught one. Keep D first-class.
2. **Mode without effect.** Listing "the API call fails" without saying what that *causes*. The effect drives severity; without it, the score is meaningless.
3. **Proximate-cause stopping.** "Root cause: someone forgot." Why was forgetting possible? Go to the structural cause the action can actually fix.
4. **Monitoring as panacea.** Reflexively recommending "add a dashboard." That lowers D only. If the failure is severe, you may need to lower S or O instead. Name the lever.
5. **RPN tunnel vision.** Ignoring a severity-10 mode because its RPN is modest. High-severity modes get flagged regardless of RPN.
6. **Gut scoring.** Rating without the anchored scales, making modes incomparable. Always anchor.
7. **Decomposition gaps.** Analyzing the obvious steps and skipping the handoffs between them — failures cluster at interfaces. Include transitions/handoffs as steps.
8. **Action inflation.** Recommending heavy actions for low-RPN modes. Match effort to RPN; document low-RPN modes but don't over-engineer them.

---

## Output Format

```
# FMEA — [process or product] ([domain])

## Decomposition
[Ordered steps or components, including handoffs/interfaces]

## FMEA table
| Step/Component | Failure mode | Effect | S | O | D | RPN | Root cause | Recommended action | Lever | Target RPN |
|----------------|--------------|--------|---|---|---|-----|------------|--------------------|-------|------------|
| [step 1] | [mode] | [effect] | 8 | 4 | 7 | 224 | [why it occurs] | [action] | detect ↓ | 64 |
| [step 1] | [mode] | [effect] | 9 | 2 | 3 | 54 | [why] | [action] | severity ↓ | 18 |
| [step 2 → 3 handoff] | [mode] | [effect] | 6 | 6 | 8 | 288 | [why] | [action] | occurrence ↓ | 96 |
| … | | | | | | | | | | |

## High-severity flags (S ≥ 9, regardless of RPN)
- [mode] — S=[ ], why it's flagged, recommended action
- …

## Ranked action list (by RPN, high-severity elevated)
| Rank | Failure mode | Current RPN | Lever | Action | Owner | Target RPN |
|------|--------------|-------------|-------|--------|-------|------------|
| 1 | [mode] | 288 | occurrence ↓ | [action] | [name] | 96 |
| 2 | [mode] | 224 | detect ↓ | [action] | [name] | 64 |
| … | | | | | | |

## Summary
- Highest-RPN failure mode: [...]
- Most dangerous high-severity mode: [...]
- Where failures concentrate (which step/interface): [...]
```

---

## Verification

- [ ] Target decomposed into steps/components, including handoffs/interfaces.
- [ ] Every step/component has its failure modes enumerated with effects.
- [ ] S, O, D each rated 1–10 on the anchored scales; D treated as inverted (high = bad).
- [ ] RPN = S × O × D computed for every mode.
- [ ] Every S ≥ 9 mode flagged regardless of RPN.
- [ ] Root cause traced beyond the proximate cause for prioritized modes.
- [ ] Each recommended action names the lever it moves (severity / occurrence / detectability).
- [ ] Target RPN estimated after each action.
- [ ] Action list ranked by RPN with high-severity modes elevated.
- [ ] No detectability collapse; no monitoring-as-universal-fix.
