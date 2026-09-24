---
title: "Q&A Anticipation and Hostile-Question Prep for a Presentation"
category: presentations/narrative-delivery
description: "Prepare for the question period after a pitch, keynote, board presentation, or town hall: map who is in the room and what each wants, build a question bank across clarifying, sceptical, hostile, loaded, and off-topic types, write a short honest answer with its evidence for each, set an 'I don't know' protocol and red lines, decide which answers move into the talk itself, and run a hostile rehearsal. Distinct from domain-science/public-engagement/science_media_interview_prep.md (journalist interviews about a finding) and domain-science/public-engagement/science_congressional_or_parliamentary_testimony_prep.md (legislative testimony)."
techniques:
  - QA-02
  - NE-23
  - RT-05
  - QA-04
  - OC-03
difficulty: intermediate
tags:
  - presentations
  - q-and-a
  - hostile-questions
  - objection-handling
  - public-speaking
  - preparation
  - tough-questions
  - unpopular-announcement
  - town-hall
updated: "2026-09-24"
related_prompts:
  - domain-science/public-engagement/science_media_interview_prep.md
  - domain-science/public-engagement/science_congressional_or_parliamentary_testimony_prep.md
  - domain-presentations/narrative-delivery/presentation_investor_pitch_narrative.md
---

# Q&A Anticipation and Hostile-Question Prep

**Objective:** Make the question period after a presentation the part you are most prepared for rather than least. The prompt maps the audience's interests, generates the questions each segment is likely to ask — including the one you fear most — drafts short, honest answers with the evidence behind them, sets rules for what you will not answer and how you will say "I don't know", and decides which questions are so predictable that the talk should answer them before anyone asks. It ends with a rehearsal script in which the hardest questions are asked in their hardest form.

---

## When to Use

- You are presenting to an audience that includes sceptics, decision makers, or people affected by what you are announcing.
- A pitch, board meeting, town hall, or conference talk has a Q&A you are dreading.
- Past presentations went well until a single question derailed them.
- You are announcing something unpopular (a reorganisation, a price rise, a delay).

**Distinct from:**
- `domain-science/public-engagement/science_media_interview_prep.md` — a journalist-led interview about a research finding, with message maps and bridge phrases for broadcast.
- `domain-science/public-engagement/science_congressional_or_parliamentary_testimony_prep.md` — legislative testimony with formal procedure and an opening statement.
- `domain-negotiation/preparation/negotiation_pre_meeting_rehearsal.md` — a two-party negotiation with asks and walk-aways, not an audience Q&A.
- `domain-presentations/narrative-delivery/presentation_investor_pitch_narrative.md` — builds the pitch's objection table; this prompt drills the live answers.

**When NOT to use:**
- Crisis communications with legal exposure — see `domain-presentations/powerpoint_crisis_management.md` and counsel.
- A press conference; use the media-interview prompt.

---

## Inputs / Context

1. **The presentation.** Summary, key claims, and any numbers shown.
2. **The audience.** Segments present, their stake, and anyone known to be hostile.
3. **Weak points you already know.** Data gaps, delays, unpopular decisions.
4. **Constraints.** Confidential topics, legal limits, commitments you cannot make.
5. **Format.** Q&A length, moderated or open, written questions or live microphone.

---

## Method

### Step 1 — Map the room
For each audience segment, state what it wants from you, what it fears, and what it would count as a good answer.

### Step 2 — Generate the question bank
For each segment, produce questions across six types:
- **Clarifying** — "What do you mean by active user?"
- **Sceptical** — "How do you know this isn't seasonal?"
- **Hostile** — attacks motive or competence: "Isn't this just cost-cutting dressed up?"
- **Loaded / false premise** — "Why did you ignore the safety data?"
- **Off-topic or grandstanding** — a statement with a question mark.
- **The one you fear most** — named explicitly.
Aim for 15–30 questions; merge duplicates across segments.

### Step 3 — Prioritise
Score each question by likelihood (1–3) and damage if answered badly (1–3). Draft full answers for anything scoring 6 or more; one-liners for the rest.

### Step 4 — Draft answers
Each answer: direct response in the first sentence, one piece of evidence, then stop. Under 45 seconds spoken. For loaded questions, correct the premise before answering. For hostile ones, answer the substance and ignore the tone.

### Step 5 — Set the "I don't know" protocol and red lines
Write the exact wording for not knowing ("I don't have that figure; I'll send it to you by Friday") and who follows up. List topics you cannot discuss and a truthful sentence for each ("That's under legal review, so I can't comment on specifics").

### Step 6 — Move predictable answers into the talk
Any question scoring 9 (likely and damaging) should be answered in the presentation itself. Note where.

### Step 7 — Write the hostile rehearsal
Order the top 8–10 questions for a rehearsal partner, phrased in their most aggressive realistic form, with follow-up pushes for the evasive answer. Record what a good answer sounds like for each.

---

## Output Format

```
# Q&A prep — [presentation], [audience]

## Room map
| Segment | Wants | Fears | Good answer looks like |

## Question bank
| # | Segment | Type | Question | Likelihood | Damage | Score |

## Prepared answers (score ≥ 6)
### Q[#]: [question]
Answer (≤45 s): ...
Evidence: ...
If pushed: ...

## "I don't know" wording and follow-up owner
## Red lines
| Topic | Truthful holding sentence |

## Moved into the talk
| Question | Where it's now answered |

## Hostile rehearsal script
1. [question, aggressive form] → push: [...] → good answer sounds like: [...]
```

---

## Verification

- [ ] Every segment in the room map has at least two questions.
- [ ] All six question types present, including the one you fear most.
- [ ] Answers lead with a direct response and cite evidence.
- [ ] Loaded questions have their premise corrected explicitly.
- [ ] Red lines have truthful holding sentences, not evasions.
- [ ] Score-9 questions moved into the talk.
- [ ] Rehearsal script includes follow-up pushes.

---

## False-Positive Prevention

1. **Bridging as evasion.** Pivoting to a message without answering is visible to every audience. Answer first; bridge only after.
2. **Invented answers.** Never draft an answer that asserts a fact the inputs do not support. Use the "I don't know" protocol.
3. **Softball banks.** A bank of only friendly questions is rehearsal for a Q&A you will not get. Include the fear question.
4. **Accepting a false premise.** Answering "why did you ignore the data?" with reasons for ignoring it concedes that you did.
5. **Long answers.** A two-minute answer to a hostile question reads as defensiveness. 45 seconds, then stop.
6. **"No comment" as a red line.** Say truthfully *why* you cannot answer, not just that you won't.
7. **Treating tone as substance.** A rude question can still be a fair one. Answer what was asked.

---

## Example

**Presentation:** an engineering director announcing at an all-hands that on-call will move from team-based to a central platform rotation. **Audience:** 80 engineers, 12 managers, 2 executives.

- **Room map:** engineers — want fairness, fear more nights on call; managers — want coverage, fear losing context; executives — want reliability, fear attrition.
- **Fear question (engineer, hostile, score 9):** "Isn't this just a way to cut on-call pay?" **Moved into the talk:** a slide stating on-call pay is unchanged and the rotation frequency per person drops from every 6 weeks to every 9 (actual, from the draft schedule).
- **Loaded (score 6):** "Why are you ignoring the incidents caused by handovers last year?" → *Premise:* "We didn't ignore them — three of the seven major incidents involved handover gaps, and that's why the runbook requirement is part of this change." Evidence: incident review list.
- **I don't know:** "I don't have the per-team numbers here; I'll post them in the channel by Thursday — Priya owns that."
- **Red line:** individual performance data — "I won't discuss any individual's on-call record in a group setting."
- **Rehearsal push:** after the pay answer — "So why not guarantee it in writing?" Good answer: "Fair ask. It's in the updated policy doc going out today."

---

## Techniques Used

- **QA-02 Adversarial Stress-Test** — hostile rehearsal with follow-up pushes.
- **NE-23 Objection Pre-emption** — score-9 questions moved into the talk.
- **RT-05 Evidence-Based Reasoning** — each answer cites its evidence.
- **QA-04 Uncertainty Acknowledgment** — the "I don't know" protocol and truthful red lines.
- **OC-03 Markdown Table Specification** — room map, scored bank, red-line tables.

---

## Related Prompts

- `domain-science/public-engagement/science_media_interview_prep.md` — journalist interviews.
- `domain-science/public-engagement/science_congressional_or_parliamentary_testimony_prep.md` — legislative testimony.
- `domain-presentations/narrative-delivery/presentation_investor_pitch_narrative.md` — the pitch whose objections this prompt rehearses.
