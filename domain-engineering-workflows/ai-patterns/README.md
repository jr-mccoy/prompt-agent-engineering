# AI-Augmented Development Patterns

**Scope:** Prompts for developers whose primary working mode is partnering with an AI coding agent (Claude Code, Cursor, Copilot, or similar). The patterns here cover the full life cycle of an AI-augmented task — from stance and intent-setting, through exploration and review, to rule extraction, reflection, and maintenance of code you no longer fully remember.

**When to use this subfolder:**
- You've moved from writing code mostly yourself to managing code the agent produces
- You want to install specific habits (intent-first, outcome review, pre-mortem) rather than vague "use AI well" advice
- A failure mode keeps recurring and you want a pattern to apply next time
- You're setting team norms for reviewing, delegating to, and maintaining AI-generated code

**When NOT to use this subfolder:**
- The task is a one-shot code question — use a direct prompt from `domain-software-engineering/` instead
- You need a gate-based convergence loop for a specific task — see [`../done-definition/`](../done-definition/)
- You're choosing whether to use AI at all — see [`../../domain-prompt-engineering/delegation/`](../../domain-prompt-engineering/delegation/)

---

## Prompts

### Orientation
| File | What it does |
|------|--------------|
| [`../../domain-personal-development/prompts/identity/identity_engineering_manager_stance.md`](../../domain-personal-development/prompts/identity/identity_engineering_manager_stance.md) | Reorients from writer to manager: diagnoses current stance, reallocates time, names failure modes, sets a one-week experiment |

### Task opening (before the agent starts)
| File | What it does |
|------|--------------|
| [`ai_pattern_intent_and_verification_first.md`](ai_pattern_intent_and_verification_first.md) | Produces the pre-task brief: intent, verification criteria, out-of-scope, reviewer checklist |
| [`ai_pattern_outcome_language_translator.md`](ai_pattern_outcome_language_translator.md) | Rewrites prompts from implementation language into outcome language; flags load-bearing constraints vs. preferences |
| [`ai_pattern_unstructured_start_exploration.md`](ai_pattern_unstructured_start_exploration.md) | Runs a bounded dialogue-based exploration for novel tasks, with convergence gate and exit criteria |

### Review and verification (during / after the agent's work)
| File | What it does |
|------|--------------|
| [`ai_pattern_verification_depth_calibrator.md`](ai_pattern_verification_depth_calibrator.md) | Assigns a verification depth (L0–L4) based on stakes, reversibility, blast radius, and prior-knowledge coverage |
| [`ai_review_failure_mode_premortem.md`](ai_review_failure_mode_premortem.md) | Generates specific failure modes across five axes, each paired with a runnable verification |
| [`ai_review_outcome_level_code_review.md`](ai_review_outcome_level_code_review.md) | Five-question outcome-level review producing a verdict (ship / fix / rework / redesign) and concrete agent instructions |
| [`ai_verification_mental_model_audit.md`](ai_verification_mental_model_audit.md) | Probes the developer's own narration of AI code against the code itself to catch silent misunderstandings |

### Maintenance (for AI-generated code you no longer fully remember)
| File | What it does |
|------|--------------|
| [`ai_verification_understanding_decay_tracker.md`](ai_verification_understanding_decay_tracker.md) | Scores decay (Fresh/Dim/Faded/Gone) and gates modification behind a layer-appropriate refresh |
| [`ai_verification_architectural_taste_gate.md`](ai_verification_architectural_taste_gate.md) | Classifies a decision as Taste (human) / Pattern (rule) / Contextual, with routing and draft rule |

### Rule building (from repeated decisions to codified guidance)
| File | What it does |
|------|--------------|
| [`ai_pattern_rule_extraction_from_decisions.md`](ai_pattern_rule_extraction_from_decisions.md) | Mines recent sessions for ≥3-instance decisions and drafts rules with exceptions, scope, and placement |
| [`ai_pattern_delegation_rule_test.md`](ai_pattern_delegation_rule_test.md) | Stress-tests a candidate rule across five scenarios; outputs DELEGATE / PROVISIONAL / DO NOT DELEGATE |

### Reflection and capture (the compounding layer)
| File | What it does |
|------|--------------|
| [`../../domain-personal-development/prompts/agency/agency_ai_session_weekly_reflection.md`](../../domain-personal-development/prompts/agency/agency_ai_session_weekly_reflection.md) | 30-minute structured weekly reflection: session inventory, friction log, pattern findings, ≤3 actions |
| [`../../domain-productivity/bottlenecks/bottleneck_observation_capture_habits.md`](../../domain-productivity/bottlenecks/bottleneck_observation_capture_habits.md) | Designs a low-friction in-session capture habit tailored to the developer's actual environment |

---

### Auto-improving agent systems
| File | What it does |
|------|--------------|
| [`ai_pattern_auto_improving_triplet_diagnostic.md`](ai_pattern_auto_improving_triplet_diagnostic.md) | Audits the three preconditions for real improvement — task set, metrics, traces — and names the weakest leg |
| [`ai_pattern_auto_improving_metric_gaming_premortem.md`](ai_pattern_auto_improving_metric_gaming_premortem.md) | Pre-mortem against seven gaming-path shapes with counter-measures, early-warning signals, and stop-the-loop triggers |
| [`ai_pattern_auto_improving_trace_infrastructure_audit.md`](ai_pattern_auto_improving_trace_infrastructure_audit.md) | Four-axis audit (Coverage / Linkage / Fidelity / Retention) of the observability behind the loop |

### Agent task design (choosing, scoping, and running agent-delegated tasks)
| File | What it does |
|------|--------------|
| [`ai_pattern_agent_task_first_delegation_spec.md`](ai_pattern_agent_task_first_delegation_spec.md) | Screens a candidate first-delegation task and produces the spec + what-to-learn note |
| [`ai_pattern_agent_task_code_distance_scorer.md`](ai_pattern_agent_task_code_distance_scorer.md) | Five-axis code-distance score (Entry / Read / Edit / Semantic / Implicit) with Delegate / Decompose / DIY verdict |
| [`ai_pattern_agent_work_loop_design.md`](ai_pattern_agent_work_loop_design.md) | Per-task loop: schema, drift checks, convergence, stop policy, fallback, observability, pseudocode |
| [`ai_pattern_agent_code_footgun_detector.md`](ai_pattern_agent_code_footgun_detector.md) | Targeted scan for 12 recurring footguns in agent-generated code with re-prompt for the agent |
| [`ai_pattern_agent_autonomy_jargon_translator.md`](ai_pattern_agent_autonomy_jargon_translator.md) | Translates agent / autonomy jargon into accurate plain language for a specific non-technical audience |

---

## Existing workflow prompts (from prior passes)

| File | What it does |
|------|--------------|
| [`workflow_ai_codebase_subtraction_pass.md`](workflow_ai_codebase_subtraction_pass.md) | Systematic deletion audit across seven categories of AI-generated bloat |
| [`workflow_ai_comment_narration_cleanup.md`](workflow_ai_comment_narration_cleanup.md) | Removes AI-style narrating comments while preserving load-bearing documentation |
| [`workflow_ai_prelaunch_overengineering_audit.md`](workflow_ai_prelaunch_overengineering_audit.md) | Pre-launch review that catches speculative abstractions and premature generalization |

---

## Typical flow

1. **Stance check** — `../../domain-personal-development/prompts/identity/identity_engineering_manager_stance.md`. Set the frame once; revisit every few months.
2. **Per-task opening** — `ai_pattern_intent_and_verification_first.md` (with `ai_pattern_outcome_language_translator.md` if your first draft of the prompt leaked implementation). For novel problems, swap to `ai_pattern_unstructured_start_exploration.md`.
3. **Calibrate verification** — `ai_pattern_verification_depth_calibrator.md` before the agent starts; escalate to `ai_review_failure_mode_premortem.md` for high-stakes changes.
4. **Review the diff** — `ai_review_outcome_level_code_review.md`, followed by `ai_verification_mental_model_audit.md` for code you intend to own.
5. **Ship, then capture** — `../../domain-productivity/bottlenecks/bottleneck_observation_capture_habits.md` feeds the reflection pipeline.
6. **Weekly** — `../../domain-personal-development/prompts/agency/agency_ai_session_weekly_reflection.md` and `ai_pattern_rule_extraction_from_decisions.md`.
7. **When codifying** — `ai_pattern_delegation_rule_test.md` stress-tests candidate rules; `ai_verification_architectural_taste_gate.md` draws the line between delegable pattern and human-only taste.
8. **Before modifying older code** — `ai_verification_understanding_decay_tracker.md` gates the edit on a refresh appropriate to the decay.

---

## Core techniques used across this subfolder

| Technique | What it contributes |
|-----------|---------------------|
| ST-01 Clear Objective Statement | Every prompt names a narrow output, not a general field |
| ST-02 Structured Sequential Instructions | Numbered pipelines keep sessions on-track and reproducible |
| RT-02 Multi-Dimensional Analysis | Decisions scored across multiple axes rather than single-feeling judgments |
| CM-02 Constraint Specification | Explicit Must / Must Not rules guard against common AI-augmented failure modes |
| QA-01 Chain-of-Verification | Self-check sections force a second pass before the output is trusted |
| QA-02 Adversarial Stress-Test | Pre-mortem and rule-test prompts actively attack the candidate answer |
| DS-06 Prioritization Guidance | Likelihood × severity, L0–L4 ladders, rule-priority ordering |
| ED-03 Guided Discovery | Reflection and exploration prompts surface the user's own tacit knowledge |
| RT-05 Evidence-Based Reasoning | ≥3-instance minimum for pattern claims; cited evidence per rule |
| RT-03 Tree of Thoughts | Exploration prompt requires multiple alternative shapes before convergence |

---

## Related subfolders

- [`../done-definition/`](../done-definition/) — gate-based convergence loops for agentic tasks
- [`../workflows/`](../workflows/) — general engineering workflow prompts
- [`../../domain-agentic-resources/commands/multi-agent/`](../../domain-agentic-resources/commands/multi-agent/) — multi-agent architecture design (planner / worker / judge, coordination, isolation boundaries)
- [`../../domain-prompt-engineering/delegation/`](../../domain-prompt-engineering/delegation/) — choosing whether to delegate and specifying intent upstream
- [`../../domain-software-engineering/analysis/`](../../domain-software-engineering/analysis/) — single-shot code analysis prompts
