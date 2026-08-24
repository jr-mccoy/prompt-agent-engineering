---
title: PACU Orientation Journal Club Facilitator
category: pacu/orientation-curriculum
task_type: CREATE
audience: PACU educator running a journal club during orientation
updated: "2026-05-15"
tags:
  - pacu
  - orientation
  - journal-club
  - evidence-based-practice
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-01
  - ED-02
difficulty: intermediate
related_prompts:
  - prompts/pacu_orientation_curriculum_designer.md
  - prompts/pacu_orientee_weekly_learning_plan.md
references:
  - ASPAN Standards of Perianesthesia Nursing Practice
  - Drain's PeriAnesthesia Nursing Practice (7th ed.)
---

# PACU Orientation Journal Club Facilitator

> Safety reminder: Journal club teaches evidence appraisal; it does not change facility practice. Practice changes follow facility policy review.

## Objective

Produce a **journal club facilitation packet** for one article: article selection criteria, pre-read questions for participants, discussion structure with timing, and a "translate to bedside" wrap-up. Designed to be run every 2–4 weeks during orientation.

## Inputs

- **Article candidate (title + author + journal + year):** {{paste the candidate article}}
- **Orientation week context:** {{which orientation week — to align topic to bedside theme}}
- **Group size:** {{e.g., 2 orientees + lead preceptor; whole unit; etc.}}
- **Time budget:** {{default 45 min, up to 60 min}}
- **Article access status:** {{full text available to all participants? Y/N — if N, the packet uses a public summary, not invented detail}}

## Audience / Scope

- **Primary:** Educator facilitating.
- **Secondary:** Orientee participants.
- **Scope:** One article per packet. The packet does not select the article (selection criteria are output below; final selection is the educator's).

## Output requirements

```markdown
# Journal Club Packet — {Article short title}

> Safety reminder: Journal club appraises evidence. It does not change facility practice; practice changes follow facility policy review.

**Article:** {full citation}
**Orientation week alignment:** {n}
**Group size + roles:** {…}
**Time budget:** {≤ 60 min}

## Selection rationale (≤ 4 sentences)

State why this article belongs in journal club this week. Tie to the orientation theme + the unit's clinical patterns. Surface any concern about article quality up front (sample size, generalizability, publication date).

## Pre-read assignment (≤ 30 min for participants)

- Read the article.
- Hold these 3 questions while reading:
  1. What clinical question does this article try to answer?
  2. What's the single biggest threat to the validity of the conclusion (sample, design, conflict of interest, generalizability)?
  3. What would have to be true for this to change practice in our unit?

## Discussion structure (timed)

**Opening (5 min):** Each participant gives a 30-second statement of "the article said X." Compare statements — where do summaries differ? Why?

**Clinical question + design (10 min):** Walk through the PICO (or comparable) framing. Was the design appropriate to the question? Name one alternative design that could have addressed the question.

**Critical appraisal (15 min):** Surface the single biggest threat to validity. Each participant names theirs; group converges or stays explicit about disagreement.

**Bedside relevance (10 min):** "In what case in our PACU this past week would this have applied? In what case would it clearly *not* apply?" Anchor in unit-specific exposure.

**Translate-to-bedside wrap (5 min):** Two outputs:
- One sentence on what this article supports that our practice already does.
- One sentence on what this article does not justify changing.

## What this packet is not

- Not a practice-change recommendation.
- Not a meta-analysis.
- Not a clinical decision-support tool.

## Sources / reference

- ASPAN *Standards* — frame on evidence-based practice in PACU.
- *Drain's* — clinical context for the article's topic, {chapter}.
```

## Must / Must not

**Must:**
- Surface article quality concerns up front in the selection rationale.
- Build the "translate to bedside" wrap as **what this supports** + **what this does not justify changing**.
- Keep total time ≤ 60 min including reading-prep guidance.
- Anchor bedside-relevance in actual cases the participants likely saw that week.

**Must not:**
- Treat one article as a practice-change recommendation.
- Invent article details if the article is not pasted in.
- Reframe the article's findings to fit the bedside theme — name disconnect where it exists.
- Use this packet for HR or sign-off.
- Project group dynamics ("everyone will love this").

## Quality signals

- An orientee leaves the discussion better at saying "this article is interesting but doesn't justify a practice change yet."
- The facilitator can run the packet without further prep beyond reading the article.
- The discussion structure produces convergence on appraisal, not just consensus on conclusion.

## Verification

- [ ] Selection rationale surfaces at least one quality concern.
- [ ] Pre-read 3 questions present.
- [ ] Discussion structure has timed segments summing to ≤ 60 min.
- [ ] Translate-to-bedside wrap produces two specific sentences.
- [ ] Article details only come from the user-pasted article.
- [ ] Safety + FPP sections present.

## False-Positive Prevention

- **No invented article details** — abstract, methods, sample size, conclusions all come from the user-pasted article.
- **No invented citation metadata** — DOI, journal, year per the user input.
- **No invented appraisal tools** ("our unit uses the X scoring system" — unless user names it).
- **No invented effect sizes or statistics.**
- **No invented practice-change implications.**
- **No protected-characteristic content** in discussion prompts.
- **No license-pathway-based discussion roles** ("BSN participants lead appraisal").

## Worked Example

<details>
<summary>Example: short worked example (click to expand)</summary>

```markdown
# Journal Club Packet — {abbreviated example}

**Article:** [user-pasted full citation]
**Orientation week alignment:** Wk 5 (regional block recovery theme)
**Group size:** 2 orientees + lead preceptor + 1 staff RN
**Time budget:** 50 min

## Selection rationale

This article addresses regional block resolution timing, which is the Wk 5 bedside theme. Sample size is small (n declared by user); generalizability to our mixed surgical mix is unclear. Article is from 2022 (recent enough). Concern: single-center study — appraisal will need to surface this.

## Pre-read assignment

Read the article. Hold:
1. What clinical question is the article addressing?
2. What's the single biggest threat to validity?
3. What would have to be true for this to change practice in our unit?

## Discussion (50 min)

5 min opening → 10 min question/design → 15 min appraisal → 10 min bedside relevance → 5 min translate-to-bedside.

## Translate-to-bedside

- Supports: our existing practice of monitoring block resolution by qualitative cues over time.
- Does not justify changing: standard discharge criteria thresholds — single-center small-sample evidence is not enough.
```

Notes: quality concerns surfaced, timing respects budget, translate-to-bedside dual-sentence frame, no invented article detail.
</details>

## Self-check

- [ ] Quality concerns surfaced in selection rationale.
- [ ] Pre-read questions present.
- [ ] Discussion structure timed.
- [ ] Translate-to-bedside dual sentence.
- [ ] No invented article detail.
- [ ] FPP section passed.
