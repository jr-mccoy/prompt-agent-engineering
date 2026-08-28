---
title: "Education Guides: College & Adult Learner Edition"
category: education-teaching/guides
description: "Front-door for learners. Pick your audience — college student, adult returning to school, or career changer — to find workflows, cross-domain prompt kits, and adult-learner-specific tooling."
audience:
  - college-students
  - adult-learners-returning
  - career-changers
status: active
updated: "2026-05-13"
---

# Education Guides: For Learners

These guides exist because no single prompt does what a real student needs. A college thesis, a returning adult's first semester back, a career changer's six-month skill pivot — each pulls together a chain of prompts from across this repo (education, productivity, personal development, prompt engineering). The guides here are the **stitching**: workflows that chain prompts in the right order for the job you're actually doing.

---

## Pick Your Path

| If you are… | Start here |
|-------------|------------|
| A **traditional college student** writing essays, doing research papers, studying for finals, working through STEM problem sets | [`college-students/GUIDE.md`](college-students/GUIDE.md) |
| An **adult returning to school** after years away — working, balancing family, brushing off academic rust | [`adult-returning/GUIDE.md`](adult-returning/GUIDE.md) |
| A **career changer or self-directed adult learner** designing your own skill-pivot path, deciding degree vs. cert vs. bootcamp, building a portfolio while you learn | [`career-changers/GUIDE.md`](career-changers/GUIDE.md) |

If you're not sure, the table below maps common situations to the right path.

| Situation | Path |
|-----------|------|
| "I need to write a 10-page paper for class" | college-students |
| "I haven't written an essay in 17 years and I just enrolled in night classes" | adult-returning |
| "I'm an accountant who wants to be a data analyst — what do I study?" | career-changers |
| "Finals week and I'm drowning" | college-students |
| "I'm 42 in a class of 22-year-olds and I feel out of place" | adult-returning |
| "I'm doing a bootcamp at night and want to build a portfolio while I learn" | career-changers |
| "I need to turn 15 years of work into a CPL portfolio for credit" | adult-returning |
| "I have a 40-hour job, 9 credits this semester, and two kids" | adult-returning |

---

## What's in Each Path

### `college-students/` — Workflow Kit (no new prompts)

All workflows here chain **existing prompts** from `domain-education-teaching/learner/` plus selected productivity/identity prompts. Aimed at traditional 18–22 undergrads and grad students.

- `GUIDE.md` — overview, when to use which workflow
- `workflow_essay_draft_to_submit.md` — topic → thesis → outline → draft → revise → integrity self-check
- `workflow_research_paper_full_arc.md` — question → search → sources → synthesis → draft
- `workflow_exam_prep_finals_week.md` — triage → spaced retrieval → mistake review → test-day strategy
- `workflow_stem_problem_solving.md` — word problem decode → Socratic solve → error analysis
- `workflow_office_hours_and_class_discussion.md` — turn confusion into productive questions
- `learn_workflow_cross_domain_kit.md` — productivity, identity, agency prompts useful at college

### `adult-returning/` — Cold Start + Net-New Tooling

For adults coming back to higher ed after a break — often working, often with families. **Some workflows here ship new prompts** (in `domain-education-teaching/learner/adult-learner/`) that don't exist anywhere else in the repo yet.

- `GUIDE.md` — overview, first-four-weeks ramp
- `workflow_cold_start_return.md` — syllabus decoding, time-on-task recalibration, academic tone rehearsal
- `workflow_working_learner_time_architecture.md` — weekly blocks under job + family constraints
- `workflow_writing_rust_recovery.md` — diagnose what's rusty and rehearse it
- `workflow_imposter_calibration_age_cohort.md` — being 30/40/50+ in age-mixed classes
- `workflow_prior_learning_articulation.md` — turn career experience into CPL portfolio or SOP language
- `learn_workflow_cross_domain_kit.md` — deep-work, identity, agency, career-transformation kit

### `career-changers/` — Self-Directed Skill Pivot

For adults pivoting to a new field via degree, cert, bootcamp, MOOC, or self-study. Partially built on existing `career-transformation/` and `agency/` prompts; **ships 3 new prompts** for the self-study planning gap.

- `GUIDE.md` — overview, pivot stages
- `workflow_skill_pivot_self_study_plan.md` — diagnostic → target competence → 3/6/12-month plan
- `workflow_credential_pathway_decision.md` — degree vs. cert vs. bootcamp vs. MOOC vs. OJT
- `workflow_portfolio_while_learning.md` — ship public artifacts before mastery
- `workflow_proof_of_work_for_pivot.md` — adapts existing proof-of-work portfolio prompt for pivot context
- `learn_workflow_cross_domain_kit.md` — career-transformation, agency, identity, bottlenecks kit

### `shared/` — Cross-Cutting Foundations

Read these once; they inform how every workflow in this guide section operates.

- `andragogy_principles.md` — adult learning theory (Knowles, Mezirow) applied to prompt design
- `socratic_vs_direct_decision.md` — when AI should coach vs. when it should answer directly
- `ai_as_study_partner_integrity.md` — academic integrity for self-directed adult learners
- `prompt_index_for_learners.md` — curated cross-domain index across ~115 prompts

---

## The Cross-Domain Reality

A typical college student's needs touch **3 domains** in this repo. A typical adult returner's needs touch **6**. A career changer's path touches **7**. The relevant prompts are scattered:

| Domain / Path | What it covers | Prompts |
|---------------|----------------|--------:|
| `domain-education-teaching/learner/` | Writing, research, study, time, reading, math/science | 40 |
| `domain-education-teaching/learner/adult-learner/` | Adult-specific: cold-start, time architecture, writing rust, imposter, prior learning, skill-pivot, credential pathway, portfolio-while-learning, andragogy workflow | 9 (new) |
| `domain-personal-development/career-transformation/` | Coordination tax, role vulnerability, residual skills, 90-day repositioning | 4 |
| `domain-personal-development/prompts/agency/` | Ownership, execution, skill-gap reframe, foundation session, proof-of-work, weekly review | 15 |
| `domain-personal-development/prompts/identity/` | Confidence, comparison, values, life audit, purpose, taste | 7 |
| `domain-productivity/deep-work/` | Focus, calendar audit, future-self handoff, project chunking | 20 |
| `domain-productivity/bottlenecks/` | Procrastination, perfectionism, capture/triage, PKM | 8 |
| `domain-productivity/reviews/` | Weekly systems, monthly cadence, time audit | 3 |
| `domain-prompt-engineering/skill-development/` | Using AI as a learning partner, eval harness, four-discipline diagnostic | ~8 |

**Total relevant inventory: ~115 prompts.** This guide section makes them findable in the order you actually need them.

---

## How to Read a Workflow Guide

Every `workflow_*.md` in this section uses the same structure:

1. **Who this is for** — audience and stage
2. **What you'll have at the end** — deliverable
3. **What you need to bring** — inputs / state
4. **The chain** — numbered sequence of prompts to run, in order, with handoff notes between them
5. **When to skip steps** — variations
6. **Time budget** — realistic hours
7. **Common failure modes** — what to watch for

You can run a workflow in one sitting or spread it across days. Each step names the exact prompt file and what you're carrying forward to the next step.

---

## Related Resources

- [`../../README.md`](../../README.md) — full education domain catalog (130+ prompts including K-12, instructor-side, and corporate)
- [`../../field_guide.md`](../../field_guide.md) — prompt engineering techniques specific to education
- [`../../../NON_CODING_QUICK_START.md`](../../../NON_CODING_QUICK_START.md) — universal non-coding prompt principles
- [`../../../PROMPT_INDEX.md`](../../../PROMPT_INDEX.md) — searchable index across all 2000+ prompts

---

*Audience: learners (college, returning adult, career changer). Authored: 2026-05-13.*
