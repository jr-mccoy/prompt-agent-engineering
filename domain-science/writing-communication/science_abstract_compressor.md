---
title: "Abstract Compressor (Structured & Unstructured)"
category: science/writing-communication
description: "Compresses user-supplied results into a structured and/or unstructured abstract calibrated to discipline conventions and a target word limit, with the confirmatory result kept front and center."
techniques:
  - ST-01
  - ST-03
  - DS-02
  - QA-01
  - CM-02
difficulty: advanced
tags:
  - abstract-writing
  - structured-abstract
  - word-limit
  - equator-guidelines
  - confirmatory-result
  - scientific-writing
  - open-science
  - calibrated-language
updated: "2026-06-26"
related_prompts:
  - domain-science/writing-communication/science_imrad_paper_drafter.md
  - domain-science/writing-communication/science_lay_summary_translator.md
  - domain-science/methods-foundations/science_methods_section_drafter.md
---

# Abstract Compressor (Structured & Unstructured)

**Objective:** Produce a structured abstract (Background/Methods/Results/Conclusions or an IMRaD-mini) and, where the venue allows, an unstructured prose abstract — both compressed to a target word count and calibrated to discipline conventions. Every quantitative claim comes only from user-supplied results, the primary confirmatory finding stays front and center, and no conclusion exceeds what the reported results support.

**When to use:** Once results are settled and the take-home message is fixed, when you need an abstract that fits a specific journal/conference word and structure limit.

**Required inputs:**
- **Discipline.** Field and subfield (drives word limit, structure norm, and reporting expectations).
- **Manuscript / finding context.** The actual results — effect sizes, intervals, p-values, sample sizes — user-supplied; never invented.
- **Target venue or audience.** Journal/conference name and its abstract word limit and structured/unstructured requirement (if unknown, ask or use a labeled default).
- **Study type.** Selects the relevant EQUATOR abstract checklist (e.g., CONSORT for Abstracts, PRISMA for Abstracts, STROBE).
- **Primary claim.** The single confirmatory take-home message, distinguished from secondary/exploratory findings.

**Optional inputs:**
- Keywords list and any required abstract subheadings the venue mandates.
- Pre-registration reference (to confirm what was pre-specified).
- Data/code availability and preprint status.
- Both a tight (e.g., 150-word) and a longer (e.g., 250-word) target if the venue range is wide.

**Constraints — Must:**
- Hit the target word count; report the exact word count of each abstract delivered.
- Keep the primary confirmatory result first; label secondary and exploratory findings as such.
- Pull every number from user-supplied results and tag any missing figure `[user-supplied]`.
- Follow the venue's structured/unstructured requirement and the relevant EQUATOR-for-abstracts checklist.
- Use calibrated, falsifiable language; report effect direction and magnitude, not just significance.
- Surface preprint and data/code availability as a default consideration.

**Constraints — Must Not:**
- Do not invent results, numbers, citations, DOIs, author claims, or journal requirements. Draft only from user-supplied content; mark gaps `[user-supplied]` and ask.
- Do not state a conclusion the abstract's own reported results do not support.
- Do not present an exploratory or post-hoc result as the primary confirmatory finding.
- Do not use "novel," "groundbreaking," "first-ever," "gold standard," or "unprecedented" in drafted text.
- Do not pad to reach a word count with content not backed by supplied results.

**Instructions:**

1. **Confirm constraints.** Restate discipline, study type, target venue, structured-vs-unstructured requirement, and word limit (or range). Name the EQUATOR-for-abstracts checklist that applies.
2. **Extract the reportable facts.** Pull from user-supplied content: the question, design, key methods, the primary confirmatory result with effect size/interval, secondary findings, and the supported conclusion. Tag anything missing `[user-supplied]`.
3. **Order by confirmatory priority.** Place the primary confirmatory result first; queue secondary/exploratory findings behind it, explicitly labeled.
4. **Draft the structured abstract.** Fill the venue's subheadings (or Background/Methods/Results/Conclusions). Keep Results numeric and supplied; keep Conclusions inside what those Results support.
5. **Draft the unstructured abstract (if allowed).** Convert the structured content to a single calibrated prose paragraph without losing the result-conclusion link.
6. **Compress to target.** Trim to the word limit, cutting redundancy and hedging before cutting substance; never cut the primary result or its caveat.
7. **Calibrate language.** Replace any promotional or causal-overreach phrasing with specific, falsifiable statements matched to the design.
8. **Word-count and consistency check.** Report exact counts; confirm every number traces to supplied results and the conclusion does not exceed them; add preprint/data-availability note if the venue permits.

**Output format (locked):**

```
## Constraints
[discipline; study type → EQUATOR-for-abstracts checklist; venue; structured/unstructured; word limit]

## Reportable Facts (from user-supplied results)
- Question / design / key methods
- Primary confirmatory result: [effect, interval, p — user-supplied if missing]
- Secondary / exploratory findings (labeled)
- Supported conclusion

## Structured Abstract  (word count: N / limit)
**Background:** ...
**Methods:** ...
**Results:** ...
**Conclusions:** ...

## Unstructured Abstract  (word count: N / limit)
[single calibrated paragraph — include only if venue allows]

## Keywords
[user-supplied or proposed]

## Open Science Note
- Preprint / data / code availability: [if venue permits]

## Checks
- Every number traced to supplied results: yes/no
- Conclusion within reported results: yes/no
- Confirmatory result first: yes/no
- Outstanding [user-supplied] gaps: [...]
```

**Reporting-standard / convention alignment:** EQUATOR reporting guidelines for abstracts (CONSORT for Abstracts, PRISMA for Abstracts, STROBE abstract items, and discipline equivalents); target-journal abstract word limit and structured/unstructured requirement; discipline word-count norms (many fields cap at 150–300 words).

**Verification checklist (before delivering):**
- [ ] Exact word count is reported and within the venue limit.
- [ ] The primary confirmatory result appears first and secondary/exploratory findings are labeled.
- [ ] Every quantitative claim traces to a user-supplied result (or is `[user-supplied]`).
- [ ] The Conclusions do not exceed what the reported Results support.
- [ ] Structured vs. unstructured form matches the venue requirement.
- [ ] The relevant EQUATOR-for-abstracts items are covered.
- [ ] No banned promotional words appear in drafted text.
- [ ] Preprint/data-availability note surfaced where the venue allows.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Conclusion creep | A confident closing sentence broader than the reported numbers | Test the conclusion against the listed Results before finalizing |
| Result swap | An eye-catching exploratory finding leading the abstract | Enforce confirmatory-first ordering from the facts list |
| Significance-only | "Significant improvement" with no effect size | Require magnitude + interval; flag bare p-values |
| Invented precision | A clean stat the user never supplied | Tag any unsupplied number `[user-supplied]`; never fill |
| Word-count padding | Filler clauses added to reach the limit | Trim hedging first; do not add unsupported content to lengthen |
