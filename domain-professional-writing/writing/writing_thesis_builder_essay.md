---
title: "Thesis Builder — Surface the Stakes and Forge a Defensible Essay Thesis"
category: professional-writing/writing
description: "Surface the stakes underlying a loose idea, then craft graded thesis options (safe / sharp / boldest) each with three supporting sub-claims and the strongest counter-argument it must survive, plus the trade-off of each option."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-01
  - QA-04
difficulty: intermediate
tags:
  - thesis
  - essay
  - argument
  - stakes
  - counter-argument
  - persuasion
updated: "2026-06-07"
related_prompts:
  - domain-professional-writing/writing/writing_narrative_arc_builder.md
  - domain-professional-writing/writing/writing_precision_doc_edit.md
---

# Thesis Builder

**Objective:** Take a loose idea or topic, surface the stakes that make it worth arguing, and produce three graded thesis options — safe, sharp, and boldest — each paired with three supporting sub-claims, the single strongest counter-argument it must survive, and the trade-off of choosing it.

**When to Use:**
- You have a topic or a vague "I want to write about X" but no sharp claim yet.
- Your draft argues several things at once and you need to commit to one defensible point.
- You can state your opinion but can't yet say *why it matters* or what would defeat it.
- You're choosing how bold to be and want the options laid out with their risks.

**When NOT to use:**
- You already have a locked thesis and need structure — use `writing_narrative_arc_builder.md`.
- You need line-level editing of finished prose — use `writing_precision_doc_edit.md`.
- The piece is descriptive/reference, not argumentative (a thesis would be forced).

**Audience:** Essayists, students, op-ed and longform writers, analysts, and anyone who must commit to a single arguable claim.

---

## Inputs / Context

1. **The loose idea / topic** (required): whatever the user has, even a single phrase.
2. **Audience:** who reads it and what they currently believe about the topic.
3. **Field / context:** academic, op-ed, business, personal essay, blog.
4. **Length / venue:** affects how much a thesis can defend.
5. **Stance signal** (optional): any leaning the writer already has.
6. **Material** (optional): wrap supplied notes or evidence in `<source_material>` … `</source_material>`.

---

## Constraints

### Must
- First **surface the stakes**: name who cares, what changes if the claim is true vs. false, and why this is worth a reader's time.
- Produce **three graded theses**: *safe* (widely defensible, low risk), *sharp* (specific and contestable, the recommended default), and *boldest* (high-conviction, high-risk).
- Make each thesis a **single declarative, arguable sentence** — something a reasonable person could disagree with.
- Give each thesis **exactly three supporting sub-claims** that, if true, carry the thesis.
- For each thesis, state the **single strongest counter-argument** it must survive (steel-manned, not a strawman).
- State the **trade-off** of each option (what you gain and what you risk).
- Recommend a default and say **why**, given the audience and venue.

### Must Not
- Offer a "thesis" that is actually a topic ("the impact of social media") or an undebatable fact.
- Strawman the counter-argument — it must be the version a smart opponent would actually make.
- Pad to more or fewer than three sub-claims per thesis.
- Fabricate evidence, studies, or statistics to support sub-claims; mark needed evidence as `[EVIDENCE NEEDED]`.
- Default to the boldest option for impact's sake when the writer can't defend it at the given length.

---

## Instructions

1. **Clarify the latent claim.**
   - Restate the loose idea as the most likely *argument* the writer is reaching for. If ambiguous, name 2 readings and pick the more productive one.

2. **Surface the stakes.**
   - Who cares about this and why? What is true/possible if the claim holds? What's lost if it's false or ignored? If you can't find real stakes, say so — that's a signal the idea isn't yet essay-worthy.

3. **Generate the safe thesis.**
   - The most defensible version most informed readers would grant. Low risk, lower originality. Three sub-claims. Strongest counter. Trade-off.

4. **Generate the sharp thesis (recommended default).**
   - Specific, contestable, and original enough to be worth reading, but defensible at the stated length. Three sub-claims. Strongest counter. Trade-off.

5. **Generate the boldest thesis.**
   - The high-conviction version that stakes out real ground. Three sub-claims. Strongest counter (this one will be the hardest to survive). Trade-off, including the risk of overreach.

6. **Pressure-test each (QA-01).**
   - For each thesis, check: Is it one sentence? Is it arguable? Do the three sub-claims actually carry it? Is the counter steel-manned?

7. **Acknowledge uncertainty (QA-04).**
   - Where a thesis depends on contested or thin evidence, label it. Don't present a contestable empirical claim as settled.

8. **Recommend.**
   - Name the default (usually *sharp*) and justify it against the audience, venue, and length.

---

## False-Positive Prevention

1. **Topic-as-thesis.** "The role of AI in education" is a topic, not a thesis. Verify each option is a *claim someone could deny*. If it can't be negated, it isn't a thesis.
2. **Fake stakes.** If the "stakes" are generic ("this is important to understand"), they're empty. Demand a concrete consequence of the claim being true vs. false; if none exists, flag that the idea may not be essay-worthy.
3. **Strawman counter.** A counter-argument you can easily knock down proves nothing. Steel-man it: state the strongest case an informed opponent would make, then note whether the thesis actually survives it.
4. **Sub-claims that don't carry.** Three supporting points that are merely *related* don't support a thesis. Check that if all three are true, the thesis follows.
5. **Fabricated support.** Never invent a study, statistic, or example to make a sub-claim land. Use `[EVIDENCE NEEDED]`.
6. **Bold-by-default bias.** The boldest thesis is the most quotable and the most likely to collapse under scrutiny at short length. Recommend it only when the writer can actually defend it.
7. **Overconfident empirical claims.** If a thesis rests on contested data, label it `(contested)` rather than asserting it flatly (QA-04).
8. **Three near-identical theses.** Safe / sharp / boldest must genuinely differ in risk and scope, not be reworded versions of one claim.

---

## Output Format

```
# Thesis options — [topic]

## Latent claim (restated)
[The argument the writer is reaching for, in one line]

## Stakes
- Who cares: [...]
- If true: [what becomes possible / what changes]
- If false or ignored: [what's lost]
- Worth-arguing verdict: [yes / not yet — why]

## Option A — Safe
**Thesis:** [single arguable sentence]
**Sub-claims:**
1. [...]
2. [...]
3. [...]
**Strongest counter (steel-manned):** [...]  → Survives? [yes/partly/no, why]
**Trade-off:** gain [...] / risk [...]

## Option B — Sharp (recommended default)
**Thesis:** [...]
**Sub-claims:** 1. [...] 2. [...] 3. [...]
**Strongest counter:** [...]  → Survives? [...]
**Trade-off:** [...]

## Option C — Boldest
**Thesis:** [...]
**Sub-claims:** 1. [...] 2. [...] 3. [...]
**Strongest counter:** [...]  → Survives? [...]
**Trade-off:** gain [...] / risk [...]

## Evidence to gather
- [EVIDENCE NEEDED: ...]

## Recommendation
[Which option, and why — given audience, venue, length]
```

---

## Verification

- [ ] Stakes are concrete (a real consequence of true vs. false), not generic.
- [ ] Exactly three thesis options, genuinely graded by risk: safe / sharp / boldest.
- [ ] Each thesis is one declarative, arguable sentence (can be negated).
- [ ] Each thesis has exactly three sub-claims that, if true, carry it.
- [ ] Each counter-argument is steel-manned, with a survival verdict.
- [ ] Each option states its trade-off (gain vs. risk).
- [ ] Contested empirical claims are labeled, not asserted as settled.
- [ ] No fabricated studies/statistics; gaps marked `[EVIDENCE NEEDED]`.
- [ ] A default is recommended and justified against audience/venue/length.
