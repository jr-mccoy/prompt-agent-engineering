---
title: "Mentor Pipeline and Capacity — Growing Supply Without Lowering the Bar"
category: discipleship/program-operations
description: "Plan mentor supply against demand for a discipleship program — modelling the pipeline from invitation through screening and training to pairing, with honest lead times — and holding the readiness bar fixed by naming what the program will do instead when supply cannot meet demand."
techniques:
  - ST-02
  - RT-02
  - CM-02
  - OC-03
  - QA-01
difficulty: intermediate
tags:
  - discipleship
  - program-operations
  - capacity
  - recruitment
  - pipeline
updated: "2026-08-04"
related_prompts:
  - domain-discipleship/program-operations/discipleship_program_health_review.md
  - domain-discipleship/mentor-equipping/discipleship_mentor_readiness_assessment.md
  - domain-discipleship/mentor-equipping/discipleship_mentor_support_and_sustainability.md
  - domain-discipleship/curriculum-architecture/discipleship_multiplication_design.md
  - domain-discipleship/mentor-equipping/discipleship_mentor_training_curriculum.md
---

# Mentor Pipeline and Capacity

**Objective:** Model a discipleship program's mentor supply against its demand — the pipeline from
invitation through screening and training to pairing, with honest lead times and honest loss at each
stage — and hold the readiness bar fixed by deciding in advance what the program does instead when
supply cannot meet demand.

> **Boundary guardrail.** Capacity pressure is the most common reason unsafe mentors are approved. This
> prompt exists to absorb that pressure so that
> `../mentor-equipping/discipleship_mentor_readiness_assessment.md` and the safeguarding policy never
> have to. Screening and training requirements are fixed inputs here; they are never variables to be
> relaxed, and any legal requirement is `[VERIFY]` via `domain-legal/`.

**When to use:** More people are asking for mentors than you have, or you are planning growth and want
to know what the pipeline will actually deliver and when.

**When NOT to use:**
- You are assessing one candidate — use `../mentor-equipping/discipleship_mentor_readiness_assessment.md`.
- Existing mentors are overloaded rather than too few — use
  `../mentor-equipping/discipleship_mentor_support_and_sustainability.md`.
- You want reproduction designed into the pathway — use
  `../curriculum-architecture/discipleship_multiplication_design.md`.
- You are reviewing the program's overall health — use `discipleship_program_health_review.md`.

**Audience:** Program leads and leadership planning capacity.

---

## Inputs / Context

**Required:**

1. **Demand.** How many are waiting, arrival rate, and how long the longest has waited.
2. **Current supply.** Active mentors, how many each carries, and the program's stated capacity limit.
3. **Pipeline reality.** How long screening takes, when training runs, and honestly how many people
   drop out or are not ready at each stage.
4. **Where mentors come from.** How people currently hear about it and who invites them.

**Optional:**

5. **Declared tradition (optional).** May gate who may mentor — membership, eldership, ordination,
   gender-specific pairing — which constrains the addressable pool and must be modelled, not ignored.
6. **Completers.** Participants who have finished and might reproduce.
7. **Past recruitment.** What has been tried and what it yielded.

**If any required input is missing:** Ask clarifying questions before proceeding. Ask for the honest
attrition at each pipeline stage — plans built on the assumption that everyone invited becomes a mentor
overpromise by a wide margin and then create the pressure this prompt exists to prevent.

---

## Constraints

### Must

- Treat **screening and training requirements as fixed**. They are inputs, not levers.
- Model the pipeline with **realistic lead time and loss at each stage** — invited, interested,
  screened, trained, paired.
- State the **honest time to first new pair**, which is usually months rather than weeks.
- Decide in advance **what the program does when supply cannot meet demand**, from a named set of
  options that does not include lowering the bar.
- Report the **unmatched consequence** plainly: how long people wait and what they are told.
- Identify the **actual bottleneck stage**, since recruiting harder is the wrong fix when the constraint
  is screening throughput or trainer availability.
- Include **reproduction from completers** as a supply source with its own honest lead time.
- State what **growth would cost** in coordinator, screener, and trainer hours — supply growth is never
  free.

### Must Not

- Propose lowering, waiving, expediting, or making exceptions to screening or training. Not for a
  shortage, not for a trusted person, not temporarily.
- Model a pipeline with no loss between stages.
- Recommend raising mentor caseloads above the stated capacity limit.
- Invent recruitment conversion rates, volunteer statistics, or pipeline benchmarks.
- Quote Scripture text from memory, and do not use passages about the harvest and the workers to
  pressure recruitment.
- Treat a waiting list as a failure requiring an emergency response — it is a signal, and the honest
  responses to it are legitimate.
- Assume the addressable pool is the whole congregation or user base.
- Promise anyone a match by a date the pipeline cannot support.

### Tradition-neutral stance (Must / Must Not)

- **Must:** where a tradition restricts who may mentor, model the addressable pool accordingly and name
  the restriction as that stream's requirement; note that it materially changes the capacity picture.
- **Must Not:** propose relaxing a tradition's authorization requirement to solve a shortage, or treat
  a tradition with formal gates as simply having a supply problem.

---

## Instructions

### Step 1 — State the gap

Demand, supply, and the arithmetic. Include the longest wait and the arrival rate, since a stable gap
and a growing one need different responses.

### Step 2 — Model the pipeline honestly

Walk invited → interested → screened → trained → paired, with the loss and the lead time at each stage.
Where the number is unknown, say so and use a stated assumption rather than a flattering one.

### Step 3 — Find the actual bottleneck

Identify which stage constrains throughput. It is frequently not recruitment — it is screening
capacity, trainer availability, or coordinator hours. Recruiting harder into a blocked pipeline
produces frustrated volunteers and no new pairs.

### Step 4 — Compute the honest time to first new pair

From today, through the pipeline, to a new pair meeting. State it plainly. This number is what makes
recruitment-as-the-answer visibly insufficient for a shortage that is urgent now.

### Step 5 — Choose from the legitimate options

When supply cannot meet demand, the options are: **wait with honest communication** · **small groups
instead of pairs** · **shorter seasons so mentors cycle sooner** · **a lighter offer for those waiting**
· **reproduction from completers** · **pause intake**. Choose, with the trade named. Lowering the bar is
not on this list and never enters it.

### Step 6 — Model reproduction from completers

Completers are the most sustainable supply source and the slowest. Model the lead time honestly and
route the design to `../curriculum-architecture/discipleship_multiplication_design.md`.

### Step 7 — Cost the growth and check

State the coordinator, screener, and trainer hours that growth requires. Then check: is the bar
untouched, is loss modelled at every stage, is the bottleneck correctly identified, and is the
unmatched communication written?

---

## Output Format

Produce exactly this structure.

```
# Mentor Pipeline and Capacity — [program]

## The Gap
- Waiting: [n] | Arriving: [n]/month | Longest wait: [..]
- Active mentors: [n] | Capacity limit: [n] each | **Total capacity: [n]**
- **Gap: [n]** — and it is [stable / growing]

## The Pipeline
| Stage | Currently | Loss to next stage | Lead time | Assumption |
|---|---|---|---|---|
| Invited | [..] | [..] | [..] | [stated, not flattering] |
| Interested | [..] | [..] | [..] | [..] |
| Screened | [..] | [..] | [..] | [..] |
| Trained | [..] | [..] | [..] | [..] |
| Paired | [..] | — | — | |

## The Bottleneck
**[stage]** — because [..].
**Recruiting harder will not help if the bottleneck is downstream of recruitment.**

## Honest Time to First New Pair
**[n weeks/months]** from today. [Working shown.]

## What We Do About the Gap
| Option | Trade | Chosen? |
|---|---|---|
| Wait, with honest communication | [..] | [..] |
| Small groups instead of pairs | [..] | [..] |
| Shorter seasons, faster cycling | [..] | [..] |
| A lighter offer while waiting | [..] | [..] |
| Reproduction from completers | slow but most sustainable | [..] |
| Pause intake | [..] | [..] |

**Not an option: lowering, waiving, expediting, or making exceptions to screening or training.**
This is fixed. See `discipleship_safeguarding_and_conduct_policy.md`.

## What People Waiting Are Told
> "[Honest about timing. No promised date the pipeline can't support.]"

## Reproduction from Completers
- Completers who might reproduce: [n] | Honest lead time: [..]
- Design routes to `../curriculum-architecture/discipleship_multiplication_design.md`

## What Growth Costs
| Role | Extra hours needed | Owned? |
|---|---|---|
| Coordinator | [..] | [..] |
| Screener | [..] | [..] |
| Trainer | [..] | [..] |

## Check
| Check | Result |
|---|---|
| Readiness bar untouched | [..] |
| Loss modelled at every stage | [..] |
| Bottleneck correctly identified | [..] |
| Unmatched communication written | [..] |
```

---

## Verification

- [ ] No option lowers, waives, expedites, or excepts screening or training.
- [ ] Every pipeline stage has a stated loss rate and lead time, with assumptions named.
- [ ] The bottleneck is identified and is not assumed to be recruitment.
- [ ] The honest time to first new pair is computed and shown.
- [ ] The response to the gap is chosen from the legitimate options, with the trade named.
- [ ] Growth is costed in coordinator, screener, and trainer hours.

---

## False-Positive Prevention

❌ **DON'T:**
- Treat recruitment as the answer by default. Most pipelines are blocked at screening or training, and
  more volunteers into a blocked pipeline produces disappointed people, not new pairs.
- Model the pipeline without loss. Perhaps a third of those invited express interest and fewer complete
  training; a lossless model overpromises and creates the pressure that breaks the bar.
- Make an exception for someone trusted and well known. That is the exception that appears in every
  safeguarding failure review.
- Raise caseloads to close the gap. It converts a mentor shortage into a mentor-attrition problem within
  two cohorts.
- Use harvest-and-workers language to recruit. It is pressure dressed as calling, and it produces
  volunteers who cannot say no.
- Promise a match by a date the pipeline cannot support. The broken promise costs more than the wait.

✅ **DO:**
- Put the honest time-to-first-new-pair in front of leadership. It reframes the conversation from
  "recruit more" to "what do we do for the people waiting now."
- Name the bottleneck explicitly, and direct effort there rather than at the most visible stage.
- Choose from the legitimate options and name the trade, so the decision is made rather than drifted
  into.
- Write what waiting people are told, since silence is the default and it is the worst option available.
- Model reproduction from completers as real supply with a slow lead time — it is the only source that
  compounds.
- Cost growth in hours and check the roles are owned. Supply growth that outruns coordinator capacity
  fails at the coordinator.

---

## Techniques Used

- **ST-02 (Structured Sequential Instructions):** the gap and pipeline are modelled before options are
  considered, so the response is chosen against a real bottleneck rather than against the pressure of a
  visible waiting list.
- **RT-02 (Multi-Dimensional Analysis Framework):** supply, loss, lead time, bottleneck, and cost are
  separate axes, which is what surfaces the common case where recruitment is healthy and screening
  throughput is the constraint.
- **CM-02 (Constraint Specification):** screening and training are declared fixed inputs and the
  no-exceptions rule is absolute, so this prompt absorbs capacity pressure rather than transmitting it
  to the readiness assessment.
- **OC-03 (Markdown Table Specification):** the pipeline table forces a loss rate and a stated
  assumption per stage, making a lossless, over-optimistic model structurally impossible to present.
- **QA-01 (Self-Verification):** the check confirms the bar is untouched, loss is modelled everywhere,
  and the bottleneck was identified rather than assumed.

---

## Related Prompts

- [`discipleship_program_health_review.md`](discipleship_program_health_review.md) — where overload and
  unmatched findings originate
- [`../mentor-equipping/discipleship_mentor_readiness_assessment.md`](../mentor-equipping/discipleship_mentor_readiness_assessment.md) —
  the bar this prompt protects from capacity pressure
- [`../mentor-equipping/discipleship_mentor_support_and_sustainability.md`](../mentor-equipping/discipleship_mentor_support_and_sustainability.md) —
  the capacity limit this planning respects
- [`../curriculum-architecture/discipleship_multiplication_design.md`](../curriculum-architecture/discipleship_multiplication_design.md) —
  designing the completer-reproduction supply source
- [`../mentor-equipping/discipleship_mentor_training_curriculum.md`](../mentor-equipping/discipleship_mentor_training_curriculum.md) —
  the training stage whose throughput is often the bottleneck
