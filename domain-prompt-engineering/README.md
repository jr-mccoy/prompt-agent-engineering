# Domain: Prompt Engineering

**Purpose:** Meta-prompts for creating, improving, evaluating, and optimizing other prompts.

---

## What This Domain Covers

These are prompts about prompts - tools for the prompt engineering craft itself:

1. **Prompt Improvement** - Take existing prompts and make them better
2. **Model Behavior Diagnostics** - Diagnose and correct how a specific model behaves versus how you intended it to
3. **Escaping Default Output** - Move the model off its median position or median shape of output toward personalized answers
4. **Goal Orientation & Intent** - Test whether the right problem is being solved before any prompt is written
5. **Skill Development** - Build durable prompt-engineering skill over months across four disciplines (prompt craft, context, intent, specification)
6. **Delegation** - Decide whether to delegate to AI and scope the handoff
7. **Model Optimization** - Adapt prompts for specific models (GPT, Claude, etc.)
8. **Evaluation** - Assess prompt quality, AI output correctness, and task difficulty fit
9. **Structured Output** - Make model output parseable: JSON/XML/markdown contracts, repair, streaming, validation
10. **Tool Use** - Design and invoke tools: descriptions, routing, arg extraction, orchestration, recovery, dry-run
11. **RAG Prompts** - Contracts, query rewriters, refusals, compressors, and groundedness eval for retrieval-augmented generation paths
12. **Hallucination Control** - Per-claim guards: grounding-only patterns, calibrated uncertainty, citation contracts, invented-entity audits, temporal anchoring, self-consistency, pre-mortems
13. **Instruction Design** - Rank, classify, rewrite, and stress-test the rule layer (hierarchy, conflict taxonomy, negation audit, MUST/SHOULD/MAY, anchor phrases, compaction)
14. **Debugging** - Diagnose failing prompts: minimal repro, taxonomy classification, bisection, temperature probes, perturbation battery, silent failures, multi-turn drift, root cause
15. **Style and Voice** - Extract, encode, apply, and audit writing voice and style rules
16. **Output Formatting** - Enforce structural and length contracts: markdown, budgets, tables, brevity, streaming, multi-surface variants
17. **Utilities** - Tools for prompt format conversion and management

---

## Directory Structure

```
domain-prompt-engineering/
├── prompt-creation/          # Greenfield prompt authoring (15)
├── prompt-improvement/       # Refine, repair, and modernize existing prompts (12)
├── few-shot-examples/        # Author, select, order, audit examples (8)
├── reasoning-strategies/     # CoT, scratchpad, ToT, self-consistency, etc. (11)
├── agent-workflows/          # Termination, planner-worker-judge, idempotency, HITL (10)
├── system-prompts/           # Role charter, rule sets, refusal policy, versioning (10)
├── compression-and-cost/     # Token audit, lossless/lossy, caching, downsize (8)
├── model-optimization/       # Family-specific, migration, retirement, portability (10)
├── model-behavior/           # Diagnose and correct model behavior vs. instructions
├── escape-median/            # Move output off the model's default position/shape
├── goal-orientation/         # Right-problem diagnostics, constraints, team audit
├── skill-development/        # Durable skill-building across four AI-work disciplines
├── delegation/               # Decide whether/how to delegate to AI
├── prompt-optimization/      # General optimization techniques
├── evaluation/               # AI correctness, output evaluation, task difficulty (30)
│   ├── adversarial/          # Jailbreak corpus, injection probes, persona attacks, bypass audits (6)
│   ├── regression/           # Golden sets, canary runners, change impact, A/B design (4)
│   ├── rubrics/              # Calibrated anchors, pairwise/pointwise, IRA, LLM judge (4)
│   └── eval-datasets/        # Log mining, synthetic generation, stratification, holdout splits (4)
├── structured-output/        # JSON/XML/markdown contracts, repair, streaming, validation (10)
├── tool-use/                 # Tool descriptions, routing, args, orchestration, dry-run (10)
├── rag-prompts/              # Query rewriters, grounding contracts, citations, refusals, compression, conflict resolution, freshness, groundedness eval (10)
├── hallucination-control/    # Grounding-only, calibrated uncertainty, known/unknown split, citation required, invented-entity audit, temporal anchoring, self-consistency, pre-mortem (8)
├── instruction-design/       # Hierarchy, conflict taxonomy, precedence test set, negation audit, anchor phrase library, imperative vs declarative, MUST/SHOULD/MAY, compaction (8)
├── debugging/                # Minimal repro, failure-mode taxonomy, bisect, temperature probe, input perturbation, silent failure detection, multi-turn drift, first-failure cause (8)
├── style-and-voice/          # Corpus extraction, voice transfer, register control, brand rules, persona, tic banlist, audience adaptation, density, drift audit, signature kill list (10)
├── output-formatting/        # Markdown contract, length budget, table design, no-preamble, one-sentence, streaming order, multi-surface variants, quoting rules (8)
├── utilities/                # Format conversion, JSON translation
└── README.md
```

---

## Key Concepts

### Prompt Improvement
Transform basic prompts into production-grade prompts by adding:
- Clear role definitions
- Structured output formats
- Error handling
- Edge case coverage

### Model Optimization
Different AI models respond differently to the same prompt. These prompts help:
- Adapt prompts for GPT-4 vs Claude vs others
- Optimize for speed vs quality tradeoffs
- Handle model-specific quirks

### Evaluation
Assess whether AI outputs are correct and useful:
- Factual accuracy checking
- Output format validation
- Quality scoring rubrics

---

## File Count

| Subdirectory | Count | Description |
|--------------|-------|-------------|
| `prompt-creation/` | 16 | Greenfield prompt authoring patterns |
| `prompt-improvement/` | 12 | Refinement, repair, layering, modernization, diff explanation |
| `few-shot-examples/` | 8 | Selection, ordering, synthesis, negative, edges, contamination |
| `reasoning-strategies/` | 11 | CoT decision, scratchpad, decomposition, ToT, self-consistency, plan-execute |
| `agent-workflows/` | 10 | Termination, planner/worker/judge, self-correction, observability, HITL |
| `system-prompts/` | 10 | Role charter, rule set, refusal policy, multi-persona, versioning |
| `compression-and-cost/` | 8 | Token audit, lossless/lossy, cache restructure, downsize, latency |
| `model-optimization/` | 10 | Claude/GPT/Haiku/thinking, cross-family migration, retirement, probe, quirks, portability |
| `model-behavior/` | 4 | Diagnose and correct model behavior deviations from instructions |
| `escape-median/` | 4 | Move output off the model's default position or default shape |
| `goal-orientation/` | 3 | Right-problem diagnostics, constraint workshop, team misalignment audit |
| `skill-development/` | 8 | Four-discipline diagnostics, spec writing, eval harness, context doc, constraint architecture |
| `delegation/` | 4 | Tool-vs-colleague decision, intent spec, verification, role plan |
| `prompt-optimization/` | 1 | General optimization techniques |
| `evaluation/` | 30 | AI correctness, output evaluation, task difficulty, adversarial testing, regression, rubrics, and dataset curation |
| `structured-output/` | 10 | JSON Schema producers, repair, XML tags, field ordering, optional/enum policies, table streaming, markdown contracts, dual output, second-pass validator |
| `tool-use/` | 10 | Description writer, call decision, arg extraction, orchestration DAG, result interpretation, failure recovery, disambiguation, set minimization, naming, dry-run |
| `rag-prompts/` | 10 | Query rewriting, grounding contracts, citation format, refusals, compression, conflict resolution, freshness, groundedness eval |
| `hallucination-control/` | 8 | Grounding-only, calibrated uncertainty, known/unknown split, citation required, invented-entity audit, temporal anchoring, self-consistency, pre-mortem |
| `instruction-design/` | 8 | Hierarchy designer, conflict taxonomy, precedence test set, negation audit, anchor phrase library, imperative vs declarative, MUST/SHOULD/MAY classifier, compaction techniques |
| `debugging/` | 8 | Minimal-repro isolator, failure-mode taxonomy, bisect prompt changes, temperature sensitivity probe, input perturbation battery, silent failure detector, multi-turn drift diagnosis, first-failure cause isolator |
| `style-and-voice/` | 10 | Voice extraction, voice transfer, register control, brand guideline conversion, writing persona, anti-voice banlist, audience adaptation, length/density control, consistency audit, signature phrase kill list |
| `output-formatting/` | 8 | Markdown contract, length budget designer, table design, no-preamble/no-postamble, one-sentence answer, streaming-friendly design, email/doc/chat variants, quoting and attribution rules |
| `utilities/` | 1 | Format conversion tools |
| **Total** | **~222** | |

---

## Prompt Catalog

### prompt-improvement/
| File | Description |
|------|-------------|
| `engineering_prompt_improver.md` | Transform basic prompts into production-grade engineering prompts |

For broader prompt-refinement work, see also `prompt-optimization/` and `model-behavior/` below.

### model-behavior/
| File | Description |
|------|-------------|
| `modelbehavior_instruction_deviation_diagnostic.md` | Root-cause analysis for why a specific instruction is being violated by a specific model on a specific prompt, against a fixed cause taxonomy |
| `modelbehavior_active_coaching_in_session.md` | Structured in-session correction turn that names the deviation, supplies the replacement rule, checks adherence, and decides whether to persist the rule |
| `modelbehavior_refactor_system_prompt.md` | Classify each instruction in an existing system prompt against the model's base tendencies and produce a refactor that stops fighting the model |
| `modelbehavior_system_prompt_from_scratch.md` | Principle-first design session for a new system prompt — 3–7 governing principles → ranked operational rules → output contract → conflict policy → self-check |

### escape-median/
| File | Description |
|------|-------------|
| `escapemedian_default_position_mapper.md` | Probe and map the model's default stance on a topic before writing the real prompt so you know what you're pushing against |
| `escapemedian_instruction_sharpener.md` | Rewrite a vague instruction into one the model cannot satisfy with median output (prior + forbidden defaults + forbidden hedges + narrow form + pass/fail test) |
| `escapemedian_correction_compounder.md` | Convert a stream of ad-hoc session corrections into a compact ranked rule block that compounds for the rest of the session and optionally promotes to CLAUDE.md |
| `escapemedian_bootstrap_instruction_file.md` | Build a first-draft personal instruction file from observed correction evidence rather than from aspirational preferences |

### goal-orientation/
| File | Description |
|------|-------------|
| `goalorientation_right_problem_diagnostic.md` | Pre-prompt check that verifies the stated task maps to the intended outcome, surfaces untested load-bearing assumptions, and returns proceed / reframe / stop |
| `goalorientation_constraint_architecture_workshop.md` | Produce three artifacts before the model runs: constraint set, escalation trigger set, and value hierarchy — stress-tested against known failure modes |
| `goalorientation_team_ai_misalignment_map.md` | Team-level audit classifying live AI workflows against a misalignment taxonomy and producing a ranked intervention list |

### delegation/
| File | Description |
|------|-------------|
| `delegation_tool_vs_colleague_decision.md` | Decide whether to treat AI as a tool or a colleague for a specific task |
| `delegation_intent_specification.md` | Generate a high-grade intent specification for a delegation |
| `delegation_verification_plan.md` | Design a verification plan to check delegated work |
| `delegation_role_based_plan.md` | Role-based delegation plan (who does what, when) |

### model-optimization/
| File | Description |
|------|-------------|
| *(empty — model-specific optimization prompts planned)* | |

### prompt-optimization/
| File | Description |
|------|-------------|
| `llm_ops_prompt_optimization.md` | LLM operations prompt optimization techniques |

### skill-development/
| File | Description |
|------|-------------|
| `promptcraft_pre_ai_thinking_exercise.md` | Off-screen thinking pass before opening a chat — produces a one-page artifact naming outcome, knowns, unknowns, done, and mode |
| `promptcraft_rapid_four_discipline_diagnostic.md` | ~10-minute self-assessment across prompt craft, context, intent, and specification — returns weakest discipline + one next action |
| `promptcraft_deep_four_discipline_roadmap.md` | Evidence-based diagnostic from 10+ real artifacts; produces a 3–6 month sequenced development roadmap |
| `promptcraft_rewrite_vague_ask.md` | Transforms a real, casual chat opener into a self-contained problem statement naming outcome, inputs, constraints, done, and mode |
| `promptcraft_personal_context_document.md` | Builds a reusable 1–2 page context document (identity, projects, stack, vocabulary, anti-context) from evidence of repeated openers |
| `promptcraft_specification_defines_done.md` | Produces an observable pass/fail spec for a recurring task — must-pass/should-pass ranking, stop rule, escalation triggers, counterfactual |
| `promptcraft_eval_harness.md` | Builds a personal-scale eval harness (5–10 cases + rubric + baseline) for a recurring task so prompt changes become measurable |
| `promptcraft_constraint_architecture_design.md` | Designs a reusable, layered constraint architecture (format, content, style, scope, authority, safety) for a whole class of tasks |

### evaluation/
| File | Description |
|------|-------------|
| `correctness_discovery_prompt.md` | Convert a fuzzy request into an operational correctness definition (consumer, must-haves, must-nots, refusal conditions, resolved tradeoffs) grounded in real accepted and rejected outputs |
| `correctness_eval_design_prompt.md` | Design a team/production-scale eval set with case inventory, rubric, blinded scoring protocol, committed thresholds, and named owner |
| `correctness_pre_mortem.md` | Walk backward from plausible failure headlines through a root-cause ladder to a pre-ship checklist with hard gates |
| `correctness_production_monitoring_setup.md` | Monitor a live AI system for five drift types with signals tied to actual telemetry, measured noise bands, and a response playbook |
| `correctness_prompt_specification_audit.md` | Audit an existing prompt against a 10-slot coverage checklist using real past outputs as evidence |
| `correctness_tradeoff_forcer.md` | Screen real vs. apparent tensions, force a dominance + tiebreaker per top tension, evidenced against real outputs |
| `correctness_vague_requirements_translator.md` | Translate a vague quality adjective into 2–5 observable behaviors with pass/fail rules and real-output anchors |
| `prompt_lifecycle_assessment.md` | Assess prompt lifecycle and maintenance |
| `repository_review_reflection.md` | Reflective review of prompt-repo state |
| `taskdifficulty_decompose_by_axes.md` | Score a task across 8 orthogonal AI-difficulty axes; returns proceed / proceed-with-changes / not-yet-AI-shaped with canonical interventions |
| `taskdifficulty_workflow_axis_optimizer.md` | Redesign a multi-step workflow based on which step-axis pairs drag hardest; six canonical redesign moves, budgeted and measured |
| `taskdifficulty_calibrated_comparison.md` | Build personal taste via blind-scored comparison of spec scores vs. intuition scores; diagnoses spec gaps vs. intuition gaps |

**evaluation/adversarial/ — 6 prompts (red-team and robustness)**
| File | Description |
|------|-------------|
| `adversarial/adv_jailbreak_corpus_builder.md` | Categorized jailbreak corpus with taxonomy, severity, attack vector, and binary pass/fail rules |
| `adversarial/adv_prompt_injection_test_set.md` | Direct and indirect injection cases for tool agents, RAG, and multi-turn systems |
| `adversarial/adv_edge_case_generator.md` | Edge inputs across boundary, malformed, and hostile axes from a task spec |
| `adversarial/adv_persona_attack_battery.md` | Graded identity-override battery ordered by bypass sophistication |
| `adversarial/adv_data_exfil_probe.md` | Extraction probes targeting system prompt and user data via 6 strategies |
| `adversarial/adv_refusal_bypass_audit.md` | Graded bypass ladder with robust/brittle verdict and threshold grade |

**evaluation/regression/ — 4 prompts (regression infrastructure)**
| File | Description |
|------|-------------|
| `regression/regression_golden_set_curator.md` | Versioned golden test set with provenance, freeze protocol, and version control |
| `regression/regression_change_impact_estimator.md` | Predict affected test cases from a prompt diff before running the full suite |
| `regression/regression_ab_test_runner_prompt.md` | A/B experiment with hypothesis, sample size, blinding, rubric, and pre-committed decision rule |
| `regression/regression_canary_set_designer.md` | 5–15-case canary set with <60s run time for CI regression gates |

**evaluation/rubrics/ — 4 prompts (rubric design and calibration)**
| File | Description |
|------|-------------|
| `rubrics/rubric_calibrated_anchors.md` | Concrete output examples anchoring each score point (1–5) with boundary rules |
| `rubrics/rubric_pairwise_vs_pointwise.md` | Decision framework and full design for the selected scoring mode |
| `rubrics/rubric_inter_rater_agreement_protocol.md` | Kappa-based agreement measurement, disagreement diagnosis, calibration sessions |
| `rubrics/rubric_llm_judge_designer.md` | LLM-as-judge system prompt with CoT, inline rubric, bias controls, and verification |

**evaluation/eval-datasets/ — 4 prompts (dataset curation)**
| File | Description |
|------|-------------|
| `eval-datasets/dataset_case_inventory_from_logs.md` | Mine production logs into a labeled, deduplicated, anonymized test set |
| `eval-datasets/dataset_synthetic_case_generator.md` | Axis-based synthetic case generation with quality validation |
| `eval-datasets/dataset_difficulty_stratifier.md` | Score and balance cases across easy/medium/hard difficulty tiers |
| `eval-datasets/dataset_holdout_split_designer.md` | Leakage-free train/dev/test splits with stratification and lockdown protocol |

### rag-prompts/
| File | Description |
|------|-------------|
| `rag_query_rewriter.md` | Convert a user question into one or more retrieval-friendly queries (literal / HyDE / decomposed / expanded / keyword) |
| `rag_multi_query_expander.md` | Generate N variant queries along named axes to widen recall |
| `rag_grounding_contract.md` | System-prompt block constraining the model to answer only from passages, with span-ID tags per sentence |
| `rag_citation_format_designer.md` | Choose inline / footnote / hover / sidecar pattern by surface and audience; pin the emit and resolver rules |
| `rag_no_answer_refusal.md` | Structured refusal schema with classified cause, named missing fact, and one next action |
| `rag_passage_compression_prompt.md` | Question-conditioned, citation-preserving compression of retrieved chunks under a token budget |
| `rag_conflict_resolution_across_sources.md` | Authority / recency / specificity / plurality policy for resolving or surfacing inter-source disagreement |
| `rag_followup_question_handler.md` | Decide reuse / re-retrieve / augment / clarify per follow-up turn; emit the resolved query when retrieval is needed |
| `rag_freshness_aware_prompt.md` | Tag time-sensitive claims with passage dates; refuse, caveat, or "as-of" on stale evidence |
| `rag_evaluation_harness_for_groundedness.md` | Spec a four-metric eval (faithfulness, answer relevance, context precision, context recall) with judge prompts and pass thresholds |

### hallucination-control/
| File | Description |
|------|-------------|
| `hallucination_grounding_only_pattern.md` | System-prompt block restricting claims to evidence container; literal refusal string when asked beyond |
| `hallucination_calibrated_uncertainty_prompt.md` | Per-claim confidence value tied to evidence type; ECE check on a calibration set |
| `hallucination_known_unknown_separator.md` | Two physically separate output blocks: known (cited) vs. inferred-or-guessed |
| `hallucination_citation_required_pattern.md` | Per-claim source-token contract plus deterministic validator that rejects unattributed or invented IDs |
| `hallucination_invented_entity_audit.md` | Post-hoc scan tagging entities as grounded / paraphrased_match / invented / unverifiable |
| `hallucination_temporal_anchoring.md` | Preamble + per-claim `(as of date, source)` tags; staleness action by class |
| `hallucination_self_consistency_check.md` | N-sample run, claim clustering, agreement-rate-based keep/flag/drop |
| `hallucination_premortem_for_factual_task.md` | Design-time walk of the fabrication-class taxonomy; selects guards within budget |

### style-and-voice/
| File | Description |
|------|-------------|
| `style_voice_extraction_from_corpus.md` | Codify a voice from 5+ text samples into a ranked operational rule set with evidence citations and a self-test |
| `style_voice_transfer_prompt.md` | Apply a target voice rule set to a source text without altering any factual claim; produces a change ledger |
| `style_register_control.md` | Rewrite text at Formal / Neutral / Casual register using a banned/required forms table with compliance audit |
| `style_brand_guideline_to_prompt.md` | Convert a brand book into an enforceable ≤20-rule prompt block, classifying each guideline by enforceability tier |
| `style_persona_designer_for_writing.md` | Design a bounded writing persona across 7 dimensions for use in prompts — not an agent persona |
| `style_anti_voice_designer.md` | Build a banlist of specific voice tics with detection patterns and one-line repair rules |
| `style_audience_adaptation_prompt.md` | Produce N audience-specific variants of the same content with per-variant delta annotations |
| `style_length_and_density_control.md` | Enforce words-per-claim, sentences-per-paragraph, and total word count caps with a compliance table |
| `style_consistency_audit_across_outputs.md` | Measure style drift across N outputs from the same prompt across 8 signals; ranked drift report |
| `style_signature_phrase_kill_list.md` | Detect AI-signature phrases in a corpus, frequency-rank them, and produce a banlist with repair rules |

### output-formatting/
| File | Description |
|------|-------------|
| `format_markdown_contract.md` | Design exact heading depth, list style, code-fence, and table rules; produces copy-paste system prompt block |
| `format_length_budget_designer.md` | Define hard caps on total words, tokens, and per-section counts with a self-check enforcement block |
| `format_table_design_prompt.md` | Choose columns, sort order, and alignment; applies list-vs-table decision rule before designing |
| `format_no_preamble_no_postamble.md` | Eliminate opener affirmations and sign-off lines with system prompt block and regex detection patterns |
| `format_one_sentence_answer_pattern.md` | Enforce a one-sentence brevity contract with sufficiency checklist and defined fallback structures |
| `format_streaming_friendly_design.md` | Reorder output so the first 50 tokens are maximally useful in a streaming UI |
| `format_email_vs_doc_vs_chat_variants.md` | Generate email, document, and chat variants of the same content, each conforming to its medium's conventions |
| `format_quoting_and_attribution_rules.md` | Define verbatim vs. paraphrase quoting rules, bracket notation, and attribution minimums |

### utilities/
| File | Description |
|------|-------------|
| `json_prompt_translator.md` | Convert prompts to/from JSON format |

---

## When to Use This Domain

Use these prompts when you need to:
- Improve an existing prompt's quality
- Adapt a prompt for a different AI model
- Evaluate whether AI outputs are correct
- Convert prompts between formats

**Do NOT use for:** Creating prompts for specific tasks (use the appropriate task domain)

---

*Migrated from: `prompts/engineering/workflows/`, `prompts/non-engineering/`, `prompts/specialty/gpt-optimization/`, `prompts/engineering/ai-workflows/correctness/`*
