---
title: "Literature Review Plan — Scope, Search Strategy, Synthesis Approach"
category: research-academic/literature-review
description: "Plan a literature review before opening a single paper. Defines the question being reviewed, scope (inclusion/exclusion criteria), search strategy across databases and source types, screening approach, extraction template, and synthesis method (narrative / thematic / systematic / meta-analytic). Prevents the most common failure mode: drowning in sources without a frame."
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
  - literature-review
  - search-strategy
  - synthesis
  - prisma
updated: "2026-05-10"
reasoning:
  styles: [systematic, decomposition, planning]
  stakes: variable
  horizon: weeks_to_months
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo_or_pair
  output_format: review_protocol
  user_role: [researcher, student, analyst, policy, founder, journalist]
  mode: [synthesize, audit]
related_prompts:
  - domain-research-academic/research_question_formulation.md
  - domain-research-academic/research_evidence_map.md
  - domain-research-academic/research_secondary_source_synthesis.md
---

# Literature Review Plan

**Objective:** Plan a literature review before opening a single paper. Define the question being reviewed, the scope (what's included, what's excluded), the search strategy (databases, search terms, source types, time window), the screening process, the extraction template, and the synthesis method. Output a review protocol the user can execute and a peer can audit.

The most common failure mode in literature reviews is starting with reading and ending with an unsynthesizable pile of sources. Planning prevents this.

**When to use:**
- Beginning any structured literature review (academic, policy, market, technical, due-diligence).
- A literature search has already started and is sprawling — replan before continuing.
- Preparing a systematic review or meta-analysis (use this prompt as the front end of a PRISMA-style protocol).
- Evaluating an existing literature review for completeness and quality.

**When NOT to use:**
- A quick "what does the field say about X" check that doesn't need defensible coverage. Use a lighter tool.
- The literature is so small (<10 sources) that a plan is overhead.
- The user is doing primary research, not synthesis. Different prompt needed.

**Audience:** Academic researchers, graduate students, policy analysts, journalists, due-diligence analysts, anyone whose deliverable depends on defensible coverage of prior work.

---

## Inputs / Context

1. **The review question.** Sharply stated (run `research_question_formulation.md` first if needed). May be descriptive ("what is known about X") or evaluative ("what does the evidence say about whether X works").
2. **Purpose.** Why the review exists — to inform a decision, write a paper, scope a project, build a position, support a policy proposal.
3. **Audience.** Who will read or act on the review.
4. **Resources.** Time available, access to databases, language constraints, software (reference manager, screening tool).
5. **Required defensibility.** Some reviews need to be auditable (systematic / PRISMA-grade); others can be selective. Be honest about which.

---

## Constraints

### Must
- State the **review question** at the top, separate from the topic.
- Specify **inclusion and exclusion criteria** before searching, not after.
- Define a **search strategy**: databases / sources, search terms (Boolean), date range, languages, document types (peer-reviewed, grey literature, preprints, books, reports).
- Specify a **screening process**: title/abstract screen → full-text screen → final inclusion. Note who screens and how disagreements are handled.
- Define an **extraction template**: what fields will be extracted from each included source (year, authors, design, sample, key findings, evidence quality, relevance to review question).
- Choose a **synthesis method** explicitly: narrative, thematic, framework analysis, systematic, meta-analytic. The choice depends on question type and evidence heterogeneity.
- Identify **evidence quality criteria** appropriate to the source types (e.g., risk-of-bias tools for clinical, transparency standards for empirical social science, methodology checks for technical reports).
- Plan for **transparency**: how the search will be documented so a peer could re-run it.

### Must Not
- Start searching before the protocol is written.
- Assume "I'll know it when I see it" inclusion criteria — the criteria are part of the protocol.
- Conflate the review question with the underlying empirical question. The review asks "what does the literature say about X"; that's different from asking "is X true."
- Choose synthesis method based on convenience rather than question type.
- Skip grey literature in domains where it carries the field (policy, technical, industry).

---

## Instructions

### Step 1 — Restate the review question
One sentence. Distinguish from the underlying empirical question (e.g., empirical: "does intervention X work?"; review: "what does the published and grey literature say about whether intervention X works, and how confidently?").

### Step 2 — Type and purpose
- Type: descriptive / evaluative / methodological / theoretical
- Purpose: decision support / publication / scoping / due diligence / position
- Required defensibility: high (systematic) / medium (structured) / low (selective)

### Step 3 — Inclusion / exclusion criteria
- **Population / phenomenon:** what cases qualify?
- **Intervention / exposure / variable:** what is the focus?
- **Comparison:** what's being compared (if applicable)?
- **Outcome:** what outcomes count?
- **Study design:** what designs are included (RCT, observational, qualitative, theoretical, etc.)?
- **Time window:** publication dates included.
- **Language:** which languages.
- **Geography:** which regions.
- **Other inclusion / exclusion:** field-specific rules.

State each criterion as a binary test against which a candidate source can be evaluated.

### Step 4 — Search strategy
- **Databases / sources:** name them (e.g., PubMed, Scopus, Google Scholar, JSTOR, SSRN, arXiv, GAO, Cochrane, OECD, internal corpus, industry reports, government databases).
- **Search terms:** Boolean strings for each database. Include synonyms, MeSH terms, abbreviations, and field-specific terminology.
- **Backward / forward citation tracking:** which seed papers will be used and how citations will be followed.
- **Grey literature:** which sources (organizational reports, working papers, dissertations, preprints, conference proceedings, government documents).
- **Hand-search:** which journals or sources will be hand-searched.
- **Search date:** when the search will be conducted (literature reviews are time-stamped).

### Step 5 — Screening
- **Title/abstract screen:** what fraction of candidates expected; binary inclusion at this stage.
- **Full-text screen:** criteria applied at this stage.
- **Reviewer count:** single, dual independent, or one reviewer with adjudication of edge cases.
- **Disagreement resolution:** how disagreements between reviewers are settled.
- **Logging:** record of inclusion/exclusion decisions with reasons (PRISMA flow diagram).

### Step 6 — Extraction template
For each included source, record:
- Bibliographic info
- Year
- Authors / affiliation
- Country / setting
- Design / method
- Sample / population
- Intervention / exposure (if applicable)
- Outcome measures
- Key findings
- Effect size / direction (if applicable)
- Evidence quality (per applicable rubric)
- Relevance to review question (high / medium / low with note)
- Disclosed conflicts / funding (where relevant)

### Step 7 — Quality assessment
- Tool to use (Cochrane RoB 2, ROBINS-I, AMSTAR for reviews of reviews, CASP for qualitative, custom rubric for non-clinical).
- How quality affects synthesis weighting (excluded, sensitivity-analyzed, qualitatively flagged).

### Step 8 — Synthesis method
- **Narrative synthesis:** appropriate for heterogeneous designs and small N; synthesizes via thematic argument.
- **Thematic synthesis:** identify themes across sources; common in qualitative reviews.
- **Framework analysis:** use a pre-specified framework to organize findings.
- **Systematic review:** structured method with risk-of-bias assessment, may include meta-analysis if data permit.
- **Meta-analysis:** quantitative pooling; requires comparable outcome measures and effect-size data.
- **Realist synthesis:** for complex interventions; asks what works for whom under what conditions.

Choose explicitly. Justify the choice based on question type and expected evidence heterogeneity.

### Step 9 — Reporting
- Where the review will be reported (paper, memo, internal doc).
- PRISMA-style flow diagram included? (Almost always yes for systematic; advisable for others.)
- Search strategy documented enough that a peer could re-run? (Always yes.)
- Limitations section planned? (Always yes.)

### Step 10 — Risks and mitigations
- Risk of insufficient sources: [mitigation]
- Risk of overwhelming sources: [mitigation: tighten criteria, smaller scope, narrower question]
- Risk of bias from missing source types: [mitigation: grey literature, hand-search]
- Risk of out-of-date by completion: [mitigation: search update before finalizing]
- Risk of single-reviewer bias: [mitigation: independent screen of subsample]

---

## False-Positive Prevention

1. **Search-before-protocol.** Starting to read papers before the protocol is written; the resulting review will have no defensible scope.
2. **Inclusion drift.** Modifying inclusion criteria during screening to fit what's been found. Either modify deliberately and document, or hold the line.
3. **Database mono-culture.** Searching only one database introduces source bias; combine 2–4 databases plus grey literature.
4. **Synthesis-method mismatch.** Doing meta-analysis on heterogeneous designs; doing narrative synthesis when meta-analysis was possible. Match method to data.
5. **Quality assessment as gatekeeping theater.** Doing risk-of-bias scoring without using it in the synthesis is decoration.
6. **Grey-literature blindness.** In policy, technical, and industry domains, the most relevant sources are often grey. Including only peer-reviewed work is incomplete.
7. **Forgotten time-stamping.** A literature review without a search date is unreproducible.
8. **Underspecified screening.** "We screened the results" without a flow diagram is opaque. Flow is always documentable.

---

## Output Format

```
# Literature review protocol — [topic]

## Review question
> [Sharply stated, distinct from underlying empirical question]

## Type / purpose / defensibility
- Type: [...]
- Purpose: [...]
- Defensibility: [systematic / structured / selective]

## Inclusion criteria
| Dimension       | Criterion                                  |
|-----------------|--------------------------------------------|
| Population      | [...]                                      |
| Intervention    | [...]                                      |
| Comparison      | [...]                                      |
| Outcome         | [...]                                      |
| Study design    | [...]                                      |
| Time window     | [...]                                      |
| Language        | [...]                                      |
| Geography       | [...]                                      |
| Other           | [...]                                      |

## Exclusion criteria
- [bullet list]

## Search strategy
| Database / source     | Search string (Boolean)                                  | Date range |
|-----------------------|----------------------------------------------------------|------------|
| [PubMed]              | (X OR Y) AND (Z OR W) NOT (...)                          | [yyyy–yyyy]|
| [Scopus]              | …                                                        |            |
| …                     |                                                          |            |

- Grey literature sources: [...]
- Hand-search journals: [...]
- Backward / forward citation tracking: [seed papers, depth]
- Search date: [planned date]

## Screening
- Title / abstract screen: [reviewer setup]
- Full-text screen: [reviewer setup]
- Disagreement resolution: [process]
- PRISMA flow diagram: [yes / no]

## Extraction template
[Fields listed]

## Quality assessment
- Tool: [...]
- Use of quality scores in synthesis: [excluded / weighted / flagged]

## Synthesis method
- Method: [narrative / thematic / framework / systematic / meta-analysis / realist]
- Justification: [why this method given question type and evidence heterogeneity]
- If meta-analysis: pooling approach, heterogeneity test, sensitivity analysis

## Reporting
- Output: [paper / memo / internal doc]
- PRISMA flow: [included / not]
- Search strategy documentation: [reproducible]
- Limitations section: [included]

## Risks and mitigations
| Risk                     | Mitigation                |
|--------------------------|---------------------------|
| [risk]                   | [mitigation]              |
| …                        |                           |

## Timeline
- Protocol finalized: [date]
- Search complete: [date]
- Screening complete: [date]
- Extraction complete: [date]
- Synthesis complete: [date]
- Final review: [date]
```

---

## Verification

- [ ] Review question stated and distinguished from underlying empirical question.
- [ ] Inclusion / exclusion criteria are binary-testable.
- [ ] Search strategy includes 2+ databases, grey literature where appropriate, backward/forward citation tracking.
- [ ] Search terms include synonyms, abbreviations, field-specific terminology.
- [ ] Screening process includes reviewer setup and disagreement resolution.
- [ ] Extraction template enumerates all fields.
- [ ] Quality assessment tool named and its use in synthesis specified.
- [ ] Synthesis method matched to question type and evidence heterogeneity.
- [ ] Reporting includes PRISMA flow (or justified omission) and search documentation.
- [ ] Risks and mitigations are specific.
- [ ] Search date stamped.
- [ ] No "I'll know it when I see it" criteria.
