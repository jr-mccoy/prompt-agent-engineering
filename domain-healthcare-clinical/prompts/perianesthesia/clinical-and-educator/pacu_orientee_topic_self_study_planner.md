---
title: PACU Orientee Topic Self-Study Planner
category: pacu/orientation-curriculum
task_type: CREATE
audience: PACU orientee planning their own next-2-weeks self-study
intended_use: orientee learning tool
updated: "2026-05-15"
tags:
  - pacu
  - orientation
  - self-study
  - orientee
techniques:
  - ST-01
  - ST-02
  - RT-02
  - ED-02
  - DS-06
difficulty: beginner
related_prompts:
  - prompts/pacu_self_directed_learning_module_designer.md
  - prompts/pacu_orientee_question_log_builder.md
  - prompts/pacu_orientee_reflective_journal_prompts.md
  - prompts/pacu_topic_primer.md
references:
  - ASPAN Standards of Perianesthesia Nursing Practice
  - Drain's PeriAnesthesia Nursing Practice (7th ed.)
---

# PACU Orientee Topic Self-Study Planner

> Safety reminder: Self-study supplements bedside teaching. It does not change your scope of practice or facility protocols.

## Objective

Help a PACU orientee build a **2-week self-study plan** organized around their actual shift exposure gaps and recurring cueing moments — not a generic reading list.

## Inputs

- **Current orientation week:** {{n}}
- **Shifts coming up (next 2 weeks):** {{day pattern + likely surgical mix}}
- **Topics you keep getting cued on:** {{from question log + journal + preceptor debrief}}
- **Topics you have NOT been exposed to yet:** {{from your shift log}}
- **Time available off-shift for study:** {{hours / week}}

## Audience / Scope

- **Primary:** Orientee, self-use.
- **Secondary:** Primary preceptor can review the plan and suggest swaps.
- **Scope:** Two-week study plan. Single-topic deep dive: use `pacu_self_directed_learning_module_designer.md`.

## Output requirements

```markdown
# My 2-Week Self-Study Plan — Wk {n} to Wk {n+1}

> This is my plan. My preceptor reviews it; I own it.

## My current state

- Topics I keep getting cued on: {3–5 from input}
- Topics I have not been exposed to yet: {3–5 from input}
- My biggest "I think I know this but I'm not sure" topic: {1}
- Time I have: {hours/week}

## What I want to be able to do in 2 weeks

Three concrete behaviors:
1. {behavior 1 — e.g., "recognize post-spinal hypotension on the second cycle without preceptor cue"}
2. {behavior 2}
3. {behavior 3}

Anchor behaviors in cueing-decay language (with cue / without cue), not "understand" or "know."

## Week 1 plan

| Day | What I'm doing off-shift | Source | Time |
|---|---|---|---|
| Mon eve | Re-read post-spinal hypotension primer | `pacu_topic_primer.md` / *Drain's* regional chapter | 30 min |
| Tue eve | Self-directed module on the topic | use `pacu_self_directed_learning_module_designer.md` | 60 min |
| Wed off-shift | Apply on Wed shift: lead two spinal admissions, log cues | shift | n/a |
| Thu eve | Write up what I noticed on Wed shift; bring to preceptor Fri | journal | 15 min |
| Fri off | Read PONV pre-arrival recognition material | *Drain's* PONV chapter | 30 min |

## Week 2 plan

(Similar structure, focused on the next behavior target.)

## What I will NOT study

3–5 topics I'm tempted to study but don't need in the next 2 weeks. Naming them out loud reduces scope creep.

## Mid-plan check (end of Week 1)

After Wk 1 shifts, I check:
- Did I do the behaviors I targeted?
- What surprised me?
- Did I cue myself or did my preceptor cue me?

If a behavior didn't shift: rerun this planner.

## Bring to preceptor (5 min, Mon week 1)

Share the plan. Ask:
1. Does this match what you'd choose for me?
2. Is there something I'm not naming that you'd add?
3. Is there a shift assignment that would help one of these behaviors?

## What this plan is not

- Not an evaluation rubric.
- Not a contract.
- Not something my preceptor grades.

## Sources

- *Drain's*, {chapters relevant to my topics}.
- *Core Curriculum*, {modules}.
- Toolkit prompts: as noted in the table.
```

## Must / Must not

**Must:**
- Anchor behaviors in cueing-decay language (with cue / without cue / on which trigger).
- Tie each study item to a specific shift opportunity to apply it.
- Include the "what I will not study" list to limit scope.
- Build a mid-plan check.
- Keep it owned by the orientee (preceptor reviews; doesn't dictate).

**Must not:**
- Project a fixed grade or threshold.
- Treat the plan as a contract.
- Generate generic "read these chapters" lists without bedside ties.
- Recommend study items beyond current orientation scope.
- Reference protected characteristics.
- Generate study items that pressure the orientee outside the declared time budget.

## Quality signals

- The orientee can hand the plan to their preceptor in 30 seconds and have a meaningful conversation.
- Each study item has a paired shift application.
- The "will not study" list is honest, not strategic.

## Verification

- [ ] Behaviors named in cueing-decay terms.
- [ ] Each study item has a paired shift application.
- [ ] "Will not study" list present.
- [ ] Mid-plan check scheduled.
- [ ] Orientee ownership explicit.
- [ ] Safety + FPP sections present.

## False-Positive Prevention

- **No invented Drain's / Core Curriculum chapter or page numbers.**
- **No invented orientation requirements** ("you must complete 8 self-study modules").
- **No invented competency thresholds.**
- **No invented preceptor expectations.**
- **No protected-characteristic study item selection.**
- **No license-pathway-based study items.**
- **No pressure assertions** ("if you don't study you'll fall behind") — neutral framing.

## Worked Example

<details>
<summary>Example: Wk 3 orientee, 4 hrs/week off-shift, post-spinal + PONV pre-recognition targets (click to expand)</summary>

```markdown
# My 2-Week Self-Study Plan — Wk 3 to Wk 4

## My current state

- Cued on: post-spinal hypotension trend recognition, PONV pre-arrival risk, regional block resolution.
- Not yet exposed: significant blood-loss hemodynamics, urology cases.
- "Think I know but not sure": SBAR placement on Recommendation.
- Time: 4 hrs / week.

## What I want to do in 2 weeks

1. Recognize post-spinal trend on second cycle without preceptor cue.
2. Verbalize PONV risk before patient symptoms appear.
3. Place a clear Recommendation in every SBAR escalation.

## Week 1 plan

| Day | What | Source | Time |
|---|---|---|---|
| Mon eve | Re-read post-spinal primer | `pacu_topic_primer.md` + Drain's | 30 |
| Tue eve | Self-directed module on post-spinal | module designer | 60 |
| Wed shift | Apply: lead two spinals if available | n/a | shift |
| Thu eve | Journal what I noticed; SBAR self-review | journal | 30 |
| Fri eve | PONV pre-arrival risk material | Drain's PONV chapter | 60 |

## Week 2 plan

| Day | What | Source | Time |
|---|---|---|---|
| Mon eve | PONV self-directed module | module designer | 60 |
| Tue shift | Apply on first GYN case if available | n/a | shift |
| Wed eve | SBAR practice scripts (3 cases) | journal | 30 |
| Thu shift | Apply SBAR in real escalation | n/a | shift |
| Fri eve | Mid-plan check — what shifted? | journal | 30 |

## What I will NOT study

- Cardiac surgery recovery (not in mix this month)
- Peds (not in mix)
- Bariatric (rare here)
- Crash cart drug doses by memorization (recall vs reasoning — chooseable later)

## Mid-plan check (end of Week 1)

Re-read this section Sat morning.

## Bring to preceptor

Share Mon morning of Wk 3. Ask 3 questions.
```

Notes: behaviors in cueing-decay terms, shift application paired, will-not list present, mid-plan check scheduled.
</details>

## Self-check

- [ ] Behaviors in cueing-decay terms.
- [ ] Each item has shift application.
- [ ] Will-not list present.
- [ ] Mid-plan check scheduled.
- [ ] Orientee ownership explicit.
- [ ] FPP section passed.
