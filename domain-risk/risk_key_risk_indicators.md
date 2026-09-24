---
title: "Key Risk Indicators — Measures That Move Before the Loss, With Thresholds Someone Acts On"
category: risk/monitoring
description: "Design key risk indicators for the top risks in a register: trace each risk to a causal driver, pick a leading indicator where one exists and label lagging ones honestly, define the formula, source and frequency, set green/amber/red thresholds from appetite or history, name an owner and the action each band forces, back-test against past incidents, and list how each KRI could be gamed; distinct from `domain-finance/risk-management/finance_operational_risk_rcsa.md` (KRIs as one step of a control self-assessment) and `domain-data-analytics/` business KPI dashboards (performance, not risk)."
techniques:
  - DS-02
  - RT-06
  - DS-36
  - QA-21
  - QA-12
difficulty: intermediate
tags:
  - key-risk-indicators
  - kri
  - risk-monitoring
  - thresholds
  - escalation
  - leading-indicators
  - early-warning-signs
  - what-to-track
updated: "2026-09-24"
reasoning:
  styles: [causal, quantitative, structural]
  stakes: variable
  horizon: weeks_to_months
  uncertainty: risk
  evidence_quality: moderate
  domain_complexity: cross_domain
  collaboration: small_team
  output_format: matrix_ranked_list
  user_role: [risk-lead, operator, executive, analyst, pm]
  mode: [design, plan, audit]
related_prompts:
  - domain-risk/risk_register_builder.md
  - domain-risk/risk_appetite_statement.md
  - domain-finance/risk-management/finance_operational_risk_rcsa.md
---

# Key Risk Indicators

**Objective:** For the handful of risks that matter most, choose measures that move
*before* the loss does, set thresholds at which a named person must act, and prove —
against your own history — that the indicator would have warned you. A KRI that only
confirms what already happened is a report, not a warning.

**When to Use:**
- A register exists (`risk_register_builder.md`) but its "monitoring" column says
  "watch closely" and nobody knows what number would trigger escalation.
- The board or a lender asks "how would you know this risk is getting worse?"
- An incident happened and, looking back, the signs were in data you already had.
- A dashboard has 40 red/amber/green tiles and nobody acts on any of them.

**Not this prompt if:**
- You are running a full operational-risk control self-assessment — `domain-finance/risk-management/finance_operational_risk_rcsa.md`
  (it attaches KRIs as one step; use this prompt when the indicators themselves need design).
- You want performance KPIs or a business dashboard — `domain-data-analytics/`.
- The risks are not yet identified — build the register first.

## Inputs / Context

1. **The top risks** (5–10) from the register, with owners and current scores.
2. **Appetite and tolerance limits** from `risk_appetite_statement.md`, if they exist.
3. **Data you already collect:** systems, reports, logs, surveys — and how often they refresh.
4. **Incident and near-miss history** for the last 1–3 years, with dates.
5. **Who can act:** the roles able to intervene at each level of severity.

## Method

1. **Trace each risk to its driver.** Risk → the cause that makes it more likely → an
   observable that moves with that cause. "Loss of key client" → "relationship
   deteriorating" → "days since last executive contact" and "open escalations on their account".

2. **Label every candidate leading or lagging.** Leading: moves before the loss (backlog
   age, overtime hours, unpatched systems). Lagging: counts losses after they happen
   (incidents, write-offs). Keep at least one leading KRI per top risk; if none exists, say
   so — that risk is monitored blind.

3. **Define each KRI precisely (DS-02).** Formula with numerator and denominator, data
   source, refresh frequency, and who produces the number. If two people would compute
   different values from the definition, it is not defined.

4. **Set thresholds from something.** Green/amber/red cut-offs anchored to the appetite
   limit, a historical percentile of your own data, or an external obligation — and state
   which. Amber should give enough lead time to act before red.

5. **Attach owner and action to each band (DS-36).** Green: owner reviews at the stated
   cadence. Amber: owner acts within a stated time and reports what they did. Red:
   escalates to a named decision-maker with a fixed message. A band with no action is decoration.

6. **Back-test against history (RT-06).** For each past incident, did the KRI reach amber
   beforehand, and with how much lead time? Also count amber breaches that were followed by
   nothing (false alarms). Report hits, misses and false alarms; a KRI with no hits across
   several relevant incidents is replaced.

7. **Enumerate gaming vectors (QA-21).** How could someone make the number look green without
   reducing the risk? Pair each with a counter-measure (a second indicator, an audit sample,
   an ownership split between producer and reviewer).

8. **Prune.** No more than two KRIs per risk and roughly 10–12 in total. Drop any KRI whose
   threshold breach would not change anyone's behaviour.

## Output Format

```
# Key risk indicators — [scope], [date]
Appetite source: [statement / thresholds / none — and consequence]

## KRI set
| Risk | KRI | Leading/lagging | Formula · source · frequency | Green | Amber | Red | Threshold basis | Owner | Amber action (time) | Red escalation (to whom) |

## Back-test (last [n] months)
| KRI | Incidents it should catch | Hits (lead time) | Misses | False alarms |

## Gaming vectors
| KRI | How it could be gamed | Counter-measure |

## Risks monitored blind (no leading KRI)
[risk — why no indicator exists — what would create one]

## Review
KRI set reviewed [cadence] by [role]; thresholds re-based when [...]
```

## Verification

- [ ] Every top risk has at least one KRI, and at least one leading KRI or a "monitored blind" entry.
- [ ] Every KRI has formula, source, frequency and producer.
- [ ] Every threshold states its basis (appetite, historical percentile, obligation).
- [ ] Every band has an owner action with a time limit; red names an escalation recipient.
- [ ] Back-test reports hits, misses and false alarms, not hits alone.
- [ ] Every KRI has at least one gaming vector and counter-measure.
- [ ] Total set is small enough to be reviewed in one meeting.

## False-Positive Prevention

1. **Lagging dressed as leading.** "Number of incidents" is a count of losses. Call it
   lagging and find what precedes it.
2. **Thresholds from nowhere.** A red at "10" with no basis will be ignored the first time it
   fires. State the anchor.
3. **Reporting hits only.** A KRI that went amber before 3 of 5 incidents and 8 other times
   with nothing following is noisy; show both numbers.
4. **Watermelon indicators.** Green outside, red inside: "backups completed" says nothing
   about whether a restore works. Measure the outcome the control exists for.
5. **The producer marks their own homework.** When the person whose performance the KRI
   reflects also computes it, pair it with an independent check.
6. **Dashboard sprawl.** Forty indicators means none are read. Prune to what changes action.
7. **A breach with no consequence.** If amber has triggered three times without any action,
   either the threshold or the ownership is wrong; fix one.

## Example Output

```
# Key risk indicators — 40-person IT managed-services firm, 2026-09-22
Appetite source: appetite statement 2026-06 (no client-impacting outage > 4h; cash ≥ 60 days)

## KRI set
| Ransomware on client estate | % client servers with critical patches > 14 days old | Leading | patched/total from RMM · weekly · Service Lead | <5% | 5–15% | >15% | appetite + 2025 median 6% | Service Lead | Amber: patch sprint within 5 days | Red: to MD same day |
| Loss of key engineer | % of P1 tickets resolved by one named engineer | Leading | tickets by resolver / all P1 · monthly · Ops Mgr | <25% | 25–40% | >40% | concentration limit in appetite | Ops Mgr | Amber: pair-shadow plan in 10 days | Red: to MD, hiring decision |
| Cash shortfall | Days of cash on hand | Leading | cash / avg daily outflow · weekly · Finance | ≥90 | 60–89 | <60 | appetite floor 60 | Finance Lead | Amber: chase debtors > 45 days | Red: to MD + board chair |
| Client outage | Client-impacting outages > 4h | Lagging | count per quarter · Service Lead | 0 | 1 | ≥2 | appetite | Service Lead | Amber: AAR within 7 days | Red: to MD |

## Back-test (last 24 months)
| Patch-age KRI | 5 security incidents | 3 hits (lead 9–20 days) | 2 misses (both phishing, not patch-related) | 5 of 8 amber breaches had no incident |
| P1 concentration | 1 resignation crisis | 1 hit (lead 3 months) | 0 | 1 |

## Gaming vectors
| Patch age | Servers removed from RMM to shrink the denominator | Monthly asset count reconciliation by Finance |
| P1 concentration | Tickets reassigned before closure | Measure by time spent, not closer |

## Risks monitored blind
Client consolidation by acquisition — no internal data precedes it; Account Mgr to log owner-change news monthly.
```

## Techniques Used

- **DS-02 Metric Specification** — formula, source, frequency and producer per KRI.
- **RT-06 Correlation and Cross-Analysis** — back-testing indicators against past incidents.
- **DS-36 Blocker Escalation Framework** — owner action per band and a fixed red escalation.
- **QA-21 Metric Gaming Vector Enumeration** — how each KRI could be made green falsely.
- **QA-12 False Positives Identification** — false alarms counted alongside hits.

## Related Prompts

- `domain-risk/risk_register_builder.md` — the risks and owners the KRIs attach to.
- `domain-risk/risk_appetite_statement.md` — the tolerance limits thresholds anchor to.
- `domain-risk/risk_board_risk_report.md` — where KRI status is reported upward.
- `domain-finance/risk-management/finance_operational_risk_rcsa.md` — KRIs inside a full RCSA.
