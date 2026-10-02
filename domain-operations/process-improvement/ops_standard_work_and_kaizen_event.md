---
title: "Standard Work and Kaizen Event — Takt Time, Work-Element Timing, Line Balance, and a Scoped 3–5 Day Event with a 30-Day Sustain Check"
category: operations/process-improvement
description: "Plan and run a kaizen event on one process: compute takt from customer demand, time work elements from observation, build the standard work combination sheet and operator balance chart, scope a 3–5 day event with a measurable target and a fixed team, and define the sustain audit that decides whether the new standard actually held."
techniques:
  - NE-11
  - CM-03
  - AG-40
  - DP-24
difficulty: intermediate
tags:
  - standard-work
  - kaizen
  - takt-time
  - line-balancing
  - lean
  - rapid-improvement-event
  - everyone-does-it-differently
  - improvement-week
  - make-the-fix-stick
updated: "2026-10-02"
related_prompts:
  - domain-operations/process-improvement/ops_process_map_and_waste_scan.md
  - domain-operations/process-improvement/ops_capacity_and_bottleneck_model.md
  - domain-professional-writing/business-writing/business_writing_sop.md
---

# Standard Work and Kaizen Event

**Objective:** Produce a kaizen event plan and the standard work it will install —
takt from demand, observed element times, a balanced allocation of work to
operators — with a target fixed in advance and a sustain audit that tests whether
the new method is still being followed 30 days later.

**When to Use:**
- A diagnosed process (you already know where the waste is) needs a focused week to fix it.
- Each operator or shift does the same job a different way and output varies with who is on.
- A cell or line is being rebalanced after a demand change.
- Past kaizen events produced a celebration and no lasting change.
- **Not this prompt if** you do not yet know where the time goes — map it first with
  `domain-operations/process-improvement/ops_process_map_and_waste_scan.md`. If the
  limit is a single overloaded resource rather than the work method, use
  `domain-operations/process-improvement/ops_capacity_and_bottleneck_model.md`. If the
  method is settled and you only need the written procedure, use
  `domain-professional-writing/business-writing/business_writing_sop.md`.

## Inputs / Context

1. **Customer demand** for the process: units per day or week, and its range.
2. **Available time** per shift: shift length minus breaks, meetings, planned
   maintenance.
3. **Work elements**: the steps of the job at a level you can time (5–60 s each),
   with at least 10 observed cycles per element. Tag `measured` (stopwatch/video) or
   `estimated`.
4. **Walk and wait** within the cycle; machine automatic time separately.
5. **Current state**: output, operators, WIP, defects, from the process map if one exists.
6. **Constraints**: safety requirements, union or HR rules for job changes,
   equipment that cannot move during the event.

## Method

1. **Takt (NE-11).** `takt = available time per period / customer demand per period`.
   Plan to a planned cycle time slightly below takt (typically 90–95%) to absorb
   variation, and say which you used.
2. **Time the elements.** For each element take the lowest *repeatable* time
   (not the single fastest) and note variation. Separate manual, walk, and machine
   time. Work content = sum of manual + walk.
3. **Operators needed.** `theoretical operators = total work content / takt`. Round
   up and show the fraction — 3.3 means three people plus a 0.3 problem to remove,
   not four people.
4. **Balance.** Allocate elements to operators so each loads close to the planned
   cycle time; draw the operator balance chart (load per operator vs. takt line).
   Put the remainder on the last operator so the waste is visible and targetable.
5. **Standard work documents.** Three: the **standard work combination sheet**
   (sequence, manual/walk/machine times per element), the **standard work chart**
   (layout with walk path and quality/safety check points), and **standard WIP**
   (minimum in-process stock to keep flow).
6. **Scope the event (CM-03, AG-40).** One process, one target, 3–5 days:
   - *Pre-event (2–3 weeks)*: charter, baseline data, team (5–8, including operators
     who do the job), materials and maintenance support booked.
   - *Day 1*: train, observe, time. *Day 2*: brainstorm and try. *Day 3*: implement
     and run. *Day 4*: refine, write standard work. *Day 5*: report out.
   - *Post-event*: 30-day action list with owners for anything not finished.
7. **Define done before the event (DP-24).** Target (e.g. output per labour hour,
   cycle time, WIP) with the measurement method, and the sustain audit: at 7, 14,
   and 30 days a leader observes three cycles against the standard work sheet and
   records adherence and the metric. Adherence below the threshold triggers
   rework of the standard, not discipline.

## Output Format

```
# Kaizen event — [process]   Dates: [..]   Sponsor: [..]   Facilitator: [..]

## Charter
Problem: [..]  Target: [metric, from → to, measured how]  Scope in/out: [..]
Team: [..]   Constraints: [..]

## Takt
Available time: [..]  Demand: [..]  Takt: [..]  Planned cycle time: [..]

## Element times (observed n= [..])
| # | Element | Manual | Walk | Machine | Variation | Notes |
Total work content: [..]   Theoretical operators: [..]

## Balance (current → proposed)
| Operator | Elements | Load (s) | vs. planned cycle time |

## Standard work set
Combination sheet ✓  Standard work chart ✓  Standard WIP: [..]

## Event schedule
| Day | Activities | Output |

## Done criteria and sustain audit
| Check | Day 7 | Day 14 | Day 30 | Threshold |

## 30-day action list
| Action | Owner | Due |
```

## Verification

- [ ] Takt uses available time net of breaks and planned downtime.
- [ ] Element times come from ≥10 observed cycles and state variation.
- [ ] Theoretical operators shows the fraction, not only the rounded number.
- [ ] Balance chart loads each operator against the planned cycle time.
- [ ] The target, measurement method, and sustain thresholds were set before the event.
- [ ] Operators who do the work are on the team.
- [ ] Any change to guarding, lifting, or equipment is flagged for safety review.

## False-Positive Prevention

1. **Fastest observed time as the standard.** A standard built on the best cycle
   will be missed most of the day. Use the lowest repeatable time.
2. **Takt confused with cycle time.** Takt is the demand rate; cycle time is what the
   process does. A process can be fast and still miss takt on variation.
3. **Rounding operators up silently.** 3.3 → 4 hides 0.7 of a person in idle time.
4. **Day-5 numbers as results.** Output during the event is under observation with
   extra support. The 30-day audit is the result; label day-5 figures as preliminary.
5. **Standard work as a binder.** If nobody audits it, it lapses. The sustain audit is
   part of the deliverable.
6. **Standard work as blame.** Non-adherence usually means the standard is wrong or
   impossible at real conditions. Fix the standard first.
7. **Headcount as the stated goal.** Events framed as headcount reduction lose the
   operators' knowledge. State where freed capacity goes.

## Example Output

```
# Kaizen event — Valve sub-assembly cell   Dates: 3–7 Nov   Sponsor: Plant manager

## Charter
Problem: 3 operators produce 380/day vs demand 420; overtime 6 h/week;
417 operator-seconds per unit (3 × 52,800 / 380).
Target: 420/day without overtime and ≤320 operator-s/unit, from MES counts over
20 production days. Out: leak-tester replacement (capital). Team: 3 cell operators,
manufacturing engineer, maintenance tech, quality tech, facilitator.

## Takt
Available: 2 shifts × (480 − 30 break − 10 meeting) = 880 min = 52,800 s
Demand: 420/day (range 390–450)   Takt: 52,800 / 420 = 125.7 s
Planned cycle time: 118 s (94% of takt)

## Element times (seconds; video, n=15 cycles, measured)
| # | Element                  | Manual | Walk | Machine | Variation | Notes                 |
| 1 | Get body, load fixture   | 24     | 6    | —       | ±3        |                       |
| 2 | Insert seat + spring     | 48     | —    | —       | ±12       | springs tangle in bin |
| 3 | Torque bonnet            | 36     | 4    | —       | ±3        |                       |
| 4 | Leak test                | 14     | 4    | 60      | ±2        | operator waits out cycle |
| 5 | Label, inspect           | 40     | —    | —       | ±4        |                       |
| 6 | Pack                     | 32     | 8    | —       | ±3        |                       |
| 7 | Fetch parts from stores  | —      | 64   | —       | ±25       | per unit, averaged    |
Total work content: 194 manual + 86 walk = 280 s
Theoretical operators: 280 / 118 = 2.37 → 2 people plus a 0.37 problem.
The third person exists to absorb waiting at the leak tester and walking to stores.

## Balance (current → proposed)
Current: Op1 = 1, 2, own fetch (100 s); Op2 = 3, 4 incl. 60 s wait, fetch (140 s);
Op3 = 5, 6, fetch (100 s). Op2 at 140 s sets output: 52,800 / 140 = 377/day ✓ matches 380.
Changes trialled day 2–3: springs pre-separated (element 2: 48 → 34 s);
leak tester set to auto-cycle so the operator loads and walks away (wait removed);
a water spider delivers parts to point of use (element 7 leaves the cell).
| Operator | Elements | Load (s)            | vs. 118 s |
| Op 1     | 1, 2, 3  | 30 + 34 + 40 = 104  | 88%       |
| Op 2     | 4, 5, 6  | 18 + 40 + 40 = 98   | 83%       |
Modeled capacity: 52,800 / 104 = 507/day. Third operator becomes water spider for
this and the adjacent cell (64 s × 420 = 26,880 s ≈ 51% of one person's 52,800 s) —
freed capacity, not a headcount cut. Modeled labour: (2 + 0.51) × 52,800 / 420 =
316 operator-s/unit. Day-5 output (preliminary): 431.

## Standard work set
Combination sheet ✓  Standard work chart (walk path, torque check point) ✓
Standard WIP: 1 at each fixture + 1 in leak tester = 3

## Event schedule
| Pre (3 wk) | charter, 20-day MES baseline, spring supplier contacted | baseline |
| Day 1 | train, video, time elements | element table |
| Day 2–3 | trial changes, run cell at 2 + spider | balance chart |
| Day 4 | write standard work, train both shifts | standard work set |
| Day 5 | report out to sponsor | 30-day list |

## Done criteria and sustain audit (fixed 14 Oct)
| Output ≥420/day (MES)     | d7 [measure] | d14 [measure] | d30 [measure] | 18 of 20 days |
| Operator-s per unit       | d7 [measure] | d14 [measure] | d30 [measure] | ≤320          |
| Adherence (3 cycles obs.) | d7 | d14 | d30 | ≥90% of elements in sequence and ±10% time |

## 30-day action list
| Spring supplier to ship pre-separated | Buyer | 30 Nov |
| Auto-cycle setting locked in tester PLC | Maintenance | 14 Nov |
| Water-spider route covering both cells | Cell lead | 14 Nov |
```

## Techniques Used

- **NE-11 Embedded Calculation Formulas** — takt, planned cycle time, theoretical operators, balance loads.
- **CM-03 Scope Definition** — one process, one target, explicit out-of-scope.
- **AG-40 Numbered Phase Discipline** — pre-event, five event days, post-event, each with an output.
- **DP-24 Done Fudge Prevention** — target and sustain thresholds fixed before day 1.

## Related Prompts

- `ops_process_map_and_waste_scan.md` — the diagnosis that tells you which process to kaizen.
- `ops_capacity_and_bottleneck_model.md` — when the limit is a resource, not the method.
- `domain-professional-writing/business-writing/business_writing_sop.md` — writing the procedure once the method is set.
