---
title: "Live-Ops Calendar and Monetization Ethics Review"
category: game-development/economy
description: "Plan a live-ops season the team can actually staff — events, cadence, content load against capacity — and audit every offer in it against explicit must-nots: no dark patterns, disclosed odds, real-money prices visible, paid random items flagged for minors and for jurisdictions that restrict them; distinct from the economy system design (currencies, sinks, drop tables)."
techniques:
  - DP-04
  - DS-32
  - DS-33
  - QA-21
  - OC-10
difficulty: advanced
tags:
  - live-ops
  - monetization
  - loot-boxes
  - dark-patterns
  - minors
  - game-economy
  - ethics
updated: "2026-09-24"
related_prompts:
  - domain-game-development/economy/economy_system_design.md
  - domain-data-analytics/analysis-and-sql/analytics_cohort_retention_analysis.md
  - domain-business-strategy/startup/monetization_model_selector.md
---

# Live-Ops Calendar and Monetization Ethics Review

**Objective:** Produce a season calendar that fits the team's capacity, and an
offer-by-offer audit that removes manipulative mechanics and flags where paid
randomness, minors or a jurisdiction make an offer a legal question rather than a
design one.

**When to Use:**
- A live game is planning its next season, event run, or battle pass.
- A new store offer, bundle, or gacha/loot mechanic is proposed.
- The team suspects the calendar is burning people out or the store is drifting
  toward pressure tactics.

**When NOT to use:**
- Currency design, sources and sinks, drop-rate tables, inflation —
  `economy_system_design.md`. This prompt is distinct because it operates the
  economy over time and audits offers, not the underlying model.
- Choosing a business model for a non-game app — `domain-business-strategy/startup/monetization_model_selector.md`.
- Legal advice. Regulatory items here are flags to take to counsel, not rulings.

## Inputs

1. **Game, platforms, age rating, and the audience actually playing** (telemetry
   or survey, not only the rating).
2. **Markets** the game is sold in.
3. **Season length and planned beats**: launches, events, passes, store rotations.
4. **Team capacity** in the unit the team uses (points, person-weeks).
5. **Offer list**: each offer's price, currency path, contents, randomness,
   time limits, targeting rules.
6. **KPIs** the season will be judged on.

## Method

1. **Lay out the calendar.** Week by week: beats, content each requires, and who
   builds it. Leave a no-content week for fixes after each major beat.
2. **Load against capacity.** Sum content demand; target ≤ 85% of capacity. Cut
   by reruns, reuse, or dropping a beat — never by assuming overtime.
3. **Apply the must-nots to every offer (DP-04).**
   - No countdowns that reset or fake scarcity.
   - Real-money price visible at the point of purchase; no currency bundles sized
     so a leftover always remains.
   - No friction added to sell its removal (pay-to-skip designed waits).
   - No targeting by signals of vulnerability (spend spikes, late-night sessions,
     recent losses) or of being a minor.
   - Paid random items disclose odds before purchase and have a pity/guarantee.
   - No pay-to-win in competitive modes.
   - No confirm-shaming or pre-checked purchases; purchases are easy to refund
     where the platform allows.
4. **Enumerate the rules that apply (DS-32, DS-33).** Per market and storefront:
   odds-disclosure requirements, paid-random-item restrictions, age-rating
   consequences, children's privacy law, consumer-protection actions on dark
   patterns. Mark each `[verify current]` with the date checked.
5. **Minors gate.** If the rating or the real audience includes under-18s: no paid
   random items for them (or a parental-consent gate), spending limits, no
   behavioural targeting, parental controls surfaced.
6. **Red-team the KPIs (QA-21).** For each KPI, list how it could rise through a
   harmful mechanic (conversion via fake urgency, ARPPU via whale targeting,
   retention via streak punishment). Add a guardrail metric for each.
7. **Attach the disclaimer (OC-10)** to the output, always.

## Output Format

```
## Calendar        — week | beat | content units | owner
## Capacity        — demand vs capacity, % loaded, cuts made
## Offer audit     — offer | must-not check | verdict (keep / change / remove) | change
## Regulatory flags — market/store | rule | applies? | [verify current] | action
## Minors          — audience evidence | gate applied
## KPI guardrails  — KPI | gaming vector | guardrail metric
## Disclaimer
```

## Verification

- [ ] Calendar content sums to the capacity table's demand figure.
- [ ] Every offer has a verdict against every must-not, not only the relevant-looking ones.
- [ ] Every paid random item has odds disclosure and a pity rule, or is removed.
- [ ] Every regulatory line carries `[verify current]` and a checked date.
- [ ] Every KPI has at least one guardrail metric.
- [ ] The disclaimer is present.

## False-Positive Prevention

1. **Monetization is not a dark pattern.** A clearly priced cosmetic with no
   pressure mechanic is fine; do not flag honest selling.
2. **Time-limited is not fake urgency.** A real, non-resetting event window is
   legitimate; the defect is scarcity that is not true.
3. **Not every market restricts loot boxes.** Flag by the markets actually served;
   do not apply the strictest rule everywhere without saying it is a choice.
4. **A rating is not the audience.** A 12+ game with a large under-13 audience
   needs the minors gate; a 17+ rating does not prove the audience is adult.
5. **Do not state regulatory rules as settled.** They change; say what to verify.
6. **Capacity at 100% is a finding, not a plan.** Treat it as over-loaded.

## Example

**Input:** Free-to-play mobile hero shooter, rated 12+ (telemetry: ~18% of
players self-report under 16). Markets: EU, UK, US, Australia. 12-week season.
Capacity: 70 content units.

```markdown
## Calendar
| Week | Beat | Units |
|---|---|---|
| 1 | Season launch + battle pass | 30 |
| 3–4 | Event A "Night Market" | 12 |
| 6 | Mid-season balance + hero | 10 |
| 8–9 | Event B → rerun of last season's event | 4 (was 12) |
| 1–12 | Store rotations (reuse cosmetics) | 3 (was 8) |
| 2, 5, 7, 10 | Fix weeks — no new content | 0 |
| | **Total** | **59** |

## Capacity
Original demand 30 + 12 + 10 + 12 + 8 = 72 of 70 (103%). After cuts (Event B rerun
−8, store reuse −5): 30 + 12 + 10 + 4 + 3 = 59 of 70 (84%), under the 85% target.

## Offer audit
| Offer | Issue | Verdict | Change |
|---|---|---|---|
| Battle pass $9.99 | none | Keep | — |
| "Flash bundle" 2-h timer | timer restarts each login | Change | fixed end time shown in local time |
| Gem pack 550 (items cost 500/600) | leftover engineered | Change | add 500 and 1,200 packs |
| Hero crate (random, paid) | odds not shown; no pity | Change | show odds pre-purchase; guarantee at 40 crates; minors gate |
| "Skip matchmaking wait" | wait inflated to sell skip | Remove | — |
| Push offer after 3 losses | targets frustration | Remove | — |

## Regulatory flags (checked 2026-09-24, all [verify current])
| Market/store | Rule | Applies? | Action |
|---|---|---|---|
| App Store / Google Play | odds disclosure for paid random items | Yes | odds screen before purchase |
| Belgium | regulator position that paid loot boxes may be gambling | Yes (EU) | counsel review; consider disabling paid crates in BE |
| UK | industry principles on under-18 access to paid loot boxes | Yes | parental-consent gate |
| Australia | classification impact of paid loot boxes | Yes | check rating impact before launch |
| US | children's privacy (COPPA) if under-13s present; FTC action on dark patterns | Yes | age gate; remove patterns above |

## Minors
18% self-report under 16 → gate applied: no paid crates without parental consent,
monthly spend cap, no push offers, parental controls in settings.

## KPI guardrails
| KPI | Gaming vector | Guardrail |
|---|---|---|
| Conversion | fake urgency | refund-request rate; % purchases in last 5 min of a timer |
| ARPPU | whale targeting | share of revenue from top 1% of spenders; spend-cap hits |
| D7 retention | streak punishment | % sessions under 3 min (log-in-only) |

## Disclaimer
Regulatory lines are flags for review, not legal advice. Rules on paid random
items, children's data and consumer protection vary by market and change; confirm
each with qualified counsel before launch.
```

## Techniques Used

- **DP-04 (Must-Not Constraints):** the explicit must-nots every offer is checked against.
- **DS-32 (Regulatory Enumeration Pattern):** rules listed per market and storefront.
- **DS-33 (Jurisdiction-Adaptive Output):** actions differ by market served.
- **QA-21 (Metric Gaming Vector Enumeration):** KPIs red-teamed for harmful routes to growth.
- **OC-10 (Mandatory Disclaimer Pattern):** not-legal-advice block required in every output.

## Related Prompts

- `domain-game-development/economy/economy_system_design.md` — currencies, sinks and drop tables.
- `domain-data-analytics/analysis-and-sql/analytics_cohort_retention_analysis.md` — measuring season retention honestly.
- `domain-business-strategy/startup/monetization_model_selector.md` — business-model choice outside games.
