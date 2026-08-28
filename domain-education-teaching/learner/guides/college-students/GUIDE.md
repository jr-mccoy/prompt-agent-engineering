---
title: "College Students Guide"
category: education-teaching/guides/college-students
description: "Workflow guide for traditional college undergrads and grad students. Maps common academic jobs-to-be-done to chains of existing learner-facing prompts plus selected productivity and identity prompts."
audience: college-students
status: active
updated: "2026-05-13"
---

# College Students Guide

This guide is for traditional college students (undergrad and grad, 18–22 typical, full-time enrollment, primary identity = student). If you're returning to school as an adult after a break, see [`../adult-returning/GUIDE.md`](../adult-returning/GUIDE.md) instead — the rhythm and constraints are different.

## What This Guide Does

It tells you **which prompt to run, in what order, for the academic job in front of you.** Every workflow chains existing prompts from `domain-education-teaching/learner-*/` plus selected cross-domain prompts. Zero new prompts are required to use this section.

## The Stance: AI as Study Partner, Not Ghostwriter

Every prompt this guide points you to enforces a strict Socratic stance: AI quotes your text, asks diagnostic questions, names patterns, points to where revision is needed. **It does not write theses, paragraphs, citations, final answers, or finished outlines you could submit as your own work.** If you want to understand why that matters, read [`../shared/ai_as_study_partner_integrity.md`](../shared/ai_as_study_partner_integrity.md).

This isn't an accident or a limitation. The prompts are designed this way because what an undergrad needs from AI in 2026 is calibrated practice and feedback — not a finished product that they didn't build the thinking for.

## Workflow Map

| Your job | Workflow | Time |
|----------|----------|------|
| Write an essay (3–10 pages) | [`workflow_essay_draft_to_submit.md`](workflow_essay_draft_to_submit.md) | 4–10 hr over 3–5 sessions |
| Write a research paper (10+ pages, multiple sources) | [`workflow_research_paper_full_arc.md`](workflow_research_paper_full_arc.md) | 15–40 hr over 2–4 weeks |
| Prep for finals or a major exam | [`workflow_exam_prep_finals_week.md`](workflow_exam_prep_finals_week.md) | 6–20 hr over 1–2 weeks |
| Solve STEM problem sets | [`workflow_stem_problem_solving.md`](workflow_stem_problem_solving.md) | Per problem |
| Prep for office hours or class discussion | [`workflow_office_hours_and_class_discussion.md`](workflow_office_hours_and_class_discussion.md) | 20–45 min |

## Cross-Domain Prompts You'll Want

College students need more than academic-task prompts. The [`cross_domain_kit.md`](cross_domain_kit.md) file points you to:

- **Time and focus** — calendar audit, project chunking, focus-block context capture (from `domain-productivity/deep-work/`)
- **Procrastination and perfectionism** — diagnostics that aren't just "stop procrastinating" (from `domain-productivity/bottlenecks/`)
- **Confidence and comparison** — calibrating against peers, dealing with envy or impostor feelings (from `domain-personal-development/prompts/identity/`)
- **Stuckness and execution** — diagnosing why you can't start, designing tomorrow's first action (from `domain-personal-development/prompts/agency/`)

## When to Use Which Mode

The learner-facing prompts are strictly Socratic. That's right most of the time. But occasionally — when you're under hard deadline and you genuinely need information, not coaching — direct-answer mode is the right tool.

See [`../shared/socratic_vs_direct_decision.md`](../shared/socratic_vs_direct_decision.md) for the decision rule. Short version: if the deliverable is graded work you're going to submit, stay Socratic. If you're trying to understand a concept you'll use later (and won't paste anything into a submission), direct is fine.

## Starting a Workflow

Each workflow guide has the same structure:

1. **Who this is for** — audience and stage
2. **What you'll have at the end** — the deliverable
3. **What you need to bring** — inputs / current state
4. **The chain** — numbered prompt sequence with handoff notes
5. **When to skip steps** — variations for your situation
6. **Time budget**
7. **Common failure modes**

Pick the workflow, scan it once, then start at step 1 with the inputs the workflow asks for. Each step names a specific prompt file you'll open in a new conversation.

## What's NOT in This Guide

- **Subject-specific tutoring** — for math/science problem-by-problem help, the workflow points you to `learnmath_socratic_step_by_step_solver.md` and similar. There's no domain-specific tutor for, say, organic chemistry vs. calculus — the existing Socratic prompts are general enough to handle both.
- **Foreign language coursework** — see `learner-language/` directly; it has its own coaching prompts.
- **Mental health support, accommodations, or disability services** — out of scope. If you're struggling in ways academic prompts can't address, talk to your school's counseling or accessibility services.
- **Grad-school applications** — partially covered by `career-changers/` workflows; otherwise see `domain-personal-development/prompts/agency/`.

## Quick Reference Card

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                 COLLEGE STUDENT QUICK REFERENCE                            ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║  ESSAY: thesis → outline → draft → revise → integrity check               ║
║  RESEARCH PAPER: question → search → synthesize → outline → draft         ║
║  EXAM PREP: triage → spaced retrieval → mistake review → test day         ║
║  STEM: decode → Socratic solve → error analysis → concept map             ║
║  PRE-OFFICE-HOURS: confusion → specific question → seek the answer        ║
║                                                                           ║
║  AI WILL NOT: write theses, paragraphs, citations, finished outlines,     ║
║              final numerical answers, or essays you submit.               ║
║  AI WILL: quote your text, diagnose, ask, point, model the question       ║
║                                                                           ║
║  STUCK? Run agency_stuck_diagnosis.md before re-attempting the workflow.  ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

*Part of [`../README.md`](../README.md). For adult learners, see sibling [`../adult-returning/`](../adult-returning/) and [`../career-changers/`](../career-changers/) sections.*
