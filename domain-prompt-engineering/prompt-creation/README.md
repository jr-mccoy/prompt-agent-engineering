# Prompt Creation

Greenfield prompt-authoring patterns. Use these when starting from a blank page or formalizing a tacit prompt.

| File | Description |
|------|-------------|
| `creation_task_prompt_from_blank.md` | Convert a fuzzy goal into a first-draft task prompt |
| `creation_user_prompt_template_designer.md` | Parameterize a one-off prompt with `${variables}` |
| `creation_system_vs_user_split_designer.md` | Classify each rule into system / developer / user role |
| `creation_role_first_prompt_builder.md` | Open with a tightly bounded role; derive the rest from it |
| `creation_constraint_first_prompt_builder.md` | Lead with `Must` / `Must Not`; derive role and format |
| `creation_progressive_disclosure_prompt.md` | Hot-path minimal prompt + triggered cold-path expansions |
| `creation_negative_prompt_designer.md` | Build the `Must Not` block as a first-class artifact |
| `creation_chain_prompt_designer.md` | Decompose into a multi-call chain with typed handoffs |
| `creation_prompt_for_prompt.md` | Meta-prompt that emits structured task prompts |
| `creation_clarification_loop_prompt.md` | Ask targeted questions before answering, with caps |
| `creation_input_validation_prompt.md` | Reject malformed input with a structured error first |
| `creation_default_value_designer.md` | Define explicit defaults for every optional input |
| `creation_terse_vs_verbose_variant.md` | Two equivalent variants for different cost budgets |
| `creation_skeleton_first_then_fill.md` | Lock structure before content; mark gaps explicitly |
| `creation_prompt_from_examples.md` | Reverse-engineer a prompt from accepted outputs |
| `creation_prompt_pack_for_role.md` | Coherent bundle of prompts for a single role |
