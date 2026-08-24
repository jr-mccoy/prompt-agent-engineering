---
title: "Judgment Assessment — Ten-Principle Self-Audit"
category: "productivity/validation"
description: "Run an honest, example-forced self-assessment of judgment across ten principles, surface blind spots and hidden strengths, and produce a single-focus 30-day growth plan."
techniques:
  - ST-01
  - RT-02
  - QA-02
  - DS-02
  - QA-04
difficulty: intermediate
tags:
  - validation
  - self-assessment
  - judgment
  - professional-development
  - blind-spots
  - growth-plan
updated: "2026-06-19"
related_prompts:
  - domain-productivity/validation/validation_adversarial_mini_check.md
  - domain-productivity/validation/validation_reality_check.md
  - domain-productivity/validation/validation_disconfirmation_pass.md
---

# Judgment Assessment — Ten-Principle Self-Audit

**Objective:** Assess your judgment across ten principles of good decision-making, separate inflated self-ratings from your actual track record using concrete examples, and convert the gaps into a single-focus 30-day growth plan.

**When to use:**
- For a periodic, honest check on how your judgment is developing.
- After a project where decision quality (not execution) was the deciding factor.
- When you suspect a self-narrative ("I'm great at prioritization") isn't backed by your recent behavior.

**When NOT to use:**
- As a substitute for real feedback from people who've watched you decide.
- For a single in-the-moment decision — use a fast adversarial check instead.

**Audience:** Individual contributors, leads, and founders building decision-making skill over time. Best run with a reasoning-capable model that will push back.

---

## Inputs / Context

1. **Your honest self-ratings** — a 1–5 score per principle, supplied during the interview.
2. **Concrete recent examples** — a specific instance (ideally within ~3 months) per principle where you did this well or struggled.
3. **Your role / level** — so growth areas can be weighed against what your role demands.

**The ten principles:**
1. **Find What's Scarce** — identify the true bottleneck, not surface problems.
2. **Reuse Patterns, Know the Context** — apply past patterns while seeing what makes this situation unique.
3. **Know What's Possible Now** — separate theoretical solutions from what's executable under current constraints.
4. **Sequence for Momentum** — order your bets to build credibility and proof before resistance mounts.
5. **Defend Your Non-Goals** — state explicitly what you're NOT doing and why.
6. **Calibrate Through Feedback** — learn judgment from what worked and failed in past projects.
7. **Map the Social Graph** — understand who influences whom and sequence conviction moments accordingly.
8. **Own the Consequences** — say what you'll do if you're wrong and hold yourself accountable.
9. **Show Your Reasoning** — make trade-offs and decisions transparent.
10. **Encode Judgment into Systems** — turn judgment into playbooks/automations others can use.

---

## Constraints

### Must
- Force a concrete, recent example for every principle before scoring it.
- Distinguish self-rating from evidenced performance: flag blind spots (inflated rating vs. weak example) and hidden strengths (strong example vs. low rating).
- Pick exactly one principle for the 30-day focus — do not hand back a long list.
- Tie each growth area to why it matters for the person's role/level.

### Must Not
- Accept vague, hand-waving answers; push for specifics.
- Invent achievements, examples, or strengths the person didn't supply.
- Assert a definitive judgment of a person from thin evidence — label inferences as inferences and uncertainty as uncertainty.
- Sugarcoat: if an example reveals self-deception about a skill, name it.

---

## Instructions

1. **Gather inputs** by running the interview — one principle at a time, refusing vague answers.
2. **Run the assessment prompt below verbatim.**

```
You're going to help me assess my judgment across 10 principles and identify
exactly where I need to improve. Be honest and direct — don't sugarcoat.

The 10 principles:
1. Find What's Scarce — identify the true bottleneck, not surface problems
2. Reuse Patterns, Know the Context — apply past patterns while seeing what's
   unique here
3. Know What's Possible Now — theoretical solution vs. what's executable now
4. Sequence for Momentum — order bets to build credibility before resistance
5. Defend Your Non-Goals — state what you're NOT doing and why
6. Calibrate Through Feedback — learn from what worked/failed in past projects
7. Map the Social Graph — who influences whom; sequence conviction accordingly
8. Own the Consequences — what you'll do if wrong; hold yourself accountable
9. Show Your Reasoning — make trade-offs and decisions transparent
10. Encode Judgment into Systems — turn judgment into reusable playbooks

STEP 1 — Assessment questions. For each principle ask me:
- "On a scale of 1–5, how strong are you at [principle]?"
- "Give me a specific example from the last 3 months where you did this well OR
   struggled."
Do not let me get away with vague answers. Push for concrete examples.

STEP 2 — Gap analysis. After all 10, tell me:
- My weakest 3 principles (lowest ratings or weakest examples)
- My blind spots (ratings that look inflated relative to my examples)
- My hidden strengths (examples stronger than my self-rating)

STEP 3 — Growth roadmap for my weakest 3. For each:
- One concrete practice I can do this week
- One recognition pattern to spot myself failing at it in real time
- One success metric to know I'm improving over a month

STEP 4 — Action plan:
- Which ONE principle to focus on first (don't overwhelm me)
- What to do in my next project or decision point
- What to track over the next 30 days

RULES:
- Push me to be specific. No hand-waving allowed.
- If my examples reveal I'm lying to myself about a skill, call it out.
- Do NOT invent examples, achievements, or strengths I didn't give you.
- Label inferences about my judgment as inferences, and say when you're unsure
  rather than asserting false certainty.
- Prioritize ruthlessly — I can only focus on one thing at a time.

Output the final assessment in the format provided.
```

3. **Self-check before output.** Confirm every principle had a concrete example, blind spots and hidden strengths are evidence-based, the focus is a single principle, and no claims were invented.
4. **Deliver** the result in the Output Format below.

---

## False-Positive Prevention

❌ **DON'T:**
- Accept "I'm pretty good at that" with no example — that's not data.
- Manufacture a strength or a recent win to be encouraging.
- State "you are weak at X" as fact when the example was ambiguous.
- Return five "focus areas" — that's a way to avoid prioritizing.

✅ **DO:**
- Require a concrete, dated example before scoring each principle.
- Mark any judgment that rests on thin evidence as an inference / a guess.
- Name self-deception when an example contradicts the self-rating.
- Force the plan down to one principle for the next 30 days.

---

## Output Format

```
JUDGMENT ASSESSMENT RESULTS

Top 3 Strengths:
- [Principle] — [brief evidence from my own examples]
- [Principle] — [brief evidence]
- [Principle] — [brief evidence]

Top 3 Growth Areas:
- [Principle] — [why it matters for my role/level]
- [Principle] — [why it matters]
- [Principle] — [why it matters]

Blind Spots (rating looks inflated vs. example):
- [Principle] — [the mismatch; labeled as inference]

Hidden Strengths (example stronger than rating):
- [Principle] — [the mismatch]

YOUR 30-DAY FOCUS: [single principle]

Week 1 Practice: [specific action]
Week 2 Practice: [specific action]
Week 3 Practice: [specific action]
Week 4 Review: [what to assess]

Recognition Pattern: [how to catch yourself failing at this in real time]
Success Metric: [how you'll know you're improving]

Signs You're Improving:
- [specific behavior change 1]
- [specific behavior change 2]
- [specific behavior change 3]

Next Principle to Tackle: [after the first improves]

Confidence note: [where this assessment rests on solid examples vs. thin evidence]
```

---

## Verification

- [ ] Every principle scored only after a concrete, recent example was given.
- [ ] Blind spots and hidden strengths are tied to specific example/rating mismatches.
- [ ] Exactly one principle chosen for the 30-day focus.
- [ ] Growth areas connected to the person's role/level.
- [ ] No invented examples, strengths, or achievements.
- [ ] Inferences and uncertainty labeled, not stated as fact.

---

## Techniques Used
- **ST-01 (Clear Objective Statement):** Sets the job as an honest, example-grounded judgment audit with a single-focus plan.
- **RT-02 (Multi-Dimensional Analysis Framework):** Ten judgment principles as orthogonal assessment axes.
- **QA-02 (Adversarial Stress-Test):** Refuses vague answers and calls out self-deception.
- **DS-02 (Metric/Criteria Specification):** Requires concrete examples, success metrics, and recognition patterns.
- **QA-04 (Uncertainty Acknowledgment):** Forces labeling of inferences and prevents fabricated certainty about the person.

---

## Related Prompts
- `domain-productivity/validation/validation_adversarial_mini_check.md` — apply judgment to a single high-stakes decision before shipping.
- `domain-productivity/validation/validation_reality_check.md` — surface the objections a credible expert would raise about a conclusion.
- `domain-productivity/validation/validation_disconfirmation_pass.md` — actively attack a belief instead of confirming it.
