---
title: "Search Strategy Designer — Boolean Strings, Database Selection, Coverage Tradeoffs"
category: research-academic/search-strategy
description: "Design a defensible search strategy for a literature, evidence, or intelligence-gathering task. Specifies databases and source types, builds Boolean strings per database with synonyms and field-specific terminology, plans grey literature, and documents the recall-vs-precision tradeoff. Output is a search protocol a peer can re-run."
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
  - search-strategy
  - boolean
  - databases
  - literature-review
updated: "2026-05-10"
reasoning:
  styles: [systematic, taxonomic, planning]
  stakes: variable
  horizon: hours_to_days
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo_or_pair
  output_format: search_protocol
  user_role: [researcher, analyst, journalist, student, policy]
  mode: [synthesize, document]
related_prompts:
  - domain-research-academic/research_literature_review_plan.md
  - domain-research-academic/research_question_formulation.md
  - domain-research-academic/research_evidence_map.md
---

# Search Strategy Designer

**Objective:** Design a defensible search strategy for a literature, evidence, or intelligence-gathering task. Specify databases and source types, build per-database Boolean strings with synonyms and field-specific terminology, plan grey literature and citation tracking, and document the recall-vs-precision tradeoff explicitly. Output is a protocol a peer could re-run and reproduce.

**When to use:**
- Beginning a literature review, evidence synthesis, or systematic intelligence scan.
- An ad-hoc search returned too much (low precision) or too little (low recall) — the search needs structure.
- Audit-grade defensibility required (systematic review, regulatory filing, expert testimony).
- Multiple researchers will execute the same search and need shared specification.

**When NOT to use:**
- A casual "what does the field say about X" check that doesn't need defensible coverage.
- A specific known item to retrieve (use citation tracking, not strategy design).

**Audience:** Researchers, analysts, journalists, policy people, students, anyone whose deliverable depends on defensible coverage.

---

## Inputs / Context

1. **The research question** (sharply stated).
2. **Concept components.** The 2–4 conceptual pieces of the question (e.g., "intervention X" + "population Y" + "outcome Z").
3. **Discipline / domain.** Affects database choice, terminology, and grey-literature relevance.
4. **Date range** for inclusion.
5. **Languages** to include / exclude.
6. **Recall-vs-precision priority.** Are you willing to screen many false positives to avoid missing relevant items (high recall) or do you want a clean small set (high precision)?
7. **Time / access budget.** Limits database choice and depth.

---

## Constraints

### Must
- Identify 2–6 **concept components** of the question. Boolean strings will combine them with AND between concepts and OR within each concept.
- For each concept, list 5–15 **synonyms / variants** including: alternate spellings, abbreviations, hyphenation variants, controlled vocabulary terms (MeSH, EMTREE, ERIC thesaurus), field-specific jargon, and historical terminology.
- Select 2–5 **databases / sources**, justified by domain coverage. Include at least one general (Google Scholar, Scopus, Web of Science) and one domain-specific where appropriate.
- Build a Boolean string **per database** — different databases use different syntax (PubMed's `[tiab]`, Scopus's `TITLE-ABS-KEY`, Google Scholar's lack of advanced operators).
- Plan **grey literature** sources by name (organizational reports, working papers, dissertations, regulator publications, industry reports, preprints).
- Plan **backward and forward citation tracking** from named seed papers.
- State the **recall-vs-precision tradeoff** explicitly and which side this strategy errs on.
- Stamp the **search date** when executed (literature reviews are time-bound).

### Must Not
- Use the same Boolean string across databases that have different syntaxes.
- Skip grey literature in domains where it carries the field (policy, technical, industry, government).
- Use a single database — single-database searches have known coverage gaps.
- Generate synonym lists from intuition only — check at least one controlled vocabulary.
- Pretend high precision and high recall simultaneously; one is sacrificed for the other.

---

## Instructions

### Step 1 — Decompose into concepts
Break the question into 2–6 concept components. Each becomes one parenthesized OR group in the final Boolean string.

### Step 2 — Generate synonym sets per concept
For each concept, produce 5–15 variants. Sources: controlled vocabulary (MeSH, etc.), Wikipedia disambiguation pages, glossaries, recent landmark papers' keyword lists, the user's own domain knowledge.

### Step 3 — Select databases
Pick 2–5 with a one-line justification each. Map each concept to relevant database fields (title, abstract, full text, keyword, MeSH, etc.).

### Step 4 — Build per-database Boolean strings
For each database:
- Use that database's syntax precisely
- Combine synonyms within concepts with `OR`
- Combine concepts with `AND`
- Apply field tags appropriate to that database
- Add filters (date, language, document type)

### Step 5 — Grey literature plan
Name organizations, document types, and sources to hand-search. Don't just say "grey literature"; name the specific outlets.

### Step 6 — Citation tracking plan
Identify 2–5 seed papers (most-cited recent reviews or pivotal studies). For each: how many generations of backward citations, how many of forward.

### Step 7 — Estimate yield and screen burden
Run the strategy mentally: roughly how many hits per database? Total expected after deduplication? Title/abstract screen burden? If yield is way too high (>5,000) or too low (<20), revise.

### Step 8 — Document recall-vs-precision tradeoff
State which side the strategy errs on and why. Note what an alternate strategy would change.

### Step 9 — Reproducibility check
Could a peer execute this strategy and get the same result set ±5%? If not, sharpen.

---

## False-Positive Prevention

1. **Synonym thinness.** A 3-synonym list misses load-bearing variants. Aim for 5–15.
2. **Database mono-culture.** One database has known biases. Use 2+.
3. **Syntax transfer error.** PubMed Boolean does not work in Google Scholar. Build per database.
4. **Controlled-vocab skip.** MeSH / EMTREE / ERIC capture decades of indexing work; skipping them costs recall.
5. **Grey-literature blindness.** In policy / technical / industry domains, grey is the literature.
6. **Recall-precision dishonesty.** Claiming "comprehensive and clean" — pick one to optimize.
7. **Undocumented date.** A search without a stamped date is unreproducible.

---

## Output Format

```
# Search strategy — [research question]

## Question
> [Sharply stated]

## Concept components
| # | Concept | Synonyms / variants |
|---|---------|---------------------|
| 1 | [...]   | term1, term2, abbreviation, MeSH term, ... |
| 2 | [...]   | ... |

## Databases
| Database | Justification | Field mapping |
|----------|---------------|----------------|
| [name]   | [domain coverage] | title/abstract/keyword |

## Boolean strings (per database)

### [Database 1]
```
("term1" OR "term2" OR "term3"[MeSH]) AND ("term4" OR "term5") AND ("term6" OR "term7")
filters: 2015–2026, English, Article OR Review
```

### [Database 2]
[...]

## Grey literature
- [Org / outlet] — [what to look for]
- [...]

## Citation tracking
- Seed papers: [list with citations]
- Backward: [N generations]
- Forward: [N generations]

## Yield estimate
- Per database: [estimates]
- Total after dedup: [estimate]
- Screen burden: [time / per-screener]

## Recall-vs-precision
- Erring toward: [recall / precision]
- Tradeoff cost: [...]
- Alternate strategy would change: [...]

## Search date
- Planned: [date]

## Reproducibility check
- Peer could re-run? [yes / no, with what additional spec]
```

---

## Verification

- [ ] 2–6 concept components identified.
- [ ] 5–15 synonyms per concept including controlled vocabulary terms.
- [ ] 2–5 databases selected with justification.
- [ ] Boolean string per database with correct syntax.
- [ ] Grey literature named by source, not generic.
- [ ] Citation tracking plan with seed papers.
- [ ] Recall-vs-precision priority stated explicitly.
- [ ] Search date stamped.
- [ ] Yield estimate within reasonable range.
- [ ] Strategy reproducible by a peer.
