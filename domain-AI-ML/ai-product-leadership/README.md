# AI Product & Leadership

The decisions made about ML work rather than inside it — which use cases to fund, what to build versus buy, how to structure the team, what to tell executives, and what to do after a project fails. Written for ML PMs, engineering leads, and decision-makers.

**12 prompts.** Part of [`domain-AI-ML/`](../README.md) — see the domain README for the lifecycle routing table and the [boundary with adjacent domains](../README.md#boundary-with-adjacent-domains).

## When to enter here

- Prioritizing or scoping AI work across a portfolio.
- Building the business case, or briefing executives on model risk.
- Choosing a vendor, structuring a team, or writing an AI policy.

**Not here:**
- The question is whether a specific problem needs ML at all — [`../problem-framing-scoping/mlframe_is_this_an_ml_problem.md`](../problem-framing-scoping/mlframe_is_this_an_ml_problem.md).
- The question is enterprise or board-level AI strategy → `domain-business-strategy/ai-strategy/`.
- You need a regulatory assessment rather than an executive summary of one → [`../responsible-ai-governance/`](../responsible-ai-governance/README.md).

## Prompts


**Choose the work**

| Prompt | Use it to |
|---|---|
| [`aipm_use_case_prioritization.md`](aipm_use_case_prioritization.md) | Rank candidate AI/ML use cases against value, feasibility, data readiness, and risk to produce a defensible, sequenced portfolio rather than a wishlist. |
| [`aipm_ml_project_scoping.md`](aipm_ml_project_scoping.md) | Turn a chosen ML idea into a delivery-ready scope: problem framing, measurable success criteria, data plan, milestones, and the risks that actually kill ML projects. |
| [`aipm_roi_business_case.md`](aipm_roi_business_case.md) | Build a defensible ROI / business case for an ML initiative using value ranges, scenarios, and labeled assumptions rather than fabricated precise figures. |
| [`aipm_build_buy_partner_decision.md`](aipm_build_buy_partner_decision.md) | Decide whether to build, buy, or partner for an AI capability by weighing cost, control, time-to-value, strategic differentiation, and risk from a leadership vantage. |
| [`aipm_vendor_model_selection.md`](aipm_vendor_model_selection.md) | Evaluate and select AI vendors or foundation models against weighted criteria — capability fit, cost, latency, data terms, lock-in, and viability — with a defensible scorecard. |

**Build the organization**

| Prompt | Use it to |
|---|---|
| [`aipm_ml_team_structure_hiring.md`](aipm_ml_team_structure_hiring.md) | Design an ML team structure and sequenced hiring plan matched to the organization's stage, mandate, and existing capability — avoiding both over-hiring and missing-role bottlenecks. |
| [`aipm_ai_roadmap_design.md`](aipm_ai_roadmap_design.md) | Design a phased AI roadmap aligned to business strategy and honest capability maturity, sequencing bets so each phase builds the foundations the next one needs. |
| [`aipm_mlops_maturity_for_leaders.md`](aipm_mlops_maturity_for_leaders.md) | Assess an organization's MLOps maturity across the model lifecycle and build the investment case to leadership in business terms — what breaks today and what each level of investment buys. |

**Govern and communicate**

| Prompt | Use it to |
|---|---|
| [`aipm_ai_policy_authoring.md`](aipm_ai_policy_authoring.md) | Author an internal AI use policy covering acceptable use, data handling, human review, and accountability — specific and enforceable rather than aspirational boilerplate. |
| [`aipm_model_risk_brief_for_execs.md`](aipm_model_risk_brief_for_execs.md) | Translate a model's technical risks and controls into a one-page executive brief that an accountable leader can read, question, and sign off on without an ML background. |
| [`aipm_jargon_translator_for_stakeholders.md`](aipm_jargon_translator_for_stakeholders.md) | Translate ML jargon, metrics, and tradeoffs into language matched to a specific stakeholder audience — preserving the real tradeoff while removing the technical noise. |

**Learn from failure**

| Prompt | Use it to |
|---|---|
| [`aipm_failed_ml_project_postmortem.md`](aipm_failed_ml_project_postmortem.md) | Run a blameless postmortem on a failed or stalled ML project, separating symptom from root cause and extracting systemic fixes that prevent the next failure. |

## Conventions

- **Prefix:** `aipm_` — one prefix per subdirectory, so a filename identifies its home.
- **Frontmatter:** the domain's eight fields — `title`, `category` (`AI-ML/ai-product-leadership`), `description`, `techniques` (validated against `techniques/MASTER_TECHNIQUE_INDEX.md`), `difficulty`, `tags`, `updated`, `related_prompts`.
- **Structure:** five H2 sections — `Inputs / Context`, `Constraints`, `Verification`, `False-Positive Prevention`, `Example Output` — with `Objective`, `When to Use`, `When NOT to Use`, `Instructions`, `Output Format`, `Techniques Used`, `Related Prompts` as bold labels inside them.
- **No fabrication:** no invented benchmark numbers, accuracy figures, SOTA claims, or dataset statistics. Quantities that would change a decision are marked for measurement or verification.
- **Framework-neutral:** the user names the stack; prompts avoid hardcoding APIs that drift.

## What lives elsewhere

- Cost attribution and forecasting as engineering artifacts → [`../mlops-infrastructure/mlops_cost_attribution_showback.md`](../mlops-infrastructure/mlops_cost_attribution_showback.md), [`mlops_cost_budget_forecasting.md`](../mlops-infrastructure/mlops_cost_budget_forecasting.md).
- The model inventory a leadership conversation usually needs → [`../production-monitoring/mlmonitor_model_portfolio_health_review.md`](../production-monitoring/mlmonitor_model_portfolio_health_review.md).
- Enterprise AI strategy, vendor switch cost, capability compounding → `domain-business-strategy/ai-strategy/`.
