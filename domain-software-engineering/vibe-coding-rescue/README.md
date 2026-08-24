# Vibe Coding Rescue

Prompts for the specific situation where AI-assisted coding has stopped producing reliable forward progress — regressions keep landing, the AI keeps rewriting the same file, or the project has quietly accumulated security and resilience debt. These are rescue operations, not preventive advice.

## When to Use This Cluster

- A project built largely with AI assistance has hit a wall — forward progress is slow, every new feature breaks two old ones, or the codebase no longer matches your mental model.
- A specific task keeps failing across multiple AI attempts and you need to decompose rather than re-prompt.
- The project is going to production or being handed off and you need a rigorous audit or briefing first.
- A team is standardizing how they constrain AI output in their codebase via a rules file.

## Prompts

| # | Prompt | Use When |
|---|--------|----------|
| 1 | [`viberescue_wall_diagnosis.md`](viberescue_wall_diagnosis.md) | The project has hit a wall; classify the failure mode into a fixed taxonomy (10 modes) and get the rescue action that fits. |
| 2 | [`viberescue_rules_file_design.md`](viberescue_rules_file_design.md) | Build a rules file (CLAUDE.md / .cursorrules / equivalent) tuned to this codebase's actual conventions and repeated AI mistakes. |
| 3 | [`viberescue_decompose_stuck_task.md`](viberescue_decompose_stuck_task.md) | AI has failed the same task 3+ times; decompose into agent-sized subtasks with specs, acceptance, and dependency order. |
| 4 | [`viberescue_security_audit.md`](viberescue_security_audit.md) | Audit AI-generated code for the patterns it tends to produce — confidently-wrong auth, concat'd SQL, swallowed exceptions, optimistic happy paths, missing input validation. |
| 5 | [`viberescue_engineer_handoff_briefing.md`](viberescue_engineer_handoff_briefing.md) | Generate a briefing so a new engineer can take over safely — what works, what's fragile, what not to touch, and what the author honestly doesn't know. |

## Recommended Sequence

These are not usually run in full sequence; a typical use pattern:

1. **Suspect a wall:** run `viberescue_wall_diagnosis.md`.
2. **If diagnosis points to Mode 6 (no rules):** run `viberescue_rules_file_design.md`.
3. **If diagnosis points to Mode 9 (task too big):** run `viberescue_decompose_stuck_task.md`.
4. **Before production or handoff:** run `viberescue_security_audit.md`.
5. **Before handoff to a new owner:** run `viberescue_engineer_handoff_briefing.md` last — it often pulls in outputs of the others.

## Cross-References

- Broader software-engineering security analysis: [`../analysis/security/`](../analysis/security/)
- LLM / AI application security review (for products that embed LLMs): [`../analysis/security/security_llm_application_review.md`](../analysis/security/security_llm_application_review.md)
- Agent task design and decomposition: [`../../domain-engineering-workflows/ai-patterns/`](../../domain-engineering-workflows/ai-patterns/)
- AI-native rollouts (team-level AI adoption practices): [`../../domain-engineering-workflows/ai-native-rollouts/`](../../domain-engineering-workflows/ai-native-rollouts/)
- Agent code footgun detection: [`../../domain-engineering-workflows/ai-patterns/ai_pattern_agent_code_footgun_detector.md`](../../domain-engineering-workflows/ai-patterns/ai_pattern_agent_code_footgun_detector.md)
- Long-running project memory: [`../../domain-engineering-workflows/ai-native-rollouts/airollout_long_running_project_memory.md`](../../domain-engineering-workflows/ai-native-rollouts/airollout_long_running_project_memory.md)

## Design Principles

- **Diagnose before treating.** Generic "add tests" or "refactor" advice is refused. Every rescue is keyed to a specific failure mode.
- **One rescue at a time.** Stacking rescues causes thrash. The wall-diagnosis prompt picks one primary mode and one rescue; secondary modes are noted for later.
- **Evidence over reassurance.** Security findings cite file + line + traced data flow; handoff briefings separate "confidence: high" from "confidence: low" explicitly.
- **Honest handoff.** Briefings are written for the new engineer, not for the outgoing author's ego — the don't-touch-yet section and the open-questions section are as important as the what-works section.
- **Rules files are evidence-sourced.** Every rule must trace to a positive exemplar, a forbidden pattern, a repeated AI mistake, or a domain-vocabulary entry. Generic rules are rejected.
