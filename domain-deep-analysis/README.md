# Deep Analysis System

A five-scope, multi-perspective deep-think system designed to compensate for the absence of a human team when working through hard problems with an AI model. Each scope drives the model through five disciplined phases (Frame → Decompose → Multi-perspective → Stress-test → Synthesize), with `AskUserQuestion` (or its plain-text equivalent) used as the primary back-and-forth mechanism at each gate.

**Why five scopes instead of one:** A diagnosis, a recommendation, a sequenced plan, a design spec, and an evaluation report are genuinely different terminal artifacts. Forcing them under one roof waters down the synthesize phase. The five prompts share a backbone but diverge where it matters: framing question, decomposition axes, perspective additions, and final output.

---

## Two versions: rigorous and plain-English

Each of the five scopes ships in **two equivalent versions**:

- **Rigorous version** (`/deepthink-*`) — written in the precise vocabulary of business strategy and engineering analysis ("orthogonal axes," "load-bearing assumption," "reversibility Type 1 / Type 2," "critical path," "tripwires vs. abort conditions"). Best for users already fluent in that vocabulary.
- **Plain-English version** (`/deepthink-*-plain`) — same five-phase rigor, same mandatory perspective roster from [`BACKBONE.md`](BACKBONE.md), same gate-based interaction, same output-format requirements. Just translated into everyday language with worked examples and friendlier check-ins. Best for non-technical users (parents, teachers, freelancers, small business owners, anyone outside business/engineering) or anyone who finds the rigorous original intimidating.

**Quality is equivalent across both versions** — only vocabulary, framing, and scaffolding differ. Pick whichever reads more naturally to you.

---

## When to use which scope

| Scope | Underlying prompt | Rigorous command | Plain-English command | Use when |
|-------|-------------------|------------------|------------------------|----------|
| **Problem analysis** | [`deepthink_problem_analysis.md`](deepthink_problem_analysis.md) / [`_plain`](deepthink_problem_analysis_plain.md) | `/deepthink-problem` | `/deepthink-problem-plain` | "Why is X happening?" / "What's actually going on?" — exploratory, no fixed deliverable, goal is understanding + leverage points |
| **Decision** | [`deepthink_decision.md`](deepthink_decision.md) / [`_plain`](deepthink_decision_plain.md) | `/deepthink-decision` | `/deepthink-decision-plain` | "Should I do A or B?" — converges to a recommendation with rationale, confidence, reversibility, and tripwires |
| **Plan / strategy** | [`deepthink_plan.md`](deepthink_plan.md) / [`_plain`](deepthink_plan_plain.md) | `/deepthink-plan` | `/deepthink-plan-plain` | "How do I get from here to there?" — produces a sequenced plan with risks, checkpoints, and abort conditions |
| **Design / architecture** | [`deepthink_design.md`](deepthink_design.md) / [`_plain`](deepthink_design_plain.md) | `/deepthink-design` | `/deepthink-design-plain` | "What should we build?" — produces a spec with documented tradeoffs and open questions |
| **Evaluation** | [`deepthink_evaluation.md`](deepthink_evaluation.md) / [`_plain`](deepthink_evaluation_plain.md) | `/deepthink-evaluation` | `/deepthink-evaluation-plain` | "Is this existing thing good enough?" — produces an evaluation report with weighted criteria, strengths, defects/risks, missing evidence, recommendation, confidence, and caveats |

Pick by terminal artifact, not by topic. A "security review" can be any of the five depending on whether you want diagnosis, a go/no-go decision, a remediation plan, a hardening spec, or an evaluation report.

---

## The shared backbone

[`BACKBONE.md`](BACKBONE.md) is the single source of truth for behavior shared by all deep-think scopes and their plain-English companions. It defines:

- The five phases: Frame → Decompose → Multi-perspective → Stress-test → Synthesize.
- Gate behavior, including `AskUserQuestion` and plain-chat `**GATE:**` fallback.
- The mandatory Phase 3 perspective roster.
- Scope-conditional perspective candidates.
- Anti-procrastination guidance so deep-think does not become avoidance.
- The rule that scope prompts may extend, but not override, the backbone.

Scope files keep only the scope-specific details: inputs, examples, decomposition method, gate wording, stress-test specifics, output format, and verification checklist.

---

## Files

### User-facing prompts and slash-command wrappers

```
domain-deep-analysis/
├── README.md                                    (this file)
├── BACKBONE.md                                  Shared behavior for every deep-think scope
├── deepthink_problem_analysis.md                Tier-1 prompt for problem/question analysis (rigorous)
├── deepthink_problem_analysis_plain.md          Plain-English companion version
├── deepthink_decision.md                        Tier-1 prompt for decisions (rigorous)
├── deepthink_decision_plain.md                  Plain-English companion version
├── deepthink_plan.md                            Tier-1 prompt for plans / strategies (rigorous)
├── deepthink_plan_plain.md                      Plain-English companion version
├── deepthink_design.md                          Tier-1 prompt for designs / architectures (rigorous)
├── deepthink_design_plain.md                    Plain-English companion version
├── deepthink_evaluation.md                      Tier-1 prompt for evaluating an existing artifact (rigorous)
├── deepthink_evaluation_plain.md                Plain-English companion version
└── commands/
    ├── deepthink-problem.md                     Slash command wrapper (rigorous)
    ├── deepthink-problem-plain.md               Slash command wrapper (plain-English)
    ├── deepthink-decision.md                    Slash command wrapper (rigorous)
    ├── deepthink-decision-plain.md              Slash command wrapper (plain-English)
    ├── deepthink-plan.md                        Slash command wrapper (rigorous)
    ├── deepthink-plan-plain.md                  Slash command wrapper (plain-English)
    ├── deepthink-design.md                      Slash command wrapper (rigorous)
    ├── deepthink-design-plain.md                Slash command wrapper (plain-English)
    ├── deepthink-evaluation.md                  Slash command wrapper (rigorous)
    └── deepthink-evaluation-plain.md            Slash command wrapper (plain-English)
```

---

## Related prompts in this repo

The deep-analysis system pulls techniques from across the repo. If you want to drill into a specific phase rather than run a full session:

- **Frame phase**: [`domain-prompt-engineering/goal-orientation/goalorientation_right_problem_diagnostic.md`](../domain-prompt-engineering/goal-orientation/goalorientation_right_problem_diagnostic.md), [`domain-prompt-engineering/evaluation/correctness_discovery_prompt.md`](../domain-prompt-engineering/evaluation/correctness_discovery_prompt.md)
- **Decompose phase**: [`domain-prompt-engineering/evaluation/taskdifficulty_decompose_by_axes.md`](../domain-prompt-engineering/evaluation/taskdifficulty_decompose_by_axes.md), [`domain-prompt-engineering/evaluation/correctness_tradeoff_forcer.md`](../domain-prompt-engineering/evaluation/correctness_tradeoff_forcer.md)
- **Multi-perspective phase**: [`domain-decision-making/decisioning_blind_spot_mirror_see_what_im_missing.md`](../domain-decision-making/decisioning_blind_spot_mirror_see_what_im_missing.md), [`domain-productivity/validation/validation_adversarial_mini_check.md`](../domain-productivity/validation/validation_adversarial_mini_check.md)
- **Stress-test phase**: [`domain-prompt-engineering/evaluation/correctness_pre_mortem.md`](../domain-prompt-engineering/evaluation/correctness_pre_mortem.md), [`domain-presentations/visual-planning/visualplan_cascade_effects_scan.md`](../domain-presentations/visual-planning/visualplan_cascade_effects_scan.md)
- **Final gate**: [`domain-productivity/validation/validation_final_gate.md`](../domain-productivity/validation/validation_final_gate.md)

---

**Last updated:** 2026-06-30
