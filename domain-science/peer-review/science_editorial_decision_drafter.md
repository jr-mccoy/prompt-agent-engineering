---
title: "Editorial Decision Drafter"
category: science/peer-review
description: "Draft an editor's decision letter that synthesizes divergent reviewer reports with the editor's own assessment, adjudicates disagreement rather than averaging it, separates must-fix from optional, and sets a clear, justified decision with an actionable path for authors."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - NE-10
  - CM-02
difficulty: advanced
tags:
  - editorial-decision
  - decision-letter
  - reviewer-synthesis
  - cope
  - peer-review
  - manuscript-disposition
  - constructive-feedback
  - editorial-process
updated: "2026-06-26"
related_prompts:
  - domain-science/peer-review/science_peer_review_drafter.md
  - domain-science/peer-review/science_peer_review_self_check.md
  - domain-science/writing-communication/science_response_to_reviewers.md
  - domain-science/methods-foundations/science_threats_to_validity_walkthrough.md
  - domain-science/statistics/science_statistical_results_interpreter.md
---

# Editorial Decision Drafter

**Objective:** Draft a handling editor's decision letter that integrates two or more reviewer reports — which may disagree — together with the editor's own read of the manuscript. The letter must summarize areas of consensus, actively adjudicate genuine disagreement (weighing evidence, not averaging recommendations), separate must-fix issues from optional suggestions, state a clear decision with a reasoned rationale, and give the authors a concrete, actionable revision path. The tone is professional, specific, and COPE-aligned.

**When to use:** You are the handling editor (or simulating that role) and have the reviewer reports in hand and a manuscript-level judgment to render. Use after reviews are complete and any reviewer COI has been cleared.

**Required inputs:**
- **Discipline.** Field and subfield of the manuscript.
- **Study type.** Observational / experimental / RCT / computational / theoretical / systematic review / meta-analysis / qualitative / mixed-methods.
- **Reviewer reports.** The text or substance of each review (at least the major concerns and recommendation from each). Provide the editor's own assessment if available.

**Optional inputs:**
- The journal's recommendation categories, scope, and decision-policy `[user-supplied]`.
- The manuscript abstract/claims for the editor's independent read.
- Any reviewer COI notes or confidential editor comments already prepared.
- Whether the venue permits transparent/open review (affects what is shared).

**Constraints — Must:**
- Follow the COPE Ethical Guidelines (editor responsibilities): decisions are based on the manuscript's merit and validity, are free of bias, respect confidentiality, and give authors a fair, constructive account of the basis for the decision.
- Synthesize — do not merely concatenate or average — the reviews: identify consensus, then adjudicate each genuine disagreement by weighing the evidentiary basis each reviewer gave.
- Where reviewers conflict, weigh the competing positions explicitly (a probability-weighted, evidence-based judgment of which concern is decisive), and state the editor's resolution and reasoning.
- Separate **must-fix** (conditions for any acceptance) from **optional/suggested** improvements.
- Anchor the editor's own points to manuscript locations or reporting-standard items, mirroring reviewer evidence where it is cited.
- State one clear decision from standard categories — accept / minor revision / major revision / reject — with a rationale that follows from the synthesis.
- Keep author-facing content and any confidential editor-only notes separate.

**Constraints — Must Not:**
- Do not invent reviewer content, citations, data, or manuscript facts; synthesize only what is supplied. If a needed policy or fact is unavailable, mark it `[user-supplied]`.
- Do not resolve disagreement by vote-counting or by averaging recommendations; adjudicate on evidence.
- Do not pass hostile or ad hominem reviewer language to authors; reframe it constructively or move it to editor-only notes.
- Do not use promotional language in the drafted letter — ban "novel," "groundbreaking," "first-ever," and "gold standard."
- Do not transmit confidential comments-to-editor to authors, and do not breach reviewer anonymity where the venue is single/double-anonymized.

**Instructions:**

1. **State context.** Record discipline and study type, the number of reviews, and each reviewer's recommendation; confirm COPE governs the decision.
2. **Extract claims from each review.** For each reviewer, list their major concerns and the evidentiary basis each gave, plus their recommendation. Note where the editor's own read agrees or differs.
3. **Map consensus.** Identify concerns and judgments shared across reviewers and the editor; these become the spine of the letter.
4. **Adjudicate disagreement.** For each genuine conflict, weigh the competing positions by the strength of evidence each rests on (a probability-weighted judgment of which concern actually threatens the conclusions), incorporate the editor's independent read, and state a resolution with reasoning. Do not average.
5. **Triage to must-fix vs optional.** Convert the synthesized concerns into a must-fix list (conditions of acceptance) and an optional/suggested list, each item actionable and located.
6. **Render the decision.** Choose accept / minor revision / major revision / reject; justify it from the consensus + adjudication, not from a tally of recommendations.
7. **Write the actionable path for authors.** Give clear, ordered guidance on what a successful revision must address, what is at the authors' discretion, and (if revision) what the resubmission should include (e.g., point-by-point response).
8. **Draft confidential editor-only notes.** Capture reviewer COI, anonymity handling, decisive reasoning, and anything not appropriate for the author-facing letter.
9. **Assemble the letter** in the locked format, professional and specific throughout.

**Output format (locked):**

```
## Decision Context (editor-internal header)
- Discipline / study type: [...]
- Reviews received: [n] — recommendations: R1 [...], R2 [...], ...
- Editor's independent read: [summary]

## Decision Letter to Authors

Dear Authors,

[1–2 sentence framing of the decision and appreciation of the submission — calibrated, no promotional terms]

### Summary of Reviewer Consensus
[Shared concerns and points of agreement across reviewers and the editor]

### Adjudication of Divergent Points
- Disagreement: [topic] — R[x] holds […based on…]; R[y] holds […based on…].
  - Editor's resolution: [which concern is decisive and why — evidence, not vote]
- ...

### Required Revisions (must-fix — conditions for acceptance)
1. [Located, actionable item]
2. ...

### Suggested Revisions (optional)
1. [Located, actionable item]
2. ...

### Decision
[Accept | Minor revision | Major revision | Reject] — [rationale from synthesis]

### Path Forward
[What a successful revision must address; resubmission requirements, e.g., point-by-point response; timeline if [user-supplied]]

Sincerely,
[Handling Editor]

## Confidential Editor-Only Notes
[Reviewer COI, anonymity handling, decisive reasoning, items withheld from authors]
```

**Reporting-standard alignment:** COPE Ethical Guidelines (editor responsibilities and decision integrity); ICMJE recommendations on editorial decisions and confidentiality; the EQUATOR reporting checklist for the study type (CONSORT/STROBE/PRISMA/ARRIVE) as the anchor for must-fix methodological items; TOP guidelines for any Open-Science conditions placed on the authors.

**Verification checklist (before delivering):**
- [ ] Discipline, study type, and each reviewer's recommendation are recorded internally.
- [ ] The letter synthesizes (not concatenates) the reviews; consensus is identified.
- [ ] Each genuine disagreement is adjudicated on evidence, with the editor's resolution stated — no averaging or vote-counting.
- [ ] Must-fix and optional items are separated, each located and actionable.
- [ ] One clear decision is stated with a rationale that follows from the synthesis.
- [ ] No invented reviewer content, citations, data, or manuscript facts; unavailable policy marked `[user-supplied]`.
- [ ] Author-facing text and confidential editor notes are separate; reviewer anonymity preserved; no hostile language passed through.
- [ ] No banned promotional terms appear in the drafted letter.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Averaging recommendations | "Two reviewers said minor, one said reject, so: major revision" with no reasoning | Adjudicate on evidentiary strength of the decisive concern, not on the tally |
| Concatenation masquerading as synthesis | Letter that just lists each reviewer's comments back-to-back | Require an explicit consensus section and an explicit adjudication of each conflict |
| Leaking confidential content | Reviewer-to-editor remarks or anonymity-breaking detail reaching authors | Keep editor-only notes separate; scrub identifying detail from the author letter |
| Inventing the editor's evidence | Asserting manuscript facts or citations not supplied to bolster the decision | Anchor only to supplied content; mark gaps `[user-supplied]` or as author queries |
| Passing through hostility | Verbatim dismissive reviewer phrasing in the author letter | Reframe constructively or relocate to editor-only notes |
