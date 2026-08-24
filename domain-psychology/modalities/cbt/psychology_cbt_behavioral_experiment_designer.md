---
title: "CBT Behavioral Experiment Designer"
category: psychology/modalities/cbt
description: "Design a Beckian behavioral experiment to test a specific belief (prediction or theory A vs theory B), including safety-behavior identification, outcome criteria, and post-experiment reformulation."
techniques:
  - ST-04
  - RT-02
  - DT-02
  - ED-04
  - QA-04
  - CM-02
difficulty: intermediate
tags:
  - CBT
  - behavioral-experiment
  - belief-testing
  - safety-behaviors
  - Bennett-Levy
  - Padesky
intended_use: model-testing
updated: "2026-05-19"
related_prompts:
  - domain-psychology/modalities/cbt/psychology_cbt_thought_record_drafter.md
  - domain-psychology/modalities/cbt/psychology_cognitive_distortion_identifier.md
  - domain-psychology/modalities/cbt/psychology_cbt_social_anxiety_protocol_session_plan.md
---

# CBT Behavioral Experiment Designer

## Objective

Design a single behavioral experiment (BE) following the Bennett-Levy / Oxford Guide framework: a planned, real-world action that tests a specific belief, with explicit predictions, outcome criteria, and a post-experiment reflection. The experiment must be specific enough that the client can run it without the clinician, and yield data the client cannot easily dismiss.

Two design types are supported:

- **Hypothesis-testing experiment** — tests a single prediction (e.g., "If I ask for help in a meeting, my coworkers will think I'm incompetent").
- **Discovery / Theory A vs Theory B** — pits an anxious theory ("I am dangerous / disgusting / will fail") against a balanced theory ("I have an *idea* about myself that this experiment can examine").

## When to Use

- Following thought records, when a specific belief has been isolated but not disconfirmed at the gut level.
- Mid-protocol for social anxiety, panic, OCD (with caution and ERP framing), health anxiety, perfectionism, body-image concerns, low self-esteem.
- After identifying safety behaviors that maintain the belief.
- When verbal restructuring has plateaued and the client says "I know it intellectually but don't believe it."
- As recurring homework — clients typically need 2–4 BEs per target belief.

## Inputs / Context

- Target belief, specifically worded (verbatim from client) with current belief rating (0–100).
- Origin: which thought record / case formulation produced this belief.
- Safety behaviors currently used to prevent feared outcome (rehearsing speech, scanning faces, checking pulse, reassurance-seeking, avoidance).
- Client's available real-world contexts (workplace, gym, family, public spaces) and timing/feasibility.
- Risk factors: medical contraindications (e.g., cardiac history for interoceptive exposure), trauma history, social/employment risks of the experiment.
- Cultural/linguistic considerations affecting feasibility (e.g., experiments involving asking strangers).
- Modality (in-vivo / interoceptive / imaginal / behavioral / observational).
- Time horizon: in-session, between-session within a week, or staged across weeks.

## Constraints

### Must

- Specify the **belief** as a falsifiable proposition with a current belief rating.
- Specify **predictions** as observable outcomes ("3+ coworkers will smirk or look away") with thresholds, not vague ("It'll go badly").
- Identify **safety behaviors** that must be dropped or reduced; the experiment is invalid if they remain.
- Define **what counts as evidence for the belief vs against** before running the experiment.
- Match the experiment's difficulty to a level the client rates ≥ 60% likely to complete; otherwise reduce.
- Include a **fallback** if the experiment cannot proceed (rain, target person absent, panic crests) — what to do instead, not abandon.
- Plan a **debrief** with explicit comparison of prediction vs outcome and re-rating of belief.
- Document at design time who the client will tell if they want to back out (clinician, support person).
- For OCD / trauma / panic, frame as exposure rather than a "test of whether the feared thing happens" — the goal is tolerating uncertainty, not getting reassurance.

### Must Not

- Do not design an experiment whose only outcome is "I'll feel less anxious" — feelings shift, beliefs may not; require an evidence outcome.
- Do not design experiments that test reality in unsafe ways (e.g., for paranoid beliefs, "test whether they're really following me").
- Do not allow safety behaviors to remain implicit; name and address every one.
- Do not design experiments the client has agreed to only to please the clinician; check willingness explicitly.
- Do not bundle multiple beliefs into one experiment; one belief, one experiment.
- Do not use the experiment to confirm a positive replacement thought; the goal is data, not affirmation.
- Do not omit the post-experiment reformulation; an experiment without debrief is a behavioral activation, not a BE.

## Instructions

1. Confirm the target belief verbatim and the current belief rating (0–100).
2. Make the belief falsifiable: rewrite vague beliefs as specific predictions ("People will judge me" → "≥ 50% of the people in the meeting will visibly disapprove via facial expression, body language, or comments").
3. Identify Theory A (anxious) vs Theory B (alternative) if discovery-frame is appropriate.
4. List safety behaviors actively maintaining the belief; specify which must be dropped for the experiment.
5. Design the experiment: what action, with whom, where, when, for how long. Match to difficulty ≤ client's ≥60%-feasibility threshold.
6. Specify outcome criteria before running:
   - What would confirm the belief? (concrete observable)
   - What would disconfirm it?
   - What would be ambiguous, and how will it be interpreted?
7. Predict (client states what they expect to happen, with probability).
8. Identify cognitive distortions likely to fire post-experiment ("They were just being polite"), and pre-empt them.
9. Plan the debrief: when, with whom, what to record (use the BE record format below).
10. Document fallback if experiment cannot proceed.
11. Re-rate belief after debrief; plan next experiment.

## Output Format

```
=== BEHAVIORAL EXPERIMENT DESIGN ===
Client: [Initials/MRN]    Date: [YYYY-MM-DD]    Session #: [N]
Target diagnosis / protocol: [...]
Linked thought record: [Date / theme]

1) TARGET BELIEF
Wording: "[verbatim from client]"
Belief rating now: [0–100]
Source: [thought record / formulation / session quote]

2) FRAME
[ ] Hypothesis test
[ ] Theory A (anxious) vs Theory B (alternative)
  Theory A: "[...]"
  Theory B: "[...]"

3) PREDICTIONS (what client expects, observable)
- Specific outcome: [...]
- Probability client assigns: [%]

4) SAFETY BEHAVIORS TO REDUCE OR DROP
- [Behavior + how it will be reduced]
- [...]

5) THE EXPERIMENT
What:     [Specific action]
Who:      [Specific person / group]
Where:    [Specific location]
When:     [Specific date/time]
Duration: [N minutes / one instance / staged]
Difficulty (client rating, 0–100): [N]
Feasibility (client estimate of completion likelihood, %): [≥ 60%]

6) WHAT WOULD COUNT AS EVIDENCE
For the belief:     [Specific observable]
Against the belief: [Specific observable]
Ambiguous:          [How will it be interpreted? — agreed in advance]

7) ANTICIPATED COGNITIVE PUSHBACK
- "[Likely distortion: e.g., 'They were just being polite']"
- Pre-empt: [How will we handle this in debrief?]

8) FALLBACK
If experiment cannot run: [Specific alternative, not abandonment]
If panic / urge to escape: [Plan — stay, modify, end?]
Person to contact if backing out: [Clinician / support]

9) DEBRIEF PLAN
When: [Next session / within 24 hours]
Record: [Use BE record template below]

=== BEHAVIORAL EXPERIMENT RECORD (post-run) ===
Date / setting: [...]
What actually happened: [Observable]
Prediction match: [Confirmed / Disconfirmed / Mixed / Ambiguous]
Evidence for belief: [...]
Evidence against belief: [...]
Belief rating now: [0–100] (Δ from pre [+/−N])
What I learned: "[client verbatim, 1–3 sentences]"
Next experiment: [...]
```

## Verification

- [ ] Target belief is a falsifiable proposition with pre-rating.
- [ ] Predictions are observable, not affective.
- [ ] Safety behaviors named and reduction plan documented.
- [ ] Evidence criteria for/against specified before the experiment.
- [ ] Difficulty matches client's feasibility threshold (≥ 60% likely to complete).
- [ ] Fallback specified.
- [ ] Debrief plan present with belief re-rating.
- [ ] No reassurance-style experiments (especially for OCD / health anxiety).
- [ ] Cultural / risk / employment considerations flagged.
- [ ] Single belief per experiment.
- [ ] Gaps flagged; nothing fabricated.
