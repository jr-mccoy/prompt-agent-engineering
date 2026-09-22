---
title: "Employee Onboarding 30/60/90 — Derived from the Role's Outcomes, With Named Owners"
category: hr-management/onboarding
description: "Build a 30/60/90 plan for a new employee from the outcomes the role was hired against: a first-week access and context checklist, staged deliverables with observable completion, a named owner for every commitment made to the new hire, and honest checkpoints that can conclude the hire is not working. Refuses plans where the manager's obligations are unnamed or where day 90 has no decision."
techniques:
  - ST-02
  - CM-02
  - QA-08
  - OC-03
  - DD-07
difficulty: intermediate
tags:
  - onboarding
  - thirty-sixty-ninety
  - ramp-up
  - manager-obligations
  - new-hire
updated: "2026-09-22"
related_prompts:
  - domain-hr-management/hiring/hr_job_description_writer.md
  - domain-hr-management/performance-reviews/hr_reviewer_approach_guide.md
  - domain-hr-management/people-ops/hr_performance_improvement_plan.md
---

# Employee Onboarding 30/60/90

**Objective:** Produce a ramp plan derived from the **outcomes the role was hired
against**, with staged deliverables whose completion is observable, a named owner for
every commitment the organisation makes to the new hire, and a day-90 checkpoint that
reaches an actual conclusion. Plans are refused if the manager's obligations are
unnamed, or if day 90 has no decision attached.

**When to Use:**
- Someone has accepted an offer and you need their first three months planned.
- A new hire is two weeks in and drifting with no stated expectations.
- Your onboarding is an IT checklist and a wiki link, and ramp times are long and
  variable.

**When NOT to use:**
- You mean **customer** onboarding — that is
  `../../domain-business-strategy/go-to-market/workflow_customer_success_onboarding_plan.md`
  and `../../domain-agentic-resources/skills/marketing/onboarding-cro/`. All 39 of this
  repository's onboarding hits are customer, education, lab or ministry onboarding; this
  is the employee one.
- You are onboarding a cohort into a training programme — route to
  `../../domain-education-teaching/instructor/higher-ed-corporate/teaching_corporate_onboarding_program.md`.
- The person is underperforming after a completed ramp — that is
  `../people-ops/hr_performance_improvement_plan.md`. A PIP is not a late 30/60/90, and
  conflating them is both unfair and legally risky.
- You are onboarding a contractor into a scope of work — route to
  `../../domain-legal/employment-labor/solo_dev_contractor_management.md`.

---

## Context Gathering

1. **What they were hired to do**
   - "The role's first-year outcomes." (from `../hiring/hr_job_description_writer.md` —
     if the plan is not derived from these, the new hire is being measured against
     something they were never told)
   - "Which attributes came back as *developable in role* at debrief?"
   - "Anything the scorecards flagged that they will need support on?"

2. **The environment they are entering**
   - "What access, accounts, hardware and permissions do they need, and who grants
     each?"
   - "Who are the five people they must know by week two, and why each?"
   - "What is genuinely confusing about how this place works?"

3. **Real early work**
   - "What is a small, real, shippable piece of work they could complete in the first
     two weeks?"
   - "What is the first thing they could own outright?"

4. **The manager's capacity**
   - "How much time can the manager actually give in weeks one to four?"
   - "Who covers when the manager is away?"

The manager-capacity question is the one that determines whether the plan is real. A
30/60/90 that assumes four hours a week of manager attention, written by a manager with
one, fails in week three and the new hire is blamed.

---

## Method

### Step 1 — Derive the stages from the outcomes, not from a template

Each outcome in the job description gets decomposed backwards:

| Outcome (12 months) | By day 90 | By day 60 | By day 30 |
|---|---|---|---|

The shape this produces is the useful one, and it is consistent across roles:

- **Days 1–30 — learn and contribute small.** Context, relationships, and one small
  real thing shipped. Not a project: something finished.
- **Days 31–60 — own something.** A defined area, small enough to succeed at, where
  they make decisions rather than execute them.
- **Days 61–90 — deliver against the bar.** Work indistinguishable in kind from what
  they will do in month twelve, at lower volume.

### Step 2 — Make every deliverable observably complete

Same discipline as the hiring scorecard's anchors: a stage goal that cannot be judged
complete will be judged on impression.

| Weak | Strong |
|---|---|
| "Get up to speed on the codebase" | "Has shipped two merged PRs, one of them touching the billing path" |
| "Build relationships with stakeholders" | "Has met the five named people and can say what each needs from this role" |
| "Understand our customers" | "Has sat in on three support calls and written up what surprised them" |

### Step 3 — Name what the organisation owes, with owners

The half of the plan most 30/60/90s omit. The new hire's obligations are listed; the
organisation's are assumed and then missed.

| What the new hire needs | Owner | By when | If it slips |
|---|---|---|---|
| Laptop, accounts, repo access | | Day 1 | |
| Named buddy or mentor | | Day 1 | |
| Weekly 1:1 booked for 12 weeks | Manager | Before day 1 | |
| Intro to each of the five key people | Manager | Week 2 | |
| Access to the systems for their first task | | Week 1 | |
| Written statement of what good looks like at 90 days | Manager | Week 1 | |

A commitment with no owner is not a commitment. And the "if it slips" column matters:
if repo access takes three weeks, the day-30 goals move — the plan should say so rather
than leaving the new hire behind a line they never had a chance to reach.

### Step 4 — Write down what good looks like at 90 days, in week one

Give it to them in writing, in the first week. This is the single highest-value act in
onboarding and the most commonly skipped: most new hires guess at the bar for three
months and find out at a review.

### Step 5 — Set checkpoints that can conclude something

Four: end of week 1, day 30, day 60, day 90. Each with an agenda in both directions —
how they are doing, and how the organisation is doing at supporting them.

**Day 90 reaches a conclusion**, and one of three:

- **On track** — ramp complete, moving to normal cadence and objectives.
- **Behind, with a named cause and a plan** — and the cause is stated honestly, which
  frequently means an organisational failure (access, unclear scope, an absent manager)
  rather than the person.
- **Not working** — the hire is not going to succeed in this role.

The third outcome has to be nameable or the checkpoint is theatre. Onboarding plans
that can only conclude "on track" are how organisations arrive at month nine with a
problem that was visible at week six.

If the conclusion is "not working", this prompt hands off — to a role change, an honest
early conversation, or the separate legally-careful process in
`../people-ops/hr_performance_improvement_plan.md`. Do not retrofit the ramp plan into
a performance case; a 30/60/90 is a support document, and using it as evidence against
someone is both unfair and, where probation and dismissal law applies, exposure.

### Step 6 — Ask the new hire to edit it

Give them the draft in week one and invite changes. They will spot goals that are
impossible given a dependency nobody mentioned, and a plan they have edited is one they
have agreed to.

---

## Output Format

```markdown
## Onboarding plan — [name], [role], start [date]

### Derived from
| Role outcome (12 months) | Day 90 | Day 60 | Day 30 |
|---|---|---|---|

### What good looks like at 90 days
*(given to the new hire in writing in week 1)*
[two or three sentences]

### Days 1–30 — learn and contribute small
| Goal | Observably complete when | Support needed | From whom |
|---|---|---|---|

### Days 31–60 — own something
| Goal | Observably complete when | Support needed | From whom |
|---|---|---|---|

### Days 61–90 — deliver against the bar
| Goal | Observably complete when | Support needed | From whom |
|---|---|---|---|

### What the organisation owes
| Commitment | Owner | By when | If it slips |
|---|---|---|---|

### The five people
| Who | Why | Introduced by | By when |
|---|---|---|---|

### Checkpoints
| When | Agenda — them | Agenda — us | Conclusion available |
|---|---|---|---|
| Week 1 | | | Plan agreed / plan revised |
| Day 30 | | | |
| Day 60 | | | |
| Day 90 | | | **On track / behind with named cause and plan / not working** |

### Reviewed with the new hire
Draft shared [date] · their edits: [summary]
```

---

## Verification

- [ ] Every stage goal derives from a stated role outcome
- [ ] Every goal has an observable completion condition
- [ ] The organisation's commitments are listed with named owners and dates
- [ ] Every commitment has an "if it slips" consequence for the plan
- [ ] "What good looks like at 90 days" is written and given in week 1
- [ ] Four checkpoints, each with a two-way agenda
- [ ] Day 90 has three available conclusions, including "not working"
- [ ] The manager's time commitment matches the time the manager actually has
- [ ] The new hire has seen and edited the draft
- [ ] Nothing in the plan is framed as a performance threshold

**False-positive prevention.** The dominant failure is a plan that lists only the new
hire's obligations. It reads as thorough and is one-sided: when ramp goes badly, the
plan contains no record of the access that arrived on day 18 or the 1:1s that were
cancelled four weeks running. Fill in the organisation's column with owners, or the
document cannot support an honest day-90 conversation.

The second failure is goals that measure activity — "complete onboarding training",
"read the documentation". Those are attendance. Ask what the person can now *do*, or
what now exists that did not.

The third failure is a day-90 checkpoint that can only pass. If "not working" is not a
statable outcome, nobody will state it, and the cost of that silence lands eight months
later on the person and on the team.

The fourth is optimism about manager capacity. A plan requiring more attention than the
manager has is a plan that fails and blames the wrong party. Halve the assumption and
name a backup.

**Legally careful, per this domain's standing principles.** In jurisdictions with
probation periods or statutory dismissal procedures, onboarding documents can become
evidence. Keep the plan a support instrument: state what the organisation owes, record
what was delivered, and if performance becomes the question, start the separate,
properly-constructed process rather than reinterpreting this one. This is not legal
advice — see `../../domain-legal/employment-labor/`.

---

## Related

- `../hiring/hr_job_description_writer.md` — the outcomes this plan is derived from
- `../hiring/hr_structured_scorecard.md` — the debrief flags that inform support needs
- `../performance-reviews/hr_reviewer_approach_guide.md` — the first real review after ramp
- `../people-ops/hr_performance_improvement_plan.md` — the separate process if day 90 concludes "not working"
