---
title: "Vendor Evaluation for Purchase Decision"
category: business-strategy/research
description: "Deeply evaluate a single vendor/product against a specific situation and produce a source-cited decision document — fit, true total cost, feature-by-requirement evidence, integration and risk assessment, and a clear Buy/Don't Buy/Investigate recommendation."
techniques:
  - ST-01
  - RT-02
  - DS-02
  - RT-05
  - DS-06
difficulty: advanced
tags:
  - research
  - vendor-evaluation
  - procurement
  - decision-support
  - web-research
updated: "2026-06-07"
related_prompts:
  - domain-business-strategy/research/research_tool_comparison.md
  - domain-business-strategy/research/research_company_deep_dive.md
  - domain-business-strategy/research/research_competitive_landscape.md
---

# Vendor Evaluation for Purchase Decision

**Objective:** Evaluate a single vendor/product against a specific situation and produce a source-cited decision document — fit assessment, true total cost for the buyer's scale, feature-by-requirement evidence, integration and risk assessment, and a clear Buy / Don't Buy / Needs More Investigation recommendation.

**When to use:**
- Final vendor selection or procurement decisions.
- Contract renewals where you're re-justifying the spend.
- Build-vs-buy analysis for a specific candidate product.

**When NOT to use:**
- You're still shortlisting among several tools — use the tool comparison prompt first.
- The decision needs legal/security sign-off you can't source publicly — route those to the right owners.
- Requirements and scale aren't defined (fit and cost can't be assessed honestly).

**Audience:** Buyers, procurement, IT/ops leads, and decision-makers committing to a vendor.

---

## Inputs / Context

The user should supply (or the evaluation should flag what is missing):

1. **Vendor/product name** and the **buyer's situation** (team size, requirements, constraints).
2. **Scale** for pricing (seats, data volume, usage).
3. **Key requirements** (the must-haves to evaluate against) and **key tools** to integrate with.
4. **Current solution** being compared against (to assess what's gained/lost).
5. **Available sources** (official docs/pricing, G2/Capterra/TrustRadius, forums, case studies, security/compliance docs).

---

## Constraints

### Must
- Assess **fit against the buyer's stated requirements**, requirement by requirement, with evidence (doc/review link) per claim.
- Compute **true total cost for the buyer's exact scale**, including add-ons, overages, implementation/training, and year-1 vs. year-2 — all from official pricing/docs.
- Back **user-experience claims with quoted, linked reviews**, weighting feedback from similar companies; distinguish marketing claims from verified experience.
- **Never invent** prices, features, quotes, or sources; if a feature is "coming soon," do **not** count it as available.
- Assess **risks** (vendor stability, lock-in, implementation complexity, reliability) with sourced signals.
- End with a **clear recommendation** (Buy / Don't Buy / Needs More Investigation), the factors driving it, and what would change it; note the research date.

### Must Not
- Use generic "starting at" pricing in place of the buyer's actual cost.
- Count roadmap/"coming soon" features as present.
- Present case studies (vendor marketing) as neutral evidence.
- Give a recommendation without grounding it in the sourced evidence above.

---

## Instructions

1. **Restate the situation.** Vendor, buyer context, scale, key requirements, current solution.
2. **Fit assessment.** How well it matches requirements, what workflow changes adoption demands, and gains vs. the current solution.
3. **Pricing analysis.** Exact cost for the scale; what's included vs. extra; annual vs. monthly; hidden costs; year-1 and year-2 totals — sourced.
4. **Feature deep dive.** For each key requirement: how the product addresses it, limitations/caveats, and an evidence link. Exclude "coming soon."
5. **Integration assessment.** Native/Zapier/API/none for each key tool; known integration issues from reviews.
6. **User-experience evidence.** What users praise and complain about (quoted, linked), prioritizing similar companies.
7. **Risk factors.** Vendor stability, lock-in, implementation complexity, reliability — sourced; inference labeled.
8. **Recommendation + verification step.** Buy/Don't Buy/Investigate with driving factors and change-conditions. Then re-read: is every price/feature/quote sourced? Any "coming soon" counted as present? Is the recommendation traceable to the evidence? Note the research date.

---

## False-Positive Prevention

❌ **DON'T:**
- Quote a generic starting price as the buyer's cost.
- Count a roadmap feature as currently available.
- Treat a vendor case study as independent proof of fit.
- State a feature exists without a doc/review link.
- Recommend Buy/Don't Buy on vibes rather than the sourced findings.

✅ **DO:**
- Compute the true total cost for the exact scale, including hidden costs, from official sources.
- Verify each requirement against documentation; mark "coming soon" as not available.
- Quote real, linked reviews, weighting similar companies, and separate marketing from experience.
- Source every risk signal and label inference.
- Tie the recommendation explicitly to the evidence and state what would change it.

---

## Output Format

```
# Vendor Evaluation: [Vendor/Product] — for [Buyer Situation]
*Scale: [...] | Current solution: [...] | Research date: [...]*

## Fit Assessment
- Requirement match: [...]
- Workflow changes needed: [...]
- Gains vs. current solution: [...]

## Pricing Analysis (for [scale])
- Cost at our scale: [...] — [pricing source]
- Included vs. extra: [...]
- Annual vs. monthly: [...]
- Hidden costs (implementation, training, add-ons, overages): [...]
- Year-1 total / Year-2 total: [...]

## Feature Deep Dive
| Requirement | How addressed | Limitations | Evidence (link) |
|-------------|---------------|-------------|-----------------|
| ...         | ...           | ...         | ...             |
(Exclude "coming soon" features; note them separately.)

## Integration Assessment
- [Tool]: Native / Zapier / API / None — [source]; known issues: [...]

## User Experience Evidence
- Praise: "[quote]" — [source]
- Complaints: "[quote]" — [source]
- From companies like ours: [...]

## Risk Factors
- Vendor stability / lock-in / implementation / reliability: [...] — [source]; (inference noted)

## Recommendation
- [Buy / Don't Buy / Needs More Investigation]
- Driving factors: [...]
- What would change this: [...]
```

---

## Example Output

```
# Vendor Evaluation: ToolB (placeholder) — for a 5-person ops team
*Scale: 5 users, 10k records, must integrate with Slack | Current solution: spreadsheets | Research date: 2026-06-07*

## Fit Assessment
- Requirement match: covers 4 of 5 must-haves; lacks native bulk import.
- Workflow changes: team must move from ad-hoc sheets to structured records.
- Gains vs. current: automation and audit trail spreadsheets can't provide.

## Pricing Analysis (for 5 users, 10k records)
- Cost at our scale: $20/user/mo × 5 = $100/mo; 10k records within base — [toolb.example/pricing, 2026-06].
- Included vs. extra: advanced reporting is a paid add-on (+$15/mo) — [pricing page].
- Annual vs. monthly: ~15% discount annual — [pricing page].
- Hidden costs: ~4 hrs onboarding (self-serve, no paid implementation tier) — [docs].
- Year-1 total: ~$1,380 (annual + reporting add-on); Year-2 total: ~$1,380 (no intro pricing found).

## Feature Deep Dive
| Requirement | How addressed | Limitations | Evidence |
|-------------|---------------|-------------|----------|
| Automation | Visual rule builder | steep learning curve | [docs]; [G2 review, 2026-04] |
| Slack alerts | Native integration | none noted | [docs] |
| Bulk import | CSV import only | no API bulk import (NOT "coming soon" — confirmed absent) | [docs] |
| Reporting | Add-on module | extra cost | [pricing page] |
| Audit trail | Built-in | retention capped at 90 days on this tier | [docs] |

## Integration Assessment
- Slack: Native — [docs]; no major issues in recent reviews.

## User Experience Evidence
- Praise: "[verbatim quote on automation power]" — [G2, 2026-03].
- Complaints: "[verbatim quote on onboarding difficulty]" — [Capterra, 2026-02].
- From companies like ours (small ops teams): mixed on learning curve; positive once set up.

## Risk Factors
- Vendor stability: Series A, growing headcount per LinkedIn — [LinkedIn, 2026-06] (inference: reasonably stable, not a market leader).
- Lock-in: full CSV export available — [docs] (low lock-in).
- Implementation: moderate; learning curve is the main cost (inference from reviews).

## Recommendation
- Needs More Investigation → likely Buy.
- Driving factors: strong fit + low lock-in + acceptable cost; concern is onboarding effort and the audit-retention cap.
- What would change this: a free trial confirming the team can absorb the learning curve in <1 week; clarity on whether audit retention can be extended.
```

---

## Verification

- [ ] Fit assessed requirement by requirement with evidence links.
- [ ] Total cost computed for the exact scale, including hidden/year-2 costs, from official sources.
- [ ] "Coming soon" features excluded from available capabilities.
- [ ] User-experience claims quoted and linked, weighting similar companies.
- [ ] No invented prices, features, quotes, or sources.
- [ ] Risks sourced; inference labeled.
- [ ] Recommendation is explicit and traceable to the evidence; change-conditions and research date stated.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the task as a sourced, decision-ready single-vendor evaluation.
- **RT-02 (Multi-Dimensional Analysis Framework):** Evaluates fit, cost, features, integration, experience, and risk.
- **DS-02 (Evidence-Based Decision Making):** Requires sourced pricing/features/quotes and forbids fabrication or roadmap-counting.
- **RT-05 (Evidence-Based Reasoning):** The Buy/Don't Buy recommendation follows explicitly from the sourced findings.
- **DS-06 (Prioritization and Severity Guidance):** Weights risks and decision factors to produce a clear, conditioned recommendation.

---

## Related Prompts

- `domain-business-strategy/research/research_tool_comparison.md` — Shortlist among several tools before this deep evaluation.
- `domain-business-strategy/research/research_company_deep_dive.md` — Assess the vendor's company stability behind the product.
- `domain-business-strategy/research/research_competitive_landscape.md` — Understand the vendor's market and alternatives.
