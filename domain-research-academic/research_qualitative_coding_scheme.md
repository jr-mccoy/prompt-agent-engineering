---
title: "Qualitative Coding Scheme — Inductive + Deductive Codebook with Reliability Plan"
category: research-academic/qualitative
description: "Build a codebook for qualitative data analysis combining deductive (top-down from theory) and inductive (bottom-up from data) codes. Specifies code structure (definition, inclusion/exclusion criteria, exemplar quote), inter-rater reliability plan, code-tree organization, and memo-writing guidance."
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
  - qualitative
  - coding
  - codebook
  - thematic-analysis
  - reliability
updated: "2026-05-10"
reasoning:
  styles: [systematic, qualitative, iterative]
  stakes: variable
  horizon: weeks
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: variable
  collaboration: solo_or_pair
  output_format: codebook_plus_process
  user_role: [researcher, ux_researcher, ethnographer, policy]
  mode: [design, synthesize]
related_prompts:
  - domain-research-academic/research_interview_guide_designer.md
  - domain-business-strategy/research/user_research_synthesis.md
  - domain-research-academic/research_secondary_source_synthesis.md
---

# Qualitative Coding Scheme

**Objective:** Build a codebook for analyzing qualitative data (interviews, open-ends, field notes, documents). Combine **deductive codes** (top-down from theory or research question) with **inductive codes** (bottom-up from the data itself). Specify code structure, inter-rater reliability process, code-tree organization, and memo-writing guidance. Output a codebook a second analyst could apply with reasonable agreement.

**When to use:**
- Analyzing qualitative data from interviews, open-ended survey responses, ethnographic field notes, document corpora.
- Multiple analysts will code the same data and need shared specification.
- Audit-grade qualitative analysis where coding decisions need to be defensible.

**When NOT to use:**
- Single quick read-through of small data (overkill).
- Quantitative content analysis where code-counts are the deliverable (this prompt focuses on theme development).

**Audience:** Qualitative researchers, UX researchers, ethnographers, policy researchers.

---

## Inputs / Context

1. **Research question.**
2. **Data type and corpus size** (e.g., 20 hour-long interviews, 200 open-ends, 50 documents).
3. **Theoretical framework** if any (drives deductive codes).
4. **Number of analysts.** Single-analyst coding is acceptable but lacks reliability check.
5. **Software** (NVivo, Atlas.ti, MAXQDA, Dedoose, manual / spreadsheet).
6. **Output deliverable** (paper, report, deck).

---

## Constraints

### Must
- Distinguish **deductive** (pre-specified) from **inductive** (data-emergent) codes.
- For each code: **name**, **definition** (1–2 sentences), **inclusion criteria** (when this code applies), **exclusion criteria** (when it doesn't), **exemplar quote** from the data.
- Organize codes into a **tree** with parent / child relationships where conceptually warranted.
- Plan **inter-rater reliability** (when 2+ analysts): subset of data double-coded, agreement metric (Cohen's kappa, Krippendorff's alpha, or percent agreement with discussion), threshold (typically κ > 0.6 acceptable, > 0.8 strong).
- Plan **memo-writing** alongside coding — observations, hypotheses, surprises, code-revision notes.
- Plan for **codebook iteration**: codes added, merged, split, or retired as analysis proceeds; document changes.
- Saturate before stopping: code until new codes stop emerging.

### Must Not
- Lock the codebook before coding begins (deductive-only). Pure deductive coding misses what the data has to say.
- Code without definitions. Undefined codes drift across passes and analysts.
- Skip exemplar quotes. Without them, code application becomes idiosyncratic.
- Treat reliability as a one-shot check; iterate until agreement is reached.
- Confuse code application with interpretation. Codes tag content; themes interpret patterns.

---

## Instructions

### Step 1 — Deductive code generation
From research question and any theoretical framework, generate 5–15 deductive codes. Each gets the standard structure (name, definition, inclusion, exclusion, planned exemplar — to be filled when found).

### Step 2 — Open coding pass on subsample
Take 2–4 transcripts / documents (10–20% of corpus). Code line-by-line, tagging anything that seems meaningful. Capture inductive codes as they emerge. Keep memo: what surprised you, what categories formed.

### Step 3 — First-draft codebook
Combine deductive + inductive codes. Group related codes into parent-child tree. Define each code with full structure.

### Step 4 — Second pass on subsample
Re-code the same subsample with the first-draft codebook. Note: codes that don't apply anywhere (consider retiring), codes that apply to too much (consider splitting), content that has no code (consider new code).

### Step 5 — Inter-rater reliability (if 2+ analysts)
- Both analysts code 10–20% of corpus independently using the codebook.
- Compute agreement metric.
- Discuss disagreements; revise codebook if disagreement reveals definition ambiguity.
- Re-test on additional subset until threshold reached.
- Document the agreement reached and the revisions made.

### Step 6 — Apply to full corpus
Code remaining data. Capture memos throughout: pattern hypotheses, surprises, edge cases, code revisions needed.

### Step 7 — Saturation check
Have you stopped finding new codes / new variants of existing codes in recent transcripts? If yes, saturated. If new codes still emerging, continue or expand sample.

### Step 8 — Theme development
Codes ≠ themes. Themes are interpretations of patterns across codes. After coding complete:
- Identify which codes co-occur
- Identify which codes have variants by participant subgroup
- Build themes that explain *why* these patterns exist
- Test themes against negative cases

### Step 9 — Codebook revision log
Throughout: log every code added, merged, split, retired, with date and reason. The log makes the analytic process auditable.

### Step 10 — Final codebook delivery
Cleaned codebook with: tree structure, full code definitions, exemplar quotes from corpus, frequency / distribution if relevant, themes built from codes.

---

## False-Positive Prevention

1. **Pure-deductive lock-in.** Misses data-emergent insight.
2. **Pure-inductive sprawl.** Without theoretical grounding, codes can multiply uselessly. Anchor inductive codes in the research question.
3. **Definition drift.** Codes applied differently across passes; symptom of weak definitions or analyst fatigue.
4. **Reliability as ceremony.** Computing kappa once and ignoring patterns of disagreement misses revision opportunities.
5. **Code-as-theme conflation.** Codes tag; themes interpret. Both are needed; neither substitutes for the other.
6. **Saturation theater.** Stopping early because of time pressure when new codes are still emerging.
7. **No memo trail.** Without memos, the analytic reasoning becomes unrecoverable.
8. **Negative case neglect.** Themes that ignore disconfirming cases are weak.

---

## Output Format

```
# Qualitative codebook — [research question]

## Corpus
- Type: [...]
- Size: [...]
- Sampling: [...]

## Theoretical anchor (if any)
- Framework: [...]
- Deductive codes derived: [...]

## Codebook (tree)
### [Parent code 1]
- Definition: [...]
- Inclusion: [...]
- Exclusion: [...]
- Exemplar: "[verbatim from corpus]" (Source ID)

#### [Child code 1.1]
- Definition: [...]
- Inclusion: [...]
- Exclusion: [...]
- Exemplar: [...]

### [Parent code 2]
[Same structure]

[Full tree]

## Code provenance
| Code | Origin (deductive / inductive) | First seen in (source) |
|------|-------------------------------|-------------------------|
| [...]| inductive                     | T07                     |
| [...]| deductive                     | from framework          |

## Inter-rater reliability (if 2+ analysts)
- Method: [Cohen's κ / Krippendorff α / % agreement + discussion]
- Subset coded: [N or %]
- Initial agreement: [...]
- Revisions made: [...]
- Final agreement: [...]
- Threshold met: [yes / no]

## Saturation
- Reached at: [N transcripts / documents]
- Evidence: [no new codes in last K sources]

## Themes (interpretations of code patterns)
### Theme 1: [...]
- Codes contributing: [...]
- Pattern: [...]
- Negative cases checked: [...]

### Theme 2: [...]
[...]

## Memo highlights
- [...]
- [...]

## Revision log
| Date | Change | Reason |
|------|--------|--------|
| [...]| [...]  | [...]  |
```

---

## Verification

- [ ] Deductive and inductive codes both present and labeled.
- [ ] Each code has definition, inclusion, exclusion, exemplar.
- [ ] Code tree organized.
- [ ] Inter-rater reliability done (if multi-analyst), with iteration to threshold.
- [ ] Memos captured throughout.
- [ ] Saturation reached or expansion plan in place.
- [ ] Themes distinguished from codes.
- [ ] Negative cases tested against themes.
- [ ] Revision log maintained.
