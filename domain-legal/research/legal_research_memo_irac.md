---
title: "IRAC Legal Research Memo"
category: legal/research
description: "Produce an interoffice legal research memo in IRAC (Issue, Rule, Application, Conclusion) format with a Question Presented, Brief Answer, Statement of Facts, Discussion, and Conclusion — built around authority the user supplies."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - legal
  - research
  - memo
  - irac
  - legal-writing
updated: "2026-05-08"
related_prompts:
  - domain-legal/research/legal_issue_spotter_from_facts.md
  - domain-legal/research/legal_statutory_interpretation.md
  - domain-legal/research/legal_precedent_comparison_table.md
  - domain-legal/research/legal_case_brief_generator.md
---

**Purpose:** Draft a closed-universe interoffice research memo on a discrete legal question, using only the authority and facts the user provides. Output is structured for a partner or senior associate to review, edit, and file in the matter.

**When to use:** Substantive research questions that need a written work product — pre-litigation assessment, motion preparation, transactional risk question, or training/evaluation tasks where the universe of authority is bounded.

---

## Your Input

- **Jurisdiction (controlling):** [Required — federal circuit, state, or "apply both X and Y and flag the conflict"]
- **Question Presented (one or more):** [The discrete legal question. If you give me only a vague topic, I will draft a Question Presented for you and ask you to confirm.]
- **Facts assumed true:** [Bullet list — the memo will not invent additional facts]
- **Authority provided:** [Cases, statutes, regulations, secondary sources — full citations + relevant text or pinpoints. Memo is closed-universe to this set.]
- **Audience:** [Partner / GC / litigation team / transactional team / regulator-facing — affects tone and length]
- **Length target:** [Short (1–2 pages) / Standard (3–5) / Long (6+)]
- **Citation style:** [Bluebook (default) / ALWD / state-specific — name it]
- **Use:** [Internal advisory / litigation work product / pre-engagement / regulator submission draft]

---

## Constraints

**Must:**
- Use the IRAC structure inside the Discussion section, with a separate IRAC pass per sub-issue.
- Open with **Question Presented** in a single sentence ending in a question mark, framed under-the-jurisdiction-when-X-facts-are-true.
- Follow with **Brief Answer**: a yes/no/probably-yes/probably-no in the first clause, then the operative reason in the next sentence.
- Include a **Statement of Facts** that uses only facts the user supplied; do not invent or paraphrase facts beyond what is provided.
- In **Application**, walk fact-by-fact through each element of the rule, citing the supplied authority by pinpoint.
- Address **counter-arguments** and the strongest opposing authority the user supplied.
- End with a **Conclusion** that mirrors the Brief Answer with added nuance and identifies follow-up research or factual development needed.
- Use the citation style specified; default to Bluebook signals (See, See, e.g., Cf., But see) when chained citations are appropriate.

**Must Not:**
- Cite any authority not in the user's authority list. If a needed citation is missing, insert `[NEED CITE: {what kind of authority}]` and continue.
- Quote or paraphrase any case beyond the text the user supplied. If a holding is needed and not provided, insert `[NEED HOLDING: {case name}]`.
- Treat secondary authority (Restatements, treatises, ALR) as binding; identify it as persuasive.
- Conclude on a question where the supplied authority is genuinely insufficient — instead, state that and identify what's needed.
- Hedge with "consult a licensed attorney" boilerplate. The memo is internal work product; the recipient is a lawyer.
- Fabricate a procedural posture or appellate history.

---

## Instructions

1. **Confirm or draft the Question Presented.** A good QP is one sentence, names the controlling jurisdiction or doctrine, and ends with the operative legal question. If multiple discrete questions are bundled, separate them and run a sub-IRAC for each.
2. **Draft the Brief Answer.** First clause: yes / no / probably yes / probably no / unclear-because-of-X. Next sentence: the reason. Maximum two sentences.
3. **Write the Statement of Facts** using only the supplied facts. Mark assumptions as such (e.g., "We assume X as stated in your input.").
4. **Discussion section:**
   - For each sub-issue, run an IRAC pass.
   - **Issue:** restate the discrete sub-question.
   - **Rule:** synthesize the applicable rule from the supplied authority. If multiple authorities conflict, name the conflict and identify what binds in the controlling jurisdiction.
   - **Application:** apply the rule to the facts, element by element, with pinpoints. Address the strongest counter-reading.
   - **Sub-conclusion:** answer the sub-issue.
5. **Conclusion:** integrate sub-conclusions, state remaining uncertainty, and identify next steps (additional research, factual development, decision points for the partner).
6. **Footnote / endnote** any methodological caveats: closed-universe research, pending appeals in supplied authority, jurisdictional gaps.

---

## Output Format

```markdown
# MEMORANDUM

**To:** {recipient}
**From:** {author}
**Date:** {date}
**Re:** {short matter description and the legal question}
**Privileged & Confidential — Attorney Work Product**

## Question Presented

{One sentence, ending in a question mark.}

## Brief Answer

{Two sentences max. Yes/no in first clause, operative reason in second.}

## Statement of Facts

{Narrative using only supplied facts. Mark assumptions explicitly.}

## Discussion

### I. {Sub-issue 1 short title}

**Issue.** {restated}

**Rule.** {synthesized from supplied authority, with pinpoints}

**Application.** {fact-by-fact, element-by-element, with pinpoints; address counter-reading}

**Sub-conclusion.** {one or two sentences}

### II. {Sub-issue 2}
...

## Conclusion

{Integrated answer. Remaining uncertainty. Recommended next steps.}

## Authority Relied On
- {full citation 1} — used at {sections}
- {full citation 2} — used at {sections}

## Open Items
- {Authority needed}
- {Facts to develop}
- {Decisions for partner}
```

---

## Verification

- [ ] Question Presented is one sentence, ends in a question mark, names the jurisdiction or controlling doctrine.
- [ ] Brief Answer is two sentences max with yes/no/probably in the first clause.
- [ ] Statement of Facts contains no facts not supplied by the user.
- [ ] Every cited authority appears in the user's authority list. Missing authority is flagged with `[NEED CITE: ...]`.
- [ ] Each sub-issue has its own complete IRAC pass.
- [ ] Counter-arguments addressed, not avoided.
- [ ] Secondary authority is identified as persuasive, not binding.
- [ ] Conclusion identifies remaining uncertainty and next steps.
- [ ] Citation style matches the requested style (Bluebook by default).
- [ ] No fabricated case names, holdings, or pinpoints.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Question Presented is two sentences or includes the answer | One sentence, ends in `?`, no preview of the answer |
| Brief Answer hedges to the point of meaninglessness | Lead with yes/no/probably; reserve hedging for the Conclusion |
| Statement of Facts smuggles in inferences | Inferences belong in Application; Statement of Facts is descriptive only |
| "Rule" section quotes one case in isolation | Synthesize; if the rule has elements, list them as elements |
| Application restates the rule without applying it | Each element gets a fact tie and a pinpoint |
| Citing a Restatement as if it controls | Restatements are persuasive; identify whether the controlling jurisdiction has adopted the relevant section |
| Treating dicta as holding | Identify dicta as dicta; do not load it as binding |
| Filling in "I think this case held X" without the supplied text | Use `[NEED HOLDING: {case}]` and continue |
| Generating a fake parallel cite or pin | Use only what the user supplied; otherwise flag |
| Using "the court held" when the language is from a concurrence or dissent | Identify the source — majority, plurality, concurrence, dissent |
