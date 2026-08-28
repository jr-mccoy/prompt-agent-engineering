# AI Strategy & Context Accumulation

Prompts for making defensible organizational AI strategy decisions: where context actually accumulates, what it would cost to switch vendors, which capabilities compound vs stay flat, and how to frame a platform decision for a board or executive team.

**Audience:** Strategy team, CTO, CIO, enterprise architect, chief of staff to the CEO. These prompts require visibility across multiple teams and tools — they are not individual-user exercises.

**Scope:** This cluster is about **strategy framing and analysis**, not implementation. It produces briefs, maps, and estimates that feed into a decision — not the decision itself, and not the rollout plan.

---

## Prompts

| Prompt | One-liner |
|--------|-----------|
| [aistrategy_context_accumulation_map.md](aistrategy_context_accumulation_map.md) | Audit where organizational understanding lives across tools, docs, and people — and where AI can and can't reach it. |
| [aistrategy_vendor_switch_cost.md](aistrategy_vendor_switch_cost.md) | Estimate the cost of switching AI model vendors at a future date, broken into five buckets with ranges. |
| [aistrategy_capability_compounding_evaluation.md](aistrategy_capability_compounding_evaluation.md) | Evaluate whether a specific AI capability compounds over time or stays flat, and what investment would change that. |
| [aistrategy_platform_brief.md](aistrategy_platform_brief.md) | Produce a board-ready brief on an enterprise AI platform decision: options, trade-offs, recommendation, invalidation conditions. |

---

## Suggested sequence for a platform decision

1. **`aistrategy_context_accumulation_map.md`** — map where context lives today. This shapes option design later.
2. **`aistrategy_capability_compounding_evaluation.md`** — run for the top 2–3 capabilities the platform would enable. Separates strategic bets from commodity utilities.
3. **`aistrategy_vendor_switch_cost.md`** — estimate for the leading candidate vendors. This is the quantitative input to the lock-in dimension of the platform brief.
4. **`aistrategy_platform_brief.md`** — synthesize into an executive-ready brief with recommendation and invalidation conditions.

Running the brief first without the upstream analyses produces generic AI-strategy writing. Running the upstream analyses without the brief produces interesting artifacts that never land.

---

## Relationship to adjacent clusters

- **[ambition-leverage/](../ambition-leverage/)** — once AI strategy is framed, ambition-leverage prompts turn that into organizational moves (expansion vs savings, domain-expert-as-builder, workflow compression).
- **[domain-software-engineering/analysis/business/](../../domain-software-engineering/analysis/business/)** — traditional business-model, financial, and competitive analyses. AI strategy usually needs to plug into these, not replace them.
- **[domain-productivity/operating-cadence/](../../domain-productivity/operating-cadence/)** — operationalizes decisions from AI strategy into the user's personal working cadence.
