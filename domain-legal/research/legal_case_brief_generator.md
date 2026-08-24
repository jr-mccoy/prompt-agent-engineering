---
title: "Case Brief Generator"
category: legal/research
description: "Produce a structured case brief from an opinion: caption, procedural posture, facts, issue(s), holding(s), reasoning, disposition, separate writings, and significance — all grounded in the supplied opinion text."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - QA-01
difficulty: beginner
tags:
  - legal
  - research
  - case-brief
  - opinion-analysis
updated: "2026-05-08"
related_prompts:
  - domain-legal/research/legal_research_memo_irac.md
  - domain-legal/research/legal_precedent_comparison_table.md
  - domain-legal/research/legal_jurisdiction_split_analysis.md
---

**Purpose:** Produce a precise, reusable case brief from an opinion the user supplies. Designed to be filed in a research file or pasted into a memo — not to summarize for a non-lawyer.

**When to use:** Reading a new opinion for a matter, building a case-law file on an issue, prepping for oral argument, training/evaluation tasks where the opinion text is the closed universe.

---

## Your Input

- **Opinion text:** [Paste the opinion. If only an excerpt, mark `[EXCERPT]` and the brief will note that scope.]
- **Citation:** [Full Bluebook citation; if uncertain, supply what you have]
- **Court and year:** [If not obvious from the citation]
- **Why you are reading it:** [Issue you are tracking, motion you are preparing for, doctrinal question — drives the "Significance" section]
- **Reading depth:** [Quick (½ page) / Standard (1 page) / Deep (2+ pages, doctrinal genealogy)]

---

## Constraints

**Must:**
- Identify and separately label: holding (binding rule of decision) vs. dicta.
- Identify the procedural posture and standard of review the court applied.
- Distinguish majority, plurality, concurrence, and dissent. Track which justices joined which writings.
- Quote the operative holding language verbatim.
- Note any test the court announces and its elements.
- Flag whether the opinion overrules, distinguishes, or limits prior authority — only if the opinion text says so.
- For "Significance," tie the case to the user's stated reason for reading it.

**Must Not:**
- Invent quotations or pinpoints. Quote only language present in the supplied text.
- Convert dicta into holding language.
- Smooth over a fractured opinion. If the majority is a plurality, say so and identify the narrowest concurrence (Marks rule for federal cases).
- Generate facts not in the opinion to "complete" the picture.
- Cite parallel reporters or unsupplied subsequent history.
- Add "this case stands for" platitudes that are not anchored in the text.

---

## Instructions

1. Identify the caption, court, and date from the supplied text or supplied citation.
2. Extract the procedural posture: who appealed, from what ruling, on what record, under what standard of review.
3. Build the **Facts** section using the court's recitation. Mark facts the court flagged as undisputed vs. construed in favor of the non-movant.
4. Identify each **Issue** the court resolved. If the court framed multiple, list each separately.
5. State each **Holding** in one sentence and quote the operative language verbatim. Mark dicta separately.
6. Walk the **Reasoning** in the order the court used. Identify the doctrinal moves: rule statement, test articulation, application, response to counter-arguments.
7. Capture **Disposition** (affirmed / reversed / remanded / vacated; in part where applicable).
8. Summarize **Concurrences and Dissents** by justice. Note partial joins.
9. **Significance** for the user's purpose — strictly grounded in what the opinion says, not in what later courts may have done with it.

---

## Output Format

```markdown
## {Case Name}, {citation}

- **Court:** {...}
- **Date:** {...}
- **Author of opinion:** {...}
- **Joined by:** {...}
- **Vote:** {e.g., 5–4, 6–3 with two concurrences}

## Procedural Posture

{Who, from what ruling, on what record, under what standard of review.}

## Facts

{Court's recitation. Note disputed vs. undisputed where the court flagged it.}

## Issue(s)

1. {...}
2. {...}

## Holding(s)

1. {One-sentence holding.} **Operative language:** "{quoted verbatim, with pinpoint}"
2. ...

## Test / Rule Announced

{If the court articulated a test, list its elements. Otherwise: "No new test articulated."}

## Reasoning

{Walk the court's argument in its order. Identify rule statement, test application, treatment of counter-arguments.}

## Treatment of Prior Authority

- Overruled: {... or "none stated"}
- Distinguished: {...}
- Limited: {...}
- Reaffirmed: {...}

## Disposition

{Affirmed / reversed / vacated / remanded; in part if applicable.}

## Concurrences

- **{Justice}, concurring**, joined by {...}: {one-paragraph summary; note whether concurrence is in judgment only or in full}.

## Dissents

- **{Justice}, dissenting**, joined by {...}: {one-paragraph summary}.

## Dicta Worth Noting

{List statements that are likely dicta but may be useful to opposing or supporting positions.}

## Significance for Our Matter

{Tied to the user's stated reason for reading the case. Distinguish what the case actually held from what one might argue from it.}

## Open Items

- Subsequent history not in supplied text: {...}
- Cited authority worth pulling: {...}
```

---

## Verification

- [ ] Holding stated as one sentence with operative language quoted verbatim.
- [ ] Dicta separately identified, not laundered into holding.
- [ ] Plurality / majority / concurrence / dissent mapped to which justices.
- [ ] Disposition stated precisely, including partial reversals or remands.
- [ ] Test elements listed if the court announced a test.
- [ ] Significance section tied to the user's stated reason; no untethered platitudes.
- [ ] No quotations or pinpoints not present in supplied text.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Treating a plurality as a majority | Note plurality; identify the narrowest controlling concurrence under Marks (federal) or the analog in state systems |
| Capturing dicta as holding | The holding is the rule of decision necessary to the disposition; everything else is dicta or background |
| Inventing pinpoints | Pinpoints come from the supplied text only |
| Saying "the court held that…" when describing the standard of review | Standard of review is procedural framing, not a holding |
| Smoothing a 4-1-4 split into one rule | Identify the fracture; the controlling rule may be the narrowest concurrence |
| Adding subsequent history not supplied | Flag in Open Items as something to verify externally |
| Calling a footnote a holding | Footnotes can be holding or dicta — assess whether the footnote was necessary to the disposition |
| Quoting a dissent as if it were the majority | Always label the source — majority, plurality, concurrence, dissent |
