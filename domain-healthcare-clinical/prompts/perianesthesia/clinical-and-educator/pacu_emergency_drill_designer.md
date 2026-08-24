---
title: PACU Emergency Drill Designer (MH, Anaphylaxis, Laryngospasm, Hemorrhage)
category: pacu/simulation
task_type: SIMULATE
audience: PACU educator, charge, or simulation lead designing a mock-code / emergency drill
updated: "2026-04-16"
tags:
  - pacu
  - simulation
  - emergency-drill
  - mock-code
  - crisis-management
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-02
  - ED-02
  - DS-06
difficulty: advanced
related_prompts:
  - prompts/pacu_simulation_scenario_builder.md
  - prompts/pacu_simulation_debrief_facilitator.md
  - prompts/pacu_red_flag_card.md
  - prompts/pacu_complication_deep_dive.md
  - prompts/pacu_skill_drill_designer.md
references:
  - MHAUS (Malignant Hyperthermia Association of the United States) — current MH protocol
  - AAAAI / WAO anaphylaxis guidelines
  - ASPAN Standards of Perianesthesia Nursing Practice — emergency response
  - Drain's PeriAnesthesia Nursing Practice (7th ed.) — crisis chapters
  - INACSL Healthcare Simulation Standards of Best Practice
---

# PACU Emergency Drill Designer

> Safety reminder: Drill design aid only. All doses, concentrations, cart contents, and activation codes in this output are illustrative placeholders; the running team follows current facility protocol, MHAUS hotline guidance, and pharmacy-supplied concentrations in real events.

## Objective

Produce a **mock-code / emergency drill script** for a PACU crisis scenario — malignant hyperthermia (MH), anaphylaxis, laryngospasm, or post-op hemorrhage. Output names team roles, equipment required, a time-based action checklist, cognitive-aid references, and post-drill debrief seeds. This is drill discipline (roles + time + equipment + escalation) layered on top of the scenario builder — not a replacement for bedside judgment.

## When to use

- Quarterly or semi-annual unit-wide emergency drills.
- After a near-miss for targeted team re-drill (use carefully — pair with `pacu_simulation_debrief_facilitator.md` for psychological safety).
- New-preceptor / new-staff orientation to unit crisis response.
- Pre-drill before a JCAHO / regulatory mock-code.

## When not to use

- For single-learner competency sims — use `pacu_simulation_scenario_builder.md`.
- For bedside skill-drill reps — use `pacu_skill_drill_designer.md`.
- For post-event root-cause analysis on a real crisis — facility RCA process only.

## Inputs

- **Emergency type:** {{malignant hyperthermia | anaphylaxis | laryngospasm | post-op hemorrhage | other per facility}}
- **Team size available:** {{nurses, RT, anesthesia, charge, pharmacy runner, scribe, observer(s)}}
- **Runtime:** {{10–20 min drill + 15–20 min debrief}}
- **Format:** {{in situ (on unit with real equipment) | lab-based (mannequin in sim room)}}
- **Known unit gaps (from prior drills or near-misses):** {{e.g., "MH cart location unclear," "dantrolene mixing slow," "role assignment unclear at start"}}
- **Cognitive-aid reference:** {{MHAUS hotline card + current MHAUS protocol, facility emergency-response flowchart, anaphylaxis algorithm per facility}}

## Audience / Scope

- **Primary user:** Drill designer (educator / charge / sim lead).
- **Participants:** Full PACU team + anesthesia + pharmacy runner + scribe.
- **Scope:** Unit-wide emergency drill for PACU. Does not substitute for certified crisis training (ACLS / PALS) or facility MH drill requirements per MHAUS.

## Output requirements

```markdown
# {Emergency type} — PACU Drill Script

> Safety reminder: Drill. All doses, concentrations, cart contents, and codes are illustrative. Live events follow facility protocol, MHAUS hotline (if MH), and pharmacy-supplied specifics.

## Drill Purpose & Learning Objectives (3 max)
1. ...
2. ...
3. ...

## Pre-Drill Briefing (5 min, before start)
- Confirm this is a drill — state aloud: "This is a drill. No real patient will be affected. We'll pause if a real emergency occurs."
- Orient to mannequin or in-situ setup; identify observers.
- Review roles and cognitive-aid location.
- Invoke psychological-safety framing: "We debrief behavior, not people; our goal is to find gaps in the system."

## Team Roles (assign before start)
| Role | Primary responsibility | Backup |
|---|---|---|
| Team leader (anesthesia by role, in a code) | Calls the code, assigns tasks, manages algorithm | Charge nurse |
| Airway | Positions, bag-mask ventilation, prepares for advanced airway | RT |
| Circulation | Compressions if indicated, IV access, fluid boluses per order | Secondary RN |
| Meds / pharmacy | Draws and delivers meds per order; tracks concentrations and timing | Pharmacy runner |
| Documentation / scribe | Timeline of events, meds, interventions, response | Charge or designated RN |
| Family liaison | Relocates family; communicates per facility | Social work / charge |
| Runner | Fetches equipment, MH cart, blood bank products | Any available |

## Equipment / Supplies Checklist (pre-drill verification)

### Generic items
- Crash cart with current code-blue drugs (per facility pharmacy).
- Bag-valve-mask + supplemental O2 delivery.
- Suction setup.
- IV start kit + large-bore IV supplies.
- Cognitive aid / algorithm card accessible.

### Emergency-specific items (pick list per emergency type)

**Malignant hyperthermia:**
- MH cart (dantrolene, sterile water, ice packs or cooling per facility protocol).
- MHAUS hotline card visible.
- Blood draw supplies (ABG, CK, electrolytes, lactate).
- Cooling supplies per facility.

**Anaphylaxis:**
- Epinephrine per facility protocol (generic; no specific concentration written here).
- Adjunct agents (H1/H2 blockers, corticosteroids) per facility protocol.
- Airway adjuncts (bag-valve-mask, advanced airway supplies).
- IV access + fluid bolus supplies.

**Laryngospasm:**
- Bag-valve-mask; anesthesia at bedside.
- Positive pressure capability (per anesthesia).
- Neuromuscular blocker per provider order (succinylcholine or rocuronium per order; doses per order).
- Advanced airway cart.

**Post-op hemorrhage:**
- Pressure / dressing supplies.
- Large-bore IV kits.
- Blood-bank request pathway identified; type-and-screen / type-and-cross per facility.
- Rapid-transfusion protocol reference (per facility massive-transfusion activation).

## Time-Based Action Checklist (minute-by-minute)

| Time | Cue / trigger | Expected team action | Cognitive-aid reference | Success marker |
|---|---|---|---|---|
| T+0 | Patient cue triggers drill (e.g., tachycardia + rising ETCO₂ for MH) | Team leader calls the emergency by name; assigns roles aloud | Algorithm / hotline card | All roles verbally assigned in ≤ 60 sec |
| T+1 | Initial assessment | Airway + circulation intervention begins; documentation starts | — | Interventions happen in parallel, not serial |
| T+2 | Escalation call | Activate facility code / rapid response; call MH hotline if MH | Facility activation code + MHAUS hotline for MH | Activation occurs ≤ 90 sec from trigger |
| T+3–T+5 | First-line meds / interventions per algorithm | Meds drawn and given per order; concentrations confirmed with pharmacy runner | Algorithm / protocol | Each med has time + dose + response charted |
| T+5–T+8 | Reassessment; second-line interventions if indicated | Team leader reassesses; adjusts plan per algorithm | — | Reassessment occurs on protocol-defined interval |
| T+8–T+15 | Resolution or escalation to ICU / OR / code | Transfer prep; blood products staged if indicated; family liaison deployed | Facility transfer pathway | Transfer criteria named; handoff SBAR ready |
| T+15 | Drill end | Freeze; transition to debrief | — | — |

## Cognitive Aids (referenced, not reproduced)
- **MH:** MHAUS emergency hotline card + MHAUS current protocol.
- **Anaphylaxis:** facility anaphylaxis algorithm (based on AAAAI / WAO guidelines).
- **Laryngospasm:** facility airway algorithm; anesthesia-led.
- **Hemorrhage:** facility massive-transfusion protocol + post-op bleeding pathway.

Do **not** reproduce specific doses, concentrations, or activation codes in this output — reference the cognitive aid by name, and confirm with pharmacy / anesthesia in the pre-drill briefing.

## Embedded Realism (optional)
- Radio chatter in hallway.
- Family member (SP) at bay entrance asking questions — tests family liaison.
- Second patient in adjacent bay with minor need — tests prioritization.
- Scribe operating from a rolling cart instead of a wall station.

## Post-Drill Debrief Seeds (hand off to `pacu_simulation_debrief_facilitator.md`)
- "Walk me through the first 60 seconds — when were roles assigned, and by whom?"
- "When did the team leader emerge, and was that clear to everyone?"
- "Where did the algorithm / hotline card get consulted, and by whom?"
- "What's the single system gap this drill surfaced?"
- {one emergency-specific question tied to the learning objectives}

## Drill Observer Checklist (for observer, not learners)
- [ ] Roles assigned verbally within 60 sec.
- [ ] Facility activation code called (MHAUS hotline if MH).
- [ ] Cognitive aid consulted during drill.
- [ ] Documentation / scribe captured interventions and times.
- [ ] Family liaison dispatched.
- [ ] Closed-loop communication used for orders.
- [ ] No freelancing outside scope.

## Sources / reference
- MHAUS — current MH emergency protocol.
- AAAAI / WAO anaphylaxis guidelines.
- Facility emergency-response algorithms: {{per facility protocol}}.
- ASPAN *Standards of Perianesthesia Nursing Practice* — emergency response.
- Drain's PeriAnesthesia Nursing Practice (7th ed.) — crisis chapters.
- INACSL Healthcare Simulation Standards of Best Practice.
```

## Must / Must not

**Must:**
- Name the emergency type explicitly in the title and purpose.
- Assign team roles before drill start; no "figure it out" role ambiguity.
- Reference cognitive aids by name (MHAUS card, facility anaphylaxis algorithm) without reproducing doses.
- Build a time-based action checklist with success markers observable by an outside observer.
- Include a family-liaison role and a documentation / scribe role — both are frequently under-assigned and critical.
- Pair the drill with `pacu_simulation_debrief_facilitator.md` for post-drill debrief.
- Identify observer role(s) and observer checklist separate from learner tasks.

**Must not:**
- Reproduce specific drug doses, concentrations, dilution volumes, or mixing instructions. These vary by pharmacy and change — always defer to current facility protocol and pharmacy-supplied specifics.
- Invent MHAUS hotline numbers, activation codes, or facility pager systems.
- Invent specific MH cart contents or drug quantities — facility MH cart inventories follow current MHAUS guidance.
- Write expected learner actions outside nursing scope — nurses assist with advanced airway and medication preparation per order; they do not intubate or give unordered medications.
- Invent blood-bank activation pathways, massive-transfusion protocol triggers, or transfusion lab cutoffs. Reference facility protocol.
- Include patient-identifying information (MRN, full name, full DOB, room number).
- Reference age, race, sex, disability, religion, national origin, pregnancy, license pathway, or prior unit as performance signals (clinically relevant pregnancy for anaphylaxis dosing is a **clinical** variable handled per order, not a performance signal).
- Substitute for required facility drills under regulatory mandate (e.g., MHAUS-recommended MH drills follow MHAUS cadence).
- Run a drill as punishment for a prior near-miss without psychological-safety framing.

## Quality signals

- Roles are verbally assigned within 60 sec of drill start.
- Cognitive aid is consulted, not bypassed.
- Documentation / scribe output is readable post-drill.
- Family liaison role is filled.
- Closed-loop communication is observable ("I'm giving the med per order now. Med given.").
- Debrief seeds are tied to system gaps, not individual blame.

## Verification

Before running the drill, verify the script:

- [ ] Names the emergency type and ≤ 3 learning objectives.
- [ ] Assigns all team roles in advance; backups named.
- [ ] Equipment checklist is verified with pharmacy / anesthesia for the emergency-specific items.
- [ ] Time-based action checklist has success markers observable by an outside observer.
- [ ] Family liaison + documentation / scribe roles assigned.
- [ ] Cognitive aid is referenced by name (not reproduced).
- [ ] Observer checklist is separate from learner tasks.
- [ ] Pre-drill briefing includes "this is a drill" statement and psychological-safety framing.
- [ ] Debrief handoff to `pacu_simulation_debrief_facilitator.md` seeded.

## False-Positive Prevention

Do **not** fabricate:

- **No invented drug doses, concentrations, dilutions, or mixing volumes.** These vary by pharmacy and change; defer to facility pharmacy and current cognitive aid.
- **No invented activation codes, overhead-page phrasing, or MHAUS hotline numbers.** Reference "per facility protocol" / "MHAUS hotline per current MHAUS card."
- **No invented MH cart contents, vial counts, or cooling-supply quantities.**
- **No invented massive-transfusion protocol activation thresholds or lab cutoffs.**
- **No invented facility codes (code blue, code red, rapid-response activation)** — every facility has its own.
- **No invented anaphylaxis dosing ranges** — reference WAO / AAAAI algorithm and provider order.
- **No invented laryngospasm reversal dosing** — reference anesthesia at bedside and provider order.
- **No scope-creep actions** — nurses prepare and assist; providers order and perform advanced airway / prescribing.
- **No patient-identifying information.**
- **No protected-characteristic references as performance signals.**

## Worked Example

<details>
<summary>Example: Malignant hyperthermia drill, 15-min runtime, in-situ (click to expand, abbreviated)</summary>

```markdown
# Malignant Hyperthermia — PACU Drill Script

## Drill Purpose & Learning Objectives
1. Roles verbally assigned within 60 sec of MH recognition.
2. MHAUS hotline called, MH cart at bedside, dantrolene preparation initiated per current MHAUS protocol within 5 min of recognition.
3. Closed-loop communication observable for every med / intervention.

## Team Roles
| Role | Primary responsibility | Backup |
|---|---|---|
| Team leader (anesthesia by role) | Calls MH, directs team, manages MHAUS algorithm | Charge nurse |
| Airway / ventilation | Hyperventilate per protocol, switch to non-triggering circuit per anesthesia | RT |
| Circulation | IV access ≥ 2 large-bore, fluids per order, active cooling per facility protocol | Secondary RN |
| Meds (dantrolene lead) | Prepares dantrolene per current MHAUS protocol (reference card on MH cart); works with pharmacy runner | Pharmacy runner |
| Scribe | Timeline, meds, concentrations per pharmacy, patient response (HR, ETCO₂ trend, temp, K+, etc.) | Charge |
| Family liaison | Moves family to private area, communicates per facility policy | Social work |
| Runner | Retrieves MH cart, lab supplies, blood bank products if indicated | Any available |

## Time-Based Action Checklist

| Time | Cue | Expected action | Cognitive aid | Success marker |
|---|---|---|---|---|
| T+0 | Rising ETCO₂, unexplained tachycardia, muscle rigidity | Team leader says "This is MH — we're activating MH protocol." Roles assigned aloud. | MHAUS card | Roles verbally assigned ≤ 60 sec |
| T+2 | MH declared | Call MHAUS hotline (per facility protocol — number on MH cart). Runner retrieves MH cart. | MHAUS card | Hotline called ≤ 2 min |
| T+3 | Discontinue triggering agent | Anesthesia switches to non-triggering circuit; circulation starts cooling per facility protocol | MHAUS protocol | Triggering agent discontinued immediately |
| T+5 | Dantrolene prep | Meds lead + pharmacy runner prepare dantrolene per current MHAUS dose guidance (do not recite doses; consult card) | MHAUS card | First dose ready ≤ 5 min from declaration |
| T+8 | Reassess | ETCO₂, HR, temp, K+ labs drawn per facility; scribe documents | Facility labs pathway | Reassessment + labs at protocol interval |
| T+12 | Transfer prep to ICU or continue in PACU per anesthesia | Family liaison updates family; handoff SBAR ready | — | Transfer criteria named |
| T+15 | Drill end | Freeze, transition to debrief | — | — |

## Debrief Seeds
- "Who assigned the roles, and when did 'meds lead' become distinct from 'general RN'?"
- "MHAUS hotline was called at T+{X} — what was the barrier, if any?"
- "Dantrolene preparation — which step slowed you down?"
- "What does the scribe's timeline show vs. what we think happened?"
```

Notes: no specific dantrolene mg/kg written — defer to MHAUS card; activation code "per facility protocol"; roles explicit; success markers observable; debrief seeds tied to systems.
</details>

## Self-check

- [ ] Emergency type + ≤ 3 LOs explicit.
- [ ] All roles (including family liaison + scribe) assigned.
- [ ] Cognitive aid referenced by name, not reproduced.
- [ ] No invented doses, concentrations, or activation codes.
- [ ] Observer checklist separate from learner tasks.
- [ ] Debrief handoff to `pacu_simulation_debrief_facilitator.md`.
- [ ] "This is a drill" statement included in pre-brief.
- [ ] Safety reminder at top.
- [ ] Verification section passed.
- [ ] False-Positive Prevention section passed.
