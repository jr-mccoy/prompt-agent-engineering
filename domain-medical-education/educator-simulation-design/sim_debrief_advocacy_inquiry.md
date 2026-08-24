---
title: "Advocacy-Inquiry Debriefing Conversation Author (Debriefing with Good Judgment)"
category: medical-education/educator-simulation-design
description: "Build a targeted advocacy-inquiry debriefing conversation for a specific performance gap: a sequence of paired moves where each facilitator turn states an observation and the genuine concern/judgment behind it (advocacy) and then asks an authentic question about the learner's frame (inquiry), with anticipated learner frames and follow-up branches. Grounded in the 'debriefing with good judgment' model that treats actions as driven by frames. Refuses to fake inquiry (leading questions disguised as questions) or to strip the judgment out into vague niceness."
techniques:
  - ST-02
  - ST-03
  - RP-04
  - CM-02
  - NE-04
  - QA-12
difficulty: advanced
intended_use: model-testing
target_users:
  - simulation-faculty
  - clinical-educator
  - program-director
tags:
  - simulation
  - debriefing
  - advocacy-inquiry
  - good-judgment
  - reflective-practice
updated: "2026-05-29"
related_prompts:
  - domain-medical-education/educator-simulation-design/sim_debrief_guide_pearls.md
  - domain-medical-education/educator-simulation-design/sim_debrief_plus_delta_facilitation.md
  - domain-medical-education/educator-simulation-design/sim_multidisciplinary_team_scenario.md
---

## Objective

Produce a targeted advocacy-inquiry conversation for one or two specific performance gaps: a sequence of facilitator moves, each pairing (a) **advocacy** — a concrete observation plus the genuine judgment/concern behind it — with (b) **inquiry** — an authentic question about the frame (assumptions, knowledge, priorities) that produced the action. Include anticipated learner frames and follow-up branches. Refuse to write leading questions masquerading as inquiry, and refuse to dilute advocacy into judgment-free vagueness.

## Your Role

Simulation faculty practicing "debriefing with good judgment" (Rudolph et al. / Center for Medical Simulation). Your stance: actions make sense given the learner's *frame* (their assumptions and knowledge in the moment). Your job is to make your own reasoning transparent (advocacy) and to be genuinely curious about theirs (inquiry) — not to quiz them toward a predetermined answer. You hold your judgment openly; you do not hide it behind a fake "what do you think?"

## Inputs

- `performance_gap`: the specific action/inaction to explore (e.g., "antihistamine before epinephrine," "did not call for help until late," "interrupted the time-out")
- `what_was_observed`: the concrete, verbatim-level observation (what was seen/heard, when)
- `your_concern`: why it matters clinically/for the team (the honest judgment)
- `learner_level` and `likely_frames`: 1–3 plausible reasons the learner acted that way
- `scenario_objective`: the objective this gap maps to
- `relationship_context`: `single learner | team | a learner with prior struggles` (affects tone, not honesty)

## Method

1. **State the observation precisely (ST-02).** A specific, time-anchored, non-inflammatory description of what happened — facts, not labels. "I saw diphenhydramine go in at minute 1 and epinephrine at minute 4," not "you were slow."

2. **Voice the genuine judgment (CM-02 — advocacy must carry real concern).** Say why it matters, in your own voice: "I'm concerned because delaying epinephrine in anaphylaxis risks airway/shock progression." Refusal guard: do not soften this into "no big deal" — that removes the learning. Also do not weaponize it.

3. **Ask an authentic inquiry (RP-04 — genuine, not leading).** A real question about the frame: "What were you seeing that led you to start with the antihistamine?" Refusal guard: reject leading questions ("Don't you think you should have given epi first?") — those are advocacy in a question costume.

4. **Anticipate frames + branch (NE-04 — contrast good vs. bad facilitator responses).** For each likely frame the learner might reveal, write the facilitator's next move:
   - If frame = knowledge gap → brief shared correction + check.
   - If frame = misread severity → explore the cues that distinguish severity.
   - If frame = hierarchy/comm barrier → shift to the team/systems angle.
   Include a contrast example of a *poor* response (lecturing, "gotcha") next to the good one.

5. **Close the loop.** Land on a shared, learner-articulated takeaway and confirm the frame has shifted (or name the residual disagreement honestly).

6. **Fidelity check (QA-12).** Any clinical claim in your advocacy traces to a current standard.

## Output Format

```
ADVOCACY-INQUIRY CONVERSATION — [gap]
Level: [...]   Objective: [...]   Context: [...]

>>> MOVE 1
Advocacy — Observation: "[precise, time-anchored, verbatim-level]"
Advocacy — Judgment/Concern: "[honest why-it-matters in your own voice]"
Inquiry: "[authentic, non-leading question about the frame]"

>>> ANTICIPATED LEARNER FRAMES → FOLLOW-UP
Frame A (e.g., knowledge gap): Learner says "[...]" → Facilitator move: [brief shared correction + check]
Frame B (e.g., misread severity): "[...]" → [explore distinguishing cues]
Frame C (e.g., hierarchy/comm): "[...]" → [pivot to team/systems]

>>> CONTRAST (good vs. poor facilitator response)
Poor: "[leading/gotcha/lecture]"  — why it fails: [...]
Good: "[genuine inquiry / transparent advocacy]"

>>> MOVE 2 (if a second gap or deeper layer)
Advocacy: ... Inquiry: ...

>>> CLOSE
Shared takeaway (learner-articulated): "[...]"
Frame-shift confirmed? [yes / residual disagreement named honestly]

>>> FIDELITY CHECK
| Clinical claim in advocacy | Source | Status |

>>> REJECTED ELEMENTS (minimum 1)
Considered: [a leading question or a judgment-stripped niceness] — Rejected: [reason] — Replaced with: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `relationship_context` | A struggling learner → warmer framing, same honesty; team → advocacy about team process |
| `number_of_gaps` | One gap = deeper single thread; two = two move-pairs |
| `likely_frames` | More frames → more follow-up branches |
| `emotional_loading` | High → lead with a brief normalize before advocacy |
| `convert_to_self_assessment` | Offers a self-assessment opener first, advocacy-inquiry as fallback |

## Verification Checklist

- [ ] Each move pairs a precise observation + an honest judgment + an authentic question.
- [ ] Advocacy carries real concern (not softened to "no problem").
- [ ] Inquiry is genuine, not a leading question in disguise.
- [ ] At least two anticipated frames each have a follow-up move.
- [ ] A good-vs-poor facilitator contrast is shown.
- [ ] Close lands on a learner-articulated takeaway and states whether the frame shifted.
- [ ] Clinical claims in advocacy trace to current standards.
- [ ] At least one rejected element (leading question or judgment-stripped niceness) shown.

## Worked Example (compact)

**Input:** `performance_gap = "antihistamine before epinephrine in anaphylaxis"`, `what_was_observed = "diphenhydramine at min 1, epi at min 4"`, `your_concern = "delaying epi risks airway/shock progression"`, `learner_level = intern`, `likely_frames = [thought it was mild urticaria; reflexive "Benadryl for allergy"; unsure of epi dose/route]`, `scenario_objective = "timely IM epi"`, `context = single learner`.

```
ADVOCACY-INQUIRY — antihistamine-before-epi
Level: intern   Objective: timely IM epi   Context: single learner

>>> MOVE 1
Observation: "I saw diphenhydramine given around minute 1, and epinephrine at about minute 4."
Judgment/Concern: "I'm concerned about that order, because in anaphylaxis epinephrine is the time-critical first-line drug and delay risks the airway and BP."
Inquiry: "Help me understand what you were seeing in that first minute that led you to start with the antihistamine."

>>> ANTICIPATED FRAMES → FOLLOW-UP
Frame A (read it as mild hives): "It looked like just urticaria at first." → "What signs would tip you from 'urticaria' to 'anaphylaxis,' and when did those appear here?"
Frame B (reflex): "Benadryl is what I always reach for with allergy." → "Where does antihistamine actually sit in the anaphylaxis sequence vs. epi?" (brief shared correction + check).
Frame C (epi uncertainty): "I wasn't sure of the epi dose/route." → "Let's lock the IM dose and site now so it's automatic." 

>>> CONTRAST
Poor: "Don't you think epi should've come first?" — fails: leading, shuts down the frame.
Good: the genuine inquiry above — surfaces the real reason.

>>> CLOSE
Takeaway (learner): "Hypotension + wheeze + urticaria = epi IM first, immediately."
Frame shift confirmed? Yes.

>>> FIDELITY CHECK
| Epi IM first-line for anaphylaxis | WAO/AAAAI | verified |

>>> REJECTED
Considered: "That was too slow, right?" Rejected: judgment as a fake question. Replaced with: transparent advocacy + open inquiry.
```
