---
title: "CBT Thought Record Drafter (7-Column)"
category: psychology/modalities/cbt
description: "Draft a structured 7-column CBT thought record with cognitive restructuring and a balanced alternative thought, from session content or client homework."
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
  - thought-record
  - cognitive-restructuring
  - homework
  - Beck
  - Padesky
intended_use: model-testing
updated: "2026-05-19"
related_prompts:
  - domain-psychology/modalities/cbt/psychology_cognitive_distortion_identifier.md
  - domain-psychology/modalities/cbt/psychology_cbt_behavioral_experiment_designer.md
  - domain-psychology/modalities/cbt/psychology_cbt_relapse_prevention_module.md
---

# CBT Thought Record Drafter (7-Column)

## Objective

Draft a complete 7-column CBT thought record (Beck / Greenberger & Padesky lineage) from session content, an in-session sample, or client homework. The thought record must isolate one specific situation, capture the hot automatic thought, weigh evidence in both directions, and produce a balanced alternative thought with pre/post mood ratings.

The 7 columns:

1. **Situation** (when / where / who / what — concrete and time-bounded)
2. **Moods** (single-word emotions with 0–100 intensity, before)
3. **Automatic thoughts / images** (with the **hot thought** identified)
4. **Evidence that supports the hot thought**
5. **Evidence that does not support the hot thought**
6. **Alternative / balanced thought** (with 0–100 belief rating)
7. **Re-rate moods** (same emotions, 0–100 intensity, after)

## When to Use

- Mid-CBT-protocol for depression, GAD, social anxiety, health anxiety, or low self-esteem.
- After identifying cognitive distortions but before behavioral experiments.
- As recurring between-session homework where client logs 3–5 records/week.
- In-session demonstration with a recent activating event (Beck's "guided discovery").
- Adapting for inpatient, intensive-outpatient, or telehealth modalities.

## Inputs / Context

- Brief case formulation (presenting problem, primary diagnosis, current target symptoms).
- A specific recent situation the client wants to work on (date/time anchored, ≤ 60 minutes long, single event).
- Client's stated moods at the time (emotions and intensities).
- Verbatim or paraphrased automatic thoughts/images, with the client's identification of which thought is "hottest" (most distressing).
- Reading level, age, language; cultural / religious context that may shape what counts as evidence.
- Whether record is for between-session homework or in-session demonstration.
- Any active risk concerns (record is not a substitute for risk plan or safety planning).

## Constraints

### Must

- Output exactly 7 columns labeled in canonical order.
- Column 1 (Situation) is concrete, time-bounded, and observable — "Tuesday 8:15 a.m., kitchen, after partner left without saying goodbye," not "lately, with my partner."
- Column 2 lists emotions as single words with 0–100 intensity ratings (sad 70, anxious 60, angry 40), not blended narrative.
- Column 3 lists automatic thoughts as discrete propositions; the **hot thought** is explicitly marked (e.g., circled, asterisked, or labeled HOT).
- Columns 4 and 5 list **evidence**, not other thoughts or feelings — observable facts, past examples, others' behavior, base rates.
- Column 6 produces a **balanced** alternative thought (not a positive-thinking replacement); it acknowledges what column 4 captured. Include a 0–100 belief rating for the alternative.
- Column 7 re-rates the **same** emotions from column 2; do not add new emotions.
- Include any work-in-progress markers when client could not fill a column (`[client to complete: evidence against]`).
- If applicable, append a 1-sentence homework hand-off ("Complete 3 more records before next session, one of which involves [trigger]").

### Must Not

- Do not collapse multiple situations into one row; one row = one situation.
- Do not write affirmations or rationalizations in column 6 ("It will all be fine," "Don't think about it"). The alternative must address evidence.
- Do not list feelings ("I felt rejected") in evidence columns; feelings belong in column 2.
- Do not generate thoughts the client did not actually have; mark any clinician-suggested wording as `[clinician draft — confirm with client]`.
- Do not finalize a thought record for high-risk thoughts (e.g., active suicidal ideation, command hallucinations) without integrating risk plan; flag and route.
- Do not omit the hot-thought marker; without it, restructuring drifts.

## Instructions

1. Confirm one specific situation with date/time anchoring; restate it back to the client.
2. Elicit emotions and intensities (column 2) **before** asking about thoughts (the mood anchors the record).
3. List automatic thoughts/images (column 3); ask "Which of these, if true, would be the most distressing?" to identify the hot thought.
4. **Evidence FOR the hot thought** (column 4): "What evidence makes you believe this is true?" Push for concrete instances, not feelings.
5. **Evidence AGAINST the hot thought** (column 5): use Beckian discovery questions:
   - "What would you tell a friend in this situation?"
   - "What evidence have you overlooked or discounted?"
   - "Has this prediction been wrong before?"
   - "How would someone you respect see this?"
6. Generate the **balanced alternative** (column 6) that integrates columns 4 and 5. Confirm client believes it ≥ 30 (if < 30, the alternative is too far from the hot thought; iterate).
7. Re-rate the original emotions (column 7). Note any mood that did or did not move; clinical hypotheses follow.
8. Append: takeaway, between-session homework, and any follow-up belief to test in a behavioral experiment.

## Output Format

```
=== CBT THOUGHT RECORD ===
Client: [Initials / MRN]    Date: [YYYY-MM-DD]    Session #: [N]    Modality: [Outpatient / Telehealth]
Diagnosis (working): [...]    Protocol stage: [Early / Mid / Late]

1) SITUATION (when / where / who / what)
[Concrete, time-bounded, observable.]

2) MOODS (pre)
- [emotion 1]: [0–100]
- [emotion 2]: [0–100]
- [...]

3) AUTOMATIC THOUGHTS / IMAGES
- [thought 1]
- [thought 2] *** HOT THOUGHT ***
- [image, if any]
- [...]

4) EVIDENCE THAT SUPPORTS THE HOT THOUGHT
- [observable fact / past instance / others' behavior]
- [...]

5) EVIDENCE THAT DOES NOT SUPPORT THE HOT THOUGHT
- [counterexample / overlooked fact / alternative explanation]
- [base rate / friend-perspective / past disconfirmation]
- [...]

6) BALANCED / ALTERNATIVE THOUGHT
"[Wording that integrates 4 and 5; not affirmation, not catastrophizing]"
Belief rating: [0–100]

7) MOODS (post — same emotions as column 2)
- [emotion 1]: [0–100]    (Δ [+/−N])
- [emotion 2]: [0–100]    (Δ [+/−N])
- [...]

TAKEAWAY
[1–2 sentences from the client about what shifted.]

HOMEWORK / FOLLOW-UP
- [Next record assignment.]
- [Belief to test via behavioral experiment, if any.]
- [Hot thought theme to track across records.]

CLINICIAN NOTES
- [Pattern across recent records.]
- [Cognitive distortion(s) most active.]
- [Risk re-screen if applicable.]
```

## Verification

- [ ] Exactly one situation, time-bounded.
- [ ] Emotions in column 2 are single-word with 0–100 ratings.
- [ ] Hot thought explicitly marked in column 3.
- [ ] Columns 4 and 5 contain evidence, not feelings or other thoughts.
- [ ] Column 6 alternative believed ≥ 30 by client; integrates columns 4 and 5.
- [ ] Column 7 re-rates the same emotions; deltas reported.
- [ ] No fabricated client wording; clinician drafts marked.
- [ ] Homework assignment present.
- [ ] Risk concerns flagged and routed if applicable.
- [ ] Gaps flagged with `[client to complete]` markers, not auto-filled.
