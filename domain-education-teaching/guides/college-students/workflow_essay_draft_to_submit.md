---
title: "Workflow: Essay — Draft to Submit"
category: education-teaching/guides/college-students
description: "Full chain for writing a college essay (3–10 pages): topic to thesis to outline to draft to revision to integrity self-check. Uses existing Socratic prompts only — AI does not write the essay."
audience: college-students
chain_length: 7
estimated_time: "4-10 hours over 3-5 sessions"
status: active
updated: "2026-05-13"
---

# Workflow: Essay — Draft to Submit

## Who This Is For

- Undergrad or grad student with a 3–10 page essay assignment
- Single thesis, single argument, supported by 3–8 sources (or a few course readings)
- Submission is graded

If you have 10+ pages with extensive research, use [`workflow_research_paper_full_arc.md`](workflow_research_paper_full_arc.md) instead.

## What You'll Have at the End

- A thesis you constructed (not borrowed from AI)
- An outline you populated
- A draft you wrote, revised by you with AI's diagnostic feedback
- An integrity self-check confirming the submission is genuinely yours

## What You Need to Bring

- The assignment prompt (paste it verbatim into step 1)
- The relevant readings, sources, or course material (you'll quote from them)
- A first guess at what you might argue (even if rough)
- The grading rubric if you have one
- 4–10 hours of focused time spread across at least 3 sessions

**Do not start this workflow the night before submission.** The Socratic prompts will not let you skip thinking, and that takes time.

## The Chain

### Step 1 — Refine your thesis

**Prompt:** [`../../learner-writing/learnwrite_thesis_with_critique.md`](../../learner-writing/learnwrite_thesis_with_critique.md)

**Input:** assignment prompt + your rough thesis attempt

**What you'll get:** diagnostic critique of your thesis (is it arguable, specific, defensible, scoped) and questions that push you to a sharper version

**Carry forward:** the revised thesis you wrote yourself

**Skip if:** your professor assigned the exact thesis. Move to step 2.

---

### Step 2 — Surface counterarguments

**Prompt:** [`../../learner-writing/learnwrite_counterargument_generator.md`](../../learner-writing/learnwrite_counterargument_generator.md)

**Input:** your refined thesis

**What you'll get:** Socratic questions that surface 2–4 plausible counterarguments and the strongest objection a reader could raise

**Carry forward:** the counterargument you'll address in the essay

**Why this is step 2 and not later:** addressing a counterargument is what turns a description into an argument. Doing it before the outline keeps it integral, not bolted on.

---

### Step 3 — Build an outline

**Prompt:** [`../../learner-writing/learnwrite_outline_generator.md`](../../learner-writing/learnwrite_outline_generator.md)

**Input:** thesis + counterargument

**What you'll get:** genre-specific skeleton (intro, body sections, counterargument, conclusion) with empty content slots

**Carry forward:** the outline with your content in it — every slot filled by you

**You will not get:** the outline pre-filled. The prompt refuses to populate slots.

---

### Step 4 — Source credibility check (if research-based)

**Prompt:** [`../../learner-writing/learnwrite_source_credibility_evaluator.md`](../../learner-writing/learnwrite_source_credibility_evaluator.md)

**Input:** the sources you plan to cite

**What you'll get:** lateral-reading / SIFT / CRAAP walkthrough that helps you decide if each source is appropriate to cite

**Carry forward:** a vetted source list

**Skip if:** all sources are required course readings.

---

### Step 5 — Write your draft

Do this without AI assistance for the first pass. Fill the outline with your prose. Quote your sources directly. This is the part the assignment is actually evaluating.

**Time estimate:** 2–4 hours for a 3–5 page essay; 4–6 hours for an 8–10 page essay.

**If you get stuck:** run [`../../../domain-personal-development/prompts/agency/agency_stuck_diagnosis.md`](../../../domain-personal-development/prompts/agency/agency_stuck_diagnosis.md) — diagnose whether you're stuck on understanding, structure, or execution.

---

### Step 6 — Revise with Socratic coaching

**Prompt:** [`../../learner-writing/learnwrite_revision_socratic_coach.md`](../../learner-writing/learnwrite_revision_socratic_coach.md)

**Input:** your complete draft

**What you'll get:** the prompt quotes your sentences and asks diagnostic questions — does this sentence support the thesis? does this transition work? is this claim backed by evidence? — but **does not rewrite your sentences for you.**

**Carry forward:** a revised draft, fully written by you

**Pass count:** 2 passes is typical. Pass 1 surfaces structural issues; pass 2 catches paragraph- and sentence-level problems.

---

### Step 7 — Integrity self-check before submission

**Prompt:** [`../../learner-writing/learnwrite_academic_integrity_self_check.md`](../../learner-writing/learnwrite_academic_integrity_self_check.md)

**Input:** your final draft

**What you'll get:** a structured pre-submission audit — every quote properly attributed, every paraphrase genuinely yours, every AI use within your school's policy, every claim backed by a source you actually read

**Carry forward:** a submittable essay you are confident is yours

## When to Skip Steps

| Situation | Skip |
|-----------|------|
| Prof gave you the thesis | Step 1 |
| No outside sources required | Step 4 |
| Short reflective essay (no formal argument) | Step 2 |
| You're an experienced writer and revision is the constraint | Steps 1–3, jump to 5–6 |
| Submission is a take-home final under time pressure | Don't run this workflow — you'd need to start much earlier |

## Time Budget

| Stage | Time |
|-------|------|
| Steps 1–4 (thesis, counter, outline, sources) | 1–2 hr |
| Step 5 (write draft) | 2–6 hr |
| Step 6 (revise, 2 passes) | 1–2 hr |
| Step 7 (integrity self-check) | 15–30 min |
| **Total** | **4–10 hr** |

**Spread across at least 3 sessions** so your subconscious does part of the work between sittings. The biggest leverage in essay writing is sleeping between draft and revision.

## Common Failure Modes

| Failure | What to do |
|---------|-----------|
| **"The AI won't write my thesis for me."** | That's by design. Run step 1 again with a sharper attempt; the prompt is designed to push you to better thinking, not produce a finished thesis. |
| **Started step 5 (draft) and froze.** | You probably don't actually know what you're arguing. Go back to step 1. |
| **Revision feedback feels generic.** | Quote specific passages into the revision coach instead of pasting the whole draft. The prompt works on the text you give it. |
| **Running out of time, considering pasting AI prose.** | Stop. Use what you have, take the lower grade, learn the lesson. Pasted AI text is detectable and a violation of every integrity policy this guide cares about. Better essay next time. |
| **Got AI to write a passable thesis by tricking it.** | You'll be unable to defend it in class or on a follow-up. The thesis isn't yours; the argument that flows from it won't be yours either; the grader will likely notice the disconnect. |

## What This Workflow Is Not

- A way to write the essay faster than you could without AI
- A way to write the essay without doing the reading
- A way to outsource the thinking

The workflow is faster than writing without AI **on the thinking-clarification and feedback steps**, not on the actual prose. Expect to spend roughly as much time on step 5 (drafting) as you would have without AI — because there is no AI shortcut for the writing itself, and that's the whole point.

---

*Part of [`../college-students/GUIDE.md`](GUIDE.md). For research papers, see [`workflow_research_paper_full_arc.md`](workflow_research_paper_full_arc.md).*
