# Solo Developer Operations

Prompts for the operational reality of running a software product alone: deciding what to automate, preventing and recovering from burnout, reducing context-switching across all the "hats" you wear, building a network without losing build time, figuring out which skill gap is actually holding the business back, pricing with confidence, deciding well without a team to bounce off, holding yourself accountable when no one is watching, designing a pace that lasts, and countering the motivation drain of working alone. Written for a solo founder, indie hacker, or freelancer who is simultaneously the engineer, support rep, marketer, and CEO.

## When to use these

Use this subfolder when:

- You're a one-person operation and the breadth of responsibilities is the problem, not any single task.
- You're spending too much time on repetitive non-build work.
- You're exhausted, dreading the laptop, or running flat-out with no end time.
- You feel scattered — constantly interrupted, switching between coding and support and marketing.
- You're isolated and want a network without it eating your week.
- You don't know what to learn next, or whether to learn / outsource / automate a responsibility.

**Not the right subfolder when:**

- You work on a team with assigned roles — most of these assume *you* wear every hat.
- The problem is execution stuckness on a specific project, not operational load → see the `../agency/` cluster.
- You need clinical mental-health support (the burnout prompt is wellbeing/risk-management, not therapy) → see a professional, or `domain-psychology/`.
- You want general (non-dev) productivity tooling → see `domain-productivity/`.

## Prompts in this subfolder

| Prompt | One-line description |
|---|---|
| `solo_dev_automation_audit.md` | Inventory recurring tasks, calculate automation ROI (setup vs. ongoing savings), and produce a phased, prioritized automation plan with tool recommendations. |
| `solo_dev_burnout_prevention.md` | Detect, prevent, and recover from burnout — assessment, "stop doing" list, sustainable-pace definition, boundaries, and a recovery protocol. |
| `solo_dev_context_switching_reducer.md` | Audit task switches, batch activities by cognitive mode, set notification boundaries, and design a deep-work-protecting weekly schedule. |
| `solo_dev_network_building.md` | Build a bounded professional network (communities, mentorship, accountability, open source) without taking excessive time from the product. |
| `solo_dev_skill_gap_assessment.md` | Rate skills across all solo-dev domains, identify the single highest-impact gap for your business stage, and decide learn / outsource / automate. |
| `solo_dev_pricing_value_confidence.md` | Separate the value-anchored part of your price from the fear-set part, then set one defensible number backed by delivered-value evidence and a pre-committed raise trigger. |
| `solo_dev_deciding_alone.md` | Stress-test a consequential decision with no team by convening a synthetic adversarial "board," writing the counter-case, and converging on one call plus its reversal condition. |
| `solo_dev_accountability_system.md` | Read the lever that actually moves you (from what you never break), then design one matched external accountability system — commitment, witness, stake, cadence — with a kill condition. |
| `solo_dev_sustainable_pace_design.md` | Proactively design a repeatable weekly operating cadence — load ceiling, scheduled recovery, throughput rhythm, bounded-crunch rule — so output survives past the sprint (distinct from burnout triage). |
| `solo_dev_isolation_motivation.md` | Diagnose which isolation deficit (no witnesses / no feedback / invisible progress) is draining your motivation, then engineer the minimal matching structure into the coming week. |

## How the prompts relate

These form a small operating system for the solo developer; common compositions:

- **Workload is unsustainable:** `solo_dev_burnout_prevention.md` first → its "stop doing" list points to `solo_dev_automation_audit.md` (eliminate tasks) and `solo_dev_context_switching_reducer.md` (batch what remains).
- **Feeling scattered, velocity dropping:** `solo_dev_context_switching_reducer.md` → `solo_dev_automation_audit.md` for the tasks worth removing entirely.
- **Deciding what to get better at:** `solo_dev_skill_gap_assessment.md` → if the answer is "automate," go to `solo_dev_automation_audit.md`; if "learn with help," go to `solo_dev_network_building.md` and `../goals/goals_skill_breakdown_blueprint.md`.
- **Isolation:** `solo_dev_isolation_motivation.md` diagnoses *which* isolation deficit is draining motivation (witnesses / feedback / visible progress); if the fix is a deeper social gap, escalate to `solo_dev_network_building.md`. Isolation is also a common burnout-prevention remedy.
- **Pace that keeps crashing:** if you're already exhausted, `solo_dev_burnout_prevention.md` first (triage); once stable, `solo_dev_sustainable_pace_design.md` locks in a repeatable weekly cadence so it doesn't recur.
- **Undercharging / freezing on price:** `solo_dev_pricing_value_confidence.md`; where a low price is genuinely a nerve rather than a strategy, it pairs with `../resilience/resilience_motivation_diagnosis.md` and `../identity/identity_confidence_calibration.md`.
- **A hard call with no one to ask:** `solo_dev_deciding_alone.md` builds a synthetic board and a reversal condition; pair with `../../domain-decision-making/tradeoff_reversibility_stakes_grid.md` for the stakes triage.
- **Breaking promises to yourself:** `solo_dev_accountability_system.md` designs one matched external system; it often instantiates the commitments produced by `../agency/agency_ship_sprint_design.md` or `solo_dev_sustainable_pace_design.md`.

## solo-dev/ vs. the agency/ cluster

Both subfolders serve a solo operator, but they cut the problem differently — use whichever matches your situation:

- **`solo-dev/` is about operational *load and breadth*** — the many-hats problem of running a product business alone (automation, burnout, switching, network, skill spread). Reach here when the issue is "too much surface area / unsustainable pace."
- **`../agency/` is about *execution on a specific project*** — moving a vague goal to a shipped artifact, diagnosing stuckness, shipping on a schedule, repairing habits. Reach there when the issue is "I'm not moving this one thing forward."

They cross-link rather than overlap: `solo_dev_burnout_prevention.md` ↔ `../agency/agency_burnout_recovery.md` (solo-dev-specific vs. general burnout), and `solo_dev_skill_gap_assessment.md` ↔ `../agency/agency_skill_gap_reframe.md` (which gap to close vs. whether the gap is real or avoidance).

## Shared design principles

- **One person wears every hat.** Recommendations assume no team to delegate to; "outsource" is a deliberate, priced choice.
- **Bounded time.** Plans state realistic weekly hour budgets; nothing assumes unlimited time.
- **Remove before you add.** Automation and "stop doing" come before new activities or new tools.
- **Free-first tooling.** Free and low-cost options lead; paid spend is justified, not assumed.
- **No fabricated numbers.** Time estimates, ROI figures, switch counts, and skill ratings come from the user or are labeled estimates to verify.
- **Survival framing.** For a solo dev, sustainability and automation are risk management, not self-indulgence.

## Related domains in this repo

- `domain-personal-development/prompts/agency/` — project-level execution and stuckness (see the comparison above).
- `domain-productivity/deep-work/` — team-level focus norms, meeting reduction, calendar audits.
- `domain-productivity/` — general (non-dev) automation, energy, and review prompts.
- `domain-personal-development/prompts/goals/` — skill-breakdown and goal-system design downstream of a skill-gap call.
- `domain-personal-development/career-transformation/` — residual-skills inventory feeding what you can teach/share when networking.
