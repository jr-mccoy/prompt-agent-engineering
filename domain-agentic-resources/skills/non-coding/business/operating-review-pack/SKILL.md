---
name: operating-review-pack
description: Build a concise operating review pack with KPIs, narrative, risks, and decision-ready recommendations.
tags:
  - operating-review
  - executive-reporting
  - kpi-dashboard
  - business-review
  - stakeholder-communication
updated: "2026-04-11"
---

# Operating Review Pack

Build structured operating review packs that give leadership a clear, decision-ready view of business performance with KPIs, narrative context, risks, and recommended actions.

## When to Use This Skill

- Preparing monthly or quarterly operating reviews for leadership
- Building board-level performance summaries
- Creating cross-functional business review decks
- Synthesizing department metrics into an executive narrative
- Preparing for QBR (Quarterly Business Review) meetings

## Core Concepts

### Leading vs Lagging Indicators

**Lagging indicators** measure outcomes that have already occurred (revenue, churn rate, NPS). **Leading indicators** predict future performance (pipeline velocity, feature adoption rate, support ticket trends). A strong review pack includes both.

### The SCR Framework (Situation-Complication-Resolution)

Structure narrative sections using SCR:
- **Situation**: Where we are (state the metric or context)
- **Complication**: What changed or what's at risk (the tension)
- **Resolution**: What we're doing about it (the action or recommendation)

### Traffic Light Status Model

| Color | Meaning | Criteria |
|-------|---------|----------|
| Green | On track | Metric within 5% of target |
| Yellow | At risk | Metric 5-15% off target, or trend deteriorating |
| Red | Off track | Metric >15% off target, or blocker identified |

Use consistently across all sections so executives can scan quickly.

## Workflow

### Phase 1: Define Scope and Audience

1. Identify the review cadence (weekly, monthly, quarterly)
2. Clarify the audience (CEO, board, department heads, cross-functional)
3. Determine the decision horizon — what decisions should this review enable?
4. List the 5-8 KPIs that matter most for this audience
5. Identify comparison periods (MoM, QoQ, YoY)

### Phase 2: Gather and Validate Metrics

1. Pull actuals for each KPI from source systems
2. Compare against targets, prior period, and prior year
3. Flag any data quality issues or caveats
4. Calculate derived metrics (growth rates, ratios, per-unit economics)
5. Validate with data owners before including

### Phase 3: Build the Narrative

For each major section (typically 3-5 business areas):
1. State the headline metric and its traffic light status
2. Provide 2-3 sentences of SCR context
3. Call out notable wins or concerns
4. Include a forward-looking signal (leading indicator or upcoming milestone)

### Phase 4: Risk and Escalation Register

1. List 3-5 top risks with likelihood and impact ratings
2. For each risk, state the mitigation plan and owner
3. Identify any items requiring a leadership decision
4. Flag resource requests or trade-off decisions needed

### Phase 5: Recommendations and Action Items

1. State 3-5 recommended actions with clear owners
2. Use RACI for accountability (Responsible, Accountable, Consulted, Informed)
3. Include timelines and success criteria
4. Link actions to specific KPIs they aim to improve

### Phase 6: Package and Review

1. Assemble into standard template with consistent formatting
2. Pre-read with key stakeholders for accuracy
3. Prepare talking points for live presentation

## Templates

### Executive Summary Template

```markdown
## Operating Review — [Period]

**Overall Status:** 🟢 / 🟡 / 🔴

### Headlines
- [Metric 1]: $X (+Y% vs target) 🟢
- [Metric 2]: $X (-Y% vs target) 🟡
- [Metric 3]: $X (-Y% vs target) 🔴

### Key Wins
1. [Win with quantified impact]
2. [Win with quantified impact]

### Key Risks
1. [Risk]: [Mitigation] — Owner: [Name]

### Decisions Needed
1. [Decision with options and recommendation]
```

### KPI Scorecard Row

```
| KPI | Target | Actual | Variance | Trend | Status | Owner |
|-----|--------|--------|----------|-------|--------|-------|
| Revenue | $1.2M | $1.15M | -4.2% | ↗ | 🟢 | VP Sales |
```

## Best Practices

- **Lead with the punchline**: Put overall status and key headlines first. Executives scan — don't bury insights.
- **One page per section maximum**: If a section needs more, the scope is too broad.
- **Quantify everything**: Replace "sales improved" with "sales grew 12% MoM to $1.4M."
- **Show trend, not just snapshot**: Include directional arrows. A metric at target but trending down is yellow, not green.
- **Separate fact from opinion**: Clearly label recommendations and interpretations vs. data.
- **Pre-wire controversial items**: Never surprise leadership in a review meeting.
- **Maintain a consistent template**: Repetition builds executive muscle memory.
- **Include "so what" for every metric**: A number without context is noise.

## Common Pitfalls

| Pitfall | Why It Happens | How to Avoid |
|---------|----------------|--------------|
| Data dump without narrative | Over-reliance on dashboards | Add SCR context to every section |
| Inconsistent status colors | No agreed-upon thresholds | Define green/yellow/red criteria upfront |
| Missing forward-looking signals | Focus on trailing data only | Include at least one leading indicator per section |
| Action items without owners | Rushed assembly | Require RACI for every recommendation |
| Stale comparisons | Using wrong baseline period | Align on comparison periods before gathering data |
| Sandbagging or spin | Political pressure on metrics | Report actuals honestly; add context, not excuses |

## Quality Checklist

- [ ] All KPIs have targets, actuals, variance, and trend
- [ ] Traffic light status applied consistently using defined thresholds
- [ ] Narrative uses SCR framework (not just data recitation)
- [ ] At least one leading indicator per business area
- [ ] Risk register includes likelihood, impact, mitigation, and owner
- [ ] Recommendations are specific, actionable, and owned
- [ ] Template is consistent with prior reviews
- [ ] Data validated with source owners
- [ ] No surprises — red items pre-socialized with stakeholders

## Examples

### Example: Monthly SaaS Operating Review

**Audience:** CEO + VP-level leadership | **Cadence:** Monthly

| Section | Content | Pages |
|---------|---------|-------|
| Executive Summary | Overall status, 3 headlines, 1 decision | 1 |
| Revenue & Growth | ARR, MRR growth, expansion, churn | 1 |
| Product & Engineering | Velocity, uptime, feature adoption | 1 |
| Customer Success | NPS, retention, time-to-value | 1 |
| People & Operations | Headcount, hiring, engagement | 1 |
| Risk Register | Top 5 risks with mitigations | 1 |
| Actions & Decisions | 5 actions with RACI, 2 decisions | 1 |

**Total:** 7 pages, 30-minute presentation, 15-minute discussion
