---
title: "Nonprofit Board Governance Health Check — Evidence-Rated, with Legal Items Flagged"
category: business-strategy/nonprofit
description: "Assess a nonprofit board across composition, fiduciary oversight, core policies, executive oversight, meeting practice, fundraising role and board-staff boundaries, rating each red/amber/green from documents rather than impressions and routing compliance questions to counsel; distinct from finance_board_finance_package_builder (the finance pack presented to a board) and domain-presentations/board-decks/ (slides for a board meeting)."
techniques:
  - DT-05
  - DP-28
  - RT-05
  - DD-05
  - OC-03
difficulty: intermediate
tags:
  - nonprofit
  - board-governance
  - fiduciary-duty
  - board-assessment
  - policies
  - executive-director
updated: "2026-09-24"
related_prompts:
  - domain-finance/corporate-finance-fpa/finance_board_finance_package_builder.md
  - domain-presentations/board-decks/boarddeck_executive_summary_slide.md
  - domain-legal/corporate-ma/legal_board_resolution_drafter.md
---

# Nonprofit Board Governance Health Check

**Objective:** Produce an evidence-based assessment of how well a nonprofit board is
governing — what is working, what is missing, and the three changes that matter most
in the next twelve months — with every legal or regulatory question routed to a
qualified reviewer rather than answered.

**When to Use:**
- Annual board self-assessment, or before a board retreat.
- A new executive director or board chair wants to know what they have inherited.
- A funder, auditor or incident has raised a governance question.
- The board meets but nobody can say what it decided last quarter.

**Not this prompt if:**
- You need the finance package the board reviews —
  `domain-finance/corporate-finance-fpa/finance_board_finance_package_builder.md`.
- You need slides for a board meeting — `domain-presentations/board-decks/`.
- You need a resolution drafted — `domain-legal/corporate-ma/legal_board_resolution_drafter.md`.
- You need a legal opinion on compliance with state nonprofit law, exempt-status
  requirements or filing obligations — that is counsel's work; this prompt flags it.

## Inputs

1. Bylaws and board roster (terms, officers, committees, skills if known).
2. Last 12 months of minutes and board packets.
3. Policies on file: conflict of interest (and signed annual disclosures),
   whistleblower, document retention, gift acceptance, executive compensation
   process, investment policy if applicable.
4. Most recent financial statements, audit or review report and management letter.
5. Executive director's last evaluation date and process.
6. Board giving and fundraising participation records.
7. Any known incident or funder question prompting the review.

## Method

1. **Assess element by element (DT-05).** Eight dimensions, each rated from documents:

   | Dimension | Green looks like |
   |---|---|
   | Composition | Skills matrix exists; terms staggered and enforced; vacancies < 20% |
   | Fiduciary oversight | Financials reviewed every meeting; budget approved before year start; audit or review received and management letter answered |
   | Core policies | Conflict-of-interest policy adopted, disclosures signed this year; other core policies adopted and dated |
   | Executive oversight | Written ED evaluation within 12 months; compensation set by the board with documented comparables |
   | Meeting practice | Quorum met; minutes approved; decisions recorded with votes |
   | Fundraising role | Every member gives at a personally meaningful level; a stated expectation exists |
   | Board-staff boundary | Board sets policy and oversees; does not manage staff day to day |
   | Succession | Chair and ED succession or emergency cover documented |

2. **Rate with evidence (DP-28, RT-05).** Green, amber or red — each rating cites a
   document, a minute or a count. "Unknown" is its own rating and counts as amber:
   if nobody can find the conflict-of-interest disclosures, they are not in force.

3. **Flag for qualified review (DD-05).** Anything that asks "are we compliant?" —
   exempt-status requirements, public filings, state registration, executive
   compensation reasonableness, related-party transactions, lobbying or political
   activity — is listed with the question and the reviewer (counsel, auditor), not
   answered.

4. **Prioritise.** Pick three changes for the next twelve months. Fiduciary and
   conflict-of-interest gaps rank above composition and meeting practice, because
   they create the largest exposure.

5. **Tabulate the output (OC-03)** so the board can review it in a single session.

## Output Format

```
# Board governance health check — [organisation], [date]

## Summary
[Green n / Amber n / Red n] — top three changes: 1. … 2. … 3. …

## Dimension ratings
| Dimension | Rating | Evidence | Gap |

## Flags for qualified review
| Question | Why it matters | Reviewer |

## Twelve-month plan
| Change | Owner | By when | Evidence it is done |

## What this check could not see
[documents not provided, and how that limits the ratings]
```

## Verification

- [ ] Every rating cites a document, minute or count.
- [ ] Missing documents are rated Unknown / amber, not assumed.
- [ ] No compliance conclusion is stated; all are flagged with a reviewer.
- [ ] The top three changes follow from red or amber ratings.
- [ ] Each change has an owner, a date and a verifiable completion signal.

## False-Positive Prevention

1. **A policy on file is not a policy in force.** A conflict-of-interest policy with
   no signed disclosures this year is amber at best.
2. **Attendance is not oversight.** Full attendance at meetings where the financials
   are "received" without discussion is not fiduciary review.
3. **Do not diagnose compliance.** "The board is out of compliance with state law" is
   a legal conclusion; write "question for counsel".
4. **Do not score from impressions.** "The board is engaged" is not evidence;
   "8 of 9 members attended 4 of 4 meetings and 3 served on committees" is.
5. **Small boards are not automatically weak.** Rate against the organisation's size
   and bylaws, not a large-institution template.
6. **Board micro-management can look like diligence.** Directors approving staff
   schedules is a boundary problem, not a strength.
7. **Dual failure:** an all-red report nobody can act on is as useless as an
   all-green one. Three changes, not thirty.

## Example Output

```
# Board governance health check — Riverbend Literacy, Sep 2026

## Summary
Green 3 / Amber 3 / Red 2 — top three changes:
1. Collect signed conflict-of-interest disclosures from all 9 members by Nov.
2. Complete the overdue written ED evaluation by Dec.
3. Put financial statements on every agenda with a treasurer's summary.

## Dimension ratings
| Dimension | Rating | Evidence | Gap |
| Composition | Amber | 9 of 11 seats filled; 4 terms end Jun 2027 | No skills matrix; no finance professional |
| Fiduciary oversight | Red | Financials on agenda at 2 of 4 meetings (minutes); FY25 review received, management letter not discussed | Regular review missing |
| Core policies | Red | COI policy adopted 2019; 3 of 9 disclosures signed in 2026 | Disclosures lapsed |
| Executive oversight | Amber | Last written ED evaluation Mar 2024 | 30 months since the last one; 18 months past the annual cycle |
| Meeting practice | Green | Quorum 4/4; minutes approved 4/4 | — |
| Fundraising role | Green | 9 of 9 gave in FY26 | — |
| Board-staff boundary | Green | No operational items in minutes | — |
| Succession | Amber | No emergency ED cover plan | Document interim cover |

## Flags for qualified review
| Question | Why it matters | Reviewer |
| Whether the public annual filing's governance answers match practice | Filing asks about COI and review of the return | Auditor / counsel |
| Board member's firm supplies printing — related-party process | Needs documented disinterested approval | Counsel |

## Twelve-month plan
| Change | Owner | By when | Evidence |
| COI disclosures | Secretary | 30 Nov 2026 | 9 of 9 signed forms on file |
| ED evaluation | Chair + exec committee | 15 Dec 2026 | Written evaluation in personnel file |
| Financials every meeting | Treasurer | From Oct 2026 | Minutes show review 4/4 |

## What this check could not see
Committee minutes were not supplied; the fiduciary rating may understate finance-
committee review.
```

## Techniques Used

- **DT-05 Element-by-Element Assessment Matrix:** eight dimensions rated separately.
- **DP-28 Traffic-Light Verdict System:** green/amber/red with Unknown as amber.
- **RT-05 Evidence-Based Reasoning:** every rating cites a record.
- **DD-05 Human Review Flags:** compliance questions routed to counsel or auditor.
- **OC-03 Markdown Table Specification:** one-session reviewable tables.

## Related Prompts

- `domain-finance/corporate-finance-fpa/finance_board_finance_package_builder.md` — the finance pack the board should review
- `domain-presentations/board-decks/boarddeck_executive_summary_slide.md` — presenting the findings
- `domain-legal/corporate-ma/legal_board_resolution_drafter.md` — adopting the policies
