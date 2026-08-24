---
title: "Point-by-Point Response to Reviewers"
category: science/writing-communication
description: "Produce a traceable, non-defensive point-by-point response that quotes each reviewer comment and classifies the action as acceded, argued, or partial — with a change log mapping every comment to a manuscript edit and a remaining-disagreements summary for the editor."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-02
  - CM-02
difficulty: advanced
tags:
  - peer-review
  - response-to-reviewers
  - revision
  - change-log
  - cope
  - rebuttal
  - traceable-edits
  - non-defensive-tone
updated: "2026-06-26"
related_prompts:
  - domain-science/writing-communication/science_cover_letter_to_editor.md
  - domain-science/writing-communication/science_journal_target_selector.md
  - domain-science/writing-communication/science_appeal_to_editor_after_rejection.md
---

# Point-by-Point Response to Reviewers

**Objective:** Turn a reviewer report into a complete, traceable response document. Each comment is quoted verbatim (from the user's supplied report), then answered with a reply that explicitly classifies the action as ACCEDED (changed), ARGUED (respectfully disagree), or PARTIAL — citing the exact manuscript location and the revised text for every change. The output includes a comment-to-edit change log and a remaining-disagreements summary the editor can adjudicate. Tone is professional, non-defensive, and gratitude-calibrated.

**When to use:** After receiving a "revise" decision, when preparing the response letter and revised manuscript.

**Required inputs:**
- **Discipline.** Field and sub-field.
- **Manuscript / finding context.** What the paper claims and the main results (user-supplied; never invented).
- **Target venue or audience.** The journal and the editor's decision letter framing (e.g., major vs minor revision).
- **Reviewer comments.** The verbatim reviewer text, numbered by reviewer and comment (user-supplied). Never paraphrase or invent reviewer wording.
- **Intended actions.** For each comment, what the authors actually did or intend to argue (user-supplied), including the manuscript location and the revised text where a change was made.

**Optional inputs:**
- Editor's specific requests or summary of priorities.
- Constraints (word limits, no new experiments possible, data already locked).
- Co-author disagreements to reconcile before drafting.

**Constraints — Must:**
- Quote each reviewer comment verbatim before responding; preserve numbering.
- Classify every response as ACCEDED, ARGUED, or PARTIAL.
- For every ACCEDED/PARTIAL item, cite the exact manuscript location (section, line/page, figure) and include the revised text (or a `[revised text — user-supplied]` placeholder if not yet written).
- Maintain a change log mapping each comment to its manuscript edit.
- Keep tone non-defensive and gratitude-calibrated (acknowledge once, substantively; not per sentence).

**Constraints — Must Not:**
- Do not invent results, citations, DOIs, journal metrics, editor names, or reviewer text. Draft only from user-supplied content; mark gaps `[user-supplied]`.
- Do not write hollow "we thank the reviewer" replies with no substantive response.
- Do not claim an edit that was not actually made; if a change is only intended, mark it as pending and as a placeholder.
- Do not concede a point that compromises the validity of the work just to please a reviewer; ARGUE with evidence where warranted.
- Do not alter or soften the reviewer's wording when quoting it.

**Instructions:**

1. **Index the report.** From the user's verbatim text, list every comment with a stable ID (R1.1, R1.2, R2.1, ...). Do not merge or reword comments.
2. **Classify intent per comment.** For each, determine from user input whether the action is ACCEDED, ARGUED, or PARTIAL. If the user has not decided, mark `[action — user to decide]`.
3. **Draft acceded responses.** Open with a brief, sincere acknowledgment, state precisely what was changed, cite the exact manuscript location, and quote the revised text (or insert `[revised text — user-supplied]`). Avoid over-thanking.
4. **Draft argued responses.** Respectfully state the disagreement, give the evidence or reasoning, and explain why the manuscript stands as is. Acknowledge the legitimacy of the concern even while disagreeing. No dismissiveness.
5. **Draft partial responses.** State what was changed and what was not, with the rationale for the boundary, and cite locations for the portion that changed.
6. **Build the change log.** Produce a table: comment ID → classification → manuscript location → one-line description of the edit. This is the editor's audit trail.
7. **Summarize remaining disagreements.** Collect all ARGUED (and unresolved PARTIAL) items into a short summary for the editor, framed as points for adjudication, not as defiance.
8. **Tone and gratitude pass.** Scan for hollow thanks, defensiveness, and any claim of an edit not backed by a location. Calibrate: one substantive acknowledgment per reviewer, not per comment.
9. **Self-check (adversarial).** Read as a skeptical reviewer: would they feel heard, and could the editor verify each claimed change from the change log?

**Output format (locked):**

```
## Response to Reviewers — [manuscript title], [journal]

### Summary to the Editor
[2-4 lines: scope of revision; how many acceded/argued/partial; note remaining disagreements]

### Reviewer 1
**Comment R1.1 (verbatim):**
> [reviewer text — user-supplied]
**Response — [ACCEDED | ARGUED | PARTIAL]:**
[substantive reply; for changes: location + revised text or [revised text — user-supplied]]

**Comment R1.2 (verbatim):**
> [...]
**Response — [...]:**
[...]

### Reviewer 2
[same structure]

## Change Log (comment → edit)
| Comment ID | Classification | Manuscript location | Edit description |
|---|---|---|---|

## Remaining Disagreements (for editor adjudication)
- [comment ID] — [concise statement of the unresolved point + evidence]

## Tone & Traceability Check
- [ ] No hollow thanks; one substantive acknowledgment per reviewer
- [ ] Every ACCEDED/PARTIAL item has a location + revised text/placeholder
- [ ] No claimed edit lacks a change-log entry
```

**Reporting-standard / convention alignment:** COPE guidance on peer review and author responses (constructive, evidence-based engagement); ICMJE recommendations (handling of revisions and disclosures); journal author guidelines on response-letter format; transparent reporting (changes traceable to manuscript locations).

**Verification checklist (before delivering):**
- [ ] Discipline, finding context, journal, and verbatim reviewer comments are captured from user input.
- [ ] Every comment is quoted verbatim and given a stable ID.
- [ ] Every response is classified ACCEDED / ARGUED / PARTIAL.
- [ ] Every acceded/partial change cites a manuscript location and includes revised text or a flagged placeholder.
- [ ] No edit is claimed without a matching change-log entry.
- [ ] Argued points carry evidence/reasoning and acknowledge the concern.
- [ ] Tone is non-defensive and gratitude-calibrated (no per-sentence thanks).
- [ ] Remaining disagreements are summarized for the editor.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Hollow courtesy | Every reply opens with thanks but says nothing substantive | Ban hollow thanks; require substantive action per comment |
| Phantom edit | Reply claims "we have revised" but no change was made | Every change needs a location + change-log entry |
| Defensive drift | Argued replies read dismissive or combative | Acknowledge concern; evidence-based, respectful tone |
| Reviewer paraphrase | Comment is reworded, softening the critique | Quote verbatim; never alter reviewer text |
| Over-concession | Author changes valid analysis just to appease | ARGUE with evidence where the work is sound |
| Untraceable claim | Editor cannot verify what changed | Change log maps every comment to an edit |
