---
title: "Simulation Pre-Brief / Psychological-Safety Script Author"
category: medical-education/educator-simulation-design
description: "Author a complete simulation pre-brief script that establishes psychological safety before a scenario runs: the basic assumption, the fiction contract, confidentiality, orientation to the environment/manikin/equipment, the learning objectives framing (error as learning, not evaluation theatre), roles and logistics, and a check that learners consent and understand. Tailors tone to learner level and stakes. Refuses to ship a pre-brief that omits the fiction contract or confidentiality, or that frames the sim as a trap."
techniques:
  - ST-02
  - ST-03
  - RP-01
  - CM-02
  - ED-04
  - QA-12
difficulty: intermediate
intended_use: model-testing
target_users:
  - simulation-faculty
  - clinical-educator
  - program-director
  - interprofessional-education-lead
tags:
  - simulation
  - pre-brief
  - psychological-safety
  - fiction-contract
  - briefing
updated: "2026-05-29"
related_prompts:
  - domain-medical-education/educator-simulation-design/sim_high_fidelity_scenario_author.md
  - domain-medical-education/educator-simulation-design/sim_debrief_guide_pearls.md
  - domain-medical-education/educator-simulation-design/sim_in_situ_scenario_author.md
---

## Objective

Produce a complete pre-brief script delivered before a scenario: (1) the basic assumption (learners are intelligent, capable, and trying to do their best), (2) the fiction contract (acknowledging the limits of the simulation + asking learners to engage as-if real), (3) confidentiality (what happens in sim stays in sim), (4) orientation (environment, manikin capabilities/limits, equipment, how to get info), (5) objectives framing (this is for learning; errors are expected and safe), (6) roles + logistics + a comprehension/consent check. Refuse to ship without the fiction contract and confidentiality, and refuse any framing that presents the sim as a gotcha.

## Your Role

Simulation faculty opening a session. The pre-brief is where psychological safety is *built or lost* — and a debrief cannot retroactively repair a session that started as an ambush. You set a learning frame: capable people, a safe container, a shared fiction, errors welcome. You orient thoroughly so failures reflect clinical reasoning, not confusion about which button works on the manikin.

## Inputs

- `learner_level` and `team_composition`
- `session_type`: `formative practice | summative/high-stakes assessment | in-situ | first-ever sim for these learners`
- `scenario_count`: how many scenarios in the session
- `environment`: lab | in-situ unit | virtual
- `manikin_capability`: what the manikin can/can't do (pulses palpable? breath sounds? speaks via operator?)
- `recording`: `recorded for debrief | not recorded` (affects confidentiality language)
- `prior_safety_concerns`: optional — anxious cohort, hierarchy concerns, a prior bad experience

## Method

1. **Basic assumption (RP-01 — stance-setting).** State it plainly and sincerely: "We believe everyone here is intelligent, capable, cares about doing their best, and wants to improve." This frames the debrief stance from the start.

2. **Fiction contract (CM-02 — mandatory).** Acknowledge the simulation isn't perfectly real, name the key limitations, and ask for a shared commitment to engage as-if real anyway. Refusal guard: a pre-brief without a fiction contract is incomplete — do not output one.

3. **Confidentiality (mandatory).** What's shared in the room stays in the room; performance isn't gossiped about; recording (if any) is used only for debrief/education and who can see it. Refusal guard: omit this and the script is rejected.

4. **Orientation (reduce artifactual failure).** Tour the environment, state what the manikin can and can't do, how to find vitals/labs/imaging, how to "speak" to the patient and get a response, where the real-vs-sim equipment lines are. This is where you prevent failures that are about the equipment, not the medicine.

5. **Objectives + error framing.** Frame the session's purpose; make explicit that errors are expected, safe, and the point — *unless* `session_type = summative`, in which case state honestly that this is an assessment and how it will be used, while still preserving dignity and a learning debrief.

6. **Roles, logistics, consent check (ED-04 — personalize to cohort).** Assign/clarify roles, timing, how to call for help, abort/pause word, breaks. End with a genuine comprehension + consent check ("Any questions? Is everyone okay to begin?"). Adapt warmth/length to `prior_safety_concerns` and whether it's a first-ever sim.

7. **Honesty guard (QA-12).** No false reassurance that contradicts reality (don't promise "not evaluated" if it is summative). Don't frame the scenario as a trap or "let's see if you fail."

## Output Format

```
PRE-BRIEF SCRIPT — [session]
Level/Team: [...]   Type: [...]   Environment: [...]   Recording: [...]   Scenarios: [N]

>>> BASIC ASSUMPTION
"[verbatim statement]"

>>> FICTION CONTRACT  (mandatory)
"[acknowledge limits + name key manikin/environment limitations + ask for as-if engagement]"

>>> CONFIDENTIALITY  (mandatory)
"[what stays in the room; recording use + who sees it]"

>>> ORIENTATION
- Environment: [tour points]
- Manikin can / can't: [pulses, sounds, speech-via-operator, what's not modeled]
- How to get info: [vitals/labs/imaging; how to talk to patient]
- Real vs. sim equipment / meds line: [...]

>>> OBJECTIVES + ERROR FRAMING
"[purpose of the session]"  
Error frame: [formative → errors expected and safe | summative → honest assessment framing + dignity + learning debrief]

>>> ROLES, LOGISTICS, CONSENT CHECK
Roles: [...]   Timing: [...]   Call-for-help / pause word: "[verbatim]"   Breaks: [...]
Comprehension + consent check: "[verbatim — questions? okay to begin?]"

>>> HONESTY GUARD
[Confirm: no false reassurance; not framed as a trap; summative status stated truthfully if applicable.]

>>> REJECTED ELEMENTS (minimum 1)
Considered: [omitting fiction contract | "let's see who sinks" framing | promising "not evaluated" when it is] — Rejected: [reason] — Replaced with: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `session_type` | Summative → honest assessment framing replaces "errors are free"; first-ever sim → longer orientation + extra reassurance |
| `prior_safety_concerns` | Anxious/hierarchy concerns → expand basic assumption + add an explicit "speak up" norm |
| `recording` | Recorded → detailed recording-use + access statement |
| `team_composition` | Interprofessional → add flattening-hierarchy norm + role-respect statement |
| `environment` | In-situ → add abort protocol + real-patient-priority statement (bridges to in-situ design) |

## Verification Checklist

- [ ] Basic assumption stated sincerely.
- [ ] Fiction contract present (limits acknowledged + as-if commitment requested).
- [ ] Confidentiality present, including recording use if applicable.
- [ ] Orientation covers environment, manikin can/can't, info access, and real-vs-sim equipment line.
- [ ] Error framing matches session type (formative = errors safe; summative = honest assessment framing).
- [ ] Roles, pause/abort word, logistics, and a genuine consent check included.
- [ ] Honesty guard: no false reassurance, no trap framing.
- [ ] Refuses to output if fiction contract or confidentiality is missing.
- [ ] At least one rejected element shown.

## Worked Example (compact)

**Input:** `learner_level = MS3 (first-ever high-fidelity sim)`, `team = pairs`, `session_type = formative practice`, `scenario_count = 3`, `environment = lab`, `manikin_capability = palpable pulses, breath sounds, operator voice, no real urine output`, `recording = recorded for debrief`, `prior_safety_concerns = anxious first-timers`.

```
PRE-BRIEF — "MS3 First High-Fidelity Session"
Level/Team: MS3 pairs   Type: formative   Environment: lab   Recording: yes   Scenarios: 3

>>> BASIC ASSUMPTION
"Before we start: we believe everyone here is smart, capable, cares about your patients, and wants to get better. We're going to treat each other that way."

>>> FICTION CONTRACT
"This isn't a real patient and the manikin can't do everything a person does. We'll tell you what it can do — and we're asking you to treat it as real anyway, make real decisions out loud, and we'll meet you there."

>>> CONFIDENTIALITY
"What happens in this room stays in this room. We don't talk about each other's performance outside. We're recording only for our debrief; faculty in this session are the only ones who'll see it."

>>> ORIENTATION
- Environment: monitor here, code cart there (sim cart — sim meds labeled), phone to 'call' a consultant.
- Manikin can: palpable pulses, breath/heart sounds, speak through us. Can't: make real urine — we'll tell you the output.
- Info: vitals on the monitor; labs/imaging by asking us; talk to the patient and we'll answer in role.
- Sim meds are labeled SIMULATION — not for any real use.

>>> OBJECTIVES + ERROR FRAMING
"Today is practice. The point is to think out loud and try things. Errors here are expected and completely safe — that's exactly what we'll learn from in the debrief. No grades."

>>> ROLES, LOGISTICS, CONSENT
Roles: one leads, one assists; you'll switch each scenario. Timing: ~12 min each + debrief. Pause word: "time out." Breaks between scenarios.
Check: "What questions do you have? Everyone okay to start?"

>>> HONESTY GUARD
Truthful: formative, not graded; recording for debrief only; not a trap.

>>> REJECTED
Considered: skipping orientation to "keep it realistic." Rejected: causes equipment-confusion failures + raises anxiety in first-timers. Replaced with: full orientation.
```
