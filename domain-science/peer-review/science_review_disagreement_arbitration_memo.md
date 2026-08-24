---
title: "Review Disagreement Arbitration Memo"
category: science/peer-review
description: "Adjudicate two strongly divergent peer reviews into a single evidence-weighted editorial recommendation that resolves the genuine crux rather than splitting the difference."
techniques:
  - ST-01
  - RT-01
  - QA-02
  - CM-02
  - NE-10
difficulty: advanced
tags:
  - peer-review
  - editorial-decision
  - reviewer-disagreement
  - associate-editor
  - arbitration
  - cope
  - evidence-weighting
  - calibration
updated: "2026-06-26"
related_prompts:
  - domain-science/peer-review/science_peer_review_drafter.md
  - domain-science/peer-review/science_post_publication_critique_drafter.md
  - domain-science/peer-review/science_review_for_replication_or_robustness.md
  - domain-science/methods-foundations/science_replicability_premortem.md
---

# Review Disagreement Arbitration Memo

**Objective:** Help an Associate Editor (AE) or invited third reviewer arbitrate a manuscript where two prior reviews diverge strongly (e.g., one Accept/Minor, one Reject). The memo maps each reviewer's claims to evidentiary strength, isolates the true crux of disagreement, weighs which concerns are decision-relevant, and produces a reasoned recommendation. It must reach a defensible decision rather than mechanically averaging the two reviews.

**When to use:** Two completed reviews of the same manuscript are in hand and their recommendations or substantive judgments materially conflict, and you must produce an editorial recommendation or third-reviewer memo.

**Required inputs:**
- **Discipline.** Field and subfield (e.g., cognitive psychology, materials chemistry, health economics).
- **Study type.** Observational / experimental / computational / theoretical / meta-analytic / mixed.
- **Manuscript summary.** Core claim(s), methods, and headline results as the authors state them.
- **Reviewer A's report.** Full text or faithful summary, with stated recommendation.
- **Reviewer B's report.** Full text or faithful summary, with stated recommendation.

**Optional inputs:**
- Journal scope, acceptance bar, and section (e.g., Letters vs full Articles).
- Reviewer expertise hints (statistician, domain expert, methods specialist).
- Author response or rebuttal, if this is a later round.
- Reporting checklist or registered-report stage, if relevant.

**Constraints — Must:**
- Treat the memo as confidential editorial work product consistent with COPE peer-review and editor guidelines; preserve reviewer and author confidentiality.
- Classify every reviewer claim as substantiated (located, evidence-backed), matter-of-taste/preference, or scope-creep (a demand beyond the paper's stated claims or the journal's bar).
- Distinguish fatal flaws (invalidate the central claim) from degree concerns (weaken, qualify, or require revision).
- Distinguish confirmatory from exploratory framing, and correlation from causation, when weighing whether a concern is decision-relevant.
- Identify the single genuine crux: is the disagreement about validity, importance/novelty-of-contribution, scope/fit, or interpretation?
- Apply an Open-Science lens: note whether data/code availability, preregistration, or reporting transparency is a live point of contention between the reviewers.
- Use probability-weighted language (NE-10) where the evidence is incomplete (e.g., "≈70% this is a genuine confound, ≈30% an artifact of presentation").

**Constraints — Must Not:**
- Do not invent citations, data, or facts not supplied. If a claim needs a reference, mark `[user-supplied]` or phrase it as a verifiable question. No ad hominem; critique the work and the reviews, not the people.
- Do not resolve the conflict by averaging or "splitting the difference" without a stated evidentiary reason.
- Do not defer to the more senior, more confident, or more verbose reviewer; weight by evidence, not tone.
- Do not import your own new objections as if they were reviewer concerns — flag any editor-originated point separately.
- Do not treat reviewer disagreement as automatic grounds for rejection or for a third review without justifying the need.

**Instructions:**

1. **Restate the manuscript's central claim and bar.** In one or two sentences, state what the paper asserts and what threshold the journal/section requires for acceptance. The decision hinges on whether concerns threaten *that* claim against *that* bar.
2. **Extract every distinct claim from each review.** List Reviewer A's and Reviewer B's points atomically. Merge duplicates; do not lose minority points buried in a positive review.
3. **Classify each claim.** Tag as substantiated / taste / scope-creep, and as fatal / degree / cosmetic. Locate substantiated claims to a specific section, figure, table, or statistic where possible.
4. **Find the crux.** Determine whether the reviewers actually disagree on facts, or are applying different standards (importance, fit, interpretation). Name the crux explicitly; most strong disagreements reduce to one or two load-bearing points.
5. **Adjudicate the crux on evidence.** For the load-bearing point(s), reason step by step about which reviewer's position the manuscript's content supports. Where evidence is incomplete, assign probability-weighted plausibility to each position and state what would resolve it.
6. **Weigh decision-relevance.** Separate concerns that change the verdict from those that are addressable in revision. A single fatal, substantiated, unaddressable flaw outweighs many cosmetic agreements.
7. **Stress-test your own leaning (QA-02).** Argue the opposite recommendation for one paragraph. If it survives, downgrade your confidence and consider a targeted third review or a major-revision-with-conditions path.
8. **Draft the recommendation.** State a verdict (Accept / Minor / Major / Reject / third review needed) with the conditions that must be met, mapped to the substantiated concerns. If recommending a third reviewer, specify the exact expertise and the exact question they should resolve.
9. **Write author- and reviewer-facing notes.** Provide a short, neutral synthesis the editor can adapt for the decision letter, and a private note on how reviewer credit/weighting was handled.

**Output format (locked):**

```
## Manuscript & Bar
[Central claim; journal/section acceptance threshold]

## Crux of Disagreement
[Validity | Importance | Scope/Fit | Interpretation] — [one-sentence statement of the load-bearing point]

## Claim-by-Claim Adjudication
| # | Reviewer | Claim (located) | Type (substantiated/taste/scope-creep) | Severity (fatal/degree/cosmetic) | Manuscript support | Decision-relevant? | Confidence |
|---|---|---|---|---|---|---|---|
| 1 | A | ... (§/Fig/Tbl) | ... | ... | ... | Yes/No | ~XX% |

## Open-Science Points in Dispute
[Data/code availability, preregistration, reporting transparency — if contested]

## Reasoned Recommendation
[Verdict + conditions mapped to substantiated concerns. State explicitly why this is NOT a split-the-difference outcome.]

## If a Third Review Is Needed
[Exact expertise required + the single question it must answer]

## Editor-Facing Synthesis (adaptable for decision letter)
[Neutral, non-ad-hominem summary]

## Confidence & What Would Change It
[Probability-weighted; named tripwires]
```

**Reporting-standard alignment:** COPE Ethical Guidelines for Peer Reviewers and COPE Core Practices (editorial decisions); ICMJE recommendations on editorial responsibility; EQUATOR/relevant reporting checklist where a reviewer's concern is about reporting completeness.

**Verification checklist (before delivering):**
- [ ] Discipline and study type were captured before adjudication.
- [ ] Every reviewer claim is listed atomically and located to a section/figure/stat where substantiated.
- [ ] Each claim is classified by type and severity; fatal vs degree is explicit.
- [ ] The single crux is named and categorized (validity/importance/scope/interpretation).
- [ ] The recommendation resolves the crux on evidence and explicitly is not an average of the two reviews.
- [ ] Probability-weighted language is used wherever evidence is incomplete.
- [ ] No fabricated citations/data; unsupported needs are marked `[user-supplied]` or posed as questions.
- [ ] Language is calibrated and non-ad-hominem; the banned hype terms do not appear in drafted text.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Deferring to confidence/seniority | The more forceful or senior reviewer's verdict is adopted as the "expert" one | Weight by located evidence, not tone or rank; require manuscript support for each adopted claim |
| Splitting the difference | "Major revision" chosen only to placate both reviewers | Verdict must map to substantiated concerns; state the evidentiary reason it is not an average |
| Scope-creep dressed as rigor | A reviewer demands experiments beyond the paper's claim, framed as a fatal gap | Tag scope-creep explicitly; test demands against the paper's stated claim and the journal's bar |
| Taste mistaken for validity | Stylistic/framing preference treated as a substantive flaw | Classify as taste; exclude from decision-relevance unless it obscures the actual claim |
| Misconduct inference | A data/stat anomaly is read as fraud, escalating the dispute | Describe the anomaly factually; route suspected misconduct to the journal/institution/COPE process, do not accuse |
| Correlation-as-causation carryover | A reviewer's causal critique accepted (or dismissed) without checking design | Re-derive from study type; an observational design cannot license causal claims regardless of reviewer stance |
