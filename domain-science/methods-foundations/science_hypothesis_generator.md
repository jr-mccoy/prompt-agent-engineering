---
title: "Hypothesis Generator"
category: science/
description: "Generate testable hypotheses from observations with clear predictions, falsification criteria, and experimental approach suggestions"
techniques:
  - RT-01
  - RT-03
  - QA-04
  - NE-09
difficulty: intermediate
tags:
  - hypothesis-generation
  - scientific-method
  - testability
  - falsification
  - predictions
  - research-planning
updated: "2026-01-28"
---

# Hypothesis Generator

**Objective:** Starting from observations or preliminary data, generate testable hypotheses with clear predictions, falsification criteria, and suggested experimental approaches. Iteratively refine hypotheses based on feasibility and novelty assessment.

**Instructions:**

1. **Gather the observation or preliminary finding**
   * Request the starting point for hypothesis generation:
     - A puzzling observation from the field or lab
     - An unexpected finding from preliminary data
     - A pattern noticed across studies or datasets
     - An anomaly that current theories don't explain
     - A practical problem seeking explanation
   * Ask clarifying questions:
     - "What specifically have you observed?"
     - "Under what conditions did you observe this?"
     - "How reliable/replicable is this observation?"
     - "What is the context (field, prior research, your expertise)?"
   * Confirm understanding: "You observed [X] under [conditions], and you're wondering [what might explain it / whether it generalizes / etc.]. Is that correct?"

2. **Analyze the observation for hypothesis directions**
   * Break down the observation into components:
     - What is happening? (the phenomenon)
     - When/where does it occur? (boundary conditions)
     - Who/what is involved? (entities and variables)
     - How might it work? (potential mechanisms)
   * Identify the key question types the observation raises:
     - **Descriptive:** What is the nature of this phenomenon?
     - **Correlational:** What co-occurs with this phenomenon?
     - **Causal:** What produces this phenomenon?
     - **Mechanistic:** How does this phenomenon work?
     - **Functional:** What purpose does this serve?
     - **Comparative:** How does this vary across contexts?
   * Consider multiple levels of analysis:
     - Proximate explanations (immediate causes)
     - Distal explanations (evolutionary/historical causes)
     - Micro-level (individual units)
     - Macro-level (systems, populations)

3. **Generate multiple candidate hypotheses**
   * Produce 3-5 alternative hypotheses that could explain the observation:

   **For each hypothesis, specify:**
   - **Hypothesis Statement:** Clear, declarative statement
   - **Theoretical Basis:** Why this explanation is plausible
     - Connect to existing theories where possible
     - If novel, explain the reasoning
   - **Assumptions:** What must be true for this hypothesis to hold
   - **Relationship Type:** Causal, correlational, moderating, mediating

   **Example Format:**
   ```
   Hypothesis 1: [Variable X] causes [Variable Y] through [Mechanism Z]

   Theoretical Basis: This aligns with [Theory A], which predicts...

   Assumptions:
   - [Variable X] is present/manipulable
   - [Mechanism Z] is operative in this context
   - No confounding variables override this effect

   Relationship: Causal (X → Z → Y mediation)
   ```

   * Include at least one hypothesis that challenges conventional thinking
   * Consider hypotheses at different levels of specificity
   * Note: "These hypotheses represent candidate explanations, not established facts. Scientific progress involves testing and potentially rejecting them."

4. **Specify testable predictions for each hypothesis**
   * Transform each hypothesis into specific, observable predictions:

   **Prediction Requirements:**
   - **Observable:** Can be measured or detected
   - **Specific:** Precise enough to confirm or disconfirm
   - **Novel:** Goes beyond what is already known
   - **Risky:** Could be wrong (not trivially true)

   **For each prediction, specify:**
   - What you would observe IF the hypothesis is true
   - What you would observe IF the hypothesis is false
   - The comparison: "If H1, then [outcome A]; if not H1, then [outcome B]"

   **Example:**
   ```
   Hypothesis: Caffeine improves memory consolidation during sleep

   Prediction 1: Participants who consume caffeine before sleep will
   show higher next-day recall on memory tasks than those who consume
   placebo.

   If true: Caffeine group recall > Placebo group recall (d > 0.3)
   If false: Caffeine group recall ≤ Placebo group recall

   Prediction 2: The effect will be specific to tasks completed
   before sleep (consolidation), not tasks completed after waking
   (encoding).

   If true: Caffeine × Timing interaction (pre-sleep tasks show
   effect, post-wake tasks don't)
   If false: Caffeine effect on all tasks or no tasks
   ```

   * Distinguish between:
     - Primary predictions (core test of the hypothesis)
     - Secondary predictions (additional implications if true)
     - Auxiliary predictions (test underlying assumptions)

5. **Define falsification criteria**
   * Specify what evidence would conclusively refute each hypothesis:

   **Falsification Requirements:**
   - **Decisive:** Not easily explained away
   - **Obtainable:** Feasible to gather this evidence
   - **Fair:** A genuine test, not a strawman

   **For each hypothesis, state:**
   - "This hypothesis would be falsified if..."
   - The specific result or pattern that would disconfirm it
   - How confident you could be in rejection given this result

   **Example:**
   ```
   Hypothesis: Social isolation causes depression in adolescents

   Falsification Criteria:
   1. A randomized intervention reducing isolation shows no effect
      on depression symptoms (strong falsification)
   2. Longitudinal data shows depression precedes isolation rather
      than following it (temporal falsification)
   3. Identical twins discordant for isolation show no depression
      differences (genetic confound falsification)

   Note: Null findings in underpowered studies or with poor measures
   would NOT constitute strong falsification.
   ```

   * Acknowledge: "Falsification is rarely absolute in science. A single null result doesn't definitively disprove a hypothesis, but consistent null results across rigorous tests should reduce confidence substantially."

6. **Suggest experimental approaches**
   * Recommend research designs to test each hypothesis:

   **For each hypothesis, propose:**
   - **Design Type:** Experimental, quasi-experimental, correlational, qualitative
   - **Key Features:** What makes this design appropriate for this hypothesis
   - **Sample/Population:** Who or what would be studied
   - **Manipulation or Comparison:** What is varied or compared
   - **Measurement:** How outcomes would be assessed
   - **Critical Controls:** What must be controlled for a valid test

   **Example:**
   ```
   Hypothesis: Sleep deprivation impairs moral reasoning

   Experimental Approach A (Laboratory Experiment):
   - Design: Between-subjects RCT
   - Sample: Healthy adults, N = 80
   - Manipulation: Sleep-deprived (4 hrs) vs. rested (8 hrs)
   - Measure: Moral dilemma responses, reaction times, justifications
   - Controls: Time of testing, caffeine, prior sleep
   - Strengths: Causal inference, controlled environment
   - Weaknesses: Artificial setting, demand characteristics

   Experimental Approach B (Field Study):
   - Design: Within-subjects observation
   - Sample: Medical residents, N = 40
   - Comparison: Same individuals on-call vs. off-call
   - Measure: Naturalistic moral decisions in practice
   - Controls: Case severity, patient characteristics
   - Strengths: Ecological validity, real consequences
   - Weaknesses: Confounds with workload, stress
   ```

   * Rank approaches by:
     - Feasibility given typical constraints
     - Strength of causal inference
     - Generalizability of findings

7. **Assess feasibility and novelty**
   * Evaluate each hypothesis on practical dimensions:

   **Feasibility Assessment:**
   | Hypothesis | Resources Needed | Timeline | Technical Challenges | Ethical Issues | Feasibility Score |
   |------------|-----------------|----------|---------------------|----------------|-------------------|
   | H1 | [Low/Med/High] | [Months] | [Description] | [Description] | [1-5] |
   | H2 | [Low/Med/High] | [Months] | [Description] | [Description] | [1-5] |

   **Novelty Assessment:**
   - How much would testing this hypothesis advance the field?
   - What is already known that this builds on?
   - What new ground would this break?
   - Is this incremental advancement or potential paradigm shift?

   **Priority Matrix:**
   | Hypothesis | Scientific Importance | Practical Importance | Feasibility | Priority Rank |
   |------------|----------------------|---------------------|-------------|---------------|
   | H1 | [Rating] | [Rating] | [Rating] | [1-n] |

8. **Refine and finalize hypotheses**
   * Based on analysis, recommend 1-2 hypotheses for priority testing
   * For recommended hypotheses, provide:
     - Refined statement with maximum clarity
     - Primary prediction to test first
     - Recommended experimental approach
     - Potential pitfalls and how to avoid them
     - What a successful test would contribute to the field

   * Offer iterative refinement: "Based on this analysis, would you like to:
     - Refine any of these hypotheses further?
     - Generate additional hypotheses?
     - Explore experimental designs in more detail?
     - Discuss how to address a specific limitation?"

   * Conclude with: "These hypotheses represent starting points for investigation. The scientific process will likely require refinement as evidence accumulates. Be prepared to revise or abandon hypotheses that don't survive empirical testing."

**Science-Specific Considerations:**
- Good hypotheses are falsifiable—unfalsifiable claims are not scientific hypotheses
- The goal is not to "prove" hypotheses but to test them rigorously
- Negative results (falsification) are scientifically valuable, not failures
- Hypotheses should connect to existing theory when possible, or explicitly propose new theoretical frameworks
- Consider pre-registration to prevent post-hoc hypothesis modification
- Multiple competing hypotheses are preferable to single "pet" hypotheses—approach with equipoise
- Disciplinary norms affect what counts as a good hypothesis (e.g., psychology vs. physics vs. biology)
- Creative hypothesis generation is valuable, but hypotheses must ultimately be testable

**Expected Output:** A comprehensive hypothesis development document containing:
1. Observation/finding summary and clarification
2. Analysis of the observation (components, question types, levels)
3. 3-5 candidate hypotheses with theoretical basis and assumptions
4. Testable predictions for each hypothesis (with if-true/if-false specifications)
5. Falsification criteria for each hypothesis
6. Suggested experimental approaches with comparisons
7. Feasibility and novelty assessment
8. Priority ranking and recommendations
9. Refinement options for next steps

**Example Output:**

---

## Hypothesis Generation: [Observation/Phenomenon]

### Observation Summary

**What you observed:** [Description of the phenomenon]

**Context:** [Field, setting, circumstances]

**Reliability:** [How consistent/replicable is this observation?]

### Analysis

**Key Question Types Raised:**
- Causal: What produces this effect?
- Mechanistic: How does it work?
- Comparative: Does it vary across contexts?

**Levels to Consider:**
- Proximate: Immediate mechanisms
- Distal: Why this mechanism evolved/developed

---

### Candidate Hypotheses

**Hypothesis 1: [Name/Label]**

*Statement:* [Variable X] produces [Outcome Y] through [Mechanism Z].

*Theoretical Basis:* This aligns with [Theory], which holds that...

*Assumptions:*
- [Assumption 1]
- [Assumption 2]

*Predictions:*
- If H1 true: [Specific observable outcome]
- If H1 false: [Alternative outcome]

*Falsification Criteria:* H1 would be falsified if [specific evidence] were observed in a well-powered study.

*Suggested Test:* [Brief experimental approach]

---

**Hypothesis 2: [Name/Label]**

*Statement:* [Alternative explanation]

*Theoretical Basis:* Alternatively, [competing theory] suggests...

*Assumptions:*
- [Different assumptions]

*Predictions:*
- If H2 true: [Different outcome pattern]
- If H2 false: [Alternative]

*Falsification Criteria:* H2 would be falsified if...

*Suggested Test:* [Brief experimental approach]

---

**Hypothesis 3: [Contrarian/Novel]**

*Statement:* [Challenges conventional thinking]

*Why Consider This:* Current explanations may overlook...

[Continue pattern]

---

### Priority Assessment

| Hypothesis | Scientific Importance | Feasibility | Novelty | Priority |
|------------|----------------------|-------------|---------|----------|
| H1 | High | High | Moderate | 1 |
| H2 | High | Moderate | Moderate | 2 |
| H3 | Moderate | Low | High | 3 |

### Recommendation

**Priority Hypothesis:** H1: [Statement]

**Recommended First Test:** [Experimental approach] because [rationale]

**Key Prediction to Test:** [Most decisive prediction]

**Potential Pitfalls:**
- [Pitfall 1] — Address by [mitigation]
- [Pitfall 2] — Address by [mitigation]

**If Confirmed:** This would advance understanding of [contribution]

**If Falsified:** This would redirect attention to [alternative explanations]

---

### Next Steps

Would you like to:
1. Refine any of these hypotheses further?
2. Generate additional candidate explanations?
3. Develop a detailed experimental protocol for the priority hypothesis?
4. Discuss how to address specific feasibility constraints?

---

**Techniques Used:**
- **RT-01 (Chain-of-Thought):** Explicit step-by-step reasoning from observation to hypothesis to prediction
- **RT-03 (Tree of Thoughts):** Multiple competing hypotheses generated and compared systematically
- **QA-04 (Uncertainty Acknowledgment):** Clear statements about what is hypothesis vs. established fact; falsifiability emphasized
- **NE-09 (Scope Reduction Pressure):** Refinement process narrows from broad observation to specific, testable hypotheses
