# Domain: Learning

Deliberate, self-directed skill acquisition. The five prompts in this domain cover the arc from "I need to get good at X" to a sequenced, checkable plan: defining what "good" observably means, building the curriculum or practice loop to get there, curating what to read, and auditing whether understanding is real or illusory. They are domain-agnostic — the same prompts work for a language, an instrument, a sales motion, a research method, or a management skill.

The shared premise is that most self-directed learning fails on structure, not effort. People learn at the wrong level (attempting level-3 material with a level-2 gap), confuse exposure with mastery, practice without feedback (so repetition isn't deliberate), read breadth-first with no spine, and never define a finish line they can test against. Each prompt attacks one of these failure modes and forces an observable output: a week-by-week plan, a timed practice rep with a feedback mechanism, a layered reading list, or a Feynman-style explanation that exposes the actual gap.

Users are self-directed learners, career-changers, professionals closing a job-relevant skill gap, managers designing growth plans for reports, and anyone who has stalled in a domain and suspects the problem is their learning process rather than their aptitude. Every prompt works solo.

## When to use this domain

- You need to reach a defined level in a domain by a deadline and want a real week-by-week plan, not a vibe.
- You're practicing a skill but not improving — reps without feedback, or reps that have gone rote.
- You're drowning in recommended books/papers and need a sequenced path from foundations to frontier.
- You think you understand a concept but can't tell if the understanding is solid or surface.
- A job, project, or goal requires a skill you currently lack and you need to translate that gap into a plan.

## When NOT to use this domain (use a different one)

- **You're learning to code specifically** → `domain-learning-coding/` (`learning_teach_me_to_code.md` and code-specific exercises).
- **The bottleneck is execution/shipping, not skill** → `domain-personal-development/prompts/agency/` (`agency_skill_gap_reframe.md`, `agency_next_action_spec.md`).
- **You want to teach others / design a course for a class or program** → `domain-education-teaching/` (lesson plans, curriculum-design, program outcomes).
- **You're deciding whether to do a degree / bootcamp / certificate at all** → `domain-personal-development/major-decisions/personal_education_program_choice.md`.
- **You want a single rigorous reasoning move rather than a learning plan** → `domain-reasoning-craft/reasoning-moves/`.

## Prompts in this domain

| File | Purpose |
|------|---------|
| `learning_curriculum_designer.md` | Design an N-week curriculum to a defined target level, with prerequisite tree, weekly theory+practice, and a shippable output each week |
| `learning_deliberate_practice_designer.md` | Build a narrow deliberate-practice loop for one sub-skill: the rep, the immediate-feedback mechanism, cadence, and a 4-week ramp |
| `learning_reading_list_curator.md` | Curate a layered reading list (foundations → surveys → frontier → contrarian) sequenced with notes-prompts and absorption checks |
| `learning_concept_explanation_audit.md` | Feynman-test your understanding: write a plain-language explanation, then audit it for jargon-as-substitute and skipped load-bearing steps |
| `learning_skill_gap_to_curriculum.md` | Translate a precise skill gap into the smallest learning loop, choosing among study / practice / apprenticeship / doing |

## Quick routing

| You're saying | Use |
|---------------|-----|
| "I want to get to level X in this domain in 12 weeks" | `learning_curriculum_designer.md` |
| "I practice but I'm not getting better" | `learning_deliberate_practice_designer.md` |
| "What should I read, and in what order?" | `learning_reading_list_curator.md` |
| "I think I understand this — do I really?" | `learning_concept_explanation_audit.md` |
| "I can't do this thing my job/project needs — where do I start?" | `learning_skill_gap_to_curriculum.md` |

## How prompts in this domain compose

The canonical chain is **scope the gap → plan → practice → verify**. Start with `learning_skill_gap_to_curriculum` when the gap is concrete and job-driven, or `learning_curriculum_designer` when the goal is a whole domain to a target level. Both define an observable finish line first. Feed the "study" portions into `learning_reading_list_curator` for a sequenced spine, and the "practice" portions into `learning_deliberate_practice_designer` for feedback-bearing reps. Throughout, use `learning_concept_explanation_audit` as the verification step — it exposes whether a week's material actually landed and points to the next highest-leverage thing to learn. The audit's output loops back into the curriculum, retargeting the next week on the load-bearing gap it surfaced.

## Frontmatter conventions specific to this domain

All prompts carry the repo-standard frontmatter plus a machine-readable `reasoning:` block (styles, stakes, horizon, uncertainty, output_format, user_role, mode). The load-bearing fields here are `horizon` (these plans run weeks to months, unlike the minutes-to-hours reasoning moves) and `mode` (`plan` for the designers, `audit` for the explanation check). `output_format` is typically `structured` or `spec` — every prompt yields a checkable artifact, never just advice. `related_prompts` encodes the composition chain above.

## Companion domains

- `domain-learning-coding/` — the code-specific sibling; use it when the skill is programming, this domain when it isn't.
- `domain-personal-development/prompts/agency/` — when the real bottleneck is shipping rather than skill (`agency_skill_gap_reframe.md`), or when you need to convert a learning plan into owned execution.
- `domain-reasoning-craft/` — the rigorous reasoning moves several learners need as content (first-principles reconstruction, analogical inference) and the epistemic tools that make `learning_concept_explanation_audit` sharper.
- `domain-productivity/deep-work/` — scheduling and protecting the focus blocks a curriculum or practice ramp depends on.
