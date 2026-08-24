---
title: "Supervised Visitation and Safety Plan"
category: legal/custody
description: "Design supervised or safety-conditioned parenting time: select the supervision level (professional, agency, therapeutic, or designated-family supervisor), specify location/duration/frequency and cost allocation, set conduct and safety conditions (no substances, no removal, approved topics), define a step-up/reunification pathway tied to objective milestones, and draft the order language — proportionate to the documented risk and anchored to the child's safety and best interests."
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
  - supervised-visitation
  - safety-plan
  - reunification
updated: "2026-06-01"
related_prompts:
  - domain-legal/custody/legal_custody_best_interests_analysis.md
  - domain-legal/custody/legal_temporary_and_emergency_custody_motion.md
  - domain-legal/custody/legal_high_conflict_parenting_coordination_provisions.md
  - domain-legal/divorce/legal_domestic_violence_protective_order_petition.md
  - domain-legal/custody/legal_parenting_plan_drafter.md
---

**Purpose:** Design a supervised or safety-conditioned parenting-time arrangement that protects the child while preserving the parent-child relationship where appropriate, with a concrete step-up pathway toward less restrictive contact tied to objective milestones. Output is a supervision/safety plan and order language proportionate to the documented risk, anchored to the child's best interests.

**When to use:** A parent's contact must be supervised or conditioned due to documented risk (abuse, substance use, untreated mental illness, abduction risk, re-introduction after absence); designing a reunification pathway; responding to a request for supervision.

---

## Your Input

- **Jurisdiction:** [State; supervised-visitation provisions and provider standards; whether the court orders or approves supervisors `[CITE: …]`]
- **Risk basis:** [The documented risk — abuse, neglect, substance use, mental illness, abduction risk, prolonged absence — with evidence]
- **Child(ren):** [Ages, needs, comfort with the parent, prior relationship]
- **Supervision options available:** [Professional supervisor, supervised-visitation agency/center, therapeutic supervision, or a designated family member]
- **Logistics:** [Proposed location, duration, frequency, who supervises, cost and who pays]
- **Conditions needed:** [No substances/testing, no removal, approved topics, no discussion of the case, no recording]
- **Step-up goals:** [Milestones for reducing restriction — clean tests, completed treatment, demonstrated stability]
- **Safety overlay:** [Any protective order; exchange safety]

---

## Constraints

**Must:**
- Tie the supervision level and conditions to the **documented risk** and make them **proportionate** — the least restrictive arrangement that protects the child.
- Select an appropriate **supervision level** (professional/agency/therapeutic/designated family) with the provider's qualifications and a neutral designation; specify **location, duration, frequency, cost, and cost allocation**.
- Specify **conduct and safety conditions** (sobriety/testing, no removal from the site, approved topics, no disparagement of the other parent, no discussion of the litigation, no unauthorized recording or third parties).
- Define a **step-up / reunification pathway** with **objective, measurable milestones** (e.g., negative tests over a period, completion of a treatment program, an interval without incident) and the mechanism to advance — avoiding indefinite supervision without a path.
- Coordinate with any **protective order** and ensure **exchange safety**.
- Keep the plan **child-centered**, including the child's comfort and a therapeutic component where re-introduction is involved.
- Provide **order language** the court can adopt.
- Use placeholders `[CITE: ...]`, `[NEED: ...]` for unsupplied authority or facts.

**Must Not:**
- Impose restrictions disproportionate to the risk or use supervision punitively.
- Leave supervision open-ended with no step-up criteria.
- Designate a supervisor who is partial or unqualified for the risk involved.
- Ignore a protective order or create unsafe exchanges.
- Invent provider standards or the state's supervised-visitation rules.
- Insert generic "consult counsel" disclaimers.

---

## Instructions

1. **Risk-to-restriction match.** State the documented risk and select the proportionate supervision level.
2. **Provider & logistics.** Designate the supervisor type/qualifications; set location, duration, frequency, cost, and allocation.
3. **Conditions.** Specify sobriety/testing, no-removal, approved topics, anti-disparagement, no recording/third parties.
4. **Step-up pathway.** Define objective milestones, the review mechanism, and the progression to less restrictive contact.
5. **Safety coordination.** Integrate any protective order and safe exchange logistics.
6. **Therapeutic component.** Add reunification therapy where re-introduction is involved.
7. **Order language.** Draft adoptable provisions.

---

## Output Format

```markdown
SUPERVISED VISITATION & SAFETY PLAN — {Child(ren)}
**State:** {…} [CITE: …]   **Documented risk:** {…}

1. SUPERVISION LEVEL. {Professional / agency / therapeutic / designated family}; supervisor: {name/qualifications}; rationale (proportionate to risk): {…}.

2. LOGISTICS. Location: {…}; duration {…}; frequency {…}; cost {…} paid by {…}.

3. CONDITIONS. {Sobriety + testing}; no removal from the supervised site; approved topics only; no disparagement; no discussion of the case with the child; no recording or unauthorized third parties.

4. STEP-UP / REUNIFICATION PATHWAY.
   - Milestone 1: {e.g., {N} consecutive negative tests} → {extended supervised time}.
   - Milestone 2: {completion of {program}} → {monitored unsupervised / day visits}.
   - Review: {by whom / when}; regression triggers: {…}.

5. SAFETY COORDINATION. {Protective-order terms}; exchange: {neutral/curbside}; {no contact between parents}.

6. THERAPEUTIC COMPONENT. {Reunification therapy with {provider}, goals, reporting}.

[PROPOSED] ORDER. The Court orders supervised parenting time as set forth, subject to the step-up pathway and review on {date}.
```

---

## Verification

- [ ] Supervision level and conditions proportionate to the documented risk.
- [ ] Supervisor type/qualifications, location, duration, frequency, and cost allocation specified.
- [ ] Conduct/safety conditions enumerated (sobriety/testing, no removal, topics, no recording).
- [ ] Step-up/reunification pathway with objective milestones and a review mechanism — not open-ended.
- [ ] Protective-order coordination and safe exchanges addressed.
- [ ] Therapeutic component included where re-introduction applies.
- [ ] Order language adoptable.
- [ ] No disproportionate/punitive restrictions; no invented provider standards.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Open-ended supervision with no path off it | Define objective step-up milestones and a review date |
| Restrictions disproportionate to the risk | Use the least restrictive arrangement that protects the child |
| Designating a partial/unqualified supervisor | Match the supervisor's qualifications to the risk; ensure neutrality |
| Vague conditions | Specify sobriety/testing, no-removal, topics, recording, and third-party rules |
| Ignoring a protective order | Coordinate the plan with the order and safe exchanges |
| Using supervision punitively | Anchor to child safety and relationship preservation, not punishment |
| No therapeutic support for re-introduction | Add reunification therapy where the child needs it |
| Inventing the state's supervised-visitation standards | Use [CITE]/[NEED] placeholders |
| Milestones that are subjective | Make milestones measurable (tests, completion, time without incident) |
| Unsafe exchange logistics | Use neutral/curbside exchanges and limit parent contact |
