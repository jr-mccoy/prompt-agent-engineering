# Science & Research Field Guide

**Purpose:** Prompt engineering techniques and ideas specifically curated for scientists, researchers, research students, lab managers, science communicators, and R&D professionals across all scientific disciplines (biology, chemistry, physics, environmental science, etc.).

---

## Top 10 Prompt Ideas for Science & Research

### 1. Literature Review Synthesizer
Systematically analyze a collection of research papers on a topic, extracting methodologies, key findings, contradictions, gaps, and emerging trends. Generate structured synthesis with citation mapping and research frontier identification.

### 2. Experimental Design Advisor
Given a research question and constraints (budget, time, equipment, sample access), propose experimental designs with appropriate controls, sample sizes, randomization strategies, and potential confounds. Include power analysis considerations.

### 3. Hypothesis Generator and Refinement Tool
Starting from observations or preliminary data, generate testable hypotheses with clear predictions, falsification criteria, and suggested experimental approaches. Iteratively refine based on feasibility and novelty assessment.

### 4. Statistical Analysis Selector
Given a research question, data structure, and assumptions, recommend appropriate statistical methods with justification. Include assumption checking procedures, effect size considerations, and interpretation guidance.

### 5. Methods Section Structurer
Help write rigorous methods sections that ensure reproducibility. Prompt for essential details often omitted, suggest standard reporting frameworks (CONSORT, ARRIVE, etc.), and verify completeness against field standards.

### 6. Research Gap Identifier
Analyze existing literature to identify understudied questions, methodological limitations, conflicting findings, and opportunities for novel contribution. Prioritize by scientific importance and feasibility.

### 7. Grant Proposal Logic Checker
Review grant proposal arguments for logical coherence, gap in knowledge justification, innovation claims, feasibility concerns, and alignment between aims and methods. Identify weaknesses and suggest strengthening strategies.

### 8. Data Interpretation Challenger
Given experimental results, generate alternative interpretations, potential confounds, and additional experiments needed to distinguish between explanations. Prevent confirmation bias in result interpretation.

### 9. Science Communication Translator
Transform technical research findings into accessible explanations for different audiences (public, policymakers, journalists, students) while maintaining scientific accuracy. Include appropriate caveats and context.

### 10. Peer Review Assistant
Generate structured peer review feedback covering significance, novelty, methodology rigor, data presentation, interpretation validity, and writing clarity. Balance constructive criticism with acknowledgment of strengths.

---

## Relevant Prompt Engineering Techniques

### Tier 1: Essential Techniques for Science

#### RT-05: Evidence-Based Reasoning
**Relevance:** Core to scientific method
**Pattern:** Require specific evidence (data, citations, experimental results) for all claims
**Science Application:** Literature claims, result interpretation, hypothesis justification
**Why Essential:** Science is evidence-based; unsupported claims are unscientific

#### QA-01: Chain-of-Verification
**Relevance:** Scientific rigor and reproducibility
**Pattern:** Self-critique after initial response, verify claims, provide revised analysis
**Science Application:** Result validation, methodology review, conclusion checking
**Why Essential:** Prevents errors from propagating through scientific reasoning

#### RT-01: Chain-of-Thought (CoT)
**Relevance:** Complex scientific reasoning
**Pattern:** Explicit step-by-step reasoning showing logic progression
**Science Application:** Deriving predictions, analyzing data, building arguments
**Why Essential:** Makes reasoning auditable and identifies logical gaps

#### QA-04: Uncertainty Acknowledgment
**Relevance:** Scientific honesty
**Pattern:** State confidence levels, limitations, and verification methods
**Science Application:** Result interpretation, conclusion scope, generalizability
**Why Essential:** Overstatement of findings is a major scientific problem

#### RT-03: Tree of Thoughts
**Relevance:** Hypothesis generation and experimental design
**Pattern:** Generate multiple approaches, compare systematically, select with rationale
**Science Application:** Alternative hypotheses, experimental designs, analytical approaches
**Why Essential:** Science requires considering alternatives, not just confirming preferred ideas

---

### Tier 2: Highly Valuable Techniques

#### QA-02: Adversarial Stress-Test
**Relevance:** Challenging conclusions and methods
**Pattern:** Attack your own answer to find weaknesses and failure modes
**Science Application:** Methodology critique, result interpretation challenges, confound identification
**Why Valuable:** Anticipates peer review criticisms; strengthens arguments

#### DT-02: Specific Focus Areas with Examples
**Relevance:** Systematic analysis and review
**Pattern:** Detailed enumeration of what to examine with concrete examples
**Science Application:** Literature review categories, experimental variables, quality criteria
**Why Valuable:** Ensures comprehensive coverage in complex analyses

#### RT-06: Correlation and Cross-Analysis
**Relevance:** Multi-variable data analysis
**Pattern:** Combine multiple data sources or metrics to identify patterns
**Science Application:** Dataset integration, meta-analysis, systems-level understanding
**Why Valuable:** Science increasingly requires integrating diverse data types

#### DS-02: Metric Specification
**Relevance:** Quantitative rigor
**Pattern:** Define specific, measurable criteria with thresholds
**Science Application:** Effect sizes, significance criteria, quality benchmarks
**Why Valuable:** Provides objective, reproducible standards

#### NE-10: Probability-Weighted Scenarios
**Relevance:** Uncertainty quantification
**Pattern:** Multiple scenarios with explicit probability estimates
**Science Application:** Model predictions, risk assessment, scenario planning
**Why Valuable:** Honest representation of scientific uncertainty

---

### Tier 3: Valuable Supporting Techniques

#### QA-05: Citation Requirements
**Relevance:** Academic integrity and traceability
**Pattern:** Cite sources for claims, distinguish data from interpretation
**Science Application:** Literature review, methodology justification, context setting
**Supporting Role:** Ensures claims are traceable and verifiable

#### ST-02: Structured Sequential Instructions
**Relevance:** Protocol development
**Pattern:** Numbered step-by-step instructions for complex procedures
**Science Application:** Experimental protocols, analytical procedures, workflows
**Supporting Role:** Ensures reproducibility of methods

#### CM-03: Scope Definition
**Relevance:** Research boundaries
**Pattern:** Clearly define what is and isn't included in analysis
**Science Application:** Literature review scope, experimental boundaries, generalizability limits
**Supporting Role:** Prevents scope creep and clarifies claims

#### DT-04: Layered Analysis Structure
**Relevance:** Multi-scale scientific analysis
**Pattern:** Both micro-level (specific findings) and macro-level (patterns, trends) analysis
**Science Application:** Individual results + field-level trends, mechanism + systems view
**Supporting Role:** Bridges detailed findings with broader understanding

#### RT-02: Multi-Dimensional Analysis Framework
**Relevance:** Comprehensive evaluation
**Pattern:** Analyze from multiple perspectives systematically
**Science Application:** Paper evaluation (methods, results, interpretation, impact)
**Supporting Role:** Ensures thorough assessment

---

### Tier 4: Specialized Applications

#### NE-06: Self-Audit Requirements
**Relevance:** Quality checkpoints
**Pattern:** Verify output meets specific criteria before completion
**Science Application:** Methods completeness, statistical assumption checking, reporting standards
**Specialized Use:** Ensuring compliance with field-specific standards

#### RP-03: Multi-Persona Debate
**Relevance:** Considering alternative viewpoints
**Pattern:** Simulate debate between experts with different perspectives
**Science Application:** Theoretical debates, methodological controversies, interdisciplinary synthesis
**Specialized Use:** Exploring contested scientific questions

#### MP-01: Reverse Prompting
**Relevance:** Research question refinement
**Pattern:** Ask AI to generate optimal prompt for a task, then execute
**Science Application:** Refining vague research questions into testable hypotheses
**Specialized Use:** Early-stage research conceptualization

#### NE-04: Good vs Bad Example Calibration
**Relevance:** Quality standards in writing
**Pattern:** Show contrasting examples to illustrate quality gap
**Science Application:** Methods writing, result presentation, figure design
**Specialized Use:** Training and calibration for scientific communication

#### DT-01: Hierarchical Task Breakdown
**Relevance:** Research project planning
**Pattern:** Break complex tasks into phases, subtasks, dependencies
**Science Application:** Research timeline, grant workplan, thesis structure
**Specialized Use:** Large-scale research project management

---

### Tier 5: Quality Assurance for Scientific Content

#### AG-02: Skeptical Default Stance
**Relevance:** Preventing overconfident conclusions
**Pattern:** Default to skepticism, requiring strong evidence for claims
**Quality Application:** Avoiding confirmation bias, demanding rigor

#### NE-09: Scope Reduction Pressure
**Relevance:** Focused research questions
**Pattern:** Challenge, cut, and reduce scope throughout process
**Quality Application:** Refining overly broad research questions into tractable studies

#### CM-02: Constraint Specification
**Relevance:** Experimental boundaries
**Pattern:** Explicit must/must-not requirements
**Quality Application:** Defining experimental constraints, ethical boundaries

#### OC-04: Conditional Output Logic
**Relevance:** Handling null results
**Pattern:** Instructions for output when expected findings aren't present
**Quality Application:** How to interpret and report negative results

#### ED-05: Reference Class Priming
**Relevance:** Maintaining standards across analyses
**Pattern:** Show excellent example, request similar quality
**Quality Application:** Consistent quality in systematic reviews or large analyses

---

## Technique Combinations for Science

### Literature Review
```
RT-05 (Evidence-Based) + QA-05 (Citations) + DT-02 (Focus Areas) + DT-04 (Layered Analysis) + CM-03 (Scope)
```

### Experimental Design
```
RT-03 (Tree of Thoughts) + QA-02 (Stress-Test) + DS-02 (Metrics) + CM-02 (Constraints) + NE-10 (Scenarios)
```

### Hypothesis Development
```
RT-01 (Chain-of-Thought) + RT-03 (Tree of Thoughts) + QA-04 (Uncertainty) + NE-09 (Scope Reduction)
```

### Data Interpretation
```
RT-05 (Evidence-Based) + QA-01 (Verification) + QA-02 (Stress-Test) + QA-04 (Uncertainty)
```

### Grant Writing
```
ST-01 (Clear Objectives) + RT-05 (Evidence-Based) + DT-01 (Task Breakdown) + QA-01 (Verification)
```

### Peer Review
```
RT-02 (Multi-Dimensional) + QA-02 (Stress-Test) + QA-04 (Uncertainty) + NE-07 (Emotional Validation for feedback)
```

### Science Communication
```
RP-02 (Audience Framing) + RT-04 (Analogies) + QA-04 (Uncertainty) + ED-01 (Scaffolding)
```

---

## Scientific Integrity Considerations

When building science prompts, ensure:

1. **Evidence traceability** - All claims linked to sources or data
2. **Uncertainty explicit** - Confidence intervals, limitations, caveats stated
3. **Alternative explanations** - Competing hypotheses considered
4. **Reproducibility focus** - Methods described with sufficient detail
5. **Conflict of interest awareness** - Potential biases acknowledged
6. **Null results respected** - Absence of effect is also a finding
7. **Statistical rigor** - Appropriate methods with assumption checking
8. **Scope honesty** - Clear boundaries on generalizability

### Discipline-Specific Considerations

Different scientific fields have specific standards:

- **Biology/Medicine:** CONSORT, ARRIVE, PRISMA reporting guidelines
- **Psychology:** Pre-registration, effect sizes, power analysis
- **Physics/Engineering:** Uncertainty propagation, measurement standards
- **Environmental Science:** Spatial/temporal scale, confound control
- **Chemistry:** Compound characterization, purity standards
- **Social Sciences:** Reflexivity, positionality, generalizability limits

---

*Last Updated: 2025-12-09*
*Part of the Prompting Guides repository expansion into domain-specific applications*
