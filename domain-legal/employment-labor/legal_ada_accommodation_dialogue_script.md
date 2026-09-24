---
title: "ADA Accommodation Interactive-Process Dialogue Script — Employer Side"
category: legal/employment-labor
description: "Counsel-built, employer-side script and documentation set for running the interactive process on a disability accommodation request — recognizing the request, scoped medical inquiries, essential-functions analysis, option exploration, undue-hardship reasoning, and a decision letter — distinct from an employee drafting their own accommodation request and from a post-charge EEOC position statement."
techniques:
  - SV-08
  - ST-02
  - CM-09
  - QA-01
  - QA-12
difficulty: intermediate
tags:
  - legal
  - employment-labor
  - ada
  - reasonable-accommodation
  - interactive-process
  - employee-asked-for-accommodation
  - disability-at-work
updated: "2026-09-24"
related_prompts:
  - domain-legal/employment-labor/legal_pip_and_termination_risk_review.md
  - domain-legal/employment-labor/legal_eeoc_position_statement_drafter.md
  - domain-psychology/client-self-use/communication-system/clientself_workplace_accommodations_request.md
---

# ADA Accommodation Interactive-Process Dialogue Script — Employer Side

> **Scope guard — attorney-facing only.** This prompt is for employment counsel, and for HR professionals running the process under counsel's direction. It prepares the employer's side of the conversation. If the person running it is the employee seeking an accommodation, stop and route to `domain-written-advocacy/institutions-and-records/advocacy_workplace_written_request.md` or `domain-legal/personal-self-advocacy/workplace/legalprep_hr_complaint_narrative_preparer.md`.

> **No-fabrication rule.** Do not invent statutory text, EEOC guidance language, case names, or state-law requirements. Name the governing statutes only as the user confirms them; mark coverage thresholds, deadlines, and state-specific rules `[VERIFY: …]` and unsupplied authority `[CITE: …]` / `[NEED PIN: …]`.

## When to Use

- An employee (or someone on their behalf) has asked for a change at work connected to a medical condition, and the employer needs to run a documented, good-faith interactive process.
- A request is stalled — options exchanged but no decision — and counsel wants a script to restart it properly.
- Counsel is preparing managers for a first accommodation meeting on a sensitive request (mental health, leave extension, remote work, reassignment).

**Not this prompt if:**
- The employee is drafting their own request — see `domain-psychology/client-self-use/communication-system/clientself_workplace_accommodations_request.md`.
- A charge has already been filed and you need the employer's response — use `domain-legal/employment-labor/legal_eeoc_position_statement_drafter.md`.
- The question is whether a performance action or termination is defensible — use `domain-legal/employment-labor/legal_pip_and_termination_risk_review.md` (and resolve any open accommodation request first).
- The request is a religious accommodation — the legal standard differs; do not reuse this script without adapting it.

## Inputs

- **Jurisdiction (required):** Federal law plus the state (and locality) where the employee works; employer headcount for coverage `[VERIFY: federal and state coverage thresholds]`. State law may define disability more broadly or add pregnancy, leave, or process requirements `[VERIFY]`.
- **The request:** Exact words used, by whom, when, and through what channel.
- **Job facts:** Written job description, how the job is actually performed, which duties are claimed as essential and why (time spent, consequences if not performed, others available to perform).
- **Medical information already received:** What was provided, by whom — kept to functional limitations.
- **Options on the table:** The employee's requested accommodation; alternatives the employer is considering; cost and operational data.
- **Overlapping regimes:** Whether leave laws, pregnancy accommodation law, workers' compensation, or a collective bargaining agreement are also in play `[VERIFY]`.
- **History:** Prior requests, performance or discipline issues, prior accommodations.

## Method

1. **Recognize the request.** Treat any communication that links a need for a workplace change to a medical condition as the start of the process — no particular words or form are required. Record the date received; the clock on reasonable promptness starts here.
2. **Coverage and regime map.** Identify which laws apply (disability, pregnancy-related limitations, leave, state law) and whether any imposes stricter documentation limits or timelines `[VERIFY]`. Where regimes overlap, the process must satisfy each.
3. **Scoped information request.** Draft a medical-information request limited to what is needed to establish the limitation and the need for accommodation — functional limitations, not diagnosis detail, and no genetic or family medical history. If the disability and need are obvious or already documented, request nothing further. Route medical records to a confidential file separate from the personnel file.
4. **Essential-functions analysis.** For each disputed duty, list the evidence of essentiality. Do not treat the written job description as conclusive where practice differs.
5. **Meeting script with branches.** Opening (purpose, confidentiality, non-retaliation) → the employee's description of limitations and ideas → employer's questions (open-ended, functional) → options discussion → next steps with dates. Include branch responses for: employee declines to provide information; employee insists on one specific accommodation; manager wants to say "we don't do that here"; employee raises harassment or retaliation concerns (escalate separately).
6. **Option evaluation.** For each option: effectiveness for the stated limitation, whether it removes an essential function (not required), cost and operational impact, and whether an interim accommodation is appropriate while the process continues. The employee's preference is given weight, but the employer may choose among effective options.
7. **Undue hardship or direct threat.** If invoked, require an individualized assessment on the facts supplied — resources of the relevant entity, actual operational impact, or current objective medical evidence of risk. Blanket policies and speculative costs are not an assessment.
8. **Decision and follow-up.** Draft a decision letter: what is granted, what is not and why, alternatives offered, how to raise concerns, and a check-in date. Include reassignment to a vacant position as a last-resort option where no accommodation works in the current role `[VERIFY: jurisdiction-specific reassignment standard]`.

## Output Format

```markdown
# Accommodation Interactive Process — {Employee initials} / {Role} — {Jurisdiction}
**Request received:** {date, channel}  |  **Regimes:** {…} [VERIFY]  |  **Privileged & Confidential — prepared at direction of counsel**

## 1. Request Recognition Note (what was said, when, who received it)
## 2. Regime Map
| Law | Applies? | Basis | Process or timing requirement [VERIFY] |
## 3. Medical Information Request (draft letter, scoped)
## 4. Essential-Functions Analysis
| Duty | Evidence of essentiality | Disputed? | Notes |
## 5. Meeting Script (with branches)
## 6. Options Evaluation
| Option | Effective for limitation? | Removes essential function? | Cost / impact | Interim? | Decision |
## 7. Undue Hardship / Direct Threat Assessment (only if invoked)
## 8. Decision Letter (draft)
## 9. Process Log Template (date · participant · content · next step)
```

## Verification

- [ ] Jurisdiction lock: federal and state regimes named; coverage thresholds and state requirements `[VERIFY]`.
- [ ] Citation discipline: no statute section, regulation, or guidance quoted without a supplied source or `[CITE]`.
- [ ] Scope discipline: script addresses the accommodation process only; harassment, discipline, and leave-eligibility decisions are flagged, not resolved.
- [ ] Medical request asks for functional limitations only; no diagnosis fishing, no genetic or family history.
- [ ] Every "no" in the decision letter has an individualized reason and an alternative offered.
- [ ] The script contains no statement a manager could read as discouraging the request or linking it to performance.
- [ ] Dates are logged so reasonable promptness can be shown.

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Waiting for a formal written request | Any communication linking a workplace change to a medical condition starts the process |
| Asking for the full diagnosis and records | Limit requests to what establishes the limitation and need; nothing if already obvious |
| Treating the job description as final | Test essentiality against how the work is actually done |
| Denying because of a blanket policy ("no remote work") | Policies do not replace individualized assessment |
| Letting the process go silent | Script each meeting's next step and a date; silence reads as bad faith |
| Mixing the accommodation with a pending performance issue | Separate them; resolve the request before or alongside, and have counsel review any discipline |

## Example

**Input (abridged):** California-based fictional employer Pinewood Logistics (400 employees). Warehouse supervisor Dana R. emails HR: "My doctor says I can't lift over 20 lbs for a while after surgery — can we figure something out?" Job description lists "lift 50 lbs" as essential; supervisors in practice lift rarely because they direct a team.

**Output (excerpt):**

> **Recognition note.** The email links a needed change to a medical restriction — this is an accommodation request received on the email's date. Start the log now.
>
> **Regime map.** Federal disability law and California law both apply `[VERIFY: state statute, regulations, and any stricter process rules]`; ask whether any leave is also sought `[VERIFY: leave-law overlap]`.
>
> **Medical request.** The restriction and its temporary nature are stated; request only the expected duration and confirmation of the lifting limit. Do not request the surgical diagnosis.
>
> **Essential function.** Lifting 50 lbs is listed but rarely performed by supervisors — likely marginal. Evidence needed: time records or manager statements `[NEED]`.
>
> **Script branch — manager says "everyone on the floor has to lift."** Response: "Let's look at how often this role actually lifts and who else can cover those tasks before we decide."
