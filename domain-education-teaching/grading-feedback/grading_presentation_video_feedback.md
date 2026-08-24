---
title: "Student Presentation / Video Feedback"
category: education-teaching/grading-feedback
description: "Generate timestamped feedback on a student presentation or video — content, structure, delivery, and visual aids — that names a single highest-leverage revision while protecting the relational stakes of giving public-performance feedback."
techniques:
  - CM-01  # Context Framing
  - ST-02  # Sequential Steps
  - DS-01  # Framework Application (presentation rubric components)
  - OC-01  # Output Templates
  - RT-04  # Relational Tone
difficulty: intermediate
tags:
  - grading
  - feedback
  - presentation
  - public-speaking
  - video
  - revision
  - middle-school
  - high-school
updated: "2026-05-10"
related_prompts:
  - domain-education-teaching/grading-feedback/grading_essay_feedback_by_rubric_criterion.md
  - domain-education-teaching/teaching_assessment_rubric_builder.md
  - domain-education-teaching/grading-feedback/grading_comment_library_generator.md
---

# Student Presentation / Video Feedback

## Objective

Produce timestamped feedback on a single student presentation, video, or recorded performance. Output addresses content, structure, delivery, and visual aids; quotes specific moments (timestamps) from the student's work; identifies a single highest-leverage revision; and uses tone calibrated to the relational stakes of public-performance feedback.

## When to Use

- Returning recorded presentations or videos for revision
- Conferring prep before a one-on-one with a presenter
- Rehearsal feedback before a live performance
- Calibrating feedback across many presentations from one class

## When NOT to Use

- Whole-class feedback on patterns across many presentations — produce a class memo separately
- Pure content / written feedback on a script — use `grading_essay_feedback_by_rubric_criterion.md`
- Building the rubric in the first place — use `teaching_assessment_rubric_builder.md`

---

## Inputs Needed

- **Student presentation / video:** [Description of the work, ideally with transcript or notes]
- **Length:** [Total time]
- **Topic / assignment:** [What the presentation was about]
- **Rubric:** [If used; criteria + levels]
- **Grade / course:** [...]
- **Stage:** [Rehearsal / draft / final]
- **Audience for the presentation:** [Class peers / panel / public / camera-only]
- **Tone preference:** [Direct / warm / mix — default: direct + warm with extra care for live performance]

---

## Instructions

### Step 1: Watch / Read Twice

The first pass: experience it as the audience would. Note moments that landed and moments that lost you.

The second pass: structured analysis with timestamps.

### Step 2: Score the Components

Score these components, with timestamped evidence for each:

| Component | What it looks at |
|-----------|------------------|
| **Content accuracy and depth** | Is the information correct, sufficient, well-sourced? |
| **Structure** | Does the presentation have a clear opening, development, and close? |
| **Argument or thread** | Is there a through-line the audience can follow? |
| **Delivery (vocal)** | Pace, volume, clarity, intonation, ums/likes |
| **Delivery (physical / on-camera)** | Eye contact (or camera presence), gestures, posture |
| **Visual aids** | Are slides / props legible, useful, not distracting? |
| **Audience awareness** | Did the speaker calibrate to the audience? |
| **Time management** | Did the presentation fit the assigned time? |

For each component, capture **timestamps** of specific moments that justify the rating.

### Step 3: Recognize Public-Performance Vulnerability

Performance feedback is more emotionally costly than essay feedback because the work is the person. Calibrate accordingly:

- Lead with what's working — be specific, not generic
- Frame "not yet" as growth, not deficiency
- Be especially specific (vague critique on performance is worse than specific critique)
- Where possible, name the move; not the person

This isn't about softening rigor — it's about being precise enough that the student can act without taking it as a personal verdict.

### Step 4: Identify the Highest-Leverage Revision

Across components, pick **one** revision that would most lift the next attempt. Common high-leverage moves:

- "The opening doesn't tell us why this matters — open with the stakes"
- "Filler words are crowding out your strongest sentences — pause instead"
- "Slide 4 has too much text; the slide is reading you, not vice versa"
- "Eye contact with camera/audience drops in the middle — that's where the argument loses force"
- "Time ran 2 minutes long — what would you cut, and why?"

### Step 5: Write the Feedback

Use this structured template:

```
WHAT'S WORKING (2–3 specific moments with timestamps)
- [00:12]: "Your opening question 'What if we...?' immediately set the stakes."
- [02:34]: "When you said '___,' the room shifted. That's the move."

WHAT'S NOT YET WORKING (2–3 specific moments with timestamps, named in rubric language)
- [01:45]: Filler words crowd the strongest sentence — five "ums" in 20 seconds.
- [04:10]: Slide reads aloud — audience can't listen and read at the same time.
- [05:30]: Argument shifts from claim to anecdote without a transition.

YOUR NEXT REVISION (one move):
[Verb + object move]
- Where: [Timestamp / section]
- Why: [Which component this lifts]
- How to practice: [Specific rehearsal move]

(Optional) ONE QUESTION TO HOLD:
[A diagnostic that surfaces the speaker's intention]
```

Hard rules:
- Use timestamps for both warm and cool comments
- Name the move, not the person ("the opening doesn't yet hook" not "you're not engaging")
- Don't rewrite the script
- Don't pile on multiple revisions — name one
- Frame in rubric language, not personal preference

### Step 6: Pattern-Matched Next Moves

Match the next move to the diagnosis:

| Diagnosis | Next move |
|-----------|-----------|
| Weak opening | "Cut your first 30 seconds. Open with [the stakes / the question / the surprising fact]." |
| Filler words crowding clarity | "Practice with a count: every um you catch, replace with a 1-second pause. Re-record." |
| Slides over-text | "Reduce slide ___ to ≤5 words. Speak the rest." |
| No transition between sections | "Add one sentence that names the move: 'Now I want to turn from ___ to ___.'" |
| Time over | "Identify the segment that's least connected to your claim. Cut it." |
| Eye contact / camera presence drops | "Mark the spot where you lose the audience. Practice that 30 seconds with eye contact / direct camera." |
| Pace too fast | "Add three pauses, marked in your script — at moments where you want the audience to feel something." |

### Step 7: Tonal Calibration

| Speaker context | Tone adjustment |
|-----------------|-----------------|
| Anxious or new presenter | Lead with two specific things working before any cool comment |
| Strong presenter | Push harder; name the next-level move |
| Resistant to feedback | Quote their own moments back; let evidence do the work |
| Live-performance feedback (no second take) | Frame as "for next time" — don't dwell on what can't be revised |

### Step 8: Self-Check Before Output

- [ ] Did I include timestamps for both warm and cool comments?
- [ ] Did I name moves, not the person?
- [ ] Did I identify a single highest-leverage revision?
- [ ] Is the next-move guidance specific enough to rehearse?
- [ ] Is tone calibrated to the speaker's context?

---

## Output Format

1. Component scoring with timestamps
2. What's working (specific timestamped moments)
3. What's not yet working (specific timestamped moments, in rubric language)
4. Highest-leverage revision with rehearsal guidance
5. (Optional) Diagnostic question
6. Self-check confirmation

---

## False-Positive Prevention

❌ **DON'T:**
- Give vague feedback ("more energy") that the student can't rehearse
- Rewrite the script
- Pile on every issue from a single performance
- Frame in personal terms ("you're nervous") instead of move terms ("the pace is rushed at 2:30")
- Ignore the relational stakes of public-performance critique

✅ **DO:**
- Use timestamps for both warm and cool feedback
- Name the move, not the person
- Identify one highest-leverage revision
- Provide rehearsal guidance, not just evaluation
- Calibrate tone to the speaker's context

---

## Quality Indicators

- [ ] All comments have timestamp anchors
- [ ] Warm comments are as specific as cool ones
- [ ] One highest-leverage revision named
- [ ] Next move is rehearsable
- [ ] Tone matches relational stakes
- [ ] No script rewriting

---

## Techniques Used

| Technique | How It's Applied |
|-----------|-----------------|
| **CM-01** | Topic, audience, stage, and tone preference anchor feedback shape. |
| **ST-02** | Eight-step sequence: watch → score → calibrate → choose → write → match → tune → check. |
| **DS-01** | Presentation-rubric framework (content / structure / delivery / visual / audience / time) structures feedback. |
| **OC-01** | Timestamped warm/cool template enforces consistent structure. |
| **RT-04** | Relational-tone calibration protects the student under public-performance critique. |
