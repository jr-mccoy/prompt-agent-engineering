---
title: "First Employee Readiness — Fully Loaded Cost, Break-Even Work, Cash Runway, Classification Flag"
category: business-strategy/small-business
description: "Decide whether an owner-operator of a local shop, trades business or freelance practice is ready to hire a first employee — fully loaded annual cost, the billable hours or extra sales that pay for it, a slow-season stress test, a cash runway gate, and a contractor-versus-employee flag routed to qualified review rather than decided; distinct from hr_job_description_writer (writing the posting once the decision is made) and legal_wage_hour_classification_analysis (the legal classification analysis itself)."
techniques:
  - QA-08
  - NE-11
  - QA-02
  - DD-05
  - RT-05
difficulty: intermediate
tags:
  - small-business
  - hiring
  - first-employee
  - payroll
  - break-even
  - owner-operator
updated: "2026-09-24"
related_prompts:
  - domain-hr-management/hiring/hr_job_description_writer.md
  - domain-legal/employment-labor/legal_wage_hour_classification_analysis.md
  - domain-business-strategy/small-business/smallbiz_weekly_owner_numbers_review.md
---

# First Employee Readiness

**Objective:** Answer one question for a business owner who has done everything
alone: can the business afford a first employee, and what does the hire have to
produce to pay for itself — with the legal set-up questions listed for the people
who can answer them.

**When to Use:**
- You are turning work away, or working evenings on tasks someone else could do.
- You are about to "just pay someone cash" or "put them on a 1099" and want to
  check the numbers and the risks first.
- A family member or friend has offered to help and you need to decide what that
  arrangement is.

**Not this prompt if:**
- You have decided to hire and need the job posting —
  `domain-hr-management/hiring/hr_job_description_writer.md`.
- You need the legal analysis of whether a worker is an employee or a contractor, or
  of overtime and wage rules — `domain-legal/employment-labor/legal_wage_hour_classification_analysis.md`
  and a qualified adviser. This prompt flags the question; it does not answer it.
- You are planning a team of several hires in a funded company — that is headcount
  planning, not first-hire readiness.

## Inputs

1. The work the hire would do, hours per week, and whether it is billable to
   customers or frees your time for billable work.
2. Proposed pay rate and hours.
3. Employer cost rates you have been quoted: payroll taxes, workers' compensation,
   any benefits, payroll service. Unknown rates are marked `[get quote]`.
4. Your prices: what you bill per hour, or your gross margin on sales.
5. Demand evidence: jobs turned away, waitlist, seasonal pattern.
6. Cash: operating reserves after tax set-asides.

## Method

1. **Gate 1 — is there work for a person (RT-05)?** Evidence of demand: jobs turned
   down in the last 90 days, hours you spend on tasks below your rate, lead time
   customers wait. Opinion ("we're busy") is not evidence.

2. **Gate 2 — fully loaded cost (NE-11).**
   `loaded cost = wages + employer payroll taxes + workers' comp + benefits + payroll service + equipment + training`
   Then `productive hours = paid hours − leave − ramp-up lost hours`, and
   `cost per productive hour = loaded cost ÷ productive hours`.

3. **Gate 3 — break-even.** Two routes; use whichever applies:
   - Billable hire: `billable hours needed = loaded cost ÷ hire's billing rate`,
     then as a share of productive hours.
   - Sales hire (shop, café): `extra sales needed = loaded cost ÷ gross margin %`.
   - Owner-time route: hours freed × your rate — only counts if demand exists for
     those hours.

4. **Gate 4 — slow-season stress test (QA-02).** Re-run break-even at your slowest
   quarter's demand. State the annual loss or gain if the whole year looked like that.

5. **Gate 5 — cash runway.** Reserves must cover at least three months of loaded cost
   while the hire ramps up, after tax set-asides and your cash floor.

6. **Flag the set-up and classification questions (DD-05).** Contractor or employee;
   employer registration; payroll withholding; workers' compensation; required
   workplace notices; licensing or apprenticeship rules in regulated trades. Each is
   listed with who answers it — accountant, payroll provider, insurer, lawyer, trade
   licensing body.

7. **Verdict (QA-08).** Ready / Ready with conditions / Not yet — with the specific
   gate that failed and what would change it.

## Output Format

```
# First employee readiness — [business], [role]

## Verdict
[Ready | Ready with conditions | Not yet] — [gate and reason]

## Gate 1: demand evidence
## Gate 2: fully loaded cost
| Item | Annual | Source |
Productive hours: … | Cost per productive hour: …
## Gate 3: break-even
## Gate 4: slow-season stress test
## Gate 5: cash runway
## Questions for qualified advisers
| Question | Who answers |
## If ready: next steps
```

## Verification

- [ ] Every cost line has a source or `[get quote]`.
- [ ] Productive hours subtract leave and ramp-up.
- [ ] Break-even is stated as a weekly number the owner can check.
- [ ] The slow-season case is run, not skipped.
- [ ] Classification is flagged with a named adviser, not decided.

## False-Positive Prevention

1. **The hourly wage is not the cost.** Payroll taxes, insurance, leave, equipment
   and ramp-up commonly add a substantial share on top; use your own quotes.
2. **"I'll call them a contractor" is not a cost-saving decision.** Whether someone is
   a contractor depends on how the work is controlled, not what you call it.
   Misclassification risk is a question for an adviser — flag it every time.
3. **Freed owner hours only count if someone will pay for them.** If you have no
   waiting customers, time freed is quality of life (which may still be worth it —
   say so honestly), not revenue.
4. **Busy season is not the year.** Break-even in the best quarter and a loss in the
   worst is a seasonal hire, or a part-time one.
5. **Do not skip the ramp.** A new helper is not fully productive in week one; the
   first weeks cost your time too.
6. **No legal or tax determinations.** Registrations, withholding, insurance and
   licensing requirements vary by place; list them, route them.
7. **Dual failure:** waiting until the numbers are perfectly safe often means the
   owner breaks first. A part-time or seasonal version is a legitimate conditional yes.

## Example Output

```
# First employee readiness — Kestrel Electric (owner-operator), electrical helper

## Verdict
Ready with conditions — break-even needs 20.4 billable hours/week; demand supports
it 9 months a year but not in winter, and reserves fall $3,559 short of the runway
gate today. Start at 40 hrs in March once reserves reach $21,559; plan reduced
winter hours from December.

## Gate 1: demand evidence
14 jobs declined Jun–Aug (job log); owner spends ~10 hrs/week on hauling, prep and
clean-up (2-week time log). Pass.

## Gate 2: fully loaded cost
| Item | Annual | Source |
| Wages $22 × 40 × 52 | $45,760 | Proposed rate |
| Employer payroll taxes | $4,576 | 10% [verify with accountant] |
| Workers' comp | $3,200 | Insurer quote |
| Payroll service | $1,200 | Provider pricing |
| Tools, PPE | $1,500 | Supplier estimate |
| Total | $56,236 | |
Productive hours: 2,080 − 80 leave − 160 ramp (8 weeks at half output) = 1,840
Cost per productive hour: $56,236 ÷ 1,840 = $30.56

## Gate 3: break-even
Helper billed at $55/hr: $56,236 ÷ $55 = 1,022 billable hours = 55.6% of productive
hours ≈ 20.4 billable hours/week over 50 weeks.
At the expected 70% (1,288 hours): $70,840 billed − $56,236 = +$14,604/yr.

## Gate 4: slow-season stress test
Winter demand (Dec–Feb, job log): 12 billable helper hours/week.
Whole year at 12 hrs/week: 600 hrs × $55 = $33,000 − $56,236 = −$23,236.
Winter quarter alone (13 weeks): 156 hrs × $55 = $8,580 billed vs $14,059 cost
(one quarter of loaded) = −$5,479 for the quarter.

## Gate 5: cash runway
Three months loaded cost = $14,059. Reserves after tax set-asides $18,000, floor
$7,500 → usable $10,500. Fails by $3,559. Needed before start: $7,500 + $14,059 =
$21,559 in reserves — the weekly look-ahead shows when (target: March, busy season).

## Questions for qualified advisers
| Question | Who answers |
| Employee or contractor for a supervised helper on owner's schedule and tools | Employment lawyer / accountant |
| Apprentice or helper registration rules for electrical work | State licensing board |
| Registration, withholding, required notices | Payroll provider / accountant |
| Workers' comp class code for helper | Insurer |

## If ready: next steps
Set the March start and winter-hours terms → write the posting with hr_job_description_writer.
```

## Techniques Used

- **QA-08 Gate-Based Verification:** five gates to a readiness verdict.
- **NE-11 Embedded Calculation Formulas:** loaded cost, productive hours, break-even.
- **QA-02 Adversarial Stress-Test:** the slow-season case.
- **DD-05 Human Review Flags:** classification and set-up routed to advisers.
- **RT-05 Evidence-Based Reasoning:** demand evidence from logs, not impressions.

## Related Prompts

- `domain-hr-management/hiring/hr_job_description_writer.md` — the posting, once ready
- `domain-legal/employment-labor/legal_wage_hour_classification_analysis.md` — classification analysis
- `domain-business-strategy/small-business/smallbiz_weekly_owner_numbers_review.md` — watching cash after the hire
