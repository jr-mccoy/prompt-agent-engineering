---
title: "Parenting Plan Drafter"
category: legal/custody
description: "Draft a detailed parenting plan (custody/co-parenting agreement): legal custody and a decision-making framework (education, health, religion, activities), physical custody with a concrete residential schedule, holiday/vacation/school-break allocation, exchange logistics, communication protocols, travel and relocation notice, right of first refusal, dispute-resolution, and modification terms — anchored to the child's best interests and sized to the controlling state's parenting-plan requirements."
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
  - parenting-plan
  - co-parenting
  - residential-schedule
updated: "2026-06-01"
related_prompts:
  - domain-legal/custody/legal_custody_best_interests_analysis.md
  - domain-legal/custody/legal_holiday_and_vacation_schedule_builder.md
  - domain-legal/custody/legal_high_conflict_parenting_coordination_provisions.md
  - domain-legal/custody/legal_child_support_calculation_framework.md
  - domain-legal/divorce/legal_marital_settlement_agreement_drafter.md
  - domain-legal/divorce/legal_post_mediation_term_sheet_and_mou_drafter.md
---

**Purpose:** Draft a complete, court-ready parenting plan that allocates decision-making, sets a concrete residential and holiday schedule, and specifies the logistics and protocols that prevent future disputes — all anchored to the child's best interests and the state's parenting-plan requirements. Output is a full parenting plan suitable for agreement or court adoption, not a memo.

**When to use:** Memorializing custody and parenting time in a divorce/parentage/custody case; converting a custody decision into an operational plan; replacing a vague or conflict-prone existing arrangement.

---

## Your Input

- **Jurisdiction:** [State; mandatory parenting-plan elements and any required form `[CITE: …]`]
- **Child(ren):** [Names, ages, school, activities, special needs]
- **Legal custody:** [Joint/sole; how decisions are made by category (education, medical, religion, extracurriculars)]
- **Physical custody / schedule:** [Desired residential pattern — e.g., week-on/week-off, 2-2-3, alternating weekends, school-year vs. summer]
- **Holidays/breaks:** [Holiday list, school-break and summer preferences, birthdays, special days]
- **Exchanges:** [Times, locations, transportation, who provides it]
- **Communication:** [Parent-child contact during the other's time; parent-parent communication method]
- **Travel/relocation:** [Notice requirements, out-of-state/international travel, passports]
- **Conflict level & safety:** [Whether high-conflict provisions or supervised/safety terms are needed]
- **Right of first refusal:** [Threshold for offering care to the other parent]

---

## Constraints

**Must:**
- Include the state's **mandatory parenting-plan elements** `[CITE: …]`; do not omit required components.
- Separate **legal custody (decision-making)** from **physical custody (schedule)** and specify a **decision-making framework by category**, including how disagreements are resolved.
- Provide a **concrete, unambiguous residential schedule** (specific days/times), not a vague "reasonable parenting time."
- Allocate **holidays, school breaks, summer, and special days** with a clear rotation and a precedence rule (holiday schedule overrides the regular schedule).
- Specify **exchange logistics** (time, place, transportation, late/no-show protocol).
- Set **communication protocols** (child's contact with each parent; the co-parenting communication channel).
- Include **travel/relocation notice**, **right of first refusal** (with a threshold), **dispute-resolution** (mediation before court), and **modification/review** terms.
- Where conflict or safety warrants, incorporate **high-conflict** or **safety/supervised** provisions (cross-reference those prompts).
- Keep every provision **child-centered** and operationally clear so a third party could follow it.
- Use placeholders `[CITE: ...]`, `[NEED: ...]` for unsupplied requirements or facts.

**Must Not:**
- Use vague terms ("reasonable," "as agreed") for the core schedule without a default fallback.
- Make child support or the court's continuing jurisdiction non-modifiable.
- Omit a precedence rule for overlapping schedules (regular vs. holiday vs. vacation).
- Invent the state's mandatory elements or required form.
- Draft provisions that are unworkable or invite repeated litigation.
- Insert generic "consult counsel" disclaimers.

---

## Instructions

1. **State requirements.** List the mandatory parenting-plan elements for the state `[CITE: …]`.
2. **Legal custody & decisions.** Allocate decision-making by category; specify the process for resolving disagreements.
3. **Residential schedule.** Draft the concrete regular schedule (school-year and, if different, summer) with specific days/times.
4. **Holidays/breaks.** Allocate holidays, breaks, and special days with a rotation and a precedence rule.
5. **Exchanges.** Specify time, place, transportation, and a late/no-show protocol.
6. **Communication.** Set child-parent contact and the co-parenting communication channel.
7. **Travel/relocation, ROFR, dispute resolution, modification.** Add notice rules, right of first refusal, mediation-first dispute resolution, and review/modification terms.
8. **Conflict/safety provisions.** Add high-conflict or supervised/safety terms where needed.

---

## Output Format

```markdown
PARENTING PLAN — {Child(ren)} — Case No. {____}
**State requirements:** {…} [CITE: …]

1. LEGAL CUSTODY & DECISION-MAKING. {Joint/sole}. Decisions: education {…}, medical {…}, religion {…}, activities {…}. Disagreements resolved by {mediation/PC/tie-breaker}.

2. PHYSICAL CUSTODY — RESIDENTIAL SCHEDULE.
   - School year: {specific pattern with days/times}.
   - Summer: {pattern}.

3. HOLIDAYS, BREAKS & SPECIAL DAYS. {Rotation table}. The holiday/vacation schedule takes precedence over the regular schedule; vacation over holiday {or as specified}.

4. EXCHANGES. Time/place: {…}; transportation: {…}; late/no-show protocol: {…}.

5. COMMUNICATION. Child-parent contact during the other's time: {…}; co-parent communication via {method}.

6. TRAVEL & RELOCATION. Notice: {N days}; out-of-state/international: {consent/itinerary/passport}.

7. RIGHT OF FIRST REFUSAL. If a parent is unavailable for {threshold}, the other parent is offered the time first.

8. DISPUTE RESOLUTION. {Mediation before court}; {parenting coordinator if high-conflict}.

9. MODIFICATION/REVIEW. {Review trigger}; custody and child support remain subject to the Court's continuing jurisdiction.

{Safety/supervised provisions if applicable}
{Signatures / for court adoption}
```

---

## Verification

- [ ] State's mandatory parenting-plan elements included.
- [ ] Legal custody decision-making allocated by category with a disagreement-resolution process.
- [ ] Residential schedule is concrete (specific days/times), not vague.
- [ ] Holidays/breaks/summer allocated with a rotation and a precedence rule.
- [ ] Exchange logistics and late/no-show protocol specified.
- [ ] Communication protocols set for child and co-parents.
- [ ] Travel/relocation notice, right of first refusal, dispute resolution, and modification terms included.
- [ ] Conflict/safety provisions added where warranted.
- [ ] No vague core-schedule terms; no non-modifiable child support; no invented requirements.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| "Reasonable parenting time" with no schedule | Specify exact days/times with a default fallback |
| No precedence rule for overlapping schedules | State that holiday/vacation overrides the regular schedule |
| Conflating decision-making with the residential schedule | Separate legal and physical custody provisions |
| Omitting the state's mandatory elements | Include all required components [CITE] |
| Making child support/custody non-modifiable | Recite continuing jurisdiction and modifiability |
| Vague exchange terms inviting disputes | Specify time, place, transportation, and a no-show protocol |
| No dispute-resolution mechanism | Require mediation/PC before returning to court |
| Ignoring travel/relocation and ROFR | Add notice rules and a right-of-first-refusal threshold |
| Plan a third party couldn't follow | Make every provision operationally clear and unambiguous |
| Inventing the required parenting-plan form | Use [CITE]/[NEED] placeholders |
