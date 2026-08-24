# Model Optimization

Adapt prompts for specific model families, sizes, and reasoning modes; migrate within and across families; replace retired models; probe new ones; track quirks; test portability.

| File | Description |
|------|-------------|
| `modelopt_claude_specific_patterns.md` | Claude conventions: XML tags, prefill, extended thinking |
| `modelopt_gpt_specific_patterns.md` | GPT conventions: JSON Schema, function calling, terse system |
| `modelopt_haiku_constraints.md` | Adapt for small/fast models with single concern + tight schema |
| `modelopt_thinking_model_patterns.md` | Patterns for reasoning-mode models; remove CoT scaffolding |
| `modelopt_cross_model_migration.md` | Translate prompts across families with substitution map |
| `modelopt_within_family_migration.md` | Bump model versions with regression diff and changelog |
| `modelopt_retired_model_replacement.md` | Plan, execute, monitor, rollback model retirement |
| `modelopt_capability_probe_prompt.md` | Profile a new model on 10 capability axes |
| `modelopt_quirks_catalog_builder.md` | Document model-specific tics with reproductions and mitigations |
| `modelopt_prompt_portability_test.md` | Score how consistently a prompt behaves across N models |
