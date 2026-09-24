---
title: "Board Risk Report — What Changed, What Breached, and What the Board Must Decide"
category: risk/reporting
description: "Assemble the periodic risk report for a board or risk committee from the working instruments: lead with what changed since the last report and the decisions requested, show top-risk movement with reasons, appetite breaches, amber and red KRIs only, open and expiring risk acceptances, incidents with their lessons, and emerging risks — each item tagged note / discuss / decide, within a page budget; distinct from `domain-risk/risk_heat_map.md` (visualizes and re-ranks the register), `domain-finance/corporate-finance-fpa/finance_board_finance_package_builder.md` (financial results package) and `domain-presentations/powerpoint_board_deck.md` (slide production)."
techniques:
  - ST-46
  - QA-28
  - DS-05
  - NE-17
  - QA-12
difficulty: intermediate
tags:
  - board-reporting
  - risk-committee
  - risk-governance
  - kri
  - risk-appetite
  - executive-communication
updated: "2026-09-24"
reasoning:
  styles: [synthetic, evaluative, communicative]
  stakes: high
  horizon: months
  uncertainty: variable
  evidence_quality: moderate
  domain_complexity: cross_domain
  collaboration: small_team
  output_format: structured_memo
  user_role: [risk-lead, executive, company-secretary, founder, cfo]
  mode: [synthesize, document, decide]
related_prompts:
  - domain-risk/risk_heat_map.md
  - domain-risk/risk_key_risk_indicators.md
  - domain-finance/corporate-finance-fpa/finance_board_finance_package_builder.md
---

# Board Risk Report

**Objective:** Give the board what it needs to govern risk in the time it has to read:
what changed, where the organisation is outside its own limits, which accepted risks are
coming due, and the specific decisions it is being asked to make. Everything else is an
appendix.

**When to Use:**
- A board or risk committee meets quarterly (or monthly) and receives a risk paper.
- The current paper is the full register pasted in, and directors skim it.
- An appetite statement exists and the board has never been told when it was breached.
- After a serious incident, the board wants to know whether the risk process saw it coming.

**Not this prompt if:**
- You need to build or re-rank the register, or draw the heat map — `domain-risk/risk_register_builder.md`,
  `domain-risk/risk_heat_map.md` (both feed this report).
- The paper is the finance package with a risk section — `domain-finance/corporate-finance-fpa/finance_board_finance_package_builder.md`.
- You need the slides produced — `domain-presentations/powerpoint_board_deck.md` after this content is settled.
- A live crisis needs a board briefing now — `domain-risk/risk_crisis_severity_triage.md` first.

## Inputs / Context

1. **The register** now and at the last report (to compute movement).
2. **Appetite statement** with tolerance limits.
3. **KRI status** from `risk_key_risk_indicators.md`, with the prior period.
4. **Open risk acceptances** and their expiry dates (`risk_acceptance_exception_memo.md`).
5. **Incidents and near-misses** since the last report, with AAR status.
6. **Emerging risks** from a tail scan or management horizon-scanning.
7. **The board's format:** page limit, committee remit, what was asked for last time.

## Method

1. **Triage findings before writing (QA-28).** Sort every candidate item into: needs a board
   decision; board should discuss; board should note; management-only (appendix or omit). Only
   the first three reach the body.

2. **Write the front page as assertions with evidence (ST-46).** Three to five headline
   sentences, each a claim followed by the number that supports it ("Cyber exposure rose:
   patch-age KRI red for 6 weeks, 22% of servers"). Then the decisions requested.

3. **Show movement, not position.** For the top risks: rating now vs last report, direction,
   and the reason it moved. A risk that did not move needs no paragraph.

4. **Report breaches against appetite plainly.** Each breach: which limit, by how much, since
   when, what management is doing, and whether it asks the board to accept, fund or direct.

5. **Show only amber and red KRIs (DS-05).** Give the count by band and list the non-green ones
   with trend. Full KRI table goes to the appendix.

6. **List acceptances expiring before the next meeting** and any renewed without evidence.

7. **Incidents and lessons.** One line each: what happened, cost, whether a register risk
   predicted it, the AAR action and its status.

8. **Emerging risks.** Two to four, each with why now and what would make it a register entry.

9. **Close with the decision requests (NE-17).** Numbered, each with the options, management's
   recommendation, and what happens if the board defers.

## Output Format

```
# Risk report to [board / committee] — [period], [date]
Prepared by: [role] · Pages: [n] of [budget]

## Headlines
1. [assertion] — [evidence]
...
## Decisions requested
D1. [decision] — options [...] — recommendation [...] — if deferred [...]

## Top-risk movement
| Risk | Last | Now | Direction | Why it moved | Tag (decide/discuss/note) |

## Appetite breaches
| Limit | Actual | Since | Management action | Board ask |

## KRIs: [g] green · [a] amber · [r] red (of [n])
| KRI (amber/red only) | Value | Trend | Owner action |

## Risk acceptances
Open: [n] · Expiring before next meeting: [list] · Renewed without evidence: [list or none]

## Incidents since last report
| Incident | Cost | Predicted by register? | AAR action | Status |

## Emerging risks
| Risk | Why now | Would enter register if |

Appendix: full register, full KRI table, heat map
```

## Verification

- [ ] Every body item is tagged decide / discuss / note; management-only items are in the appendix.
- [ ] Headlines are assertions with a supporting number.
- [ ] Top risks show last vs now, with a reason for each move.
- [ ] Every appetite breach states the limit, the actual value and the board ask.
- [ ] KRI counts by band add up to the total; only non-green listed in the body.
- [ ] Expiring acceptances listed with dates.
- [ ] Each decision request has options, a recommendation and the cost of deferral.
- [ ] Body within the page budget.

## False-Positive Prevention

1. **The register as the report.** Forty rows transfer the reading burden to directors. Triage first.
2. **Position without movement.** "Cyber: high" every quarter tells the board nothing; show what changed and why.
3. **Green reassurance.** Eleven green tiles and one red one should read as "one red"; list non-green only.
4. **Breaches softened into "areas of focus".** If a limit was exceeded, say so with the number.
5. **Decisions implied, not asked.** "The board may wish to consider" is not a request. Number it
   and state the options.
6. **Incidents detached from the register.** Whether the process predicted the incident is the
   most useful thing the board can learn about the process itself.
7. **Emerging-risk padding.** Generic trends ("AI", "geopolitics") with no link to the business
   are filler; each needs a why-now and an entry condition.

## Example Output

```
# Risk report to Audit & Risk Committee — Q3 2026, 2026-10-08
Prepared by: Head of Risk · Pages: 3 of 4

## Headlines
1. Cyber exposure rose — patch-age KRI red for 6 weeks (22% of servers past 14 days vs limit 15%).
2. Client concentration eased — top client fell from 24% to 19% of revenue after two new contracts.
3. One appetite breach — cash buffer at 52 days vs 60-day floor since 2026-09-12.
4. Two incidents; the register predicted one.

## Decisions requested
D1. Approve $85k for a managed patching service — options: approve / defer to Q1 / reject — recommend approve —
    if deferred, patch-age likely stays red through year-end.
D2. Accept cash buffer below floor until 2026-12-31 — recommend accept with monthly reporting —
    if rejected, management will draw the credit line now ($9k interest to year-end).

## Top-risk movement
| Cyber / ransomware | 12 | 16 | ↑ | Patching backlog after staff departure | decide (D1) |
| Client concentration | 16 | 12 | ↓ | Two new contracts signed | note |
| Liquidity | 8 | 12 | ↑ | Delayed receipts from one public-sector client | decide (D2) |

## Appetite breaches
| Cash ≥ 60 days | 52 days | 2026-09-12 | Debtor chase; receipts due Nov | Accept to 12-31 (D2) |

## KRIs: 7 green · 3 amber · 1 red (of 11)
| Patch age (red) | 22% | ↑ 3 periods | Interim sprint; D1 |
| Days of cash (amber) | 52 | ↓ | Debtor chase |
| P1 tickets by one engineer (amber) | 31% | → | Pairing plan |
| Staff attrition 12-mo (amber) | 18% | ↑ | Exit interviews reviewed |

## Risk acceptances
Open: 4 · Expiring before next meeting: RA-2026-03 (legacy payroll export, 2026-11-30) · Renewed without evidence: none

## Incidents since last report
| Phishing led to one mailbox compromise | $4k | Yes (R-07) | MFA enforced for all | Done |
| Supplier invoice paid twice | $11k recovered | No | Add duplicate-payment check to register | Open, due 11-15 |

## Emerging risks
| Largest client under acquisition review | Announced 2026-09-30 | Deal closes and new owner consolidates suppliers |

Appendix: full register (14 risks), KRI table, heat map
```

## Techniques Used

- **ST-46 Assertion-Evidence Content Structure** — headlines as claims with numbers.
- **QA-28 Findings-vs-Presentation Triage** — decide / discuss / note / appendix sorting.
- **DS-05 Visualization and Communication Guidance** — non-green only, movement over position.
- **NE-17 Call-to-Action Mandatory Close** — numbered decisions with options and deferral cost.
- **QA-12 False Positives Identification** — green reassurance and softened breaches named as failures.

## Related Prompts

- `domain-risk/risk_heat_map.md` — the visual that goes in the appendix.
- `domain-risk/risk_key_risk_indicators.md` — the KRI status this reports.
- `domain-risk/risk_acceptance_exception_memo.md` — the acceptances and expiries listed.
- `domain-finance/corporate-finance-fpa/finance_board_finance_package_builder.md` — the finance paper that sits beside this one.
