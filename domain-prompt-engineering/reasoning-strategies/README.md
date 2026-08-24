# Reasoning Strategies

Decide how the model thinks: chain-of-thought, scratchpad, decomposition, self-check, tree-of-thought, self-consistency, extended thinking, silent reasoning, plan-then-execute, premise check, and explanation-vs-answer separation.

| File | Description |
|------|-------------|
| `reasoning_cot_vs_direct_decision.md` | Decide whether to use chain-of-thought at all |
| `reasoning_scratchpad_designer.md` | Bounded scratchpad with named slots |
| `reasoning_decomposition_prompt.md` | Ordered named subtasks with acceptance checks |
| `reasoning_self_check_pattern.md` | Answer → self-verify → revise pattern |
| `reasoning_tree_of_thought_template.md` | Branch / score / prune within a budget |
| `reasoning_self_consistency_runner.md` | N samples, vote, surface disagreement |
| `reasoning_extended_thinking_budget.md` | Set thinking-token budgets empirically |
| `reasoning_silent_reasoning_then_answer.md` | Reason internally; emit only the answer |
| `reasoning_plan_then_execute_split.md` | Two-prompt split for reviewable plans |
| `reasoning_premise_check_pattern.md` | Verify input premises before reasoning |
| `reasoning_explanation_then_answer_split.md` | Dual output: answer + auditable explanation |
