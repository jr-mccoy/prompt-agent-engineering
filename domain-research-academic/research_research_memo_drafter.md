---
title: "Research Memo Drafter — Question / Method / Findings / Interpretation / Limits"
category: research-academic/communication
description: "Convert raw research findings into a structured memo for an audience. Sections: question, method, findings, interpretation, limitations, next steps. Discipline: separate findings from interpretation, attribute every claim, calibrate confidence, distinguish what to include vs append. For communicating research output, not for making decisions."
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
  - research-communication
  - memo
  - findings
  - attribution
  - calibrated
updated: "2026-05-10"
reasoning:
  styles: [structured, attributional, communication]
  stakes: variable
  horizon: hours_to_days
  uncertainty: variable
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo_or_pair
  output_format: structured_memo
  user_role: [researcher, analyst, ux_researcher, journalist, consultant]
  mode: [synthesize, document]
related_prompts:
  - domain-research-academic/research_secondary_source_synthesis.md
  - domain-decision-making/documentation/decisiondoc_options_memo.md
  - domain-business-strategy/research/user_research_synthesis.md
---

# Research Memo Drafter

**Objective:** Convert raw research findings into a structured memo for an audience. Distinct from `decisiondoc_options_memo.md` (which is for decisions): this prompt is for *communicating research output* — what was asked, how it was answered, what was found, what it means, what's uncertain. Discipline: separate findings from interpretation, attribute every claim, calibrate confidence, distinguish core memo content from appendix.

**When to use:**
- Research is complete or substantially complete and needs to be communicated.
- Sponsor / client / stakeholders need a digestible summary of findings.
- Internal team is shipping a research report.
- Pre-publication draft for academic / industry papers.

**When NOT to use:**
- Decision-shaped output (use options memo).
- Real-time updates during ongoing research (use shorter status update format).
- Interactive presentations (memo is for reading).

**Audience:** Researchers, UX researchers, analysts, journalists, consultants producing research deliverables.

---

## Inputs / Context

1. **Research question.**
2. **Method summary.**
3. **Findings** (raw or partially organized).
4. **Audience.**
5. **Length budget** (one-pager? 5 pages? 20 pages?).
6. **Decision or action this informs** (if any).

---

## Constraints

### Must
- Lead with the **question** and the **answer** (top-line finding) — readers should know within 30 seconds.
- **Separate findings from interpretation.** Findings are what the data shows; interpretation is what it means. Mark each clearly.
- **Attribute every claim** to evidence (data point, source, observation count). No floating "research suggests".
- **Calibrate confidence** per finding: high / moderate / low / preliminary.
- Section limitations **honestly** and prominently — not in a footnote.
- Distinguish **core memo content** (must read) from **appendix** (reference / detail).
- End with **next steps**: what this enables, what's still unknown, what would be highest-leverage to study next.

### Must Not
- Bury the headline finding.
- Smuggle interpretation into findings ("the data shows X is bad" — "bad" is interpretation).
- Stack findings without confidence calibration.
- Limit limitations to a brief disclaimer.
- Include all the analysis in main body — push detail to appendix.

---

## Instructions

### Step 1 — Top-line block
- Question (one sentence)
- Top-line finding (one sentence)
- Confidence (high / moderate / low / preliminary)
- One-sentence implication (what this means for the audience's decision / understanding / action)

### Step 2 — Question and method
- Restate question with operationalization.
- Method summary: design, data, sample, analysis approach. 1–3 paragraphs; detailed methodology to appendix.

### Step 3 — Findings
For each finding:
- **Statement:** what was found (descriptive, not interpretive)
- **Evidence:** what data point / source / pattern supports it
- **Confidence:** high / moderate / low / preliminary
- **Caveat:** what conditions limit the finding

Group findings by theme, not by data source. Order by importance to the audience.

### Step 4 — Interpretation
Separate section. For each finding (or clusters):
- What it means in the audience's domain
- How it connects to prior knowledge / theory / practice
- What it implies — but flag inference vs evidence

### Step 5 — Limitations
Honest treatment:
- Method limitations (sample, design, measurement)
- Scope limitations (what wasn't studied)
- Inference limitations (what conclusions don't follow even from what was found)
- Generalizability bounds

### Step 6 — Next steps
- What this research enables
- What's still unknown
- Highest-leverage next study / question
- Recommended timeline / resources if user is the next-step decision-maker

### Step 7 — Appendix
- Detailed methodology
- Data tables
- Coding schemes / instruments
- Source list / participant list (anonymized)
- Analytic process notes

### Step 8 — Audience adaptation
Adjust language, length, and depth for audience. Same memo content can have different surface forms for technical vs lay audiences; the underlying findings and confidence don't change.

---

## False-Positive Prevention

1. **Buried headline.** Make readers wait → they'll miss the point. Lead.
2. **Findings-interpretation conflation.** "The intervention worked" is interpretation. "70% of users completed task X (vs 40% baseline)" is finding.
3. **Floating attribution.** "Research suggests" without specifying which study / data point.
4. **Confidence inflation.** Marking everything "high confidence" weakens the signal. Reserve high for genuine high.
5. **Limitations as disclaimer.** Brief disclaimer doesn't honor the limits; section them honestly.
6. **Appendix-as-main.** If main body is 30 pages, appendix has been confused with body.
7. **No next steps.** Research without forward-looking section dies on arrival.
8. **Audience misfit.** Technical jargon for non-technical audience, or oversimplification for technical one.

---

## Output Format

```
# Research memo — [research question]

**To:** [audience]
**From:** [author]
**Date:** [yyyy-mm-dd]

## Top-line
- **Question:** [one sentence]
- **Finding:** [one sentence]
- **Confidence:** [high / moderate / low / preliminary]
- **Implication:** [one sentence]

## Question and method
[Question restated; method summary in 1–3 paragraphs]

## Findings

### Finding 1: [name]
- **What:** [descriptive]
- **Evidence:** [data / source / observation]
- **Confidence:** [...]
- **Caveat:** [...]

### Finding 2: [name]
[Same structure]

[etc.]

## Interpretation
[What findings mean, how they connect, what they imply — flagged as inference]

## Limitations
- Method: [...]
- Scope: [...]
- Inference: [...]
- Generalizability: [...]

## Next steps
- This research enables: [...]
- Still unknown: [...]
- Highest-leverage next study: [...]
- If pursued: [timeline / resources]

## Appendix
- A. Detailed methodology
- B. Data tables
- C. Instruments / coding schemes
- D. Source / participant list
- E. Process notes
```

---

## Verification

- [ ] Top-line block present and readable in 30 seconds.
- [ ] Findings separated from interpretation.
- [ ] Every finding attributed to evidence.
- [ ] Confidence calibrated per finding.
- [ ] Limitations honest and prominent.
- [ ] Next steps explicit.
- [ ] Appendix carries the heavy detail; main body lean.
- [ ] Audience-adapted language.
- [ ] No floating "research suggests".
- [ ] No buried headline.
