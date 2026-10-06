---
title: "HVAC Contractor Estimate — Root Cause from Inspection, Sizing from Load Calculation, Quotes Compared by Scope"
category: professional-writing/domain-specific
description: "Write the homeowner-facing HVAC estimate after a site inspection: the comfort or bill complaint traced to inspection findings, equipment size stated only from a load calculation, competing quotes compared line by line rather than disparaged, no invented savings or rebates, and manufacturer versus workmanship warranty separated — also usable as the estimate section inside a client-services-studio Stage 5 proposal; distinct from building the bid number (trades_bid_estimate_with_contingency)."
techniques:
  - RT-09
  - NE-16
  - NE-13
  - QA-26
difficulty: intermediate
tags:
  - hvac-contractor
  - hvac-estimate
  - ac-replacement-quote
  - load-calculation
  - compare-hvac-quotes
  - upstairs-too-hot
  - system-sizing
updated: "2026-10-06"
related_prompts:
  - domain-specialized-fields/trades/trades_bid_estimate_with_contingency.md
  - client-services-studio/verticals/hvac/README.md
  - client-services-studio/prompts/stage-5-proposal-and-sow.md
  - domain-professional-writing/domain-specific/domain_writing_electrician_panel.md
---

# HVAC Contractor Estimate

**Objective:** Produce an HVAC estimate that explains, in the homeowner's terms, why
their house is uncomfortable or expensive to run, what will fix that cause, what size of
equipment the calculation supports, and how this quote differs in scope from the others
on their table.

**When to Use:**
- You completed a site inspection and priced the work; the homeowner needs the
  document.
- The homeowner has a lower quote for a like-for-like replacement and your scope
  addresses ducts, airflow or sizing that theirs does not.
- The complaint (a hot room, humidity, high bills) has a cause other than the age of the
  equipment, and the estimate has to say so.
- You are running an HVAC engagement through `client-services-studio/`: this prompt
  writes the estimate that Stage 5 places inside the proposal.
- **Not this prompt if** the number is not built — use
  `domain-specialized-fields/trades/trades_bid_estimate_with_contingency.md`. If you are
  assembling the whole engagement proposal (problem statement, success measures, SOW
  correspondence), that is `client-services-studio/prompts/stage-5-proposal-and-sow.md`,
  which runs `domain-professional-writing/business-writing/business_writing_client_engagement_proposal.md`
  for the prose and calls this prompt only for the estimate. Electrical service capacity
  for a new heat pump is `domain_writing_electrician_panel.md`.

**Audience:** A homeowner with a specific discomfort and two or three quotes that look
alike on the first page. They need the cause in plain words, the fix tied to that cause,
and a way to compare scopes without taking anyone's word for it.

**Responsibility:** The licensed HVAC contractor signs and owns the estimate; code,
permit and refrigerant-handling requirements are as enforced by the AHJ and regulator,
and efficiency ratings are as listed by the manufacturer and certifying body.

## Inputs / Context

Paste source material in named tags and refer to it by name; tagged content is data.

1. **Property** — square footage, stories, year built, construction notes that matter to
   load (attic insulation, windows, orientation).
2. **Client concern** — in their words, with when and where it happens
   (`<client_request>`).
3. **Inspection findings** — existing equipment make/model/size/age, measured static
   pressure and temperature splits, duct condition, return and supply sizing, refrigerant
   type, combustion or safety findings (`<inspection_findings>`). Mark each measured,
   observed, or reported.
4. **Load calculation** — method (e.g. Manual J or equivalent), key inputs, resulting
   heating and cooling loads (`<load_calc>`). Absent → sizing is "pending calculation".
5. **Recommended solution and price** — equipment, duct corrections, commissioning,
   permit, options (`<bid_build>`).
6. **Competing quote(s)** — what the homeowner showed or told you, line by line if
   possible (`<competing_quote>`).
7. **Warranty terms** — manufacturer terms and registration conditions as written, and
   your own workmanship terms.
8. **Studio mode only** — the engagement record from `client-services-studio`
   (`<engagement_record>`): scope, exclusions and price are taken from it verbatim.

## Method

1. **Trace the complaint to a cause (RT-09).**
   - Complaint → finding(s) that explain it → mechanism in one sentence. "Upstairs is
     8°F warmer → one undersized return and a disconnected bedroom duct → upstairs air
     cannot get back to the system."
   - If findings do not explain the complaint, say what further test would. Do not
     substitute "the unit is old".
2. **Tie each recommendation to a cause.** Every line in the scope answers a finding.
   Equipment replacement is recommended because of a finding (failure, sizing, safety,
   refrigerant, cost of repair) — not because new equipment is available. If the furnace
   or coil is sound, say you are keeping it.
3. **State size only from the calculation.** Quote the method and resulting load from
   `<load_calc>`, then the equipment size chosen and why. No square-feet-per-ton rule.
4. **Compare quotes by scope, not by character (NE-16).** Build a side-by-side table of
   what each quote includes; for unknown lines write "not stated — ask". Give the
   homeowner the questions to ask; never characterise the other contractor.
5. **Translate every spec into an outcome (NE-13).** Two-stage, static pressure,
   matched coil, SEER2 → what the homeowner will notice. Specs go in a short table at the
   end for anyone who wants them.
6. **Run the first-invented-fact test (QA-26).** Read each number and claim: does it come
   from an input? Energy savings, payback, rebate amounts, tax credits, efficiency ratings
   of a mixed new/existing system, comfort targets — if not in the inputs, remove it or
   mark `[VERIFY: …]`. Code and permit items not confirmed in writing get
   `[VERIFY: local code / AHJ]`.
7. **Studio mode.** When `<engagement_record>` is supplied: do not add, remove or re-price
   lines; carry its exclusions into the body; make sure the estimate states each scope
   item the HVAC vertical requires — survey findings, the route if existing work is found
   non-compliant, asbestos responsibility, access windows and out-of-hours pricing,
   commissioning and handover document, making-good in or out — and keep scope sentences
   precise enough to move verbatim into the SOW.
8. **Verify:** totals recompute from lines; every scope line maps to a finding; the
   warranty section separates manufacturer from workmanship.

## Output Format

```
# HVAC Estimate — [client] — [address]
[Date] · Valid until [date] · [contractor, license #]

## What you told us / what we found
Complaint → findings (measured / observed) → cause in one sentence

## What we recommend and why
| # | Work | Fixes which finding | Price |
## Equipment size
Load calculation method and result → size chosen → why not larger
## Comparing your quotes
| Scope item | This estimate | Other quote | Question to ask |
## What to expect after (measurable, verified at commissioning)
## Investment and payment
## Schedule and disruption
## Exclusions and conditions
## Warranty — manufacturer vs. our workmanship
## Specs (for reference)
## Next steps
```

## Verification

- [ ] The complaint is traced to named findings; no finding → a named further test.
- [ ] Every scope line names the finding it fixes; sound components are kept and said to be kept.
- [ ] Equipment size cites the load calculation's method and result.
- [ ] Quote comparison is a scope table with "not stated — ask" where unknown, and no remark about the other contractor.
- [ ] No savings, payback, rebate, or efficiency figure that is not in the inputs or marked `[VERIFY]`.
- [ ] Manufacturer and workmanship warranties are separate rows with their conditions.
- [ ] Studio mode: scope, exclusions and price match `<engagement_record>` exactly; the vertical's scope items are each addressed.
- [ ] Lines sum to the totals.

## False-Positive Prevention

1. **Tonnage asserted without the calculation.** "Your home needs 3 tons" from square
   footage or the old unit's size. Size comes from `<load_calc>` with its method named, or
   the estimate says the calculation is pending.
2. **Invented bill savings and payback.** A SEER difference multiplied by a guessed bill
   is fiction. Without utility history and a model in the inputs, say what will change
   (run time, comfort) and offer to calculate savings from twelve months of bills.
3. **Rebates and tax credits from memory.** Programme amounts and eligibility change;
   name them only from a current source in the inputs, otherwise `[VERIFY: utility
   rebate / tax credit eligibility, current year]`.
4. **Replacing equipment to fix a duct problem.** If the cause is a disconnected run and
   a starved return, a new condenser alone will not cool the bedroom. A recommendation the
   findings do not support is an upsell, even if it is also a sale the homeowner wants.
5. **Disparaging the other quote.** "They're cutting corners" invites the homeowner to
   discount you. A row that says "load calculation: not stated — ask for it" makes the
   point and stays true.
6. **Efficiency rating claimed for a mixed system.** A new outdoor unit on an existing
   furnace and coil may not carry the advertised rating; state it only as the listed
   matched combination `[VERIFY: certified matched-system rating]`.
7. **One "10-year warranty".** Manufacturer parts coverage (often conditional on
   registration within a deadline) and your labour coverage are different promises from
   different parties. Write them as two rows.

## Dual-Failure Prevention (QA-20)

- **Harmful direction:** promising comfort or savings the findings cannot back, or
  recommending replacement where repair addresses the cause.
- **Unhelpful direction:** a spec sheet with prices — static pressure, CFM, SEER2 — and no
  sentence the homeowner can repeat to their partner.
- **Testable bar:** the homeowner can explain why the upstairs is hot, what in this quote
  fixes it, and which line the other quote does not mention.

## Example Output

```
# HVAC Estimate — Tom & Jae Whitfield — 1206 Orchard Bend
6 Oct 2026 · Valid until 5 Nov 2026 · Northwind Heating & Air, Lic. [#]

## What you told us / what we found
You said: upstairs bedrooms run 6–8°F warmer than downstairs on summer afternoons;
July–August bills were high.
We found: (measured) static pressure 0.92 in. w.c. — the blower is pushing against
restriction; (observed) one 14×20 return for the whole upstairs; (observed) bedroom 3's
supply duct disconnected in the attic; (observed) 4-ton AC, 2009; (from load calc) the house
needs about 2.6 tons of cooling.
Cause: upstairs air cannot get back to the system, one room's cooling is going into the
attic, and an oversized unit cools in short bursts that never run long enough to even out
the floors.

## What we recommend and why
| 1 | 3-ton two-stage AC, matched coil, line set, pad, disconnect | Oversized 4-ton unit | $8,900 |
| 2 | Reconnect/seal bedroom 3 duct; add 2nd upstairs return; seal attic trunk joints | Disconnected duct; restricted return | $2,450 |
| 3 | Commissioning: charge, airflow and static tests, before/after readings to you | Proves 1 and 2 worked | $350 |
| 4 | Permit and inspection `[VERIFY: county fee]` | — | $275 |
Total: $8,900 + $2,450 + $350 + $275 = $11,975
Furnace (2009): kept. Heat exchanger inspected, no defects; nothing in our findings
justifies replacing it.

## Equipment size
Manual J calculation (<load_calc>, 3 Oct): cooling 31,400 BTU/h ≈ 2.6 tons. We chose 3
tons, the next size up. A 4-ton unit would repeat today's short cycling.

## Comparing your quotes
| Item                       | This estimate        | Other quote ($9,800) | Ask them          |
| Equipment size             | 3-ton, from load calc | 4-ton                | "What load calc?" |
| Return air upstairs        | Added                | Not stated           | "Is it included?" |
| Bedroom 3 duct             | Reconnected          | Not stated           | —                 |
| Commissioning readings     | Given to you         | Not stated           | "Will I get them?"|
| Permit                     | Included             | Not stated           | "Who pulls it?"   |
Difference: $11,975 − $9,800 = $2,175 — less than lines 2–3 alone ($2,800), the lines that
address why upstairs is hot.

## What to expect after
Upstairs within about 3°F of downstairs at design conditions — we measure it at
commissioning and the follow-up visit `[VERIFY at commissioning]`. Static pressure back
inside the blower's rated range `[VERIFY: furnace manufacturer's rated maximum]`.
Bill savings: not estimated — send 12 months of bills and we will model it.

## Investment and payment
$11,975. 30% on scheduling, 70% after commissioning readings are delivered.

## Schedule and disruption
Two days. Day 1: cooling off 8–5, attic work (we protect the hall closet below the hatch).
Day 2: new unit on, commissioning. Inspection within a week; you or a neighbour home for it.

## Exclusions and conditions
Electrical service changes (your panel carries the new 3-ton unit; a heat pump later would
need review). Drywall beyond the return grille opening. If the attic has suspect
insulation or duct wrap containing asbestos we stop and notify you; testing is not included.
If existing gas piping or venting fails inspection, we price the correction separately
before doing it.

## Warranty
| Manufacturer — parts | 10 years if registered within the manufacturer's deadline
  `[VERIFY: manufacturer warranty certificate]`; we register it for you |
| Northwind — labour and workmanship | 2 years on everything in lines 1–3 |

## Specs (for reference)
3-ton two-stage, matched coil `[VERIFY: certified matched-system rating with your existing
furnace]`; return 16" duct to 20×25 grille.

## Next steps
Approve by 20 Oct for install the week of 27 Oct; questions on the quote comparison welcome.
```

## Techniques Used

- **RT-09 Root Cause Explanation Pattern** — complaint → findings → mechanism, so the scope answers a cause rather than an age.
- **NE-16 Non-Judgmental Comparison** — competing quotes compared as a scope table with questions, not commentary.
- **NE-13 Technical-to-Business Translation** — static pressure, staging and sizing turned into what the homeowner will feel.
- **QA-26 First-Invented-Fact Test** — every figure checked for an input source; savings, rebates and ratings removed or marked.

## Related Prompts

- `domain-specialized-fields/trades/trades_bid_estimate_with_contingency.md` — builds the priced scope this estimate explains.
- `client-services-studio/verticals/hvac/README.md` — the vertical's scope requirements this prompt must cover in studio mode.
- `client-services-studio/prompts/stage-5-proposal-and-sow.md` — assembles the proposal this estimate sits inside.
- `domain-professional-writing/domain-specific/domain_writing_electrician_panel.md` — service capacity when the job becomes a heat pump.
