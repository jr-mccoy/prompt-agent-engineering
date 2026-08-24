# Divorce / Custody Flag Framework

This documents the four flagging dimensions, what each flag captures, and how to
tune them. It is organizational, not legal advice. Which categories matter — and
how they are treated — depends on your jurisdiction and your attorney's strategy.
Marital vs. separate property rules differ between community-property and
equitable-distribution states; support and custody standards differ everywhere.

A flag means **"a reviewer may want to look at this row."** Nothing more. It is
not evidence, an accusation, or a statement about anyone's intent.

## Flag code format

The `flags` column holds `;`-joined codes: `DIMENSION:CODE|PRIORITY`, e.g.
`CASH:LARGE_CASH|HIGH; ASSET:ACCOUNT_TRANSFER|MEDIUM`. Priorities are
`HIGH | MEDIUM | LOW | INFO`; any HIGH flag sets `needs_review = TRUE`.

## Dimension 1 — Asset & property tracing (`ASSET:*`)

Surfaces movement, conversion, or large acquisition of assets.

| Code | Captures |
|------|----------|
| `ACCOUNT_TRANSFER` | Transfers/wires between accounts |
| `LARGE_TRANSFER` | Transfers/wires at or above your large-amount threshold (HIGH) |
| `LARGE_PURCHASE` | Large single outflows |
| `CRYPTO_EXCHANGE` | Activity with crypto exchanges (HIGH) |
| `BROKERAGE_INVESTMENT` | Movements to/from brokerages or robo-advisors |
| `PRECIOUS_LUXURY` | Jewelry, precious metals, luxury, pawn |

**Tune:** set `min_abs_amount` for `LARGE_TRANSFER`/`LARGE_PURCHASE` to a level
that is unusual for your household; add your banks'/brokerages' names.

## Dimension 2 — Income tracing (`INCOME:*`)

Builds a picture of money coming in.

| Code | Captures |
|------|----------|
| `PAYROLL` | Payroll / direct deposit (INFO — baseline income) |
| `LARGE_DEPOSIT` | Large inflows |
| `CASH_DEPOSIT` | Cash deposits (source worth confirming) |
| `SIDE_INCOME` | Inflows via Venmo/Zelle/PayPal/Cash App/Square/Stripe |

**Tune:** set `min_amount` for `LARGE_DEPOSIT` near your typical paycheck so only
unusual inflows stand out. Note: P2P platforms can be income *or* reimbursements —
this only flags for review.

## Dimension 3 — Child & custody expenses (`CHILD:*`)

Surfaces spending tied to children — relevant to custody and child-support
discussions.

| Code | Captures |
|------|----------|
| `CHILDCARE` | Daycare, childcare, preschool, nanny |
| `SCHOOL_TUITION` | School / tuition / PTA |
| `CHILD_MEDICAL` | Pediatric / children's medical / orthodontia |
| `CHILD_ACTIVITY` | Sports, lessons, camps, activities |

**Tune:** add the actual names of your children's providers to the regex or to
the categorizer whitelist for cleaner capture.

## Dimension 4 — Cash & undocumented flows (`CASH:*`)

Surfaces money that leaves a clear paper trail and becomes hard to trace.

| Code | Captures |
|------|----------|
| `ATM_WITHDRAWAL` | ATM / cash withdrawals |
| `LARGE_CASH` | Cash withdrawals at/above threshold (HIGH) |
| `ROUND_CASH` | Round-dollar cash withdrawals (a pattern worth noting) |
| `CHECK_TO_CASH` | Checks written to cash/self |
| `P2P_OUT` | Outgoing peer-to-peer payments above a threshold |

**Tune:** set the `LARGE_CASH` `min_abs_amount` and `ROUND_CASH` `round_step`
to your normal cash habits.

## How to use the review queue

`<stem>_review_queue.csv` contains only flagged rows, sorted HIGH→INFO, with the
priority, date, description, amount, category, and flag codes. Hand it to your
attorney, or use it to prepare answers/explanations they may ask for. You don't
need a flag to be "bad" — many will have ordinary explanations. The point is that
nothing relevant is silently missing.

## A note on completeness and good faith

These tools help you organize and disclose your finances thoroughly. Full, honest
financial disclosure is the expectation in family-law matters. Use this to
prepare a complete picture for your attorney — not to hide or shade anything.
