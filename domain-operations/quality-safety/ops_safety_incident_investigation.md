---
title: "Safety Incident and Near-Miss Investigation — Facts First, Just-Culture Review, Systemic Causes, and Controls by the Hierarchy"
category: operations/quality-safety
description: "Investigate a workplace injury, near miss, or dangerous occurrence to learn and prevent recurrence: secure facts and a timeline with each item's source, compare work-as-done with work-as-imagined, trace causes to the system conditions that made the act likely, apply a just-culture test before any individual conclusion, and set controls by the hierarchy with an effectiveness check — drafted for review by a qualified safety professional and making no regulatory or legal determination."
techniques:
  - RT-09
  - RT-23
  - OC-10
  - DD-05
difficulty: advanced
tags:
  - incident-investigation
  - near-miss
  - just-culture
  - root-cause
  - workplace-safety
  - ehs
  - someone-got-hurt-at-work
  - near-miss-report
  - prevent-it-happening-again
updated: "2026-10-02"
related_prompts:
  - domain-operations/quality-safety/ops_job_hazard_analysis.md
  - domain-legal/employment-labor/legal_workplace_investigation_plan_and_report.md
  - domain-operations/process-improvement/ops_root_cause_a3_report.md
---

# Safety Incident and Near-Miss Investigation

> **Safety review required.** This prompt structures a *draft* investigation for
> learning and prevention. A qualified safety professional must review the findings
> and corrective actions before they are adopted. It makes **no regulatory
> compliance, reportability, or legal liability determination** — whether an event
> is recordable or reportable to a regulator, and any legal exposure, are decided by
> the employer's safety professional and counsel. Serious injuries and fatalities
> may require immediate regulator notification and scene preservation; do that first.

**Objective:** Produce an investigation report that establishes what happened from
sourced facts, explains why it made sense to the people involved at the time, names
the system conditions that allowed it, and sets controls that would have prevented it
— without blaming an individual by default or excusing reckless conduct.

**When to Use:**
- An injury, first-aid case, near miss, property damage, or dangerous occurrence
  needs an investigation.
- A near miss "almost" became serious and you want to learn before it does.
- Previous investigations ended in "worker did not follow procedure — retrained".
- **Not this prompt if** the matter is alleged **misconduct** — harassment,
  discrimination, retaliation, policy violation — use
  `domain-legal/employment-labor/legal_workplace_investigation_plan_and_report.md`
  (a findings-of-fact process about conduct, often under privilege). This prompt is
  about how work hurt or nearly hurt someone. If an investigation turns up deliberate
  sabotage or a criminal act, stop and route to HR and counsel. For a quality
  defect with no safety dimension, use `ops_root_cause_a3_report.md`. For a software
  outage, use `domain-engineering-workflows/workflows/engineering_post_mortem_root_cause_ladder.md`.

## Inputs / Context

1. **Event basics**: date, time, location, people involved, injury or potential
   injury, equipment, immediate actions taken.
2. **Evidence**: photos, scene sketch, equipment state, data logs, CCTV, permits,
   maintenance and training records.
3. **Statements** from the involved person(s) and witnesses, taken separately and soon.
4. **The written procedure or JHA** for the task, and how the task is actually done.
5. **Prior incidents and near misses** on the task or equipment.

## Method

1. **Immediate response check.** Confirm care given, scene made safe, evidence
   preserved, and notifications started by the responsible person. The prompt
   records these; it does not decide reportability.
2. **Facts and timeline with provenance (RT-23).** Each fact carries its source:
   `[physical]` (equipment, scene, log), `[record]` (permit, training file),
   `[statement: who]`, or `[inference]`. Conflicting statements are recorded side by
   side, not reconciled by the investigator's preference.
3. **Work-as-imagined vs. work-as-done.** Compare the procedure to what people
   actually do, and ask why the difference exists (time pressure, tool missing,
   procedure unworkable). The gap is a finding about the system.
4. **Causal analysis (RT-09).** Trace from the event: the immediate cause (the
   energy release or contact), the failed or absent barriers, and the underlying
   conditions (design, maintenance, staffing, scheduling, supervision, procedures,
   training design). Use 5-why or a causal tree; each link must be supported by a
   sourced fact. Stop at conditions the organisation can change.
5. **Just-culture test before any individual conclusion.** For any individual action
   in the chain, ask in order: was it intended to cause harm (sabotage)? Was the
   person impaired? Did they knowingly take an unjustifiable risk (reckless)? Would
   another similarly trained person in the same situation have done the same
   (substitution test)? Were there prior near misses or a known workaround? Most
   answers point to the system; a reckless or malicious finding goes to HR and is
   outside this report.
6. **Controls by the hierarchy.** For each underlying condition: elimination,
   substitution, engineering, administrative, PPE — with owner, due date, and the
   reason any higher level was rejected.
7. **Flag judgment items (DD-05)** for the safety professional: severity potential,
   reportability, exposure assessments, whether other sites have the same condition.
8. **Effectiveness check and sharing.** Define how and when each control will be
   checked as working (not just installed), and the lesson shared with similar sites.
9. **Mandatory review block (OC-10)** closes the report.

## Output Format

```
# Incident investigation (DRAFT) — [event]   Ref: [..]   Date of event: [..]
Type: [injury | first aid | near miss | property damage | dangerous occurrence]
Actual severity: [..]   Potential severity (reviewer to confirm): [..]

## Immediate response (recorded, not assessed)
## Timeline
| Time | Event | Source |
## Work-as-imagined vs. work-as-done
## Causal analysis
Immediate cause: [..]   Failed / absent barriers: [..]
Underlying conditions: | Condition | Supporting facts (sources) |
## Just-culture review
| Action | Intent | Impairment | Reckless? | Substitution test | Conclusion |
## Corrective and preventive actions
| Condition | Control | Hierarchy level | Owner | Due | Effectiveness check |
## Items for qualified judgment
## Lessons to share
## Review
This is a draft. A qualified safety professional must review it before adoption.
No regulatory compliance, reportability, or legal determination is made.
Reviewer: ________  Date: ________
```

## Verification

- [ ] Every timeline entry has a source tag; inferences are labelled.
- [ ] Conflicting statements are shown side by side.
- [ ] The work-as-done gap is explained, not only recorded.
- [ ] No causal link rests on an unsourced assertion.
- [ ] The just-culture test is completed before any individual conclusion.
- [ ] Each action maps to an underlying condition and states its hierarchy level.
- [ ] Each action has an effectiveness check, not just a completion date.
- [ ] The review block is present.

## False-Positive Prevention

1. **"Human error" as the cause.** It is where the investigation starts. Ask why the
   error was likely and why nothing caught it.
2. **Hindsight bias.** Knowing the outcome makes the risk look obvious. Reconstruct
   what the person could see and knew at the time.
3. **Retraining as the fix.** If the person knew the procedure, training changes
   nothing; fix the condition that made the shortcut attractive.
4. **Near misses downgraded.** A near miss with fatal potential deserves the depth of
   a serious injury. Rate potential, not only actual, severity.
5. **Investigation as discipline.** If reports feed discipline by default, near-miss
   reporting stops. Keep conduct matters on the HR/legal path.
6. **Closing on installation.** A guard installed but bypassed next month did not
   work. Check effectiveness.
7. **Reportability guessed.** Recordability and regulator notification rules are
   jurisdiction-specific; leave them to the safety professional.

## Example Output

```
# Incident investigation (DRAFT) — Forklift / pedestrian near miss, aisle 7   Ref: NM-2026-044
Type: near miss   Actual: no injury   Potential: fatal (crush) — reviewer to confirm

## Immediate response (recorded)
Area cordoned 10 min; forklift inspected (no defect); CCTV saved; supervisor notified 14:12.

## Timeline
| 14:05:10 | Picker exits aisle 7 end-cap on foot, looking at handheld | [physical: CCTV] |
| 14:05:12 | Forklift travelling 9 km/h crosses aisle 7 mouth           | [physical: telematics] |
| 14:05:13 | Forklift stops 0.8 m from picker                            | [physical: CCTV] |
| —        | Picker: "racking blocks the view, everyone steps out there" | [statement: picker] |
| —        | Driver: "I sounded the horn"; CCTV has no audio              | [statement: driver]; horn [unverified] |

## Work-as-imagined vs. work-as-done
Procedure: pedestrians use marked crossing at aisle 9. Done: pickers exit at aisle 7
because the pick path ends there and aisle 9 adds ~60 m per trip [inference from WMS route].

## Causal analysis
Immediate: pedestrian and forklift in same space with no sightline.
Failed/absent barriers: no physical barrier at aisle 7 mouth; no convex mirror;
speed limit 8 km/h exceeded by 1 km/h [physical: telematics].
Underlying conditions: pick-path design ends at an uncontrolled crossing [record: WMS];
end-cap racking added in August blocks sightline [record: change log, no safety review];
two prior near misses at aisle 7 not trended [record: NM log].

## Just-culture review
| Picker exits at aisle 7 | no harm intent | none | no — common practice | others do same (6 of 8 pickers observed) | system |
| Driver at 9 km/h       | no harm intent | none | no — limiter not fitted | others same (telematics avg 8.7) | system |

## Corrective and preventive actions
| Uncontrolled crossing | Re-route pick path to end at aisle 9 | elimination | WMS lead | 20 Oct | CCTV sample: 0 exits at aisle 7 in 2 wks |
| Sightline             | Barrier + gate at aisle 7 mouth      | engineering | Facilities | 31 Oct | gate in place, not propped (weekly check) |
| Speed                 | Speed limiters 8 km/h in zone        | engineering | Fleet | 15 Nov | telematics max ≤ 8 |
| Change without review | Layout changes require safety sign-off | admin | Ops manager | 31 Oct | next 3 changes audited |

## Items for qualified judgment
Potential-severity rating; whether other DC aisles share the end-cap condition.

## Review
This is a draft. A qualified safety professional must review it before adoption.
No regulatory compliance, reportability, or legal determination is made.
Reviewer: ________  Date: ________
```

## Techniques Used

- **RT-09 Root Cause Explanation Pattern** — immediate cause → failed barriers → underlying conditions.
- **RT-23 Input Provenance Tagging** — every fact tagged physical, record, statement, or inference.
- **OC-10 Mandatory Disclaimer Pattern** — the review and no-determination block is structural.
- **DD-05 Human Review Flags** — severity, reportability, and spread questions routed to the reviewer.

## Related Prompts

- `ops_job_hazard_analysis.md` — updating the task's JHA with what the investigation found.
- `domain-legal/employment-labor/legal_workplace_investigation_plan_and_report.md` — misconduct investigations, a different process.
- `domain-operations/process-improvement/ops_root_cause_a3_report.md` — the same causal discipline for non-safety problems.
