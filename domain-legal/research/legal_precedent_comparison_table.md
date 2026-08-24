---
title: "Precedent Comparison Table"
category: legal/research
description: "Compare three or more cases on a common dispositive issue in a structured table — facts, holdings, reasoning, distinguishing facts, and analogical fit to the user's matter."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - legal
  - research
  - precedent
  - comparison
  - case-analysis
updated: "2026-05-08"
related_prompts:
  - domain-legal/research/legal_case_brief_generator.md
  - domain-legal/research/legal_research_memo_irac.md
  - domain-legal/research/legal_jurisdiction_split_analysis.md
---

**Purpose:** Generate a side-by-side table comparing multiple cases on a common issue, then assess analogical fit to the user's matter. Designed for the moment in research when you have 3–8 candidate cases and need to decide which to lead with.

**When to use:** Brief writing, motion preparation, settlement positioning, factual analogue selection, training/evaluation tasks where you have a closed set of cases to compare.

---

## Your Input

- **Common issue / question:** [The doctrinal question all the cases address]
- **Jurisdiction (controlling for our matter):** [Federal circuit / state]
- **Cases to compare:** [Full citations + the relevant text or holdings — minimum 3, no useful maximum]
- **Our matter's key facts:** [The facts that need to map onto these cases]
- **Our position:** [What we want the rule and the analogy to support]
- **What I already think is the strongest case for us:** [Optional — useful to test against]

---

## Constraints

**Must:**
- Use a single comparison table with columns chosen for the issue, not a generic template.
- For each case, populate columns from the supplied text only; do not extrapolate.
- Mark each case as **binding**, **persuasive (in-circuit)**, **persuasive (out-of-circuit / sister-state)**, or **non-precedential** for the user's controlling jurisdiction.
- Identify the **narrowest holding** of each case relevant to the issue.
- Add an **analogical fit** column: how the case's operative facts map onto the user's facts.
- After the table, identify the **strongest** and **weakest** cases for the user's position with the operative reason.

**Must Not:**
- Cite to language not in the supplied case text. Use `[NEED PIN: {what}]` for missing pinpoints.
- Treat distinguishable cases as analogous because they reach the user's preferred outcome.
- Average the cases into a "general rule" that no one case actually announces.
- Combine binding and persuasive authority in ranking without flagging the difference.
- Generate procedural posture or appellate history not in the supplied text.

---

## Instructions

1. Identify the **operative legal question** the cases share.
2. Choose **comparison columns** suited to the issue. Minimum useful columns:
   - Citation
   - Authority status (binding / persuasive in-circuit / persuasive out-of-circuit / non-precedential)
   - Procedural posture
   - Operative facts
   - Test or rule applied
   - Holding (narrowest, on this issue)
   - Reasoning move that did the work
   - Outcome
   - Analogical fit to our matter (Strong / Moderate / Weak / Adverse) with one-sentence reason
3. Populate the table from the supplied case text.
4. Below the table, write a **Lead-with** recommendation: which case to cite first, and why.
5. Write a **Distinguish** section: which adverse cases need distinguishing and the operative distinction.
6. Identify **gaps**: what facts or authority are missing to make the strongest argument.

---

## Output Format

```markdown
## Issue Under Comparison

{One-sentence statement of the doctrinal question.}

## Authority Map

| Case | Court | Year | Status (for our jurisdiction) | Procedural posture | Operative facts | Test/rule applied | Narrowest holding | Reasoning move | Outcome | Analogical fit |
|------|-------|------|-------------------------------|-------------------|-----------------|--------------------|-------------------|----------------|---------|----------------|
| ...  | ...   | ...  | ...                           | ...               | ...             | ...                | ...               | ...            | ...     | Strong/Moderate/Weak/Adverse — {why} |

## Lead With

**{Case}** — because {operative reason: facts most analogous, binding, recent, narrowly tailored holding, etc.}.

## Distinguish

| Adverse case | Why it looks bad for us | Operative distinction (fact / law / posture) |
|--------------|--------------------------|-----------------------------------------------|

## Synthesis

{One paragraph: what the cases collectively support, where they conflict, where the user's matter falls.}

## Gaps

- Facts to develop in our matter: {...}
- Additional authority worth pulling: {...}
- Pinpoints needed: {... `[NEED PIN: ...]` placeholders}

## Recommended Citation Order in a Brief

1. {Case} — primary support for {proposition}
2. {Case} — secondary support, addresses {sub-issue}
3. {Case} — distinguishing the leading adverse authority
```

---

## Verification

- [ ] Each row populated only from the supplied case text or flagged with `[NEED PIN: ...]`.
- [ ] Authority status reflects the user's controlling jurisdiction, not the case's home jurisdiction.
- [ ] Holding column shows the narrowest holding on the issue, not the headline rule.
- [ ] Analogical fit column has a one-sentence reason for each rating.
- [ ] Lead-with case identified with operative reason.
- [ ] Adverse cases addressed with operative distinctions, not waved away.
- [ ] No invented case names, holdings, or pinpoints.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Calling a sister-circuit case "binding" because it's federal | Sister-circuit decisions are persuasive only |
| Inflating analogical fit because outcome is favorable | Fit is measured by facts and reasoning, not result |
| Listing the headline rule as the holding | The narrowest rule of decision is usually narrower than the headline |
| Distinguishing only on outcome rather than reasoning | A distinction must identify the doctrinal or factual move that flips the result |
| Treating an unpublished or non-precedential opinion as precedent | Mark as non-precedential and follow the controlling local rule on citation |
| Combining concurrence reasoning with majority reasoning | Track which writing each move comes from |
| Drawing a "trend" from cases at different procedural postures | A 12(b)(6) ruling and a post-trial ruling are not directly comparable |
