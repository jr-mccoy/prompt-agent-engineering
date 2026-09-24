---
title: "Usability Test Plan — Research Questions, Tasks, Recruiting, and Success Metrics Before Anyone Is Scheduled"
category: frontend-development/ux-research
description: "Design a usability study for a web or app interface before sessions are booked: decision-linked research questions, method choice (moderated/unmoderated, remote/in-person), realistic scenario tasks with observable success criteria, a screener and sample size justified by the method, and the metrics that will be recorded — distinct from the moderator's word-for-word script and from the post-study findings log."
techniques:
  - ST-01
  - CM-03
  - DS-02
  - RT-05
  - QA-01
difficulty: intermediate
tags:
  - ux-research
  - usability-testing
  - study-design
  - recruiting
  - task-design
  - metrics
updated: "2026-09-24"
related_prompts:
  - domain-frontend-development/ux-research/frontend_ux_moderated_session_script.md
  - domain-frontend-development/ux-research/frontend_ux_usability_findings_severity_log.md
  - domain-agentic-resources/personas/design/design_ux_researcher.md
---

# Usability Test Plan

**Objective:** Produce a study plan that a team can approve and a recruiter can
act on: every research question tied to a pending design decision, every task
written as a realistic scenario with an observable success criterion, and every
metric named before the first participant is seen.

**When to Use:**
- A design, prototype, or live flow needs evidence before a decision (ship,
  redesign, pick between two variants).
- Stakeholders want "some user testing" and nobody has written down what it
  must answer.
- Previous rounds produced interesting sessions and no decisions.

**Not this prompt if:**
- You have the plan and need the moderator's actual words — intro, think-aloud
  instructions, neutral probes → `frontend_ux_moderated_session_script.md`.
- Sessions are done and you need to rate problems → `frontend_ux_usability_findings_severity_log.md`.
- You want an expert review without users → `frontend_ux_heuristic_evaluation.md`.
- You need open-ended discovery interviews, not task-based testing →
  `domain-research-academic/research_interview_guide_designer.md`.
- Distinct from `domain-agentic-resources/personas/design/design_ux_researcher.md`,
  a general-purpose role persona; this prompt is the single study-design artifact.

## Inputs

1. **The decision** the study must inform, and who makes it, by when.
2. **The artifact**: live URL, prototype fidelity, or build; which flows exist.
3. **Target users**: who uses this, and who must be excluded (employees,
   power users if testing first-run, etc.).
4. **Constraints**: budget, incentive, calendar window, tooling
   (e.g. remote moderated video, unmoderated platform), accessibility needs.
5. **Prior evidence**: analytics, support tickets, earlier rounds.

If the decision is missing, stop and ask. A study without a decision is a demo.

## Method

1. **State the decision and research questions (ST-01).** Write one decision
   sentence, then 2–5 research questions. Each question must name what answer
   would change the decision. Delete any question whose every answer leads to
   the same action.
2. **Bound the scope (CM-03).** List flows in scope, flows explicitly out of
   scope, and the prototype's dead ends (so the moderator can steer around them).
3. **Choose the method with a stated reason.**
   | Situation | Default method |
   |---|---|
   | Early prototype, "why" matters | Moderated, remote or in-person |
   | Mature flow, comparing variants on time/success | Unmoderated, larger n |
   | Accessibility or assistive-tech users | Moderated, participant's own setup |
   | Findability of labels, not layout | Tree test → `frontend_ux_card_sort_tree_test.md` |
4. **Write scenario tasks.** For each: a goal the user would really have, no UI
   vocabulary from the screen ("find the Billing tab" leaks the answer), a
   start state, and an **observable success criterion** (reaches page X with
   Y set). Order from low to high stakes; put the most decision-critical task
   no later than second.
5. **Define metrics before data exists (DS-02).** Per task: completion
   (success / partial / fail by the criterion), time on task (only if
   unmoderated or no think-aloud), errors, and a post-task SEQ. Per session:
   SUS or UMUX-Lite (`frontend_ux_standardized_survey_sus.md`).
6. **Size and screen the sample (RT-05).** Justify n by purpose: ~5 per
   distinct user segment for problem discovery in a qualitative round;
   benchmark/comparison metrics need far larger samples and a confidence
   interval. Write screener questions that select behaviour, not
   self-description, and include one disqualifier the recruiter can check.
7. **Plan logistics and ethics.** Consent, recording, data retention,
   incentive, pilot session, observer rules.
8. **Self-check (QA-01).** Run the Verification list; revise before sharing.

## Output Format

```
# Usability test plan — [product / flow]
Decision: [one sentence] — owner [role], needed by [date]

## Research questions
| # | Question | Answer that would change the decision |

## Scope
In: [...]  Out: [...]  Known prototype dead ends: [...]

## Method
[method] — because [reason tied to decision and fidelity]

## Tasks
| # | Scenario (user's words) | Start state | Success criterion | Maps to RQ |

## Metrics
Per task: [...]   Per session: [...]   Not collected, and why: [...]

## Participants
Segments × n: [...] — justification: [...]
Screener: [questions, with qualify/disqualify rules]

## Logistics & ethics
Consent · recording · retention · incentive · pilot date · observer rules

## Risks to validity
[...]
```

## Verification

- [ ] Every research question names the answer that would change the decision.
- [ ] No task wording uses a label that appears on the screen being tested.
- [ ] Every task has an observable success criterion, not "understands X".
- [ ] Sample size is justified by purpose (discovery vs benchmark).
- [ ] Time-on-task is not reported from think-aloud sessions.
- [ ] A pilot session is scheduled before the first real one.

## False-Positive Prevention

1. **"Five users is enough" is a discovery heuristic, not a benchmark.** Do
   not plan to report completion percentages from n=5 as if they generalise.
2. **Leading task wording is a plan defect, not a moderator defect.** If the
   task says "use the filter", the filter's findability is untested.
3. **Screeners that ask "Are you tech-savvy?" select self-image.** Ask what
   they did in the last 30 days instead.
4. **A preference question is not a usability task.** "Which design do you
   like?" measures taste; plan it separately or drop it.
5. **Do not test what analytics already answers.** If 60% abandon step 3,
   the study question is *why*, not *whether*.
6. **Prototype gaps are not user failures.** List dead ends in scope so a
   participant hitting one is not scored as a fail.

## Example Output

```
# Usability test plan — Team-plan checkout (Figma prototype v4)
Decision: ship the single-page checkout or keep the 3-step flow for Q4 —
owner Head of Growth, needed by 2026-10-15

## Research questions
| # | Question | Answer that would change the decision |
|---|---|---|
| 1 | Can admins add seats and pay without help? | ≥2 of 6 fail seat step → keep 3-step |
| 2 | Is the proration line understood before paying? | Misread by most → add explainer before ship |
| 3 | Does the invoice-billing option get found by those who need it? | Not found by invoice segment → surface it |

## Scope
In: plan select → seats → payment → confirmation.
Out: trial sign-up, SSO setup.
Known dead ends: "Edit company address" link is not wired — moderator redirects.

## Method
Remote moderated, 45 min — fidelity is a clickable prototype and RQ2 needs "why".

## Tasks
| # | Scenario | Start | Success criterion | RQ |
|---|---|---|---|---|
| 1 | Your team grew to 12; get everyone access this month | Plan page, 5 seats | Confirmation shows 12 seats | 1 |
| 2 | Before paying, tell me what you'll be charged today and why | Payment step | States prorated amount and reason | 2 |
| 3 | Finance needs a bill they can pay by transfer | Payment step | Selects invoice option | 3 |

## Metrics
Per task: success/partial/fail, errors, SEQ. Per session: UMUX-Lite.
Not collected: time on task (think-aloud inflates it).

## Participants
Card-paying admins × 3, invoice-paying admins × 3 — discovery round, n per segment.
Screener: "In the last 90 days, did you add or remove paid seats for your team?"
(yes → continue); "How does your company usually pay software bills?" (sorts segment);
disqualify anyone employed by a billing-software vendor.

## Logistics & ethics
Recorded with consent; recordings deleted after 90 days; $75 incentive;
pilot 2026-10-01 with an internal non-designer.

## Risks to validity
Prototype shows static prices, so RQ2 depends on the explainer copy only.
```

## Techniques Used

- **ST-01 Clear Objective Statement** — the plan starts from one decision sentence.
- **CM-03 Scope Definition** — in/out flows and known prototype dead ends.
- **DS-02 Metric Specification** — metrics fixed per task before data exists.
- **RT-05 Evidence-Based Reasoning** — sample size and method justified by purpose.
- **QA-01 Self-Verification** — checklist run before the plan circulates.

## Related Prompts

- `frontend_ux_moderated_session_script.md` — the moderator's words for this plan.
- `frontend_ux_usability_findings_severity_log.md` — rating what the sessions found.
- `frontend_ux_standardized_survey_sus.md` — SUS / UMUX-Lite / SEQ scoring.
- `domain-agentic-resources/personas/design/design_ux_researcher.md` — the role persona.
