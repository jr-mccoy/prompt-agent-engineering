---
title: "Journal Club Facilitation Guide Designer"
category: science/teaching-research-methods
description: "Build a journal-club facilitation package: paper-selection criteria (including teaching with flawed papers), pre-read guiding questions, an in-room plan that gets everyone participating and teaches structured critical appraisal, a reusable appraisal question bank, and a follow-up action step."
techniques:
  - ST-01
  - RT-01
  - RT-03
  - QA-01
  - CM-02
  - NE-10
difficulty: advanced
tags:
  - journal-club
  - critical-appraisal
  - facilitation
  - reproducibility
  - peer-review
  - research-training
  - open-science
  - lab-culture
updated: "2026-06-26"
related_prompts:
  - domain-science/teaching-research-methods/science_research_methods_syllabus_designer.md
  - domain-science/teaching-research-methods/science_undergraduate_lab_course_designer.md
  - domain-science/methods-foundations/science_confound_and_bias_audit.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
---

# Journal Club Facilitation Guide Designer

**Objective:** Produce a complete facilitation package for a research-group or course journal club that turns reading a paper into training in structured critical appraisal — separating claims from evidence, interrogating design and statistics, and probing reproducibility — while getting every participant to contribute rather than letting one or two people dominate. The package includes paper-selection criteria, pre-read guiding questions, a timed in-room facilitation plan, a reusable appraisal question bank, a rotation plan, and a concrete follow-up/action step.

**When to use:** You run or are launching a journal club and want a repeatable structure that teaches appraisal skills, builds an inclusive discussion culture, and produces follow-through — not just a once-over of whatever paper is convenient.

**Required inputs:**
- **Discipline.** Field and sub-area, so appraisal questions target the methods that matter (e.g., wet-lab controls, observational confounding, computational reproducibility, field sampling).
- **Level / audience.** Mix of the group (undergrads, grad students, postdocs, PIs), group size, and prior appraisal experience.
- **Cadence & format.** Frequency, session length, in-person/remote/hybrid, and whether attendance is for a course or a lab.

**Optional inputs:**
- **The specific paper(s)** under discussion (user-supplied — the guide will not select or invent papers).
- **Learning goals** (e.g., "teach power analysis," "build reproducibility instincts," "practice peer-review writing").
- **Recurring problems** to fix (silence, domination, surface-level praise, no follow-up).
- **Whether the club ties to a methods course** so it can reuse that course's outcomes.

**Constraints — Must:**
- Provide paper-selection criteria that weigh methodological teachability and relevance, and explicitly include selecting *flawed or contested* papers for critical-appraisal practice (clearly framed as a teaching choice, not an attack).
- Structure appraisal around separating claims from evidence, scrutinizing design and statistics, and assessing reproducibility/data-and-code availability.
- Build a facilitation plan that distributes participation (assigned roles, think-time, round-robin or small-group steps) so discussion isn't dominated by a few voices.
- Deliver a reusable critical-appraisal question bank organized by appraisal dimension that works across papers.
- End every session with a follow-up/action step (e.g., a method to try, a reproducibility check, a short written critique, a question to email authors).
- Keep critique rigorous *and* charitable: appraise the work, model constructive scientific disagreement, and avoid ad hominem framing.

**Constraints — Must Not:**
- Do not invent institutional/course requirements, papers, or citations the user hasn't supplied. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not invent, name, summarize, or critique specific papers the user did not provide; papers are user-supplied.
- Do not use "novel," "groundbreaking," "first-ever," or "gold standard" in any drafted materials.
- Do not frame critical appraisal as paper-bashing; flaws are teaching material, and authors are treated with professional respect.
- Do not duplicate generic facilitation/classroom-management theory — reference `domain-education-teaching/` for it and keep this output about appraising research.

**Instructions:**

1. **Confirm discipline, audience, and cadence.** Restate field, group composition, size, format, and frequency, and note any stated learning goals or recurring problems to solve.
2. **Set selection criteria.** Define how papers get chosen: methodological teachability, relevance to the group, variety of designs, and deliberate inclusion of flawed/contested papers for appraisal practice — with a note on framing those respectfully. Papers themselves stay `[user-supplied]`.
3. **Write pre-read guiding questions.** Provide questions participants answer *before* the session that force engagement with the paper's claims, evidence, design, statistics, and reproducibility — not just a read-through.
4. **Design the in-room plan.** Lay out a timed agenda with facilitation roles (lead, methods critic, stats critic, reproducibility checker, devil's advocate) and participation mechanics (think-time, small groups, round-robin) so everyone contributes. Reference `domain-education-teaching/` for generic facilitation mechanics.
5. **Teach structured appraisal.** Walk the group through claims-vs-evidence separation, design/confound scrutiny (`domain-science/methods-foundations/science_confound_and_bias_audit.md`), statistical critique, and reproducibility/data-and-code assessment (`domain-science/methods-foundations/science_reproducibility_self_audit.md`).
6. **Build the question bank.** Produce a reusable, dimension-organized appraisal question bank (claims & framing; design & controls; sampling & power; statistics & inference; reproducibility & transparency; interpretation & overreach) usable for any future paper.
7. **Design the rotation.** Create a rotation plan for who leads/serves each role across sessions so responsibility and skill-building are shared.
8. **Define the follow-up.** Specify a per-session action step that converts discussion into practice (try a method, run a reproducibility check, draft a referee-style critique, log a calibrated takeaway).
9. **Surface assumptions and gaps.** List `[user-supplied]` items and assumptions, and note how the facilitator will iterate the format.

**Output format (locked):**

```
## Journal Club Setup
- Discipline / audience / group size:
- Cadence, session length, format:
- Learning goals / problems to solve:

## Paper-Selection Criteria
[Teachability, relevance, design variety; how and why to include flawed/contested papers; respectful framing. Papers remain [user-supplied].]

## Pre-Read Guiding Questions
[Questions participants complete before the session, spanning claims, evidence, design, stats, reproducibility]

## In-Room Facilitation Plan
| Time | Segment | Facilitation move / role | Participation mechanic |
|---|---|---|---|
[Roles: lead, methods critic, stats critic, reproducibility checker, devil's advocate]

## Critical-Appraisal Question Bank (reusable)
- Claims & framing:
- Design & controls:
- Sampling & power:
- Statistics & inference:
- Reproducibility & transparency:
- Interpretation & overreach:

## Rotation Plan
| Session | Lead | Methods critic | Stats critic | Reproducibility checker |
|---|---|---|---|---|

## Follow-Up / Action Step
[Per-session step that converts discussion into practice]

## Assumptions & [user-supplied] Items
- Items to supply (papers, goals):
- Assumptions made:
- Iteration plan:
```

**Reporting-standard alignment:** No formal reporting standard; aligns to structured critical-appraisal practice, peer-review training, and Open-Science pedagogy (reproducibility, data/code transparency). For generic facilitation theory, see `domain-education-teaching/`.

**Verification checklist (before delivering):**
- [ ] Selection criteria weigh teachability and include flawed/contested papers, framed respectfully.
- [ ] Pre-read questions force engagement with claims, evidence, design, stats, and reproducibility.
- [ ] The in-room plan distributes participation via roles and mechanics so no one dominates.
- [ ] Appraisal explicitly separates claims from evidence and probes design, statistics, and reproducibility.
- [ ] A reusable, dimension-organized question bank is included.
- [ ] A rotation plan and a per-session follow-up/action step are present.
- [ ] No invented or summarized papers; papers remain `[user-supplied]`; no fabricated requirements or citations.
- [ ] No banned hype terms; critique is charitable and free of ad hominem framing.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Praise session | Discussion stays at "interesting paper," no real appraisal | Pre-read + question bank force claims-vs-evidence and design scrutiny |
| One-voice domination | A structure that lets the PI or one student carry the room | Build assigned roles, think-time, round-robin, and a rotation plan |
| Paper-bashing | Critique slides into attacking authors | Frame flaws as teaching material; require respectful, work-focused critique |
| No follow-through | Good discussion that changes nothing | Mandatory per-session action step converting talk into practice |
| Invented paper content | Filling in a plausible-sounding study to look complete | Keep papers `[user-supplied]`; never name, summarize, or critique unsupplied work |
| Reproducibility skipped | Appraisal covers stats but ignores data/code availability | Question bank and roles include a reproducibility/transparency dimension |
