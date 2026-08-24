---
title: "Translation Comparison & Variant Notes — Why Renderings Differ"
category: biblical-studies/exegesis-interpretation
description: "Compare how major translations render a verse and explain the kinds of reasons translations differ — translation philosophy, lexical choice, syntax, and textual-critical variants — without inventing manuscript data, apparatus readings, or specific variant attributions. Routes textual-critical questions to named real resources."
techniques:
  - RT-02
  - RT-05
  - QA-04
  - QA-05
  - OC-12
difficulty: intermediate
tags:
  - translation
  - textual-criticism
  - variants
  - anti-fabrication
updated: "2026-06-11"
related_prompts:
  - domain-biblical-studies/exegesis-interpretation/biblical_word_study_original_language.md
  - domain-biblical-studies/exegesis-interpretation/biblical_passage_exegesis_workflow.md
  - domain-biblical-studies/exegesis-interpretation/biblical_multiview_interpretation_map.md
---

# Translation Comparison & Variant Notes

**Objective:** Help a user understand why translations of a verse differ — and what (if anything) the differences mean for interpretation — by categorizing the *kinds* of reasons translations diverge, **without fabricating manuscript or apparatus data.**

> **STRONG-GUARD prompt.** Invented variant readings, manuscript sigla, and "the oldest manuscripts say…" claims are a serious fabrication risk. This prompt categorizes reasons for difference and routes textual-critical specifics to real resources rather than asserting them from memory.

**When to use:**
- Two translations render a verse differently and you want to know why.
- A teaching hinges on a particular translation and you want to test it.
- Understanding whether a difference is stylistic or substantive.

**When NOT to use:**
- You need a focused word study — use `biblical_word_study_original_language.md`.
- You want a full interpretation map of a contested reading — use `biblical_multiview_interpretation_map.md`.

**Audience:** Pastors (P), seminary/academic (A), equipped group leaders (G).

---

## Inputs / Context

1. **The verse and the translations.** The reference plus the actual wording of each translation the user is comparing — **pasted by the user**. The model does not reproduce translation text from memory.
2. **The specific difference (optional).** The word/phrase the user is asking about.
3. **Declared tradition (optional).** Some traditions prefer particular translations/textual bases; note this descriptively without endorsing.

---

## Constraints

### Must
- Categorize each difference by its likely *type*: **translation philosophy** (formal vs. dynamic), **lexical choice** (a word with a range), **syntactic/grammatical** ambiguity, or **textual variant** (the underlying text differs).
- For suspected textual-variant differences, state that the specifics (which manuscripts, which reading is preferred) must be checked in a real apparatus/resource — and **do not** invent them.
- Distinguish differences that are **stylistic** (no meaning change) from those that are **substantive** (affect interpretation).
- Work only from the translation wording the user supplied.

### Must Not
- Invent manuscript names/sigla, dates, apparatus readings, or "the earliest/best manuscripts" claims.
- Reproduce translation text from memory (risk of misquotation) — use the user's pasted text.
- Assert which reading is "original" as settled; route to textual-critical resources.
- Use a translation difference to push a contested doctrine.

### Tradition-neutral stance (Must / Must Not)
- **Must:** note translation/text-base preferences descriptively across traditions.
- **Must Not:** present one translation or textual tradition as the correct one.

---

## Instructions

### Step 1 — Lay out the renderings
Restate each supplied translation's wording (from the user) side by side and pinpoint exactly where they differ.

### Step 2 — Categorize the difference
For each point of difference, identify the likely type (philosophy / lexical / syntactic / textual variant), with reasoning.

### Step 3 — Stylistic vs. substantive
Say whether the difference changes the meaning or is stylistic. If substantive, describe the interpretive options (route to the multi-view map if needed).

### Step 4 — Route textual questions
If a textual variant is likely, first point the user to the translations' own footnotes — most major translations flag variants ("some manuscripts read…"), and the footnote is a legitimate, already-verified starting point. For specifics beyond the footnote (which manuscripts, which reading is preferred), state plainly that they must be verified in a real apparatus/resource (e.g., NA28/UBS apparatus, BHS/BHQ, a critical commentary) — and do not fabricate them.

### Step 5 — Bottom line
Summarize what the user should conclude and what they still need to verify.

---

## Output Format

```
# Translation Comparison — [reference]

## Renderings (as supplied by user)
- [Translation A]: "[user-pasted wording]"
- [Translation B]: "[user-pasted wording]"

## Point(s) of difference
| Where | Likely type | Stylistic or substantive | Notes |
|-------|------------|--------------------------|-------|
| [..]  | philosophy/lexical/syntactic/textual-variant | [..] | [..] |

## Textual-variant routing (if applicable)
- Verify specifics in: [apparatus/critical resource] — do not rely on recalled manuscript claims.

## Bottom line
- [what to conclude] | Still verify: [..]
```

---

## Verification

- [ ] Worked only from user-supplied translation wording (no memory quotes).
- [ ] Each difference categorized by type.
- [ ] Stylistic vs. substantive distinguished.
- [ ] No invented manuscripts, sigla, dates, or apparatus readings.
- [ ] Textual specifics routed to a real resource; nothing asserted as "original."
- [ ] No doctrine pushed via a translation difference.

---

## False-Positive Prevention

❌ **DON'T:**
- Say "the oldest/best manuscripts read…" or name manuscripts from memory.
- Reproduce a translation's wording from memory (you may misquote).
- Treat a dynamic vs. formal rendering as a meaning change when it's stylistic.
- Declare which reading is "the original."

✅ **DO:**
- Use the user's pasted translations and pinpoint the difference.
- Categorize the difference (philosophy/lexical/syntactic/textual).
- Point to the translations' own footnotes as the first, already-verified check on variants.
- Route manuscript/variant specifics to a real apparatus and mark verify-required.
- Separate stylistic differences from substantive ones.

---

## Techniques Used

- **RT-02 (Multi-Dimensional Analysis Framework):** Requires analyzing each translation difference across multiple dimensions — translation philosophy, lexical choice, syntactic/grammatical ambiguity, and textual-variant possibility — preventing attribution of every difference to a single cause.
- **RT-05 (Evidence-Based Reasoning):** Works exclusively from translation wording supplied by the user; no translation text is reproduced from model memory (misquotation risk), and every categorization is grounded in the supplied text.
- **QA-04 (Uncertainty Acknowledgment):** Distinguishes stylistic differences from substantive ones and routes textual-variant questions to real resources with an explicit statement that specifics are unverified — making the limits of what can be known without a real apparatus visible.
- **QA-05 (Citation Requirements):** Routes textual-critical specifics (manuscript names, apparatus readings, "oldest manuscripts" claims) to named real resources (NA28/UBS, BHS/BHQ, critical commentaries) rather than asserting them from memory.
- **OC-12 (External Reference Catalog):** The bottom-line summary includes a structured Still verify field and a Textual-variant routing entry naming specific resources — turning the comparison output into a structured research roadmap.
