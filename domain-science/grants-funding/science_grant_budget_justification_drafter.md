---
title: "Grant Budget Justification Drafter"
category: science/grants-funding
description: "Draft a category-by-category budget justification (personnel/effort, fringe, equipment, supplies, travel, other direct, subawards, indirect/F&A) where every line is justified by the science it serves — then run an internal-consistency check and flag common red flags."
techniques:
  - ST-01
  - ST-03
  - RT-03
  - QA-01
  - QA-02
  - DS-02
difficulty: advanced
tags:
  - nih
  - nsf
  - budget-justification
  - effort-allocation
  - person-months
  - allowability
  - grant-writing
  - research-funding
updated: "2026-06-26"
related_prompts:
  - domain-science/grants-funding/science_specific_aims_drafter.md
  - domain-science/grants-funding/science_grant_approach_section_drafter.md
  - domain-science/grants-funding/science_letter_of_support_drafter.md
---

# Grant Budget Justification Drafter

**Objective:** Draft a budget justification organized by standard cost category in which each line item is justified by the science — why this person at this effort, why this equipment, why this travel — and tied to the specific aim(s) it supports, not merely listed. Then check internal consistency (effort vs. role vs. aims; category totals roll up correctly) and flag the red flags reviewers and grants-management staff commonly catch.

**When to use:** You have a proposed budget (numbers, effort, and costs) and a set of aims, and you need the narrative justification that accompanies the budget pages for a research application.

**Required inputs:**
- **Discipline.** The scientific field.
- **Study type.** Observational / experimental / computational / mixed — this drives what personnel, equipment, and supplies are credible.
- **Mechanism and budget type.** Target mechanism (e.g., NIH R01 modular vs. detailed, NSF) and whether the budget is modular or detailed (`[user-supplied]`); the effort convention (NIH person-months: calendar / academic / summer; NSF academic + summer).
- **The aims.** The aims the budget must serve, so each cost can be mapped to a scientific purpose.
- **Budget figures.** Personnel and their roles, effort (in person-months or % effort), salaries/fringe, equipment, supplies, travel, other direct costs, subawards, and the indirect/F&A rate — all `[user-supplied]`.

**Optional inputs:**
- **Salary cap / institutional rates.** Any applicable salary cap, fringe rate, or negotiated F&A rate (`[user-supplied]`).
- **Period of performance.** Project years, for multi-year escalation and equipment timing.
- **Subaward / consortium details.** Subrecipient scope and budget, if any.

**Constraints — Must:**
- Justify, do not list: every line states why the cost is needed and which aim(s) it serves.
- Express personnel effort in the funder's convention (NIH person-months by type; NSF academic/summer months) and tie each person's effort to their role and the aims they execute.
- Place each cost in the correct category (e.g., a general-purpose computer is typically a supply/other-direct item, not equipment; equipment usually means a unit above the capitalization threshold with a useful life — threshold `[user-supplied]`).
- Apply allowability/allocability/reasonableness as framing concepts (Uniform Guidance) without quoting specific dollar thresholds or rates from memory — those are `[user-supplied]`/verify.
- Run a consistency check: effort sums are plausible per person across all projects (flag if a PI's combined effort would exceed available time), category subtotals roll into the correct totals, and direct vs. indirect are handled correctly (e.g., equipment and the subaward portion above the first threshold are typically excluded from the F&A base — confirm against the institution's rate agreement).

**Constraints — Must Not:**
- Do not invent citations, summary-statement critiques, personnel, effort percentages, costs, institutional commitments, or signatory names. If needed and not supplied, mark `[user-supplied]` and ask; the prompt drafts from the user's actual budget figures, never fabricates them.
- Do not assert salary figures, fringe rates, F&A rates, capitalization thresholds, or salary caps from memory — all `[user-supplied]`/verify against the current rate agreement and funder policy.
- Do not justify effort with circular or empty rationale ("the PI will provide overall leadership" with no tie to aims); require a science-anchored reason.
- Do not move costs between categories to game the indirect base, and do not pad effort beyond what the aims require.
- Do not use "novel," "groundbreaking," "first-ever," or "gold standard" filler in drafted text.

**Instructions:**

1. **Intake and gate.** Confirm discipline, study type, mechanism, budget type (modular/detailed), effort convention, and that the aims and figures are present. Any missing number, rate, or threshold is `[user-supplied]` — do not invent it.
2. **Map costs to aims.** For each proposed line, identify the aim(s) it serves. If a cost serves no aim, flag it for removal or rejustification.
3. **Draft personnel justification.** For each person: role, effort (in the funder's units), and a science-anchored rationale (which aims they execute and why their effort level fits the work). Note key personnel vs. other significant contributors. Mark salary/fringe figures `[user-supplied]`.
4. **Draft non-personnel categories.** Justify equipment (and confirm it meets the capitalization threshold — threshold `[user-supplied]`), supplies, travel (purpose + tie to dissemination/data collection), other direct costs, and patient-care/participant costs where applicable — each with a specific need, not a generic line.
5. **Handle subawards and indirect.** Summarize each subaward's scope and budget; note how subaward costs and equipment interact with the F&A base. State the indirect treatment using the institution's rate as `[user-supplied]`.
6. **Run the consistency check.** Verify effort vs. role vs. aims; flag any individual whose total committed effort across projects looks implausible; confirm category subtotals and the direct/indirect split roll up correctly. Surface arithmetic the user must confirm.
7. **Red-flag scan.** Check for the common reviewer/grants-management flags: unjustified or round-number effort, equipment miscategorized as supplies (or vice versa), general-purpose computers booked as equipment, travel with no stated purpose, missing rationale, effort that doesn't match the role's contribution, escalation not explained.
8. **Overclaim and tone pass.** Strip hype; keep the justification factual and tied to the work. Confirm every figure is user-supplied or flagged.

**Output format (locked):**

```
## Budget Justification (draft)

### Personnel
- **[Name / TBD], [Role]** — Effort: [N] [person-months: calendar/academic/summer] ([user-supplied]). Rationale: executes [Aim(s)]; [why this effort level fits the work]. Salary/fringe: [user-supplied].
- [Repeat per person; mark key personnel.]

### Fringe Benefits
- Rate and basis: [user-supplied]. Applied to: [personnel above].

### Equipment
- **[Item]** — Cost: [user-supplied]. Meets capitalization threshold ([user-supplied]): [yes/confirm]. Need: [which aim, why this instrument].

### Supplies
- **[Category]** — Cost: [user-supplied]. Need: [aim-tied rationale; e.g., reagents/animals/consumables].

### Travel
- **[Trip / purpose]** — Cost: [user-supplied]. Purpose: [data collection / dissemination / required meeting], tied to [aim/dissemination plan].

### Other Direct Costs
- **[Item]** — Cost: [user-supplied]. Need: [rationale]. (e.g., publication, participant incentives, computing.)

### Subawards / Consortium
- **[Subrecipient]** — Scope: [...]. Budget: [user-supplied]. F&A-base treatment: [user-supplied].

### Indirect Costs (F&A)
- Rate and base: [user-supplied] (verify against the negotiated rate agreement). Exclusions noted: [equipment, subaward portion above threshold, etc.].

## Cost-to-Aim Map
| Line item | Category | Aim(s) served | Justified? |
|---|---|---|---|
| [...] | [...] | [...] | yes / needs rationale / no aim — flag |

## Consistency Check
- Effort vs. role vs. aims: [flags].
- Per-person total committed effort plausibility: [flags].
- Category subtotals → totals roll up: [confirm / arithmetic to verify].
- Direct/indirect split & F&A-base exclusions: [confirm].

## Red-Flag Scan
- [Unjustified/round-number effort; miscategorized equipment vs. supplies; computers as equipment; travel without purpose; missing rationale; escalation unexplained.]

## Open Items ([user-supplied])
- [All figures, rates, thresholds, salary cap — supply or verify against the current rate agreement and funder policy.]
```

**Reporting-standard alignment:** NIH and NSF budget categories and effort conventions (NIH person-months — calendar/academic/summer; NSF academic + summer months; key personnel effort commitments) and budget-justification norms; Uniform Guidance concepts of allowability, allocability, and reasonableness as framing only. Capitalization thresholds, salary caps, fringe rates, and negotiated F&A rates are `[user-supplied]`/verify against the institution's rate agreement and current funder policy.

**Verification checklist (before delivering):**
- [ ] Discipline, study type, mechanism, budget type, and effort convention captured.
- [ ] Every line item mapped to the aim(s) it serves; aimless costs flagged.
- [ ] Personnel effort stated in the funder's units and tied to role + aims.
- [ ] Each category includes a science-anchored rationale, not a bare list.
- [ ] Equipment vs. supplies categorization checked against the (user-supplied) threshold.
- [ ] Effort-vs-role-vs-aims and total-effort plausibility checked.
- [ ] Category subtotals and direct/indirect split roll up correctly (or arithmetic flagged for confirmation).
- [ ] No fabricated figures, rates, thresholds, or personnel; all marked `[user-supplied]`.
- [ ] Red-flag scan run; common flags surfaced.
- [ ] No hype filler in drafted text.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Invented numbers | Plausible-looking salaries, fringe, or F&A rate supplied from memory | All figures/rates/thresholds are `[user-supplied]`/verify; never assert from memory |
| Listed, not justified | "Postdoc: 12 calendar months" with no tie to any aim | Cost-to-aim map requires a science-anchored rationale per line |
| Miscategorized cost | A general-purpose laptop booked as Equipment to shift the F&A base | Category-placement check + capitalization-threshold confirmation; never move costs to game indirect |
| Implausible effort | A PI committing effort that, summed across grants, exceeds available time | Per-person total-effort plausibility check flags overcommitment |
| Roll-up error | Category subtotals that don't sum to the stated total | Consistency check verifies subtotals → totals and flags arithmetic to confirm |
| Empty leadership rationale | "The PI provides overall scientific direction" with no aim linkage | Require effort justified by specific aims executed, not a title |
