---
title: "Reduction in Force — Criteria Before Names, a Humane Day-Of, and the People Who Stay"
category: hr-management/people-ops
description: "Plan the people side of a reduction in force: alternatives considered in writing, a decisional unit and role-based selection criteria fixed before any names are applied, a selection-rate check that routes any skew to counsel, a sequenced notification day, a manager conversation script that states a final decision plainly, and a same-day plan for the people who remain — legal exposure is routed to legal_pip_and_termination_risk_review and the release terms to legal_employment_offer_and_separation_package, which this does not replace."
techniques:
  - ST-02
  - QA-08
  - DD-05
  - DP-04
  - CM-02
difficulty: advanced
tags:
  - reduction-in-force
  - layoffs
  - termination-conversation
  - selection-criteria
  - survivor-communication
  - legally-careful
updated: "2026-09-24"
related_prompts:
  - domain-legal/employment-labor/legal_pip_and_termination_risk_review.md
  - domain-legal/employment-labor/legal_employment_offer_and_separation_package.md
  - domain-negotiation/difficult-conversations/difficultconvo_delivering_bad_news.md
---

# Reduction in Force

**Objective:** Produce the people-side plan for eliminating roles. Record the
alternatives considered. Fix the decisional unit and role-based selection criteria
before anyone's name is applied, and check selection rates so counsel sees any skew
first. Sequence the notification day, give managers a conversation script that does
not pretend the decision is open, and plan for the people who stay. The prompt refuses
three things: a RIF used to exit individuals for performance, criteria written after
names were chosen, and notifications by email or group call where a private
conversation is possible.

**When to Use:**
- Leadership has decided headcount must fall and you own the execution.
- You are a manager who will hold some of the conversations.
- A previous reduction was handled badly and you want the next one planned.

**Distinct from / route to:**
- `../../domain-legal/employment-labor/legal_pip_and_termination_risk_review.md` —
  **legal risk review of selection**, including decisional-unit documentation and
  disparate-impact analysis. This prompt prepares the inputs; that one reviews them.
- `../../domain-legal/employment-labor/legal_employment_offer_and_separation_package.md` —
  the release and separation agreement terms, including age-related disclosure and
  review-period rules.
- `../../domain-negotiation/difficult-conversations/difficultconvo_delivering_bad_news.md`
  — the general craft of delivering a decision you did not make. This applies it to one
  specific, high-stakes conversation.
- `hr_performance_improvement_plan.md` — if the real issue is one person's performance,
  that is the honest route. A RIF is about roles, not people.

**This is not legal advice.** Notice periods, collective consultation, mass-layoff
notification thresholds, selection rules and release validity vary by jurisdiction and
are decided with counsel.

---

## Inputs

1. **The business reason and the target** — cost, headcount or both, and by when.
2. **Org chart with roles**, and which functions are in scope.
3. **Alternatives already considered** — hiring freeze, attrition, reduced hours,
   redeployment, voluntary programmes.
4. **Package parameters** agreed with finance: severance formula, benefits continuation,
   equity treatment, outplacement.
5. **Jurisdictions of affected staff** and any works council or union.
6. **Who has counsel engaged**, and their availability for review dates.

---

## Method

1. **Record the alternatives (DD-05).** One line per alternative: considered, why it does
   not meet the target, who decided. This is a judgement item for leadership. The prompt
   records it and does not make it.

2. **Define the decisional unit and criteria before names (CM-02).** State which roles or
   teams are in scope and the criteria for which roles are eliminated: work being
   discontinued, duplicated roles, skills required going forward. Where criteria compare
   people within a role, use documented, job-related measures that existed before the
   RIF was planned. Freeze the criteria document with a date before any list is produced.

3. **Apply names, then check selection rates (QA-08).** Once the list exists, compute the
   selection rate for each group counsel specifies, commonly including age bands, and
   compare. Any material skew is a **gate**: the plan pauses and goes to counsel with the
   decisional unit, the criteria and the list. The prompt reports the arithmetic and does
   not decide what it means legally.

4. **Sequence the day.** Conversations happen early in the day and early in the week, all
   within a short window, before any company-wide message. System access changes at the
   moment of the conversation, not before. Assign each conversation a manager and an HR
   partner, a private room or video call, and a 20-minute slot.

5. **Script the conversation (DP-04).** Six parts, in this order:
   the decision in the first sentence; that it is a role decision and final; the date
   employment ends; the package in one sentence, with written detail to follow; what
   happens in the next hour; who to contact. Managers must not argue, blame others,
   speculate about who else is affected, or suggest the decision could change.

6. **Plan for the people who stay.** A same-day message from the most senior leader:
   what happened, why, how many, that it is complete (only if true), and what changes for
   remaining teams. Within a week, re-plan the departed roles' work. Unassigned work falls
   on whoever is most conscientious.

7. **Plan the support.** Reference policy, outplacement start date, benefits dates, how
   to collect belongings, and an alumni or job-board list if the people affected want one.

---

## Output Format

```markdown
## Reduction in force — people plan, [org], [date]
**Status:** DRAFT · counsel review: [pending / complete, date]

### Alternatives considered
| Alternative | Why it does not meet the target | Decided by |
|---|---|---|

### Decisional unit and criteria (frozen [date])
Unit: [...] · Criteria: [...]

### Selection-rate check
| Group | In unit | Selected | Rate |
|---|---|---|---|
Flag: [none / skew — paused for counsel]

### Notification day
| Time | Person (ID only) | Manager | HR | Room/link | Access change |
|---|---|---|---|---|---|
Company message: [time, sender]

### Conversation script
[six parts, verbatim]

### Remaining teams
Message: [...] · Work re-plan owner and date: [...]

### Support
[references, outplacement, benefits dates, belongings]
```

---

## Verification

- [ ] Alternatives are recorded with who decided
- [ ] Criteria were frozen and dated before any name was applied
- [ ] Criteria are role-based or use measures that existed before the RIF
- [ ] Selection rates were computed and any skew was sent to counsel before proceeding
- [ ] Every conversation has a manager, an HR partner, a private setting and a slot
- [ ] Access changes at the conversation, not before
- [ ] The script states the decision in the first sentence and does not imply it is open
- [ ] The remaining-team message says "complete" only if it is
- [ ] Legal and package terms have gone to the two legal prompts and to counsel

## False-Positive Prevention

1. **Do not use a RIF to handle performance.** Including someone because they are hard
   to manage turns a role decision into a pretext, and it is often visible in the
   record. Use the performance process.
2. **Names first, criteria after is the defining failure.** If a list existed before the
   criteria document, say so to counsel. Do not backdate.
3. **A clean selection-rate table is not legal clearance.** It is one input. Counsel
   decides.
4. **Softening the decision is not kind.** "We're exploring options for your role"
   leaves the person unable to plan. State the decision.
5. **Do not cut access before the conversation.** Someone who finds out from a failed
   login learns that the organisation chose convenience over them.
6. **"This is the only round" is a promise.** Make it only if leadership has committed to it.
7. **Survivors are affected too.** A plan that ends at the last conversation leaves the
   remaining team to work out the workload themselves.

---

## Example

**Context:** 120-person company. Target: 14 roles by 1 Oct. Decisional unit: Sales (30)
and Marketing (16) = 46 people. Alternatives recorded: a hiring freeze (already in
place, saves 3 roles' cost by year end, short of target) and reduced hours (rejected by
the CEO: customer coverage).

Criteria frozen 2 Sep: the outbound SDR function is discontinued (7 roles); regional
field marketing is consolidated from 3 regions to 1 (4 roles); duplicated sales-ops
roles are reduced from 5 to 2 (3 roles, compared on documented FY review ratings).
7 + 4 + 3 = 14.

| Group | In unit | Selected | Rate |
|---|---|---|---|
| Age 40+ | 18 | 9 | 50.0% |
| Under 40 | 28 | 5 | 17.9% |

The rates differ materially (17.9 / 50.0 = 0.36). **Plan paused 4 Sep and sent to counsel**
with the unit, the criteria and the list. Counsel review is booked for 9 Sep. The
notification day is held until counsel signs off. This prompt makes no finding on what
the disparity means.

**Draft day (pending review):** 14 conversations across 7 managers, 2 each, in 20-minute
slots from 09:00 to 11:00, each with an HR partner. Company message from the CEO at
11:30. Severance formula: 4 weeks' base plus 1 week per full year of service, so an
employee with 3 years receives 7 weeks.

**Script opening:** "I have difficult news. Your role is one of fourteen being eliminated,
and the decision is final. Your last day of employment is 30 September."

---

## Techniques Used

- **ST-02 Structured Sequential Instructions** — alternatives, criteria, check, day, script, survivors, support.
- **QA-08 Gate-Based Verification** — a selection-rate skew pauses the plan for counsel.
- **DD-05 Human Review Flags** — business alternatives and legal meaning are marked as human judgement.
- **DP-04 Must-Not Constraints** — what managers must not say in the conversation.
- **CM-02 Constraint Specification** — criteria frozen and dated before names.

## Related Prompts

- `../../domain-legal/employment-labor/legal_pip_and_termination_risk_review.md` — selection and disparate-impact review
- `../../domain-legal/employment-labor/legal_employment_offer_and_separation_package.md` — release and separation terms
- `../../domain-negotiation/difficult-conversations/difficultconvo_delivering_bad_news.md` — the conversation craft
- `hr_performance_improvement_plan.md` — the honest route when the issue is performance
