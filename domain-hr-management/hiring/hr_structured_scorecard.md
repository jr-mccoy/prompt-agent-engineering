---
title: "Structured Hiring Scorecard — Behaviourally Anchored, Independently Submitted"
category: hr-management/hiring
description: "Build the scoring instrument interviewers fill in: one scorecard per stage covering only that stage's attributes, behaviourally anchored levels, a required evidence field per rating, an explicit insufficient-evidence option, and a hire recommendation separated from the numeric scores. Refuses scorecards with unanchored numeric scales or a single overall impression field."
techniques:
  - ST-03
  - CM-02
  - QA-04
  - QA-18
  - OC-03
difficulty: intermediate
tags:
  - hiring
  - scorecard
  - behavioural-anchors
  - evidence-based
  - anti-bias
updated: "2026-09-22"
related_prompts:
  - domain-hr-management/hiring/hr_interview_loop_design.md
  - domain-hr-management/hiring/hr_job_description_writer.md
  - domain-hr-management/performance-reviews/hr_performance_review_meta_prompt.md
---

# Structured Hiring Scorecard

**Objective:** Produce the instrument an interviewer actually fills in — one scorecard
per stage, scoped to that stage's owned attributes, with **behaviourally anchored**
levels, a mandatory evidence field beside every rating, a first-class
**insufficient evidence** option, and the hire recommendation recorded separately from
the scores. Unanchored 1–5 scales and single "overall impression" fields are refused.

**When to Use:**
- The interview loop exists and interviewers need something to record into.
- Debriefs produce numbers that nobody can explain or defend.
- Two interviewers give the same candidate a 3 and a 5 and there is no way to tell why.
- Feedback consists of "strong candidate" with no evidence attached.

**When NOT to use:**
- You need a **review** rubric for someone already employed — that is
  `../performance-reviews/hr_performance_review_meta_prompt.md`, the domain's anchor,
  which generates role- and level-tailored *review* scaffolds. Different artifact,
  different moment, different evidence base: a review scores observed work over a
  period; this scores inferences from a conversation.
- You need to decide which attributes to test and where — that is
  `hr_interview_loop_design.md`. Run it first; this instrument is derived from its
  attribute-to-stage matrix.
- You need the take-home's grading rubric specifically — that is inside
  `hr_hiring_screen_challenge_designer.md`.

---

## Context Gathering

1. **The loop's output**
   - "The attribute-to-stage matrix from `hr_interview_loop_design.md`."
   - "Which attributes are non-negotiable, and which are developable in role?"

2. **The role's bar**
   - "For each attribute, what does 'meets the bar for this level' look like
     concretely?"
   - "What does one level above look like? One level below?"

3. **Who scores**
   - "Which interviewers run which stage, and how experienced are they at
     interviewing?"
   - "Is there a bar-raiser or cross-team interviewer?"

4. **Current pain**
   - "Show me a completed scorecard from a recent loop." — the fastest diagnosis
     available. Look for whether any rating has evidence attached.

---

## Method

### Step 1 — One scorecard per stage, scoped to that stage

Not one master scorecard used everywhere. Each stage's scorecard lists **only the
attributes that stage owns** from the loop design. An interviewer asked to rate an
attribute their stage did not probe will rate it anyway, from general impression, and
that reading enters the debrief looking like evidence.

### Step 2 — Anchor every level behaviourally

This is the step that makes the instrument work. A numeric scale without anchors
records the interviewer's calibration, not the candidate's ability, which is why two
interviewers produce a 3 and a 5.

For each attribute, write what each level **looks like** — an observable behaviour, not
an adjective:

| Level | Anchor shape | Example (attribute: debugging an unfamiliar system) |
|---|---|---|
| Below bar | The behaviour you actually saw that falls short | "Guessed at causes without reading the error; did not ask for logs when offered" |
| At bar | The behaviour that meets the level | "Formed a hypothesis, said what would confirm it, asked for the specific evidence, narrowed twice" |
| Above bar | The behaviour that exceeds it | "Also named what they would add to make the next failure diagnosable" |

Four levels is usually right: below, approaching, at, above. Avoid five — the middle of
an odd scale absorbs every uncertain rating and the instrument stops discriminating.

Write anchors in the past tense and in terms of what the candidate *did*. An anchor
phrased as a trait ("is a strong debugger") cannot be checked against a transcript.

### Step 3 — Require evidence beside every rating

Every rating has a mandatory adjacent field: **what the candidate said or did that
supports this**. Not a summary, not an impression — a quote or a described action.

The rule that gives this teeth: **a rating with no evidence does not count at debrief.**
That must be stated on the scorecard itself and enforced by whoever runs the debrief.
Without enforcement the field is filled with "see above".

### Step 4 — Make insufficient evidence a first-class option

Every attribute offers **INSUFFICIENT EVIDENCE** as a selectable verdict, ranked
alongside the levels rather than hidden as a blank.

Interviewers rate attributes they did not probe because the form has a box and blank
looks like carelessness. Given a legitimate option, they use it, and the debrief learns
something true: this attribute was not established, and either it does not matter or
the loop has a gap. A blank teaches nothing; an explicit "not established" is a
finding.

### Step 5 — Separate the recommendation from the scores

Two distinct fields:

- **Attribute ratings** — the evidence-backed readings above.
- **Recommendation** — hire / no hire / hire at a different level, with a one-paragraph
  reason.

They are separated because they answer different questions and because collapsing them
lets a strong overall impression back-fill the individual ratings. An interviewer who
must write "I rated communication at bar and problem-solving below bar, and I still
recommend hire, because…" is doing visible reasoning. One who writes only "strong yes"
is not.

Forbid a numeric overall score. Summing anchored attribute ratings into a single number
implies a weighting nobody agreed and discards the shape of the result — and a
candidate who is above bar on three attributes and below bar on a non-negotiable one is
not an average.

### Step 6 — Add the bias checks that are structural

Three, all mechanical:

- **Submit before discussing.** Printed on the scorecard: submit before reading any
  other interviewer's. Per `hr_interview_loop_design.md` step 5 and the same discipline
  `../performance-reviews/hr_calibration_facilitator.md` applies to reviews.
- **Score attributes, not the person.** The form has no field for "culture fit",
  "likeability" or "would I want to work with them" — those are documented bias vectors
  and, if a real requirement is hiding behind them, it belongs in the attribute list as
  an observable behaviour.
- **Note the conditions.** A short field for anything that affected the sample:
  technical problems, the candidate being unwell, a rushed session, an interruption.
  This is what stops a bad connection being recorded as poor communication.

---

## Output Format

One block per stage.

```markdown
## Scorecard — [stage name] · [role], [level]
**Interviewer:** ___  **Date:** ___
**Submit this before reading any other interviewer's scorecard.**

### [Attribute 1] — [non-negotiable / developable]
*What this stage probes:* [one line]

| | Anchor |
|---|---|
| Above bar | [observable behaviour] |
| At bar | [observable behaviour] |
| Approaching | [observable behaviour] |
| Below bar | [observable behaviour] |
| **Insufficient evidence** | Not probed, or the sample does not support a rating |

**Rating:** ☐ Above ☐ At ☐ Approaching ☐ Below ☐ Insufficient evidence
**Evidence — what they said or did (required; a rating with no evidence does not count at debrief):**
> ___

### [Attribute 2] …

---

### Recommendation
☐ Hire  ☐ Hire at a different level: ___  ☐ No hire  ☐ Cannot say — [what is missing]

**Reason (one paragraph, referring to the ratings above):**
___

### Conditions affecting this sample
___

*No overall numeric score. Attribute ratings are not summed.*
```

---

## Verification

- [ ] One scorecard per stage, covering only that stage's owned attributes
- [ ] Every attribute has anchors at every level, written as observable past-tense behaviour
- [ ] Four levels, not five
- [ ] Every rating has a mandatory adjacent evidence field
- [ ] The "no evidence, does not count" rule is printed on the form
- [ ] INSUFFICIENT EVIDENCE is a selectable option on every attribute
- [ ] Recommendation is a separate field from the ratings
- [ ] No overall numeric score, and no field for fit, likeability or affinity
- [ ] Submit-before-discussing is printed on the form
- [ ] Non-negotiable attributes are marked as such

**False-positive prevention.** The dominant failure is anchors written as adjectives —
"excellent communicator", "good problem solver". Those are the unanchored scale with
extra words, and they produce the same divergence. Test each anchor against a
transcript: could two people reading the same transcript disagree about whether the
anchor was met? If yes, it describes a judgement rather than a behaviour. Rewrite it as
something the candidate did.

The second failure is an evidence field filled with restated ratings — "showed strong
debugging skills" beside a rating of Above. That is the rating again, not evidence. The
field wants a quote or a described action, and the debrief owner has to send it back
when it does not contain one.

The third is keeping a culture-fit field because it feels informative. It is
informative — about the interviewer. If there is a genuine requirement underneath it,
name the behaviour: "explains technical decisions to non-technical colleagues without
condescension" is observable and checkable. "Fit" is neither.

The fourth is summing to an overall score because stakeholders want one number. The
shape matters more than the total: below bar on a non-negotiable attribute is
disqualifying regardless of the other ratings, and an average hides exactly that.

**Evidence-anchored and bias-checked, per this domain's standing principles.** Every
mechanism here is structural — anchors, mandatory evidence, independent submission, no
affinity field. None of them asks interviewers to be less biased; they change what the
form makes easy.

---

## Related

- `hr_interview_loop_design.md` — supplies the attribute-to-stage matrix this is derived from
- `hr_job_description_writer.md` — supplies the outcomes the attributes come from
- `hr_hiring_screen_challenge_designer.md` — the take-home's own weighted rubric
- `../performance-reviews/hr_performance_review_meta_prompt.md` — the review-scaffold counterpart
- `../performance-reviews/hr_calibration_facilitator.md` — independent-then-discuss, applied to ratings
