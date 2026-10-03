---
title: "Repeat-Failure and Equipment Reliability Analysis — MTBF and MTTR Done Honestly, Failure-Mode Pareto, Trend Before Weibull, and RCM-Lite Task Selection"
category: operations/quality-safety
description: "Work out why a machine, pump, vehicle or component keeps failing: clean the work-order history into failures by mode and censored removals, compute MTBF and MTTR with the repair-time waterfall, rank failure modes by downtime hours, test whether failures are getting more frequent before reaching for Weibull (and state when Weibull is not valid), then run a reliability-centred-maintenance-lite decision on the top modes and set a verifiable target — distinct from OEE loss accounting (ops_oee_loss_analysis), from designing the whole PM program (ops_preventive_maintenance_program), and from a general root-cause A3."
techniques:
  - NE-11
  - DP-06
  - QA-04
  - RT-09
difficulty: advanced
tags:
  - reliability-engineering
  - mtbf
  - mttr
  - repeat-failures
  - weibull-analysis
  - reliability-centred-maintenance
  - same-machine-keeps-failing
  - equipment-breaks-down-often
  - how-reliable-is-this-machine
updated: "2026-10-03"
related_prompts:
  - domain-operations/quality-safety/ops_preventive_maintenance_program.md
  - domain-operations/quality-safety/ops_oee_loss_analysis.md
  - domain-operations/process-improvement/ops_root_cause_a3_report.md
---

# Repeat-Failure and Equipment Reliability Analysis

**Objective:** Turn a messy repair history into a clear account of how one asset (or
a fleet of identical components) fails — how often, how long it stays down and why,
which failure mode costs the most hours, whether it is getting worse — and into the
maintenance or design change most likely to stop it, with a target you can check.

**When to Use:**
- The same pump, motor, conveyor or vehicle keeps failing and each repair "fixes" it
  for a shorter time.
- Leadership quotes an MTBF and you are not sure what it means or whether it is
  trustworthy.
- You must choose between more PM, condition monitoring, a better spare-parts
  position, or a redesign for one problem asset.
- **Not this prompt if** you need all of a machine's lost time (setups, minor stops,
  speed, quality) — `domain-operations/quality-safety/ops_oee_loss_analysis.md`. To
  set strategies and schedules for a whole site, use
  `domain-operations/quality-safety/ops_preventive_maintenance_program.md`. Once the
  dominant failure mode is known and its physical cause needs a structured
  investigation, hand it to
  `domain-operations/process-improvement/ops_root_cause_a3_report.md`.

## Inputs / Context

1. **The asset or component population**: identical units, duty and operating
   context (speed, load, product, environment).
2. **Work-order history**: date, operating hours or cycles at event, failure mode
   as found, parts replaced, repair time — tagged `measured` (CMMS/run-hour meter)
   or `estimated` (reconstructed).
3. **Censored events**: units replaced before failure (planned), and units still
   running with their current hours.
4. **Repair-time detail**: time to detect, respond, diagnose, wait for parts,
   repair, and test, where available.
5. **Condition data**: vibration, temperature, pressure, oil analysis, if any.
6. **Changes**: modifications, supplier or part changes, process changes, with dates.

## Method

1. **Define failure and clean the data.** One written definition of failure (e.g.
   "leakage requiring shutdown"). Split by failure mode; separate planned removals
   (censored) from failures. Mixing modes is the commonest analytic error.
2. **Compute MTBF and MTTR (NE-11).**
   `MTBF = total operating time / number of failures` (by mode and overall);
   `MTTR = total repair time / number of repairs`;
   `Inherent availability = MTBF / (MTBF + MTTR)`.
   Break MTTR into a waterfall: detect, respond, diagnose, wait for parts, repair,
   test. Parts waits are often the largest piece and the cheapest to fix.
3. **Rank failure modes by downtime (DP-06).** Hours = failures × MTTR per mode.
   Name the mode that dominates and its share.
4. **Test for a trend before any distribution.** List the intervals between
   failures in order. Shortening intervals mean the system is **deteriorating** —
   something is progressively wrong and Weibull on the intervals is invalid. Use a
   cumulative-failures-versus-time plot or a trend test (Laplace or Crow-AMSAA
   for repairable systems).
5. **Weibull only when valid (QA-04).** For a non-repairable part with no trend,
   one failure mode, a homogeneous population, at least ~6–10 failures, and
   suspensions included: shape β < 1 suggests early-life failures (installation,
   quality), β ≈ 1 random, β > 1 wear-out. Report β with its uncertainty and the
   count; label the result indicative.
6. **Repeat-failure check.** Same mode on the same unit within 30 days (or a
   stated window) of a repair indicates repair quality or an unaddressed cause.
7. **RCM-lite on the top 1–3 modes.** Function → functional failure → failure mode →
   effect → consequence (hidden, safety/environmental, operational,
   non-operational) → task: condition-based if a warning is detectable, scheduled
   restoration or replacement if age-related, failure-finding if hidden, redesign if
   nothing else works, run-to-failure if consequence is minor.
8. **Root-cause hypotheses (RT-09).** For the dominant mode, list competing physical
   causes with the evidence that would discriminate between them; test the cheapest
   discriminator first.
9. **Target and verification.** Modeled MTBF/MTTR after the change, the date by
   which enough operating hours will have passed to check it, and the measure.

## Output Format

```
# Reliability analysis — [asset / component]   Period: [..]   Operating hours: [..]
Failure definition: [..]   Data: [measured / estimated]

## 1. Event table (failures by mode, censored removals)
## 2. MTBF / MTTR
| Mode | Failures | MTBF (h) | MTTR (h) | Downtime (h) | Share |
Inherent availability: [..]
## 3. MTTR waterfall (dominant mode)
| Detect | Respond | Diagnose | Parts wait | Repair | Test |
## 4. Trend and distribution
Intervals in order: [..] → trend: [improving / none / deteriorating]
Weibull: [valid? β, n, caveats | not applied because ..]
## 5. Repeat failures within [window]
## 6. RCM-lite decision (top modes)
| Function | Functional failure | Mode | Consequence | Task | Interval |
## 7. Root-cause hypotheses and discriminating tests
## 8. Actions, modeled target, verification date
```

## Verification

- [ ] Failure is defined once and modes are separated before any statistic.
- [ ] Planned removals are treated as censored, not as failures.
- [ ] MTBF, MTTR and availability recompute from the event table.
- [ ] Interval trend is checked before any Weibull fit.
- [ ] Any Weibull result states n, β, uncertainty and validity conditions.
- [ ] Each RCM-lite task matches its consequence category and failure behaviour.
- [ ] Targets are labelled modeled with a verification date.

## False-Positive Prevention

1. **MTBF as a guaranteed interval.** An MTBF of 1,000 h does not mean the unit runs
   1,000 h; with a constant failure rate, about 63% fail before the mean.
2. **Few failures, false precision.** Three failures give a very wide MTBF range;
   say so.
3. **Weibull on a deteriorating system.** Shortening intervals violate the
   identical-and-independent assumption; the β is meaningless.
4. **Mixed modes.** Seal leaks and bearing seizures pooled give a curve that
   describes neither.
5. **Planned replacements counted as failures.** Inflates the failure rate and
   hides wear-out.
6. **"Replaced part, fixed."** A repeat within weeks says the cause is upstream of
   the part.
7. **Time-based PM for random failures.** If failures are not age-related, a fixed
   replacement interval spends parts without reducing failures.

## Example Output

```
# Reliability analysis — Slurry transfer pump P-104 (single, no standby)
Period: 12 months   Operating hours: 8,200 [measured, run-hour meter]
Failure definition: any event requiring shutdown to repair.

## 2. MTBF / MTTR
| Mechanical seal leak | 6 | 1,367 | 9.5  | 57.0 | 65% |
| Bearing failure      | 2 | 4,100 | 14.0 | 28.0 | 32% |
| Coupling insert      | 1 | 8,200 | 3.0  | 3.0  | 3%  |
| All                  | 9 | 911   | 9.8  | 88.0 |     |
Inherent availability: 911 / (911 + 9.8) = 98.9%

## 3. MTTR waterfall — seal (9.5 h)
Detect 0.5 · Respond 1.0 · Diagnose 0.0 · Parts wait 4.0 (seal kits held at central
store, 120 km) · Repair 3.0 · Test 1.0

## 4. Trend
Seal intervals in order: 2,100 → 1,650 → 1,300 → 980 → 760 → 410 h. Deteriorating.
Weibull NOT applied: intervals are trending (not identically distributed) and n = 6.

## 5. Repeat failures (30 days)
1 of 6 (410 h ≈ 17 days after the previous repair).

## 6. RCM-lite — seal
Function: contain slurry up to 6 bar. Functional failure: visible leakage.
Mode: face wear from solids ingress. Consequence: environmental (spill) + operational
→ run-to-failure not acceptable. Task: condition-based — daily flush-water pressure
and flow log with low-flow alarm. Redesign option: slurry-duty cartridge seal.

## 7. Hypotheses and discriminating tests
H1 Flush-water pressure declining (supply line scaling) — flush log shows 3.2 → 1.9 bar
   over the year [measured, operator rounds] → consistent with shortening intervals.
H2 Shaft run-out from bearing wear — dial-indicator check at next stop (30 min).
H3 Installation error — 4 different fitters; no pattern by fitter.
Cheapest discriminator first: run-out check, then restore flush pressure.

## 8. Actions and target
1. Descale flush line, restore ≥ 3.0 bar, alarm < 2.5 bar.  2. Stock 2 cartridge
seals on site → seal MTTR 9.5 → 5.5 h (modeled).  3. Run-out check at next stop.
Modeled: seal failures ~4/yr (MTBF ~2,050 h, the first-interval level) → seal
downtime 57 → 22 h/yr. Verify after 4,000 operating hours (~6 months).
```

## Techniques Used

- **NE-11 Embedded Calculation Formulas** — MTBF, MTTR, availability and downtime by mode from the event table.
- **DP-06 Dominant Driver Identification** — the failure mode that owns most downtime, then its MTTR's biggest slice.
- **QA-04 Uncertainty Acknowledgment** — small-sample MTBF ranges and explicit Weibull validity conditions.
- **RT-09 Root Cause Explanation Pattern** — competing physical causes with discriminating tests.

## Related Prompts

- `domain-operations/quality-safety/ops_preventive_maintenance_program.md` — folding the chosen task into the site's PM program.
- `domain-operations/quality-safety/ops_oee_loss_analysis.md` — the full loss picture when breakdowns are only one loss.
- `domain-operations/process-improvement/ops_root_cause_a3_report.md` — the structured root-cause report for the dominant mode.
