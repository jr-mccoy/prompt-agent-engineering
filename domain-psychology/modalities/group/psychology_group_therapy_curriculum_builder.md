---
title: "Group Therapy Curriculum Builder (Process or Psychoeducational)"
category: psychology/modalities/group
description: "Design a group therapy curriculum anchored to Yalom's therapeutic factors (process groups) and structured session-by-session skills design (DBT/CBT psychoeducational groups), producing a session curriculum table, group norms, and a screening/fit summary."
techniques:
  - ST-04
  - RT-02
  - DT-02
  - ED-04
  - QA-04
  - CM-02
difficulty: intermediate
tags:
  - group-therapy
  - Yalom
  - therapeutic-factors
  - psychoeducational
  - DBT-skills-group
  - CBT-group
  - cohesion
  - group-norms
intended_use: model-testing
updated: "2026-06-08"
related_prompts:
  - domain-psychology/populations/cross-population/psychology_group_therapy_member_screening.md
  - domain-psychology/modalities/behavioral-parent-training/psychology_behavioral_parent_training_module.md
  - domain-psychology/treatment-planning/psychology_smart_treatment_goal_generator.md
---

# Group Therapy Curriculum Builder (Process or Psychoeducational)

## Objective

Design a complete group therapy curriculum, anchored to **Yalom's therapeutic factors** for interpersonal/process groups (universality, instillation of hope, imparting information, altruism, corrective recapitulation of the primary family group, development of socializing techniques, imitative behavior, interpersonal learning, group cohesiveness, catharsis, existential factors) and to **structured session-by-session design** for psychoeducational/skills groups (e.g., DBT skills group format, CBT group). Output is a session-by-session curriculum table, an explicit group-norms block, and a screening/fit summary.

## When to Use

- Standing up a new process group, psychoeducational group, or skills group.
- Choosing between process vs structured formats for a presenting population.
- Planning open (rolling-admission) vs closed group structure.
- Building facilitation plans across Tuckman stages (forming → storming → norming → performing → adjourning).
- Designing measurement and screening pathways for a group offering.
- Not for use as the screening decision itself (use the member-screening prompt), and not a substitute for clinician judgment on suitability, risk, or curative-factor titration.

## Inputs / Context

- Group purpose and presenting concern (e.g., trauma-processing, DBT skills, depression CBT, interpersonal/process).
- Target population, age band, and severity/acuity.
- Format: process vs psychoeducational/skills; open/rolling vs closed; number of sessions and length.
- Setting (IOP/PHP, outpatient, telehealth) and co-facilitation availability.
- Inclusion/exclusion considerations and prior screening data.
- [clinician input required] — suitability thresholds, risk/exclusion criteria, and any program-mandated curriculum.

## Constraints

### Must

- Select and justify **group type** (process vs psychoeducational/skills) against the population and goals.
- For **process groups**, explicitly map which **Yalom therapeutic factors** the design cultivates and how (e.g., cohesion via norms, interpersonal learning via here-and-now feedback).
- For **psychoeducational/skills groups**, lay out a **session-by-session content sequence** (theme → objectives → activities → home practice), following a structured format (e.g., DBT skills modules; CBT psychoeducation → skill → practice arc).
- Define **inclusion/exclusion and screening** criteria and reference the member-screening prompt.
- Specify **open vs closed / rolling admission** and the implications for cohesion and content pacing.
- Provide explicit **group agreements/norms** (confidentiality, attendance, no-contact-outside or contact policy, feedback ground rules, safety/crisis plan).
- Build the **session arc** (check-in → content/theme → practice/here-and-now → check-out) and adapt across **Tuckman stages** (forming/storming/norming/performing/adjourning).
- Include **facilitation guidance** for the monopolizer, the silent member, conflict, and subgrouping; specify **co-facilitation roles**.
- Specify **outcome measurement** (named measures by name only, cadence, and what they track).

### Must Not

- Do not conflate process and psychoeducational formats without justifying the chosen structure.
- Do not invoke "Yalom's factors" generically without mapping specific factors to specific design choices.
- Do not omit inclusion/exclusion or screening linkage.
- Do not present a content sequence without objectives and home practice per session for skills groups.
- Do not fabricate normed cutoffs, program-specific module counts, or measure thresholds; mark as [clinician input required].
- Do not finalize norms or a crisis plan the facilitator cannot uphold.
- Do not ignore risk/exclusion (e.g., acute risk, severe interpersonal disruption) when defining fit.

## Instructions

1. Clarify purpose, population, and goals; select process vs psychoeducational/skills and justify.
2. Define open/rolling vs closed structure, number/length of sessions, and co-facilitation roles.
3. For process: map targeted Yalom therapeutic factors to concrete design and facilitation choices.
4. For psychoeducational/skills: sequence sessions (theme → objectives → activities → home practice).
5. Draft the group agreements/norms block, including a confidentiality, attendance, and crisis/safety provision.
6. Lay out the standard session arc and adapt facilitation across Tuckman stages.
7. Provide facilitation responses for the monopolizer, silent member, conflict, and subgrouping.
8. Define inclusion/exclusion and link to the screening prompt; summarize fit factors.
9. Specify outcome measures (by name), cadence, and tracking targets.
10. Note adaptations for telehealth, culture/language, and developmental level.

## Output Format

```
=== GROUP THERAPY CURRICULUM — DESIGN RECORD ===
Group name: [...]   Date: [YYYY-MM-DD]   Designer: [...]
Type: [Process / Psychoeducational-Skills]   Population: [...]   Age band: [...]
Format: [Open-rolling / Closed]   Sessions: [N x length]   Setting: [...]
Co-facilitation: [roles]

GROUP-TYPE SELECTION & RATIONALE
- Chosen type: [...]   Why (population/goals fit): [...]

THERAPEUTIC-FACTORS MAP (process groups)
Yalom factor                  | How the design cultivates it
------------------------------+------------------------------------------
Cohesion                      | [...]
Universality                  | [...]
Interpersonal learning        | [...]
Instillation of hope          | [...]
Altruism                      | [...]
[other targeted factors]      | [...]

SESSION-BY-SESSION CURRICULUM (skills/psychoeducational)
Session # | Theme/Module        | Objectives                | Activities/Exercises   | Home practice
----------+---------------------+---------------------------+------------------------+--------------
1         | [...]               | [...]                     | [...]                  | [...]
2         | [...]               | [...]                     | [...]                  | [...]
...       | [...]               | [...]                     | [...]                  | [...]

STANDARD SESSION ARC
Check-in [N min] → Content/Theme [N min] → Practice/Here-and-now [N min] → Check-out [N min]

STAGE PLAN (Tuckman)
- Forming: [norms, safety, goals]
- Storming: [conflict/here-and-now use]
- Norming: [cohesion building]
- Performing: [deeper work / skills generalization]
- Adjourning: [termination/relapse-prevention]

GROUP AGREEMENTS / NORMS
- Confidentiality: [...]
- Attendance / lateness: [...]
- Contact-outside policy: [...]
- Feedback ground rules: [...]
- Safety / crisis plan: [clinician input required]

FACILITATION PLAYBOOK
- Monopolizer: [...]
- Silent member: [...]
- Conflict / rupture: [...]
- Subgrouping: [...]

SCREENING / FIT SUMMARY
- Inclusion criteria: [...]
- Exclusion criteria / risk flags: [clinician input required]
- Screening pathway: see psychology_group_therapy_member_screening.md
- Fit notes per candidate type: [...]

MEASUREMENT PLAN
- Measures (by name): [...]
- Cadence: [pre / mid / post / per-session]
- Targets tracked: [...]

NOTES / ADAPTATIONS
- Telehealth / culture-language / developmental: [...]
- Open-question for clinician: [...]
```

## Verification

- [ ] Group type selected and justified against population/goals.
- [ ] Yalom therapeutic factors mapped to concrete design choices (process groups).
- [ ] Session-by-session curriculum table with theme, objectives, activities, and home practice (skills groups).
- [ ] Open/rolling vs closed structure and co-facilitation roles specified.
- [ ] Group-norms block includes confidentiality, attendance, contact policy, feedback rules, and crisis plan.
- [ ] Session arc and Tuckman-stage facilitation plan present.
- [ ] Facilitation responses for monopolizer, silent member, conflict, subgrouping included.
- [ ] Inclusion/exclusion defined and screening prompt referenced.
- [ ] Outcome measures named with cadence and targets.
- [ ] Program-specific cutoffs/module counts marked [clinician input required].
- [ ] No fabricated normed thresholds or measure cutoffs.
