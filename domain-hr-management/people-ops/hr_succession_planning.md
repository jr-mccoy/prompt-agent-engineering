---
title: "Succession Planning — Critical Roles, Evidenced Readiness, and Emergency Cover Before Ambition"
category: hr-management/people-ops
description: "Build a succession plan for the roles that matter most: critical roles scored on impact and vacancy risk, emergency cover named for every one, successors rated ready-now / ready-in-1–2-years against next-level anchors with evidence rather than a 'high potential' label, a development action per successor, a bench-strength figure, and a slate-breadth check — distinct from risk_business_continuity_plan (keeping operations running through a disruption) and hr_calibration_facilitator (rating this cycle's performance)."
techniques:
  - RT-02
  - DS-06
  - DP-03
  - QA-04
  - OC-03
difficulty: advanced
tags:
  - succession-planning
  - talent-review
  - key-person-risk
  - bench-strength
  - leadership-pipeline
  - people-ops
updated: "2026-09-24"
related_prompts:
  - domain-hr-management/performance-reviews/hr_calibration_facilitator.md
  - domain-hr-management/performance-reviews/hr_performance_review_meta_prompt.md
  - domain-risk/risk_business_continuity_plan.md
---

# Succession Planning

**Objective:** Answer two questions for each role the organisation cannot afford to leave
empty. Who covers it next week if the holder leaves suddenly? Who could hold it
permanently, when, and what would get them there? Readiness is judged against written
anchors with evidence, emergency cover is named before long-term successors, and the
output is a bench-strength figure leadership can track. Plans that consist of a list of
"high potentials" with no evidence and no development action are refused.

**When to Use:**
- One departure would stall a function, and everyone knows which one.
- The board or investors have asked "what happens if [name] leaves?"
- A leader is planning to step back in the next two years.
- Talent reviews produce a 9-box grid and nothing changes afterwards.

**Distinct from:**
- `../../domain-risk/risk_business_continuity_plan.md` — keeps operations running through
  a disruption of any kind. This prompt covers the *people* dependency. Its emergency-cover
  column can feed that plan.
- `../performance-reviews/hr_calibration_facilitator.md` — rates performance in the
  current role this cycle. Succession asks about readiness for a *different* role, which
  is a separate judgement.
- `hr_career_ladder_framework.md` — defines the next-level anchors this plan uses to judge
  readiness.

---

## Inputs

1. **The org chart**, with tenure in role and any known departure intentions (retirement,
   stated plans).
2. **Candidate critical roles** proposed by leadership.
3. **Level anchors** for the successor roles, from the ladder or role descriptions.
4. **Evidence on candidate successors**: stretch work they have done, reviews,
   feedback. Evidence, not reputation.
5. **Who will see the plan.** It is confidential, and its distribution list is an input.

---

## Method

1. **Score roles, not people, first (RT-02).** For each candidate role, rate **impact if
   vacant** (1–3) and **vacancy risk** (1–3: flight risk, retirement horizon, market
   demand). Critical = product ≥ 6, or impact 3 on its own. Keep the list short. A plan
   with 30 critical roles in a 60-person company has not prioritised.

2. **Name emergency cover for every critical role.** The person who holds the role for 90
   days if the holder leaves tomorrow. They need not be the long-term successor. Record
   what documentation or access they would need, and whether they have it now.

3. **Rate successors against anchors (DP-03).** For each role, up to three candidates,
   each rated:
   - **Ready now** — already demonstrates the role's anchors, with evidence.
   - **Ready in 1–2 years** — demonstrates most anchors. Name the gap.
   - **Longer / not a successor** — say so rather than listing them to fill the grid.
   Each rating cites evidence against a named anchor. "High potential" is not a rating.

4. **Attach one development action per successor.** A specific stretch assignment,
   exposure or skill, with an owner and a date, aimed at the named gap. A successor with
   no development action is a hope.

5. **Compute bench strength and check slate breadth (DS-06, QA-04).** Bench strength = the
   share of critical roles with at least one ready-now or ready-in-1–2-years successor.
   Rank the gaps: critical roles with no successor first, then roles whose only
   successor is also the successor for another role. Check whether each slate draws only
   from the incumbent's own team or from people who resemble the incumbent. A narrow
   slate is a finding.

6. **Decide what is communicated.** People may be told they are being developed for
   broader scope. They should not be told they are "the successor", which is a promise
   the organisation cannot guarantee. Record the decision for each person.

---

## Output Format

```markdown
## Succession plan — [org], [date] · CONFIDENTIAL · distribution: [names]

### Critical roles
| Role | Holder | Impact (1–3) | Vacancy risk (1–3) | Score | Critical? |
|---|---|---|---|---|---|

### Emergency cover
| Role | Cover (90 days) | Needs access/docs to | Has them now? |
|---|---|---|---|

### Successors
| Role | Candidate | Readiness | Evidence vs anchor | Gap | Development action · owner · date |
|---|---|---|---|---|---|

### Bench strength
[roles with ≥1 ready-now or ready-in-1–2 successor] / [critical roles] = [x%]
Ranked gaps: [...]
Slate breadth: [finding]

### Communication
| Person | What they are told | By whom |
|---|---|---|
```

---

## Verification

- [ ] Roles were scored before any names were discussed
- [ ] Every critical role has named emergency cover, with an access and documentation check
- [ ] Every readiness rating cites evidence against a named anchor
- [ ] No candidate is listed only to fill a slot
- [ ] Every successor has one development action with an owner and date
- [ ] Bench strength is computed and shown with its components
- [ ] People who are the only successor for two or more roles are flagged
- [ ] Slate breadth was checked
- [ ] No one is promised a role

## False-Positive Prevention

1. **Performance in the current role is not readiness for the next one.** An excellent
   specialist may not be ready to lead the function. Rate against the target role's
   anchors.
2. **A 9-box position is not evidence.** Replace every "high potential" with the stretch
   work that demonstrated it, or downgrade the rating.
3. **Do not count the same person twice.** A successor named for three roles makes bench
   strength look healthy while covering only one departure.
4. **Emergency cover is not optional because a successor exists.** The long-term
   successor may need six months. The role needs someone on Monday.
5. **Self-similar slates are the common hidden gap.** If every successor came up through
   the incumbent's team, the plan reproduces the incumbent rather than preparing for the
   role.
6. **Do not share the plan casually.** A leaked succession list damages both the named
   and the unnamed. Distribution is an input for a reason.

**Legally careful, per this domain's standing principles.** Do not record health,
family plans or age-based retirement assumptions as vacancy risk. Use only what the
person has stated.

---

## Example

**Context:** 60-person company. Five roles scored critical.

| Role | Impact | Risk | Score | Emergency cover | Best successor | Readiness |
|---|---|---|---|---|---|---|
| CFO | 3 | 2 | 6 | Controller (has bank access; lacks board-deck history) | Controller | Ready in 1–2 years: gap is investor relations |
| Head of Engineering | 3 | 3 | 9 | Staff engineer A | Staff engineer A | Ready now: led a 2-team migration, ran hiring for a quarter |
| Head of Sales | 3 | 2 | 6 | Senior AE | — | No successor |
| Lead data engineer | 2 | 3 | 6 | Staff engineer A | Staff engineer A | Ready in 1–2 years |
| Head of Support | 3 | 1 | 3 | Support lead | Support lead | Ready now |

Head of Support is critical on impact 3 alone.

- **Bench strength:** 4 of 5 roles have a ready-now or 1–2-year successor = 80%. But staff
  engineer A covers two roles. Counting each person once, 3 distinct people cover 4 roles,
  so one departure opens two gaps.
- **Ranked gaps:** (1) Head of Sales has no successor. Action: the Senior AE runs pipeline
  forecasting for Q1 (owner: CEO, by 31 Mar). (2) Lead data engineer shares its successor
  with Head of Engineering. Action: a second data engineer takes ownership of the
  warehouse on-call (owner: Head of Engineering, by 15 Feb).
- **Slate breadth:** every engineering successor came from the platform team. Flagged for
  the next talent review.
- **Communication:** the Controller is told they are being developed toward investor
  relations. They are not told they are the CFO's successor.

---

## Techniques Used

- **RT-02 Multi-Dimensional Analysis Framework** — roles scored on impact and vacancy risk before people.
- **DS-06 Prioritization and Severity Guidance** — gaps ranked, with no-successor roles first.
- **DP-03 Anchored Scoring Scales** — readiness rated against written anchors with evidence.
- **QA-04 Uncertainty Acknowledgment** — "not a successor" allowed, and double-counting exposed.
- **OC-03 Markdown Table Specification** — roles, cover and successors as comparable tables.

## Related Prompts

- `../performance-reviews/hr_calibration_facilitator.md` — current-role performance, a separate judgement
- `../performance-reviews/hr_performance_review_meta_prompt.md` — role and level anchors when no ladder exists
- `../../domain-risk/risk_business_continuity_plan.md` — the wider continuity plan emergency cover feeds
- `hr_career_ladder_framework.md` — next-level anchors for readiness
