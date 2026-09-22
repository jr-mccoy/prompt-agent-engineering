---
name: engagement-economics
description: Compute the money side of a client-services practice — the rate floor below which work destroys value, the realised margin on a completed engagement, and Gate C on close-out. Use this skill to "work out my day rate", "what is my rate floor", "what did this engagement actually earn", "run the post-calc", "can I quote fixed price for this", or "close out the engagement". Derives walk-away, floor and standard rates from the full cost of delivery and a utilization assumption; computes realised effective rate from COLLECTED revenue and TOTAL effort including unbilled; maintains the estimate-error series that decides fixed-price eligibility.
license: MIT
compatibility: Standard library only, Python 3.9+. `scripts/economics.py` implements the rate-floor model, engagement post-calculation, the estimate-error series and Gate C; `--self-check` proves the arithmetic (including that margin is applied as a divisor), that unbilled effort lowers the realised rate, that outstanding amounts are excluded from revenue, and that each Gate C condition blocks. No dependencies, no network, no writes.
metadata:
  tags: [client-services, rate-floor, margin, utilization, profitability, gate, consulting]
  updated: "2026-09-21"
---

# Engagement Economics

## Purpose

A services practice can be busy and unprofitable for a long time without noticing,
because the two numbers that would reveal it are rarely computed: the rate below
which work destroys value, and what an engagement actually earned once unbilled
effort and uncollected invoices are counted honestly.

This skill computes both, and closes the loop between them.

**Rate floor.** Works down from the total annual cost of being in business —
fixed costs, target income, employment burden, self-funded pension and healthcare
— divided by genuinely billable days, then loaded for bad debt and typical
overrun, then raised by the target margin. Three thresholds come out: walk-away,
floor, and standard. A utilization sensitivity table shows what the floor does at
50/60/70/80% billable, which is usually the most persuasive artifact in any
conversation about discounting.

Two arithmetic points the script enforces. Margin is applied as `/(1 − m)`, not
`× (1 + m)` — the latter is the common error and produces a rate roughly 4
percentage points of margin too low. And the billable fraction is the dominant
lever: at 0.50 rather than 0.80, the floor rises by 60%.

**Post-calculation.** Revenue is **collected**, not invoiced: write-offs and
outstanding amounts are subtracted rather than assumed. Effort is **total**,
billed plus unbilled. Both corrections are necessary; either one alone still
flatters the result.

**Estimate-error series.** Each close-out appends an actual/estimated ratio. Once
five engagements exist the coefficient of variation decides fixed-price
eligibility: below 0.25 yes, to 0.40 with a tight input contract, above that no.
Fewer than five points is itself a "do not fix a price" verdict.

**Gate C (close-out complete)** refuses to close an engagement while an invoice is
outstanding and not written off, while unbilled effort or the original estimate is
unrecorded, or while case-study consent and the repeat/decline verdict are missing.

## When to Use This Skill

- Setting or revisiting rates, annually or when costs change
- Before agreeing any discount — hold the conversation against the floor
- At close-out of every engagement, including the ones that went well
- Deciding whether an engagement type can be sold at a fixed price

## Usage

```bash
python scripts/economics.py --floor ../../config/practice.json
python scripts/economics.py --postcalc closeout.json --config ../../config/practice.json
python scripts/economics.py --gateC closeout.json
python scripts/economics.py --self-check
```

## Boundaries

- **Not tax, accounting or financial advice.** Employment-burden rates,
  deductibility and entity treatment are jurisdiction-specific. The output is the
  input to a conversation with an accountant.
- **The floor is where value creation stops, not where pricing starts.** Quoting at
  the floor means every overrun is a loss.
- See [`references/method.md`](references/method.md) for the derivation and the
  failure modes.
