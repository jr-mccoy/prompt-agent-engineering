---
title: "504 Plan Accommodation Menu"
category: education-teaching/instructor/student-support
description: "Generate a categorized menu of 504-style classroom accommodations matched to a student's documented impairment, ranked by leverage and feasibility — with implementation specifics and progress-monitoring notes."
techniques:
  - CM-01
  - ST-02
  - DS-01
  - OC-01
  - QA-01
difficulty: advanced
tags:
  - 504
  - accommodations
  - inclusive
  - special-education
  - access
  - adhd
  - anxiety
  - chronic-condition
updated: "2026-05-09"
related_prompts:
  - domain-education-teaching/instructor/student-support/teaching_iep_goal_writer.md
  - domain-education-teaching/instructor/student-support/teaching_udl_lesson_redesign.md
  - domain-education-teaching/instructor/student-support/teaching_behavior_support_planner.md
---

# 504 Plan Accommodation Menu

## Objective

Build a categorized menu of classroom accommodations appropriate for a student with a documented disability under Section 504 (US) or equivalent. Output is ranked by leverage and feasibility, with concrete implementation, who is responsible, and how progress will be monitored. Output is decision-support for a 504 team — not a substitute for clinical or legal judgment.

## When to Use

- Drafting or revising a 504 plan
- Initial referral conversation between teacher, parent, and counselor
- Refreshing a stale 504 plan after a year of implementation
- New teacher needs to translate a plan into daily practice
- Considering whether 504 supports may be sufficient (vs. IEP referral)

## When NOT to Use

- Building IEP goals — use `teaching_iep_goal_writer.md`
- Behavior intervention plan — use `teaching_behavior_support_planner.md`
- Whole-class universal design — use `inclusive_udl_lesson_redesign.md`

---

## Inputs Needed

- **Student grade and setting:** [Elementary / middle / high; gen-ed / co-taught]
- **Documented condition or impairment:** [As described by the team — e.g., ADHD, anxiety disorder, Type 1 diabetes, dyslexia, chronic migraines, post-concussion]
- **Major life activity affected:** [Per Section 504 — learning, concentrating, reading, communicating, eating, etc.]
- **Specific impacts in school:** [What the team has observed — e.g., difficulty with sustained attention; missed class for medical appointments; sensory overwhelm in cafeteria]
- **Current supports already in place:** [...]
- **Teacher / parent priorities:** [...]
- **Constraints:** [Resources, scheduling realities, technology]

---

## Instructions

### Step 1: Frame the Need

Restate the access need in functional terms — what the student needs to be able to do that is currently barriered:

> Because of [impact], the student currently cannot [reliably do X] in [setting Y]. The accommodation goal is to remove the barrier so the student can demonstrate learning at the same standard as peers.

Confirm this is an access issue (504) and not a specially-designed-instruction need (which would point to IEP). If unclear, flag for the team.

### Step 2: Categorize the Accommodation Menu

Generate options across these standard 504 categories. For each category, list 3–6 specific accommodations.

**Presentation accommodations** (how content is presented):
- [...]

**Response accommodations** (how the student responds):
- [...]

**Setting accommodations** (where and with whom):
- [...]

**Timing & scheduling accommodations:**
- [...]

**Organization & executive function supports:**
- [...]

**Behavioral / regulation supports** (when condition affects regulation):
- [...]

**Health-related accommodations** (if applicable):
- [...]

**Assessment accommodations** (specifically for tests, including state tests):
- [...]

### Step 3: Per-Accommodation Specification

For each candidate accommodation, output:

```
ACCOMMODATION: [Name]
─────────────────────────────────────────────
Category:           [Presentation / response / setting / etc.]
Targets impact:     [Which specific impact this addresses]
What it looks like: [Concrete: what the teacher does, what the student does]
Who is responsible: [Teacher / counselor / nurse / student / parent]
Materials needed:   [...]
Frequency / when:   [Always / specific subjects / specific tasks / as requested]
Leverage:           [High / Med / Low — based on impact removal]
Feasibility:        [High / Med / Low — based on classroom reality]
Stigma risk:        [Low / Med / High — visibility to peers]
Progress signal:    [What the team will look at to know it's working]
```

### Step 4: Rank and Recommend

Sort accommodations by **(leverage × feasibility) ÷ stigma risk**. Recommend a starter set of 4–8 accommodations, balancing across categories.

State the rationale: "We recommend starting with these because [combined coverage of impacts; sustainable for teacher; low stigma]."

Hold the rest as a "consider if starter set is insufficient" list.

### Step 5: Implementation Specs

For the starter set, produce a single-page implementation summary the teacher can reference daily:

| Accommodation | Trigger / when | Teacher action | Student action | Where documented |
|---------------|---------------|---------------|----------------|------------------|

### Step 6: Progress Monitoring Plan

Define how the team will know the plan is working:

| Indicator | Measurement | Cadence | Threshold for review |
|-----------|------------|---------|---------------------|
| [e.g., assignment completion] | [Tracker / gradebook] | Weekly | [< 70% triggers review] |
| [e.g., self-reported regulation] | [Brief student check-in] | Bi-weekly | [Pattern of overwhelm triggers review] |
| [e.g., attendance] | [Absence log] | Monthly | [Increase triggers review] |

Include a 6- to 8-week formal review point.

### Step 7: Communication Plan

- **To student:** how the plan will be explained; student voice in the plan
- **To family:** documentation, copy of plan, communication channel for issues
- **To teaching team:** how each teacher receives the plan, training if needed
- **Confidentiality:** who has access to what

### Step 8: Boundaries & Disclaimers

State explicitly:

> "This menu is decision-support for a 504 team meeting, not a legal opinion or clinical recommendation. Final accommodations should be selected by the team with the student, family, school counselor or 504 coordinator, and any treating clinician input. Local and state requirements may add or change required elements."

If the impacts described suggest the student may also need specially designed instruction, note: "Team may consider whether IEP evaluation is also appropriate."

---

## Output Format

1. Functional access-need statement
2. Categorized menu of candidate accommodations
3. Per-accommodation specification cards
4. Recommended starter set with rationale
5. Hold-list (consider if starter set insufficient)
6. Implementation summary (one-page)
7. Progress monitoring plan
8. Communication plan
9. Boundaries and disclaimers

---

## False-Positive Prevention

❌ **DON'T:**
- Treat 504 as "lower the standard" — accommodations remove access barriers, not standards
- Pile on accommodations the student doesn't need (overshoot causes stigma and stalls self-advocacy)
- Skip stigma audit — visibility matters at adolescence
- Confuse 504 (access) with IEP (specially designed instruction)
- Provide accommodations the team can't realistically implement

✅ **DO:**
- Frame in functional terms
- Rank by leverage × feasibility ÷ stigma
- Specify who is responsible for what
- Build in a review point
- Include the student's voice

---

## Quality Indicators

- [ ] Access need stated functionally
- [ ] Menu spans relevant categories
- [ ] Each accommodation specified with implementation details
- [ ] Starter set recommended and justified
- [ ] Progress monitoring plan includes review point
- [ ] Communication plan present
- [ ] Disclaimer about team authority included

---

## Techniques Used

| Technique | How It's Applied |
|-----------|-----------------|
| **CM-01** | Documented condition, impacts, setting, and constraints drive selection. |
| **ST-02** | Sequential frame → menu → spec → rank → implement → monitor. |
| **DS-01** | 504 framework (access, not modification) and standard accommodation categories structure choices. |
| **OC-01** | Per-accommodation card and implementation summary enforce reproducibility. |
| **QA-01** | Stigma audit, feasibility ranking, and disclaimer guard against over-prescription and scope creep. |
