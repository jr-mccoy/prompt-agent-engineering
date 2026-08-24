# Instruction Design

Prompts for designing the rule layer of a prompt: ranking, classifying, rewriting, and stress-testing instructions so the model resolves them deterministically.

## When to Use This Subdirectory

- The prompt has more than ~10 rules and behavior is becoming inconsistent.
- Two authors are editing the same prompt and disagree on what is mandatory.
- The model violates a rule it was clearly given.
- A migration to a new model family broke previously reliable wordings.

## Files

| File | One-line description |
|------|----------------------|
| `instruction_hierarchy_designer.md` | Encode SYSTEM > DEVELOPER > USER precedence with rule IDs and conflict-report schema. |
| `instruction_conflict_taxonomy.md` | Classify every internal conflict into DIRECT / SCOPE_OVERLAP / PRIORITY_TIED / VACUOUS and emit a resolution edit per pair. |
| `instruction_precedence_test_set.md` | Generate adversarial test cases (injection, role-play, authority claim, etc.) that prove the hierarchy holds. |
| `instruction_negation_audit.md` | Find "do not X" rules that prime X and rewrite each into a positive form. |
| `instruction_anchor_phrase_library.md` | Build a per-model-family library of empirically calibrated anchor phrases with paired baselines and effect sizes. |
| `instruction_imperative_vs_declarative.md` | Decide whether each rule should be imperative (process) or declarative (artifact), and convert mismatched rules. |
| `instruction_must_should_may_classifier.md` | Apply RFC-2119-style MUST / SHOULD / MAY ranking to a flat rule list with failure_consequence and override_condition fields. |
| `instruction_compaction_for_long_prompts.md` | Cut a prompt to ≤50% of original tokens using a fixed catalogue of 10 compaction techniques, with a no-loss constraint map. |

## Suggested Workflow

1. `instruction_must_should_may_classifier.md` — rank what matters.
2. `instruction_imperative_vs_declarative.md` — set form per rule.
3. `instruction_negation_audit.md` — fix priming risks.
4. `instruction_conflict_taxonomy.md` — resolve internal conflicts.
5. `instruction_hierarchy_designer.md` — encode precedence across layers.
6. `instruction_precedence_test_set.md` — verify with adversarial cases.
7. `instruction_compaction_for_long_prompts.md` — trim once stable.
8. `instruction_anchor_phrase_library.md` — extract reusable phrases for the team library.

## Related

- `../debugging/` — when an instruction-design fix doesn't hold, debug the failure.
- `../system-prompts/` — full system-prompt patterns.
- `../model-behavior/` — root-cause why the model deviates from a clear rule.
