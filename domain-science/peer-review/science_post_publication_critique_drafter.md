---
title: "Post-Publication Critique Drafter"
category: science/peer-review
description: "Draft a PubPeer-style critique of a published paper where every concern is anchored to located, checkable evidence, severity-calibrated, framed as a question, and free of ad hominem."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-01
  - CM-02
difficulty: advanced
tags:
  - post-publication-review
  - pubpeer
  - critique
  - research-integrity
  - calibration
  - cope
  - evidence-based
  - good-faith
updated: "2026-06-26"
related_prompts:
  - domain-science/peer-review/science_peer_review_drafter.md
  - domain-science/peer-review/science_review_disagreement_arbitration_memo.md
  - domain-science/peer-review/science_review_for_replication_or_robustness.md
  - domain-science/ethics-integrity/science_misconduct_self_audit.md
---

# Post-Publication Critique Drafter

**Objective:** Help a reader draft a constructive, public post-publication critique (PubPeer-style) of a published paper. Every concern must be anchored to specific, located evidence, calibrated for severity, and phrased as a question inviting author response. Where a concern could indicate misconduct, observations are stated factually and routed to the appropriate process rather than asserted as accusation.

**When to use:** You have read a published paper, hold one or more concrete, checkable concerns about its data, figures, methods, statistics, or claims, and want to articulate them publicly and responsibly.

**Required inputs:**
- **Discipline.** Field and subfield of the target paper.
- **Study type.** Observational / experimental / computational / theoretical / meta-analytic / mixed.
- **Target paper.** Title, authors as listed, venue, year, and DOI `[user-supplied]`; the relevant passages, figures, tables, and statistics you are critiquing.
- **Your concern(s).** A plain-language statement of what looks wrong and where.

**Optional inputs:**
- The reporting checklist or preregistration the paper claims to follow.
- Public data/code links, if available.
- Prior comments, errata, or corrections already attached to the paper.
- Your relevant expertise and any competing interest to disclose.

**Constraints — Must:**
- Anchor every concern to a precisely located object: figure panel, table cell, equation, page/paragraph, or a specific reported statistic.
- Calibrate severity for each concern: cosmetic/typo, interpretive overreach, methodological weakness, or integrity-relevant anomaly.
- Default to assuming honest error over misconduct; phrase concerns as questions or requests for clarification that a good-faith author could answer.
- Distinguish confirmatory from exploratory claims, and correlation from causation, when assessing whether a conclusion is supported.
- Apply an Open-Science lens: where data/code/preregistration would resolve a concern, say so and request it.
- Follow responsible post-publication-critique norms (PubPeer: public, evidence-based, civil): factual, specific, and verifiable by any reader.
- For potential-misconduct observations (e.g., apparent image duplication, statistically impossible values), state only what is observable and route to the journal/institution/COPE process; cite `domain-science/ethics-integrity/`.

**Constraints — Must Not:**
- Do not invent citations, data, or facts not supplied. If a claim needs a reference, mark `[user-supplied]` or phrase it as a verifiable question. No ad hominem; critique the work, not the authors.
- Do not assert intent, fraud, or misconduct as a conclusion; do not name motive.
- Do not use the banned hype/derision register — no "novel," "groundbreaking," "first-ever," "gold standard," nor mirror-image sneers ("sloppy," "incompetent").
- Do not generalize from one located issue to a verdict on the authors' whole body of work.
- Do not publish a concern you cannot point another reader to and have them verify.

**Instructions:**

1. **Anchor the target precisely.** Record the paper's identifiers `[user-supplied]` and pin each concern to a located object (Fig 2B, Table 3 row 4, p. 6 ¶2, "F(2,57)=...").
2. **Restate the authors' claim faithfully.** Before critiquing, state what the authors actually conclude at that location, so the concern targets the real claim, not a strawman.
3. **State the observation.** Describe what you see, factually and reproducibly, with no interpretation yet (e.g., "the error bars in panels A and C appear identical to the pixel").
4. **Supply the evidence.** Show the checkable basis: the numbers, the visual feature, the inconsistency between text and table, the assumption violated. If a check requires the raw data or code, request it rather than assuming the result.
5. **Explain why it matters and to what degree.** Tie the observation to the conclusion it threatens, and rate severity. Separate "this weakens an exploratory claim" from "this invalidates the headline result."
6. **Calibrate honest-error vs integrity (RT-01 reasoning).** Reason explicitly about benign explanations first. Only if the anomaly resists benign explanation, mark it integrity-relevant and route it; never accuse.
7. **Convert each concern into a question.** Phrase as a clarification request a good-faith author can answer (e.g., "Could the authors confirm whether panels A and C share a source image, and if so, clarify the labeling?").
8. **Self-check before posting (QA-01).** Verify each concern is located, evidence-backed, severity-rated, and ad-hominem-free; remove any point you cannot have a stranger reproduce.
9. **Assemble and disclose.** Order concerns by severity, add a one-line competing-interest disclosure, and append the routing note for any integrity-relevant items.

**Output format (locked):**

```
## Target Paper
[Title; authors as listed; venue; year; DOI [user-supplied]]

## Disclosure
[Relevant expertise; competing interest, or "none declared"]

## Concerns (most to least severe)
### Concern 1 — [severity: cosmetic | interpretive | methodological | integrity-relevant]
- **Location:** [Fig/Table/§/stat]
- **Authors' claim here:** [faithful restatement]
- **Observation:** [factual, no interpretation]
- **Evidence:** [checkable basis]
- **Why it matters:** [conclusion threatened + degree; confirmatory vs exploratory]
- **Question / requested clarification:** [good-faith, answerable]
[repeat per concern]

## Open-Science Requests
[Specific data/code/preregistration that would resolve concerns]

## Integrity Routing (if any concern is integrity-relevant)
[Factual observation only + the appropriate journal/institution/COPE channel; no accusation of intent]
```

**Reporting-standard alignment:** Responsible post-publication-critique norms (PubPeer guidelines: public, evidence-based, civil); COPE guidance on handling concerns about published research and on errors vs misconduct; EQUATOR reporting checklist for the study type, where the concern is incomplete reporting.

**Verification checklist (before delivering):**
- [ ] Discipline and study type were captured before drafting.
- [ ] Every concern is pinned to a precise, named location another reader can find.
- [ ] Each concern carries an explicit severity rating.
- [ ] Benign/honest-error explanations were considered before any integrity flag.
- [ ] Every concern is phrased as an answerable question, not an accusation.
- [ ] No fabricated citations/data; identifiers and any needed references marked `[user-supplied]`.
- [ ] Banned hype/derision terms are absent; no motive or intent is asserted.
- [ ] Integrity-relevant items are routed, with factual observations only, and never assert fraud.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Misconduct leap | An image/stat anomaly is presented as proof of fraud | State only what is observable; consider honest error first; route, never accuse intent |
| Unlocated grievance | A general complaint ("the stats are wrong") with no anchor | Require a figure/table/stat/page pin a stranger can verify before it ships |
| Severity inflation | A cosmetic or interpretive quibble framed as fatal | Rate severity explicitly; separate weakening from invalidating |
| Strawman target | Critiquing a claim the authors did not actually make | Restate the authors' claim faithfully at the location before the observation |
| Hidden hype/derision | Polite-sounding text still carries "sloppy" or "groundbreaking" | Lexical scrub against the banned register; neutral, located language only |
| Correlation/causation slip | Faulting (or excusing) a causal claim without checking design | Re-derive admissible claims from the study type; observational ≠ causal |
| Reference fabrication | Bolstering a concern with a plausible but unverified citation | Mark `[user-supplied]` or pose as a checkable question; never assert from memory |
