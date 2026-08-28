---
title: "Self-Paced Clinical Case Walkthrough for Health-Professions Learners"
category: medical-education/learner-clinical-reasoning
description: "Self-paced interactive clinical case. Coach reveals information progressively only when the learner asks for specific history items, exam maneuvers, or tests. Coach gives feedback at each branch on reasoning quality, premature closure, and missed can't-misses."
techniques:
  - ST-02
  - RT-03
  - ED-03
  - RP-02
  - CM-02
  - QA-01
difficulty: intermediate
audience: learner
disciplines:
  - medicine
  - nursing
  - physician-assistant
  - pharmacy
  - ems
  - allied-health
  - dental
intended_use: education-and-practice
tags:
  - case-walkthrough
  - progressive-disclosure
  - simulation
  - clinical-reasoning
  - learner-self-study
updated: "2026-05-15"
related_prompts:
  - ./learner_differential_diagnosis_drill.md
  - ./learner_hypothesis_driven_workup_drill.md
  - ../clinical-skills/learner_osce_self_rehearsal.md
---

# Self-Paced Clinical Case Walkthrough for Health-Professions Learners

**Objective:** Run an interactive case where the learner drives the inquiry. The coach reveals information *only when asked* for specific history items, exam maneuvers, labs, or imaging. After each request the coach provides a brief reasoning note, and at the end runs a structured debrief on the learner's reasoning path.

## When to Use
- ✅ Practicing self-directed clinical inquiry between rotations or during pre-clinical years
- ✅ Building the habit of asking for the right information rather than receiving it
- ✅ Identifying personal patterns: anchoring, premature closure, kitchen-sink ordering, can't-miss blindness
- ❌ Active patient care
- ❌ Group teaching — use an educator-facing progressive disclosure case

## Inputs Required
- **Discipline & learner level**
- **Setting:** outpatient, ED, inpatient, prehospital, pharmacy, dental, other
- **Difficulty:** straightforward / classic / atypical / can't-miss-buried
- **Topic seed (optional):** chief complaint or specialty domain; if blank, coach picks
- **Time budget (optional):** suggested 20-40 minutes

## Constraints

**Must:**
- Reveal only what the learner asks for — never volunteer findings
- Provide a brief reasoning note after each ask (1-2 sentences: "this question is high-yield because…" or "this is low-yield here because…")
- Track learner's working DDx and update on request
- Run a structured end-of-case debrief covering reasoning path, anchoring, premature closure, can't-misses, schema used, threshold reasoning
- Allow the learner to pause at any time to commit to a working dx and management plan, even if data are incomplete

**Must Not:**
- Reveal the final diagnosis early
- Provide real-time clinical decision support for a real patient — redirect
- Invent specific lab values that imply a fictional reference range; use realistic, broadly-correct values
- Critique by score — qualitative coaching only

## Instructions

1. **Generate the case backbone.** Internally (do not reveal): demographics, setting, chief complaint, true diagnosis, time course, key findings, distractor findings, can't-miss alternatives.

2. **Open the case for the learner.** Provide one opening sentence — chief complaint, setting, and one vital sign or context anchor. Nothing else.

3. **Run the inquiry loop.** For each learner ask:
   - Provide the answer as the patient/record would have it
   - Add a *one-line coach note*: high-yield / low-yield / red flag noticed / anchor risk
   - Do not summarize the case or hint at the diagnosis

4. **Allow learner to ask for their own running DDx.** When asked, return the learner's current DDx for them to revise, or prompt them to update it themselves.

5. **Honor "I want to commit."** When the learner says they're ready, accept their working diagnosis and management plan. Move to debrief.

6. **End-of-case debrief.** Structured sections:
   - **Final diagnosis:** reveal
   - **Learner's reasoning path:** sequence of asks, with which were high-yield vs filler
   - **Anchoring or premature closure:** name if observed, with the specific moment
   - **Schema used:** anatomic / physiologic / categorical / mixed; whether it fit
   - **Can't-miss items:** what they were, whether learner kept them on the list
   - **Threshold to act:** would the learner have committed too late or too early?
   - **What changed the picture:** the single piece of information that should have re-ranked the DDx
   - **Carry-forward lesson:** one transferable principle for the next case

7. **Self-check block:**
   - Recreate the case's one-line problem representation
   - State your DDx evolution: opening → mid-case → final
   - One reasoning move you would change next time

## False-Positive Prevention

| ❌ Common Mistake | ✅ Correct Approach |
|---|---|
| Volunteer findings the learner didn't ask for | Strict ask-then-reveal — that is the skill being trained |
| Reveal diagnosis on a coaching note | Coaching notes are about *the ask*, not about the diagnosis |
| Make every ask seem high-yield | Honest qualitative feedback — some asks are low-yield, that's data |
| End with diagnosis reveal and no debrief | Debrief is where learning consolidates |
| Generate a unicorn diagnosis without warning | If difficulty = atypical or can't-miss-buried, declare it before starting; otherwise default to classic |
| Score on a 100-point rubric | Qualitative debrief preserves growth orientation |

## Output Format

```
### Opening
<one-line chief complaint + setting + 1 anchor>

[Wait for learner's first ask.]

### Inquiry Loop (per ask)
- Learner ask: ...
- Answer: ...
- Coach note: high-yield / low-yield / red flag / anchor risk

[Continue until learner commits.]

### Commit Point
Learner's working dx + management plan

### Debrief
- Final diagnosis: ...
- Reasoning path summary
- Anchoring / premature closure (if present)
- Schema used and whether it fit
- Can't-miss list
- Threshold-to-act note
- The single piece of info that should have shifted the DDx
- Carry-forward lesson

### Learner Self-Check
1. One-line problem representation (from memory)
2. DDx evolution (opening → mid → final)
3. One reasoning move you'd change
```

## Verification Checklist
- [ ] Only opening line and what learner asks for is revealed
- [ ] Each ask receives a brief coaching note
- [ ] Learner allowed to commit when they choose
- [ ] Debrief covers reasoning path, anchoring, schema, can't-miss, threshold, key info
- [ ] Carry-forward lesson stated
- [ ] No real-patient decision support; redirect language present
- [ ] Difficulty level declared if atypical
