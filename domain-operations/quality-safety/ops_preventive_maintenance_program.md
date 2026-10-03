---
title: "Preventive Maintenance Program Design — Asset Criticality, Run-to-Failure vs Time-Based vs Condition-Based Strategy, PM Task Lists, Schedule Compliance, and Backlog"
category: operations/quality-safety
description: "Design or reset a maintenance program for a plant, fleet or facility: rank assets by consequence of failure, choose run-to-failure, time- or usage-based PM, condition-based or predictive monitoring, or failure-finding tests per failure mode, write PM tasks with measurable acceptance limits, load the schedule against real technician hours, define schedule compliance and backlog in crew-weeks, and audit the ways PM compliance is reported without the work being done — distinct from OEE loss analysis (one asset's losses) and from repeat-failure reliability analysis (why one asset keeps failing)."
techniques:
  - DS-06
  - NE-11
  - QA-21
  - RT-23
difficulty: intermediate
tags:
  - preventive-maintenance
  - predictive-maintenance
  - asset-criticality
  - maintenance-strategy
  - pm-compliance
  - maintenance-backlog
  - cmms
  - maintenance-schedule-for-equipment
  - stop-machines-breaking-down
  - too-much-firefighting-maintenance
updated: "2026-10-03"
related_prompts:
  - domain-operations/quality-safety/ops_oee_loss_analysis.md
  - domain-operations/quality-safety/ops_repeat_failure_reliability_analysis.md
  - domain-risk/risk_fmea_analysis.md
---

# Preventive Maintenance Program Design

**Objective:** Replace "fix it when it breaks, service it when someone remembers"
with a program in which every asset has a deliberate strategy matched to its
criticality and failure behaviour, every PM task is specific enough to check, the
schedule fits the hours the crew actually has, and compliance and backlog are
measured honestly.

**When to Use:**
- Most maintenance hours go to breakdowns and the PM list is a copy of OEM manuals
  nobody completes.
- You are setting up or cleaning up a CMMS and need the strategy before the data
  entry.
- PM compliance is reported at 95% but the same machines keep stopping.
- The backlog keeps growing and leadership asks whether to hire.
- **Not this prompt if** you need to know where one machine's capacity is going —
  use `domain-operations/quality-safety/ops_oee_loss_analysis.md`. If one asset or
  component keeps failing and you need the failure pattern and cause, use
  `domain-operations/quality-safety/ops_repeat_failure_reliability_analysis.md`. A
  formal design or process FMEA is `domain-risk/risk_fmea_analysis.md`. Home upkeep
  is `domain-productivity/home-life/home_seasonal_maintenance_calendar.md`.

## Inputs / Context

1. **Asset register**: assets, location, age, redundancy, whether each is on the
   constraint or a single point of failure.
2. **Failure history**: 12–24 months of corrective work orders with downtime and
   cost; tag `measured` (CMMS/MES) or `estimated` (memory).
3. **Current PM**: tasks, intervals, and their source (OEM, habit, regulation).
4. **Crew**: technicians, shifts, skills, and hours actually available for work
   orders after meetings, training, travel and breaks.
5. **Backlog**: open work orders with estimated hours and age.
6. **Statutory and safety inspections**: pressure systems, lifting equipment, fire
   systems, safety interlocks — listed so they are scheduled, not redesigned.

## Method

1. **Rank criticality (DS-06).** Score consequence of failure on safety and
   environment, production (constraint? redundancy? hours to recover), quality, and
   repair cost. Any credible safety or environmental consequence makes an asset
   class **A** regardless of other scores. Then A / B / C.
2. **Choose a strategy per dominant failure mode.**
   - **Run-to-failure**: failure is evident, consequence small, repair quick, spare
     on hand. Not allowed for A assets' safety functions.
   - **Time- or usage-based PM**: only where failure is age-related (wear, fatigue,
     corrosion) — most failures in complex equipment are not, so fixed overhauls can
     add early-life failures.
   - **Condition-based / predictive**: vibration, thermography, oil analysis,
     ultrasound, motor current — where a detectable warning precedes failure (the
     P–F interval). Inspect at no more than half the P–F interval.
   - **Failure-finding**: test hidden functions (relief valves, standby pumps,
     interlocks) at an interval set by required availability.
   - **Redesign** when none of these is effective or affordable.
3. **Write tasks to a standard.** Each PM task states what to inspect or measure,
   the acceptance limit, the action if out of limit, tools, parts, skill, duration,
   and whether isolation/lockout is required. "Check pump" is not a task;
   "Measure bearing vibration at DE/NDE, alarm at 7.1 mm/s RMS" is.
4. **Load the schedule (NE-11).**
   `PM hours/week = Σ (task duration × frequency per week)`;
   `Available hours = technicians × shift hours × share available for work orders`.
   PM plus predictive work should fit with room left for corrective work; if not,
   cut low-value PM on C assets first.
5. **Define the measures.** **Schedule compliance** = PMs completed within their
   window / PMs due (window stated, e.g. ±3 days for monthly, ±10% of interval for
   longer). **Backlog** in crew-weeks = backlog hours / available hours per week.
   **Reactive share** = corrective hours / total work-order hours. **PM
   effectiveness** = failures on PM'd assets between PMs, and defects found by PM.
6. **Audit for compliance gaming (QA-21).** Pencil-whipped tasks with no readings,
   windows silently widened, deferred PMs closed as "done", A-asset misses averaged
   away by many C-asset completions. Report compliance by criticality class.
7. **Plan the transition.** Pilot on A assets, purge obsolete backlog, set a review
   of intervals after 6 months of data. Label all improvement figures modeled.

## Output Format

```
# PM program — [site]   Assets: [n]   Crew: [n techs, hrs available/wk]
Inputs: [measured / estimated]

## 1. Criticality
| Asset | Safety/env | Production | Quality | Cost | Class |
## 2. Strategy by asset and failure mode
| Asset | Failure mode | Age-related? | Warning detectable (P–F)? | Strategy | Interval |
## 3. PM task standard (sample tasks)
| Task | Measure / acceptance | If out of limit | Duration | Skill | Isolation? |
## 4. Schedule load
PM + PdM [..] h/wk vs available [..] h/wk → [..]% of capacity
## 5. Measures and definitions
Compliance window · backlog crew-weeks · reactive share · PM effectiveness
## 6. Compliance-gaming audit
## 7. Transition plan (modeled results, review date)
## Qualified-review items (statutory inspections, isolation procedures)
```

## Verification

- [ ] Every A asset has a strategy per dominant failure mode, not one blanket interval.
- [ ] Time-based PM is used only where the failure mode is age-related.
- [ ] Condition-monitoring intervals are at most half the P–F interval.
- [ ] Every PM task has a measurable acceptance limit.
- [ ] Schedule load arithmetic recomputes against stated available hours.
- [ ] Compliance is reported by criticality class with its window defined.
- [ ] Statutory inspections and isolation procedures are listed for qualified review.

## False-Positive Prevention

1. **OEM interval as strategy.** Manufacturer intervals are conservative and
   generic; they ignore your duty cycle and failure history.
2. **More PM is always better.** Intrusive overhauls disturb working equipment and
   can cause failures; do only PM that addresses a known failure mode.
3. **Compliance without evidence.** A ticked box with no reading recorded is not a
   completed inspection.
4. **Blended compliance.** 92% overall can hide 60% on the eight assets that matter.
5. **Backlog in work-order count.** 300 small jobs and 30 large ones are not
   comparable; use hours and crew-weeks.
6. **Modeled reliability as achieved.** Fewer breakdowns are a forecast until 6–12
   months of work orders show them.
7. **Redesigning regulated inspections.** Statutory intervals are set by the
   authority or inspector, not by this analysis.

## Example Output

```
# PM program — Injection-moulding plant, Line 2   Assets: 42   Crew: 6 technicians
Available: 6 × 40 h × 75% = 180 h/wk [measured: 8-week timesheet study]
Today: reactive 62% of hours [measured, CMMS]; PM compliance "91%" (no window);
backlog 820 h = 4.6 crew-weeks.

## 1. Criticality
A = 8 (4 presses on constraint, main chiller, main compressor, 2 press guards/interlocks)
B = 16 (robots, dryers, granulators)   C = 18 (conveyors with spares, fans, pumps with standby)

## 2. Strategy (A-asset sample)
| Press hydraulic pump    | bearing wear       | Partly | Yes, P–F ~12 wk [estimate] | Vibration + oil analysis | 4-weekly |
| Press heater bands      | burn-out           | No     | Thermography shows hot spots | Thermography + spares | Quarterly |
| Main chiller            | condenser fouling  | Yes    | Approach temp rises          | Time-based clean + log | Quarterly + weekly log |
| Main compressor         | wear (hours)       | Yes    | Partly                       | Usage-based (OEM 4,000 h) + vibration | 4,000 h |
| Press guard interlocks  | hidden fail-danger | —      | No (hidden)                  | Failure-finding test | Per safety assessment [qualified review] |
C conveyor gearboxes: run-to-failure, 2 spares stocked, 45 min swap.

## 3. Sample task
| Pump vibration route | DE/NDE velocity RMS; alert 4.5, alarm 7.1 mm/s [ISO 20816 zone for this machine class — verify] | Alarm → planned bearing change within 1 week | 20 min | Mech L2 | No |

## 4. Schedule load
A: 8 × 3.5 h = 28.0   B: 16 × 1.2 h = 19.2   C: 18 × 0.2 h = 3.6
PM + PdM 50.8 h/wk = 28% of 180 h → 129 h/wk left for corrective and projects.

## 5. Measures
Compliance window: ±3 days (≤ monthly), ±10% (longer). Re-baselined compliance on
A assets: 64% (was reported inside the 91% blend).
Target: A ≥ 90%, B ≥ 80% within 6 months. Backlog target ≤ 3 crew-weeks.

## 6. Compliance-gaming audit
38% of completed PMs had no recorded reading → those tasks now require a value.
Deferred PMs were closed as "complete — deferred": reclassified as missed.

## 7. Transition
Purge 140 h of obsolete work orders (reviewed by planner + supervisor); 2-week
contractor blitz 240 h → backlog 440 h = 2.4 crew-weeks.
Modeled: reactive share 62% → ~45% in 9 months (modeled — confirm from CMMS).
Qualified review: interlock test intervals and procedures; chiller refrigerant checks
by certified technician; compressor receiver statutory inspection stays on its schedule.
```

## Techniques Used

- **DS-06 Prioritization and Severity Guidance** — criticality classes decide strategy, compliance targets and where PM is cut first.
- **NE-11 Embedded Calculation Formulas** — schedule load, available hours, backlog in crew-weeks.
- **QA-21 Metric Gaming Vector Enumeration** — the ways PM compliance rises without maintenance improving.
- **RT-23 Input Provenance Tagging** — failure history and hours tagged measured or estimated; results labelled modeled.

## Related Prompts

- `domain-operations/quality-safety/ops_oee_loss_analysis.md` — where the asset's lost hours go, including breakdowns and minor stops.
- `domain-operations/quality-safety/ops_repeat_failure_reliability_analysis.md` — the failure pattern and cause when one asset keeps failing.
- `domain-risk/risk_fmea_analysis.md` — formal failure-mode scoring when the strategy needs a full FMEA.
