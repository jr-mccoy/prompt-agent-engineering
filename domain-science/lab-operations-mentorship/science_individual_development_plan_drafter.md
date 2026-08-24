---
title: "Individual Development Plan (IDP) Drafter"
category: science/lab-operations-mentorship
description: "Draft a trainee-owned, NIH-style Individual Development Plan that moves from honest self-assessment through multi-path career exploration to SMART milestones and a mutual mentor–mentee compact."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-01
  - CM-02
difficulty: advanced
tags:
  - individual-development-plan
  - mentorship
  - career-development
  - trainee-growth
  - myidp
  - mentor-mentee-compact
  - skills-assessment
  - milestones
updated: "2026-06-26"
related_prompts:
  - domain-science/lab-operations-mentorship/science_one_on_one_mentorship_session_plan.md
  - domain-science/lab-operations-mentorship/science_lab_onboarding_packet_designer.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
---

# Individual Development Plan (IDP) Drafter

**Objective:** Help a research trainee and their advisor co-produce an Individual Development Plan (IDP) the trainee owns. The plan structures honest self-assessment of skills, values, and interests; explores multiple career paths (not only academic faculty); converts findings into SMART goals with milestones; and closes with a mutual mentor–mentee compact. The output is a working document the pair revisits, not a one-time form.

**When to use:** At the start of a training period (rotation, PhD year, postdoc start), at an annual review, or when a trainee feels directionless and needs a structured way to set goals and surface what they need from their advisor.

**Required inputs:**
- **Discipline.** The trainee's research field and subfield.
- **Career stage.** Where the trainee is (e.g., undergraduate researcher, graduate student year N, postdoc year N, staff scientist), since milestones and career options differ sharply by stage.
- **Self-assessment material.** The trainee's own ratings or notes on technical skills, transferable skills (writing, presenting, project management, mentoring), values, and interests. If absent, the prompt generates a self-assessment worksheet for the trainee to complete rather than guessing.

**Optional inputs:**
- Career paths the trainee is curious about or has ruled out.
- Time horizon for this IDP cycle (e.g., 12 months).
- Known constraints (visa timeline, funding end date, family/geographic constraints) — only if the trainee chooses to share.
- Existing program or funder IDP requirements to align to.

**Constraints — Must:**
- Frame the IDP as trainee-owned; the advisor's role is to support, not dictate. Use the trainee's voice in goals.
- Structure the plan in the canonical IDP sequence: self-assessment → career exploration → goal-setting → mentor–mentee compact, consistent with the NIH IDP expectation and the AAAS/Science Careers myIDP framework.
- Present multiple career destinations (academic research, industry/biotech/pharma, government, science policy, teaching-focused, science communication, data science, regulatory, entrepreneurship, etc.), not academia by default.
- Make goals SMART (specific, measurable, achievable, relevant, time-bound) and attach milestones with dates the trainee proposes.
- Build the compact as reciprocal: list commitments from both trainee and mentor (modeled on the AAMC mentor–mentee compact concept).
- Note that the IDP is a living document with a stated revisit date.

**Constraints — Must Not:**
- Do not invent institutional policies, named people, performance facts, or career statistics. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not assert placement rates, salary figures, or "most trainees do X" claims from memory; mark them `[user-supplied — verify against current data]`.
- Do not fill in self-assessment ratings the trainee did not provide; generate the worksheet instead.
- Do not use hype language ("novel," "groundbreaking," "first-ever," "gold standard") in any drafted text.
- Do not position the IDP as a clinical, performance-management, or disciplinary instrument.

**Instructions:**

1. **Confirm scope.** Read discipline, career stage, and self-assessment material. If self-assessment is missing, produce the self-assessment worksheet (Step 2) and pause for the trainee to complete it before goal-setting.
2. **Self-assessment.** Organize the trainee's input into three lenses — skills (technical + transferable), values, and interests. For each, surface strengths, growth areas, and one or two honest blind-spot prompts. Keep ratings as the trainee supplied them; never upgrade or invent.
3. **Career exploration.** List candidate career paths relevant to the discipline and stage, each with the core competencies it rewards and a low-cost next exploration step (informational interview, shadowing, a course, an internship). Tie each path back to the trainee's stated values and interests so fit is visible.
4. **Gap analysis.** For the path(s) the trainee leans toward, map required competencies against the self-assessment to name the two or three highest-leverage development areas. Avoid an exhaustive list — prioritize.
5. **SMART goals + milestones.** Write 3–6 goals in the trainee's voice, each measurable and time-bound, with intermediate milestones and proposed dates. Cover at least one research goal, one skill/career goal, and one well-being or sustainability goal.
6. **Resources and support.** For each goal, note what the trainee needs (training, funding, time, introductions, feedback) and who/what could provide it — flag any institution-specific resource as `[user-supplied]`.
7. **Mentor–mentee compact.** Draft reciprocal commitments: what the trainee commits to (e.g., progress updates, meeting prep, taking ownership) and what the mentor commits to (e.g., timely feedback, advocacy, regular meetings, supporting non-academic exploration). Keep it specific and revisable.
8. **Revisit plan.** State a review cadence and date, and a one-line note that goals can change as the trainee learns more.
9. **Hand-off note.** Add a short note to the trainee on how to use this in their next 1:1, and to the advisor on how to support without taking over ownership.

**Output format (locked):**

```
## IDP Overview
- Trainee career stage: [...]
- Discipline / subfield: [...]
- IDP cycle horizon: [...]
- Owned by: trainee | Supported by: advisor
- Next revisit date: [...]

## 1. Self-Assessment
### Skills (technical + transferable)
| Skill | Trainee rating (as supplied) | Strength / Growth area |
|---|---|---|
### Values
[bulleted, trainee's words]
### Interests
[bulleted]
### Blind-spot prompts
[1–2 honest reflection questions]

## 2. Career Exploration
| Career path | Core competencies rewarded | Fit with stated values/interests | Low-cost next step |
|---|---|---|---|

## 3. Gap Analysis (top development areas)
1. [...]
2. [...]
3. [...]

## 4. SMART Goals & Milestones
| Goal (trainee voice) | Type (research/skill/well-being) | Measure of success | Milestones + dates | Support needed |
|---|---|---|---|---|

## 5. Mentor–Mentee Compact
**Trainee commits to:**
- [...]
**Mentor commits to:**
- [...]
**Shared:**
- Revisit cadence: [...]

## 6. How to Use This
- For the trainee: [...]
- For the advisor: [...]
```

**Reporting-standard alignment:** No formal reporting standard; aligns to the NIH IDP requirement for graduate students and postdocs, the AAAS/Science Careers myIDP framework, and the AAMC mentor–mentee compact concept. Career-assessment items reflect responsible, individualized assessment in the spirit of DORA (judge contribution and growth, not journal-name proxies).

**Verification checklist (before delivering):**
- [ ] Discipline and career stage captured before any goal-setting.
- [ ] Self-assessment uses only trainee-supplied ratings, or a worksheet was generated instead.
- [ ] At least three distinct career paths presented, including non-academic options.
- [ ] Every goal is specific, measurable, and time-bound, with at least one well-being goal.
- [ ] Compact lists reciprocal commitments for both trainee and mentor.
- [ ] No invented policies, names, placement rates, or salary figures; gaps marked `[user-supplied]`.
- [ ] No hype adjectives in drafted text.
- [ ] A revisit date and "living document" note are present.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Advisor capture | A polished IDP that actually encodes the PI's agenda for the trainee | Keep goals in the trainee's voice; state trainee ownership explicitly in the overview |
| Academia-default bias | "Career exploration" that lists only faculty-track steps | Require ≥3 paths spanning sectors; tie each to stated values |
| Fabricated career data | Confident placement/salary numbers that read as researched | Mark all such figures `[user-supplied — verify]`; never assert from memory |
| Hollow SMART goals | Goals that sound measurable but have no metric or date | Reject any goal lacking an explicit measure and milestone date |
| One-and-done form | A complete-looking IDP treated as final | Require a revisit cadence + date and a living-document note |
