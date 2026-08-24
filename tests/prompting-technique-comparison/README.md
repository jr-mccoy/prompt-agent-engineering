# Prompting Technique Comparison Test

## Purpose

A/B test comparing **8 experimental "inside-out" techniques** (generated from model self-reflection) against **established repository techniques** (from `techniques/MASTER_TECHNIQUE_INDEX.md`) on the same complex coding task.

## The Task

**Distributed Task Scheduler with Work-Stealing** — a Python implementation requiring:

- Thread-safe priority queue with multiple priority levels
- Worker pool with work-stealing between workers
- Dead letter queue for failed tasks with retry logic
- TTL-based task expiration
- Graceful shutdown with in-flight task completion
- Metrics/observability (task counts, latency, queue depths)
- Proper error isolation (one task failure doesn't crash the scheduler)

This task was chosen because it pushes models to their limits across multiple dimensions:
- **Concurrency**: Thread safety, race conditions, deadlocks
- **State management**: Multiple interacting stateful subsystems
- **Error handling**: Failure modes at every layer
- **Architecture**: Clean separation of concerns under complexity
- **Edge cases**: Shutdown ordering, empty queues, poison pills, starvation

## Test Structure

```
prompting-technique-comparison/
├── README.md                          # This file
├── TASK_DEFINITION.md                 # The raw task (shared context for all prompts)
├── SCORING_RUBRIC.md                  # How to evaluate outputs
│
├── experimental/                      # Experimental "inside-out" techniques
│   ├── 01_pre_commitment_extraction.md
│   ├── 02_failure_simulation_first.md
│   ├── 03_attention_pincer.md
│   ├── 04_trajectory_seeding.md
│   ├── 05_adversarial_self_split.md
│   ├── 06_cognitive_load_separation.md
│   ├── 07_recursive_self_specification.md
│   ├── 08_contrastive_pair_anchoring.md
│   └── combo_pre_commitment_plus_failure_sim.md
│
├── established/                       # Repository's established techniques
│   ├── 01_standard_baseline.md        # ST-01 + ST-02 + ST-03 + CM-01 + CM-02
│   ├── 02_expert_role_with_cot.md     # RP-01 + RT-01 + RT-05 + QA-01
│   ├── 03_multi_dimensional_analysis.md # RT-02 + DT-01 + DT-04 + DS-06
│   ├── 04_tree_of_thoughts.md         # RT-03 + QA-02 + RT-07
│   ├── 05_full_production_stack.md    # CM-01 + CM-02 + DS-107 + ST-16 + QA-01
│   └── combo_expert_role_cot_adversarial.md # RP-01 + RT-01 + QA-02 + RT-05
│
└── results/                           # Placeholder for test outputs
    └── .gitkeep
```

## How to Run the Test

1. Pick a prompt file from `experimental/` or `established/`
2. Paste it into a fresh Claude conversation (or any model being tested)
3. Save the complete output to `results/` with naming: `{technique}_{model}_{run}.md`
4. Score using `SCORING_RUBRIC.md`

## What We're Testing

| Hypothesis | Experimental Technique | Established Comparison |
|------------|----------------------|----------------------|
| Self-defined criteria > externally imposed | #1 Pre-Commitment | #5 Full Production Stack (CM-02) |
| Bad-first primes quality detection | #2 Failure Simulation | #2 Expert Role + CoT |
| Primacy+recency beats single mention | #3 Attention Pincer | #1 Standard Baseline |
| Steering first thought > generic CoT | #4 Trajectory Seeding | #2 Expert Role + CoT (RT-01) |
| Motivated adversarial > generic review | #5 Adversarial Self-Split | #4 Tree of Thoughts (QA-02) |
| Separated passes > single generation | #6 Cognitive Load Separation | #3 Multi-Dimensional (DT-01) |
| Self-prompting > human prompting | #7 Recursive Self-Spec | #5 Full Production Stack |
| Contrastive examples > instructions | #8 Contrastive Pair | #2 Expert Role + CoT |
