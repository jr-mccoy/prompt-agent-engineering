---
title: "ML Jargon Translator for Stakeholders"
category: AI-ML/ai-product-leadership
description: "Translate ML jargon, metrics, and tradeoffs into language matched to a specific stakeholder audience — preserving the real tradeoff while removing the technical noise."
techniques:
  - RP-02
  - NE-13
  - ST-03
  - QA-01
  - RT-05
difficulty: beginner
tags:
  - communication
  - jargon-translation
  - stakeholders
  - tradeoffs
  - clarity
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/ai-product-leadership/aipm_model_risk_brief_for_execs.md
  - domain-AI-ML/ai-product-leadership/aipm_roi_business_case.md
  - domain-AI-ML/learning-ai-ml/mllearn_concept_explainer.md
---

# ML Jargon Translator for Stakeholders

**Objective:** Translate ML concepts, metrics, and tradeoffs into language appropriate for a specific stakeholder (executive, sales, legal, customer, board) — preserving the real decision or tradeoff that matters to them while stripping technical noise, and without dumbing it down into something misleading.

**When to Use:**
- Explaining a model's behavior, a metric, or a tradeoff to a non-technical decision-maker.
- Preparing talking points for a sales, board, or customer conversation about an AI feature.
- A previous explanation lost the room or led to a wrong conclusion.

**When NOT to Use:**
- You need to teach the concept properly for understanding (use `mllearn_concept_explainer.md`).
- You need a full risk brief (use `aipm_model_risk_brief_for_execs.md`).

## Inputs / Context

- **The concept/metric/tradeoff** to translate (e.g., precision/recall tradeoff, false-positive rate, hallucination, drift, confidence).
- **The audience** — role, technical level, what they care about, the decision they face.
- **The stakes** — what they'll do with the explanation; what a misunderstanding would cost.
- **Any real numbers** — actual metrics, if the translation must convey magnitude.

## Constraints

**Must:**
- Preserve the decision-relevant truth — the translation must lead the audience to a correct conclusion, not just a comfortable one.
- Match vocabulary and framing to the named audience and the decision they face.
- Use analogies/consequences the audience already understands, and verify the analogy doesn't break in a way that misleads.

**Must Not:**
- Oversimplify into falsehood (e.g., "95% accurate means it's right 95% of the time" on imbalanced data).
- Invent metrics or precision; use the user's real numbers or speak qualitatively.
- Strip out a tradeoff the audience needs to make a decision (e.g., hiding that catching more fraud means more false alarms).

**Instructions:**

1. **Identify the decision behind the question.** What is this stakeholder actually trying to decide or do? The translation serves that decision, not a general definition.

2. **Find the core truth to preserve.** State the one thing they must get right (e.g., "more sensitivity = more false alarms" or "the model is confident but can be confidently wrong"). Everything else is removable.

3. **Choose an audience-fit frame.** Pick the consequence or analogy that lands for this role — cost, risk, customer experience, legal exposure — in their existing vocabulary.

4. **Translate the metric to consequence.** Convert numbers into "what this means for you/the customer/the business." Avoid raw ML terms unless the audience uses them.

5. **Preserve the tradeoff explicitly.** If there's a dial (precision vs recall, speed vs cost, automation vs control), present it as a choice they own, with the cost of each direction.

6. **Stress-test the analogy.** Check where the simplification could mislead and add the one caveat that prevents a wrong conclusion.

7. **Offer a one-liner and a backup.** Give a single sentence they can repeat, plus a slightly deeper version for follow-up questions.

**Output Format:**

A markdown translation aid:
- **The Decision** — what this stakeholder is deciding.
- **Plain-Language Explanation** — the audience-fit version.
- **The Tradeoff (if any)** — the dial they own, framed as a choice.
- **The One-Liner** — a repeatable sentence.
- **If They Ask More** — the next level of depth.
- **Don't Let Them Conclude** — the misreading to head off.

## Verification

- [ ] The translation serves the stakeholder's actual decision.
- [ ] The core decision-relevant truth is preserved, not oversimplified into error.
- [ ] Any tradeoff is presented as an owned choice with both costs.
- [ ] Numbers are real or rendered qualitatively — none invented.
- [ ] A "don't conclude X" guardrail prevents the likely misreading.

## False-Positive Prevention

❌ **DON'T:**
- Say "95% accurate" without context when the positive class is 2% of data (it's misleading).
- Drop the false-positive cost when explaining a "catch more fraud" improvement.
- Translate "the model is 90% confident" as "it's right 90% of the time" — confidence ≠ accuracy.
- Use a tidy analogy that quietly implies the model is more reliable than it is.

✅ **DO:**
- Translate accuracy into consequence ("of 100 flagged, ~30 will be false alarms a person must check").
- Keep both arms of any tradeoff visible as a decision the stakeholder owns.
- Distinguish confidence/calibration from accuracy when the audience would conflate them.
- Add the one caveat that stops the analogy from over-reassuring.

## Example Output

```markdown
## Translation — "Why can't the fraud model just catch everything?" (audience: VP Ops)

### The Decision
Where to set the fraud-alert threshold — how aggressive to be.

### Plain-Language Explanation
The model scores each transaction's fraud risk. We choose a cutoff. Set it aggressive
and we catch more fraud — but also flag more legitimate customers, who get blocked and
call support. Set it relaxed and customers are happier — but more fraud slips through.

### The Tradeoff (you own this dial)
- Aggressive: catch ~more fraud, ~more false alarms (support load + customer friction).
- Relaxed: smoother customer experience, more fraud loss.
There's no setting that does both — it's a business call about which cost hurts more.

### The One-Liner
"It's a dial between fraud caught and customers annoyed — we pick where to set it."

### If They Ask More
We can move the whole curve outward (catch more at the same false-alarm rate) only by
improving the model — that's a project, not a threshold change.

### Don't Let Them Conclude
That a "better model" means zero false alarms. Even a great model trades the two off;
we're choosing the balance, not eliminating the tradeoff.
```

**Techniques Used:**
- **RP-02 (Audience-Specific Framing):** core — vocabulary and frame matched to the stakeholder.
- **NE-13 (Technical-to-Business Translation):** metrics rendered as business consequence.
- **ST-03 (Output Format Specification):** a fixed translation-aid structure.
- **QA-01 (Self-Verification):** the analogy is stress-tested against misreadings.
- **RT-05 (Evidence-Based Reasoning):** consequences derived from real numbers, not asserted.

**Related Prompts:**
- `aipm_model_risk_brief_for_execs.md` — a full brief when more than one concept is at stake.
- `aipm_roi_business_case.md` — when the translation feeds a funding conversation.
- `mllearn_concept_explainer.md` — when the goal is real understanding, not just a decision aid.
