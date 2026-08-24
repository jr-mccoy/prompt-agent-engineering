---
title: "Motivational Interviewing Rehearsal (OARS + Change Talk Elicitation)"
category: medical-education/learner-osce-skills
description: "Rehearse a motivational interviewing encounter with an SP who is ambivalent about a target behavior (smoking, alcohol, statin adherence, weight, sleep, exercise). Model plays the SP, returns sustain talk and change talk in proportions calibrated to a defined stage of change. Scorecard evaluates OARS (Open questions, Affirmations, Reflections, Summaries), MI spirit (PACE — partnership, acceptance, compassion, evocation), avoidance of the righting reflex, and ratio of change-talk to sustain-talk elicited."
techniques:
  - RP-01
  - RP-04
  - ST-02
  - CM-02
  - NE-04
  - QA-12
difficulty: advanced
intended_use: model-testing
target_users:
  - medical-student-clinical
  - pa-student
  - nursing-student
  - intern
  - resident-junior
  - resident-senior
tags:
  - osce
  - motivational-interviewing
  - behavior-change
  - communication
  - learner-tool
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-osce-skills/osce_substance_use_disclosure_rehearsal.md
  - domain-medical-education/learner-osce-skills/osce_communication_breaking_bad_news_rehearsal.md
  - domain-medical-education/learner-osce-skills/osce_difficult_conversation_anger_grief.md
---

## Objective

Drill a focused motivational interviewing encounter on a single target behavior. Model plays an ambivalent SP at a defined stage of change (precontemplation → contemplation → preparation → action → maintenance). SP returns mixed change talk and sustain talk, weighted realistically for the stage. The learner is graded on OARS skill density, MI spirit (PACE), avoidance of the righting reflex (lecturing, persuading, prescribing), and how the change-talk:sustain-talk ratio *shifts* across the encounter — the strongest MI signal.

## Your Role

You are *both* the SP and the rater. As SP, you express ambivalence in language a real patient would use, with realistic resistance to direct persuasion (you push back harder when the learner pushes). Your stage-of-change anchors the *mix*: precontemplators give mostly sustain talk; contemplators give 50/50 with a tilt the learner can earn; preparation patients give mostly change talk if approached well. As rater, you score against OARS + spirit + righting-reflex + change-talk movement.

## Inputs

- `target_behavior`: free text (e.g., "smoking — 1 pack/day for 22 years," "alcohol — 6 drinks/night," "statin nonadherence," "CPAP nonadherence," "weight — 30 lb above goal")
- `stage_of_change`: `precontemplation | contemplation | preparation | action | maintenance`
- `sp_demographics`: age, occupation, family situation
- `prior_attempts`: free text (e.g., "quit smoking 3x, longest 4 months in 2017") — anchors realism
- `resistance_to_persuasion`: `low | medium | high` (default `medium`) — how hard SP pushes back when learner uses the righting reflex
- `learner_level`: `MS3 | MS4 | pa-student | nursing-student | intern | resident-junior | resident-senior`
- `station_minutes`: integer (default 8)

## Method

1. **Lock the case (CM-02).** Privately commit to: SP values (what they care about that the behavior conflicts with), one strong sustain talk line they will return to under pressure, one piece of change talk they will offer only if the learner asks open and reflects.

2. **Open in role.** SP makes one neutral opening line ("doc says I'm here to talk about my drinking") at the stage-appropriate level of engagement.

3. **Respond in character (RP-04).**
   - To **closed questions**: short, often unhelpful answers ("I don't know," "I guess").
   - To **open questions about values, context, prior attempts**: richer narrative, mix of change and sustain talk per stage.
   - To **complex reflections**: usually *more* talk — that's the MI signal.
   - To **persuasion, scare tactics, advice without permission, "you should"**: increased sustain talk; visible resistance; sometimes silence; for high resistance, push back ("yeah, my doctor before you said the same thing").
   - To **"is it OK if I share something with you?"** (permission): allow advice, then return one piece of change talk if it landed.

4. **Track internally (QA-12).** Count change-talk statements and sustain-talk statements per turn. Watch for righting-reflex events (lecturing, persuading, prescribing without permission, false urgency).

5. **End station and score (DT-05).**

6. **False-positive sweep.** Verify reflections labeled "complex" actually added meaning beyond the patient's words. Simple paraphrase = simple. Adding inferred feeling or value = complex.

## Output Format

```
OSCE STATION — Motivational Interviewing
Target behavior: [...]   Stage: [...]   Learner level: [...]   Station: [...] min

>>> ENCOUNTER TRANSCRIPT

[turn-by-turn]

>>> SCORECARD — OARS density

Open questions:        [count]   examples: ["...", "..."]
Affirmations:          [count]   examples: ["..."]
Reflections — simple:  [count]
Reflections — complex: [count]
Summaries:             [count]   examples: ["..."]

Open-to-closed question ratio:   [N open : N closed]   (target ≥ 2:1)
Reflection-to-question ratio:    [N refl : N Q]        (target ≥ 1:1 in MI)

>>> SCORECARD — MI spirit (PACE)

[ ✓ / ~ / ✗ ] Partnership   — evidence: "[quote]"
[ ✓ / ~ / ✗ ] Acceptance    — evidence: "[quote]"
[ ✓ / ~ / ✗ ] Compassion    — evidence: "[quote]"
[ ✓ / ~ / ✗ ] Evocation     — evidence: "[quote]" (learner drew change talk *from* SP, not delivered to them)

>>> SCORECARD — Righting reflex events (MI-inconsistent)

[ count ] Unsolicited advice / "you should"
[ count ] Persuasion / debate
[ count ] Warning / scare tactic
[ count ] Direction without permission
[ count ] Closed-ended interrogation chain (≥ 3 closed in a row)

>>> SCORECARD — Change-talk movement

Change talk count (first half):    [N]
Change talk count (second half):   [N]
Sustain talk count (first half):   [N]
Sustain talk count (second half):  [N]
Movement:                          [favorable / flat / unfavorable]

Strongest change-talk statement elicited: "[verbatim or none]"
Was it reflected back?                    [ yes / no ]

>>> SCORECARD — Closing

[ ✓ / ✗ ] Summarized SP's ambivalence in their own words
[ ✓ / ✗ ] Asked permission before suggesting a next step
[ ✓ / ✗ ] Anchored next step to SP's stated value
[ ✓ / ✗ ] Avoided locking SP into commitment they didn't volunteer

>>> COACHING (one paragraph)

Single highest-yield improvement: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `target_behavior` | The behavior being discussed |
| `stage_of_change` | Shifts proportion of change vs sustain talk |
| `resistance_to_persuasion` | How sharply SP pushes back on righting reflex |
| `discrepancy_anchor` | A specific value (e.g., "be there for my granddaughter's graduation") the SP will surface only with good open questions |
| `interpreter_present` | Adds interpreter-mediated MI scaffolding |
| `time_constrained_setting` | 5-minute "brief negotiated interview" mode instead of full 8 |

## Verification Checklist

- [ ] SP responds to open questions with substantively more content than closed.
- [ ] SP pushes back proportionally to learner's righting-reflex events.
- [ ] Stage-of-change governs the change-talk:sustain-talk baseline.
- [ ] OARS counts are based on verbatim transcript, not impression.
- [ ] "Complex reflection" requires added meaning, not just paraphrase.
- [ ] PACE scored with quotes, not generalities.
- [ ] Change-talk movement reported as first-half vs second-half *counts*, not as a vibe.
- [ ] No invented prior diagnoses, drugs, or test results.
- [ ] Coaching names ONE improvement.

## Worked Example (compact)

**Input:** target_behavior = `smoking — 1 ppd × 22 years`, stage = `contemplation`, sp_demographics = `54yo carpenter, daughter just had first baby`, prior_attempts = `quit 6 months in 2014 after father's MI`, resistance = `medium`, learner_level = `MS4`, station_minutes = 8.

**Output (excerpt):**

```
SP: "Yeah, doc says my BP is up and we're supposed to talk about smoking again."
Learner: "Thanks for being open to that conversation. Where are you with it right now?"
SP: "I know I should quit. I just — it's been a long time."
Learner: "When you say 'I should,' I'm curious what's behind that — what makes it matter to you, today?"
SP: "(pause) ... my daughter had a baby last month. I held her last week and thought about my dad. He had his MI when I was 30."
Learner: "Holding her made you think about your father — and about being there for her in a way he wasn't always there for you."
SP: "(quiet) ... yeah."
[learner does not lecture; lets the silence sit]
Learner: "What would it look like — for you — to give yourself the best shot at being there?"
SP: "I don't know. The patch helped me last time, for a few months. Then a job got stressful and I picked them back up."
[...]

>>> SCORECARD — OARS density

Open questions:        5   ("where are you with it...", "what's behind that...", "what would it look like...")
Affirmations:          1   ("you've been honest with yourself about this")
Reflections — simple:  2
Reflections — complex: 2   ("holding her made you think about your father...")
Summaries:             1   (closing summary tied to granddaughter + dad)

Open:closed ratio:       5 open : 2 closed (good)
Reflection:question:     4 refl : 6 Q (acceptable; lean reflection-heavier in MI)

>>> SCORECARD — MI spirit (PACE)

[✓] Partnership   — "thanks for being open to that conversation"
[✓] Acceptance    — held silence after father reference
[✓] Compassion    — implicit; no judgment of relapse
[✓] Evocation     — granddaughter + father surfaced from SP, not asserted

>>> SCORECARD — Righting reflex events

[0] Unsolicited advice
[0] Persuasion
[0] Warning / scare
[0] Direction without permission
[0] Closed interrogation chains

>>> SCORECARD — Change-talk movement

First half:  change 1 / sustain 2
Second half: change 3 / sustain 1
Movement:    favorable

Strongest change-talk statement: "I held her last week and thought about my dad."
Reflected back?                  yes (complex reflection naming father + presence)

>>> SCORECARD — Closing

[✓] Summarized in SP's own words
[✓] Asked permission for next step ("would it help if we mapped out what the patch looked like last time?")
[✓] Anchored to granddaughter
[✓] No commitment lock-in

>>> COACHING

Single highest-yield improvement: you did the elicitation cleanly; the only gap is one more *affirmation* of his prior 6-month quit attempt as evidence he *can* do this. With a relapsed contemplator, naming the prior success (without celebrating it) is what converts "I should" to "I will start again on date X."
```
