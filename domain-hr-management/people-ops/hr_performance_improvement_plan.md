---
title: "Performance Improvement Plan Author — Genuinely Achievable, Support Named, Outcome Honest"
category: hr-management/people-ops
description: "Author a PIP that a person could actually pass: a specific evidenced gap, achievable targets with observable measures, the support the organisation commits to provide with named owners, a realistic timeframe, and an honest statement of the consequence. Refuses PIPs used as pre-documented exits, PIPs citing unevidenced or trait-based concerns, and PIPs with no organisational obligations."
techniques:
  - ST-02
  - CM-02
  - QA-04
  - QA-18
  - DD-07
difficulty: advanced
tags:
  - performance-management
  - pip
  - evidence-based
  - manager-obligations
  - legally-careful
updated: "2026-09-22"
related_prompts:
  - domain-hr-management/performance-reviews/hr_manager_writing_employee_review.md
  - domain-hr-management/performance-reviews/hr_reviewer_approach_guide.md
  - domain-hr-management/onboarding/hr_onboarding_thirty_sixty_ninety.md
---

# Performance Improvement Plan Author

**Objective:** Author a performance improvement plan the person could **realistically
pass**: one or two specific gaps with dated evidence, targets with observable measures,
the support the organisation commits to with named owners and dates, a timeframe
proportionate to the gap, and a plainly stated consequence. The prompt refuses three
things — a PIP being used to pre-document a decision already made, a PIP citing
unevidenced or trait-based concerns, and a PIP with no obligations on the organisation.

**When to Use:**
- A performance concern has persisted after direct feedback and you are formalising it.
- HR or policy requires a documented improvement process before any further step.
- A manager has asked for "a PIP" and you need to establish first whether that is the
  right instrument.

**When NOT to use:**
- You need the **legal risk review** of a PIP or a termination decision — that is
  `../../domain-legal/employment-labor/legal_pip_and_termination_risk_review.md`. That
  prompt reviews; **this one authors.** They are a deliberate pair, the same seam this
  repository maintains between the product and engineering sprint planners. Author here,
  then have it reviewed there before it is issued.
- The person is inside their onboarding ramp — that is
  `../onboarding/hr_onboarding_thirty_sixty_ninety.md`. A ramp plan is a support
  document and must not be retrofitted into a performance case.
- You are writing a periodic performance review — that is
  `../performance-reviews/hr_manager_writing_employee_review.md`.
- The concern is conduct rather than performance — misconduct follows a different,
  usually disciplinary, process. Do not route a conduct issue through a PIP.
- The real problem is a bad role fit, a reorganisation, or a manager relationship.
  Those have honest remedies, and a PIP is not one of them.

---

## The gate, before anything else

**Answer this first, in writing: has the decision already been made?**

If the manager cannot describe a version of the next 60 days in which this person
succeeds and stays, the PIP is not an improvement plan — it is documentation for an
exit. That is a real thing organisations do, and it is:

- **Unfair.** The person spends weeks in acute stress working toward an outcome that is
  not available.
- **Legally counterproductive in most jurisdictions.** A sham process is worse evidence
  than an honest early conversation, and it tends to be visible in the record: targets
  nobody could hit, support promised and not delivered, a timeframe shorter than the
  work cycle.
- **Corrosive to the team**, who can generally tell.

If the decision is made, the honest routes are a direct conversation, a negotiated exit,
or a role change — and legal advice first. **This prompt will not write a plan designed
to fail.** Say so plainly to the requester.

If the decision genuinely is not made, continue.

---

## Context Gathering

1. **The gap, with evidence**
   - "State the gap in one sentence. What is the person not doing that the role
     requires?"
   - "For each instance: what happened, when, what was the impact, who observed it?"
   - "Was this raised with them directly before now? When, by whom, and what was said?"

2. **The bar**
   - "What does meeting expectations look like for this role and level?" (from
     `../performance-reviews/hr_performance_review_meta_prompt.md`)
   - "Are others at this level doing the thing this person is not? All of them?"

3. **What the organisation did**
   - "What support has the person had — training, mentoring, tooling, clear
     requirements?"
   - "Has their manager changed? Their scope? Their team?"
   - "Has anything happened to them that the organisation knows about?"

4. **The cause**
   - "Is this a skill gap, a clarity gap, a capacity gap, a motivation gap, or a fit
     gap?"

The third group is the one that most often changes the answer. A performance gap that
began when scope doubled, or when the third manager in a year arrived, or when
requirements stopped being written down, is an organisational failure with a performance
symptom — and a PIP addressed to the individual will not fix it.

The prior-feedback question is also a gate. If the concern has never been raised
directly, a formal PIP is the wrong first step: raise it, give it a fair interval, then
escalate if it persists.

---

## Method

### Step 1 — State one or two gaps, evidenced, and not as traits

One or two. A PIP listing six concerns is not a plan, it is a case, and the person
cannot work on six things in eight weeks.

Each gap in this shape, and every claim carries dated evidence:

| Gap | Evidence (dated, specific, observable) | Impact | Previously raised |
|---|---|---|---|

Trait language is refused, because it is unfalsifiable and cannot be improved:

| Refused | Rewritten |
|---|---|
| "Lacks attention to detail" | "Three of five specs delivered since March were returned for missing acceptance criteria (14 Mar, 2 Apr, 19 Apr)" |
| "Not a team player" | "Did not attend four of six sprint planning sessions and did not respond to the reschedule requests" |
| "Poor communication" | "Two escalations (8 Feb, 3 Mar) where a slipping deadline was first reported on the due date" |
| "Bad attitude" | Not a performance gap. If it is conduct, use the conduct process; if it describes disagreement, it is not a gap at all |

If a gap cannot be evidenced, it does not go in the document. A PIP with an unevidenced
concern is both unfair and the weakest possible position if it is ever examined.

### Step 2 — Set targets the person could actually hit

Each target: observable, attributable to them, and achievable within the timeframe using
resources they will actually have.

| Weak | Strong |
|---|---|
| "Improve quality of work" | "Every spec from now includes acceptance criteria before it goes to review; measured on all specs submitted, reviewed weekly with the manager" |
| "Be more communicative" | "Flags any at-risk deadline at least five working days before it is due, in the team channel" |
| "Hit team goals" | Not attributable to one person — cannot be a PIP target |

Three tests every target must pass:

- **Within their control.** A target depending on another team's delivery is not theirs.
- **Measurable by something already recorded**, or by something you will now start
  recording — and if the latter, the measurement starts with the PIP, not retroactively.
- **Achievable at the required level.** If the target is what an exceptional performer
  does, it is not the bar, and the plan is designed to fail.

### Step 3 — Name what the organisation will do, with owners

The section that separates an improvement plan from a documentation exercise. Without
it, the document says the problem is entirely the person's and the organisation has no
part in fixing it.

| Support | Owner | By when | How the person requests it |
|---|---|---|---|
| Weekly 1:1, 30 min, written notes | Manager | Starts [date] | Standing |
| Written acceptance criteria on incoming work | [name] | Immediately | In the ticket |
| Pairing with [name] twice weekly | [name] | Weeks 1–4 | Standing |
| Training / access / tooling | | | |

**If the organisation does not deliver its side, the plan pauses.** State that in the
document. It is the fairness commitment that makes the rest credible, and it is the
clause that distinguishes an honest process on paper.

### Step 4 — Set a proportionate timeframe

Long enough for the work cycle to turn over at least twice, so the person has a second
chance at the same kind of task. For most knowledge work that is 30–90 days; a role with
a quarterly cycle cannot be assessed in 30.

State the checkpoint dates, not just the end date. Weekly or fortnightly, in writing,
each recording progress against each target and whether the organisation met its
commitments.

### Step 5 — State the consequence honestly

One sentence, plain: what happens if the targets are met, and what happens if they are
not. Do not soften it into ambiguity — "we'll reassess" is not a consequence and leaves
the person unable to make an informed decision about their own life.

And state what happens if they are **partially** met, because that is the most likely
outcome and the one most PIPs fail to anticipate. Decide it now, before you are looking
at a specific result.

### Step 6 — Have it reviewed before issuing

Two reviews, both before the person sees it:

1. **Legal risk review** —
   `../../domain-legal/employment-labor/legal_pip_and_termination_risk_review.md`.
2. **A second manager** who does not manage this person, checking one question: could
   someone meeting the bar for this level pass this plan? Author/reviewer separation, the
   same principle `../performance-reviews/hr_calibration_facilitator.md` applies to
   ratings.

### Step 7 — Deliver it as a conversation

The document is issued in a meeting, not by email. The person is told they may respond,
may have the plan amended if a target is genuinely unachievable, and may bring a
representative where policy or law provides for one. Record their response in the
document — including disagreement.

---

## Output Format

```markdown
# Performance Improvement Plan — [name], [role]
**Period:** [start] to [end] · **Manager:** [name] · **Issued:** [date]
**Reviewed by:** legal risk review [date] · second manager [name, date]

## Why this plan exists
[two or three sentences: the gap, that it was raised before, and that the intent is for
the person to succeed in the role]

## The gaps
### 1. [Gap, stated as behaviour not trait]
**Evidence:** [dated, specific, observable]
**Impact:** [what it cost, concretely]
**Previously raised:** [when, by whom, what was said]

## Targets
| # | Target | How it is measured | By when | Within their control? |
|---|---|---|---|---|

## What [organisation] will provide
| Support | Owner | By when | How to request it |
|---|---|---|---|

**If these commitments are not delivered, this plan pauses for the equivalent period.**

## Checkpoints
| Date | Progress against targets | Did we meet our commitments? | Notes |
|---|---|---|---|

## Outcomes
- **Targets met:** [what happens]
- **Targets partially met:** [what happens — decided now]
- **Targets not met:** [what happens, plainly]

## The person's response
[recorded verbatim where possible, including any disagreement or requested amendment]

**Signed:** ___ (manager) ___ (employee — signature acknowledges receipt, not agreement)
```

---

## Verification

- [ ] The gate was answered in writing: the decision has genuinely not been made
- [ ] One or two gaps, not a list of six
- [ ] Every gap is stated as behaviour, with dated specific evidence
- [ ] No trait language anywhere
- [ ] The concern was raised directly before this formal step
- [ ] Every target is observable, attributable and achievable at the required level
- [ ] No target depends on another person or team
- [ ] The organisation's commitments are listed with named owners and dates
- [ ] The pause clause is present
- [ ] The timeframe covers at least two work cycles
- [ ] Checkpoints are dated and record both sides
- [ ] All three outcomes are stated, including partial
- [ ] Legal risk review completed before issue
- [ ] A second manager confirmed a bar-meeting performer could pass this plan
- [ ] The person's response is recorded, including disagreement

**False-positive prevention.** The dominant failure is the PIP that cannot be passed,
written by a manager who has already decided. The tell is in the document, and it is
checkable: targets above the level's bar, a timeframe shorter than one work cycle, no
organisational commitments, and six gaps instead of two. Run the second-manager review
and ask only that question — could a person meeting the bar pass this? If the honest
answer is no, the plan is not an improvement plan.

The second failure is trait language, which survives because it feels like a summary of
many small things. It is unfalsifiable, it cannot be worked on, and it is the first thing
a tribunal or an appeal will attack. Convert every trait to dated instances or drop it.

The third failure is attributing an organisational cause to the individual. If the gap
began when the third manager arrived or when requirements stopped being written, the PIP
addresses the wrong party and will not work even if the person tries. The context
gathering exists to catch this; take the answer seriously when it does.

The fourth is skipping the direct conversation first. A formal PIP as the opening move
on a concern the person has never heard is procedurally unfair in most frameworks and
tends to be the single most damaging fact in the record.

**Legally careful, per this domain's standing principles. This is not legal advice.**
Requirements for procedural fairness, notice, representation, appeal rights and
documentation vary substantially by jurisdiction and by contract, and a defective
process creates liability independent of the underlying performance question. Have the
plan reviewed by
`../../domain-legal/employment-labor/legal_pip_and_termination_risk_review.md` and by
counsel before it is issued.

---

## Related

- `../../domain-legal/employment-labor/legal_pip_and_termination_risk_review.md` — the review half of this pair; run it before issuing
- `../performance-reviews/hr_manager_writing_employee_review.md` — the periodic review, not this
- `../performance-reviews/hr_reviewer_approach_guide.md` — evidence gathering and bias audit
- `../performance-reviews/hr_performance_review_meta_prompt.md` — the role-and-level bar this measures against
- `../onboarding/hr_onboarding_thirty_sixty_ninety.md` — the support document that must not be retrofitted into this
