---
title: "CBT for Social Anxiety — Session Plan with Video-Feedback and Safety-Behavior Dropping"
category: psychology/modalities/cbt
description: "Generate a CBT for Social Anxiety session plan (Clark & Wells / Heimberg lineage) including in-session role-play with video-feedback, dropping safety behaviors, and attention re-training."
techniques:
  - ST-04
  - RT-02
  - DT-02
  - ED-04
  - QA-04
  - CM-02
difficulty: advanced
tags:
  - CBT
  - social-anxiety
  - Clark-Wells
  - Heimberg
  - video-feedback
  - safety-behaviors
  - attention-training
intended_use: model-testing
updated: "2026-05-19"
related_prompts:
  - domain-psychology/modalities/cbt/psychology_cbt_behavioral_experiment_designer.md
  - domain-psychology/modalities/cbt/psychology_cbt_thought_record_drafter.md
  - domain-psychology/modalities/cbt/psychology_cbt_specific_phobia_one_session_treatment.md
---

# CBT for Social Anxiety — Session Plan with Video-Feedback and Safety-Behavior Dropping

## Objective

Generate a 50–90 minute CBT for Social Anxiety Disorder (SAD) session plan placed within Clark & Wells's cognitive model or Heimberg's group-CBT model. The plan integrates self-focused attention identification, safety-behavior dropping, an in-session role-play behavioral experiment with video-feedback (or live observer feedback), and homework that includes attention re-training and graded in-vivo exposure.

## When to Use

- DSM-5-TR Social Anxiety Disorder confirmed (LSAS ≥ 60 or comparable severity).
- Mid-protocol (sessions 4–10) after formulation, psychoeducation, and initial cognitive work.
- Telehealth: video-feedback can still be used via screen recording with consent.
- Group CBT format: adapt role-play to involve peer audience.
- Not appropriate for clients with active psychosis, severe paranoia about being recorded, or untreated trauma where video would re-traumatize.

## Inputs / Context

- LSAS-SR / SPIN / Mini-SPIN scores and trajectory.
- Formulation summarizing: feared social situation type(s), self-focused attention content (what client sees in their mind's eye when anxious), safety behaviors (specific named list), and post-event processing patterns.
- Top 1–3 social predictions (e.g., "I'll blush and they'll mock me," "I'll go blank and they'll think I'm stupid").
- Consent for video/audio recording (or live observer feedback if video declined).
- Cultural context (some "safety behaviors" may be culturally normative — verify before targeting).
- Modality, session length (90 min if doing video-feedback fully).
- Hierarchy of feared social situations.

## Constraints

### Must

- Use Clark-Wells frame: the **internal image** the client has of themselves while anxious is the primary target, not just the social situation.
- Identify safety behaviors with the client (gripping cup, rehearsing every word, avoiding eye contact, scanning faces for disapproval, pre-drinking) and plan which to drop in the role-play.
- Conduct two role-play exposures back-to-back:
  - **Round 1: with safety behaviors and self-focused attention.** Client predicts how they'll look and how the audience will respond.
  - **Round 2: dropping safety behaviors and shifting attention externally.** Same role-play scenario.
- Use video-feedback or live observer feedback between rounds: client first predicts what the recording will show, then watches it (or hears observer report) to compare prediction to data.
- Frame attention training (Wells) or task-concentration training (Bögels) as homework, not as a coping technique.
- Plan in-vivo exposure homework that drops named safety behaviors.
- For minors / vulnerable clients, obtain assent + parental consent for recording, and document retention/destruction.
- Document pre/post anxiety ratings, prediction match, and belief rating shift.

### Must Not

- Do not allow the client to use video-feedback to confirm "I look as bad as I think." Frame it: prediction vs reality, then look.
- Do not retain video without explicit retention plan; default is delete in session after viewing.
- Do not drop all safety behaviors at once if the client is in severe distress; stage them.
- Do not use the role-play as performance evaluation; the goal is data on internal image vs external reality, not performance critique.
- Do not skip the Clark-Wells internal-image elicitation (most maintenance work happens here).
- Do not use loud reassurance ("You were great!") — that becomes a safety behavior.
- Do not record video if client has trauma history involving being filmed / observed, or psychosis with paranoia.

## Instructions

1. Open with LSAS / SPIN data and last week's exposure homework.
2. Elicit the **internal image** — "When you walk into [feared situation], what do you see in your mind's eye that you look like?" Note details (sweating, shaking, blushing, dead expression).
3. Confirm the role-play scenario (presentation to one observer, conversation with stranger, asking a question in a meeting).
4. **Round 1:** with safety behaviors and self-focused attention.
   - Pre-rating: anxiety (0–100), predicted self-appearance (rating 0–100 "how visibly anxious you'll look").
   - Run role-play (3–8 min).
   - Post-rating: anxiety, predicted appearance.
5. Watch video (or receive observer feedback). Client first restates prediction; then compare to data.
6. Process internal image vs external reality discrepancy.
7. **Round 2:** drop named safety behaviors; shift attention to the task/other person.
   - Pre-rating; run; post-rating; video review; process.
8. Homework: attention training audio (Wells) or task-concentration practice; one in-vivo exposure with named safety behaviors dropped; thought record on post-event processing if it occurs.
9. Address post-event processing as a separate maintenance factor: schedule a "no rumination" window with stimulus control.

## Output Format

```
=== CBT-SAD SESSION PLAN ===
Client: [Initials/MRN]    Session #: [N of ~14]    Date: [YYYY-MM-DD]    Length: [90 min]    Modality: [...]
LSAS / SPIN: [Score, trend]
Consent for recording: [Y/N; retention: delete in session]

INTERNAL IMAGE (Clark-Wells anchor)
"When you walk into [situation], what do you see in your mind's eye?"
Client's image: "[verbatim]"
Felt-sense rating of how anxious they look (0–100): [N]

ROLE-PLAY SCENARIO
[Specific scenario; observer or partner; duration]

SAFETY BEHAVIORS (current)
- [Behavior + function]
- [...]
Drop in Round 2: [Subset]

ROUND 1: WITH SAFETY BEHAVIORS + SELF-FOCUSED ATTENTION
Pre-rating: anxiety [N], predicted "how anxious I'll look" [N]
Prediction: "[verbatim]"
Post-rating: anxiety [N]
Video / observer feedback: [Specific observable data]
Discrepancy (predicted vs data): [...]

ROUND 2: DROPPING SAFETY BEHAVIORS + EXTERNAL ATTENTION
Safety behaviors dropped: [list]
Attention shift instruction: "[focus on the other person's words and face, not your sensations]"
Pre-rating: anxiety [N], predicted appearance [N]
Post-rating: anxiety [N]
Video / observer feedback: [Specific observable data]
Discrepancy: [...]

COGNITIVE PROCESSING
- Updated internal image: "[client's reformulation after video]"
- Belief rating in original prediction: [pre N → post N]
- Cognitive distortion(s) most active: [...]

HOMEWORK
- Attention training (Wells) / task-concentration: [N minutes daily, audio file]
- In-vivo exposure: [Specific situation, when, safety behaviors dropped]
- Thought record on post-event processing if rumination occurs
- Post-event processing limit: [stimulus-control plan]

OUTCOME / RISK
- LSAS / SPIN re-screen due: [Date]
- Comorbidity check (depression, alcohol use): [Status]
- Next session focus: [...]
```

## Verification

- [ ] Internal image elicited and recorded verbatim.
- [ ] Role-play scenario is specific and feasible.
- [ ] Round 1 / Round 2 contrast: safety behaviors dropped in Round 2.
- [ ] Pre/post ratings and predictions per round.
- [ ] Video feedback (or live observer) compares prediction to data, not used as reassurance.
- [ ] Attention re-training homework specified.
- [ ] In-vivo homework drops named safety behaviors.
- [ ] Post-event processing addressed.
- [ ] Consent and video retention plan documented.
- [ ] Cultural / trauma / psychosis screen for recording-suitability.
- [ ] No fabricated client wording.
