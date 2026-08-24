---
title: "Postdoc-to-PI Transition Plan"
category: science/lab-operations-mentorship
description: "Builds a senior postdoc's transition plan — a research-independence statement, job-package components, a startup-negotiation checklist, and first-year lab-launch operations, with all figures user-supplied and market-checked."
techniques:
  - ST-01
  - ST-03
  - RT-03
  - QA-01
  - CM-02
  - NE-10
difficulty: advanced
tags:
  - postdoc-to-pi
  - faculty-transition
  - startup-negotiation
  - lab-launch
  - research-independence
  - career-development
  - mentorship
  - first-year-pi
updated: "2026-06-26"
related_prompts:
  - domain-science/lab-operations-mentorship/science_individual_development_plan_drafter.md
  - domain-science/lab-operations-mentorship/science_thesis_committee_meeting_prep.md
  - domain-science/grants-funding/science_specific_aims_drafter.md
---

# Postdoc-to-PI Transition Plan

**Objective:** Help a senior postdoc move from trainee to independent investigator. This prompt produces four linked artifacts: (1) a research-program independence statement that cleanly separates what is the postdoc's to carry forward from what belongs to the postdoc PI (with attribution/IP care); (2) the components of a faculty job package; (3) a startup-negotiation checklist covering space, equipment, personnel, protected time, and teaching relief; and (4) a first-year lab-launch operations plan (hiring, safety/approvals, mentoring, first grants). It is calibrated and realistic — no inflated claims, no invented numbers.

**When to use:** When a postdoc is preparing faculty applications, has an offer in hand to negotiate, or is about to start a PI position and needs a structured launch plan.

**Required inputs:**
- **Discipline.** Field and the kind of lab being launched (wet-bench, computational, field, hybrid).
- **Career stage / context.** Senior postdoc applying / offer-in-hand / incoming PI; institution type if known (R1, PUI, institute, industry-adjacent).
- **Research direction.** The research program the postdoc intends to build, in their own framing.
- **Provenance of the work.** Which projects, ideas, reagents, datasets, and methods originated with the postdoc vs the current PI/lab (user-supplied).

**Optional inputs:**
- **Offer details.** Any startup, space, salary, or teaching terms already on the table — `[user-supplied]`.
- **Personal constraints.** Two-body considerations, timeline, geographic limits.
- **Funding status.** Pending/awarded fellowships or transition awards (e.g., K99/R00, named transition grants).
- **Mentoring philosophy.** How the postdoc wants to run their group.

**Constraints — Must:**
- Confirm **discipline** and **career stage / context** before drafting.
- Make the independence statement explicit about attribution: carry-forward projects require a clear, documented understanding with the current PI; flag anything ambiguous for that conversation.
- Treat all financial terms — startup totals, salary, equipment costs, personnel lines — as **user-supplied or market-to-be-checked**, never asserted from the model.
- Keep expectations realistic: a first year is dominated by hiring, approvals, and setup; protect against over-promising the science timeline.
- Cross-reference Specific Aims for the first independent grant rather than re-deriving aim-writing here.
- Keep the negotiation framing principled and collegial (interests over positions), not adversarial.

**Constraints — Must Not:**
- Do not invent institutional/program requirements, exam content the user hasn't supplied, salary/startup figures, or named people. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not assert startup amounts, salary bands, equipment prices, or space allocations; mark them `[user-supplied / market-check]`.
- Do not characterize the current PI or adjudicate an IP/authorship dispute; surface the conversation to have and route formal IP/contract questions to the institution's tech-transfer / research office.
- Do not use inflated language ("novel," "groundbreaking," "first-ever," "world-class," "gold standard") in drafted statements.
- Do not promise hiring, funding, or scientific outcomes on a fixed schedule.

**Instructions:**

1. **Confirm scope.** Restate discipline, stage, institution type (if known), and lab type. Mark unknown institutional/offer specifics `[user-supplied]`.
2. **Draft the research-independence statement.** Articulate the program's central questions in the postdoc's voice, then build an explicit carry-forward / leave-behind / shared-with-permission table tied to provenance. Flag every ambiguous item as a conversation to have with the current PI before applications go out.
3. **Address attribution and IP.** Note where reagents, datasets, code, or unpublished ideas need a written understanding; route patent/MTA/licensing questions to the institutional research/tech-transfer office.
4. **Lay out the job-package components.** List what a competitive package contains (research statement, teaching/mentoring statement, diversity statement if required, chalk talk, references) — describing each, not writing them here unless asked.
5. **Build the startup-negotiation checklist.** Itemize negotiables: lab/office space, core equipment and shared-facility access, startup funds and their duration, personnel lines (techs, students, postdocs), protected research time, teaching relief/ramp, summer salary, moving/relocation, and timelines. Leave every figure as `[user-supplied / market-check]` and add prompts for benchmarking against peers and the institution's norms.
6. **Frame the negotiation principled-ly.** For each item, capture the underlying interest (what it's really for) so trades can be made without anchoring on a single number; note what to get in writing.
7. **Plan first-year lab-launch operations.** Sequence the realistic critical path: regulatory/safety approvals (IBC/IACUC/IRB/chemical/radiation as applicable), space build-out and equipment procurement, first hires and onboarding, lab culture and a mentoring plan, and the first grant cycle (cross-reference the Specific Aims prompt).
8. **Set realistic milestones.** Map quarter-by-quarter what is plausible (setup-heavy early, science later), explicitly guarding against an over-optimistic publication timeline.
9. **Close with the conversations and confirmations.** List the conversations to have (current PI, future chair, research office) and the `[user-supplied]` facts to confirm.

**Output format (locked):**

```
## Transition Context
- Discipline / lab type / stage:
- Institution type: [user-supplied if unknown]
- Offer terms on table: [user-supplied]

## Research-Independence Statement
[program in the postdoc's voice]

### Provenance Table
| Item (project / idea / reagent / dataset / code / method) | Origin | Carry-forward / Leave / Shared-with-permission | Conversation needed? |
|---|---|---|---|

### Attribution & IP Notes
- Items needing a written understanding:
- Route to institutional research/tech-transfer office:

## Faculty Job-Package Components
- [component → one-line description]

## Startup-Negotiation Checklist
| Item | Why it matters (interest) | Target (user-supplied / market-check) | Get in writing? |
|---|---|---|---|

## First-Year Lab-Launch Operations
| Quarter | Setup & approvals | Hiring & people | Science & first grant | Notes |
|---|---|---|---|---|

## Realistic Milestones & Guardrails
- [quarter-by-quarter plausibility, with over-promise warnings]

## Conversations & Confirmations [user-supplied]
- [ ]
```

**Reporting-standard alignment:** No formal reporting standard governs a faculty transition; this aligns to the NIH Individual Development Plan (IDP) framework for career transition and to common transition-award structures (e.g., K99/R00) — specific eligibility and figures are program-specific and `[user-supplied]`.

**Verification checklist (before delivering):**
- [ ] Discipline and career stage confirmed before drafting.
- [ ] Independence statement separates carry-forward from leave-behind via a provenance table.
- [ ] Every ambiguous-provenance item is flagged as a conversation to have with the current PI.
- [ ] IP/MTA/patent questions routed to the institutional research/tech-transfer office.
- [ ] No startup, salary, equipment, or space figures asserted; all marked `[user-supplied / market-check]`.
- [ ] First-year plan leads with approvals/setup/hiring and guards against an over-optimistic science timeline.
- [ ] Specific Aims cross-referenced rather than re-derived.
- [ ] Inflated language absent from drafted statements.
- [ ] Negotiation framed around interests, with "get in writing" prompts.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Invented figures | A confident "$750k startup is standard for your field" | Mark all figures `[user-supplied / market-check]`; never assert |
| IP overreach | Declaring a project is "clearly yours" | Use a provenance table; flag ambiguity for the PI conversation; route IP to the research office |
| PI characterization | Editorializing about the current PI's fairness | Stay factual; surface the conversation, don't adjudicate |
| Timeline optimism | Promising 3 first-author papers in year one | Front-load setup/hiring; flag publication-timeline over-promises |
| Hype language | "world-class, groundbreaking program" in the statement | Calibrated, plain description of the program's questions |
| Assumed institution rules | Asserting teaching load or summer-salary norms | Mark institution-specific terms `[user-supplied]` |
