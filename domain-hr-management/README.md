# HR & People Management

> Part of the [Non-Coding Quick Start](../NON_CODING_QUICK_START.md) system.
> This domain covers the employee lifecycle a manager or people-ops practitioner actually
> touches: **hiring** (job description through reference check), **onboarding**,
> **performance reviews**, and **people operations** (compensation banding, improvement
> plans, exit interviews).

---

## Purpose

A practical toolkit for anyone running a hiring loop, ramping a new joiner, writing a
review, or handling the people-ops decisions that sit around them. Every prompt is
evidence-first, bias-aware, and explicitly bans the kinds of output that get rejected by
HR, challenged by the subject, or quietly resented for being useless.

The domain grew from a performance-review suite. Hiring was routed here deliberately (see
`../domain-product-management/README.md`, which records the move) and is now built out;
the review suite remains the domain's anchor and the most developed part of it.

### Structure

```
domain-hr-management/
├── hiring/               # 6 — job description → sourcing → loop → scorecard → screen → references
├── onboarding/           # 1 — employee 30/60/90
├── performance-reviews/  # 6 — the anchor suite
└── people-ops/           # 3 — compensation banding, PIP authoring, exit interviews
```

The review suite is anchored by an **adaptive meta-prompt** (`hr_performance_review_meta_prompt.md`) that generates a role-tailored review scaffold — a rubric, a question bank, and evidence prompts — that the other five review prompts can consume. This is the "specified subject matter" layer: give it `role=senior software engineer, level=IC5` and it produces a structure sized for that role; give it `role=account executive, level=senior` and you get a completely different scaffold.

The hiring track has the same shape: `hr_job_description_writer.md` produces the role
outcomes, and `hr_interview_loop_design.md` and `hr_structured_scorecard.md` both derive
from them — so the posting, the loop and the scoring instrument cannot disagree.

---

## Who This Is For

| Persona | Start With |
|---------|-----------|
| **Manager writing a report's review** | `hr_reviewer_approach_guide.md` → `hr_performance_review_meta_prompt.md` → `hr_manager_writing_employee_review.md` |
| **IC writing their own self-review** | `hr_self_review_assessment.md` |
| **Peer asked to provide 360 feedback** | `hr_peer_360_feedback.md` |
| **HR partner / skip-level running calibration** | `hr_calibration_facilitator.md` |
| **New manager, first review cycle** | Read the review suite in order; start with the approach guide |
| **Hiring manager opening a role** | `hiring/hr_job_description_writer.md` → `hiring/hr_interview_loop_design.md` → `hiring/hr_structured_scorecard.md` |
| **Recruiter approaching passive candidates** | `hiring/hr_sourcing_outreach.md` |
| **Manager with a new joiner starting** | `onboarding/hr_onboarding_thirty_sixty_ninety.md` |
| **Founder or ops lead setting pay** | `people-ops/hr_compensation_banding.md` |
| **Manager formalising a performance concern** | `people-ops/hr_performance_improvement_plan.md` — then have it reviewed by `../domain-legal/employment-labor/legal_pip_and_termination_risk_review.md` before issuing |
| **Anyone running an exit conversation** | `people-ops/hr_exit_interview.md` |

---

## File Index

### Hiring

| File | What it does |
|------|--------------|
| [hiring/hr_job_description_writer.md](hiring/hr_job_description_writer.md) | Outcome-framed posting with every requirement audited against an outcome, the hard parts stated, and pay disclosed |
| [hiring/hr_sourcing_outreach.md](hiring/hr_sourcing_outreach.md) | Outreach to a passive candidate: one specific reason, the range in the first message, an easy decline |
| [hiring/hr_interview_loop_design.md](hiring/hr_interview_loop_design.md) | The loop as a signal pipeline — each stage owning exactly one attribute, bounded candidate cost, a debrief that resolves rather than averages |
| [hiring/hr_structured_scorecard.md](hiring/hr_structured_scorecard.md) | The instrument interviewers fill in: behavioural anchors, mandatory evidence, insufficient-evidence as a real verdict |
| [hiring/hr_hiring_screen_challenge_designer.md](hiring/hr_hiring_screen_challenge_designer.md) | One assessment instrument in depth — time-boxed, rubric-scored, refuses unpaid production work |
| [hiring/hr_reference_check_guide.md](hiring/hr_reference_check_guide.md) | Targeted at the loop's one open question; consent-gated, no backchannels |

### Onboarding

| File | What it does |
|------|--------------|
| [onboarding/hr_onboarding_thirty_sixty_ninety.md](onboarding/hr_onboarding_thirty_sixty_ninety.md) | Ramp derived from the role's outcomes, with the organisation's obligations named and a day-90 checkpoint that can conclude "not working" |

### People operations

| File | What it does |
|------|--------------|
| [people-ops/hr_compensation_banding.md](people-ops/hr_compensation_banding.md) | Levels by scope not tenure, ranges with a named market source, a written movement rule, and a compression audit |
| [people-ops/hr_performance_improvement_plan.md](people-ops/hr_performance_improvement_plan.md) | Authors a PIP a person could pass — and refuses to write one where the decision is already made |
| [people-ops/hr_exit_interview.md](people-ops/hr_exit_interview.md) | Run by someone who is not their manager, finds the reversible moment, aggregated before acted on |

### Performance reviews

| File | What it does |
|------|--------------|
| [performance-reviews/hr_reviewer_approach_guide.md](performance-reviews/hr_reviewer_approach_guide.md) | Coaches the reviewer *before* they write. Evidence gathering, bias audit, conversation prep. |
| [performance-reviews/hr_performance_review_meta_prompt.md](performance-reviews/hr_performance_review_meta_prompt.md) | **Adaptive meta-prompt.** Generates a role/level/competency-tailored review scaffold the other prompts can consume. |
| [performance-reviews/hr_manager_writing_employee_review.md](performance-reviews/hr_manager_writing_employee_review.md) | Drafts the written manager evaluation from evidence notes. Evidence-anchored, legally careful, actionable. |
| [performance-reviews/hr_self_review_assessment.md](performance-reviews/hr_self_review_assessment.md) | Helps an IC write a credible, specific self-review. Impact-framed, honest about misses. |
| [performance-reviews/hr_peer_360_feedback.md](performance-reviews/hr_peer_360_feedback.md) | Turns raw peer observations into Situation–Behavior–Impact feedback. Kind, specific, bias-checked. |
| [performance-reviews/hr_calibration_facilitator.md](performance-reviews/hr_calibration_facilitator.md) | Runs a calibration / norming meeting where managers align on ratings. Bias-check interventions built in. |

---

## Suggested Workflow (Annual or Mid-Year Cycle)

```
1. PREPARE
   └─ hr_reviewer_approach_guide.md        (1 week before drafting)
2. SCAFFOLD
   └─ hr_performance_review_meta_prompt.md (once per role/level)
3. COLLECT
   ├─ hr_self_review_assessment.md         (reviewee fills out)
   └─ hr_peer_360_feedback.md              (peers fill out)
4. DRAFT
   └─ hr_manager_writing_employee_review.md
5. CALIBRATE
   └─ hr_calibration_facilitator.md         (across managers)
6. DELIVER
   └─ (1:1 conversation — see approach guide's delivery section)
```

---

## Cross-References

Adjacent content elsewhere in the repo that pairs well with this suite:

| Content | Location | Why |
|---------|----------|-----|
| HR-Pro agent | `domain-agentic-resources/agents/business-operations/hr_pro.md` | Agent-level HR assistant; use when you want conversational back-and-forth rather than a single prompt |
| Employment law and risk | `domain-legal/employment-labor/` | PIP and termination risk review, worker classification, offer and separation packages. **Author here, review there** |
| Employer-side offer negotiation | `domain-negotiation/contexts/negotiation_hiring_offer_employer_side.md` | The offer conversation; the candidate's seat is `negotiation_salary_raise_promotion.md` |
| Cross-cutting patterns | `domain-agentic-resources/skills/non-coding/cross-domain/` | Quality-rubric, intake-triage and handoff/approval patterns that the hiring and review instruments are specific applications of |
| Feedback extraction | `domain-personal-development/prompts/agency/agency_feedback_extraction.md` | Turning feedback you received into action |
| Behavioral observation framework | `domain-psychology/psychology_behavioral_observation_framework.md` | Evidence-framing language |
| Goal system designer | `domain-personal-development/prompts/goals/` | Writing the "goals for next cycle" section of a review |
| Weekly review (personal) | `domain-personal-development/prompts/agency/agency_weekly_review.md` | Ongoing evidence capture throughout the cycle |

---

## Quality Principles (applied across every prompt)

1. **Evidence-anchored.** No claim without an observable example. If you can't cite it, you can't say it.
2. **Impact over activity.** Describe what changed, not what was done.
3. **Bias-checked.** Each prompt flags the specific biases that distort its artifact (recency, halo/horns, similar-to-me, leniency, central tendency, groupthink in calibration).
4. **Legally careful.** No protected-class references, no medical / family speculation, no personality diagnoses.
5. **Actionable.** Growth areas name the behavior and the desired change, not a label.
6. **Reversible.** Drafts are explicitly drafts. Every prompt ends with a self-check the human runs before delivery.

---

*Last updated: 2026-09-22*
