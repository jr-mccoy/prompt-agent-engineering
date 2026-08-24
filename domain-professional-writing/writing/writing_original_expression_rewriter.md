---
title: "Original-Expression Rewriter — Re-express Source Text in Your Own Words While Preserving Facts and Meaning"
category: professional-writing/writing
description: "Rewrite a nonfiction source passage into genuinely original expression that conveys the same facts, meaning, and level of certainty — reducing copied wording and structure while preserving truthfulness. Produces a rewrite, a fidelity check, and a copying-risk audit that flags anything better handled by quotation or attribution."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - QA-01
  - RT-05
difficulty: intermediate
tags:
  - paraphrasing
  - rewriting
  - original-expression
  - plagiarism-avoidance
  - fidelity
  - attribution
updated: "2026-07-06"
related_prompts:
  - domain-professional-writing/writing/writing_precision_doc_edit.md
  - domain-professional-writing/writing/writing_voice_print_extractor.md
  - domain-research-academic/research_secondary_source_synthesis.md
---

# Original-Expression Rewriter

**Objective:** Rewrite a source passage so it uses **original wording and sentence structure** rather than the source's, while conveying the **same facts, relationships, and level of certainty** — so the result is defensibly the writer's own expression and remains truthful to the source. Show the fidelity check and the copying-risk audit so the writer can trust the output and know what still needs quotation or attribution.

**Scope:** This prompt is for **nonfiction** — factual and informational source text (articles, reports, reference material, documentation, research, how-to and explanatory content). It is not for re-expressing creative works (fiction, poetry, lyrics, art). Nonfiction is the ideal case because its value is the *information*, which is exactly what re-expression is allowed to carry over.

**Grounding principle:** Copyright protects a specific *expression* (the exact words, phrasing, and structure), not the underlying **facts or ideas**. Legitimate rewriting re-expresses the facts in genuinely new language. This prompt is for that: producing your own expression of shared information — not synonym-swapping over the source's structure, and not passing another author's original *analysis, argument, or framework* off as your own. Facts are free to re-express; an author's distinctive contribution still gets credited. Where content *cannot* be re-expressed without loss (a coined term, a direct quote, a defined term, a memorable line), the correct move is quotation with attribution, and the prompt says so instead of disguising it.

**When to Use:**
- Turning research, reference material, or a source article into your own prose for a report, brief, blog post, study notes, article, or summary.
- Reducing overlap with a source you consulted so your draft is your own words, not lightly-reworded copying.
- Producing a from-scratch explanation of facts you learned from one or more nonfiction sources.

**When NOT to use:**
- The source is a creative work (fiction, poetry, lyrics) — out of scope; re-expression does not make creative expression yours.
- The passage is mostly direct quotation that must stay verbatim (legal text, a person's exact words, a defined term, a standard/spec) — rewriting would falsify it.
- You need a licensing or legal determination of infringement — this is a writing tool, not legal advice. Flag genuinely uncertain cases for a professional.
- The source's *meaning* is what you want to change — use an editing or argument prompt; this one holds meaning fixed.

**Audience:** Writers, students, researchers, analysts, journalists, and content professionals who need original nonfiction prose that faithfully conveys information drawn from sources.

---

## Inputs / Context

Provide what you have; the rewrite improves with each item.

1. **The source passage** (paste it; wrap in `<source>...</source>`).
2. **Purpose and audience:** where this rewrite will be used and who reads it (sets register and depth).
3. **Attribution context:** Is the source cited elsewhere in your work? Is this a fact-sharing use or does it lean on the source's original analysis/creativity? (Affects whether re-expression alone is enough.)
4. **Constraints (optional):** length target, required terms that must stay (technical terms, proper nouns, defined terms), forbidden words, tone/voice.
5. **Non-negotiable facts:** any numbers, names, dates, or claims that must survive exactly.

If purpose/audience are missing, state the assumption you are rewriting under at the top and proceed — do not stall.

---

## Constraints

### Must
- Preserve **factual accuracy**: every claim, number, name, date, causal relationship, and qualifier in the source survives with the same meaning.
- Preserve **certainty and stance**: hedges ("may," "in some cases"), intensifiers, and the source's confidence level carry over unchanged.
- Produce **genuinely original expression**: new sentence structure, new phrasing, and independent ordering where meaning allows — not synonym-swapping over the source's skeleton.
- Keep **terms that must not change**: proper nouns, technical/defined terms, and standard terminology stay as-is (there is no "original" synonym for *photosynthesis* or *EBITDA*), and this is fine — those are facts, not expression.
- **Quote and attribute** anything that cannot be re-expressed without loss or misrepresentation: distinctive phrasings, coined terms, direct statements, creative language. Mark these explicitly rather than paraphrasing them away.
- Run and report a **fidelity check** (claim-by-claim) and a **copying-risk audit** (how much source structure/wording remains, and what still needs a quote or citation).

### Must Not
- Change, drop, add, or soften any fact, number, relationship, or certainty level to make the rewrite flow.
- **Synonym-swap**: replacing words one-for-one while keeping the source's exact sentence structure and clause order. That is still copying the expression — it does not produce original work and does not avoid the underlying issue.
- Invent facts, examples, citations, or nuance not present in or directly entailed by the source.
- Strip required attribution or present source-original *analysis, argument, or creative expression* as the writer's own — re-expression covers facts, not someone's distinctive intellectual or creative contribution.
- Claim the output is "copyright-safe," "plagiarism-free," or legally cleared. Report what was done (re-expression, structural change, flagged items); leave legal conclusions to a qualified professional.

---

## Instructions

1. **Separate facts from expression.**
   - List the source's core facts, claims, relationships, and their certainty levels. This is the meaning to preserve. The *wording and structure* are what you will replace.

2. **Re-express from the fact list, not the sentences.**
   - Write new prose from the extracted facts, choosing your own structure and phrasing. Working from the fact list (rather than editing the source line by line) is what produces genuinely independent expression instead of a reworded copy.

3. **Restructure, don't just re-word.**
   - Change sentence boundaries, clause order, and framing where meaning allows. Combine or split ideas differently from the source. Keep only what *must* stay: required terms, proper nouns, exact figures.

4. **Handle the un-paraphrasable explicitly.**
   - A distinctive phrase, coined term, memorable line, or passage whose value *is* its exact wording should be quoted and attributed, not disguised. Flag each one; do not silently reword it into false originality.

5. **Verify fidelity (CRITICAL).**
   - Compare the rewrite to the source claim-by-claim. Confirm nothing was added, dropped, or shifted in certainty. A rewrite that reads well but changed a "some" to "all," dropped a qualifier, or invented a figure has failed.

6. **Audit copying risk.**
   - Estimate how much of the source's *structure and distinctive wording* still shows through. Identify any remaining phrases that track the source too closely and either re-express them further or mark them for quotation. Note whether the use still needs a citation regardless of rewriting.

7. **Assemble output:** rewrite → fidelity check → copying-risk audit.

---

## False-Positive Prevention

1. **Synonym-swap mistaken for rewriting.** Swapping words while keeping the source's sentence skeleton is not original expression and does not resolve the concern — it is the single most common failure. Restructure, or the rewrite is just a copy in a costume.
2. **Fidelity lost for the sake of freshness.** Changing "declined 12% in Q3" to "dropped sharply" trades a fact for fluency. Never sacrifice a number, name, or qualifier to sound more original.
3. **Certainty drift.** Turning "may reduce risk" into "reduces risk" (or vice versa) is a factual change. Preserve hedges and confidence exactly.
4. **Passing off an author's original analysis as your own.** Re-expressing facts is legitimate; re-expressing a nonfiction author's distinctive argument, framework, model, or original interpretation to claim it as yours is not — even fully reworded, the *idea* is theirs. Attribute the analysis even when you change every word. (Facts stay free; original thinking gets credited.)
5. **False "copyright-safe" guarantee.** Rewriting reduces expressive overlap; it is not a legal clearance. Do not assert the output is safe or plagiarism-free — report actions, flag uncertainty, defer legal conclusions.
6. **Dropping a required quote.** Some content (direct statements, defined terms, verbatim legal or contractual text) must stay word-for-word and attributed; paraphrasing it falsifies it. Quote instead.
7. **Over-changing terminology.** "Originalizing" a technical or proper term into a near-synonym introduces error. Standard terms are facts — keep them.

---

## Output Format

```
## Rewrite
[The re-expressed passage — original wording and structure, same facts, ready to use.
 Any content that had to stay verbatim appears as a marked quotation with attribution.]

## Fidelity Check
Claim-by-claim, source → rewrite:
- [Source claim / figure / relationship] → preserved as [rewrite wording] ✓
- [next] → ✓
- Certainty preserved: [note any hedges/intensifiers carried over]
- Nothing added / dropped: [confirm, or list any deliberate, instructed omission]

## Copying-Risk Audit
- **Structural independence:** [how much sentence structure / ordering differs from source — high / partial, with an example]
- **Residual close phrasing:** [any phrases still tracking the source, and how handled — re-expressed further or flagged for quotation; or "none"]
- **Must-quote / must-attribute items:** [distinctive phrasings, coined terms, direct quotes, or source-original analysis that need quotation/citation — or "none"]
- **Attribution note:** [whether the use still requires a citation regardless of rewriting]
- **Flag for professional review:** [any case where infringement risk is genuinely unclear — or "none"; this tool does not give legal advice]
```

---

## Verification

- [ ] Rewrite uses original sentence structure and phrasing, not synonym-swapping over the source's skeleton.
- [ ] Every fact, number, name, date, and relationship from the source is preserved with the same meaning.
- [ ] Hedges, qualifiers, and certainty level are carried over unchanged.
- [ ] Required terms, proper nouns, and defined terms are kept as-is (not "originalized" into error).
- [ ] Content that must stay verbatim is quoted and attributed, not disguised as paraphrase.
- [ ] Fidelity check confirms nothing added, dropped, or shifted in certainty.
- [ ] Copying-risk audit reports structural independence and flags anything needing quotation or citation.
- [ ] No claim that the output is "copyright-safe" or legally cleared; genuinely uncertain cases are flagged for professional review.
