# Research & Academic: Comprehensive Guide

> Part of the [Non-Coding Quick Start](../NON_CODING_QUICK_START.md) system.
> This domain covers literature review, research methodology, academic writing, and scholarly analysis.

---

## When This Domain Applies

### Trigger Phrases

Route to this domain when the request mentions:

| Category | Trigger Phrases |
|----------|----------------|
| **Literature** | "literature review", "systematic review", "meta-analysis", "sources", "citations" |
| **Methodology** | "research design", "methodology", "qualitative", "quantitative", "sampling" |
| **Analysis** | "data analysis", "findings", "results interpretation", "statistical analysis" |
| **Writing** | "academic writing", "thesis", "dissertation", "journal article", "abstract" |
| **Process** | "research question", "hypothesis", "IRB", "research proposal" |

### User Personas

| Persona | Typical Needs |
|---------|--------------|
| **Graduate Students** | Thesis/dissertation support, literature reviews, methodology |
| **Academic Researchers** | Paper writing, grant proposals, study design |
| **Undergraduate Students** | Research papers, understanding sources, proper citations |
| **Independent Researchers** | Research design, data analysis, publication support |
| **Professionals** | Evidence synthesis, applied research, white papers |

### Out of Scope

- **Clinical research specifics** - Trial design, medical studies → domain-healthcare-clinical
- **Market research** - Business analysis → domain-product-management
- **Creative writing** - Fiction, essays → domain-creative-writing
- **Educational curriculum** - Teaching materials → domain-education-teaching

---

## Domain-Specific Considerations

### What Makes Research/Academic Unique

Research prompts operate in environments where:

1. **Rigor is Essential** - Claims must be supported by evidence
2. **Methodology Matters** - How you know affects what you can claim
3. **Bias Must Be Acknowledged** - Every study has limitations
4. **Citation is Required** - Attribution and traceability are non-negotiable
5. **Peer Review Standards** - Output may face expert scrutiny
6. **Field Conventions** - Each discipline has norms for writing and methods

### The Research Content Difference

| Dimension | General Writing | Academic/Research Writing |
|-----------|-----------------|---------------------------|
| **Claims** | Can be opinion | Must be evidence-supported |
| **Sources** | Optional | Required and cited |
| **Language** | Accessible | Precise, technical when needed |
| **Limitations** | Often omitted | Must be acknowledged |
| **Structure** | Flexible | Follows disciplinary conventions |
| **Audience** | General | Expert reviewers |

### Critical Success Factors

1. **Methodological Clarity** - Clear research design and justification
2. **Evidence-Based Claims** - Every assertion linked to evidence
3. **Limitation Acknowledgment** - Honest about what study can and cannot show
4. **Proper Attribution** - Sources cited accurately and completely
5. **Logical Argumentation** - Clear reasoning from evidence to conclusions
6. **Disciplinary Fit** - Follows conventions of the field
7. **Reproducibility** - Others could verify or replicate work

### Common Failure Modes

| Failure | Example | Prevention |
|---------|---------|------------|
| **Overclaiming** | "This proves that..." | Use hedged language: "suggests," "indicates" |
| **Missing limitations** | Not discussing study weaknesses | Dedicated limitations section |
| **Poor sourcing** | Claims without citations | Every factual claim needs a source |
| **Confirmation bias** | Only citing supporting evidence | Actively seek contradicting sources |
| **Methodology mismatch** | Wrong method for research question | Design review before execution |
| **Jargon overload** | Unnecessarily complex language | Clear writing is good writing |

---

## Recommended Techniques

### Core Techniques (Always Use)

| Technique | Application in Research | Example |
|-----------|------------------------|---------|
| **RT-05 Evidence-Based** | All claims linked to evidence | "According to Smith (2023)..." |
| **QA-04 Uncertainty** | Appropriate hedging and limitations | "These findings suggest..." |
| **ST-02 Sequential Steps** | Systematic research process | Literature search → synthesis → gaps |
| **DS-01 Framework** | Apply research frameworks | PICO, PRISMA, theoretical frameworks |
| **QA-02 Adversarial** | Consider alternative explanations | "Alternative interpretation..." |

### Situational Techniques

| Situation | Add Technique | Why |
|-----------|--------------|-----|
| Literature review | CM-01 Context | Define scope, inclusion criteria |
| Methodology design | RT-02 Multi-Dimensional | Consider multiple design options |
| Synthesis | RT-03 Tree of Thoughts | Map relationships between sources |
| Writing | ST-03 Output Specification | Follow disciplinary structure |
| Critique | QA-01 Self-Verification | Multiple viewpoints on findings |

---

## Quality Indicators for Research

### What "Good" Looks Like

**A high-quality research prompt output:**

1. **Evidence-Grounded**
   - Every claim has a source or is clearly labeled as author interpretation
   - Sources are current and authoritative
   - Counter-evidence is acknowledged

2. **Methodologically Sound**
   - Research design matches research question
   - Methods are explained clearly
   - Limitations are explicitly stated

3. **Properly Hedged**
   - Findings are "suggested," not "proven"
   - Generalizability is bounded
   - Alternative interpretations are noted

4. **Well-Structured**
   - Follows disciplinary conventions
   - Logical flow from question to conclusion
   - Clear organization with signposting

5. **Honest About Gaps**
   - What we don't know is as clear as what we do
   - Future research directions identified
   - Assumptions made explicit

### Academic Confidence Calibration

```markdown
## Research Claim Confidence Levels

**Strong Evidence (Can State More Directly):**
- Multiple high-quality studies with consistent findings
- Systematic reviews and meta-analyses
- Well-replicated results
- Language: "Research consistently shows...", "Strong evidence indicates..."

**Moderate Evidence (Hedge Appropriately):**
- Limited studies but quality methodology
- Some conflicting findings
- Recent work, not yet replicated
- Language: "Evidence suggests...", "Studies indicate...", "Preliminary findings show..."

**Weak Evidence (Hedge Heavily):**
- Single studies
- Methodological limitations
- Conflicting results across studies
- Language: "One study found...", "Limited evidence suggests...", "This may indicate..."

**No/Insufficient Evidence:**
- Speculation or hypothesis
- Expert opinion without empirical backing
- Language: "It is hypothesized that...", "Further research is needed to determine..."
```

### False-Positive Prevention for Research

**DON'T:**

- Present speculation as established fact
- Cherry-pick sources that support your view
- Overclaim findings ("proves" instead of "suggests")
- Ignore methodological limitations
- Assume causation from correlation
- Present p<0.05 as definitive proof
- Omit studies that contradict the narrative
- Use jargon to obscure weak arguments

**DO:**

- Distinguish between evidence and interpretation
- Present conflicting evidence when it exists
- Use appropriate hedging language
- Dedicate space to limitations
- Explain methodology clearly
- Note effect sizes, not just significance
- Include null or negative findings
- Write for clarity, not impressiveness

---

## Existing Prompts in This Repository

This domain currently provides the framework, templates, and field guide below. Individual research prompt files are not bundled here yet — apply the templates directly or consult [`field_guide.md`](field_guide.md) for technique-by-technique guidance. Related clinical-research support lives in [`domain-healthcare-clinical/`](../domain-healthcare-clinical/).

---

## Templates

### Template 1: Literature Review Framework

```markdown
# Literature Review: [Topic]

**Research Question:** [The question this review addresses]
**Scope:** [Time period, databases, inclusion criteria]

---

## Search Strategy

**Databases Searched:**
- [Database 1]
- [Database 2]

**Search Terms:**
- Primary: [terms]
- Secondary: [terms]
- Boolean combinations: [combinations used]

**Inclusion Criteria:**
- [Criterion 1]
- [Criterion 2]

**Exclusion Criteria:**
- [Criterion 1]
- [Criterion 2]

---

## Overview of Literature

**Total Sources Identified:** [Number]
**Sources Meeting Criteria:** [Number]
**Sources Included in Review:** [Number]

### Themes Identified

#### Theme 1: [Theme Name]
**Summary:** [What the literature says on this theme]

**Key Studies:**
- [Author (Year)]: [Key finding]
- [Author (Year)]: [Key finding]

**Level of Agreement:** [Consensus / Mixed / Conflicting]

**Gaps:** [What's not addressed]

[Repeat for each theme]

---

## Synthesis

### Points of Consensus
[Where literature agrees]

### Points of Disagreement
[Where literature conflicts, with possible explanations]

### Methodological Considerations
[Quality of evidence, common limitations]

### Gaps in Literature
[What research is needed]

---

## Conclusions

[What can be concluded from this body of literature]

**Confidence Level:** [Based on evidence quality]

**Limitations of This Review:**
- [Limitation 1]
- [Limitation 2]

---

## References

[Full reference list in appropriate style]
```

### Template 2: Research Proposal Outline

```markdown
# Research Proposal: [Title]

**Principal Investigator:** [Name]
**Institution:** [Affiliation]
**Date:** [Date]

---

## Abstract
[250-word summary: background, objectives, methods, significance]

---

## Introduction

### Background
[What is known about this topic]

### Problem Statement
[The gap this research addresses]

### Significance
[Why this research matters]

---

## Research Questions and Hypotheses

### Primary Research Question
[Main question]

### Hypotheses
- H1: [Hypothesis 1]
- H2: [Hypothesis 2]

---

## Literature Review

### Theoretical Framework
[Theory guiding this research]

### Key Studies
[Summary of relevant prior work]

### Gaps
[What prior work hasn't addressed]

---

## Methodology

### Research Design
[Type: experimental, correlational, qualitative, mixed methods]
[Justification for this design]

### Participants/Sample
- Population: [Who]
- Sampling method: [How selected]
- Sample size: [N and justification/power analysis]
- Inclusion criteria: [Requirements]
- Exclusion criteria: [Disqualifiers]

### Measures/Instruments
- [Measure 1]: [Description, reliability, validity]
- [Measure 2]: [Description, reliability, validity]

### Procedures
1. [Step 1]
2. [Step 2]
3. [Step 3]

### Data Analysis Plan
- [Analysis for RQ1]
- [Analysis for RQ2]

### Ethical Considerations
- IRB status: [Pending/approved]
- Consent process: [Description]
- Risk mitigation: [How risks are addressed]

---

## Timeline

| Phase | Activities | Duration |
|-------|------------|----------|
| [Phase 1] | [Activities] | [Months] |

---

## Budget

| Category | Amount | Justification |
|----------|--------|---------------|
| [Category] | [$] | [Why needed] |

---

## Limitations

[Anticipated limitations and how addressed]

---

## References

[Full reference list]
```

### Template 3: Academic Paper Structure

```markdown
# [Paper Title]

**Authors:** [Names and affiliations]

---

## Abstract
[Structured or unstructured per journal guidelines]
- Background: [1-2 sentences]
- Objective: [1 sentence]
- Methods: [2-3 sentences]
- Results: [2-3 sentences]
- Conclusions: [1-2 sentences]

**Keywords:** [3-5 keywords]

---

## Introduction

### Background
[What is known - broad to narrow funnel]

### Problem/Gap
[What is not known or needs investigation]

### Objective
[What this paper does]

### Contribution
[How this advances the field]

---

## Literature Review / Theoretical Background
[Organize thematically or chronologically as appropriate]

---

## Methods

### Study Design
[Design and justification]

### Participants/Sample
[Who, how recruited, N]

### Measures
[What was measured and how]

### Procedure
[Step-by-step what happened]

### Analysis
[How data was analyzed]

---

## Results

### Descriptive Statistics
[Sample characteristics, means, SDs]

### Primary Findings
[Main results addressing research questions]

### Secondary Findings
[Additional findings of interest]

[Tables and figures as appropriate]

---

## Discussion

### Summary of Findings
[Brief restatement of key results]

### Interpretation
[What findings mean in context of prior research]

### Theoretical Implications
[How this advances theory]

### Practical Implications
[Real-world applications]

### Limitations
[Study weaknesses honestly stated]

### Future Directions
[What research should come next]

---

## Conclusion
[Brief summary of contribution and significance]

---

## References
[In appropriate citation style]

---

## Appendices
[Supplementary materials]
```

---

## Worked Example

### Scenario: Literature Review Assistance

**User says:** "I need to write a literature review on the effectiveness of gamification in employee training for my Master's thesis."

**Step 1: Classification**

- Task Type: CREATE (with LEARN elements)
- Domain: Research/Academic
- Specific Type: Literature review assistance

**Step 2: Context Gathering**

**Need to determine:**
- Scope (what aspects of gamification? what types of training?)
- Field (education? organizational psychology? HCI?)
- Prior searching (what have they found already?)
- Length/depth expected
- Citation style required
- Deadline

**Step 3: Build Research-Appropriate Prompt**

```markdown
# Literature Review Assistance: Gamification in Employee Training

**Objective:** Support development of a Master's thesis literature review

## Research Context

**Topic:** Effectiveness of gamification in employee training
**Field:** [Organizational psychology / HCI / Educational technology]
**Thesis Focus:** [What specific question is the thesis addressing?]

## Scope Definition

**Temporal Scope:** [What years? Last 10 years? Since gamification became prominent?]

**Conceptual Scope:**
- What counts as "gamification"? [Points, badges, leaderboards? Serious games? Game-based learning?]
- What types of "employee training"? [Onboarding? Compliance? Skills development? All?]
- What "effectiveness" measures? [Learning outcomes? Engagement? Transfer? Retention?]

**Exclusion Boundaries:**
- What's explicitly out of scope? [K-12 education? Health apps?]

## Search Strategy Guidance

**Suggested Databases:**
- Academic: Web of Science, Scopus, PsycINFO, ERIC
- Applied: Google Scholar (for grey literature)
- Specialized: ACM Digital Library (if HCI focus)

**Suggested Search Terms:**
- Primary: gamification AND (employee training OR workplace learning OR corporate training)
- Expand: game-based learning, serious games, game mechanics, game elements
- Outcome terms: effectiveness, learning outcomes, engagement, motivation, transfer

**Boolean Search Example:**
```
(gamification OR "game-based learning" OR "serious games" OR "game elements")
AND
(employee* OR workplace OR corporate OR organizational)
AND
(training OR learning OR development)
```

## Synthesis Framework

**Organize by:**
1. **Type of gamification element** (points, badges, narratives, etc.)
2. **Type of training outcome** (knowledge, skills, attitudes, behavior)
3. **Theoretical frameworks used** (self-determination theory, flow theory, etc.)
4. **Methodological quality** (RCTs, quasi-experimental, case studies)

**Key Questions for Each Source:**
- What gamification elements were used?
- What was the training context?
- What outcomes were measured?
- What was the effect size?
- What were the limitations?
- What theoretical framework was applied?

## Evidence Quality Assessment

**Rate each study on:**
- Methodological rigor (1-5)
- Sample quality (1-5)
- Outcome measure validity (1-5)
- Applicability to your context (1-5)

**Quality Categories:**
- Strong: RCTs, quasi-experimental with control
- Moderate: Pre-post without control, well-designed surveys
- Weak: Case studies, anecdotal reports

## Expected Outputs

**Deliverable Structure:**
1. Introduction (scope, rationale, organization)
2. Theoretical frameworks section
3. Thematic synthesis (by gamification element or by outcome)
4. Methodological critique section
5. Identified gaps
6. Conclusion (summary, implications for your study)

**Tables to Include:**
- Summary table of included studies
- Comparison of findings by gamification type
- Quality assessment summary

## Avoiding Common Pitfalls

**Don't:**
- Include every study found (be selective based on relevance and quality)
- Summarize each study in isolation (synthesize across studies)
- Ignore contradictory findings (address them explicitly)
- Overclaim consensus where none exists
- Forget to connect to YOUR study's contribution

**Do:**
- Group studies thematically
- Note patterns and contradictions
- Assess evidence quality throughout
- Identify specific gaps your thesis addresses
- Use your own analytical voice to interpret
```

---

## Anti-Patterns for Research

### Mistake 1: Overclaiming Findings

**Problem:** Using too-strong language for the evidence

**Bad:**
```
"This study proves that gamification increases learning outcomes."
```

**Good:**
```
"This study found a significant positive effect of gamification on learning outcomes (d = 0.45, p < .01), though the single-site design limits generalizability."
```

---

### Mistake 2: Cherry-Picking Sources

**Problem:** Only citing evidence that supports the desired conclusion

**Bad:**
```
Literature review that only includes positive findings on gamification
```

**Good:**
```
"While most studies report positive effects (Smith, 2020; Jones, 2021), some found null results (Brown, 2019) or even negative effects under certain conditions (Davis, 2022). These contradictory findings may be explained by..."
```

---

### Mistake 3: Missing Limitations

**Problem:** Presenting findings without acknowledging study weaknesses

**Bad:**
```
"This study demonstrates that X causes Y."
(No limitations section)
```

**Good:**
```
"This study has several limitations. First, the sample was limited to one organization, limiting generalizability. Second, the outcome measure was self-reported, which may be subject to social desirability bias. Third, the follow-up period was only 30 days, so long-term effects are unknown."
```

---

## Quick Reference Card

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                RESEARCH/ACADEMIC QUICK REFERENCE                           ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║  EVIDENCE LANGUAGE:                                                       ║
║  ✗ "proves" → ✓ "suggests," "indicates," "demonstrates"                  ║
║  ✗ "definitely" → ✓ "likely," "appears to"                               ║
║  ✗ "all studies show" → ✓ "most studies suggest," "evidence indicates"   ║
║                                                                           ║
║  EVERY SOURCE CITATION NEEDS:                                             ║
║  □ Author(s) and year                                                     ║
║  □ Key finding summarized                                                 ║
║  □ Methodology noted (especially limitations)                            ║
║  □ Relevance to your argument                                            ║
║                                                                           ║
║  LITERATURE REVIEW STRUCTURE:                                             ║
║  1. Define scope and search strategy                                      ║
║  2. Organize thematically (not source-by-source)                         ║
║  3. Synthesize: find patterns, contradictions, gaps                      ║
║  4. Assess evidence quality throughout                                    ║
║  5. Conclude with implications for your research                         ║
║                                                                           ║
║  LIMITATIONS SECTION MUST ADDRESS:                                        ║
║  □ Sample limitations (size, representativeness)                         ║
║  □ Measurement limitations (validity, reliability)                       ║
║  □ Design limitations (causality claims, controls)                       ║
║  □ Generalizability limitations (context-specific)                       ║
║                                                                           ║
║  METHODOLOGY MUST SPECIFY:                                                ║
║  □ Research design and justification                                      ║
║  □ Sample and sampling method                                            ║
║  □ Measures with psychometric properties                                 ║
║  □ Procedures step-by-step                                               ║
║  □ Analysis plan                                                          ║
║                                                                           ║
║  RELATED RESOURCES:                                                       ║
║  • field_guide.md (prompt techniques for researchers)                    ║
║  • domain-healthcare-clinical/ (clinical research support)               ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## Field Guide

For comprehensive prompt engineering techniques specifically tailored to science and research:

| Field Guide | Purpose |
|-------------|---------|
| [`field_guide.md`](field_guide.md) | Detailed guide on prompt techniques for scientists, researchers, and academics |

---

## Related Resources

| Resource | Purpose |
|----------|---------|
| [NON_CODING_QUICK_START.md](../NON_CODING_QUICK_START.md) | Universal non-coding principles |
| [field_guide.md](field_guide.md) | Prompt techniques for researchers and academics |
| [domain-healthcare-clinical/](../domain-healthcare-clinical/) | Clinical research support |
| [PROMPT_QUALITY_STANDARDS.md](../PROMPT_QUALITY_STANDARDS.md) | Quality tier definitions |

---

*Document Version: 1.1*
*Created: 2026-01-26*
*Updated: 2026-01-28 - Added Science & Research Field Guide*
*Domain: Research & Academic*
