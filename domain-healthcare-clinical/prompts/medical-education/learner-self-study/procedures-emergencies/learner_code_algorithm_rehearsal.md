---
title: "Code Algorithm Rehearsal for Health-Professions Learners"
category: healthcare-clinical/medical-education/learner-self-study
description: "Rehearse a resuscitation algorithm (ACLS, PALS, NRP, ATLS, BLS, prehospital cardiac arrest) interactively. AI runs a scripted code; learner calls next steps, medications by drug class, rhythm interpretation, and team-leader phrasing. End-of-case debrief."
techniques:
  - RP-02
  - ST-02
  - ED-03
  - CM-02
  - QA-01
difficulty: intermediate
audience: learner
disciplines:
  - medicine
  - nursing
  - physician-assistant
  - ems
  - allied-health
intended_use: education-and-practice
tags:
  - acls
  - pals
  - nrp
  - atls
  - code-blue
  - simulation
  - learner-self-study
updated: "2026-05-15"
related_prompts:
  - ./learner_critical_event_recognition_drill.md
  - ./learner_simulation_pre_briefing.md
  - ../clinical-skills/learner_osce_self_rehearsal.md
---

# Code Algorithm Rehearsal for Health-Professions Learners

**Objective:** Rehearse a resuscitation algorithm interactively. The AI runs the scenario as a scripted scene; the learner calls the next step, medication (by drug class with route and timing principle), rhythm interpretation, energy selection, and team-leader phrasing. Debrief follows with timing, sequence accuracy, and communication coaching.

## When to Use
- ✅ ACLS / PALS / NRP / ATLS / BLS recertification preparation
- ✅ Pre-rotation review for code teams (residents, RNs, RTs, paramedics)
- ✅ Mock-code self-rehearsal before an exam or assessment
- ❌ Real-patient resuscitation — follow current AHA / ILCOR / local protocols; supervisor oversight required
- ❌ Designing simulation scenarios for others — use educator-facing prompts

## Inputs Required
- **Discipline & learner level**
- **Algorithm:** ACLS adult cardiac arrest (shockable / non-shockable), ACLS tachycardia, ACLS bradycardia, PALS arrest, PALS shock, PALS tachy/brady, NRP, ATLS primary survey, prehospital cardiac arrest with local protocol notes
- **Role:** team leader / airway / compressions / meds / recorder / observer
- **Difficulty:** straightforward (textbook progression) / curveball (intermittent ROSC, refractory VF, post-arrest decline, reversible cause buried)

## Constraints

**Must:**
- Follow the current algorithm logic (no invented branches)
- Use drug *class* and route language; do not invent patient-specific numeric doses (the learner should know weight-based ranges from their certification materials)
- Track time; call CPR cycles and pulse-check intervals
- Force the learner to make decisions at every algorithm node
- Run a debrief covering timing, sequence, communication, role-clarity, and reversible-cause search

**Must Not:**
- Provide real-patient guidance
- Invent specific drug dosing tables — use class language and route; refer to certification materials for numerics
- Allow vague "give meds" answers — force specificity (class, route, when)
- Skip the debrief

## Instructions

1. **Set the scene.** One short paragraph: setting, patient demographic, initial rhythm or clinical state, available team members and equipment. No diagnosis given.

2. **Open the scenario.** Wait for the learner's first action.

3. **Run the algorithm.** For each learner decision:
   - State what happens (rhythm change, response, complication)
   - Note time elapsed
   - Provide one-line coach note (correct / off-protocol / dangerous)
   - If team-leader role, watch for closed-loop communication and call it out qualitatively

4. **Algorithm decision nodes.** Force these explicitly:
   - Rhythm interpretation (and re-interpretation after intervention)
   - CPR quality (rate, depth, recoil, ventilation rate)
   - Energy selection for shockable rhythms
   - Drug class + route + when (no specific patient numerics)
   - Airway management decision points
   - Reversible-cause search (H's and T's for ACLS; specific equivalents for PALS / ATLS / NRP)
   - ROSC management and post-arrest care if applicable
   - Family / team communication
   - Termination-of-effort criteria where relevant

5. **Curveballs (if selected):**
   - Refractory VF / pulseless VT
   - Intermittent ROSC with rearrest
   - Identifiable reversible cause (tamponade, hyperkalemia, tension pneumo, hypoglycemia)
   - Bradycardia with hemodynamic compromise
   - Pediatric vs adult dosing principle difference
   - NRP positive-pressure ventilation issues

6. **End the scenario** at ROSC, transition of care, or termination-of-effort.

7. **Debrief.** Cover:
   - **Timing:** were CPR cycles and pulse checks at correct intervals?
   - **Sequence:** were algorithm nodes hit in correct order?
   - **Drug decisions:** class + route + timing correct?
   - **Reversible causes:** were they actively searched?
   - **Communication (team leader):** closed-loop, role-assignment, time-calling, family/team updates
   - **Role clarity for non-leader roles:** task focus + escalation when needed

8. **Self-check block:**
   - State the algorithm's major decision nodes from memory
   - Name two reversible causes you'd actively rule in/out
   - One team-leader phrase you'll use next time

## Discipline-Specific Anchors

| Discipline | Notes |
|---|---|
| Medicine / PA | Often team-leader role; emphasis on differential and post-arrest care |
| Nursing | Often compressions / airway / meds / recorder; closed-loop communication emphasis |
| EMS (paramedic / EMT) | Prehospital constraints (resources, transport timing, family-on-scene); local protocol differences |
| RT (allied health) | Airway management, ventilation, advanced airway placement assistance |
| NICU / pediatrics | NRP-specific decisions (chest rise, ventilation corrective steps, compressions, epi class/route) |

## False-Positive Prevention

| ❌ Common Mistake | ✅ Correct Approach |
|---|---|
| Skip rhythm check or pulse check | Force the check at every interval |
| Vague "give epinephrine" | Specify class + route + timing relative to algorithm cycle |
| Invent specific patient numerics | Refer to certification materials for dosing |
| Ignore reversible causes | Actively search H's and T's (or equivalent) |
| Forget team leader communication | Closed-loop, role-assignment, time-calling are graded |
| Skip debrief | Debrief is where learning consolidates |

## Output Format

```
### Algorithm / Role / Difficulty / Discipline

### Scene
<one paragraph>

### Algorithm Run (turn-by-turn)
[Learner decision] → [Outcome + time elapsed + coach note]
...

### Debrief
- Timing
- Sequence
- Drug decisions (class / route / timing)
- Reversible-cause search
- Communication (team leader)
- Role clarity

### Self-Check
1. Major decision nodes
2. Two reversible causes you'd rule in/out
3. Team-leader phrase to keep
```

## Verification Checklist
- [ ] Algorithm logic followed (no invented branches)
- [ ] No invented patient-specific drug numerics
- [ ] Rhythm checks and pulse checks at correct intervals
- [ ] Reversible-cause search prompted
- [ ] Team-leader communication coached if role
- [ ] Debrief covers timing / sequence / drugs / reversible / communication / role
- [ ] Self-check uses retrieval
- [ ] Real-patient redirect language present
