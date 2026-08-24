---
title: "Child Custody Best-Interests Analysis"
category: legal/custody
description: "Analyze a custody dispute factor-by-factor under the controlling state's best-interests statute: apply each enumerated factor to the facts, address legal vs. physical custody and decision-making, weigh stability/primary-caregiver and any presumptions (joint custody, against an abuser), assess the child's preference where age-appropriate, and produce a position memo with factor-by-factor strength and a defensible custody/parenting recommendation."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-01
  - RT-02
  - RT-05
  - RP-01
  - CM-02
  - QA-01
  - QA-12
difficulty: advanced
tags:
  - legal
  - custody
  - family-law
  - best-interests
  - parenting
  - child-custody
updated: "2026-06-01"
related_prompts:
  - domain-legal/custody/legal_parenting_plan_drafter.md
  - domain-legal/custody/legal_custody_trial_prep_and_factor_proof_plan.md
  - domain-legal/custody/legal_custody_modification_analysis_and_motion.md
  - domain-legal/custody/legal_uccjea_jurisdiction_analysis.md
  - domain-legal/custody/legal_custody_evaluation_prep_and_response.md
---

**Purpose:** Apply the controlling state's best-interests-of-the-child factors to the facts of a custody dispute, factor by factor, and produce a reasoned custody and parenting-time recommendation with the strength of each factor and the evidence needed. Output is an internal position memo, not advice to the client and not a guaranteed result; the court applies the factors.

**When to use:** Assessing a custody position before filing or settlement; preparing a custody argument for trial; evaluating the other parent's position; framing the parenting-plan proposal.

---

## Your Input

- **Jurisdiction:** [State; the state's best-interests statute and enumerated factors `[NEED FACTOR LIST: …]` `[CITE: …]`; any presumptions]
- **Children:** [Names, ages, special needs, school, community ties, siblings]
- **Current arrangement:** [Existing schedule, primary caregiver history, who does what]
- **Each parent:** [Caregiving role, work schedule, home environment, mental/physical health, willingness to co-parent, history with the child]
- **Co-parenting facts:** [Each parent's support of the child's relationship with the other; conflict level]
- **Safety facts:** [DV, abuse, neglect, substance use, untreated mental illness — and supporting evidence]
- **Child's preference:** [If of an age/maturity the state considers]
- **Stability factors:** [Continuity of home, school, community; proposed changes]
- **Custody type sought:** [Legal (decision-making) and physical (residential) custody; joint vs. sole]

---

## Constraints

**Must:**
- Use the state's **enumerated best-interests factors** and apply **each one** to the facts `[NEED FACTOR LIST: …]` `[CITE: …]`; do not substitute a generic factor list.
- Distinguish **legal custody (decision-making)** from **physical custody (residential time)** and address each.
- Apply any **state presumptions** — a joint-custody preference, a primary-caregiver consideration, or a **presumption against custody for a perpetrator of domestic violence** `[CITE: …]`.
- Anchor every conclusion to the **child's** interests, not the parent's preferences or fairness between parents.
- Weigh **stability and continuity** (home, school, community) and the **status quo** appropriately.
- Address the **child's preference** only to the extent and weight the state allows for the child's age/maturity.
- Treat **safety factors** (DV, abuse, substance use) as potentially dispositive, with the evidence required.
- Assign **factor-by-factor strength** and an overall recommendation with **confidence**; frame as a position (QA-12).
- Use placeholders `[CITE: ...]`, `[NEED FACTOR LIST: ...]`, `[NEED: ...]` for unsupplied authority, factors, or facts.

**Must Not:**
- Invent the state's factors, presumptions, or the weight given to a child's preference.
- Frame the analysis around fairness to the parents rather than the child's best interests.
- Treat joint custody as automatic, or assume the primary caregiver always prevails.
- Minimize or ignore credible safety concerns.
- Present a definitive custody outcome where the standard is discretionary.
- Insert generic "consult counsel" disclaimers.

---

## Instructions

1. **Factor list & presumptions.** State the enumerated factors and any presumptions for the state `[CITE: …]`.
2. **Factor-by-factor application.** For each factor: facts → analysis → which parent it favors and why → evidence needed → strength.
3. **Legal vs. physical custody.** Recommend the decision-making allocation and the residential arrangement separately.
4. **Stability/primary caregiver.** Weigh continuity and caregiving history under the state's approach.
5. **Child's preference.** Address weight per the child's age/maturity and the state's rule.
6. **Safety analysis.** Apply any DV presumption; assess abuse/substance/mental-health factors with the evidence required.
7. **Recommendation.** Synthesize into a custody and parenting-time recommendation with confidence and the strongest/weakest factors.

---

## Output Format

```markdown
# BEST-INTERESTS CUSTODY ANALYSIS — PRIVILEGED WORK PRODUCT
**State:** {…} [CITE: …]   **Children:** {…}   **Presumptions:** {…}

## 1. Factors & Presumptions
{Enumerated factors} [NEED FACTOR LIST]; presumptions: {joint / primary caregiver / against DV perpetrator}

## 2. Factor-by-Factor Application
| Factor | Facts | Favors | Evidence needed | Strength |
|---|---|---|---|---|
| {Factor 1} | {…} | {Parent A/B} | {…} | {strong/weak} |

## 3. Legal vs. Physical Custody
- Legal (decision-making): {joint/sole to {}}; reason: {…}
- Physical (residential): {schedule}; reason: {…}

## 4. Stability / Primary Caregiver
{…}

## 5. Child's Preference
- Weight per age/maturity and state rule: {…}

## 6. Safety Analysis
- {DV presumption / abuse / substance / mental health}: {…}; evidence: {…}

## 7. Recommendation
- Custody/parenting recommendation: {…}; overall confidence: {…}; strongest factors: {…}; weakest: {…}
```

---

## Verification

- [ ] State's enumerated factors applied individually to the facts.
- [ ] Legal and physical custody addressed separately.
- [ ] State presumptions (joint, primary caregiver, against DV perpetrator) applied.
- [ ] Conclusions anchored to the child's interests, not parental fairness.
- [ ] Stability/continuity weighed; status quo considered.
- [ ] Child's preference weighted per age/maturity and the state's rule.
- [ ] Safety factors analyzed with required evidence; not minimized.
- [ ] Factor strength and overall confidence assigned; framed as a position.
- [ ] No invented factors, presumptions, or preference rules.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Using a generic best-interests list instead of the state's | Apply the state's enumerated factors [NEED FACTOR LIST] |
| Framing the analysis around fairness between parents | Anchor every factor to the child's best interests |
| Assuming joint custody or that the primary caregiver always wins | Apply the state's actual presumptions and weigh the facts |
| Conflating legal and physical custody | Analyze decision-making and residential time separately |
| Minimizing credible DV/abuse/substance concerns | Apply the DV presumption; treat safety as potentially dispositive |
| Overweighting the child's preference | Apply the weight the state gives for the child's age/maturity |
| Presenting a definitive outcome | Provide factor strength and overall confidence (discretionary standard) |
| Inventing presumptions or factor weights | Use [CITE]/[NEED] placeholders |
| Ignoring stability/continuity | Weigh continuity of home, school, and community |
| Recommending without identifying needed evidence | List the evidence each favorable factor requires |
