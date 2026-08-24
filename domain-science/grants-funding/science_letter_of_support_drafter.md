---
title: "Letter of Support Drafter"
category: science/grants-funding
description: "Draft a collaborator, consultant, or institutional/chair letter of support that states specific, checkable commitments (named resources, samples, access, instrument time, mentoring, data) tailored to the proposal — not generic praise — then audit every sentence for whether it is a real commitment or empty filler."
techniques:
  - ST-01
  - ST-03
  - RT-03
  - QA-01
  - QA-02
  - CM-02
difficulty: advanced
tags:
  - nih
  - nsf
  - letter-of-support
  - collaborator-commitment
  - institutional-commitment
  - chair-letter
  - grant-writing
  - research-funding
updated: "2026-06-26"
related_prompts:
  - domain-science/grants-funding/science_specific_aims_drafter.md
  - domain-science/grants-funding/science_grant_budget_justification_drafter.md
  - domain-science/grants-funding/science_grant_resubmission_response.md
---

# Letter of Support Drafter

**Objective:** Draft a letter of support written from the signatory's perspective that states specific, concrete commitments — named resources, samples, datasets, instrument or facility time, access, mentoring hours, personnel — matched to what the proposal actually needs. Then audit the letter sentence by sentence: each line is either a checkable commitment or empty praise, and praise without commitment is flagged for removal or conversion.

**When to use:** Your application needs a letter of support from a collaborator, a paid/unpaid consultant, a core facility, an institutional official, or a department chair, and you want a draft the signatory can review, edit, and sign rather than generic boilerplate.

**Required inputs:**
- **Discipline.** The scientific field of the proposal.
- **Study type.** Observational / experimental / computational / mixed — shapes what resources/access matter.
- **Letter type.** Collaborator vs. consultant vs. institutional/chair vs. core-facility/resource letter — these differ in what they should commit.
- **What the proposal needs from this signatory.** The specific resource, access, sample, dataset, instrument time, expertise, mentoring, or space the application depends on, and the aim(s) it supports.
- **The actual commitment.** What the signatory is genuinely promising — quantities, durations, conditions — all `[user-supplied]` (never invent what someone is promising).

**Optional inputs:**
- **Signatory details.** Name, title, institution, relationship to the PI/project (`[user-supplied]`).
- **Funder letter conventions.** Whether the funder wants letters of support vs. letters of collaboration with prescribed language (`[user-supplied]`/verify against the FOA or solicitation).
- **Effort or budget linkage.** If the signatory has committed effort or a subaward, so the letter and budget justification agree.

**Constraints — Must:**
- Write from the signatory's voice and point of view, committing only what the user reports the signatory has actually agreed to provide.
- Make every commitment specific and checkable: name the resource, quantify it (how much, how long, under what conditions), and tie it to the aim it supports.
- Tailor the letter type: a collaborator letter commits to joint scientific work and shared responsibility; a consultant letter commits defined advice/services (and notes compensation if applicable); an institutional/chair letter commits institutional resources (space, protected time, startup, shared equipment) and endorses feasibility; a core-facility letter commits access, rates, and prioritization.
- Keep effort and budget claims consistent with the budget justification if effort/subaward details are supplied.
- Require the signatory to review and approve the draft before submission (state this explicitly to the user).

**Constraints — Must Not:**
- Do not invent citations, summary-statement critiques, personnel, effort percentages, costs, institutional commitments, or signatory names. If needed and not supplied, mark `[user-supplied]` and ask; the prompt drafts from the user's actual reported commitments, never fabricates them.
- Do not promise resources, access, samples, effort, or institutional support the user did not report as actually committed.
- Do not pad the letter with generic praise of the PI's brilliance or the project's importance in place of commitments.
- Do not use "novel," "groundbreaking," "first-ever," or "gold standard" filler in drafted text.
- Do not state quantities, durations, rates, or conditions the user did not supply — mark them `[user-supplied]`.

**Instructions:**

1. **Intake and gate.** Confirm discipline, study type, letter type, what the proposal needs from this signatory, and what the signatory has actually committed. Missing commitment details are `[user-supplied]` — do not invent them.
2. **Match need to commitment.** For each thing the proposal needs from this signatory, confirm there is a corresponding user-supplied commitment. Flag any need with no commitment, and any commitment that doesn't map to a stated need.
3. **Select the letter frame.** Apply the structure for the letter type (collaborator / consultant / institutional-chair / core-facility) so the commitments are the right kind for the relationship.
4. **Draft the opening.** From the signatory's voice: who they are, their relationship to the project, and a one-line statement of what they are committing.
5. **Draft the commitment body.** State each commitment specifically and quantitatively (resource, amount, duration, conditions) and tie it to the aim(s) it enables. Where applicable, reference consistency with the budget (effort/subaward) — `[user-supplied]`.
6. **Draft the close.** A brief, credible statement of enthusiasm grounded in the commitments made — not free-floating praise.
7. **Specific-commitment audit.** Go sentence by sentence: classify each as a checkable commitment or empty praise. Flag empty-praise sentences for deletion or conversion into a concrete commitment.
8. **Consistency and approval pass.** Confirm commitments align with any supplied effort/budget, that nothing exceeds what the user reported, and remind the user the named signatory must review and sign.

**Output format (locked):**

```
## Letter of Support (draft — for [signatory] to review and sign)

[Letterhead / date placeholder — [user-supplied]]

Dear [Review Panel / Program Officer — [user-supplied]],

[Opening: signatory identity, relationship to the project, one-line statement of what is committed.]

[Commitment body: each commitment stated specifically — resource, quantity, duration, conditions — and tied to the aim(s) it enables. Reference budget/effort consistency where applicable ([user-supplied]).]

[Close: enthusiasm grounded in the specific commitments above.]

Sincerely,
[Name, Title, Institution — [user-supplied]]

## Need → Commitment Map
| Proposal need | Aim(s) | Committed? | Specific commitment (quantity/duration/conditions) |
|---|---|---|---|
| [...] | [...] | yes / not committed — flag | [user-supplied details] |

## Specific-Commitment Audit
| Sentence (paraphrased) | Checkable commitment or empty praise? | Action |
|---|---|---|
| [...] | commitment / praise | keep / delete / convert to commitment |

## Letter-Type Fit
- Type: [collaborator / consultant / institutional-chair / core-facility].
- Commits the right kind of support for this relationship: [yes / fix].
- Budget/effort consistency: [aligned / [user-supplied] / N/A].

## Open Items ([user-supplied])
- [Signatory name/title, exact commitment quantities, letterhead, funder letter convention to verify against the FOA/solicitation.]

## Reminder
- The named signatory must review, edit, and sign this letter before submission. Do not submit commitments they have not approved.
```

**Reporting-standard alignment:** Letters-of-support / letters-of-collaboration best practice — specific named commitments (resources, access, samples, instrument time, mentoring, data) from the committer, signed by the person making the commitment, distinguished from generic endorsement. NIH/NSF letter conventions (and any prescribed collaboration-letter language) are `[user-supplied]`/verify against the current FOA or solicitation. Effort and subaward commitments should agree with `science_grant_budget_justification_drafter.md`.

**Verification checklist (before delivering):**
- [ ] Discipline, study type, and letter type captured.
- [ ] Every proposal need from this signatory mapped to a user-supplied commitment (gaps flagged).
- [ ] Each commitment is specific and checkable (resource + quantity + duration + conditions).
- [ ] Letter type frames the right kind of commitment for the relationship.
- [ ] Written in the signatory's voice; commits nothing beyond what the user reported.
- [ ] Specific-commitment audit run; empty-praise sentences flagged.
- [ ] Effort/budget claims consistent with the budget justification (or marked N/A).
- [ ] No fabricated commitments, resources, names, or quantities; all marked `[user-supplied]`.
- [ ] No hype filler in drafted text.
- [ ] Signatory-review-and-sign reminder included.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Invented commitment | "I will provide unlimited access to our patient cohort" the signatory never agreed to | Commit only user-supplied commitments; flag any need without one |
| Praise as substance | A warm paragraph about the PI's excellence with nothing actually committed | Specific-commitment audit flags empty-praise sentences for deletion/conversion |
| Wrong letter type | A core-facility letter that endorses the science but never commits instrument time | Letter-type fit check: commit the kind of support the relationship implies |
| Quantities from memory | "20% effort and 200 hours of instrument time" not supplied by the user | All quantities/durations/conditions are `[user-supplied]`; never assert them |
| Budget mismatch | Letter implies effort the budget justification doesn't reflect | Consistency pass aligns letter commitments with supplied effort/subaward details |
| Unsigned overreach | Drafting and treating as final without signatory approval | Explicit reminder that the named signatory must review and sign before submission |
