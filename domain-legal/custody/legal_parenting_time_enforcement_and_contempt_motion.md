---
title: "Parenting-Time Enforcement and Contempt Motion"
category: legal/custody
description: "Draft a motion to enforce a custody/parenting-time order: document the specific violations (denied time, late or no-show exchanges, unilateral schedule changes), establish the elements of contempt (a clear order, knowledge, ability to comply, willful violation), request graduated remedies (make-up/compensatory parenting time, fees, modification, contempt sanctions), and supply a violation log and proposed order — sized to the controlling state's enforcement framework."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - legal
  - custody
  - family-law
  - enforcement
  - contempt
  - parenting-time
updated: "2026-06-01"
related_prompts:
  - domain-legal/custody/legal_parenting_plan_drafter.md
  - domain-legal/custody/legal_high_conflict_parenting_coordination_provisions.md
  - domain-legal/custody/legal_custody_modification_analysis_and_motion.md
  - domain-legal/divorce/legal_divorce_postjudgment_modification_and_enforcement.md
  - domain-legal/custody/legal_holiday_and_vacation_schedule_builder.md
---

**Purpose:** Draft a motion to enforce a parenting-time order and, where warranted, hold the violating parent in contempt — documenting the specific violations, establishing the contempt elements, and requesting graduated remedies. Output is a filing-ready enforcement/contempt motion with a violation log and proposed order, not a guaranteed result.

**When to use:** A parent is denying or interfering with court-ordered parenting time, missing or sabotaging exchanges, or unilaterally changing the schedule; seeking make-up time, fees, or contempt; building a record of non-compliance.

---

## Your Input

- **Jurisdiction:** [State; the enforcement and contempt framework; available remedies and standards `[CITE: …]`]
- **The order:** [The custody/parenting-time order, its date, and the specific provisions violated]
- **Violations:** [Dated, specific incidents — denied time, late/no-show exchanges, unilateral changes, gatekeeping — with evidence]
- **Knowledge & willfulness:** [That the violating parent knew of the order and the conduct was deliberate]
- **Ability to comply:** [Whether the violating parent had the ability to comply]
- **Harm:** [Lost time, impact on the child, costs incurred]
- **Prior efforts:** [Communications, prior warnings, prior motions]
- **Relief sought:** [Make-up/compensatory time, fees, modification, contempt sanctions, enforcement mechanisms]

---

## Constraints

**Must:**
- Identify the **order provision** violated and document **specific, dated violations** with evidence (messages, exchange logs, witnesses) — a **violation log**.
- Establish the **elements of contempt**: a **clear and unambiguous order**, the violating parent's **knowledge**, the **ability to comply**, and a **willful** violation `[CITE: …]`.
- Request **graduated remedies** appropriate to the conduct — **make-up/compensatory parenting time**, **fees and costs**, **modification** of the plan (e.g., neutral exchanges, ROFR), and **contempt sanctions** — escalating with the severity and pattern.
- Distinguish **civil contempt** (coercive/remedial, with a purge) from **criminal contempt** (punitive) where the state recognizes both.
- Address the respondent's likely **defenses** (ambiguous order, inability to comply, the child's refusal) and how the facts meet or rebut them.
- Keep the focus on the **child's interest** in the relationship and the integrity of the order, not punishment for its own sake.
- Supply the **supporting declaration** and a **proposed order**.
- Use placeholders `[CITE: ...]`, `[NEED: ...]` for unsupplied authority or facts.

**Must Not:**
- Seek contempt where the order is ambiguous or the violating parent lacked the ability to comply.
- Treat a child's age-appropriate refusal as automatic contempt without addressing the custodial parent's obligation to facilitate.
- Use contempt as leverage absent a genuine, documented violation (MRPC 3.1).
- Invent the contempt elements, remedies, or sanctions available.
- Threaten incarceration outside the proper civil/criminal-contempt framework.
- Insert generic "consult counsel" disclaimers.

---

## Instructions

1. **Order & provision.** Identify the clear order provision violated.
2. **Violation log.** Document each dated violation with evidence and the parenting time lost.
3. **Contempt elements.** Establish clear order, knowledge, ability to comply, and willfulness.
4. **Defenses.** Anticipate and address ambiguity, inability, and child-refusal defenses.
5. **Remedies.** Request graduated relief (make-up time, fees, modification, contempt) matched to the conduct/pattern.
6. **Contempt type.** Specify civil (with purge) vs. criminal where applicable.
7. **Motion package.** Caption, grounds, violation log, declaration, requested relief, proposed order.

---

## Output Format

```markdown
{STATE} {COURT}, COUNTY OF {COUNTY}
{Caption}     Case No. {____}

MOTION TO ENFORCE PARENTING TIME {AND FOR CONTEMPT}

1. THE ORDER. The {date} order provides: {quoted provision}.

2. VIOLATIONS (Violation Log).
| # | Date | Provision violated | What happened | Evidence | Time lost |
|---|---|---|---|---|---|
| 1 | {…} | {…} | {denied/late/no-show/unilateral change} | {msg/log/witness} | {…} |

3. CONTEMPT ELEMENTS. Clear order: {…}; knowledge: {…}; ability to comply: {…}; willfulness: {…} [CITE: …].

4. ANTICIPATED DEFENSES. Ambiguity: {rebuttal}; inability: {rebuttal}; child refusal: {custodial duty to facilitate}.

5. RELIEF REQUESTED (graduated).
   a. Compensatory/make-up parenting time of {…};
   b. Attorney's fees and costs of {$};
   c. Modification: {neutral exchanges / ROFR / specified schedule};
   d. {Civil contempt with purge of {…} / referral for criminal contempt}.

DECLARATION OF {MOVANT}: {numbered personal-knowledge facts}.
[PROPOSED] ORDER: {…}.
```

---

## Verification

- [ ] Clear order provision identified and quoted.
- [ ] Violation log documents specific, dated incidents with evidence and time lost.
- [ ] Contempt elements (clear order, knowledge, ability, willfulness) established.
- [ ] Likely defenses (ambiguity, inability, child refusal) anticipated and addressed.
- [ ] Graduated remedies matched to the conduct/pattern.
- [ ] Civil vs. criminal contempt specified where applicable.
- [ ] Supporting declaration and proposed order included.
- [ ] No contempt sought on an ambiguous order or without ability to comply; no invented remedies.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Seeking contempt on an ambiguous order | Contempt requires a clear, unambiguous order; quote the provision |
| Ignoring the violating parent's inability to comply | Inability is a defense; address ability to comply |
| Treating a child's refusal as automatic contempt | Address the custodial parent's duty to facilitate; assess willfulness |
| Going straight to incarceration | Use graduated remedies; specify civil (with purge) vs. criminal contempt |
| Conclusory "she keeps denying time" | Provide a dated violation log with evidence |
| Using contempt purely as leverage | Require a genuine, documented violation (MRPC 3.1) |
| Inventing available remedies/sanctions | Use [CITE]/[NEED] placeholders |
| Forgetting make-up/compensatory time | Request compensatory parenting time, not just sanctions |
| Omitting fees where available | Request fees and costs under the enforcement framework |
| No proposed modification to prevent recurrence | Add structural fixes (neutral exchanges, ROFR, specificity) |
