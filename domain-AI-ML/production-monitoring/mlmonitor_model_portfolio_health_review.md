---
title: "Model Portfolio Health Review"
category: AI-ML/production-monitoring
description: "Review every model an organization runs as a portfolio — finding the unowned, unmonitored, and quietly degrading ones, ranking by consequence rather than by attention received, and producing retirement decisions alongside remediation."
techniques:
  - RT-02
  - DS-06
  - CM-02
  - QA-12
  - DS-02
difficulty: intermediate
tags:
  - model-inventory
  - portfolio-review
  - model-ownership
  - retirement
  - monitoring-coverage
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/production-monitoring/mlmonitor_champion_challenger_design.md
  - domain-AI-ML/responsible-ai-governance/rai_model_risk_register.md
  - domain-AI-ML/mlops-infrastructure/mlops_model_registry_design.md
  - domain-AI-ML/ai-product-leadership/aipm_mlops_maturity_for_leaders.md
---

# Model Portfolio Health Review

**Objective:** Look at every model the organization runs as one portfolio rather than as a set of individual projects — surfacing the ones nobody owns, nothing monitors, and no one has evaluated since launch, ranking them by what a failure would cost rather than by how much attention they get, and producing retirement decisions as a first-class outcome.

**When to Use:**
- Nobody can say how many models are in production, which is the usual state past a certain scale.
- A model failure surprised the organization, and the question is what else looks like that.
- Periodically — quarterly or half-yearly — as portfolio hygiene.
- Before a governance, audit, or customer-security review asks for an inventory.

**When NOT to Use:**
- One model needs deep diagnosis — use `mlmonitor_performance_degradation_triage.md`.
- You need a regulatory risk register rather than an operational review — use `../responsible-ai-governance/rai_model_risk_register.md`, which this can feed.
- Fewer than a handful of models exist and all are actively owned.

## Inputs / Context

- **Model inventory** — every model serving predictions, including ones outside the main platform.
- **Ownership records** — named individual or team per model, and whether that person still holds the role.
- **Monitoring coverage** — what is monitored per model, and whether alerts route to someone who acts.
- **Last evaluation date** — when each model's performance was last measured against fresh labels.
- **Consumption** — what depends on each model's output, and what happens if it is wrong or unavailable.
- **Cost** — inference and maintenance cost per model.

## Constraints

**Must:**
- Find models **outside the registry** — in notebooks, scheduled jobs, embedded in services, or in a business unit's own tooling. The unregistered ones carry the most risk because nothing watches them.
- Rank by **consequence of failure**, not by traffic volume or attention; a low-traffic model gating a compliance decision outranks a high-traffic recommendation carousel.
- Treat "no named owner" and "no monitoring" as findings in their own right, independent of whether the model is currently performing.
- Include **retirement** as a first-class outcome — a model whose consumer is gone should be turned off, and this review is where that decision gets made.
- Distinguish "not monitored" from "monitored but nobody responds"; the second is more dangerous because it looks covered on a dashboard.

**Must Not:**
- Assert benchmark ratios, industry norms, or typical portfolio sizes from memory; this is an inventory of your own estate.
- Treat absence of incidents as evidence of health — an unmonitored model produces no incidents by construction, which is the point.
- Rank by recency of attention; the models people talk about are usually the ones already being looked after.
- Close the review without an owner assigned to every model, or a retirement decision recorded.
- Report a model as monitored because a dashboard exists; check that an alert exists and that it reaches someone who acts.

**Instructions:**

1. **Build the true inventory.** Start from the registry, then actively search elsewhere: scheduled jobs, service code paths calling a model, notebooks on a schedule, and business-unit tooling. Ask each team what they run rather than relying on a central list. Expect the inventory to grow, and record how many were found outside the registry — that number is itself the most informative finding about platform maturity.

2. **Establish real ownership.** Named individual and team per model. Verify the person still holds the role and knows they own it; an owner who has left or does not know is not an owner. Record models where ownership is genuinely absent.

3. **Assess monitoring coverage per model.** Three levels: **not monitored**; **monitored without response** (metrics exist, alerts fire into an unwatched channel or do not exist); **monitored with response** (alerts route to the owner and are acted on). The middle category is the dangerous one because it presents as covered.

4. **Record last evaluation against fresh labels.** Not last deployment or last retrain — last time someone measured performance on recent labelled data. Long gaps here are where silent degradation lives.

5. **Score consequence of failure.** For each model: what depends on it, what happens if the output is wrong, and what happens if it is unavailable. Regulatory exposure, customer impact, financial exposure, and safety, as applicable. This score, not traffic, sets priority.

6. **Rank into a work order.** Consequence × (ownership gap + monitoring gap + evaluation staleness). The top of this list is the portfolio's actual risk, and it usually contains models nobody had been discussing.

7. **Identify retirement candidates.** Models whose consumer is gone, whose output nobody reads, that are superseded, or whose cost exceeds their value. Retiring a model removes risk and cost permanently and is often the highest-value action available in this review.

8. **Assign remediation with owners and dates.** For each finding: the action, a named owner, and a date. Findings without owners recur at the next review unchanged.

9. **Record the portfolio metrics.** Total models, unregistered fraction, unowned count, unmonitored count, median evaluation staleness, retirement count. Tracking these across reviews shows whether the estate is getting healthier or merely larger.

**Output Format:**

A markdown review:
- **Inventory** — table: Model | Location | Registered? | Owner | Monitoring level | Last evaluated | Consumers.
- **Discovery Summary** — how many found outside the registry, and where.
- **Ownership Gaps** — models with no real owner.
- **Monitoring Gaps** — split into not-monitored and monitored-without-response.
- **Evaluation Staleness** — distribution and the worst cases.
- **Consequence Ranking** — table: Model | Consequence | Gap score | Priority.
- **Retirement Candidates** — model, reason, and the saving.
- **Remediation Plan** — finding, action, owner, date.
- **Portfolio Metrics** — this review versus the last.
- **INSUFFICIENT EVIDENCE** — the honest state of the inventory when discovery ran only against the registry. The models that cause portfolio incidents are by definition the ones not in it, so a registry-derived inventory cannot support a completeness claim. Name the unblocking datum: a sweep of serving infrastructure and code search independent of the registry.

## Verification

- [ ] The inventory includes an active search beyond the registry, and the unregistered count is reported.
- [ ] Every model has a verified owner, or is listed as an ownership gap.
- [ ] Monitoring is classified into three levels, separating monitored-without-response.
- [ ] Last evaluation against fresh labels is recorded, distinct from last deployment.
- [ ] Ranking is by consequence of failure, not traffic or attention.
- [ ] Retirement candidates are identified with their saving.
- [ ] Every finding has a named owner and a date.
- [ ] Portfolio metrics are recorded and compared with the previous review.
- [ ] Absence of incidents is not treated as evidence of health.
- [ ] Inventory completeness is marked INSUFFICIENT EVIDENCE unless discovery ran independently of the registry, with that sweep named.

## False-Positive Prevention

❌ **DON'T:**
- Treat the model registry as the inventory — the models that carry the most risk are precisely the ones nobody registered.
- Read "no incidents in 18 months" as health for an unmonitored model; nothing was watching, so there was nothing to report.
- Rank by traffic volume — a low-volume model that gates an eligibility or compliance decision outranks a high-volume ranking widget on every axis that matters.
- Count a model as monitored because a dashboard exists; check that an alert exists, that it fires, and that someone acts on it.
- Accept a departed employee or a dissolved team as the owner of record.
- Close the review with findings but no owners; those findings will be identical at the next review.

✅ **DO:**
- Search actively outside the registry and report what you find there as a maturity signal.
- Verify ownership with the named person rather than reading a field.
- Separate monitored-without-response as its own category, because it is the one that looks safe.
- Record last evaluation against fresh labels, not last deploy.
- Rank by what a failure costs, and expect the top of the list to be unfamiliar.
- Push retirement hard — it is the only action that removes risk and cost permanently.

## Example Output

```markdown
## Model Portfolio Health Review — Q3

### Discovery Summary
Registry listed 14 models. Active search found **23**.
| Found where | Count |
|---|---|
| Model registry | 14 |
| Scheduled jobs calling a pickled model directly | 4 |
| Embedded in a service, no registry entry | 3 |
| Business-unit notebook on a schedule | 2 |

**9 of 23 models (39%) were outside the registry.** That ratio is the review's headline finding
about platform maturity — more informative than any individual model's status.

### Inventory (extract)
| Model | Location | Registered | Owner | Monitoring | Last evaluated | Consumers |
|---|---|---|---|---|---|---|
| Fraud scoring v7 | platform | ✅ | Risk ML team | **with response** | 2 weeks | review queue |
| Churn score | platform | ✅ | *vacant — owner left* | **without response** | 8 months | CRM, campaigns |
| Lead scoring | BU notebook | ❌ | Sales ops (unaware) | **none** | never since launch | sales routing |
| Credit pre-check | service, embedded | ❌ | Eng team (unaware) | **none** | 14 months | **eligibility gate** |
| Doc classifier | platform | ✅ | Platform ML | with response | 3 weeks | routing |
| Price elasticity | scheduled job | ❌ | *none* | none | 22 months | pricing dashboard |

### Ownership Gaps
- **Churn score** — owner left the company 5 months ago; no reassignment.
- **Price elasticity** — no owner has ever been recorded.
- **Lead scoring**, **Credit pre-check** — nominal teams exist but neither knew they owned a model.

### Monitoring Gaps
**Not monitored (4):** lead scoring, credit pre-check, price elasticity, and one embedded model.
**Monitored without response (3):** churn score and two others — metrics are collected and alerts
fire into a channel nobody has read since the team reorganized. These present as green on the
platform dashboard, which is why they are called out separately from the unmonitored group.

### Evaluation Staleness
Median 4 months. Worst: price elasticity at 22 months, credit pre-check at 14 months. Two models
have never been evaluated against fresh labels since launch.

### Consequence Ranking
| Rank | Model | Consequence of failure | Gap score | Priority |
|---|---|---|---|---|
| 1 | **Credit pre-check** | **eligibility decisions** — regulatory and customer harm | unregistered + unowned-in-practice + unmonitored + 14 months stale | **Critical** |
| 2 | Churn score | wasted campaign spend; customer annoyance | unowned + monitored-without-response + 8 months stale | High |
| 3 | Price elasticity | pricing decisions from a 22-month-stale model | unowned + unmonitored + never evaluated | High |
| 4 | Lead scoring | misrouted leads | unowned-in-practice + unmonitored | Medium |
| … | Fraud scoring v7 | high consequence, **but fully owned, monitored, current** | none | Healthy |

The credit pre-check model tops the list and had never been discussed in any ML forum — it was
embedded in a service years ago and has been making eligibility decisions unwatched since. It has
low traffic, which is exactly why volume-based ranking would have buried it.

### Retirement Candidates
| Model | Reason | Saving |
|---|---|---|
| Price elasticity | dashboard it feeds was decommissioned last year; **nobody reads the output** | removes an unowned, unmonitored, stale model entirely |
| Doc classifier v3 (superseded) | v5 serves all traffic; v3 still running | inference cost + one fewer artifact to govern |

Retiring price elasticity resolves a High-priority finding permanently rather than remediating it.

### Remediation Plan
| Finding | Action | Owner | Date |
|---|---|---|---|
| Credit pre-check unowned/unmonitored | assign owner, register, add monitoring + alerting, evaluate on fresh labels | Eng lead + Platform ML | 2 weeks |
| Churn score owner vacant | reassign; redirect alerts to a watched channel | Marketing Data lead | 3 weeks |
| Price elasticity | **retire** | Platform ML | 4 weeks |
| Alerts into unwatched channels | audit all alert routing across the portfolio | Platform ML | 4 weeks |
| 9 unregistered models | register all; add a registration gate to the deploy path | Platform ML | 6 weeks |

### Portfolio Metrics
| Metric | This review | Last review |
|---|---|---|
| Total models | 23 | `[prior]` |
| Unregistered | 9 (39%) | `[prior]` |
| No real owner | 4 | `[prior]` |
| Unmonitored | 4 | `[prior]` |
| Monitored without response | 3 | `[prior]` |
| Median evaluation staleness | 4 months | `[prior]` |
| Retired this cycle | 2 | `[prior]` |
```

**Techniques Used:**
- **RT-02 (Multi-Dimensional Analysis Framework):** model × ownership × monitoring × staleness × consequence is the review grid.
- **DS-06 (Prioritization and Severity Guidance):** consequence-based ranking surfaces the models nobody was discussing.
- **CM-02 (Constraint Specification):** the search-beyond-the-registry and owner-with-a-date rules bound what counts as a completed review.
- **QA-12 (False Positives Identification):** separates monitored-without-response from monitored, and rejects absence of incidents as evidence.
- **DS-02 (Metric Specification):** portfolio metrics are defined so successive reviews are comparable.

**Related Prompts:**
- `mlmonitor_champion_challenger_design.md` — for models where continuous replacement is warranted.
- `../responsible-ai-governance/rai_model_risk_register.md` — the governance register this review feeds.
- `../mlops-infrastructure/mlops_model_registry_design.md` — the registration gate that prevents the unregistered problem recurring.
- `../ai-product-leadership/aipm_mlops_maturity_for_leaders.md` — translating these portfolio metrics for a leadership audience.
