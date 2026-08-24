---
title: "Experimental Design Advisor"
category: science/
description: "Propose experimental designs based on research questions and constraints, including controls, sample sizes, randomization, and confound identification"
techniques:
  - RT-03
  - QA-02
  - DS-02
  - CM-02
  - NE-10
difficulty: advanced
tags:
  - experimental-design
  - research-methodology
  - sample-size
  - power-analysis
  - randomization
  - confound-control
updated: "2026-01-28"
---

# Experimental Design Advisor

**Objective:** Given a research question and practical constraints (budget, time, equipment, sample access), propose appropriate experimental designs with controls, sample size considerations, randomization strategies, and potential confound identification.

**Instructions:**

1. **Clarify the research question and goals**
   * Request the primary research question in clear, testable form
   * Identify the key variables:
     - Independent variable(s): What is being manipulated or compared?
     - Dependent variable(s): What outcomes are being measured?
     - Potential moderators: Factors that might influence the effect
     - Potential mediators: Mechanisms through which effects might operate
   * Confirm the research goal:
     - Exploratory (what happens when...?)
     - Descriptive (what is the nature of...?)
     - Explanatory (why does...?)
     - Causal (does X cause Y?)
   * Ask: "Is the goal to establish causation, or is correlation/association sufficient for your purposes?"

2. **Assess practical constraints**
   * Gather constraint information systematically:
     - **Budget:** Total available, major cost categories
     - **Time:** Duration available for data collection, any deadlines
     - **Equipment/Resources:** What is available vs. needs to be acquired
     - **Sample access:** Target population, recruitment feasibility, expected participation rate
     - **Personnel:** Research team size and expertise
     - **Ethical constraints:** IRB requirements, vulnerable populations, deception limits
   * Create a constraint summary:
     | Constraint | Status | Impact on Design |
     |------------|--------|------------------|
     | Budget | [$X available] | [Limits sample size to ~N] |
     | Time | [X months] | [Limits to cross-sectional] |
     | Sample access | [Description] | [May require convenience sampling] |
   * Note: "Constraints shape design possibilities—there is no 'perfect' design, only designs that optimize within real-world limits."

3. **Generate multiple design options**
   * Propose 2-4 viable experimental designs, considering:

   **Design Types to Consider:**
   - **True Experiments:** Random assignment to conditions
     - Between-subjects: Different participants in each condition
     - Within-subjects: Same participants across conditions
     - Mixed designs: Combination of between and within factors
   - **Quasi-Experiments:** No random assignment but comparison groups
     - Non-equivalent control group design
     - Interrupted time series
     - Regression discontinuity
   - **Correlational/Observational:** No manipulation
     - Cross-sectional surveys
     - Longitudinal panel studies
     - Cohort studies

   * For each proposed design, specify:
     - Design type and rationale
     - Conditions/groups
     - Assignment method
     - Measurement timeline
     - Strengths for this research question
     - Limitations and threats to validity

   * Compare designs using:
     | Criterion | Design A | Design B | Design C |
     |-----------|----------|----------|----------|
     | Internal validity | [Rating] | [Rating] | [Rating] |
     | External validity | [Rating] | [Rating] | [Rating] |
     | Feasibility | [Rating] | [Rating] | [Rating] |
     | Cost | [Estimate] | [Estimate] | [Estimate] |
     | Time required | [Estimate] | [Estimate] | [Estimate] |

4. **Develop control group strategy**
   * Recommend appropriate control conditions:
     - **No-treatment control:** Baseline comparison
     - **Placebo control:** Controls for expectancy effects
     - **Active control:** Alternative treatment comparison
     - **Waitlist control:** Delayed treatment (ethical in some contexts)
     - **Attention control:** Matches time/attention without active ingredient
   * Consider control group ethics:
     - "Is it ethical to withhold treatment? Consider equipoise."
     - "Can waitlist or crossover designs address ethical concerns?"
   * Specify what the control condition controls FOR:
     - Maturation effects
     - History effects
     - Testing effects
     - Regression to the mean
     - Demand characteristics
     - Experimenter effects

5. **Address sample size and power considerations**
   * Discuss the components of power analysis:
     - **Effect size (d, r, OR):** Expected magnitude of the effect
       - Draw from prior research when available
       - Consider practical significance, not just statistical
       - Smaller expected effects require larger samples
     - **Alpha level:** Typically .05; justify if different
     - **Desired power:** Typically .80; .90 for critical studies
     - **Design factors:** Number of groups, within vs. between, covariates

   * Provide sample size guidance:
     - "For a medium effect (d = 0.5) with power = .80 and alpha = .05, a two-group between-subjects design requires approximately N = 64 per group (128 total)."
     - "Your specific parameters would require [calculation or direction to tools]."

   * Recommend power analysis tools:
     - G*Power (free software)
     - pwr package in R
     - Online calculators for specific designs

   * Note: "I can provide estimates and guidance, but formal power analysis should be calculated using appropriate software for your specific design."

6. **Plan randomization strategy**
   * Recommend appropriate randomization method:
     - **Simple randomization:** Coin flip / random number (risk of imbalance)
     - **Block randomization:** Ensures equal group sizes at intervals
     - **Stratified randomization:** Balances key covariates across conditions
     - **Cluster randomization:** Randomize groups (classrooms, clinics) not individuals
     - **Adaptive randomization:** Adjusts probabilities to maintain balance

   * Specify randomization implementation:
     - When in the procedure does randomization occur?
     - Who generates the randomization sequence?
     - How is allocation concealed (to prevent selection bias)?
     - How is blinding maintained (single, double, triple blind)?

   * Address when random assignment isn't possible:
     - Quasi-experimental alternatives
     - Statistical controls for pre-existing differences
     - Propensity score matching

7. **Identify potential confounds and threats to validity**
   * Systematically evaluate threats to internal validity:
     - **Selection:** Pre-existing differences between groups
     - **History:** External events during the study
     - **Maturation:** Changes due to time passing
     - **Testing:** Effects of repeated measurement
     - **Instrumentation:** Changes in measurement
     - **Regression:** Movement toward the mean
     - **Attrition:** Differential dropout
     - **Diffusion:** Treatment contamination across groups

   * For each identified threat, propose mitigation:
     | Threat | Risk Level | Mitigation Strategy |
     |--------|------------|---------------------|
     | [Threat] | [High/Medium/Low] | [How to address] |

   * Evaluate threats to external validity:
     - Population validity: Generalizability to other people
     - Ecological validity: Generalizability to other settings
     - Temporal validity: Generalizability across time

   * Assess construct validity:
     - Do measures actually capture the intended constructs?
     - Are manipulations actually manipulating the intended variable?
     - Recommend manipulation checks and attention checks

8. **Provide the complete experimental design proposal**
   * Synthesize recommendations into a coherent design document:
     - Executive summary of recommended design
     - Detailed protocol including:
       - Participants (eligibility, recruitment, sample size with justification)
       - Materials (measures, manipulations, equipment)
       - Procedure (step-by-step with randomization timing)
       - Analysis plan (primary analyses, secondary analyses, assumptions)
     - Threat assessment and mitigation plan
     - Timeline and resource requirements
     - Limitations of the proposed design

   * Conclude with: "This design represents one viable approach given your constraints. Alternative designs [listed above] offer different trade-offs. Consult with methodological experts in your field for additional guidance."

**Science-Specific Considerations:**
- Experimental design involves trade-offs; no design is perfect
- Internal validity (confidence in causation) often trades off with external validity (generalizability)
- Practical and ethical constraints legitimately shape design choices
- Pilot testing is valuable—consider recommending pilot studies for novel designs or measures
- Pre-registration of hypotheses and analysis plans is increasingly expected in many fields
- Different disciplines have different design conventions—acknowledge field-specific norms
- Replication considerations: Design with future replication in mind

**Expected Output:** A complete experimental design proposal containing:
1. Research question and variable clarification
2. Constraint assessment summary
3. Multiple design options with comparison table
4. Recommended design with full rationale
5. Control group strategy with ethical considerations
6. Sample size guidance with power analysis direction
7. Randomization protocol
8. Threat assessment with mitigation strategies
9. Implementation timeline and resource needs
10. Design limitations and alternatives

**Example Output:**

---

## Experimental Design Proposal: [Research Question]

### Research Question Clarification
**Primary Question:** Does [intervention X] improve [outcome Y] compared to [control condition]?

**Variables:**
- **Independent Variable:** [X] — [description, levels]
- **Dependent Variable:** [Y] — [description, measurement]
- **Potential Confounds:** [age, prior experience, etc.]

**Goal:** Causal inference (establish that X causes Y)

### Constraint Assessment

| Constraint | Your Situation | Design Implications |
|------------|----------------|---------------------|
| Budget | $5,000 | Limits N to ~60; no incentive payments |
| Time | 3 months | Cross-sectional or short-term follow-up only |
| Sample | University students | Limits generalizability to young adults |
| Ethics | IRB required | No deception; informed consent needed |

### Design Options Comparison

| Criterion | Between-Subjects RCT | Within-Subjects | Quasi-Experimental |
|-----------|---------------------|-----------------|-------------------|
| Internal validity | High | High (but carryover risk) | Moderate |
| External validity | Moderate | Moderate | Moderate-High |
| Feasibility | High | Moderate | High |
| Sample size needed | 64/group | 32 total | ~50/group |
| Cost | $4,000 | $2,000 | $3,500 |

### Recommended Design: Between-Subjects Randomized Controlled Trial

**Rationale:** Given the goal of causal inference and available resources, a two-group between-subjects RCT offers the strongest internal validity while remaining feasible.

**Design Details:**
- **Groups:** Treatment (n=35) vs. Active Control (n=35)
- **Assignment:** Stratified randomization by [key covariate]
- **Timeline:** Pre-test → Intervention (2 weeks) → Post-test → 4-week follow-up
- **Blinding:** Single-blind (participants unaware of condition hypotheses)

### Sample Size Justification
Based on prior research suggesting a medium effect (d = 0.50):
- Power = .80, Alpha = .05, two-tailed
- Required N = 64 per group for adequate power
- With expected 10% attrition, recruit 70 per group (140 total)
- **Given your constraints (N = 70 total), power is approximately .52 for d = 0.50**
- Options: Accept lower power, seek larger effect, or increase sample

### Randomization Protocol
1. Screen participants for eligibility
2. Administer pre-test measures
3. Use block randomization (blocks of 4) stratified by [gender/age]
4. Generate sequence using random.org prior to recruitment
5. Maintain allocation concealment until assignment moment

### Threat Assessment

| Threat | Risk | Mitigation |
|--------|------|------------|
| Selection | Low | Random assignment addresses |
| Attrition | Moderate | Track reasons; intent-to-treat analysis |
| Demand characteristics | Moderate | Active control; blind to hypotheses |
| History | Low | Brief study duration; simultaneous conditions |
| Measurement | Low | Standardized measures; trained assessors |

### Limitations of This Design
- Sample limits generalizability to university students
- Short follow-up (4 weeks) doesn't assess long-term effects
- Underpowered for small effects (would need N > 200)
- Self-report measures may be susceptible to response bias

### Alternative Considered
If [constraint changes], consider [alternative design] which would offer [benefit] at the cost of [trade-off].

---

**Techniques Used:**
- **RT-03 (Tree of Thoughts):** Multiple design options generated and systematically compared
- **QA-02 (Adversarial Stress-Test):** Threats to validity identified and addressed proactively
- **DS-02 (Metric Specification):** Specific numbers for sample size, power, effect sizes
- **CM-02 (Constraint Specification):** Clear must/must-not requirements from practical limits
- **NE-10 (Probability-Weighted Scenarios):** Power analysis presents different probability outcomes
