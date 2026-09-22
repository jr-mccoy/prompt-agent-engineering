---
title: "Newsletter Issue — Write One That Keeps the Promise and Earns the Next Open"
category: professional-writing/writing
description: "Draft a single newsletter issue against a stated promise: one idea, an opening that is not a greeting, the reader's own situation rather than the writer's week, a specific takeaway they could act on, and a subject line derived from the piece rather than bolted on."
techniques:
  - ST-02
  - CM-02
  - RT-05
  - DS-06
  - QA-01
difficulty: intermediate
tags:
  - newsletter
  - email
  - drafting
  - voice
  - audience
  - editorial
updated: "2026-09-22"
related_prompts:
  - domain-professional-writing/content-quality/quality_slop_email_newsletter.md
  - domain-professional-writing/writing/writing_voice_print_extractor.md
  - domain-business-strategy/creator-economy/creator_newsletter_positioning_and_cadence.md
---

# Newsletter Issue

**Objective:** Produce one shippable issue that keeps a stated promise, carries
one idea, and gives the reader something they could act on — then score it
against the evaluator that already exists before sending.

**When to Use:**
- You have a newsletter with a promise and an issue to write.
- Drafts keep coming out as a roundup of everything you noticed.
- Open rates are fine and nothing gets replied to.
- You have a good idea and it is buried in paragraph six.

**When NOT to use:**
- You need to decide what the newsletter *is* —
  `domain-business-strategy/creator-economy/creator_newsletter_positioning_and_cadence.md`.
- You need an automated sequence — welcome, nurture, onboarding —
  `domain-agentic-resources/skills/marketing/email-sequence/`. A sequence is
  written once and fires forever; an issue is written once and sent once.
- You need a marketing campaign email or a sales email —
  `skills/marketing/copywriting/` and `skills/marketing/cold-email/`.
- You need to *score* a finished draft — that is
  `content-quality/quality_slop_email_newsletter.md`, and this prompt ends by
  handing off to it.

## Inputs / Context

1. **The promise**, verbatim, from the newsletter definition. Every editorial
   decision below is made against it.
2. **The idea for this issue**, in one sentence. If it takes three, that is
   three issues or one that is not ready.
3. **The reader**, and what they already know. Writing above or below this is
   the most common failure and the hardest to see from the inside.
4. **The voice spec**, if one exists — `writing_voice_print_extractor.md`
   produces one from a sample.
5. **Raw material** — notes, a conversation, a piece of work, research from
   `writing_content_research.md`.
6. **Length band** from the newsletter format, and whether this is a bad-week
   issue.

## Method

1. **Write the one-sentence claim (ST-02).**
   What this issue says that the reader did not already think. Not the topic —
   the claim. Everything that does not serve it comes out, including the good
   parts.

2. **Open without a greeting (CM-02).**
   The first sentence is the most valuable real estate in the issue, and "Hi
   everyone, hope you've had a good week" spends it on nothing. Open on the
   reader's situation, a specific moment, or the claim itself. The writer's week
   is not an opening; it is sometimes a middle.

3. **Structure to the format, not to the thought.**
   Use the newsletter's named sections. A structure the reader recognises lets
   them find the part they want — and lets you write on a Tuesday when nothing
   feels interesting.

4. **Make the takeaway specific enough to act on (DS-06).**
   One thing the reader could do, or see differently, today. "Think about your
   process" is not a takeaway. If you cannot name what changes for them, the
   issue is an observation, and observations do not earn replies.

5. **Cut to the band (RT-05).**
   Cut the second-best idea, the background the reader already has, and the
   paragraph explaining what you will now explain. The draft after cutting is
   usually 30% shorter and unambiguously better; if cutting hurts, it is because
   it was two issues.

6. **Derive the subject line from the finished piece.**
   Written last, from the claim. Not a teaser, not a question you do not answer,
   not curiosity-gapped. A subject line that promises something the issue does
   not deliver costs the next open, which is the only thing a newsletter is
   accumulating.

7. **Score it before sending (QA-01).**
   Run the draft through
   `domain-professional-writing/content-quality/quality_slop_email_newsletter.md`.
   That evaluator exists and is the verification step for this prompt — do not
   restate its criteria here, run it.

## Output Format

```
# [Subject line]
Preview text: [one line, extending the subject rather than repeating it]

---

[Opening — no greeting; the reader's situation, a moment, or the claim]

[Body, in the newsletter's named sections]

[Takeaway — one specific thing]

[Sign-off, per the newsletter's format]

---

## Editorial notes (not sent)
- Claim in one sentence: [...]
- Promise it keeps: [verbatim from the definition]
- What was cut, and why: [...]
- Reader's prior knowledge assumed: [...]
- Length: [n] words against a band of [n]–[n]
- Scored with `quality_slop_email_newsletter.md`: [result / outstanding items]
```

## Verification

- [ ] One claim, in one sentence, stated in the editorial notes.
- [ ] The issue keeps the stated promise; the promise is quoted, not paraphrased.
- [ ] The opening is not a greeting and not the writer's week.
- [ ] There is exactly one specific, actionable takeaway.
- [ ] Length sits inside the band.
- [ ] The subject line is derived from the finished piece and promises only what
      the issue delivers.
- [ ] The draft has been scored by `quality_slop_email_newsletter.md`.

## False-Positive Prevention

1. **A roundup is not an issue.** Five interesting things with no claim reads as
   generous and accumulates nothing. If the draft is a list, find the claim
   underneath it or send the list as a list, deliberately.
2. **The writer's week is not the reader's situation.** Personal framing works
   when it is doing work for the reader. When it is throat-clearing, it is the
   paragraph they scroll past, and they learn to scroll past the opening.
3. **A curiosity-gap subject line borrows from the next open.** It works once.
   The cost lands on the following issue, where it is invisible.
4. **Do not write above the reader to seem rigorous, or below them to seem
   accessible.** State the assumed prior knowledge in the notes so the choice is
   visible and can be wrong on purpose.
5. **"Let me know what you think" is not a call to action.** Ask one specific
   question you actually want answered, or ask nothing.
6. **A bad-week issue should be shorter, not thinner.** Keeping the promise at
   half length is fine. Keeping the length and dropping the claim is not.
7. **Do not restate the evaluator's criteria.** It exists; run it. Duplicating a
   rubric into the generator is how the two drift apart.

## Related

- `domain-professional-writing/content-quality/quality_slop_email_newsletter.md`
  — the evaluator this hands off to; generate here, score there.
- `writing_voice_print_extractor.md` — a reusable voice spec from a sample.
- `writing_content_research.md` — source material for an issue.
- `domain-business-strategy/creator-economy/creator_newsletter_positioning_and_cadence.md`
  — the promise and format every issue is written against.
