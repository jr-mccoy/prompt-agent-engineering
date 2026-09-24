---
title: "Career Ladder Framework — Levels Defined by Observable Scope, Parallel Tracks, and a Promotion Evidence Rule"
category: hr-management/people-ops
description: "Write a career ladder a manager can apply and an employee can act on: four to six observable dimensions, one anchored cell per level per dimension with a nameable difference between adjacent levels, parallel IC and management tracks with stated equivalence, a declared career level, and a promotion evidence rule, then test it by blind placement of real people — distinct from hr_compensation_banding (which prices the levels) and hr_performance_review_meta_prompt (which builds one cycle's review rubric from a level)."
techniques:
  - DP-03
  - CM-02
  - RT-05
  - QA-02
  - OC-03
difficulty: advanced
tags:
  - career-ladder
  - levelling
  - career-framework
  - promotion-criteria
  - dual-track
  - people-ops
  - getting-promoted
  - unclear-job-levels
  - promoted-by-tenure
updated: "2026-09-24"
related_prompts:
  - domain-hr-management/people-ops/hr_compensation_banding.md
  - domain-hr-management/performance-reviews/hr_performance_review_meta_prompt.md
  - domain-hr-management/performance-reviews/hr_calibration_facilitator.md
---

# Career Ladder Framework

**Objective:** Produce the level definitions an organisation promotes against: a small
set of observable dimensions, an anchored description for every level on every
dimension, parallel individual-contributor and management tracks, a declared career
level, and a written rule for what evidence a promotion requires. Ladders built from
tenure, from comparative adjectives alone, or with a top level nobody can reach are
refused.

**When to Use:**
- "What would I need to do to get promoted?" has no written answer.
- Two managers promote on visibly different bars.
- The only route above senior is managing people, and good engineers are becoming
  reluctant managers.
- You are about to build compensation bands and need the levels they will price.

**Distinct from:**
- `hr_compensation_banding.md` — prices the levels. Its Step 1 is a four-column
  summary; this prompt writes the full definitions that summary compresses.
- `../performance-reviews/hr_performance_review_meta_prompt.md` — takes one level as an
  input and builds a review rubric for one cycle. It consumes a ladder; it does not
  define one.
- `../performance-reviews/hr_promotion_case_writer.md` — applies this ladder to one
  person's evidence.

**When NOT to use:** you need a skills matrix for staffing or training (proficiency per
tool is not a level), or a one-off job description (`../hiring/hr_job_description_writer.md`).

---

## Inputs

1. **Function and headcount by current title** — the ladder has to fit real people.
2. **Existing levels or titles**, and how people are assigned to them today. Be honest if
   the answer is years of experience.
3. **Two or three people everyone agrees are clearly at a level**, per level. These are
   the calibration anchors.
4. **Whether a management track exists**, and at what level it starts.
5. **Constraints** — collective agreements, a parent company's framework, published
   levels you must map to.

If the requester cannot name anyone who clearly sits at a level, that level is
hypothetical. Mark it so rather than writing anchors for it from imagination.

---

## Method

1. **Choose four to six dimensions, each observable (CM-02).** Typical: scope of work,
   autonomy, ambiguity handled, impact radius, influence on others, craft depth. Each
   must be something a second manager could check from artefacts. "Ownership" and
   "maturity" fail that test; rewrite them as what an owner visibly does.

2. **Set the number of levels against headcount.** Four to six per track for most
   organisations under 200 people. A level that nobody occupies and nobody is expected
   to reach within two years is decorative; drop it or mark it reserved.

3. **Write one anchor per cell, with an example of evidence (DP-03, RT-05).** Each cell
   states a behaviour at that level and one example artefact that would demonstrate it.
   Then run the **difference test** on adjacent cells: name, in one phrase, what
   changes from level N to N+1. If the only difference is "more", "stronger" or
   "greater", the cell is not written yet.

4. **Build the parallel tracks and state equivalence.** Say where the management track
   begins, which IC level each manager level is equivalent to in scope and pay band,
   and that moving between tracks is a lateral move, not a promotion or demotion.

5. **Declare the career level.** The level at which someone may stay indefinitely with
   full performance ratings. Below it, state the expected progression window. Above
   it, say plainly that promotion is by business need as well as by readiness, so
   people are not promised a level that the organisation cannot create.

6. **Write the promotion evidence rule.** Promotion recognises sustained operation at
   the next level, not potential: state the minimum number of distinct examples (two or
   three is typical), the period over which they must occur, and that tenure is never
   itself evidence.

7. **Stress-test with blind placement (QA-02).** Two managers independently place six
   to ten current people using only the ladder. Record exact agreement and any
   disagreement larger than one level. Every disagreement is traced to a cell whose
   wording allowed both readings, and that cell is rewritten.

---

## Output Format

```markdown
## Career ladder — [function], [date]

### Dimensions
| Dimension | What it observes | Evidence a reviewer can check |
|---|---|---|

### IC track
| Level | [Dim 1] | [Dim 2] | ... | Difference from level below |
|---|---|---|---|---|

### Management track
| Level | Equivalent IC level | [Dim 1] | ... |
|---|---|---|---|

### Career level and progression
- Career level: [level] — may remain indefinitely
- Expected window below it: [months, stated as typical, not a deadline]
- Above it: [readiness + business need]

### Promotion evidence rule
[n distinct examples, over [period], at the next level's anchors; tenure is not evidence]

### Blind placement test
| Person (anonymised) | Manager A | Manager B | Gap | Cell that caused it | Rewrite |
|---|---|---|---|---|---|
Agreement: [x / n]; gaps > 1 level: [n]

### Hypothetical levels
[any level with no current occupant, marked]
```

---

## Verification

- [ ] Every dimension can be checked from artefacts by a second manager
- [ ] Every cell has a behaviour and an example of evidence
- [ ] Every adjacent pair of cells passes the difference test without "more" or "stronger"
- [ ] No cell mentions years of experience or time in role
- [ ] Management-track levels state an IC equivalent; track moves are lateral
- [ ] A career level is declared, and levels above it state the business-need condition
- [ ] The promotion evidence rule names a count and a period
- [ ] Blind placement was run on real people and every gap > 1 level led to a rewrite
- [ ] Unoccupied levels are marked hypothetical or reserved

## False-Positive Prevention

1. **Adjectives are not anchors.** "Strong technical judgement" at level 3 and "very
   strong" at level 4 will pass a read-through and fail the first contested promotion.
   Apply the difference test to every adjacent pair.
2. **Do not write the ladder from the current top performer.** A ladder describing one
   exceptional person's profile defines a level only they can reach, and it will be
   read as written for them.
3. **Tenure in scope language is still tenure.** Test each cell: could a strong person
   satisfy this in their first year? If the honest answer is "no, because it requires
   having been here", rewrite it.
4. **A management track that starts above the IC career level forces management as the
   only route up.** Check the equivalence table for that shape.
5. **High agreement on easy cases proves little.** Include at least two people whose
   level managers already argue about in the blind placement sample.
6. **Do not invent levels to create promotion opportunities.** A new level with no
   distinct scope inflates titles and breaks the pay structure that prices it.

**Legally careful, per this domain's standing principles.** Level definitions that
require availability, travel or "culture fit" can encode indirect discrimination.
State the business requirement behind any such criterion, or remove it.

---

## Example

**Context:** a 40-person engineering function. Headcount by the new levels: E1 4,
E2 12, E3 14, E4 6, E5 1, M1 3 (total 40). Dimensions: scope, autonomy, ambiguity,
influence, craft.

| Level | Scope | Difference from level below |
|---|---|---|
| E2 | A feature within a defined project | Delivers a scoped feature without step-by-step direction |
| E3 | A project end to end | Breaks down an unscoped project and sequences the work |
| E4 | A problem spanning two or more teams | Chooses which project should exist, and gets two teams to agree |

- **Management track:** M1 is equivalent to E4 in scope and band. Moving E4 → M1 is
  lateral.
- **Career level:** E3. People may stay at E3 indefinitely with full ratings. Typical
  progression E1 → E3 is 24–36 months, stated as typical, not a deadline. E5 (one
  person today) requires both readiness and a cross-org problem that exists.
- **Promotion evidence rule:** three distinct examples at the next level's anchors within
  the last 12 months.
- **Blind placement:** 8 people placed. 6 exact agreements, 2 one-level gaps, 0 larger
  gaps → agreement 6/8 = 75%. Both gaps sat on the E3/E4 *influence* cell, which read
  "influences decisions beyond the team". It was rewritten to "a decision in another
  team's roadmap changed because of their written proposal". A re-run on the same 8
  gave 8/8.
- **Hypothetical levels:** none. E5 has one occupant.

---

## Techniques Used

- **DP-03 Anchored Scoring Scales** — every cell is a behavioural anchor with an
  evidence example, not a label.
- **CM-02 Constraint Specification** — dimensions restricted to what a second manager can
  check; tenure language banned.
- **RT-05 Evidence-Based Reasoning** — the promotion rule requires a count and a period of
  evidence.
- **QA-02 Adversarial Stress-Test** — blind placement deliberately includes contested
  cases.
- **OC-03 Markdown Table Specification** — ladder, equivalence and test results as
  comparable tables.

## Related Prompts

- `hr_compensation_banding.md` — prices the levels this defines
- `../performance-reviews/hr_performance_review_meta_prompt.md` — builds a cycle's rubric from a level
- `../performance-reviews/hr_calibration_facilitator.md` — where ladder ambiguity surfaces as rating disputes
- `../performance-reviews/hr_promotion_case_writer.md` — applies the ladder to one person
- `hr_succession_planning.md` — uses the ladder's next-level anchors to judge readiness
