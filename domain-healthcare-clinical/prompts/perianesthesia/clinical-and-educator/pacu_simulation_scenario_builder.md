---
title: PACU Simulation Scenario Builder (Mannequin / Standardized Patient)
category: pacu/simulation
task_type: SIMULATE
audience: PACU educator, lead preceptor, or simulation coordinator designing a Phase 1 sim
updated: "2026-04-16"
tags:
  - pacu
  - simulation
  - scenario
  - mannequin
  - standardized-patient
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-02
  - ED-02
  - DS-06
difficulty: advanced
related_prompts:
  - prompts/pacu_simulation_debrief_facilitator.md
  - prompts/pacu_unfolding_case_study.md
  - prompts/pacu_emergency_drill_designer.md
  - prompts/pacu_complication_deep_dive.md
  - prompts/pacu_quick_quiz_generator.md
references:
  - Drain's PeriAnesthesia Nursing Practice (7th ed.)
  - ASPAN Standards of Perianesthesia Nursing Practice
  - INACSL Healthcare Simulation Standards of Best Practice (Simulation Design, Facilitation, Debriefing)
---

# PACU Simulation Scenario Builder

> Safety reminder: Simulation design aid only — a sim does not replace bedside precepting, facility competency sign-off, or patient-safety event reporting. All doses, equipment, and escalation pathways in the scenario remain illustrative; the running team follows facility protocol.

## Objective

Produce a **full PACU mannequin or standardized-patient simulation scenario** ready to run in a sim lab or in situ: backstory, opening vitals, scripted cue ladder (deterioration *or* stable arc), expected learner actions by phase, branch points, embedded distractors, and seeded debrief questions. Output is the facilitator's script, not the debrief itself (which runs through `pacu_simulation_debrief_facilitator.md`).

## When to use

- Designing Phase 1 PACU sim for weeks 2–10, including reassessment sims during remediation.
- Building scenarios aligned to the scaffold from `pacu_orientee_evaluation_meta_prompt.md` competencies.
- Creating in situ sims to stress-test a unit workflow (e.g., admission + second bay emergence + handoff simultaneously).

## When not to use

- For emergency crash drills — use `pacu_emergency_drill_designer.md` (MH, anaphylaxis, laryngospasm, hemorrhage).
- For text-only paper cases — use `pacu_unfolding_case_study.md`.
- For bedside rapid-fire coaching — use `pacu_skill_drill_designer.md`.

## Inputs

Ask for all of these before generating. If any is missing, ask a clarifying question first.

- **Target competency** from `pacu_orientee_evaluation_meta_prompt.md` scaffold (airway, hemodynamic, PONV escalation, regional-block assessment, handoff, etc.)
- **Orientation phase / learner level:** {{Week 0–2, Week 2–6, Week 6–10, final sign-off, remediation}}
- **Scenario arc:** {{deterioration, stable-but-layered, stable arc that ends in safe discharge, branch-based}}
- **Format:** {{high-fidelity mannequin, standardized patient (SP), hybrid, in situ}}
- **Runtime available:** {{10 / 20 / 30 min run + debrief time}}
- **Roles to fill:** {{primary RN learner, charge, anesthesia (SP or facilitator), family member (SP, optional), observer(s)}}
- **Source chapters / protocols to anchor:** {{Drain's chapter, ASPAN standard, Core Curriculum module, facility protocol if supplied}}

## Audience / Scope

- **Primary:** Sim facilitator preparing the scenario.
- **Secondary:** Learners (orientees + cross-team), debrief facilitator, observer-preceptors.
- **Scope:** PACU Phase 1 orientation simulation. Not for credentialing, not a substitute for direct preceptor observation on shift.

## Output requirements

```markdown
# {Scenario title} — PACU Simulation

> Safety reminder: Simulation. All doses, equipment, and escalations illustrative; facility protocol governs real patients.

## Target Competency
{Name from scaffold} — {sub-behavior the scenario is designed to elicit}

## Learner Level & Pre-brief
- **Phase:** {Week X / final sign-off / remediation reassessment}
- **Pre-brief items:** orientation to equipment, fiction contract ("suspend disbelief about the mannequin"), psychological-safety framing, learning objectives, ground rules.
- **What learners know before start:** 2–3 sentence patient sign-out from pretend-OR.

## Backstory (facilitator eyes only)
- **Patient:** initials only, age range, no MRN or real identifying data.
- **Surgery & anesthesia type:** {generic; no facility-specific drug regimen}
- **Relevant history:** {2–3 items that matter for the scenario arc}
- **Allergies & pertinent meds:** {generic; placeholders for doses}
- **Why this patient is in PACU right now:** {the "why" sentence that orients the learner}

## Opening State (T+0)
- Vitals (range, not exact if not sourced): BP {range}, HR {range}, RR {range}, SpO₂ {range on flow rate}, temp {range}, pain {score}, LOC {A/Ox? sedation score}.
- Monitor display: {what is on the screen at T+0}
- Physical exam: {2–3 observable findings}
- Lines/devices: {IV, O2, Foley, drain, PCA — generic}
- Surgical site: {observable status}
- Environment: {family present? phone ringing? second bay demand?}

## Scripted Cue Ladder (minute-by-minute)

| Time | Cue delivered | Expected learner action | Escalation partner if triggered | Branch |
|---|---|---|---|---|
| T+0 | {opening state as above} | Initial assessment; orient to bay | — | — |
| T+2 | {first subtle change — e.g., RR drifting, shallow chest rise} | Recognize, reposition / reassess | — | If missed → T+5 worsens |
| T+5 | {first overt change — e.g., SpO₂ trending down} | Call anesthesia by role; escalate SBAR | Anesthesiologist / CRNA | If misses SBAR → facilitator pushes cue |
| T+8 | {pivot point — stabilize vs. deteriorate} | Follow through on escalation; recheck response | — | Branch A: stable; Branch B: worsens |
| T+12 | {resolution or code-edge} | Complete handoff or transition | Role named | — |
| T+15 | End / pause for debrief | — | — | — |

Adapt times and rows to the chosen arc and runtime.

## Branch Points (explicit)
- **Branch A (stable):** If learner acts by T+5 and escalates by T+7, scenario resolves with stable handoff at T+12.
- **Branch B (deterioration):** If learner misses cue at T+2 and does not escalate by T+7, scenario layers second finding at T+9 (e.g., new bradycardia + hypotension) and requires rapid-response-level escalation.
- **Branch C (red herring):** Family member (SP) interrupts at T+6 asking when the patient is going home; tests learner's prioritization and communication.

## Embedded Distractors (1–2 per scenario, realism without derailment)
- {Distractor — e.g., second bay monitor alarm audible, secretary hand-off request, family phone call, wrong dressing on the chart}
- Each distractor has a purpose (triage, prioritization, communication) — never pure noise.

## Expected Learner Actions (graded)

| Cueing level | What it looks like in this scenario |
|---|---|
| Independent | Recognizes T+2 cue without prompting; escalates by T+5 with complete SBAR; handles distractor without losing the main patient. |
| With Cues | Requires facilitator cue ("what's the trend telling you?") to recognize T+2; escalates with partial SBAR; distractor pulls focus briefly. |
| With Direction | Only responds to overt T+5 change; SBAR fragmentary; distractor derails assessment. |
| Not Yet | Waits for alarm; does not escalate until T+8 or later; SBAR absent. |

## Facilitator Operating Notes
- **Voice of the patient (for mannequin):** 2–3 prepared lines ("My chest feels tight," "I can't catch my breath").
- **Voice of the monitor:** when to change displayed values; who's operating the console.
- **SP prompts (if applicable):** 3–5 scripted family-member or anesthesia lines; what to do if learner asks something off-script.
- **When to pause:** freeze-frame criteria (imminent unsafe action that isn't recoverable within the scenario).
- **When to restart / rewind:** if learner requests, or if a critical teaching point was skipped.

## Seeded Debrief Questions (hand off to `pacu_simulation_debrief_facilitator.md`)
- "Walk me through the cue you acted on first — what did you see before you did anything?"
- "If the cue at T+2 had been more subtle, what would you have looked for?"
- "Tell me about your SBAR at T+5 — what felt solid, what was thin?"
- "How did the family interruption land? What would you do differently?"
- {one scenario-specific question tied to competency}

## Safety & Realism Rules
- No specific drug doses written into the scenario — use "per order" or "{{facility-protocol placeholder}}."
- No facility-specific pagers, room numbers, or staff names.
- No patient-identifying info (MRN, full name, full DOB).
- If the scenario involves a red-flag event (code-edge, MH, anaphylaxis), pair with `pacu_emergency_drill_designer.md` rather than embedding drill-level detail here.

## Sources / reference
- *Drain's PeriAnesthesia Nursing*, Ch. {X}
- ASPAN *Standards of Perianesthesia Nursing Practice*, {section}
- ASPAN *Core Curriculum for PeriAnesthesia Nursing Practice*, {module}
- INACSL Healthcare Simulation Standards of Best Practice (pre-brief, facilitation, debriefing)
- Facility orientation program sim policy: {{per facility protocol}}
```

## Must / Must not

**Must:**
- Target **one** competency from the scaffold — a scenario trying to hit five competencies hits none.
- Include a pre-brief block with psychological-safety framing and a fiction contract.
- Build a time-stamped cue ladder (minute-level) with explicit expected actions.
- Include at least one explicit branch point so the scenario responds to learner behavior.
- Name escalation partners by role (CRNA, anesthesiologist on call, charge, rapid response), never by name.
- Label doses and facility-specific items with placeholders ("per order," "per facility protocol").
- Seed 3–5 debrief questions that the debrief facilitator can use as starting points.

**Must not:**
- Fabricate doses, equipment specifics, or facility protocols.
- Invent ASPAN or Drain's citations — mark `{{confirm}}` when unknown.
- Include patient-identifying information (MRN, full name, full DOB, room number).
- Reference age, race, sex, disability, religion, national origin, pregnancy, license pathway, or prior unit as scenario details unless clinically essential and handled without bias.
- Design a scenario where the expected action is outside nursing scope ("nurse intubates") — reframe as "nurse prepares equipment and assists provider."
- Stage a scenario intended to humiliate or entrap learners — simulation is learning, not hazing.
- Create a code-level scenario without pairing with `pacu_emergency_drill_designer.md` for drill discipline (team roles, equipment, time-based actions).
- Substitute for facility competency sign-off documentation.

## Quality signals

- A sim facilitator unfamiliar with the learner can run the scenario from the script with minimal adaptation.
- The cue ladder visibly responds to learner action (not a fixed timeline regardless of behavior).
- Branch B (deterioration) is recoverable within the runtime — no dead ends.
- Distractors test prioritization without derailing the primary teaching point.
- Debrief questions are open-ended and tied to observable learner behavior in the scenario.

## Verification

Before returning the scenario, verify:

- [ ] Exactly one target competency is named and visibly drives the cue ladder.
- [ ] Pre-brief, psychological-safety framing, and fiction contract are present.
- [ ] Cue ladder has ≥ 4 time-stamped rows with expected learner actions per row.
- [ ] ≥ 1 explicit branch point with A/B/C (or at minimum A/B) outcomes.
- [ ] Expected-learner-action grid uses the sign-off scale tokens (Independent / With Cues / With Direction / Not Yet).
- [ ] All doses / equipment / facility references use placeholders.
- [ ] ≥ 3 seeded debrief questions pointing to observable learner behavior.
- [ ] Scenario runtime matches the available time (not bloated).

## False-Positive Prevention

Do **not** fabricate:

- **No invented doses, drip rates, concentrations, or medication orders.** Use "per order" / placeholder.
- **No invented vital-sign thresholds that drive the cue ladder** ("SpO₂ hits 91%") unless sourced. Use ranges or qualitative cues ("drifting down," "persistently below baseline").
- **No invented facility protocols, rapid-response activation codes, or pager numbers.**
- **No invented equipment models, crash-cart contents, or bag sizes.** Use generic terms.
- **No invented patient identities, demographics, or social history** beyond what the competency requires. Initials + age range only.
- **No invented citations.** Mark `{{confirm chapter in Drain's / ASPAN module}}` when unknown.
- **No scope-creep actions** — expected actions stay within nursing scope; provider actions remain provider actions.
- **No protected-characteristic references** that frame demographics as performance signals.

## Worked Example

<details>
<summary>Example: Target = post-spinal hypotension recognition, Week 6 new-grad, 20-min mannequin sim (click to expand, abbreviated)</summary>

```markdown
# Post-Spinal Hypotension Recognition — PACU Simulation (Week 6)

## Target Competency
Hemodynamic assessment & intervention — recognize post-spinal BP drift before alarm and escalate SBAR to CRNA by role.

## Learner Level & Pre-brief
- Week 6 new-grad PACU orientee.
- Pre-brief covers: mannequin orientation, monitor layout, fiction contract, psychological-safety framing, LO = "recognize trend before alarm and escalate by role with SBAR."

## Opening State (T+0)
- Vitals: BP 128/78, HR 82, RR 14, SpO₂ 97% on 2L NC, temp 36.4, pain 2/10, A&Ox3, spinal block level per handoff = T6.
- Monitor: all numbers green, no alarm.
- Exam: alert, warm extremities, no complaints.
- Environment: patient's spouse (SP) in chair, asking when patient can go home.

## Scripted Cue Ladder (20 min)
| Time | Cue | Expected action | Escalation | Branch |
|---|---|---|---|---|
| T+2 | BP cycles 120/72 → 112/68 (subtle downward trend) | Verbalize trend, recheck, reposition (legs elevated per order) | — | If missed → T+5 worsens |
| T+5 | BP 100/60, HR 70, patient says "feels a little dizzy" | Call CRNA by role with SBAR; prepare IV fluid per order | CRNA | If no escalation → T+8 Branch B |
| T+8 | Branch A: BP stabilizing 108/65 after intervention → proceed. Branch B: BP 88/50, HR 60 → rapid response. | Branch A: continue monitoring; Branch B: call rapid response, prepare vasopressor per order | CRNA or rapid response | — |
| T+14 | Stable handoff to floor OR extended PACU observation | Complete SBAR outbound | Receiving RN | — |
| T+18 | End / pause | — | — | — |

## Seeded Debrief Questions
- "What did you see at T+2 before the monitor showed any alarm?"
- "Your SBAR at T+5 — walk me through what felt complete and what was thin."
- "How did the spouse's question at T+0 affect your first few minutes?"
- "If the block level had been T4 instead of T6, what would you have looked for differently?"
- "At Branch B, what was the difference between 'call CRNA' and 'call rapid response' in your head?"
```

Notes: one competency (hemodynamic recognition), cue ladder responds to learner action, branches recover, SP distractor tests prioritization without derailing, no specific mg doses written (all "per order"), initials not needed because mannequin, escalation by role only.
</details>

## Self-check

- [ ] Single target competency named and drives the scenario.
- [ ] Pre-brief with psychological safety + fiction contract present.
- [ ] Cue ladder has time stamps and expected actions per row.
- [ ] At least one branch point explicit.
- [ ] Sign-off scale tokens used in expected-action grid.
- [ ] No invented doses, facility specifics, or citations.
- [ ] No patient-identifying information.
- [ ] No protected-characteristic references.
- [ ] Seeded debrief questions handed off to debrief facilitator prompt.
- [ ] Safety reminder at top.
- [ ] Verification section passed.
- [ ] False-Positive Prevention section passed.
