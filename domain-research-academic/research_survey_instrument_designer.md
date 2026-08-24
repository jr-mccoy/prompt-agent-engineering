---
title: "Survey Instrument Designer — Constructs to Items, Scales, Bias Checks, and Pretest Plan"
category: research-academic/quantitative
description: "Design a survey instrument from constructs through item drafting, response scale selection, bias control (acquiescence, social desirability, order effects, satisficing), branching logic, length budget, and cognitive-interview pretest. Outputs the full instrument with each item annotated for construct and bias mitigation."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - DS-02
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - survey-design
  - instrument
  - psychometrics
  - response-scales
  - bias
updated: "2026-05-10"
reasoning:
  styles: [structured, psychometric, anti-bias]
  stakes: variable
  horizon: weeks
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: variable
  collaboration: solo_or_team
  output_format: annotated_survey_instrument
  user_role: [researcher, ux_researcher, market_researcher, hr, policy]
  mode: [design, plan]
related_prompts:
  - domain-research-academic/research_question_formulation.md
  - domain-research-academic/research_interview_guide_designer.md
  - domain-research-academic/research_qualitative_coding_scheme.md
---

# Survey Instrument Designer

**Objective:** Design a survey from constructs to fielded instrument. Walk through: construct definition, operationalization, item drafting, response scale selection, bias mitigation, branching logic, length budget, and cognitive-interview pretest. Output: the full instrument with each item annotated for the construct it measures and the biases it mitigates.

**When to use:**
- Quantitative survey design for academic, UX, market, organizational, or policy research.
- Instrument development for repeated measurement (employee engagement, customer satisfaction, public opinion).
- Adaptation of an existing scale to a new context (where psychometric properties may shift).

**When NOT to use:**
- Open-ended exploratory work (use interview guides).
- Single-question polls (overkill).
- A/B testing — use direct behavioral measurement, not self-report.

**Audience:** Researchers, UX / market researchers, HR analysts, policy researchers.

---

## Inputs / Context

1. **Constructs to measure.** What latent variables (e.g., "engagement", "trust", "perceived ease of use", "intent to recommend").
2. **Target population.**
3. **Expected sample size.**
4. **Mode** (online, phone, in-person, mail).
5. **Length budget** (typically 5–15 minutes online).
6. **Existing validated scales** to consider.
7. **Comparison context** (one-shot, longitudinal, cross-population).

---

## Constraints

### Must
- For each construct: **define** it conceptually, **operationalize** it (what observable indicators count), then draft items.
- Use **validated scales** when available — don't reinvent SUS, NPS, GAD-7, etc.
- Each item: single thought, plain language, no double-barrels, no jargon, no presupposition.
- Choose **response scales** matched to the construct: Likert for attitudes, frequency for behaviors, semantic differential for evaluations, binary only when categories are truly dichotomous.
- Mitigate at least the four major biases: **acquiescence** (yea-saying), **social desirability**, **order effects**, **satisficing**.
- Build **branching logic** so respondents only see relevant items.
- Plan **cognitive interviews** (3–8) and a **soft launch** before full deployment.
- Annotate each item with construct, scale, and bias mitigation.

### Must Not
- Use a 5-point scale where a 7-point would discriminate, or vice versa, without justification.
- Stack many items in identical scale direction — invites acquiescence.
- Phrase sensitive items so the desirable answer is obvious.
- Group all items measuring one construct contiguously — invites halo and order effects.
- Field without cognitive interviews; first-draft items often misunderstand respondent reading.

---

## Instructions

### Step 1 — Construct table
For each construct: name, conceptual definition (1–2 sentences), what behavior / attitude / cognition it predicts, whether a validated scale exists (cite if so).

### Step 2 — Operationalization
For each construct: what observable indicators map to the construct? Aim for 3–7 items per construct (single-item measures are discouraged unless the construct is concrete and unidimensional).

### Step 3 — Item drafting
Per item:
- Stem (the question or statement)
- Test against rules: single thought, plain language, no double-barrel, no presupposition, no leading
- Reading level appropriate to population

### Step 4 — Response scale selection
- **Likert (agreement):** 5 or 7 points; 7 if discrimination matters, 5 if simplicity matters; include "neither agree nor disagree" or force choice
- **Frequency:** anchored ("never / rarely / sometimes / often / always") with rough quantification where possible
- **Semantic differential:** 7-point bipolar
- **Binary:** only when truly dichotomous
- **Numeric (NPS, sliders):** when interval interpretation is meaningful

State for each item which scale and why.

### Step 5 — Bias mitigation
- **Acquiescence:** mix item polarity (some reverse-coded), but document for analysis (reverse-coded items can introduce their own noise)
- **Social desirability:** anonymize when possible; use indirect framing ("some people think... do you?"); use behavioral / observational items where feasible
- **Order effects:** randomize item order within scales; counterbalance scale orders across respondents; place sensitive items mid-survey, not first or last
- **Satisficing:** keep total length short, use attention-check items, vary scale anchors to prevent straightlining

### Step 6 — Branching logic
Map respondent paths. Avoid asking irrelevant questions.

### Step 7 — Length budget
Estimate completion time (rule of thumb: 4–7 seconds per simple item, longer for complex). Cut items if over budget; long surveys produce satisficing.

### Step 8 — Cognitive interview pretest
- N: 3–8 respondents from target population
- Method: think-aloud or retrospective probe ("what came to mind when you read this?")
- Capture: item misinterpretation, response option gaps, pacing issues
- Revise based on patterns

### Step 9 — Soft launch
Field to a small subsample (5–10% of target N). Check: completion rate, dropoff points, suspicious response patterns (straightlining, speeding), scale variance (if everyone gives the same answer, the item isn't discriminating).

### Step 10 — Final instrument with annotations
Each item tagged: construct, scale, bias mitigation, expected variance.

---

## False-Positive Prevention

1. **Reinventing validated scales.** SUS, NPS, GAD-7, MBI exist for reasons; reinventing wastes effort and breaks comparability.
2. **Double-barrels.** "Was the service fast and friendly?" — split.
3. **Presupposition.** "How frustrated were you?" assumes frustration.
4. **All-positive scaling.** All items in one direction invites yea-saying.
5. **Long survey.** Past 12–15 minutes online, satisficing dominates.
6. **No cognitive interviews.** First-draft items usually misread by some respondents.
7. **Identical-anchor scales.** Invite straightlining.
8. **Single-item construct.** OK for very concrete things; bad for complex constructs.

---

## Output Format

```
# Survey instrument — [topic]

## Constructs
| Construct | Definition | Validated scale exists? | Items planned |
|-----------|------------|-------------------------|---------------|
| [name]    | [...]      | [yes — cite / no]       | [N]           |
| [...]     |            |                         |               |

## Item bank
| # | Construct | Item stem | Scale | Anchors | Bias mitigation | Notes |
|---|-----------|-----------|-------|---------|-----------------|-------|
| 1 | [name]    | [...]     | 7-pt Likert | strongly disagree → strongly agree | mixed polarity | [validated from X] |
| 2 | [...]     | [...]     | freq 5-pt | never → always | anonymized | reverse-coded |
| ... |          |           |       |         |                 |       |

## Branching logic
- If [item X] = [value], then [show / skip] [item Y]
- [...]

## Order
- Block 1: [items]
- Block 2: [items, with randomization within block]
- [...]

## Length budget
- Estimated completion time: [minutes]
- Cut items if over: [items considered for cut]

## Cognitive interviews
- N: [3–8]
- Method: [think-aloud / retrospective]
- Recruitment: [...]
- Revision criteria: [misinterpretation patterns, pacing]

## Soft launch
- N: [5–10% of target]
- Metrics tracked: [completion, dropoff, straightlining, scale variance]
- Go/no-go criteria for full launch: [...]

## Demographics block (placement: end)
- [items]
```

---

## Verification

- [ ] Each construct defined and operationalized.
- [ ] Validated scales used where available.
- [ ] Items single-thought, plain, non-leading.
- [ ] Response scales matched to construct.
- [ ] Acquiescence mitigated (mixed polarity).
- [ ] Social desirability mitigated.
- [ ] Order effects mitigated (randomization).
- [ ] Satisficing controlled (length, attention checks).
- [ ] Branching logic mapped.
- [ ] Cognitive interview plan with N and method.
- [ ] Soft launch metrics defined.
- [ ] Each item annotated for construct, scale, bias mitigation.
