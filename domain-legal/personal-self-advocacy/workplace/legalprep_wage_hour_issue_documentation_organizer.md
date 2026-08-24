---
title: "Wage & Hour Issue Documentation Organizer — Organize Hours, Pay, and Records"
category: legalprep
description: "Help an employee organize an unpaid-wages, overtime, misclassification, or missed-break concern into a factual record: hours worked, pay received, the documents that back each, and the relevant dates. Does NOT decide whether the user is owed money, whether they were misclassified, or the amount, and does NOT cite wage law — it routes those questions to a state labor board or an attorney. Not legal advice."
techniques:
  - DS-01
  - DS-21
  - NE-25
  - CM-01
  - QA-01
difficulty: intermediate
intended_use: model-testing
tags:
  - legal
  - self-represented
  - workplace
  - employment
  - wage-and-hour
  - overtime
  - misclassification
  - documentation
updated: "2026-07-23"
related_prompts:
  - domain-legal/personal-self-advocacy/workplace/legalprep_workplace_concern_documentation_organizer.md
  - domain-legal/personal-self-advocacy/workplace/legalprep_eeoc_agency_charge_preparation_organizer.md
  - domain-legal/personal-self-advocacy/workplace/legalprep_workplace_retaliation_log.md
  - domain-legal/employment-labor/legal_wage_hour_classification_analysis.md
  - domain-legal/litigation/legal_complaint_drafter.md
---

**Purpose:** Help you organize a pay concern — unpaid wages, unpaid or miscalculated overtime, being treated as exempt or as an independent contractor, or missed/interrupted breaks — into a clean factual record. It captures the hours you worked, the pay you actually received, the documents that back each, and the relevant dates, so you can hand it to a state labor board or an attorney. It organizes **your own hours, pay, and records** — it does **not** decide whether you are owed money, whether you were misclassified, or how much, and it does **not** cite wage law. Those questions go to the labor board or an attorney.

**When to use:** You think you were not paid correctly — off-the-clock work, unpaid overtime, an exempt/contractor label that does not match your day-to-day work, or missed breaks — and you want your hours and pay organized before you talk to a labor agency or lawyer.

**When NOT to use:** You want to know whether you are legally owed wages, whether your classification was correct, or the dollar amount → those are legal/factual determinations for a state labor board or an attorney. You want to organize a harassment/discrimination concern → use `legalprep_workplace_concern_documentation_organizer.md`. There is a safety emergency → Safety Block first.

---

## Safety Block

Stop and use a different pathway if:
- You are being threatened or are in physical danger over a pay dispute → call **911** for an emergency in progress. Do not confront anyone.
- You are in emotional or financial crisis → **988 Suicide & Crisis Lifeline** (US) for emotional crisis; for pay problems, contact your **state labor board / department of labor** or your **state/local bar association's** lawyer-referral service (find these via **usa.gov**).
- The person involved is an intimate partner or family member → **National Domestic Violence Hotline 1-800-799-7233** (US); mind your digital safety.
- A child is involved and unsafe → **Childhelp National Child Abuse Hotline 1-800-422-4453** (US); emergencies **911**.

This prompt is educational support for organizing your own records. It is not a substitute for legal, safety, or financial services.

---

## Scope Boundary — Read First

This **organizes your own hours, pay, and records into a factual summary**. It is **not legal advice, legal strategy, a legal filing, or a substitute for a state labor board, department of labor, or an attorney.** It will **not** decide whether you are owed wages, whether your overtime was correctly calculated, whether your exempt or independent-contractor classification was proper, or how much (if anything) you are owed. It will **not** cite or invent wage-and-hour statutes, rates, overtime formulas, exemption tests, or cases. Whether wages are owed and how classification is decided **vary by state and country and change over time**, depend on detailed legal tests, and are for a labor board or attorney. **Wage claims also have filing deadlines that can be short** — *confirm the current deadline and the legal questions with your state labor board or an attorney.* Where a legal concept appears, it is explained in plain language and flagged *confirm with the labor board or an attorney.*

---

## Core Principles

1. **Organize the numbers; don't compute the claim.** You assemble hours and pay as facts. Whether that means money is owed — and how much — is for the labor board or attorney.
2. **Hours worked and pay received are two columns.** Record what you actually worked and what you were actually paid, each from its own source, and let the reader compare.
3. **Every figure is dated and sourced.** A time record, a pay stub, a schedule, a punch export — each number ties to a document.
4. **Describe your work; don't apply the exemption/classification label.** Record your actual duties and how you were paid and titled. Do not conclude "I was misclassified" — that is a legal test for the professional.
5. **Off-the-clock time is recorded factually.** "Arrived 8:45, clocked in 9:00, worked until then" — with whatever contemporaneous note you have. Do not exaggerate or reconstruct hours you cannot support.
6. **Gaps are flagged, not filled.** Missing pay stubs or time records are listed to obtain, never estimated as if known.
7. **You organize; the professional decides.** You build the hours-and-pay record; the labor board or attorney decides entitlement, classification, and amount.

---

## Your Input

- **Your jurisdiction (state/country):** [required]
- **Employer and your role:** [company; your title; employment dates; how you were paid — hourly/salary/contractor]
- **The pay concern (in your words):** [unpaid wages / unpaid or miscalculated overtime / exempt or contractor label / missed breaks]
- **Hours worked:** [by week/pay period, as precisely as your records allow — including off-the-clock time]
- **Pay received:** [by pay period — gross/net if known; rate; any overtime paid]
- **Your actual duties:** [what you actually did day to day — factual, for the classification question]
- **Records you have:** [pay stubs, time records/punches, schedules, offer letter, contractor agreement, texts about hours]
- **Any safety dimension?:** [threats, crisis → Safety Block first]

---

## Constraints

**Must:**
- Require the jurisdiction; use only figures and facts the user supplies.
- Organize hours worked and pay received in separate, dated, sourced columns.
- Record actual duties factually for the classification question, without applying the legal test.
- Flag that wage claims have deadlines and route timing to the labor board/attorney.
- Flag missing records as `[NEED DOCUMENT:]` / `[NEED DATE:]` rather than estimating.
- Route all "am I owed / was I misclassified / how much" questions to the labor board or attorney.

**Must Not:**
- Decide whether wages/overtime are owed, or compute an amount owed.
- Decide whether the user was properly exempt or an employee vs. independent contractor.
- Cite or invent wage statutes, minimum/overtime rates, exemption tests, or cases.
- Assess the strength of the claim or predict outcomes.
- Characterize or attribute motive to the employer.
- Reconstruct or inflate hours the user cannot support from memory or records.
- Fill gaps with assumption or coach exaggeration.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen for any safety dimension (route to Safety Block). Restate the pay concern and jurisdiction. State the boundary: this organizes hours and pay; entitlement, classification, and amount are for the labor board/attorney, and deadlines can be short.

### Stage 2 — Establish Employment and Pay Basis
Capture the employer, role, dates, how the user was paid (hourly/salary/contractor), and title. Facts only.

### Stage 3 — Build the Hours-Worked Record
By pay period or week, record hours worked from the user's records, including off-the-clock time recorded factually with whatever source exists. Flag any period without support as `[NEED DOCUMENT:]`.

### Stage 4 — Build the Pay-Received Record
By pay period, record what the user was actually paid, with the pay stub or record as source. Keep it parallel to the hours record so the reader can compare — without computing a difference as "owed."

### Stage 5 — Record Duties for the Classification Question
Record the user's actual day-to-day duties, title, and pay arrangement factually. Do not apply any exemption or employee/contractor test — note that the labor board/attorney applies it.

### Stage 6 — Records, Gaps, and Route
List supporting records with dates; flag records to obtain. Route entitlement, classification, amount, and timing to the labor board or attorney; note the retaliation log if the user has raised the issue at work.

---

## Output Format

```markdown
# Wage & Hour Record — [Your name] · [jurisdiction]
Employer: [company]. My role/title: [title], [employment dates]. Paid as: [hourly/salary/contractor].
Prepared by [you], [date]. FOR THE LABOR BOARD / MY ATTORNEY — NOT A LEGAL FILING.
Does NOT decide whether wages are owed, whether I was misclassified, or the amount, and does not cite wage law.

>> DEADLINE NOTICE: Wage claims can have short filing deadlines that vary by jurisdiction.
>> I will confirm the current deadline with the labor board or an attorney. *Confirm with the labor board or an attorney.*

## 1. Employment & Pay Basis
[Employer; title; dates; how I was paid and titled — facts only.]

## 2. Hours Worked (from my records)
| Pay period / week | Hours worked | Includes off-the-clock? | Source | Status |
|---|---|---|---|---|
| 2026-02-01 to 02-07 | 47 | Yes — ~45 min/day before clock-in | Punch export + my notes | Have it |
| 2026-02-08 to 02-14 | [NEED] | | [NEED DOCUMENT: punches] | [NEED DOCUMENT:] |

## 3. Pay Received (from my pay records)
| Pay period | Rate | Regular pay | Overtime pay | Source | Status |
|---|---|---|---|---|---|
| 2026-02-01 to 02-07 | $[rate] | $[amount] | $[amount or none] | Pay stub | Have it |
| 2026-02-08 to 02-14 | | | | [NEED DOCUMENT: pay stub] | [NEED DOCUMENT:] |

## 4. My Actual Duties (for the classification question)
[What I actually did day to day; my title; how I was paid. I am NOT deciding whether this was
proper exemption or employee-vs-contractor — that is for the labor board/attorney to apply.]

## 5. Missed / Interrupted Breaks (if applicable)
| Date | What happened (facts) | Source |
|---|---|---|
| 2026-02-03 | Worked through the scheduled 30-min meal break to cover [task]. | My same-day note |

## 6. Records to Obtain
- [NEED DOCUMENT: pay stubs for [periods]]
- [NEED DOCUMENT: time/punch records — request from employer or payroll app]
- [NEED DOCUMENT: offer letter / contractor agreement]

---
For the labor board / my attorney: please assess whether wages or overtime are owed, whether my
classification was proper, and any amount and deadline. I understand this record does not decide those.
*Confirm with the labor board or an attorney.*
```

---

## Verification

- [ ] Jurisdiction captured; deadline flagged *confirm with labor board/attorney*?
- [ ] Hours worked and pay received kept in separate, dated, sourced columns?
- [ ] No decision that wages/overtime are owed and no amount computed?
- [ ] No classification decision (exempt vs. non-exempt; employee vs. contractor)?
- [ ] No wage statute, rate, overtime formula, exemption test, or case cited/invented?
- [ ] Duties recorded factually without applying a legal test?
- [ ] Off-the-clock time recorded only as far as the user can support it — not inflated?
- [ ] No strength assessment, outcome prediction, or motive attribution?
- [ ] Missing records flagged `[NEED DOCUMENT:]` / `[NEED DATE:]`, not estimated?
- [ ] Entitlement, classification, amount, and timing routed to the labor board/attorney?
- [ ] Any safety dimension screened and routed?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "You're owed about $4,200 in overtime" | Organize hours and pay; the amount is for the labor board/attorney |
| "You were misclassified as a contractor" | Record your actual duties and pay basis; classification routes to a professional |
| "Under the FLSA you must be paid time-and-a-half" | Keep it factual; the rate and formula are for the professional |
| Fill in hours for a week you can't document | Flag `[NEED DOCUMENT:]`; do not estimate as if known |
| Round 42 hours up to "about 50" | Record only the hours you can support |
| "They stole your wages on purpose" | Record what was worked and paid; motive is for counsel |
| Merge hours worked and pay received into one "amount owed" column | Keep them separate; let the professional compare |
| Treat a threat over pay as a spreadsheet task | Stop, Safety Block, call 911 if in danger, then organize |

---

## Adaptations

**By concern type:**
- **Unpaid / off-the-clock time:** Record start/stop times and any contemporaneous note (texts, app data, a personal log); flag periods you cannot support.
- **Overtime:** Record total hours per period and what overtime, if any, was paid — without computing what "should" have been paid.
- **Misclassification (exempt or contractor):** Foreground Section 4 (actual duties, title, pay arrangement); do not apply any legal test.
- **Missed breaks:** Record each date, what happened, and the source; keep it factual.

**By situation/profile:**
- **Still employed:** Keep copies of pay stubs and time records on personal storage; if you raise it at work, start a `legalprep_workplace_retaliation_log.md`.
- **Recently separated:** Request your final pay records and personnel file promptly; note your last day.
- **Paid in cash / no stubs:** Reconstruct only from what you can support (bank deposits, personal logs); flag everything else `[NEED DOCUMENT:]`.

---

## Related Prompts

- `legalprep_workplace_concern_documentation_organizer.md` — for non-pay concerns (harassment, discrimination, safety).
- `legalprep_eeoc_agency_charge_preparation_organizer.md` — a different agency may handle discrimination; ask intake where each concern belongs.
- `legalprep_workplace_retaliation_log.md` — if you are treated adversely after raising a pay issue.
- `../../employment-labor/legal_wage_hour_classification_analysis.md` — the attorney-side classification counterpart.
- `../../litigation/legal_complaint_drafter.md` — the attorney-side court-pleading counterpart, if a lawsuit follows.
