---
title: "Design a Tiered AI-Adoption Rollout (Ignore / Use / Build With)"
category: engineering-workflows/ai-native-rollouts
description: "Design a three-tier adoption rollout that separates people who can ignore AI, those who should use it, and those who build with it — with distinct enablement, support, and guardrails per tier. Produces per-tier scope, exit criteria, and migration rules, not a blanket 'everyone gets Copilot' plan."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-01
  - RT-07
  - QA-01
difficulty: intermediate
tags:
  - ai-native-rollouts
  - adoption
  - change-management
  - tiers
  - enablement
updated: "2026-04-21"
related_prompts:
  - domain-engineering-workflows/ai-native-rollouts/airollout_ambient_code_review.md
  - domain-engineering-workflows/ai-native-rollouts/airollout_delegate_like_parallel_coworker.md
  - domain-engineering-workflows/ai-native-rollouts/airollout_bottleneck_migration_plan.md
  - domain-personal-development/prompts/identity/identity_engineering_manager_stance.md
---

# Design a Tiered AI-Adoption Rollout (Ignore / Use / Build With)

**Purpose:** Rollouts that treat every engineer the same fail: heavy users get underinvested enablement, reluctant users get bulldozed, and the team learns neither fast nor evenly. This prompt produces a tiered rollout design — Ignore / Use / Build With — with per-tier scope, enablement, guardrails, and the exit criteria that move people between tiers when the evidence supports it.

**When to use:**
- An org is rolling out AI tools to a 10–500-person engineering team and needs a defensible plan.
- A prior rollout stalled; the team wants to restart with a tier-aware design.
- A platform team is deciding what to invest in per audience slice.
- An EM is asked to "drive AI adoption" without specifics and needs a concrete plan.

**Don't use when:** Team size < 5. At that scale, tiering is overhead — handle individually.

**Audience:** EM, staff engineer, or AI-enablement lead. Output is a plan document to share with leadership and the affected team.

---

## Inputs Required

1. **Team shape.** Size, function mix (backend / frontend / mobile / data / SRE / security), seniority distribution.
2. **Current AI use.** How many people already use AI for work today, at what intensity, with what tools.
3. **Target AI tools.** Specific tools in scope (IDE copilots, PR review tools, agentic tools, internal wrappers).
4. **Business context.** What does leadership want from this rollout? (Throughput, quality, cost, retention, capability buildup?) If unstated, ask.
5. **Compliance posture.** What data can or can't go to which tools; any regulatory posture that affects tier design.
6. **Prior rollout history.** Has this team had a failed rollout? What failed?
7. **Budget.** Licenses, time, enablement hours available.

---

## Instructions

### Step 1 — Name the three tiers explicitly

Reject a two-tier framing. Force three:

- **Tier 0 — Ignore.** Engineers who, for this work, for now, don't need to use AI tools. They are not a failure; they are a valid state.
- **Tier 1 — Use.** Engineers who use AI tools daily for authoring, refactoring, review, and question-answering. They do not build on top of AI capabilities.
- **Tier 2 — Build With.** Engineers who build products, workflows, or internal systems that include AI as a load-bearing component (agentic tools, RAG systems, internal AI-augmented tools).

These are not skill levels; they are role-of-AI-in-work levels. Someone can be a principal engineer in Tier 0 and a junior in Tier 2.

### Step 2 — Assign population estimates with evidence

Per the team shape (input 1) and current use (input 2), propose a starting distribution. For each tier, name:

- Rough headcount.
- Identifying signals (e.g., "works in embedded firmware with no AI-safe data" → Tier 0).
- What evidence would move someone between tiers.

Do not set aspirational targets like "everyone Tier 2 in 12 months." Assign to current state; migration is separate.

### Step 3 — Define per-tier scope

Per tier, answer:

- **In-scope tools:** Which of the input 3 tools apply.
- **In-scope tasks:** What kinds of work the tier is expected to use AI for, and what kinds they explicitly aren't.
- **Out-of-scope tasks:** Work where the tier is expected NOT to use AI (e.g., Tier 1 doesn't author prod-affecting code without an explicit review; Tier 0 uses no tools for this work at all).

Scope is specific enough that a new engineer on the team can tell which tier they're in.

### Step 4 — Define per-tier enablement

Different tiers need different investment. Propose:

| Tier | Enablement |
|------|------------|
| Tier 0 | Briefing on tools available (so they can opt in later). No ongoing training. No dashboards. |
| Tier 1 | Hands-on onboarding (1–3 hrs). Shared prompt / workflow library. Monthly office hours. Opt-in pairing with a Tier 2 peer. |
| Tier 2 | Deeper training on the specific AI system they build on. Access to eval harnesses, traces, internal observability. Allotted build time or rotation. |

Customize per the team shape and budget. Avoid treating enablement as one workshop.

### Step 5 — Define per-tier guardrails

Risk rises by tier. Per tier, name:

- **Data handling.** What data can enter which tool. (Tier 0: N/A. Tier 1: per compliance posture. Tier 2: extra scrutiny for anything that becomes prompts in prod, retrieval corpuses, or eval sets.)
- **Code review posture.** Tier 1: AI-assisted code is still reviewed with the same rigor — often more (e.g., require tests for AI-generated changes). Tier 2: production AI systems require a distinct review path (see `ai_review_outcome_level_code_review.md`).
- **Accountability.** The engineer is accountable for AI-produced output. Tier 2 has additional accountability for runtime behavior of systems they build.

### Step 6 — Define migration rules between tiers

Not everyone moves, and not every move is up.

- **Tier 0 → Tier 1 trigger:** A concrete task in the engineer's work becomes unblocked by AI; they express interest; they allocate ≥ 1 hour/week for the first month.
- **Tier 1 → Tier 2 trigger:** There is a concrete internal AI-augmented system or workflow they would build that an internal audience needs. Not "I'm curious about agents."
- **Tier 2 → Tier 1 trigger:** The build project ends or moves to maintenance. Being Tier 2 is work-shaped, not prestige-shaped.
- **Tier 1 → Tier 0 trigger:** The engineer's work moves to a domain where AI tools are out-of-scope (compliance, classified, etc.) — or the tools genuinely don't help for this work and forcing them wastes time.

Migrations happen via an explicit conversation with a named owner, not by drift.

### Step 7 — Define success signals per tier

For each tier, define what "this rollout is working for this tier" looks like at month 3.

- Tier 0: No negative signal. Engineers are not forced, not shamed, not blocked.
- Tier 1: Daily use. Observable artifact changes (PR volume, review throughput, or self-reported unblocking).
- Tier 2: At least one shipped internal AI-augmented system / workflow with observable usage.

Tie signals to input 4 (what leadership wants).

### Step 8 — Phase the rollout

Three phases, each with exit criteria:

- **Phase 1 — Assign + Enable (weeks 1–4):** Tier assignments made, enablement delivered per tier. Exit criterion: every engineer knows their tier and has baseline tool access.
- **Phase 2 — Steady state (weeks 5–12):** Signals collected; guardrails exercised; small migrations happen. Exit criterion: per-tier success signals met for ≥ 60% of the assigned population.
- **Phase 3 — Review + Adjust (weeks 13–16):** Audit tier assignments, adjust scope/enablement, plan the next quarter. Exit criterion: written review delivered.

### Step 9 — Stop conditions

Catch failure before 16 weeks are wasted:

- **Tier 1 non-adoption:** If by week 8, < 40% of Tier 1 is using tools regularly, revisit either the enablement (likely insufficient) or the tier assignment (some Tier 1s should be Tier 0).
- **Tier 2 drift into demos:** If Tier 2 output is only demos with no internal users, that's not Build With — reclassify or end the Tier 2 allocation.
- **Compliance incident:** Any incident triggers a pause on the affected tier and tool; design a mitigation before resuming.

### Step 10 — Verify and output

Run the verification checklist.

---

## Constraints

### Must
- Use three tiers, not two.
- Assign tiers to current state, not aspirations.
- Define migration rules that can move people down as well as up.
- Tie success signals to what leadership actually wants.
- Phase the rollout with exit criteria.

### Must Not
- Treat Tier 0 as failure or a pre-Tier-1 stop.
- Claim "everyone Tier 2 in N months" as a goal. Tier 2 is work-shaped and has a ceiling.
- Push Tier 1 adoption with mandates that ignore the compliance posture.
- Make tier progression a performance-review dimension. It's not an accomplishment axis; it's a where-AI-fits axis.
- Confuse "using AI tools" with "being good at the underlying engineering work."
- Let enablement default to a single onboarding workshop.

---

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Size Tier 2 larger than the team can actually sustain. Building with AI has higher ongoing cost than using it.
- Treat AI-tool usage metrics as the goal. The goal is the business context in input 4; metrics are instrumentation.
- Assign tiers by seniority. Tiers are orthogonal to seniority.
- Apply a uniform guardrail across tiers. Tier 2 needs different review; Tier 1 needs tests-for-AI-changes at minimum.
- Skip migration-down rules. Without Tier 2 → Tier 1 and Tier 1 → Tier 0 paths, the plan calcifies.

✅ **DO:**
- Check that Tier 0 is not being used to hide a resistance problem. Resistance is Tier 0 only if the work genuinely doesn't benefit.
- Check that Tier 2 is not being used to cosplay. Tier 2 requires a real user / consumer.
- Design the shared artifact Tier 1s actually learn from (prompt library, PR showcases, a channel).
- Require Tier 2 to publish postmortems / lessons back to Tier 1 (this is how the org compounds).
- Write the plan so that a skeptical engineer in Tier 0 can say "that's fair" without feeling sidelined.

---

## Dual-Failure Prevention (QA-20)

❌ **HARMFUL failure:** Plan mandates Tier 1 universally, engineers paste confidential data into consumer tools, compliance incident ensues.

❌ **UNHELPFUL failure:** Plan is so cautious that no one is actually expected to use AI. The rollout is theater.

✅ **Quality check:** An engineer in each tier could read the plan and say "yes, this is what's expected of me, and the support is appropriate."

---

## Output Format

```markdown
# Tiered AI-Adoption Rollout — [Team]

## Tiers
### Tier 0 — Ignore
- Population estimate: [N; % of team]
- Identifying signals: [list]
- In-scope tools: —
- Out-of-scope tasks: —
- Enablement: [briefing only]
- Guardrails: [data handling baseline]

### Tier 1 — Use
- Population estimate: [N; %]
- Identifying signals: [list]
- In-scope tools: [list]
- In-scope tasks: [list]
- Out-of-scope tasks: [list]
- Enablement: [hours, format, ongoing]
- Guardrails: [review rigor, data handling]

### Tier 2 — Build With
- Population estimate: [N; %]
- Identifying signals: [list + named project(s)]
- In-scope tools: [list, including internal systems]
- In-scope tasks: [list]
- Out-of-scope tasks: [list]
- Enablement: [deeper training, eval access, build-time allocation]
- Guardrails: [extra review path, runtime accountability]

## Migration Rules
| Move | Trigger |
|------|---------|
| Tier 0 → Tier 1 | |
| Tier 1 → Tier 2 | |
| Tier 2 → Tier 1 | |
| Tier 1 → Tier 0 | |

## Success Signals at Month 3
| Tier | Signal tied to leadership goal (input 4) |
|------|-----------------------------------------|
| 0 | No negative signal |
| 1 | [specific metric] |
| 2 | [specific shipped artifact + usage] |

## Phases
| Phase | Weeks | Scope | Exit Criterion |
|-------|-------|-------|---------------|
| 1 | 1–4 | Assign + enable | |
| 2 | 5–12 | Steady state | |
| 3 | 13–16 | Review + adjust | |

## Stop Conditions
- Tier 1 non-adoption: [threshold + redirect]
- Tier 2 drift into demos: [check + redirect]
- Compliance incident: [pause + mitigation]

## Budget + Investment
- Licenses: [allocation across tiers]
- Enablement hours: [allocation]
- Tier 2 build time: [allocation]

## Open Questions
- [Decisions leadership still owns]
```

---

## Verification

- [ ] Three tiers, not two.
- [ ] Population estimates tied to evidence, not aspirations.
- [ ] Per-tier scope, enablement, guardrails defined.
- [ ] Migration rules in both directions.
- [ ] Success signals tied to leadership context (input 4).
- [ ] Phases with exit criteria.
- [ ] Stop conditions with thresholds and redirects.
- [ ] Tier 0 is treated as valid, not as failure.
- [ ] Tier 2 is sized realistically.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Output is a tiered rollout plan, not a generic adoption pitch.
- **ST-02 (Structured Sequential Instructions):** Ten steps from tier definition → assignment → scope → enablement → guardrails → migration → signals → phases → stops → verify.
- **CM-02 (Constraint Specification):** Must Not block forbids two-tier shortcuts and aspirational full-Tier-2 targets.
- **DS-01 (Framework Application):** Three-tier framework with migration rules is the spine.
- **RT-07 (Cascade Effect Analysis):** Forcing down-migration rules prevents the calcification cascade where nobody can ever step back.
- **QA-01 (Self-Verification):** Verification checklist forces honest tier sizing and leadership-goal alignment.
