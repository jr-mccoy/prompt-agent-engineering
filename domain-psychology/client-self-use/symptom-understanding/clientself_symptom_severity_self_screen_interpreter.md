---
title: "Self-Screen Score Interpreter (PHQ-9, GAD-7, PCL-5, AUDIT, ACE, MDQ)"
category: psychology/client-self-use/symptom-understanding
description: "Help a client interpret a self-administered screening score (PHQ-9, GAD-7, PCL-5, AUDIT, MDQ, ACE) without diagnosing — what the band means, what the limits are, and what to do with the result."
techniques:
  - ST-04
  - DT-02
  - QA-04
  - CM-02
difficulty: beginner
tags:
  - client-self-use
  - phq-9
  - gad-7
  - pcl-5
  - audit
  - mdq
  - ace
  - self-screening
intended_use: model-testing
updated: "2026-05-08"
---

# Self-Screen Score Interpreter

## Objective

Help a client make sense of a self-administered screening score: what the band typically means, what it does not mean, and what action to take. The output is interpretation support — not a diagnosis.

## When to Use

- A client filled out a screen on a clinic portal, online, or in a clinician's office and wants to understand the result.
- Tracking a screen over time and trying to interpret a change.
- Deciding whether to bring a result to a clinician or wait.

## Inputs / Context

- Which screen: PHQ-9 (depression), GAD-7 (anxiety), PCL-5 (PTSD), AUDIT (alcohol use), MDQ (bipolar spectrum screen), ACE (childhood adversity), other.
- Score(s).
- Date of administration.
- Prior scores if any.
- Current functioning (work, sleep, relationships, self-care).
- Whether the client endorsed any safety items (e.g., PHQ-9 item 9, PCL-5 item 19 / 20).

## Constraints

### Must

- Output sections in order: **What I Filled Out**, **My Score**, **What the Band Typically Means**, **What This Score Does Not Mean**, **Trajectory (if priors exist)**, **Items Worth Re-Reading**, **Action**, **If Any Safety Item Was Endorsed**.
- For each screen, give standard band interpretations and the most-meaningful follow-up questions:
  - **PHQ-9:** 0–4 minimal, 5–9 mild, 10–14 moderate, 15–19 moderately severe, 20–27 severe; item 9 (suicide / self-harm) is always followed up.
  - **GAD-7:** 0–4 minimal, 5–9 mild, 10–14 moderate, 15–21 severe.
  - **PCL-5:** total range 0–80; ≥ 31 commonly used as probable PTSD threshold (varies); item 19 (intrusive memories) and item 20 (avoidance) clusters worth re-reading.
  - **AUDIT:** 0–7 low, 8–15 hazardous, 16–19 harmful, 20+ likely dependence; ≥ 8 = clinical conversation indicated.
  - **MDQ:** Yes to ≥ 7 of 13 symptom items + co-occurring + at least moderate problem = positive screen; warrants follow-up.
  - **ACE:** ≥ 4 = elevated risk for various health outcomes; not destiny — informs context, not diagnosis.
- Always note that scores are screens, not diagnoses, and that a clinician interprets in context.
- Always have a "what this does not mean" section to counter both over-interpretation and dismissiveness.
- Trajectory matters more than single score; a 5-point drop on PHQ-9 is a clinically meaningful improvement.

### Must Not

- Don't diagnose.
- Don't recommend a specific medication.
- Don't predict prognosis from a single score.
- Don't dismiss a low score if function is impaired ("the screen says I'm fine but I'm not" is real and worth bringing to a clinician).
- Don't override a client's reading of their own experience.

## Instructions

1. Identify which screen and the score(s).
2. State the band and typical interpretation.
3. State what the score does not mean.
4. If priors, comment on trajectory.
5. If safety items endorsed, give clear next-step routing.
6. Recommend action proportional to severity and function.

## Output Format

```
=== SELF-SCREEN INTERPRETATION ===

What I Filled Out: [PHQ-9 / GAD-7 / PCL-5 / AUDIT / MDQ / ACE / Other]
Date: [...]
My Score: [N]
Prior scores (if any): [N on date; N on date]

What the Band Typically Means:
[Standard band interpretation for the chosen screen.]

What This Score Does Not Mean:
- Not a diagnosis. A clinician interprets in context (medical, situational, cultural, developmental).
- Not a sentence. Scores change with treatment; many people drop a band within 6–12 weeks of starting evidence-based work.
- Not a green light. A low score in someone whose function is impaired is still worth bringing to a clinician — the screen may be missing what matters for you.
- Not the only data. How you actually live is the data; the screen is one snapshot.

Trajectory:
[If priors: change of N over [interval]; clinically meaningful change for this screen is approximately X.]
- PHQ-9: 5+ points = clinically meaningful change.
- GAD-7: 4+ points = clinically meaningful change.
- PCL-5: 10+ points = clinically meaningful change.

Items Worth Re-Reading:
[Items the client may want to look at again — e.g., for PHQ-9 item 9, for PCL-5 the avoidance / re-experiencing clusters, for MDQ the impairment item, for AUDIT items 4–6.]

Action:
- Minimal / mild range AND function intact: track over time; revisit if pattern persists.
- Moderate range OR function impaired: bring this to a clinician within the next 1–2 weeks.
- Severe range OR significant impairment: reach out to a clinician this week.
- New presentation OR significant deterioration from prior: clinician contact this week.
- If you don't have a clinician: this is itself a reason to start; PCP can be a first stop.

If Any Safety Item Was Endorsed:
- PHQ-9 item 9 endorsed (thoughts of death, self-harm, or being better off dead) at any level above "not at all":
  - This is the most important item; bring it to a clinician this week (or sooner).
  - If you have a plan or intent: contact your clinician today, or 988 (call or text), or go to your nearest ED.
- PCL-5 item 19 (suicidal ideation if your version includes it) or any item describing self-harm: same.
- AUDIT ≥ 16 with daily morning use, blackouts, or withdrawal: medical conversation about safe reduction; abrupt alcohol cessation can be medically dangerous.
- MDQ positive plus periods of decreased need for sleep or risky behavior currently: prescriber consult sooner.

What This Walk-Through Is Not:
A diagnosis. Use this as one input to a conversation with your clinician.
```

## Verification

- [ ] Correct screen identified.
- [ ] Band interpretation matches standard cutoffs.
- [ ] "What this does not mean" present.
- [ ] Trajectory noted with clinically-meaningful change values when priors exist.
- [ ] Safety-item endorsement → clear routing (clinician this week / today / 988 / ED).
- [ ] Low-score-but-impaired pathway preserved.
- [ ] No diagnosis, no medication recommendation.
- [ ] Action proportional to severity and function.
