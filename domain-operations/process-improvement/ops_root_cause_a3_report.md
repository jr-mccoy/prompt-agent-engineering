---
title: "Root-Cause A3 Report — Background, Current Condition with Data, 5-Why and Fishbone, Countermeasures, Follow-Up"
category: operations/process-improvement
description: "Write a one-page A3 problem-solving report for an operational problem — a quantified gap, a current condition built from data rather than opinion, a fishbone to widen the search and a 5-why chain to deepen it, countermeasures matched to verified causes, and a follow-up plan that says how you will know the cause was right."
techniques:
  - RT-09
  - RT-05
  - DS-01
  - DS-02
  - QA-02
difficulty: intermediate
tags:
  - a3
  - root-cause
  - fishbone
  - five-whys
  - countermeasures
  - lean
updated: "2026-09-24"
related_prompts:
  - domain-operations/process-improvement/ops_process_map_and_waste_scan.md
  - domain-operations/process-improvement/ops_dmaic_project_charter.md
  - domain-engineering-workflows/workflows/engineering_post_mortem_root_cause_ladder.md
---

# Root-Cause A3 Report

**Objective:** Produce a one-page A3 that takes an operational problem from a
quantified gap to verified causes to countermeasures with owners — and states in
advance what result would prove the root cause wrong.

**When to Use:**
- A recurring operational problem (defects, mis-picks, late shipments, complaints)
  has a measurable gap between standard and actual.
- Previous fixes were "retrain" or "remind people" and the problem came back.
- You need a single page a manager can read in five minutes and challenge.
- **Not this prompt if** the problem is a software incident or outage — use
  `domain-engineering-workflows/workflows/engineering_post_mortem_root_cause_ladder.md`
  (blameless incident post-mortem with parallel 5-why threads). If the problem is too
  large or too variable for one A3 and needs a formal measure-analyze cycle, charter a
  project with `ops_dmaic_project_charter.md`. For anticipating failures that have not
  happened yet, use `domain-risk/risk_fmea_analysis.md`.

## Inputs / Context

1. **The problem as a gap**: standard or target, actual, since when, and the unit
   ("pick accuracy 99.6% target, 98.9% actual since week 15").
2. **Data**: counts by type, location, shift, product, or time — at least a Pareto-able
   breakdown. Raw records beat summaries.
3. **What changed** around the onset: people, method, material, machine, layout,
   volume, supplier.
4. **What has already been tried**, and what happened.
5. **Who owns the process** and who can approve countermeasures.

If there is no breakdown data, the first countermeasure is collecting it; the A3
says so rather than reasoning from anecdotes.

## Method

1. **Background and problem statement (DS-02).** Why this matters in business terms
   (cost, customer, safety), and the gap as a number with a unit and a date range. No
   cause and no solution in the problem statement.
2. **Current condition (RT-05).** Stratify the data — Pareto by type, then by where
   and when. Go and look: one observation at the point of occurrence is worth more
   than a meeting. The goal is to narrow to a **point of cause** (where and when the
   defect is created), not yet the root cause.
3. **Widen with a fishbone (DS-01).** For the narrowed problem only, list candidate
   causes under Method, Machine/equipment, Material, Measurement, People,
   Environment. Mark each candidate *verified*, *ruled out*, or *untested*, with the
   evidence.
4. **Deepen with 5-why (RT-09).** Only on verified causes. Each "why" must be a fact
   that can be checked; stop at a cause the team can change and that, if removed,
   would have prevented the problem. "Human error" is never a terminal why — ask why
   the process let the error through.
5. **Countermeasures.** One or more per root cause, each with owner, date, and the
   cause it addresses. Prefer error-proofing and design changes over instructions.
   Separate **containment** (stop the bleeding now) from **countermeasure** (remove
   the cause).
6. **Stress-test (QA-02).** For each root cause: what result after the countermeasure
   would show this was not the cause? Write that down before implementing.
7. **Follow-up.** Metric, check dates, target, and the rule for closing or reopening
   the A3.

## Output Format

```
# A3 — [problem title]         Owner: [..]   Date: [..]   Version: [..]

## 1. Background
## 2. Problem statement   (target | actual | unit | since)
## 3. Current condition   (Pareto, stratification, point of cause)
## 4. Cause analysis
Fishbone: | Category | Candidate | Status | Evidence |
5-why:    Why 1 → ... → root cause (changeable, preventive)
## 5. Countermeasures
| Type (contain/counter) | Action | Root cause addressed | Owner | Due |
## 6. Disconfirming result   (what would prove us wrong)
## 7. Follow-up
| Metric | Check dates | Target | Close / reopen rule |
```

## Verification

- [ ] The problem statement contains a number, a unit, and a date range — and no cause.
- [ ] The Pareto categories sum to the total.
- [ ] Every fishbone candidate has a status and evidence.
- [ ] 5-why ends at a changeable cause, not "human error" or "lack of training".
- [ ] Every countermeasure maps to a stated root cause.
- [ ] A disconfirming result is written for each root cause.
- [ ] Follow-up has dates and a close/reopen rule.

## False-Positive Prevention

1. **Solution in disguise.** "The problem is we don't have a scanner" is a proposal.
   Restate as the gap it would close.
2. **Fishbone as brainstorm output.** A diagram of 30 untested candidates is not
   analysis. Status every candidate; the A3 acts only on verified ones.
3. **Stopping at the person.** "Picker grabbed the wrong item" is the symptom. The
   root cause lives in why the process made the wrong item easy to grab and failed
   to catch it.
4. **Going past the actionable.** 5-why that ends at "the market is competitive"
   has gone too far. Stop at the deepest cause you own.
5. **Retraining as the countermeasure.** Training fixes a knowledge gap only. If the
   people already knew the right way, training changes nothing.
6. **Declaring victory on one good week.** Regression to the mean produces a good
   week after a bad one without any intervention. Hold the check for the stated period.
7. **Confusing containment with correction.** 100% re-inspection stops escapes but
   removes no cause; label it containment and give it an end date.

## Example Output

```
# A3 — Mis-picks in fast-pick zone        Owner: DC ops manager   v2

## 1. Background
Mis-picks drive re-ships and credits; customer complaints about wrong items doubled.
## 2. Problem statement
Pick accuracy target 99.6%; actual 98.9% for weeks 15–20; ~42,000 lines/week.
Errors ≈ 462/week vs. 168 at target.
## 3. Current condition
Pareto (wk 20, 462 errors): wrong SKU 268 (58%), wrong qty 125 (27%), missing 69 (15%).
Wrong-SKU errors: 211 of 268 in aisles 3–4 (fast-pick zone), all shifts.
Point of cause: aisles 3–4, at slot selection, since the week-14 re-slot.
## 4. Cause analysis
| Category    | Candidate                           | Status     | Evidence                      |
| Method      | re-slot put look-alike SKUs adjacent| Verified   | 9 of top 10 error pairs adjacent |
| Machine     | scan-verify skipped at damaged tags | Verified   | 31 slots with unreadable tags; override log |
| People      | new temps                           | Ruled out  | error rate same for temps/perm|
| Material    | supplier changed packaging          | Untested   | [check 3 SKUs]                |
5-why (wrong SKU):
 Why wrong item? → adjacent look-alike slots → re-slot optimized travel only →
 slotting rules have no look-alike separation rule → ROOT (changeable).
 Why not caught? → pickers override scan at damaged tags → no tag-replacement
 trigger → ROOT (changeable).
## 5. Countermeasures
| Contain | Second-person check, aisles 3–4, end date wk 23 | both   | Shift lead | wk 21 |
| Counter | Separate look-alike pairs by ≥1 slot           | rule   | Slotting   | wk 22 |
| Counter | Replace 31 tags; alert when override >3/day/slot| scan  | Maint.     | wk 22 |
## 6. Disconfirming result
If aisles 3–4 wrong-SKU errors stay >100/week after both changes, the root cause
is elsewhere (check the packaging candidate next).
## 7. Follow-up
| Pick accuracy | wk 23, 25, 27 | ≥99.5% | Close after 3 checks at target; reopen if <99.3% |
```

## Techniques Used

- **RT-09 Root Cause Explanation Pattern** — the 5-why chain on verified causes only.
- **RT-05 Evidence-Based Reasoning** — every candidate carries status and evidence.
- **DS-01 Framework Application** — the A3 structure and fishbone categories.
- **DS-02 Metric Specification** — the gap stated as target, actual, unit, and dates.
- **QA-02 Adversarial Stress-Test** — the disconfirming result written in advance.

## Related Prompts

- `ops_process_map_and_waste_scan.md` — the as-is map that often locates the point of cause.
- `ops_dmaic_project_charter.md` — when the problem needs a full DMAIC project.
- `domain-engineering-workflows/workflows/engineering_post_mortem_root_cause_ladder.md` — software incidents.
- `domain-risk/risk_fmea_analysis.md` — failure modes before they occur.
