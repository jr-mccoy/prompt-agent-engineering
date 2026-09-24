---
title: "Change Order Pricing and Notice — Classify the Trigger, Price It Under the Contract's Own Terms, and Ask the Owner for a Dated Decision"
category: specialized-fields/trades
description: "For a change that arises mid-job — owner request, concealed condition, pre-agreed unit-price item, allowance overrun, or deleted work — classify the trigger, check whether the bid's unit prices, allowances or contingency already cover it, price each item under the change terms the user pastes from their contract (markup, credits, schedule days), and draft a plain-language notice asking the owner for a decision by a date, with an internal ledger — distinct from the scope-ledger skill, which detects drift but does not price it, and from drafting a SOW's change clause (legal_sow_drafter)."
techniques:
  - NE-11
  - RP-02
  - NE-17
  - QA-01
difficulty: intermediate
tags:
  - trades
  - construction
  - change-order
  - pricing
  - client-communication
  - contractor
  - extra-work
  - hidden-damage-found
  - client-wants-changes
updated: "2026-09-24"
reasoning:
  styles: [quantitative, procedural, communicative]
  stakes: high
  horizon: days
  uncertainty: ambiguity
  evidence_quality: rich
  domain_complexity: regulated
  collaboration: small_team
  output_format: [structured, prose]
  user_role: [contractor, estimator, tradesperson, project_manager]
  mode: [synthesize, communicate]
related_prompts:
  - client-services-studio/skills/scope-ledger/SKILL.md
  - domain-legal/contracts-transactional/legal_sow_drafter.md
  - domain-specialized-fields/trades/trades_bid_estimate_with_contingency.md
---

# Change Order Pricing and Notice

**Objective:** Price a mid-job change the way the contract says to, and get the
owner's written decision before the changed work proceeds — so the contractor is
paid for what changed and the owner is never surprised by an invoice.

**When to Use:**
- Demo opened something the bid could not see, and work is stopped until someone decides.
- The owner asked for "one small thing" and you need to price it before doing it.
- A selection came in over (or under) its allowance.
- The owner deleted something and is owed a credit.
- **Not this prompt if** you only need to know *whether* delivered work drifted from
  agreed scope — `client-services-studio/skills/scope-ledger/SKILL.md` detects
  that; this prompt prices and communicates it. Writing the change clause into a
  contract is `domain-legal/contracts-transactional/legal_sow_drafter.md` or your
  attorney. The original bid and its unknowns register are
  `trades_bid_estimate_with_contingency.md`.

## Inputs / Context

1. **The contract's change terms, pasted verbatim:** notice requirements, who may
   sign, markup on changes, how credits are figured, emergency work, concealed or
   differing conditions. If there are none, say so — this is flagged for an attorney.
2. **The bid:** unit prices, alternates, allowances, exclusions, unknowns register.
3. **What happened:** date, what was found or requested, photos or measurements.
4. **Your costs for the change:** labor hours, materials, subs, equipment.
5. **Schedule:** current completion date and what the change does to it.
6. **Whether work is stopped,** and what the owner loses each day it stays stopped.

## Method

1. **Classify each item.**
   - **Pre-priced** — a unit price or alternate already in the bid.
   - **Owner-requested** — new or different work the owner asked for.
   - **Concealed condition** — not reasonably visible at bid; whether it is a
     change depends on the contract's words, which the user supplies.
   - **Allowance reconciliation** — selection cost vs allowance amount.
   - **Deletion** — work removed; a credit is owed.
   - **Contractor's risk** — covered by carried contingency or the contractor's own
     error; **not billed**. Say so to yourself before the owner says it to you.

2. **Price under the contract's terms (NE-11).**
   - Pre-priced: `quantity × unit price` — no new markup.
   - New work: `(labor hr × rate + material + sub + equipment) × (1 + change markup)`.
   - Allowance: `(actual − allowance) × (1 + markup)` if the contract applies markup.
   - Credit: the deleted work's direct cost × (1 + markup), unless the contract
     states another method.
   - Schedule: working days added, and the new completion date.

3. **Separate facts from the ask.** What was found (with a photo reference), what
   it means for the work, what it costs, what happens to the schedule — then the
   decision you need.

4. **Write for the owner (RP-02).** Plain language: no "differing site condition",
   no "per §7.3" in the body — the reference goes in the ledger. One paragraph per
   item, each with its price.

5. **Close with a dated decision (NE-17).** Options — approve all, approve items
   separately, or decline — and the factual consequence of each. A decision time
   tied to what is actually stopped. Signature on the contract's own change form.

6. **Cross-check (QA-01).** Item prices sum to the total; the new contract sum
   equals the old sum plus this change; contractor's-risk items are absent from the
   bill; nothing in the notice interprets the contract beyond quoting it.

## Output Format

```
## A. Notice to owner
Subject: Change Order #[n] — [job] — decision needed by [date time]
[what we found / what you asked for — one paragraph per item with its price]
[schedule effect]
[options and what each means]
[how to approve]

## B. Pricing detail
| Item | Class | Basis | Direct | Markup | Price |
CO total · original contract sum · prior COs · new contract sum · new completion date

## C. Not billed (contractor's risk)
## D. Contract terms relied on (quoted) and questions for an attorney
## E. Cross-check
```

## Verification

- [ ] Every item has exactly one class and a pricing basis from the contract or bid.
- [ ] Pre-priced items use the bid's unit price with no second markup.
- [ ] Credits are shown as negatives and included in the total.
- [ ] CO total and new contract sum are recomputed and match.
- [ ] The notice states a decision time and the consequence of each option.
- [ ] No legal conclusion appears in the notice; contract text is quoted in section D.

## False-Positive Prevention

1. **Your contingency is not the owner's money** on a lump-sum job. Items you
   carried in contingency are not billed a second time.
2. **Found it is not the same as a change.** Whether a concealed condition is
   billable depends on the contract's words and what was reasonably visible —
   quote the clause; if it is unclear, ask an attorney before sending.
3. **Do the work after the signature, not before**, unless the contract's
   emergency terms apply — and then say so in writing the same day.
4. **Markup on a unit price is double-charging.** The unit price already carries it.
5. **Credits are not optional.** An owner who deletes work and sees no credit
   stops trusting every other line.
6. **"While we're in there" is still an owner request.** Price it, even if small;
   unpriced favours become expected.
7. **Code language is not yours to assert** unless you hold that license; say what
   the licensed trade or inspector said, and when.

## Example Output

```
## A. Notice to owner
Subject: Change Order #1 — hall bath remodel — decision needed by Thu 10:00

Hi Jordan,

With the old floor up, the subfloor around the toilet and tub has rotted through
in three places (photos 1–4). Your contract includes a price for this if we found
it: $360 per sheet. Three sheets: $1,080.

Under that subfloor, two floor joists are soft for about four feet (photos 5–6).
We can't set the new floor on them. We would add new lumber alongside each one
("sistering") so they carry the load again: $552. The building inspector will see
this at the framing inspection.

You asked for a recessed shelf in the tub wall, 12" × 24": $440.40.

You decided not to have the accent tile band. That comes off your price: −$244.80.
(The tile itself was inside your tile allowance and is settled when we reconcile
the allowance.)

Total for this change: $1,827.60. It adds 1.5 working days; new finish date
Tue 11-10.

Options: approve all four; approve the subfloor and joists and decide on the shelf
separately; or decline. The subfloor and joists can't be skipped — new tile over
them would crack — so declining those means the work stays stopped.
The bathroom is out of use until the floor is closed, so we need your decision by
Thursday 10:00 to keep the plumber's Friday slot.

To approve, sign the attached change-order form (the one from your contract).
— Alex Moreno, Moreno Renovation

## B. Pricing detail
| 1 | Subfloor, 3 sheets | Pre-priced (U1) | 3 × $360 unit price | — | incl. | $1,080.00 |
| 2 | Sister 2 joists | Concealed condition (contract §7.3 quoted in D) | 5 hr × $68 + $120 lumber/hangers = $460 | 20% | $92.00 | $552.00 |
| 3 | Shower niche | Owner-requested | 4 hr × $68 + $95 = $367 | 20% | $73.40 | $440.40 |
| 4 | Delete accent band | Deletion | −3 hr × $68 = −$204 | 20% | −$40.80 | −$244.80 |
CO total $1,827.60 · original $19,145.00 · prior COs $0 · new sum $20,972.60
New completion: Tue 11-10 midday (was end of Fri 11-06; +1.5 working days)

## C. Not billed (contractor's risk)
Wall out of plumb at tub (U3) — carried in contingency ($160); floated at our cost.

## D. Contract terms relied on (quoted) and questions for an attorney
§7.1 "No change shall proceed without a written change order signed by Owner and
Contractor, except in an emergency." §7.3 "Concealed conditions not reasonably
discoverable at the time of bid shall be treated as a change." §7.4 "Changes are
priced at cost plus 20% for overhead and profit."
Question: none — the clauses cover each item as quoted.

## E. Cross-check
1,080 + 552 + 440.40 − 244.80 = 1,827.60 ✓ · 19,145 + 1,827.60 = 20,972.60 ✓
Unit price not marked up twice ✓ · contingency item not billed ✓
```

## Techniques Used

- **NE-11 Embedded Calculation Formulas** — unit price, cost-plus, credit and contract-sum math.
- **RP-02 Audience-Specific Framing** — the owner reads what was found and what it costs, not clause numbers.
- **NE-17 Call-to-Action Mandatory Close** — options, consequences and a decision time.
- **QA-01 Self-Verification** — totals, markup and not-billed items cross-checked.

## Related Prompts

- `client-services-studio/skills/scope-ledger/SKILL.md` — detects drift from agreed
  scope; this prompt prices and communicates it.
- `domain-legal/contracts-transactional/legal_sow_drafter.md` — where a change-order
  procedure is written into a contract in the first place.
- `domain-specialized-fields/trades/trades_bid_estimate_with_contingency.md` — the
  unit prices, allowances and unknowns register this change is measured against.
