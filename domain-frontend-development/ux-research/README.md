# UX Research Prompts

**Category:** Frontend Development / UX Research
**Prompts:** 7

---

## Overview

Method prompts for evaluating web and app interfaces with and without users:
planning and moderating usability tests, expert heuristic review, information-
architecture studies, severity-rated findings, standardized usability
questionnaires, and design critique. Each prompt owns one artifact in the
research cycle and names its neighbours so they do not overlap.

## Prompts

| Prompt | Description | Difficulty |
|--------|-------------|------------|
| [frontend_ux_usability_test_plan.md](frontend_ux_usability_test_plan.md) | Decision-linked research questions, scenario tasks with success criteria, recruiting, and metrics | Intermediate |
| [frontend_ux_moderated_session_script.md](frontend_ux_moderated_session_script.md) | The moderator's words: consent, think-aloud warm-up, neutral probes, rescue ladder | Intermediate |
| [frontend_ux_heuristic_evaluation.md](frontend_ux_heuristic_evaluation.md) | Expert review against Nielsen's heuristics with located, severity-rated findings | Intermediate |
| [frontend_ux_card_sort_tree_test.md](frontend_ux_card_sort_tree_test.md) | Card sort to generate an IA, tree test to measure findability, cross-analysed | Intermediate |
| [frontend_ux_usability_findings_severity_log.md](frontend_ux_usability_findings_severity_log.md) | One problem per row, impact × frequency severity, traced to participants | Intermediate |
| [frontend_ux_standardized_survey_sus.md](frontend_ux_standardized_survey_sus.md) | Administer and score SUS, UMUX-Lite, and SEQ with confidence intervals | Beginner |
| [frontend_ux_design_critique_facilitator.md](frontend_ux_design_critique_facilitator.md) | Run a goal-tied critique that separates taste from evidence and ends in owned decisions | Intermediate |

## Typical Sequence

```
Heuristic evaluation (clear obvious problems)
  → Usability test plan → Moderated session script → sessions
  → Standardized questionnaire scoring + Findings severity log
  → Design critique of the revised work
Card sort / tree test runs alongside whenever navigation labels are in question.
```

## Boundaries

- Accessibility conformance → [../accessibility/](../accessibility/)
- Visual direction before critique → [../design-direction/](../design-direction/)
- Discovery interviews and cross-study synthesis →
  [`domain-research-academic/research_interview_guide_designer.md`](../../domain-research-academic/research_interview_guide_designer.md),
  [`domain-business-strategy/research/user_research_synthesis.md`](../../domain-business-strategy/research/user_research_synthesis.md)
- Designing a new survey instrument →
  [`domain-research-academic/research_survey_instrument_designer.md`](../../domain-research-academic/research_survey_instrument_designer.md)
- Voice interfaces →
  [`domain-voice-conversational-ui/voice-ux/voice_ux_best_practices_audit.md`](../../domain-voice-conversational-ui/voice-ux/voice_ux_best_practices_audit.md)

## Related Resources

- [UX Researcher persona](../../domain-agentic-resources/personas/design/design_ux_researcher.md)
- [site-architecture skill](../../domain-agentic-resources/skills/marketing/site-architecture/SKILL.md)
