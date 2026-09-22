---
title: "Interview Loop Design — Signal Per Stage, No Redundancy, Bounded Candidate Cost"
category: hr-management/hiring
description: "Design a complete interview loop: which signal each stage uniquely produces, who owns it, what it costs the candidate, where the decision points are, and how the debrief resolves disagreement. Refuses loops where two stages test the same thing, where a stage has no owner, or where total candidate time is unbounded."
techniques:
  - ST-02
  - CM-02
  - CM-03
  - QA-08
  - OC-03
difficulty: intermediate
tags:
  - hiring
  - interview-process
  - signal-design
  - candidate-experience
  - debrief
updated: "2026-09-22"
related_prompts:
  - domain-hr-management/hiring/hr_job_description_writer.md
  - domain-hr-management/hiring/hr_structured_scorecard.md
  - domain-hr-management/hiring/hr_hiring_screen_challenge_designer.md
---

# Interview Loop Design

**Objective:** Design the whole hiring process as a **signal pipeline**: each stage
named by the one thing it uniquely establishes, with an owner, a bounded candidate
cost, an explicit advance/reject decision, and a debrief that resolves disagreement
rather than averaging it. The loop is rejected if two stages test the same attribute,
if any stage lacks an owner, or if the candidate's total time commitment is not stated.

**When to Use:**
- You are designing a loop for a new role, or an existing loop produces inconsistent
  or low-confidence decisions.
- Candidates are dropping out mid-process, or the process takes so long you lose them.
- Interviewers disagree at debrief and nobody knows how to resolve it.
- The same question is being asked in three stages and nobody has noticed.

**When NOT to use:**
- You need one assessment instrument designed — that is
  `hr_hiring_screen_challenge_designer.md`, which explicitly covers a single instrument
  rather than the whole process.
- You need the scoring instrument the interviewers fill in — that is
  `hr_structured_scorecard.md`.
- You need the posting — that is `hr_job_description_writer.md`.
- You are designing a calibration session for existing employees — that is
  `../performance-reviews/hr_calibration_facilitator.md`.
- The role is regulated and the process must follow a statutory standard — defer to
  that standard.

---

## Context Gathering

1. **The outcomes and requirements**
   - "What are the role's first-year outcomes?" (from
     `hr_job_description_writer.md` — the loop tests for these or it tests nothing)
   - "Which requirements are necessary, and which are preferred?"

2. **What the current loop does**
   - "List every stage today: who runs it, how long, what they ask."
   - "Which stage has ever rejected anyone? Which has never?"
   - "Where do candidates drop out?"

3. **Constraints**
   - "How many people can realistically interview, and how much time do they have?"
   - "How fast do you need to move? What is the competing offer timeline?"
   - "Any mandatory stages — compliance, clearance, licensing, references?"

4. **History**
   - "Think of a hire who did not work out. Which stage should have caught it?"
   - "Think of a strong hire you nearly lost. What nearly lost them?"

The stage-that-has-never-rejected-anyone question is the most diagnostic. A stage with
no rejections is either a formality, a culture signal, or an unowned rubber stamp, and
naming which is the fastest simplification available.

---

## Method

### Step 1 — Enumerate the attributes to establish

From the outcomes and necessary requirements, list the attributes the loop must
establish. Typically four to seven. For each, state **how it could be observed** —
because an attribute nobody can observe cannot be a stage's job.

| Attribute | Derived from which outcome | How it can be observed |
|---|---|---|

Attributes that cannot be observed in any available format get cut, or converted into
something that can. "Passionate about our mission" is not observable; "has done
unpaid work in this domain" is, and is a weaker claim honestly made.

### Step 2 — Assign each attribute to exactly one stage

This is the core constraint. Build the matrix:

| Stage | Attributes it owns | Format | Owner | Candidate time | Decision |
|---|---|---|---|---|---|

Rules the design must satisfy:

- **Every attribute is owned by exactly one stage.** Two stages testing the same
  attribute is duplicated cost and, worse, produces two opinions on one question with
  no tiebreak.
- **Every stage owns at least one attribute.** A stage owning nothing is a stage to
  cut — or it is a *selling* stage, which is legitimate but must be labelled as such
  and must not carry a reject decision.
- **Every stage has one named owner** who runs it and records the result.
- **Every stage has an explicit decision**: advance, reject, or advance-with-a-flag.
  A stage whose result is only ever "seemed fine" produces no signal.

### Step 3 — Order by cost-to-signal ratio

Cheap, high-signal stages first. The loop should reject as early as the evidence
allows, because a candidate rejected at stage four has spent four stages' worth of
their time and yours.

Order heuristic: the stage most likely to reject, that costs the candidate least, goes
first. This frequently means a short structured screen against the two hardest
necessary requirements, before anything else.

### Step 4 — Bound the candidate's total cost

Sum it and state it:

```
Total candidate time:  [hours]
Longest single commitment: [hours]
Elapsed wall-clock, first contact to decision: [days]
```

Then check it against three things: what the market bears for this level, what the
role pays, and whether any single commitment exceeds what an employed candidate can do
without taking leave. A take-home that needs a full day is a filter on people with
caring responsibilities, whether or not that was the intent.

If a paid exercise is used, say what it pays. `hr_hiring_screen_challenge_designer.md`
refuses to generate unpaid production work, and this prompt honours the same line.

### Step 5 — Design the debrief to resolve, not average

Most loops fail here. Specify:

- **Independent submission before discussion.** Every interviewer submits their
  scorecard before hearing anyone else's, or the loop produces one opinion held by
  several people. This is the single highest-value rule in the whole design, and it is
  the same author/reviewer separation the calibration facilitator enforces.
- **Who decides.** One named decision-maker. A committee that must reach consensus
  will default to the most confident voice or to no.
- **How disagreement resolves.** Not by averaging scores. By identifying which
  attribute is disputed and what evidence would settle it — which sometimes means one
  more short, targeted conversation rather than a coin flip.
- **The bar, stated in advance.** Which attributes are non-negotiable and which can be
  developed in role. Decide before you meet anyone, because deciding afterwards means
  deciding about a person.

### Step 6 — Specify the candidate experience

What they are told, when, and by whom: the stages up front, the timeline, feedback on
rejection, and who answers their questions. Then a service-level commitment you will
actually keep — a stated 48-hour response that slips to two weeks is worse than
stating a week.

---

## Output Format

```markdown
## Interview loop — [role], [level]

### Attributes to establish
| Attribute | From which outcome | Observable how | Non-negotiable? |
|---|---|---|---|

### The loop
| # | Stage | Attributes owned | Format | Owner | Candidate time | Decision |
|---|---|---|---|---|---|---|

**Coverage check:** every attribute owned exactly once · every stage owns ≥1 attribute
or is labelled selling-only

### Candidate cost
| | |
|---|---|
| Total time | |
| Longest single commitment | |
| Elapsed, first contact to decision | |
| Paid exercise? | [amount, or n/a] |

### Debrief
- Independent submission before discussion: **required**
- Decision-maker: [name, role]
- Disagreement resolution: [the named mechanism]
- Non-negotiable attributes: [list]
- Developable in role: [list]

### Candidate communication
| Moment | What they are told | By whom | Within |
|---|---|---|---|

### Cut from the previous loop
| Stage removed | Why |
|---|---|
```

---

## Verification

- [ ] Every attribute is owned by exactly one stage — no duplication
- [ ] Every stage owns at least one attribute, or is explicitly labelled selling-only
- [ ] Every stage has a named owner and an explicit decision type
- [ ] Stages are ordered cheap-and-decisive first
- [ ] Total candidate time is summed and stated
- [ ] No single commitment requires a candidate to take leave, or it is paid
- [ ] Independent scorecard submission before discussion is specified
- [ ] One named decision-maker
- [ ] The bar — non-negotiable versus developable — is set before candidates are met
- [ ] Any stage that has never rejected anyone is either cut or relabelled

**False-positive prevention.** The characteristic failure is a loop that looks rigorous
because it has many stages. Stage count is not signal; unique attribute coverage is. A
five-stage loop where three stages all form a general impression of communication
skills produces one noisy reading of one attribute at five times the cost. Run the
coverage check honestly: if two stages would both change their verdict on the same new
piece of evidence, they are testing the same thing.

The second failure is a debrief that averages. Averaging four scores on a disputed
attribute produces a number with no meaning and lets the loop avoid the conversation
where the actual disagreement lives. Name the disputed attribute; name the evidence
that would settle it.

The third is designing the bar after meeting candidates. Deciding what "good enough"
means while looking at a specific person is how loops end up hiring the most familiar
candidate. Set it in step 5, in writing, first.

**Bias-checked, per this domain's standing principles.** Independent submission,
attribute-based scoring and a pre-set bar are the three mechanisms that most reduce
bias in a loop. All three are structural; none depends on interviewers trying harder.

---

## Related

- `hr_job_description_writer.md` — supplies the outcomes the loop tests
- `hr_structured_scorecard.md` — the instrument each stage records into
- `hr_hiring_screen_challenge_designer.md` — one stage's instrument, in depth
- `hr_reference_check_guide.md` — the late stage this loop usually under-specifies
- `../performance-reviews/hr_calibration_facilitator.md` — the same independent-then-discuss discipline, applied to reviews
