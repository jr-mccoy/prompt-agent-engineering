---
title: "Conversation Transcript QA Rubric — Anchored Dimensions, Critical Fails, Stratified Sampling, and Calibrated Review"
category: voice-conversational-ui/analytics
description: "Build a rubric for reviewing individual chatbot, voice bot, or AI phone-agent conversations: named dimensions with anchored 0-1-2 scales, critical-fail items that override the score, a stratified sampling plan that over-samples escalations and risky intents, reviewer calibration, and the conditions under which an LLM judge may score at scale; distinct from the metrics framework (aggregate KPIs) and log optimization (funnel and clustering across thousands of sessions)."
techniques:
  - DP-03
  - QA-17
  - QA-22
  - DS-35
  - QA-12
difficulty: intermediate
tags:
  - conversation-qa
  - rubric
  - transcript-review
  - llm-as-judge
  - analytics
  - quality-assurance
  - review-chat-logs
  - is-bot-helping
  - bot-mistakes
updated: "2026-09-24"
related_prompts:
  - domain-voice-conversational-ui/analytics/analytics_conversation_metrics_framework.md
  - domain-voice-conversational-ui/analytics/analytics_conversation_optimization.md
  - domain-prompt-engineering/evaluation/rubrics/rubric_pairwise_vs_pointwise.md
---

# Conversation Transcript QA Rubric

**Objective:** Give reviewers — human or model — a rubric that turns one bot
conversation into a reproducible score and a short list of named defects, and
a sampling plan that makes the weekly review say something true about the
whole bot.

**When to Use:**
- Metrics look fine but customers complain; you need to read conversations
  systematically, not anecdotally.
- Several reviewers score the same bot and disagree.
- You want to use an LLM to score transcripts at scale and need a rubric it
  can be checked against.
- A new bot version is launching and you need a before/after quality read.

**Not this prompt if:**
- You need aggregate KPIs (containment, fallback rate, CSAT) and alerting →
  `domain-voice-conversational-ui/analytics/analytics_conversation_metrics_framework.md`.
- You need funnel drop-off, utterance clustering, or A/B tests across logs →
  `analytics_conversation_optimization.md`.
- You are scoring *human* agents' calls for coaching →
  `domain-sales-customer/support/support_agent_interaction_qa_scorecard.md`;
  this rubric scores the bot's behaviour.
- You are choosing between pairwise and pointwise scoring for a model eval →
  `domain-prompt-engineering/evaluation/rubrics/rubric_pairwise_vs_pointwise.md`.

## Inputs

1. **Bot scope**: intents, channels (chat/voice), and what "resolved" means.
2. **Policies** the bot must follow: disclosures, refunds, regulated advice, escalation rules.
3. **Transcript access**: text, audio, metadata (intent, outcome, handoff).
4. **Volume** and reviewer capacity per week.
5. **Known problem areas**, if any.

## Method

1. **Choose named dimensions (QA-17).** Five to seven, each scored separately,
   never collapsed before reporting:
   - **Outcome** — did the customer get what they came for, or a correct no?
   - **Accuracy** — were facts, prices, and policies stated correctly?
   - **Understanding** — did the bot grasp the request, including corrections?
   - **Recovery** — when it failed, did it recover without loops?
   - **Handoff** — did it transfer when it should, and not when it shouldn't?
   - **Tone** — consistent with the persona, appropriate to the customer's state.
   - **Voice only: audio** — turn-taking, cut-offs, TTS misreadings.
2. **Anchor each scale (DP-03).** 0 / 1 / 2 with a concrete description for
   each point, written so two reviewers reach the same score. Add a
   **Not applicable** option (e.g., Handoff in a conversation that did not need one).
3. **List critical fails.** Items that fail the whole conversation regardless
   of other scores: a false statement about money, safety, or policy; a
   promise the business cannot keep; exposure of personal data; ignoring an
   explicit request for a person; continuing after a customer signals danger
   or distress without the defined response.
4. **Plan the sample (QA-22).** Stratify by intent, outcome (resolved,
   escalated, abandoned), and channel. Over-sample escalations, abandonments,
   low-volume high-risk intents, and conversations after a release; include a
   random slice so the sample is not only failures. Record the weights so
   results can be re-weighted to the population.
5. **Calibrate reviewers.** Two reviewers score the same 20–30 transcripts;
   compare per dimension; rewrite anchors where they disagree; repeat until
   agreement is acceptable to the team `[measure]`. Re-calibrate monthly.
6. **Screen false defects (QA-12).** Before logging a defect, check: was the
   "no" correct under policy? Did the customer change their goal? Is the
   "wrong" fact actually out of date in the source, not the bot? Is the
   transcript missing turns (ASR errors, dropped messages)?
7. **Gate LLM scoring (DS-35).** Use a model judge only after it scores a
   human-labelled set with agreement comparable to human–human agreement
   `[measure]`, per dimension. Keep critical fails human-confirmed, and
   spot-check a fixed share of model scores each week.
8. **Report** per dimension and critical-fail rate, with confidence: **High**
   (calibrated reviewers, adequate sample in stratum), **Medium** (small
   stratum), **Low** (uncalibrated or model-only).

## Output Format

```
## Scope & definitions
What "resolved" means · channels · policies referenced
## Rubric
| Dimension | 0 | 1 | 2 | N/A when |
## Critical fails
## Sampling plan
| Stratum | Population share | Sample n | Weight |
## Calibration protocol
## False-defect screen
## LLM-judge gate
## Review sheet (per transcript)
Transcript ID · stratum · scores per dimension · critical fail (Y/N + quote) · defects (named) · reviewer
## Weekly report template
Per-dimension distribution · critical-fail rate · top named defects · confidence
```

## Verification

- [ ] Every dimension has anchors for 0, 1, and 2 and an N/A rule.
- [ ] Critical fails are observable in a transcript and each needs a quoted line.
- [ ] Escalated and abandoned conversations are over-sampled and weights recorded.
- [ ] Two reviewers have scored a shared set, and anchors were revised where they disagreed.
- [ ] Model scoring is gated on agreement with human labels, per dimension.
- [ ] Results are reported per dimension, not only as a single total.

## False-Positive Prevention

1. **A correct refusal is a good outcome.** Score "the bot said no, correctly,
   and explained" as Outcome 2, not a failure.
2. **Do not blame the bot for bad source data.** If the knowledge base is
   wrong, log a content defect, not an Accuracy defect for the bot's reasoning.
3. **Do not score ASR errors as understanding failures without listening.**
   For voice, check the audio when the transcript looks garbled.
4. **Do not average away critical fails.** One critical fail outweighs high
   scores elsewhere; report its rate separately.
5. **Do not sample only complaints.** A failure-only sample cannot estimate
   quality; keep a random slice.
6. **Do not trust an uncalibrated model judge.** Agreement with humans must be
   measured per dimension before its scores are reported.
7. **Do not penalize tone for brevity.** Short, correct answers suit many
   intents; score tone against the persona, not word count.

## Example

**Input (summary):** Telecom support chat bot; intents: billing questions,
plan changes, outage checks, cancellations (to a human). 30,000 chats/month;
two reviewers × 3 hours/week.

```
## Scope & definitions
Resolved = customer's question answered correctly or task completed, or
correct transfer made. Channel: web chat. Policies: price-quote rules; all
cancellations go to a person.

## Rubric
| Dimension | 0 | 1 | 2 | N/A when |
|---|---|---|---|---|
| Outcome | Not resolved, no transfer | Resolved after avoidable friction | Resolved or correct transfer | — |
| Accuracy | Wrong price/policy stated | Vague but not wrong | All facts correct | No facts stated |
| Understanding | Misread request, never corrected | Needed ≥2 clarifications | Understood first time or on 1 clarification | — |
| Recovery | Looped ≥2 times | Recovered after 1 loop | No loop or clean recovery | No failure occurred |
| Handoff | Needed and not offered / offered wrongly | Offered late | Correct and timely | Not needed |
| Tone | Dismissive or off-persona | Neutral but mismatched to upset customer | Fits persona and customer state | — |

## Critical fails
Quoted a price not in the price book · promised a credit · showed another
customer's data · ignored "let me speak to someone" · processed a cancellation itself.

## Sampling plan (60 chats/week)
| Stratum | Pop. share | n | Weight (pop. share ÷ sample share of 55) |
|---|---|---|---|
| Resolved, random | 70% | 20 | 1.93 |
| Escalated | 20% | 20 | 0.55 |
| Abandoned | 10% | 15 | 0.37 |
| Plan changes (high-risk), any outcome | — | 5 | reported separately, not weighted |

## Calibration protocol
Week 1: both reviewers score the same 25 chats; disagreement on Understanding
(1 vs 2) → anchor rewritten to "on 1 clarification." Monthly re-run of 10.

## False-defect screen
Check price against the price book dated that day; check for customer goal
change; check for missing turns in the chat log.

## LLM-judge gate
Pilot model judge on 200 human-labelled chats; report per-dimension agreement
[measure]; critical fails always human-confirmed; 10% weekly spot-check.

## Review sheet (one entry)
ID [chat id] · Abandoned · Outcome 0 · Accuracy N/A · Understanding 1 ·
Recovery 0 · Handoff 0 · Tone 1 · Critical fail: Y — customer typed "just
let me talk to a person" twice; bot re-offered the menu.
Defects: HANDOFF-IGNORED, LOOP-MENU. Reviewer: A.

## Weekly report template
Per-dimension distribution (weighted) · critical-fail rate with quotes ·
top 3 named defects · confidence per stratum.
```

## Techniques Used

- **DP-03 Anchored Scoring Scales** — 0/1/2 anchors per dimension.
- **QA-17 Named Scores for Multi-Dimensional Metrics** — dimensions reported separately.
- **QA-22 Evaluation Diversity Planning** — stratified, weighted sampling.
- **DS-35 LLM-as-Judge with Rubric** — gated model scoring.
- **QA-12 False Positives Identification** — the false-defect screen.

## Related Prompts

- `domain-voice-conversational-ui/analytics/analytics_conversation_metrics_framework.md` — aggregate KPIs.
- `domain-voice-conversational-ui/analytics/analytics_conversation_optimization.md` — log-scale analysis.
- `domain-prompt-engineering/evaluation/rubrics/rubric_pairwise_vs_pointwise.md` — choosing the scoring mode.
