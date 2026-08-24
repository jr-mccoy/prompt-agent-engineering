---
title: "Audit Where You Gain vs. Break Under Stress"
category: personal-development/resilience
description: "Map a person's domains (work, finances, skills, relationships, health, identity) against how each responds to stress and volatility — fragile (breaks), robust (endures), or antifragile (gains) — and prescribe targeted moves to reduce fragility and add upside."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - AG-11
  - DS-06
  - QA-12
difficulty: advanced
tags:
  - resilience
  - antifragility
  - stress
  - audit
  - robustness
updated: "2026-06-21"
related_prompts:
  - domain-personal-development/prompts/resilience/resilience_failure_reframe.md
  - domain-personal-development/prompts/resilience/resilience_self_discipline_system.md
  - domain-personal-development/career-transformation/career_role_structural_vulnerability.md
  - domain-personal-development/prompts/agency/agency_proof_of_work_portfolio.md
  - domain-personal-development/prompts/identity/identity_life_audit_reckoning.md
---

# Audit Where You Gain vs. Break Under Stress

**Objective:** Classify each of the user's life domains by how it responds to stress — **fragile** (degrades or breaks), **robust** (holds), or **antifragile** (improves) — and prescribe a small number of targeted moves to remove the most dangerous fragilities and add upside exposure where it's cheap.

> **Boundary — non-clinical self-direction.** This is a structural self-audit of how your circumstances respond to volatility, not a psychological assessment. Concepts like "antifragility" describe systems, not a person's worth or mental health. If the audit surfaces that the real fragility is psychological distress — chronic anxiety, depression, trauma response, hopelessness, or self-harm risk — that is outside scope; route to a licensed professional or `domain-psychology/`. In the US, call or text 988. Do not use "you should be more antifragile" as self-criticism.

## When to Use

- Use when: the user wants a structural map of where they're exposed before a shock, not after.
- Use when: the user keeps getting hurt by the same kind of disruption and wants to see the pattern.
- Use when: the user has slack/resources and wants to invest in resilience deliberately.
- **Don't use when:** the user is mid-crisis and needs to stabilize — use `resilience_setback_recovery_framework.md`.
- **Don't use when:** the question is purely career-structural — `career_role_structural_vulnerability.md` is more focused.
- **Don't use when:** the surfaced fragility is clinical (see boundary) — refuse and refer.

## Inputs / Context

1. **Which domains to audit.** Default set: work/income, finances, skills, relationships/support, health, identity/meaning. User may add or narrow.
2. **For each domain: how it responded to the last real shock** the user experienced (a layoff, illness, breakup, market drop, etc.).
3. **The user's current slack** — savings runway, time, energy, social support — i.e., capacity to invest in resilience.
4. **The volatility the user actually faces** — what kinds of shocks are plausible in their situation (not theoretical black swans).
5. **What the user is optimizing for right now** — peak performance, stability, or growth — since the right amount of fragility differs.

**Refusal logic:** If input (2) is absent for the audited domains, ask — classification rests on observed responses, not self-image. If the user's account of any domain is dominated by clinical distress (e.g., "my health is fine but I can't stop the panic"), do not classify that as a structural fragility to engineer around; issue the boundary referral for that domain.

## Instructions

### Step 1 — Classify each domain on the fragility spectrum

For each domain, assign exactly one label, grounded in input (2):

| Label | Definition | Tell |
|---|---|---|
| **Fragile** | A shock causes lasting damage; recovery is slow or incomplete. | One bad event would set the domain back months/years (single income, no savings, one critical relationship, brittle health). |
| **Robust** | A shock is absorbed without lasting damage; the domain returns to baseline. | Has buffers/redundancy; bends but doesn't break. |
| **Antifragile** | The domain *improves* from a moderate shock — stress reveals weak points that get fixed, or volatility creates opportunity. | Past shocks made it stronger (a layoff that led to a better-diversified income; an illness that built better habits). |

Be honest about robust-vs-antifragile: most well-managed domains are *robust*, not antifragile. Antifragile requires actual gain from disorder, not just survival.

### Step 2 — Rate the danger of each fragility

For each **fragile** domain, score danger using two factors (DS-06):

- **Likelihood** of a relevant shock (from input 4 — real volatility, not imagined).
- **Severity** if it lands (recoverable inconvenience vs. catastrophic).

Rank the fragilities High / Medium / Low. A fragile domain facing low-likelihood, low-severity shocks is not urgent; a fragile domain facing plausible, severe shocks is the priority.

### Step 3 — Prescribe moves (two types)

For the top fragilities only, prescribe:

- **De-fragilizing moves:** add a buffer, redundancy, or optionality (an emergency fund, a second income stream, a backup relationship/support, a health margin). Target: convert High-danger fragile → robust.
- **Upside moves (where cheap):** small, capped-downside exposures that could pay off big under volatility (a side project, a new skill, a few low-cost bets). Target: add antifragility where the cost of trying is small and the loss is bounded.

Apply the **barbell principle**: protect the essential (make the fragile robust) while taking small, bounded risks for upside. Avoid the fragile middle — moderate exposure with uncapped downside.

### Step 4 — Limit to a few moves

Output **at most 3 moves total**, ranked. A resilience audit that produces 15 tasks is itself fragile (it won't get done). Pick the moves that most reduce the highest-danger fragility.

### Step 5 — Verify by prediction

For each prescribed move, state what would be true after a future shock if the move worked (e.g., "if income loses one client, the second stream now covers fixed costs, so the shock is absorbed rather than catastrophic"). This is the test of whether the audit was real.

## Constraints

**Must:**
- Classify each domain as exactly one of fragile / robust / antifragile, grounded in the last real shock.
- Distinguish robust (survives) from antifragile (gains) honestly.
- Rate fragilities by likelihood × severity using the user's real volatility.
- Apply the barbell principle (protect essential, bound the bets).
- Cap output at 3 ranked moves.
- Honor the clinical boundary.

**Must Not:**
- Call mere survival "antifragile."
- Prescribe uncapped-downside risks in the name of "antifragility."
- Engineer around a fragility that is actually psychological distress.
- Produce a long, fragile task list.
- Diagnose any condition or frame antifragility as a character standard the user is failing.

## False-Positive Prevention

1. **Don't inflate robust to antifragile.** Surviving a shock unchanged is robust. Antifragile requires demonstrable *gain* from the disorder. Most domains top out at robust — that's fine; don't oversell.
2. **Don't import theoretical black swans.** Anchor likelihood to the volatility in input (4). A plausible client loss matters; an asteroid does not.
3. **Don't prescribe risk without a downside cap.** "Take more risks to become antifragile" without bounding the loss is how people blow up. Every upside move must have a known, survivable worst case.
4. **Don't medicalize, and don't anti-medicalize.** A structural fragility (no savings) gets a buffer. A clinical fragility (panic, depression) gets a referral, not an emergency fund.
5. **Don't conflate fragility with weakness.** Fragility is exposure, not character. The audit reduces exposure; it does not grade the person.

## Expected Output

A domain-by-domain classification table, a danger ranking of the fragilities, at most 3 ranked moves (de-fragilizing and/or upside), and a per-move prediction.

### Example Output

```
## Domain classification
| Domain | Label | Basis (last shock) |
|---|---|---|
| Income | Fragile | Single employer; the last layoff cost 5 months of zero income. |
| Finances | Robust | 6-month emergency fund absorbed that layoff without debt. |
| Skills | Antifragile | Forced job-hunt pushed you to learn data skills that raised your ceiling. |
| Relationships | Robust | Support network held through the layoff. |
| Health | Fragile | Stress periods reliably trigger insomnia that degrades everything else. |
| Identity/meaning | Robust | Sense of self didn't collapse with the job. |

## Fragility danger ranking
1. Income — HIGH (single employer; another layoff is plausible in your field; severity high — it's your only source).
2. Health (stress-insomnia) — MEDIUM (likely to recur; severity moderate, knock-on to everything). NOTE: if the insomnia/stress is closer to an anxiety disorder, that's a clinical referral, not a structural fix.

## Moves (max 3, ranked)
1. De-fragilize income: start one small second income stream (consulting on your new data skills) — target $1k/mo within 90 days. Converts income from fragile → robust.
2. Upside (cheap, capped): publish your data work publicly (portfolio) — bounded cost (time), uncapped upside (inbound work). Adds antifragility to skills/income.
3. De-fragilize health: a fixed wind-down routine as a buffer against stress-insomnia (structural, not clinical). If it doesn't help within 3 weeks, treat as clinical and see a doctor.

## Predictions
- Move 1: if you lose the employer again, the second stream + emergency fund covers fixed costs — the next layoff becomes survivable, not catastrophic.
- Move 2: under industry volatility, public work generates inbound options you wouldn't have had — volatility now sometimes helps you.
- Move 3: next stress period, sleep degrades less, so the cascade into other domains is dampened (or it confirms a clinical referral is needed).
```

## Verification

- [ ] Every audited domain has exactly one fragile/robust/antifragile label tied to a real shock.
- [ ] Robust and antifragile are distinguished honestly (gain required for antifragile).
- [ ] Fragilities are ranked by likelihood × severity using real volatility.
- [ ] Moves apply the barbell principle; every bet has a capped downside.
- [ ] No more than 3 ranked moves.
- [ ] Each move has an observable post-shock prediction.
- [ ] Psychological fragilities routed to referral, not engineered around.
- [ ] Clinical boundary honored.

## Techniques Used

- **ST-01 (Clear Objective Statement):** Sets the goal as a fragility map plus a capped set of targeted moves.
- **ST-02 (Structured Sequential Instructions):** Classify → rate → prescribe → cap → predict, in fixed order.
- **RT-02 (Multi-Dimensional Analysis Framework):** Audits multiple life domains and rates each on likelihood and severity rather than one dimension.
- **AG-11 (Taxonomy-Based Classification Systems):** The fragile/robust/antifragile taxonomy forces a single honest label per domain.
- **DS-06 (Prioritization and Severity Guidance):** Likelihood × severity ranking focuses the (capped) moves on the highest-danger fragilities.
- **QA-12 (False Positives Identification):** Guards against robust-inflated-to-antifragile, theoretical black swans, uncapped risk, and medicalizing/anti-medicalizing errors.

## Related Prompts

- [resilience_failure_reframe.md](resilience_failure_reframe.md) — Turn the specific shocks this audit references into lessons.
- [resilience_self_discipline_system.md](resilience_self_discipline_system.md) — Build the systems that make de-fragilizing moves stick.
- [career_role_structural_vulnerability.md](../../career-transformation/career_role_structural_vulnerability.md) — A focused fragility audit of the user's specific role/income.
- [agency_proof_of_work_portfolio.md](../agency/agency_proof_of_work_portfolio.md) — Building the public-work upside move from the example.
- [identity_life_audit_reckoning.md](../identity/identity_life_audit_reckoning.md) — Broader life audit when the fragilities point to a major inflection.
