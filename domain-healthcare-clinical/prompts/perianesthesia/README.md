# Perianesthesia (Phase 1 PACU)

Prompts for post-anesthesia care: recovery-phase complications, reversal and
analgesia pharmacology, population-specific recovery considerations, and a
staged learning path for nurses entering the specialty.

All prompts here are **educational and rehearsal aids for licensed clinicians
and their educators** — not clinical decision support. The shared safety posture
for the whole set is [`SAFETY_PREAMBLE.md`](SAFETY_PREAMBLE.md): no invented
doses, no invented thresholds, no invented facility protocols, no invented
citations, and recognition-and-escalation framing throughout.

## Layout

| Directory | What's in it | Count |
|---|---|---:|
| [`clinical-and-educator/`](clinical-and-educator/) | Complication scaffolds, drug monographs, population-specialty considerations, and the educator/preceptor set (orientation curriculum, evaluation, simulation, certification prep) | 69 |
| [`spine/`](spine/) | Cross-stage progression: learning objectives by stage, self-assessment blueprint, remediation pathway | 3 |
| [`stage-0-foundations/`](stage-0-foundations/) | Before day one — what PACU is, anesthesia types, emergence physiology and pharmacology | 12 |
| [`stage-1-orientation/`](stage-1-orientation/) | Running a shift with a preceptor: handoff, prioritization, escalation, charting | 18 |
| [`stage-2-independence/`](stage-2-independence/) | Solo readiness: two-patient prioritization, charting under load, sign-off | 12 |
| [`stage-3-independent-practice/`](stage-3-independent-practice/) | Consolidation and CAPA/CPAN certification | 8 |
| [`stage-4-growth-advanced/`](stage-4-growth-advanced/) | High-acuity recovery, precepting, leadership | 16 |

[`COMPETENCY_PROGRESSION_MAP.md`](COMPETENCY_PROGRESSION_MAP.md) is the stage × competency-domain
grid; [`TOOLKIT_CROSSWALK.md`](TOOLKIT_CROSSWALK.md) maps each learner drill to the artifact that
supplies its clinical facts.

## The two sides

The set covers both sides of the same specialty:

- **Clinical and educator artifacts** supply the facts and the scaffolding — what a
  complication looks like, what a drug does, how to build an orientation curriculum,
  how to evaluate an orientee.
- **Staged learner artifacts** are operated by the nurse themselves — drills,
  rehearsals, primers, and self-assessment sequenced by career stage (novice through
  expert, on a Benner progression).

Neither restates the other. When a learner drill needs a clinical fact, it points at
the clinical artifact rather than duplicating it, so there is one source of truth.

## Related resources elsewhere in the repository

| Resource type | Location |
|---|---|
| Nursing seed prompts (shift structure, prioritization, preceptor set) | [`../nursing/`](../nursing/) |
| Visual/diagram meta-prompts for this specialty | [`../../../domain-image-generation/healthcare/`](../../../domain-image-generation/healthcare/) |
| Authoring skills (guide author, quiz generator, flashcards, explainer) | [`../../../domain-agentic-resources/skills/non-coding/healthcare/`](../../../domain-agentic-resources/skills/non-coding/healthcare/) |
| Routing command | [`../../../domain-agentic-resources/commands/non-coding/healthcare/pacu_resource_router.md`](../../../domain-agentic-resources/commands/non-coding/healthcare/pacu_resource_router.md) |
| Educator persona | [`../../../domain-agentic-resources/personas/specialized/pacu_educator_persona.md`](../../../domain-agentic-resources/personas/specialized/pacu_educator_persona.md) |
| Broader medical-education prompts | [`../../../domain-medical-education/`](../../../domain-medical-education/) |

## Conventions

- Prompts declare `related_prompts` as bare sibling filenames; cross-directory
  pointers use repository-relative paths.
- Every artifact carries a one-line safety reminder pointing at the shared preamble.
- Clinical numbers are never stated: doses, rates, thresholds, and scores are
  `per provider order` or `per facility protocol`.
