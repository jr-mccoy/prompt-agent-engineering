---
title: "Hypothesis Generator — Competing Hypotheses for an Observed Pattern, Plus Distinguishing Tests"
category: research-academic/hypothesis-generation
description: "Take an observed pattern (in data, behavior, or outcomes) and generate 4–7 competing hypotheses that could explain it. Distinguish causal from correlational hypotheses, surface confounders, and design tests that would distinguish the hypotheses from each other (not just rule each in or out individually). Counters single-hypothesis tunneling."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - DS-02
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - research
  - hypothesis-generation
  - abductive-inference
  - confounders
  - distinguishing-tests
updated: "2026-05-10"
reasoning:
  styles: [abductive, causal, dialectical]
  stakes: variable
  horizon: variable
  uncertainty: variable
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo_or_pair
  output_format: hypothesis_set_plus_test_design
  user_role: [researcher, analyst, scientist, founder, pm, operator]
  mode: [synthesize, audit, design]
related_prompts:
  - domain-research-academic/research_question_formulation.md
  - domain-research-academic/research_evidence_map.md
  - domain-reasoning-craft/reasoning-moves/reasoning_counterfactual_analysis.md
---

# Hypothesis Generator

**Objective:** For an observed pattern (a data spike, a behavior change, a counterintuitive outcome, an unexpected correlation), generate 4–7 competing hypotheses that could plausibly explain it. Distinguish causal from correlational hypotheses, surface confounders that could produce the pattern without any of the hypotheses being true, and design tests that would distinguish the hypotheses from each other rather than just attempting to confirm one. Counters single-hypothesis tunneling, which is the most common error in causal interpretation.

**When to use:**
- A surprising result needs explanation (engagement spike, churn jump, regression in a metric, public sentiment shift, experimental finding).
- A team has a leading explanation and you want to stress-test it against alternatives.
- Designing the analysis plan for a new dataset before reading the data.
- Investigating a system anomaly where multiple causes are plausible.
- Pre-mortem on a research design where the hypothesis space wasn't fully enumerated.

**When NOT to use:**
- The cause is genuinely known with high confidence (e.g., a deployment caused the change at the exact deployment time and no other variables shifted).
- The pattern is too vaguely described to hypothesize about. Sharpen the pattern first.
- The user wants a single confident answer. The output of this prompt is a hypothesis space, not a verdict.

**Audience:** Researchers, analysts, scientists, PMs, operators — anyone interpreting an observed pattern.

---

## Inputs / Context

1. **The observed pattern.** As specific as possible: what was observed, when, in what population, by what measure, magnitude relative to baseline.
2. **What changed (if anything) around the time of the pattern.** Internal changes, external events, seasonal effects, measurement changes.
3. **Current leading hypothesis (if any).** Captured up front so it doesn't dominate the generation step.
4. **What evidence is available or could be obtained.** Existing data, possible new data collection, interviews, instrumentation.
5. **Stakes.** What decision rides on the explanation.

---

## Constraints

### Must
- Generate **at least 4** hypotheses, ideally 5–7. Fewer than 4 risks tunneling; more than 7 starts including duplicates.
- Cover at least these categories:
  - **Causal — internal:** something the user / team did caused it.
  - **Causal — external:** an outside event caused it.
  - **Selection / sampling:** the pattern is real but is artifact of who or what was observed.
  - **Measurement:** the pattern is in the measurement, not the underlying phenomenon.
  - **Confounding:** an unobserved variable causes both the apparent cause and the apparent effect.
  - **Coincidence / regression to mean:** the pattern is noise, recently extreme values reverting.
- For each hypothesis: state it precisely, name the **mechanism** by which it would produce the observed pattern, and state what other observable predictions it makes.
- For each hypothesis: name the **disconfirming observation** that would rule it out.
- Design **distinguishing tests** — observations or analyses that would discriminate between hypotheses, not just confirm one.
- Identify the **most parsimonious** hypothesis (Occam) and the **most diagnostic** observation (the one that splits the hypothesis set most efficiently).

### Must Not
- Skip categories ("measurement isn't relevant here" — usually it is, especially for surprising results).
- Generate hypotheses that all share the same disconfirming observation. They aren't actually distinct hypotheses then.
- Privilege the user's leading hypothesis with extra detail. Treat all candidates symmetrically.
- Treat parsimony (simplest explanation) as decisive. Parsimony is a tiebreaker, not a verdict.
- Conflate hypothesis with description. "Engagement is up because users like the new feature" is a hypothesis; "engagement is up" is a description.

---

## Instructions

### Step 1 — Sharpen the pattern
Restate the observed pattern with specifics: what, when, who, by what measure, magnitude, baseline comparison. If any of these are vague, the hypotheses will be vague too.

### Step 2 — Capture and seal the leading hypothesis
What does the user already think happened? Record it; do not let it dominate generation.

### Step 3 — Generate hypotheses across categories
Walk the categories deliberately:

- **Causal — internal:** What did the user / team / system do that could produce this pattern?
- **Causal — external:** What outside event, market shift, regulatory change, seasonal effect, competitor action, or world event could produce this?
- **Selection / sampling:** Did the population being measured change? (New cohort entering, old cohort leaving, instrumentation changing what gets observed.)
- **Measurement:** Did the way the metric is computed change? Did a logging bug, a definition change, a tooling update, or a data pipeline modification affect the measurement?
- **Confounding:** What unobserved variable could plausibly cause both the apparent cause and the apparent effect?
- **Coincidence / regression to mean:** If the prior period was unusually low or high, the current period may be reversion. Check the baseline trend.

Generate at least one hypothesis per applicable category.

### Step 4 — Specify each hypothesis
For each:
- **Statement:** what the hypothesis claims, in one sentence.
- **Mechanism:** how it would produce the observed pattern.
- **Other predictions:** what else it predicts that we could observe.
- **Disconfirming observation:** what we'd see (or fail to see) if the hypothesis were wrong.
- **Prior plausibility:** low / moderate / high (based on what we already know about the system).

### Step 5 — Identify confounders
Even outside the "confounding" category, list 1–3 lurking variables that could be common causes producing both apparent cause and apparent effect across multiple hypotheses.

### Step 6 — Design distinguishing tests
A distinguishing test is one whose result is *predicted differently* by at least two hypotheses. For each test:
- **Observation / analysis:** what we'd look at.
- **Predicted result under H_i:** for each relevant hypothesis.
- **Hypotheses ruled in / out by each result.**
- **Cost / feasibility.**

The goal is a sequence of tests that, if executed, would converge on a single surviving hypothesis (or reveal that the pattern is a combination).

### Step 7 — Most diagnostic observation
Which single observation would do the most work to narrow the hypothesis space? Pursue that one first.

### Step 8 — Most parsimonious hypothesis
Which hypothesis requires the fewest unobserved entities or unusual circumstances? Note as a candidate, but do not treat as decisive.

### Step 9 — Action recommendation
- Which hypothesis is currently most plausible given prior evidence?
- Which test should be run first?
- What's the budget (time, cost) for testing before committing to an explanation?
- If multiple hypotheses survive testing, which decision is robust to the remaining uncertainty?

---

## False-Positive Prevention

1. **Single-hypothesis tunneling.** Stopping after the first plausible explanation. Always generate 4+; the leading explanation often falls when it has competition.
2. **Category skipping.** "Measurement isn't relevant" — often false, especially for sudden changes. Walk every category.
3. **Distinct-on-paper, identical-in-test.** Two hypotheses that share all observable predictions are functionally one hypothesis. Force a distinguishing test.
4. **Confirmation-shaped tests.** Designing tests that would confirm one hypothesis without checking what would distinguish it from alternatives.
5. **Parsimony as verdict.** "The simplest explanation wins" — only as a tiebreaker between hypotheses with equal evidence. Without evidence, parsimony is a heuristic, not a decision.
6. **Ignoring base rates of explanations.** "User behavior changed" and "logging bug" both explain a metric change; logging bugs are more common than coordinated user behavior shifts. Use base rates.
7. **Coincidence-blindness.** Especially for short observation windows, regression to the mean is often the right answer. Always include it as a candidate.
8. **Hypothesis sprawl.** Generating 12 hypotheses dilutes attention. Cap at 7 and merge duplicates.

---

## Output Format

```
# Hypothesis generation — [observed pattern]

## Pattern (sharp)
- What: [...]
- When: [...]
- Who / what population: [...]
- Measure: [...]
- Magnitude: [...]
- Baseline comparison: [...]

## What changed around that time
- Internal: [...]
- External: [...]
- Measurement: [...]

## Leading hypothesis (sealed)
- [User's current explanation]

## Hypotheses

### H1 — [name, category]
- Statement: [...]
- Mechanism: [...]
- Other predictions: [...]
- Disconfirming observation: [...]
- Prior plausibility: [low / moderate / high]

### H2 — [name, category]
[Same fields]

### H3 — H7 …

## Confounders
- [Variable that could be common cause across hypotheses]

## Distinguishing tests
| # | Test                               | Predicted result H1 | H2  | H3  | …   | Rules in/out | Cost |
|---|------------------------------------|---------------------|-----|-----|-----|--------------|------|
| 1 | [analysis or observation]          | up                  | down| flat| …   | distinguishes H1 vs H2| low |
| 2 | …                                  |                     |     |     |     |              |      |

## Most diagnostic test
- Test: [#]
- Why: [splits the hypothesis space most efficiently]

## Most parsimonious hypothesis
- H[#]
- Note: parsimony is a tiebreaker, not a verdict.

## Action recommendation
- Currently most plausible: H[#]
- Run first: Test [#]
- Test budget: [time / cost cap]
- Robust action under remaining uncertainty: [if multiple hypotheses survive, what to do anyway]
```

---

## Verification

- [ ] At least 4 hypotheses generated, covering causal-internal, causal-external, selection, measurement, confounding, coincidence (where applicable).
- [ ] Each hypothesis has statement, mechanism, other predictions, disconfirming observation, prior plausibility.
- [ ] Confounders identified.
- [ ] Distinguishing tests designed (not just confirmation tests).
- [ ] Predicted results for each hypothesis under each test.
- [ ] Most diagnostic test identified.
- [ ] Most parsimonious hypothesis identified but not treated as decisive.
- [ ] Action recommendation includes test sequencing.
- [ ] Coincidence / regression-to-mean considered.
- [ ] No two hypotheses sharing all observable predictions.
