---
title: "Concept Explanation Audit — Feynman-Style Test of What You Actually Understand"
category: learning/comprehension
description: "Test understanding of a concept by writing a Feynman-style plain-language explanation to a smart non-expert, then auditing it for the tells of shallow understanding: jargon used as a substitute for explanation, skipped load-bearing steps, things stated but not explained, and the precise place the explanation breaks down. Surfaces the user's actual gap, names the next thing to learn that closes the biggest gap, and re-does the explanation focused on the load-bearing piece."
techniques:
  - ST-01
  - ST-02
  - DS-01
  - CM-02
  - RT-02
  - QA-01
difficulty: beginner
tags:
  - learning
  - feynman-technique
  - comprehension
  - self-assessment
  - explanation
updated: "2026-06-18"
reasoning:
  styles: [analytic, dialectical, reflective]
  stakes: low
  horizon: hours
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: variable
  collaboration: solo
  output_format: [narrative, structured]
  user_role: [individual, learner, student, professional]
  mode: [audit, diagnose]
related_prompts:
  - domain-learning/learning_curriculum_designer.md
  - domain-learning/learning_skill_gap_to_curriculum.md
  - domain-learning/learning_reading_list_curator.md
---

# Concept Explanation Audit — Feynman-Style Test of What You Actually Understand

**Objective:** Use a written, plain-language explanation as an instrument to find the gaps in the user's understanding of a concept they believe they understand. The mechanism is the Feynman technique: explaining a thing to a smart non-expert, with no jargon, exposes every place where the user has memorized a label instead of understanding a mechanism. This prompt elicits that explanation, then audits it rigorously for four tells — jargon standing in for explanation, skipped load-bearing steps, claims stated but not explained, and the exact point where the explanation runs out of road. It converts those tells into a named gap, identifies the single next thing to learn that closes the biggest gap, and has the user re-explain the load-bearing piece they'd been gliding over.

**When to use:**
- The user thinks they understand a concept and wants to test that belief before relying on it.
- Before teaching, presenting, or building on a concept.
- After studying a topic, to check whether study produced understanding or just familiarity.
- When a concept "feels clear" but the user can't quite explain it simply (a classic tell).

**When NOT to use:**
- The user openly doesn't understand the concept yet — there's nothing to audit; go study it first (`learning_curriculum_designer.md` / `learning_reading_list_curator.md`).
- For procedural skills where the test is doing, not explaining — use the deliberate-practice tools.
- When the concept is a matter of opinion or taste rather than a mechanism that can be explained.

**Audience:** Students, self-directed learners, and professionals checking the depth of their own understanding.

---

## Inputs / Context

1. **The concept.** The specific thing the user believes they understand.
2. **The user's written explanation.** Plain language, no jargon, aimed at a smart non-expert (e.g., a sharp 15-year-old or a smart friend from another field). This is the core input; the prompt should elicit it if not supplied.
3. **Where they learned it.** Optional — helps locate where a gap may have crept in.
4. **The stakes.** Why understanding matters here (teaching, building, deciding) — calibrates audit depth.

---

## Constraints

### Must
- Require an actual **written explanation** in plain language to a smart non-expert. If the user hasn't written one, prompt for it before auditing — there's nothing to audit otherwise.
- Audit for **jargon-as-substitute**: every technical term that's used rather than explained. A term is fine if it's defined in plain words; it's a tell if it's leaned on to skip the actual explanation.
- Audit for **skipped load-bearing steps**: places where the explanation jumps from A to C, and B (the mechanism that makes A cause C) is missing.
- Audit for **stated-but-not-explained**: claims asserted as true without the why ("and that's why it's stable" — but why?).
- Identify the **breakdown point**: the exact place the explanation stops working — where the user would not be able to answer a non-expert's "but why?"
- Convert findings into a **named gap** — the specific thing the user doesn't actually understand, in their own concept's terms.
- Name the **single next thing to learn** that closes the biggest gap (not a list — the one highest-leverage thing).
- Have the user **re-explain the load-bearing piece** they were gliding over, to test whether the gap is now closed.

### Must Not
- Audit a vague gesture instead of a real explanation. No written explanation, no audit.
- Be polite about jargon. The whole value is in catching the words used to paper over not-knowing.
- Confuse fluency with understanding. A smooth explanation can still be hollow; the audit tests mechanism, not polish.
- Produce a long list of gaps with no priority. Name the biggest one and the single next move.
- Skip the re-explanation. The loop isn't complete until the user has re-explained the load-bearing piece.

---

## Instructions

### Step 1 — Elicit the explanation
If not provided, ask the user to explain the concept in plain language to a smart non-expert, in writing, with no jargon. Push back if they reach for technical terms as shortcuts. Wait for a real explanation.

### Step 2 — Mark the jargon
Go through the explanation and flag every technical term. For each, decide: defined in plain words (fine) or used as a substitute for explanation (tell). List the substitute-jargon — these mark places the user may not actually understand.

### Step 3 — Find the skipped steps
Trace the causal/logical chain. Wherever the explanation jumps (A → C with no B), name the missing middle. These are the load-bearing steps the user has been skipping — often without noticing.

### Step 4 — Find stated-but-not-explained claims
Flag assertions made without a why. For each, ask the non-expert's "but why?" and check whether the explanation answers it. The unanswered ones are gaps.

### Step 5 — Locate the breakdown point
Identify the single place where the explanation most clearly stops working — where one "but why?" from the non-expert would leave the user stuck. This is usually the heart of the gap.

### Step 6 — Name the gap
State, in plain terms, the specific thing the user does not actually understand. Not "you have some gaps" — the specific mechanism, step, or relationship that's missing. Tie it to the breakdown point.

### Step 7 — Name the single next thing to learn
The one highest-leverage thing that, if learned, closes the biggest gap. One thing, specific, not a reading list. State how to learn it briefly (a concept to look up, a mechanism to trace, a question to answer).

### Step 8 — Re-explain the load-bearing piece
Have the user re-write the explanation of just the load-bearing piece — the step or mechanism they were gliding over — now with the gap addressed. Re-audit this piece against the same four tells. If it still breaks, the gap isn't closed; say so and point back to Step 7.

### Step 9 — Verify and output
Run the checklist; deliver the audit, the named gap, the next thing to learn, and the re-explanation.

---

## False-Positive Prevention

1. **No-explanation audit.** Trying to audit a vague verbal gesture instead of a written explanation. Require the real artifact first.
2. **Jargon tolerance.** Letting technical terms slide because they sound right. A term used to skip the explanation is exactly the tell to catch.
3. **Fluency-as-understanding.** Grading a smooth, confident explanation as good when it's hollow. Test mechanism, not eloquence — does it survive repeated "but why?"
4. **Gap-list without priority.** Listing ten gaps so the user doesn't know where to start. Name the biggest gap and the single next move.
5. **Breakdown-point avoidance.** Stopping the audit before reaching the place the explanation actually fails because it's uncomfortable. The breakdown point is the deliverable.
6. **Skipping the re-explanation.** Ending at "here are your gaps" without testing whether the user can now explain the load-bearing piece. The re-explanation closes the loop.
7. **Auditing the easy parts.** Spending the audit on the periphery the user clearly knows, avoiding the core. Aim at the load-bearing mechanism.
8. **Over-explaining for the user.** The auditor supplying the missing explanation instead of making the user find it. Name the gap; let the learning happen.

---

## Output Format

```
# Explanation Audit — [concept]

## The explanation (as written)
[The user's plain-language explanation.]

## Tell 1 — Jargon as substitute
| Term used | Defined in plain words? | If not, this hides: |
|-----------|--------------------------|---------------------|
| [...] | no | [the mechanism skipped] |

## Tell 2 — Skipped load-bearing steps
- Jump: [A] → [C]. Missing middle [B]: [the mechanism that makes A cause C].

## Tell 3 — Stated but not explained
- "[claim]" — the "but why?" it doesn't answer: [...]

## Breakdown point
[The exact place the explanation stops working — where one "but why?" leaves you stuck.]

## The gap (named)
[The specific mechanism / step / relationship you don't actually understand.]

## Single next thing to learn (highest leverage)
[One specific thing] — how: [look up / trace / answer this question].

## Re-explanation of the load-bearing piece
[User re-writes just the load-bearing mechanism, gap addressed.]
Re-audit: [still breaks? → back to "next thing to learn" | holds? → gap closed]
```

---

## Verification

- [ ] A real written plain-language explanation exists before any audit.
- [ ] Every technical term is judged: defined plainly vs. used as a substitute.
- [ ] Skipped load-bearing steps are named with the missing middle.
- [ ] Stated-but-not-explained claims are flagged with the unanswered "but why?"
- [ ] A single breakdown point is located.
- [ ] The gap is named specifically, not as "some gaps."
- [ ] Exactly one highest-leverage next thing to learn is named.
- [ ] The user re-explains the load-bearing piece and it's re-audited.
- [ ] Fluency is never mistaken for understanding.
