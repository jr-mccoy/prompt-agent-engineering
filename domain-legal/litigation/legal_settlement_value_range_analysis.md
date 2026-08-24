---
title: "Settlement Value Range Analysis"
category: legal/litigation
description: "Build a defensible settlement value range using expected-value math: liability probability bands, damages bands, defense costs, time-value, leverage adjustments, and a recommended opening / target / walkaway."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - litigation
  - settlement
  - valuation
  - mediation
  - expected-value
updated: "2026-05-08"
related_prompts:
  - domain-legal/litigation/legal_case_strategy_assessment.md
  - domain-legal/research/legal_issue_spotter_from_facts.md
---

**Purpose:** Convert the case into a defensible number with bands and drivers — for client authority discussions, mediation prep, internal go/no-go decisions, and reserve setting.

**When to use:** Pre-mediation, demand/offer formulation, reserve adjustment, client authority requests, decision-tree analysis after a key ruling.

---

## Your Input

- **Client role:** [Plaintiff / defendant]
- **Claims / counterclaims with elements and probability bands:** [If unsupplied, the analysis will derive bands from supplied facts and authority]
- **Damages categories and ranges per claim:** [Compensatory, statutory, punitive (if available), pre/post-judgment interest, fees]
- **Defense / pursuit cost forecast through trial:** [Phase by phase: remaining discovery, dispositive motions, expert work, trial, appeal]
- **Time horizon to resolution:** [Months]
- **Discount rate (for present-value):** [Default 5–8% if unstated]
- **Insurance / indemnification:** [Coverage, retention, eroding limits]
- **Leverage factors:** [Reputational, regulatory, witness availability, parallel matters]
- **Client tolerance / objectives:** [Fast exit, principle, precedential, cash, business relationship]
- **Prior offers and demands:** [History]

---

## Constraints

**Must:**
- Use **expected-value** math: probability of liability × damages range, then subtract (plaintiff) or add (defendant) defense costs and time-value adjustments.
- Present **bands**, not point estimates. Liability and damages are separately uncertain; combine via min/median/max scenarios.
- Distinguish **liability probability** from **damages range**. Multiplying a single liability number by a single damages number understates uncertainty.
- Identify the **drivers** that move the EV most and run a sensitivity table.
- Apply a **time-value discount** for plaintiffs and a **time-value adjustment** for defendants where appropriate.
- Subtract **remaining defense / pursuit costs** from the trial scenario (and where the rule allows recovery, treat fees separately).
- Add **leverage adjustments** as transparent line items, not buried in the probability band.
- Provide an **opening / target / walkaway** triplet with rationale tied to the EV bands.

**Must Not:**
- Multiply a single liability percentage by a single damages number and call it the value.
- Treat punitives as if they were available without confirming the substantive law and the cap.
- Ignore fee-shifting where it applies (e.g., Section 1988, FLSA, contract fee provisions).
- Use a discount rate without disclosing it.
- Inflate value by adding leverage without showing the adjustment.
- Hide assumptions in prose; the math should be inspectable.

---

## Instructions

1. **Build a liability decision tree.** For each claim, list the elements; assign a probability band (low/median/high) to clearing all elements. For affirmative defenses, assign a probability band to the defense succeeding.
2. **Build a damages range** per claim and component (compensatory, statutory, punitive if available and substantively supported, fees, pre/post-judgment interest).
3. **Combine** into trial-outcome scenarios. Minimum useful scenarios: defense verdict; small plaintiff verdict; midpoint; large plaintiff verdict.
4. **Subtract defense / pursuit cost** through trial (and appeal if relevant). For plaintiff, subtract pursuit costs from the recovery (and adjust for any contingency arrangement). For defendant, sum defense costs by phase.
5. **Apply time-value discount** for delay to recovery (plaintiff) or delay to certainty (defendant).
6. **Apply leverage adjustments** as itemized line items: reputational risk delta, regulatory exposure delta, witness availability delta, parallel-matter spillover delta.
7. **Compute settlement zones**:
   - Plaintiff perspective: minimum acceptable = EV(trial) − pursuit cost − time-value − risk premium for plaintiff's risk preferences.
   - Defendant perspective: maximum acceptable = EV(trial) + defense cost − leverage gain + risk premium for defendant's risk preferences.
   - Zone of possible agreement (ZOPA) is between the two reservation values.
8. **Sensitivity table** on the two or three biggest drivers (e.g., key witness credibility, MSJ outcome, punitives availability).
9. **Opening / target / walkaway** for the client's role with rationale.

---

## Output Format

```markdown
# SETTLEMENT VALUE ANALYSIS — {MATTER}
**Privileged & Confidential — Attorney Work Product**

## Liability Probability Bands

| Claim / Defense | Element bottleneck | Low | Median | High | Driver |
|-----------------|---------------------|-----|--------|------|--------|

## Damages Range

| Component | Low | Median | High | Notes |
|-----------|-----|--------|------|-------|
| Compensatory | ... | ... | ... | ... |
| Statutory (if any) | ... | ... | ... | ... |
| Punitive (cap: {...}) | ... | ... | ... | ... |
| Pre-judgment interest | ... | ... | ... | rate: ... |
| Fees (basis: {statute / contract}) | ... | ... | ... | ... |
| Post-judgment interest | ... | ... | ... | ... |

## Trial-Outcome Scenarios

| Scenario | Liability prob. | Damages | Probability-weighted | Notes |
|----------|------------------|---------|------------------------|-------|
| Defense verdict | {p} | $0 | $0 × p | ... |
| Small plaintiff verdict | {p} | $X | ... | ... |
| Midpoint | {p} | $Y | ... | ... |
| Large plaintiff verdict | {p} | $Z | ... | ... |
| **EV(trial)** | | | $... | |

## Costs and Time

| Phase | Defense/pursuit cost | Months |
|-------|------------------------|--------|
| Remaining discovery | ... | ... |
| Dispositive motions | ... | ... |
| Expert work | ... | ... |
| Trial | ... | ... |
| Appeal (if applicable) | ... | ... |
| **Total** | **$...** | **{N} months** |

Discount rate applied: {X}%
Time-value adjustment: {value}

## Leverage Adjustments (itemized)

| Factor | Direction | Magnitude | Reason |
|--------|-----------|-----------|--------|
| Reputational | + / − | $... | ... |
| Regulatory parallel | + / − | $... | ... |
| Witness availability | + / − | $... | ... |
| Parallel matters / precedent | + / − | $... | ... |

## Reservation Values

- **Plaintiff floor:** $...
- **Defendant ceiling:** $...
- **ZOPA:** ${low}–${high} (or "no overlap — {reason}")

## Sensitivity Table

| Driver | −1σ | Base | +1σ |
|--------|------|------|-----|
| {Driver 1: e.g., MSJ probability} | $... | $... | $... |
| {Driver 2} | $... | $... | $... |
| {Driver 3} | $... | $... | $... |

## Recommendation

- **Opening:** $...  — rationale: {...}
- **Target:** $...  — rationale: {...}
- **Walkaway:** $... — rationale: {...}
- **Non-monetary terms to push for:** {confidentiality, non-disparagement, mutual release scope, no-rehire, structured payment, …}

## Decision Points
- {Trigger that would move the number, e.g., "If MSJ is denied on liability, midpoint scenario shifts from p=0.3 to p=0.5; new EV = …"}
```

---

## Verification

- [ ] Liability and damages handled as separately uncertain.
- [ ] Bands, not point estimates, throughout.
- [ ] Costs subtracted (or added) explicitly.
- [ ] Time-value discount disclosed.
- [ ] Leverage adjustments itemized, not folded into probability.
- [ ] Sensitivity table on the most-moving drivers.
- [ ] Reservation values and ZOPA computed.
- [ ] Punitives treated only if substantive law allows; cap noted.
- [ ] Fee-shifting addressed where applicable.
- [ ] Opening / target / walkaway each tied to rationale.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Multiplying one liability % by one damages number | Use min/median/max scenarios for each axis |
| Forgetting fee-shifting where it applies | Identify the basis (statute, contract) and treat fees as a separate component |
| Adding punitives without confirming availability | Verify substantive law and any applicable cap; otherwise exclude or band low |
| Ignoring eroding insurance limits | Eroding policies change leverage as defense costs accumulate |
| Hiding leverage in the probability number | Itemize leverage adjustments transparently |
| Anchoring on the prior demand | Build EV from facts and law; the prior demand is data, not a value |
| Treating contingency-fee economics as immaterial | Plaintiff floor must reflect contingency-net recovery |
| Skipping the time-value discount for a multi-year case | A nominal $1M three years out is materially less than $1M today |
| Reporting a single number without bands | Bands force the conversation onto drivers |
