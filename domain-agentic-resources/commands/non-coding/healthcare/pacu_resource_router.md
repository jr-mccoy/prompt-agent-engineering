---
name: pacu_resource_router
description: "Route a PACU topic to the right combination of skills, prompts, and image meta-prompts. Asks 2-3 clarifying questions, assembles a package (e.g., comprehensive guide + matching algorithm + image prompt + quick-ref), and returns all artifacts in one response."
version: "1.0.0"
category: healthcare
tags: [pacu, perianesthesia, orchestrator, healthcare, routing]
agents_used: []
type: command
invocation: /pacu-resource
updated: "2026-04-14"
---

# /pacu-resource — PACU Educator Resource Router

> Safety reminder: Router is a productivity aid. Each generated artifact carries its own safety reminder; the light guardrails in the toolkit are intentional, not a safety guarantee.

## Purpose

Take a single user intent like `/pacu-resource TURP postop` and produce a coordinated package of educational artifacts without the user having to chain skills manually.

## Invocation

```
/pacu-resource <topic or scenario>
```

Examples:
- `/pacu-resource spinal anesthesia hypotension`
- `/pacu-resource total knee arthroplasty orientation`
- `/pacu-resource post-op PONV escalation`
- `/pacu-resource PACU desaturation algorithm`

## Flow

1. **Parse the topic.** Classify it into one of:
   - **Procedure / specialty** (whole surgery family) → biases toward comprehensive guide + quick-ref + handoff script.
   - **Complication / physiology** (one problem) → biases toward in-depth explainer + algorithm + image + flashcards.
   - **Medication / pharmacology** → biases toward med profile + reversal chart image + flashcards.
   - **Skill / role transition** → biases toward competency checklist + case scenario + self-assessment.
   - **Orientee evaluation / sign-off** (performance review, mid/end-of-phase evaluation, calibration across preceptors, remediation planning, difficult conversation prep) → biases toward the Preceptor Evaluation Suite: meta-prompt + approach guide + writing evaluation, plus 360/calibration/remediation as needed.
   - **Orientation curriculum design** (designing the orientation pathway itself, weekly / day-by-day plans, background adaptation, pacing diagnostic, mid-orientation handoff between preceptors, facility orientation program audit, self-directed modules, sim calendars, shadow / journal-club / peer-pairing design, orientee self-use journaling and self-study planning) → biases toward the v3 Orientation Curriculum lane: curriculum designer + skill-acquisition timeline + background adapter + weekly learning plans + pacing diagnostic, with orientee-facing prompts as appropriate.
   - **CAPA/CPAN exam prep** (study plan, weak-area diagnostic, practice questions, test strategy, final week) → biases toward the CAPA/CPAN exam-prep lane: blueprint-aligned study plan + weak-area diagnostic + practice question generator + test strategy coach + final week review.
   - **Unclear** → ask question 1 below first.
2. **Ask up to 3 clarifying questions** (use only what's still unknown after parsing):
   - **Q1 — Artifact type (multi-select):** guide · quick-ref · in-depth explainer · quiz · study guide · algorithm · flashcards · case scenario · competency checklist · image · orientee primer · red-flag card · med profile · complication deep-dive · handoff script · patient education.
   - **Q2 — Audience:** novice orientee / mid-orientation / end-of-orientation / experienced nurse / patient / family.
   - **Q3 — Visual needed?** yes + which image meta-prompt / no.
3. **Select artifacts.** Use the routing table below. Never produce more than 5 artifacts in one run (if user seems to want more, ask them to split).
4. **Invoke each selected skill or prompt or image meta-prompt** and pass the topic + audience + any surgery context the user mentioned.
5. **Aggregate and return** all artifacts in one markdown response, with a short header block listing what's included and what was intentionally omitted.
6. **End with a "Next actions" block** — e.g., "Paste image prompt into Nano Banana", "Print quick-ref at 8.5×5.5 portrait", "Review draft quiz with another educator before using for sign-off".

## Routing table

| Topic class | Default bundle |
|---|---|
| Procedure / specialty | `skills/pacu-comprehensive-guide-author/` + `skills/pacu-quick-reference-author/` + `prompts/pacu_handoff_script.md` |
| Complication / physiology | `skills/pacu-in-depth-explainer/` + `skills/pacu-algorithm-flowchart-designer/` + `image-meta-prompts/pacu_algorithm_flowchart_meta.md` + `prompts/pacu_red_flag_card.md` |
| Medication | `prompts/pacu_medication_profile.md` + `image-meta-prompts/pacu_medication_reversal_chart_meta.md` + `skills/pacu-flashcard-deck-builder/` |
| Skill / role transition | `skills/pacu-competency-checklist-builder/` + `skills/pacu-case-scenario-writer/` + `prompts/pacu_competency_self_assessment.md` + `prompts/pacu_orientee_evaluation_meta_prompt.md` (for orientation-kickoff context) |
| Orientation week capstone | `skills/pacu-study-guide-builder/` + `skills/pacu-quiz-generator/` + `skills/pacu-case-scenario-writer/` |
| Orientee evaluation / sign-off | `prompts/pacu_orientee_evaluation_meta_prompt.md` + `prompts/pacu_preceptor_approach_guide.md` + `prompts/pacu_preceptor_writing_orientee_evaluation.md` (core trio). Add `prompts/pacu_peer_preceptor_360_feedback.md` if multi-preceptor input exists, `prompts/pacu_preceptor_calibration_facilitator.md` if norming across preceptors, `prompts/pacu_orientee_remediation_plan.md` + `prompts/pacu_preceptor_difficult_conversation_guide.md` if disposition is Extend/Remediation. Never mix evaluation artifacts with patient-facing artifacts. |
| Orientation curriculum design — full pathway | `prompts/pacu_orientation_curriculum_designer.md` + `prompts/pacu_orientation_skill_acquisition_timeline.md` + `prompts/pacu_background_specific_pathway_adapter.md` + (optionally) `image-meta-prompts/pacu_orientation_pathway_map_meta.md` |
| Orientation curriculum design — single week | `prompts/pacu_orientee_weekly_learning_plan.md` + `prompts/pacu_self_directed_learning_module_designer.md` (if off-shift module scheduled) |
| Orientation curriculum design — Week 1 / Day 1 | `prompts/pacu_orientation_first_day_packet.md` + `prompts/pacu_orientation_first_week_plan.md` |
| Orientation curriculum design — mid-orientation diagnostics | `prompts/pacu_preceptor_orientation_pacing_diagnostic.md` + `prompts/pacu_orientation_topic_sequencing_optimizer.md` (re-sequence) OR `prompts/pacu_orientee_evaluation_meta_prompt.md` (formal eval if pacing diagnostic triggers it) |
| Orientation operations — preceptor handoff or program audit | `prompts/pacu_preceptor_curriculum_handoff_brief.md` OR `prompts/pacu_orientation_curriculum_audit.md` (do not bundle these two; they serve different purposes) |
| Orientation curriculum design — orientee-facing self-use | `prompts/pacu_orientee_reflective_journal_prompts.md` + `prompts/pacu_orientee_topic_self_study_planner.md` + `prompts/pacu_orientee_question_log_builder.md` (these belong to the orientee — never bundle with preceptor-facing evaluation artifacts) |
| CAPA/CPAN exam prep | `prompts/pacu_capa_cpan_blueprint_aligned_study_plan.md` + `prompts/pacu_capa_cpan_weak_area_diagnostic.md`. Add `prompts/pacu_capa_cpan_practice_question_generator.md` if sub-topic deep dive needed; `prompts/pacu_capa_cpan_test_strategy_coach.md` and `prompts/pacu_capa_cpan_final_week_review.md` in the final 2 weeks. Visual: `image-meta-prompts/pacu_capa_cpan_blueprint_visual_meta.md`. Never bundle with patient-facing or orientation-design artifacts in the same response. |
| Patient-facing | `prompts/pacu_patient_education_sheet.md` (alone; do not bundle orientee artifacts with patient artifacts) |

## Must / Must not

**Must:**
- Ask clarifying questions only when parsing is ambiguous. Do not interrogate the user for every run.
- Preserve the light safety reminder in every included artifact.
- Return artifacts in a stable order: explainer → algorithm → image prompt → quick-ref → quiz/flashcards → handoff/patient-ed.
- Call out what you chose *not* to include and why (helps the user override).

**Must not:**
- Generate more than 5 artifacts per run without explicit user opt-in.
- Mix patient-facing and clinician-facing artifacts in the same bundle.
- Invent doses or facility specifics — every downstream artifact enforces this; the router passes through, does not fabricate.

## Self-check before returning

- [ ] Topic class correctly identified.
- [ ] Bundle ≤ 5 artifacts.
- [ ] Each artifact retains its own safety reminder.
- [ ] Next-actions block present.
- [ ] Omitted-artifacts rationale stated.

## Example run

**User:** `/pacu-resource spinal anesthesia hypotension`

**Router parses:** Complication / physiology.

**Router asks:**
- Q1: Do you want the quick-ref too, or just the in-depth explainer + algorithm + image?
- Q2: Audience? (defaults to mid-orientation orientee)
- Q3: Which accent color for the image flowchart? (defaults to teal + amber + red)

**Returns:**
1. In-depth explainer (pathophys → correlation → PACU implications, from `pacu-in-depth-explainer`).
2. Algorithm in Mermaid + plain text (from `pacu-algorithm-flowchart-designer`).
3. Ready-to-paste Nano Banana prompt (from `pacu_algorithm_flowchart_meta.md`, with the algorithm's plain-text branches pre-filled).
4. Red-flag pocket card (from `pacu_red_flag_card.md`).
5. Short "Next actions": print red-flag card at 4×6; paste image prompt into Nano Banana; review algorithm with anesthesia before using clinically.
