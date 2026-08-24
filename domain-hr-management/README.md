# HR & People Management: Performance Review Suite

> Part of the [Non-Coding Quick Start](../NON_CODING_QUICK_START.md) system.
> This domain covers people-management performance reviews: preparation, drafting, self-assessment, peer / 360 feedback, and calibration.

---

## Purpose

A practical toolkit for anyone touching a formal performance-review cycle. Every prompt in this suite is evidence-first, bias-aware, and explicitly bans the kinds of output that get reviews rejected by HR, challenged by the reviewee, or quietly resented for being useless.

The suite is anchored by an **adaptive meta-prompt** (`hr_performance_review_meta_prompt.md`) that generates a role-tailored review scaffold — a rubric, a question bank, and evidence prompts — that the other five prompts can consume. This is the "specified subject matter" layer: give it `role=senior software engineer, level=IC5` and it produces a structure sized for that role; give it `role=account executive, level=senior` and you get a completely different scaffold.

---

## Who This Is For

| Persona | Start With |
|---------|-----------|
| **Manager writing a report's review** | `hr_reviewer_approach_guide.md` → `hr_performance_review_meta_prompt.md` → `hr_manager_writing_employee_review.md` |
| **IC writing their own self-review** | `hr_self_review_assessment.md` |
| **Peer asked to provide 360 feedback** | `hr_peer_360_feedback.md` |
| **HR partner / skip-level running calibration** | `hr_calibration_facilitator.md` |
| **New manager, first review cycle** | Read the full suite in order; start with the approach guide |

---

## File Index

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

*Last updated: 2026-04-15*
