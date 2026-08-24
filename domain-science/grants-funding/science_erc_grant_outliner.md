---
title: "ERC Grant Outliner (Starting / Consolidator / Advanced)"
category: science/grants-funding
description: "Outline an ERC proposal (Starting/Consolidator/Advanced) around the ground-breaking question, high-risk/high-gain ambition, PI scientific identity and track record, and the B1/B2 structure — with the risk-vs-feasibility balance made explicit."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-01
  - QA-02
  - NE-10
difficulty: advanced
tags:
  - erc
  - european-research-council
  - high-risk-high-gain
  - excellence
  - principal-investigator
  - grant-writing
  - research-funding
updated: "2026-06-26"
related_prompts:
  - domain-science/grants-funding/science_specific_aims_drafter.md
  - domain-science/grants-funding/science_nsf_proposal_outliner.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
---

# ERC Grant Outliner (Starting / Consolidator / Advanced)

**Objective:** Produce an outline for an ERC proposal that foregrounds the ground-breaking research question, the ambition and high-risk/high-gain rationale, and the PI's scientific identity and track record — since Excellence is the sole ERC evaluation criterion — and that structures the proposal into the B1 (extended synopsis) and B2 (full proposal) parts with the balance between high ambition and demonstrated feasibility made explicit.

**When to use:** You are an established or emerging PI preparing an ERC application (Starting, Consolidator, or Advanced) and need a structured B1/B2 outline that frames ambition and feasibility before writing prose.

**Required inputs:**
- **Discipline.** The scientific field and ERC panel area if known.
- **Study type.** Observational / experimental / computational / theoretical / mixed.
- **Funding mechanism.** ERC scheme: Starting, Consolidator, or Advanced — eligibility, expected maturity, and ambition framing differ by scheme.
- **The science.** The central question, why it is ground-breaking, the proposed approach, and the expected gain, in the PI's words.

**Optional inputs:**
- **PI track record.** Key achievements, independence markers, formative contributions (`[user-supplied]`).
- **Preliminary results / feasibility evidence.** Pilot data or prior work supporting feasibility (`[user-supplied]`).
- **Risk register.** The PI's view of the main scientific risks and contingencies.
- **Career stage / years-from-PhD context** relevant to scheme eligibility.

**Constraints — Must:**
- Treat Excellence as the sole evaluation criterion, assessed across the ground-breaking nature and ambition of the research, its feasibility, and the PI's track record and capacity.
- Make the high-risk/high-gain framing explicit: state the ambition and the corresponding scientific risk, and balance it with feasibility evidence rather than over-detailing to the point the project looks incremental.
- Structure the outline into B1 (extended synopsis: the question, ambition, and the PI in brief) and B2 (full proposal: state of the art, objectives, methodology, feasibility, resources).
- Surface feasibility and rigor (including reproducibility considerations) as the counterweight to ambition.

**Constraints — Must Not:**
- Do not invent citations, DOIs, preliminary data, collaborator names, institutional resources, or specific funding-program rules/budget caps. If needed and not supplied, mark `[user-supplied]` and ask; funder-specific policy/figures are `[user-supplied]`/verify against the current ERC Work Programme and call.
- Do not fabricate the PI's track record, prizes, publications, or independence markers; mark all as `[user-supplied]`.
- Do not use "novel," "groundbreaking," "first-ever," or "gold standard" as empty descriptors in drafted text; substantiate ground-breaking ambition with a specific contrast to the current state of the art and the gain if it succeeds.
- Do not flatten the risk: do not over-engineer feasibility until the project reads as low-ambition/incremental.

**Instructions:**

1. **Intake and gate.** Confirm discipline/panel, study type, ERC scheme, and the science. If the central question or the ambition rationale is missing, mark `[user-supplied]` and ask before outlining.
2. **Frame the ground-breaking question (B1).** State the question, why answering it would move a field (not just extend it), and the high-gain payoff — as a specific contrast with the current frontier, not adjectives.
3. **Articulate ambition and risk explicitly.** Name the high-risk elements and the corresponding high-gain outcomes; for each major risk, note the scientific contingency or alternative path.
4. **Establish PI scientific identity (B1).** Outline the PI's track record, independence, and the trajectory that makes them the right person, calibrated to the scheme; mark all specifics `[user-supplied]`.
5. **Outline B2 — state of the art and objectives.** Bullet the current frontier and the objectives, keeping the framing ambitious; tie objectives to the central question.
6. **Outline B2 — methodology.** Bullet the approach and methods at the level that demonstrates feasibility without descending into incremental detail; flag where rigor/reproducibility matters.
7. **Outline B2 — feasibility and resources.** Present feasibility evidence (`[user-supplied]`), the risk-vs-feasibility balance, and the resources/team needed; make the balance explicit as a short statement.
8. **Add an open-science / data note.** Note data-sharing and reproducibility commitments aligned to ERC/Horizon expectations; mark specifics `[user-supplied]`.
9. **Critique for the ambition-feasibility tension.** Run a reviewer-lens pass: is the question genuinely ground-breaking, is the risk acknowledged rather than hidden, does feasibility reassure without deflating ambition, is the PI's excellence evidenced (not asserted)?

**Output format (locked):**

```
## B1 — Extended Synopsis
- Ground-breaking question (contrast with current frontier): [...]
- High-gain payoff: [...]
- Ambition vs high-risk elements (with contingencies): [...]
- PI scientific identity & track record ([user-supplied]): [...]

## B2 — State of the Art & Objectives
- Current frontier: [...]
- Objectives (tied to the question): [...]

## B2 — Methodology
- Approach & methods (feasibility-demonstrating, not incremental): [...]
- Rigor / reproducibility considerations: [...]

## B2 — Feasibility, Risk & Resources
- Feasibility evidence ([user-supplied]): [...]
- Risk-vs-feasibility balance (explicit statement): [...]
- Resources / team / environment: [...]

## Open Science / Data
- [Sharing & reproducibility commitments — [user-supplied]]

## Reviewer-Lens Critique (Excellence sole criterion)
- Ground-breaking nature & ambition: [...]
- Feasibility without deflation: [...]
- PI track record evidenced vs asserted: [...]
- Hype scan: [...]

## Open Items ([user-supplied])
- [Citations, track-record specifics, preliminary data, call-specific rules to verify]
```

**Reporting-standard alignment:** ERC evaluation under Excellence as the sole criterion — the ground-breaking nature, ambition, and feasibility of the research and the PI's track record and capacity; the B1/B2 proposal structure. Scheme eligibility, panel structure, page limits, and budget caps are `[user-supplied]`/verify against the current ERC Work Programme and call.

**Verification checklist (before delivering):**
- [ ] Discipline/panel, study type, and ERC scheme captured.
- [ ] Ground-breaking question stated as a contrast with the current frontier.
- [ ] High-risk/high-gain framing explicit, with contingencies per major risk.
- [ ] PI scientific identity/track record outlined and marked `[user-supplied]`.
- [ ] B1/B2 structure followed.
- [ ] Feasibility presented as a counterweight without making the project look incremental.
- [ ] Open-science / data note present.
- [ ] No fabricated citations, track record, data, or call rules; all `[user-supplied]`.
- [ ] No empty hype descriptors; ambition substantiated with a specific delta and gain.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Fabricated track record | Inventing prizes, citation counts, or independence markers for the PI | Mark all track-record specifics `[user-supplied]`; never assert achievements |
| Hidden risk | An ambitious project written as if risk-free | Require explicit high-risk elements with named contingencies |
| Feasibility deflation | Methodology so detailed the project reads as incremental | Balance: enough to reassure, framed against the ambitious question |
| Hype as excellence | "Groundbreaking, first-ever paradigm" without a frontier contrast | Ban empty descriptors; force a specific delta and the high gain |
| Wrong scheme framing | Advanced-PI maturity expected of a Starting applicant (or vice versa) | Calibrate ambition/track-record framing to the stated scheme; verify eligibility `[user-supplied]` |
| Stale call assumptions | Asserting budget caps/page limits from memory | Mark Work-Programme/call specifics `[user-supplied]`/verify |
