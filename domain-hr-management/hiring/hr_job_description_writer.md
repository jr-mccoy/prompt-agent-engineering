---
title: "Job Description Writer — Outcome-Framed, Requirement-Audited, Legally Careful"
category: hr-management/hiring
description: "Write a job description built from the outcomes the hire must deliver rather than a list of duties: a scoped set of first-year outcomes, requirements audited for whether each is genuinely necessary, an honest description of the work's hard parts, compensation disclosure, and inclusive language checks. Refuses to produce a requirement list that has not been justified one line at a time."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - QA-04
  - NE-09
difficulty: intermediate
tags:
  - hiring
  - job-description
  - role-scoping
  - inclusive-language
  - pay-transparency
updated: "2026-09-22"
related_prompts:
  - domain-hr-management/hiring/hr_interview_loop_design.md
  - domain-hr-management/hiring/hr_structured_scorecard.md
  - domain-hr-management/performance-reviews/hr_performance_review_meta_prompt.md
---

# Job Description Writer

**Objective:** Produce a job description derived from **what the hire must accomplish**,
not from a list of duties copied off the last posting — with each requirement audited
for necessity, the work's genuinely hard parts stated plainly, compensation disclosed,
and language checked for the constructions that measurably narrow an applicant pool.
The prompt refuses to emit a requirements list whose entries have not each been
justified.

**When to Use:**
- You are opening a role and need a posting, or the existing posting is attracting the
  wrong applicants.
- A role has drifted and nobody can state what the person is actually accountable for.
- You want a description that the interview loop and the scorecard can be derived from,
  rather than three artifacts that disagree.

**When NOT to use:**
- You need the assessment instrument itself — that is
  `hr_hiring_screen_challenge_designer.md`.
- You need the whole process (screen → loop → debrief → offer) — that is
  `hr_interview_loop_design.md`.
- You need a review rubric for someone already in the role — that is
  `../performance-reviews/hr_performance_review_meta_prompt.md`, which generates
  role-tailored review scaffolds.
- You are writing a contractor scope of work rather than employing someone — route to
  `../../domain-legal/employment-labor/solo_dev_contractor_management.md`.

---

## Context Gathering

Ask for these before writing. A job description written without them describes a
generic role and attracts generic applicants.

1. **The outcomes**
   - "Twelve months in, what will this person have delivered that would not otherwise
     exist?"
   - "What is broken, slow or unowned today that they will own?"
   - "Who will be able to tell whether it worked, and what will they be looking at?"

2. **The work, honestly**
   - "What is the least pleasant part of this job?"
   - "What has made previous people in this role leave, or struggle?"
   - "What will they spend the most hours actually doing?"

3. **The constraints**
   - "Level, reporting line, team size, budget authority."
   - "Location, remote policy, travel, hours, on-call."
   - "Compensation range, and are you required or willing to publish it?"

4. **The requirements, one at a time**
   - For each requirement the hiring manager names: "what breaks if the person does not
     have this on day one?"

If the answer to the outcome questions is a list of activities ("manage the roadmap"),
press once more: "and if they manage the roadmap well, what is different?" A
description built on activities cannot be assessed, which is why the scorecard that
follows it ends up measuring likeability.

---

## Method

### Step 1 — Write the outcomes first

Three to five outcomes, each in the shape: **verb + object + observable condition +
timeframe.**

| Weak | Strong |
|---|---|
| "Own the analytics roadmap" | "By month six, every product team has a self-serve dashboard for its top three metrics and stops filing ad-hoc data requests" |
| "Improve code quality" | "By month nine, the deploy failure rate is below 2% and the team can name why each remaining failure happens" |
| "Support the sales team" | "By month four, sales can answer the top ten technical objections without escalating" |

The outcomes are the spine. Requirements, interview stages and the scorecard all
derive from them, and anything that derives from nothing gets cut.

### Step 2 — Audit every requirement against an outcome

For each candidate requirement, fill this row. A requirement that cannot name the
outcome it serves does not go in the posting.

| Requirement | Which outcome needs it | What breaks without it | Verdict |
|---|---|---|---|

Then apply four tests:

- **Necessary or preferred?** Most postings mark everything necessary. Move anything
  that could be learned in the first quarter to preferred, or cut it.
- **Years of experience — for what?** A year count is a proxy. If you can name the
  capability directly, name it instead. If the number is load-bearing, say why.
- **Degree requirement — legally or genuinely required?** For most roles it is neither,
  and it removes candidates who can do the job.
- **Tool-specific or capability?** "Five years of Snowflake" excludes someone with
  eight years of BigQuery who would be productive in a fortnight.

This audit is the substance of the prompt. Everything else is formatting.

### Step 3 — State the hard parts

A short, honest section on what is difficult about the role: the legacy system, the
demanding stakeholder, the ambiguity, the on-call, the travel. Two effects, both
useful: candidates who would have left in month three self-select out now, and
candidates who are good at exactly that hard thing recognise themselves.

Do not dress a problem as an opportunity. "You will own our migration off a
twelve-year-old monolith with no test coverage" is a sentence the right candidate reads
with interest.

### Step 4 — Disclose compensation

Publish the range. Where disclosure is legally required, it is required; where it is
not, publishing still shortens the process and prevents the late-stage collapse where
a candidate's expectation was never in range. State the range, the level, and what
moves someone within it. Cross-reference `../people-ops/hr_compensation_banding.md`.

If the organisation will not publish, say in the posting that the range is available on
request in the first conversation, and then actually give it.

### Step 5 — Check the language

Specific, checkable edits — not a vague call to be inclusive:

| Pattern | Why | Replace with |
|---|---|---|
| "Rockstar", "ninja", "crush it" | Narrows the pool without describing the work | The actual work |
| Long lists of "must haves" | Candidates from under-represented groups apply less often when they do not meet every line | Three to five necessary, the rest preferred |
| "Native English speaker" | Usually a proxy for a communication requirement, and legally risky in many jurisdictions | "Writes clearly in English for a technical audience" |
| "Young, dynamic team" | Age signal | Describe the team's actual working style |
| "Cultural fit" | Unfalsifiable, and a documented vector for bias | The specific working behaviours you need |
| Unexplained physical requirements | May exclude disabled candidates without cause | Only what the job genuinely requires, stated as a function |

### Step 6 — State the process

What happens after applying, how many stages, roughly how long, who they will meet,
and what the take-home (if any) asks. A candidate who knows the shape of the process
drops out less often mid-way.

---

## Output Format

```markdown
# [Role title] · [Level] · [Location / remote policy]
**Compensation:** [range] · **Reports to:** [role] · **Team:** [size, shape]

## What you will accomplish
1. [outcome — verb, object, observable condition, timeframe]

## What the job is actually like
[the honest day-to-day, including the hard parts]

## What we need
- [requirement] — [the outcome it serves]

## What would help
- [preferred]

## What we are not asking for
[explicitly: the things a reader might assume and that are not required]

## The process
| Stage | What happens | Roughly how long |
|---|---|---|

## How to apply
[what to send, what not to bother sending, who reads it]

---
### Requirement audit (internal, not published)
| Requirement | Outcome served | Breaks without it | Necessary / preferred / cut |
|---|---|---|---|

### Language check (internal)
| Flagged | Reason | Replaced with |
|---|---|---|
```

---

## Verification

- [ ] Three to five outcomes, each with an observable condition and a timeframe
- [ ] Every published requirement names the outcome it serves in the internal audit
- [ ] Necessary requirements number five or fewer
- [ ] Every years-of-experience figure is either justified or replaced by the capability
- [ ] Any degree requirement is justified, or removed
- [ ] The hard parts section exists and names something a candidate might dislike
- [ ] Compensation range is published, or a stated commitment to give it on request
- [ ] The language check table has been run and its edits applied
- [ ] The process section states the number of stages and the rough duration

**False-positive prevention.** The dominant failure is a requirements list that passes
the audit on paper because the hiring manager supplied both the requirement and its
justification in the same breath. Test each one against the outcomes independently: if
the requirement were removed, which specific outcome becomes unachievable, and by what
mechanism? "They would not be able to hit the ground running" is not a mechanism.

The second failure is a description that reads well and does not describe this job. If
the posting could be used for the same title at any other organisation, nothing in it
is specific enough to attract the right person or repel the wrong one. The outcomes and
the hard-parts section are where specificity has to live.

The third is treating the language check as sanitisation. Removing "rockstar" and
leaving fourteen mandatory requirements has not widened the pool; the requirement count
is the bigger lever, and it is the one this prompt makes you justify.

**Legally careful, per this domain's standing principles.** Requirements that exclude
candidates on the basis of a protected characteristic — directly, or as a proxy — are a
legal exposure as well as a hiring defect. This prompt flags the common proxies; it is
not legal advice, and a posting for a regulated role should be reviewed by counsel. See
`../../domain-legal/employment-labor/`.

---

## Related

- `hr_interview_loop_design.md` — the process this posting promises
- `hr_structured_scorecard.md` — derived from the same outcomes
- `hr_hiring_screen_challenge_designer.md` — the assessment instrument
- `../people-ops/hr_compensation_banding.md` — where the published range comes from
