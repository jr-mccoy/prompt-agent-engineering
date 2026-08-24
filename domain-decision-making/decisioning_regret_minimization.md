---
title: "Regret Minimization Across Time Horizons"
category: decision-making
description: "Evaluate a concrete decision against a future-self regret framework at user-specified time horizons (1, 5, 20 years). Surfaces three future-me questions per horizon, scores each path on regret-of-doing vs. regret-of-not-doing, and identifies which option survives the longest horizon. Decision-focused complement to broader life-direction reframes."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - decision-making
  - regret-minimization
  - time-horizon
  - future-self
  - scoring
updated: "2026-04-25"
related_prompts:
  - domain-decision-making/decisioning_comprehensive_rapid_tradeoff_analyzer.md
  - domain-decision-making/decisioning_reasoning_emulation.md
  - domain-decision-making/decisioning_time_boxed_decision_protocol.md
  - domain-personal-development/prompts/thinking/thinking_regret_minimization.md
---

# Regret Minimization Across Time Horizons

**Objective:** Take a concrete decision the user is weighing and evaluate each option through a future-self regret framework at three explicit time horizons. Produce three "future-me" diagnostic questions per horizon, score each option on regret-of-doing vs. regret-of-not-doing, identify which option survives the longest horizon, and surface the asymmetry that should anchor the choice.

**When to Use:**
- A decision is reversible-feeling in the short term but has long-tail consequences (career moves, partnership commitments, relocations, equity decisions, large purchases).
- Two options score similarly on a rapid tradeoff analysis and the deciding factor is "which version of this would I regret more 10 years out?"
- You are aware that short-term comfort is biasing you and want to weight the longer horizon explicitly.

**When NOT to use:**
- The decision is genuinely two-way-door at all relevant horizons. Use a faster tool (`decisioning_comprehensive_rapid_tradeoff_analyzer.md`).
- You're spiraling on a life-direction question without a decision in front of you. Use the personal-development companion at `domain-personal-development/prompts/thinking/thinking_regret_minimization.md`, which is built for the broader life-direction frame.
- The decision is time-critical (next 24 hours). Regret minimization is a slower, deeper tool.

**Distinction from the personal-development companion:** This prompt is decision-scoped (a specific named choice with named options and a deadline). The personal-development version is life-direction-scoped (broader trajectory questions where the "options" emerge during the work). Use this one when you can already write the choice in one sentence.

**Audience:** Anyone facing a structured decision with long-horizon consequences and at least 24 hours to think.

---

## Inputs / Context

1. **The decision in one sentence.** Include the deadline.
2. **The options.** 2–4 named options. If only one is named, the implicit second option is "do not do this thing."
3. **Time horizons.** Default to 1 year, 5 years, 20 years. The user may swap the longest for "end of career" or "at 80 years old" — if they do, ask why; the chosen horizon is itself a signal about what they are optimizing for.
4. **The user's current leaning.** Which option would they pick if forced to decide right now, and what is the source of the pull (financial, social, identity, fear, momentum)?
5. **Asymmetry context.** Anything irreversible about any option (sunk reputation, locked-in relationships, opportunity cost on a finite window).

---

## Constraints

### Must
- Treat each horizon as a distinct evaluation. Do not collapse "5 years" and "20 years" into "long term."
- For each option × horizon, produce both a regret-of-doing score (1–5) and a regret-of-not-doing score (1–5). Both must be reasoned, not asserted.
- Generate 3 future-me questions per horizon, in the user's own voice ("If I'm sitting here in 2031 and I picked Option B, what would I be thinking about the morning I made that call?").
- Identify which option has the lowest *peak regret* across all horizons — peak regret matters more than average regret for irreversible decisions.
- Name the asymmetry: which option's regret is recoverable vs. which is structural.
- End with a "decision-anchor sentence" the user can write down: a single sentence stating the decision and the horizon at which it was anchored, so they don't re-litigate it tomorrow.

### Must Not
- Default to the conservative option just because it has lower variance. Sometimes the higher-regret-of-not-doing path is the right one.
- Treat all horizons symmetrically. The 20-year horizon should weigh more for one-way-door decisions; the 1-year horizon should weigh more for survival or burnout decisions.
- Use abstract regret descriptions ("you might feel sad"). Force concrete future-me scenes.
- Allow the user's current leaning to set the regret scores. Score independently, then compare to the leaning at the end.
- Output a "trust your gut" conclusion. The whole point is to test the gut.

---

## Instructions

### Step 1 — Frame
Restate the decision, the options, the deadline, the horizons, and the user's current leaning. If the user's leaning is unstated, ask once before scoring.

### Step 2 — Future-me questions per horizon
For each horizon (1y, 5y, 20y or user-specified), write 3 questions in the user's first-person future voice. The questions should:
- Be specific enough to evoke a concrete scene (where you are, what you're doing, who is around).
- Probe both the upside narrative ("what would it have unlocked") and the downside narrative ("what would I have lost").
- Avoid moralizing. The future-me is curious, not judgmental.

### Step 3 — Regret scoring
For each option × horizon, produce two scores on a 1–5 scale:
- **Regret-of-doing (RoD):** how much I would regret having chosen this path.
- **Regret-of-not-doing (RoND):** how much I would regret having *not* chosen this path.

Each score must come with a one-sentence reason. If a score is `?`, name what the user would need to know to score it. Do not guess.

### Step 4 — Peak-regret identification
For each option, compute the peak (highest) score across both axes and all horizons. The option with the **lowest peak regret** is the path that, in its worst-case future, hurts the least. For irreversible decisions, this is the dominant criterion.

### Step 5 — Asymmetry analysis
For each option, classify the worst-case regret as:
- **Structural** — cannot be undone (years given, relationships ended, capital gone, ages closed).
- **Recoverable** — costly but reversible within a known time window.

A regret-of-doing on a structural option is heavier than the same numerical score on a recoverable option.

### Step 6 — Compare to leaning
Set the user's stated current leaning next to the peak-regret + asymmetry analysis. Three outcomes:
- **Aligned:** the leaning matches the lowest-peak-regret option. Reinforce.
- **Diverged with reason:** the leaning diverges, but the user's stated reason (financial constraint, family obligation, time-boxed window) genuinely overrides the regret signal. Name the override.
- **Diverged without reason:** the leaning diverges and there is no overriding constraint. This is a flag: the user may be optimizing for short-term comfort over long-horizon regret.

### Step 7 — Decision-anchor sentence
Write a single sentence the user can put in a private journal entry: "On [date], I chose [option] because [the regret-anchored reason], understanding I am accepting [the named regret-of-doing risk]." Anchoring the decision in writing reduces re-litigation tomorrow.

---

## False-Positive Prevention

1. **Conservative-by-default trap.** Regret minimization is not "pick the safe option." A path with high regret-of-not-doing and low regret-of-doing is the bold-and-correct choice — regret-of-not-doing is real regret.
2. **Status-quo invisibility.** "Do nothing" is an option. If the user did not name it, name it explicitly and score it. Status quo often has higher regret-of-not-doing than the user feels in the moment.
3. **Hindsight inflation.** Future-me questions should not be written as "if only I had…" — that bakes in the answer. Write them in true uncertainty: "How would I be telling this story?"
4. **Single-horizon collapse.** The 1-year, 5-year, and 20-year horizons can disagree, and that disagreement is information. If the model produces identical scoring across horizons, restart with sharper future scenes.
5. **Asymmetric compute.** Sometimes one option dominates at every horizon — write that and stop. Don't manufacture a tradeoff to make the prompt feel "balanced."
6. **Numerical false precision.** A 1–5 scale is enough. Don't compute weighted averages to two decimals. Peak regret + asymmetry classification do most of the work.
7. **Identity smuggling.** "Future me would be the kind of person who…" — careful. The future-me is the user, not an idealized self-image. Strip identity claims and stay in concrete scenes.

---

## Output Format

```
# Regret minimization — [decision in one sentence]

**Deadline:** [date]
**Horizons:** [1y / 5y / 20y or user-specified]
**Options:** [list]
**Current leaning:** [option] — pulled by [source of pull]

## Future-me questions

### 1-year horizon
1. [first-person scene-anchored question]
2. […]
3. […]

### 5-year horizon
1. […]
2. […]
3. […]

### 20-year horizon (or user-specified)
1. […]
2. […]
3. […]

## Regret scoring (1–5)

| Option | Horizon | RoD | reason | RoND | reason |
|--------|---------|-----|--------|------|--------|
| A      | 1y      |  2  | …      |  4   | …      |
| A      | 5y      |  3  | …      |  4   | …      |
| A      | 20y     |  3  | …      |  5   | …      |
| B      | 1y      |  4  | …      |  2   | …      |
| …                                              |

## Peak regret per option

| Option | Peak score | Peak axis        | At horizon |
|--------|------------|------------------|------------|
| A      | 5          | regret-of-not-doing | 20y     |
| B      | 4          | regret-of-doing  | 5y         |
| …                                                       |

## Asymmetry

| Option | Worst-case classification | Notes                                |
|--------|---------------------------|--------------------------------------|
| A      | recoverable               | costly but reversible by year 3      |
| B      | structural                | locks in 5-year exclusivity          |
| …                                                                       |

## Leaning vs. analysis
- Stated leaning: [option] (source: [pull])
- Lowest-peak-regret option: [option]
- Asymmetry-adjusted recommendation: [option]
- Verdict: [Aligned / Diverged with reason / Diverged without reason]
- If diverged without reason: [the flag — short paragraph naming the comfort being optimized for]

## Decision-anchor sentence
> "On [date], I chose [option] because [the regret-anchored reason], understanding I am accepting [the named risk]."
```

---

## Verification

- [ ] All three horizons are evaluated separately, with their own future-me questions.
- [ ] Every option × horizon cell has both an RoD and a RoND score with a one-sentence reason (or `?` with a lookup note).
- [ ] Peak-regret table identifies the worst-case score, axis, and horizon per option.
- [ ] Asymmetry table classifies each option's worst-case regret as structural or recoverable.
- [ ] Leaning-vs-analysis section produces one of the three named verdicts and, if diverged-without-reason, flags it explicitly.
- [ ] Decision-anchor sentence names the option, the regret-anchored reason, and the accepted risk.
- [ ] No fabricated future biography (specific kids, jobs, locations the user did not name).
- [ ] No "trust your gut" conclusion.
