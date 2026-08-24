---
title: "Journal Target Selector"
category: science/writing-communication
description: "Match a completed manuscript to 3-5 candidate journals using a scored decision matrix on scope fit, audience, article-type fit, open-access policy, decision speed, and DORA-aware prestige — without asserting any journal metric from memory."
techniques:
  - ST-01
  - ST-03
  - DS-02
  - NE-10
  - QA-01
  - CM-02
difficulty: advanced
tags:
  - journal-selection
  - scope-fit
  - open-access
  - dora
  - predatory-journals
  - think-check-submit
  - publication-strategy
  - decision-matrix
updated: "2026-06-26"
related_prompts:
  - domain-science/writing-communication/science_cover_letter_to_editor.md
  - domain-science/writing-communication/science_response_to_reviewers.md
  - domain-science/writing-communication/science_appeal_to_editor_after_rejection.md
---

# Journal Target Selector

**Objective:** Build a defensible candidate-journal shortlist for a finished (or near-finished) manuscript. Score each candidate on scope/aims fit, target audience, article-type fit, open-access policy and cost, typical decision speed, indexing/discoverability, and prestige — with prestige explicitly down-weighted per DORA. Every journal-specific fact must be user-supplied or flagged for verification; the prompt never asserts impact factors, APCs, acceptance rates, or decision times from memory.

**When to use:** After you have a manuscript draft and a sense of its core claim and article type, and you need to choose where to submit (or where to submit next after a rejection).

**Required inputs:**
- **Discipline.** The field and sub-field of the work.
- **Manuscript / finding context.** The core question, the main finding(s), and whether the central claim is confirmatory or exploratory (user-supplied; never invented).
- **Target venue or audience.** Who should read this (specialists vs broad readership; practitioners vs theorists) and any journals already on your list.
- **Article type.** Original research, methods, review, short report, registered report, data paper, case study, etc.
- **Candidate journal facts.** For each journal you want scored: its aims/scope statement, OA model and APC, typical decision timeline, and indexing — each marked `[user-supplied]` if you have it, or left for verification.

**Optional inputs:**
- Constraints: budget cap for APC, funder OA mandate (e.g., Plan S / cOAlition S), embargo limits, time-to-decision pressure, prior rejections to avoid re-treading.
- Preprint already posted (server + DOI) and any preprint policy concerns.
- Co-author preferences or institutional reporting requirements.

**Constraints — Must:**
- Score scope/aims fit primarily from the journal's own aims-and-scope text (user-supplied); treat scope mismatch as a near-disqualifier regardless of prestige.
- Apply DORA: do not let journal-level metrics (impact factor) dominate ranking; weight fit-to-content and audience above prestige.
- Run a predatory-journal screen (Think-Check-Submit) before any journal enters the shortlist.
- Present the matrix and ranking transparently with the weights stated, so the user can re-weight.

**Constraints — Must Not:**
- Do not invent results, citations, DOIs, journal metrics (impact factor, acceptance rate, decision times), editor names, or reviewer text. Draft only from user-supplied content; mark gaps `[user-supplied]` or "verify on the journal site".
- Do not assert a journal's impact factor, APC, acceptance rate, or median decision time from memory — these change and must be verified on the journal's current pages.
- Do not recommend a journal solely because of prestige or because the user "aimed high"; scope and audience fit govern.
- Do not endorse a journal that fails the Think-Check-Submit screen.

**Instructions:**

1. **Restate the manuscript profile.** Summarize the core question, main finding, confirmatory-vs-exploratory status, and article type in 3-4 lines from user input only. Flag if the central claim is exploratory so significance is not oversold downstream.
2. **Define the audience target.** State explicitly who needs to read this and at what breadth. This sets the fit criteria; a finding for a narrow specialist community is mis-served by a broad-readership venue and vice versa.
3. **Assemble the candidate set.** Take the user's named journals plus any obvious siblings the user supplies scope text for. For each, mark which facts are supplied vs need verification. Do not add journals whose scope you cannot evaluate from supplied text.
4. **Predatory / quality screen (Think-Check-Submit).** For each candidate, check: do you/colleagues know the journal; is the editorial board and contact information transparent; is the peer-review process described; is it indexed in the databases you'd expect; are fees clear and stated before acceptance; is it listed in DOAJ (for OA) or recognized indexes. Drop or flag any that fail.
5. **Score the matrix.** Rate each surviving candidate 1-5 on: (a) scope/aims fit, (b) audience match, (c) article-type fit, (d) OA policy + cost fit to mandate/budget, (e) decision speed fit to timeline, (f) indexing/discoverability, (g) prestige (DORA-capped weight). State the weights; default to highest weight on scope, audience, and article-type fit.
6. **Probability-weighted outlook.** For the top candidates, give a qualitative best-/middle-/worst-case framing of likely outcome based on fit (not on invented acceptance rates) — e.g., "strong scope fit but breadth may push toward a 'better suited to a specialist journal' desk decision."
7. **Rank and justify the best fit.** Produce a ranked shortlist of 3-5 with a single-paragraph rationale for the #1 choice tied to scope and audience.
8. **Fallback ladder.** Sequence the shortlist as a submission ladder (where to go if #1 desk-rejects), noting any reformatting cost between tiers and any portable-review / cascade options the user mentions.
9. **Flag verification actions.** List every journal-specific fact the user must confirm on the journal site before submitting.

**Output format (locked):**

```
## Manuscript Profile
[core question; main finding; confirmatory/exploratory; article type]

## Audience Target
[who must read this; breadth]

## Quality Screen (Think-Check-Submit)
| Journal | Known? | Transparent board/process? | Indexed/DOAJ? | Fees clear? | Verdict |
|---|---|---|---|---|---|

## Decision Matrix (weights stated)
Weights: scope __ | audience __ | article-type __ | OA/cost __ | speed __ | indexing __ | prestige (DORA-capped) __
| Journal | Scope | Audience | Type | OA/Cost | Speed | Indexing | Prestige | Weighted total | Facts to verify |
|---|---|---|---|---|---|---|---|---|---|

## Ranked Shortlist (3-5)
1. [journal] — best-fit rationale (scope + audience)
2. ...

## Outlook (probability-weighted, qualitative)
[best / middle / worst framing for top candidates]

## Fallback Ladder
[submission sequence + reformatting/cascade notes]

## Verification Actions (before submitting)
- [ ] [journal-specific facts to confirm on the journal site]
```

**Reporting-standard / convention alignment:** DORA (San Francisco Declaration on Research Assessment — do not over-rely on journal impact factor); Think-Check-Submit (predatory-journal screening); DOAJ and recognized indexing databases; journal aims-and-scope pages; funder OA policy (e.g., Plan S / cOAlition S) where the user supplies a mandate.

**Verification checklist (before delivering):**
- [ ] Discipline, finding context, and audience target are all captured from user input.
- [ ] No impact factor, APC, acceptance rate, or decision time is asserted from memory; all are `[user-supplied]` or marked for verification.
- [ ] Every shortlisted journal passed (or was explicitly flagged in) the Think-Check-Submit screen.
- [ ] Scope/aims fit is scored from the journal's own scope text, not from reputation.
- [ ] Matrix weights are stated and DORA-capped on prestige.
- [ ] Confirmatory-vs-exploratory status of the finding is carried into the outlook.
- [ ] Shortlist is 3-5 with a single best-fit rationale and a fallback ladder.
- [ ] A verification-actions list is included.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Prestige capture | A high-IF journal tops the list despite weak scope fit | DORA cap on prestige weight; scope is a near-disqualifier |
| Stale metrics | An APC or decision time cited confidently but outdated/wrong | Never assert from memory; mark `[user-supplied]`/verify on site |
| Predatory miss | A journal looks legitimate (clean site, fast decision) but isn't indexed | Think-Check-Submit + DOAJ/index check required before shortlisting |
| Audience mismatch | Strong topical fit to a broad journal that serves the wrong readers | Score audience match separately from scope |
| Hidden reformat cost | Fallback ladder ignores cost of converting between formats | Note reformatting/cascade cost between tiers |
