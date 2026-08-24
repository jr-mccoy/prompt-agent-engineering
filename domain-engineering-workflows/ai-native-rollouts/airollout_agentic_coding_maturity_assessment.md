---
title: "Agentic Coding Maturity Assessment"
category: engineering-workflows/ai-native-rollouts
description: "Assess a team or org's agentic-coding maturity across task-horizon, role, and oversight axes, score readiness against the four agentic-coding priorities, and name the single highest-leverage next move."
techniques:
  - ST-47
  - DS-06
  - AG-28
  - QA-08
  - RT-02
difficulty: intermediate
tags:
  - agentic-coding
  - maturity-model
  - oversight
  - delegation
  - adoption
updated: "2026-06-19"
related_prompts:
  - domain-engineering-workflows/ai-native-rollouts/airollout_tiered_adoption_rollout.md
  - domain-engineering-workflows/ai-native-rollouts/airollout_bottleneck_migration_plan.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_delegation_paradox_triage.md
---

# Agentic Coding Maturity Assessment

**Objective:** Place a team or organization on a defensible maturity tier for agentic coding by scoring three axes — task horizon, role, and oversight — then test that placement against the four near-term agentic-coding priorities, and end on the single highest-leverage next move rather than a generic improvement list.

**When to Use:**
- A team is using coding agents and wants an honest read on where it sits versus where it could be.
- You are planning an adoption roadmap and need a current-state baseline before sequencing changes.
- Leadership is asking "are we actually getting step-function gains, or just faster typing?"

**When NOT to Use:**
- The team has not yet adopted coding agents at all — start with a tiered rollout (`airollout_tiered_adoption_rollout.md`), not a maturity read.
- You only need to triage a specific task set for delegation (use `ai_pattern_delegation_paradox_triage.md`).

**Source:** Figures and predictions are drawn from a vendor report, Anthropic's *2026 Agentic Coding Trends Report* — figures attributed inline; no source text reproduced.

## Inputs / Context

Provide what you can; the assessment degrades gracefully if some are missing:
- **Current task patterns** — what agents are actually asked to do, and how long those tasks take a human.
- **Role distribution** — who treats agents as a tool versus who orchestrates multiple agent workstreams.
- **Review practice** — what gets human-reviewed, what is automated, what is escalated.
- **The four priorities** — current state on multi-agent coordination, scaled oversight, non-engineering reach, and security-from-design.
- **Observed gains** — are improvements linear (faster) or step-function (newly possible)?

## Constraints

**Must:**
- Score each axis with a named current level and the specific evidence that places it there.
- Tie the maturity read to the four priorities, identifying the largest gap.
- Acknowledge the collaboration paradox: heavy AI *use* does not imply heavy *delegation*.

**Must Not:**
- Inflate the tier to flatter the team — place the level the evidence supports, not the aspiration.
- Produce a long undifferentiated improvement list instead of one highest-leverage move.
- Treat "we use AI a lot" as proof of maturity; usage and delegation are different measures.

**Instructions:**

1. **Place the team on the task-horizon ladder.** Identify the longest task the team reliably delegates: one-shot tasks (minutes) → full feature sets (hours, periodic checkpoints) → complete systems (days/weeks with human checkpoints). The reliable ceiling — not the occasional success — is the level.

2. **Assess role maturity.** Distinguish implementers (use the agent as a faster tool) from orchestrators (value has shifted to system architecture, agent coordination, quality evaluation of agent output, and strategic problem decomposition; they shepherd several features in parallel). Place the team by where most of its senior value-add sits.

3. **Assess oversight maturity.** Locate the team between review-everything and review-what-matters: is routine verification automated, with only novel, boundary, or strategic cases escalated, and do agents learn *when* to ask for help? More autonomy is earned by stronger automated verification, not by relaxed attention.

4. **Score the four priorities.** For each, mark current state and gap: (a) multi-agent coordination to handle complexity single agents cannot; (b) scaling human-agent oversight via AI-automated review systems; (c) extending agentic coding beyond engineering to domain experts; (d) embedding security architecture from the earliest design stages, given the dual-use reality that the same capability scales offense.

5. **Apply the collaboration-paradox check.** Per the report, developers use AI across roughly 60% of work yet can fully delegate only 0–20% of tasks, and about 27% of AI-assisted work is net-new work that would not otherwise happen. Verify the team's stated maturity reflects delegation depth, not just usage breadth.

6. **Test for step-function vs. linear gains.** The three compounding multipliers — agent capability × orchestration × better use of human experience — should produce step-function gains. If the team only reports "faster," that signals a missing multiplier (usually orchestration or expert leverage), not just slower progress.

7. **Name the single highest-leverage next move.** From the axis levels and the four-priority gaps, select the one change that most raises the binding constraint. State why it outranks the alternatives.

**Output Format:**

A markdown maturity assessment:
- **Axis Levels** — table: Axis | Current level | Evidence | Next level looks like
- **Four-Priority Gap List** — per priority: current state, gap, why it matters
- **Collaboration-Paradox Check** — usage vs. delegation reality for this team
- **Gains Pattern** — linear or step-function, with the missing multiplier if linear
- **Highest-Leverage Next Move** — the one move + the binding constraint it lifts

## Verification

- [ ] Each of the three axes has a named level backed by specific evidence.
- [ ] The task-horizon level reflects the reliable ceiling, not a one-off success.
- [ ] All four priorities are scored with an explicit gap.
- [ ] The collaboration-paradox check separates usage from delegation.
- [ ] Exactly one highest-leverage next move is named, with justification over alternatives.

## False-Positive Prevention

❌ **DON'T:**
- Equate broad AI usage with high delegation maturity — the paradox is precisely that they diverge.
- Score a team "orchestrator-level" because one engineer runs parallel agents; place the team by where its value mostly sits.
- Mark oversight "mature" when review-everything has simply been abandoned rather than automated.
- End with a buffet of improvements that lets the team avoid the hard binding constraint.

✅ **DO:**
- Tie each level to observable evidence (longest reliable task, who does architecture vs. typing, what gets escalated).
- Treat automated verification strength as the gate for earning more autonomy.
- Read step-function-vs-linear gains as a diagnostic for a missing multiplier.
- Force a single prioritized next move so the assessment changes behavior.

## Example Output

```markdown
## Agentic Coding Maturity: Platform Team (8 engineers)

### Axis Levels
| Axis | Current level | Evidence | Next level looks like |
|---|---|---|---|
| Task horizon | Full feature sets (hours) | Agents close scoped tickets end-to-end; systems-scale work still hand-driven | Multi-day system builds with human checkpoints |
| Role | Mixed: 2 orchestrators, 6 implementers | Two seniors shepherd parallel features; rest use agents as faster autocomplete | Most seniors orchestrating; value in architecture + eval |
| Oversight | Review-everything | Every PR fully human-read; no automated triage of routine diffs | Routine verification automated; only novel/boundary cases escalated |

### Four-Priority Gap List
- **Multi-agent coordination** — single-agent only. Gap: no orchestration of agents on complexity beyond one agent's reach.
- **Scaled oversight** — none automated. Gap: largest bottleneck; review time caps throughput.
- **Beyond engineering** — engineers only. Gap: data/PM domain experts not yet enabled.
- **Security from design** — bolted on at PR time. Gap: dual-use risk not modeled at design stage.

### Collaboration-Paradox Check
Team self-reports "heavy AI use" (~daily). Actual full delegation ~15% of tasks — consistent with the reported 0–20% band. Maturity claim was inflated by usage breadth.

### Gains Pattern
Linear ("faster"). Missing multiplier: orchestration. Capability is present; experience-leverage and coordination are not compounding.

### Highest-Leverage Next Move
Automate routine PR verification (tests/lint/type gates as the first review pass), freeing senior review for novel cases. This lifts the binding constraint (oversight throughput) and is the precondition for safely raising delegation depth and the task horizon.
```

**Techniques Used:**
- **ST-47 (Maturity / Capability Tiering):** scores the org against named levels on each axis.
- **DS-06 (Prioritization & Severity Guidance):** the largest priority gap and binding constraint drive the conclusion.
- **AG-28 (Agent Oversight Calibration):** the oversight axis and earned-autonomy logic.
- **QA-08 (Self-Consistency Check):** the collaboration-paradox check tests claimed maturity against delegation evidence.
- **RT-02 (Role-Based Expertise):** reasons as an adoption strategist placing a team on a maturity model.

**Related Prompts:**
- `airollout_tiered_adoption_rollout.md` — sequence the rollout once the baseline tier is known.
- `airollout_bottleneck_migration_plan.md` — plan migration of the binding constraint this surfaces.
- `ai_pattern_delegation_paradox_triage.md` — triage specific tasks once role/oversight maturity is set.
