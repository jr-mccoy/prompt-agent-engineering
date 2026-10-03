---
title: "Job Hazard Analysis (JHA / JSA) — Task Steps, Hazards, Risk Rating, and Controls Chosen by the Hierarchy of Controls"
category: operations/quality-safety
description: "Draft a job hazard analysis for one task: break it into observed steps, identify the hazards at each step by energy source and exposure, rate risk before and after controls, and select controls by the hierarchy — elimination, substitution, engineering, administrative, PPE — with every draft marked for review by a qualified safety professional and no regulatory compliance determination made."
techniques:
  - DT-05
  - DS-01
  - OC-10
  - DD-05
difficulty: intermediate
tags:
  - job-hazard-analysis
  - jsa
  - hierarchy-of-controls
  - workplace-safety
  - risk-assessment
  - ehs
  - is-this-task-safe
  - safety-checklist-for-a-job
  - new-task-safety-review
updated: "2026-10-02"
related_prompts:
  - domain-operations/quality-safety/ops_safety_incident_investigation.md
  - domain-risk/risk_bow_tie_analysis.md
  - domain-operations/process-improvement/ops_standard_work_and_kaizen_event.md
---

# Job Hazard Analysis (JHA / JSA)

> **Safety review required.** This prompt produces a *draft* JHA for discussion. A
> qualified safety professional (e.g. the site EHS lead or a certified safety
> professional) must review and approve it before anyone performs the task under it.
> It makes **no regulatory compliance determination** — whether the task meets
> OSHA, HSE, or any other jurisdiction's requirements is decided by that reviewer and
> the employer, not by this output.

**Objective:** Produce a step-by-step hazard table for one job — what can hurt whom,
how badly, how likely — and a control plan that works down the hierarchy of
controls instead of defaulting to "wear PPE and be careful", ready for qualified review.

**When to Use:**
- A new task, new equipment, or a changed method is being introduced.
- A task has had injuries, near misses, or first-aid cases.
- A task is non-routine (maintenance, cleaning, line clearance) and has no written analysis.
- You are refreshing JHAs for training or before a standard-work change.
- **Not this prompt if** something has already happened and you need to find out why —
  use `domain-operations/quality-safety/ops_safety_incident_investigation.md`. For a
  single catastrophic top event with threats, consequences, and barriers (a
  process-safety view), use `domain-risk/risk_bow_tie_analysis.md`. For a
  product-or-process failure-mode analysis, use `domain-risk/risk_fmea_analysis.md`.
  Permit-required confined space, lockout/tagout procedures, process safety
  management, and hazardous-chemical exposure assessments need specialist programmes;
  this prompt flags them and stops.

## Inputs / Context

1. **The job**: name, location, equipment, materials, who does it, how often.
2. **Observed steps**: from watching the task done by an experienced worker, or video.
   Steps described from memory are tagged `estimated`.
3. **Incident and near-miss history** for this task and similar ones.
4. **Existing controls**: guards, interlocks, ventilation, procedures, PPE.
5. **Worker input**: what the people who do the job say is hard, awkward, or risky.
6. **Site risk matrix**, if one exists (otherwise a 5×5 is used and labelled).

## Method

1. **Break the job into steps (8–15).** Each starts with a verb ("lift lid",
   "remove guard"). Too few steps hide hazards; too many bury them.
2. **Identify hazards per step (DT-05).** For every step, sweep the energy sources and
   exposures: gravity (falls, falling objects), motion (caught-in, struck-by),
   mechanical (pinch, shear), electrical, pressure, thermal, chemical, biological,
   noise, radiation, ergonomic (force, posture, repetition), and environment (slips,
   lighting, heat). State the hazard as *source → contact → harm*.
3. **Rate inherent risk.** Severity (1 minor first aid … 5 fatality/permanent
   disability) × likelihood (1 rare … 5 almost certain), with the anchors written.
4. **Select controls by the hierarchy (DS-01).** For each hazard, ask in order:
   eliminate (remove the step or hazard), substitute (less hazardous material or
   method), engineering (guard, interlock, ventilation, lift assist), administrative
   (procedure, permit, rotation, signage, training), PPE. Record why each higher level
   was rejected if a lower one is chosen.
5. **Rate residual risk** with the controls in place and verified to exist.
6. **Flag specialist and judgment items (DD-05).** Separate what can be checked on the
   floor (guard present, interlock tested) from what needs a qualified judgment
   (exposure limits, structural capacity, electrical work category, confined-space
   classification). The latter go to the reviewer with the question stated.
7. **Mandatory review block (OC-10).** Every output ends with the review and
   no-compliance-determination statement and the reviewer sign-off fields left blank.

## Output Format

```
# JHA (DRAFT — not approved for use) — [job]   Location: [..]   Prepared: [..]

## Job description
Equipment / materials: [..]   Performed by: [..]   Frequency: [..]   Observed: [yes/no, date]

## Risk matrix used
Severity 1–5: [anchors]   Likelihood 1–5: [anchors]   Action threshold: [..]

## Hazard table
| # | Step | Hazard (source → contact → harm) | S | L | Inherent | Controls (hierarchy level) | S | L | Residual |

## Higher-level controls considered and rejected
| Hazard | Level rejected | Reason |

## Items needing qualified judgment
| Item | Question for reviewer |

## Specialist programmes triggered
[LOTO / confined space / hot work / working at height / chemical exposure — or none]

## Review
This is a draft. A qualified safety professional must review and approve it before
use. No determination of regulatory compliance is made.
Reviewer: ________  Role/qualification: ________  Date: ________  Approved: Y / N
```

## Verification

- [ ] Steps are observed (or tagged estimated) and each begins with a verb.
- [ ] Each step has an energy-source sweep; "none" is stated where none apply.
- [ ] Every hazard has inherent and residual ratings on the stated matrix.
- [ ] Every control names its hierarchy level; PPE-only controls show why higher levels were rejected.
- [ ] Specialist programmes are flagged, not written here.
- [ ] The review block and no-compliance statement are present and unsigned.

## False-Positive Prevention

1. **PPE as the first answer.** PPE is the last line; it fails silently. If the
   control column is mostly PPE, the analysis has not tried hard enough.
2. **"Be careful" as a control.** Awareness is not a control. Name the physical or
   procedural barrier.
3. **Residual risk without verification.** A control listed but not present, or a
   guard routinely removed, does not lower residual risk.
4. **Desk-written steps.** Steps written from the procedure miss the workarounds
   people actually use. Observe.
5. **Precise-looking scores.** A 12 vs 15 on a judgment matrix is not a measurement;
   use the bands to prioritise, not to rank finely.
6. **Treating a draft as approval.** This output is not authorisation to work.
7. **Compliance claims.** "Meets OSHA 1910.212" is a determination this prompt does
   not make; it lists the question for the reviewer instead.

## Example Output

```
# JHA (DRAFT — not approved for use) — Changing slitter blades, line 2   Prepared: 2026-10-01
Equipment: rotary slitter, 8 circular blades (Ø200 mm), blade holder, hand tools
Performed by: line technician   Frequency: 2×/week   Observed: yes, 30 Sep (1 change)

## Risk matrix used
S: 1 first aid … 3 lost-time … 5 permanent disability/fatality
L: 1 rare … 3 has happened here … 5 expected each time. Action if ≥ 10.

## Hazard table
| 1 | Stop line, isolate          | unexpected start → hand in blades → amputation | 5 | 2 | 10 | Lockout per site LOTO procedure, try-start verified (admin + engineering isolation) | 5 | 1 | 5 |
| 2 | Open blade guard            | stored energy in pneumatic guard → struck-by | 3 | 2 | 6 | Bleed valve with gauge, included in LOTO (engineering) | 3 | 1 | 3 |
| 3 | Loosen blade holder         | sharp edge → hand contact → laceration | 3 | 4 | 12 | Blade-handling tool keeps hands off edge (engineering); cut-resistant gloves A4 (PPE) | 3 | 2 | 6 |
| 4 | Remove and carry old blades | sharp edge + 1.2 kg each → laceration, drop on foot | 3 | 3 | 9 | Blade carrier case at machine (engineering); safety footwear (PPE) | 3 | 1 | 3 |
| 5 | Fit new blades, torque      | awkward reach 60 cm into frame → shoulder strain | 2 | 3 | 6 | Swing-out blade shaft (engineering) [verify feasible with OEM] | 2 | 1 | 2 |
| 6 | Close guard, remove lock    | other worker's hand in machine → crush | 5 | 1 | 5 | Walk-round check, individual locks (admin) | 5 | 1 | 5 |

## Higher-level controls considered and rejected
| 3 | Elimination (quick-change cassette pre-loaded offline) | capital request open; until then engineering + PPE |

## Items needing qualified judgment
| LOTO | Does the existing written procedure cover the pneumatic guard's stored energy? |
| Step 5 | Can the OEM shaft modification be made without affecting guarding? |

## Specialist programmes triggered
Lockout/tagout (steps 1, 2, 6) — site LOTO programme governs; not written here.

## Review
This is a draft. A qualified safety professional must review and approve it before
use. No determination of regulatory compliance is made.
Reviewer: ________  Role/qualification: ________  Date: ________  Approved: Y / N
```

## Techniques Used

- **DT-05 Element-by-Element Assessment Matrix** — every step swept against every energy source.
- **DS-01 Framework Application** — the hierarchy of controls applied in order, with rejected levels recorded.
- **OC-10 Mandatory Disclaimer Pattern** — the review and no-compliance-determination block is structural.
- **DD-05 Human Review Flags** — floor-checkable items separated from those needing qualified judgment.

## Related Prompts

- `ops_safety_incident_investigation.md` — when something on this task has gone wrong.
- `domain-risk/risk_bow_tie_analysis.md` — barrier analysis for one major top event.
- `domain-operations/process-improvement/ops_standard_work_and_kaizen_event.md` — writing the controls into the standard method.
