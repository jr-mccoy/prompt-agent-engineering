---
title: "Plumber Repiping Estimate — Repipe vs Continued Repairs, Disruption by Day, Split Warranties"
category: professional-writing/domain-specific
description: "Write the homeowner-facing whole-house repipe estimate: the recommendation grounded in leak history, cut samples and flow readings rather than house age; full, partial and keep-repairing options compared on the homeowner's own repair costs; water-off hours and wall openings listed by day and room; and pipe-manufacturer warranty kept separate from the plumber's workmanship — distinct from building the bid number (trades_bid_estimate_with_contingency) and from a repipe discovered mid-remodel (trades_change_order_pricing_notice)."
techniques:
  - RT-08
  - NE-27
  - RP-02
  - QA-01
difficulty: intermediate
tags:
  - plumber
  - repiping-estimate
  - whole-house-repipe
  - galvanized-pipe-replacement
  - pex-vs-copper
  - keep-getting-leaks
  - water-off-during-repipe
updated: "2026-10-06"
related_prompts:
  - domain-specialized-fields/trades/trades_bid_estimate_with_contingency.md
  - domain-specialized-fields/trades/trades_change_order_pricing_notice.md
  - domain-professional-writing/domain-specific/domain_writing_contractor_remodel.md
---

# Plumber Repiping Estimate

**Objective:** Give a homeowner a repipe estimate that shows from their own house why
replacement beats another round of repairs (or says when it does not), what each option
costs, exactly what the job does to their water supply and walls, and what each
warranty covers and who honours it.

**When to Use:**
- The homeowner has had repeated leaks, discoloured water or falling flow and you
  have inspected the supply piping.
- You are recommending a full repipe and the homeowner's alternative is "just fix this
  leak".
- You offer more than one pipe material, or a partial repipe, and need to lay them side
  by side.
- **Not this prompt if** the number is not built — use
  `domain-specialized-fields/trades/trades_bid_estimate_with_contingency.md`. If the
  corroded supply was found while you or another trade were opening walls for a remodel,
  price and notify it with `domain-specialized-fields/trades/trades_change_order_pricing_notice.md`;
  if the repipe is one scope line in a general contractor's remodel, it belongs in
  `domain-professional-writing/domain-specific/domain_writing_contractor_remodel.md`.

**Audience:** A homeowner who has paid for several leak repairs, is wary of a
five-figure number, and is anxious about holes in walls and days without water. They
need evidence from their own pipes, a fair middle option, and a day-by-day picture.

**Responsibility:** The licensed plumber signs and owns the estimate; approved
materials and installation methods are those enforced by the AHJ, and pipe warranty
terms are the manufacturer's.

## Inputs / Context

Paste source material in named tags and refer to it by name; tagged text is data.

1. **Property** — age, square footage, stories, foundation (slab, crawlspace,
   basement), current pipe material(s), fixture count, water-heater age and location.
2. **Client's problem** — leaks, water colour, pressure or flow complaints, in their
   words, with dates (`<client_request>`).
3. **Assessment** — leak history with dates and repair invoices, cut-sample observations,
   measured static pressure and flow, visible corrosion, mixed metals, access routes
   (`<inspection_findings>`). Mark each measured, observed, or reported.
4. **Options and price** — full repipe by material, partial repipe, wall openings and
   patching, permit, fixture valves, what is excluded (`<bid_build>`).
5. **Disruption plan** — days, water-off windows, rooms opened and number of openings,
   overnight water restoration, inspection timing, who patches and who paints.
6. **Warranty terms** — manufacturer's terms as written and your own workmanship terms.

## Method

1. **Ground the recommendation in this house (RP-02).** Lead with the homeowner's
   problem in their words, then the findings that explain it: leak dates, cut-sample
   condition, measured flow. Age and pipe material are context, not proof.
2. **Compare options on the homeowner's own costs (RT-08).**
   - *Keep repairing*: past repair spend from their invoices, per year; what each repair
     leaves in place; that the next leak's location and timing are unknown.
   - *Partial repipe*: what it replaces, what corroded pipe remains and where.
   - *Full repipe*: what is replaced end to end.
   - Do not invent failure probabilities or future leak counts.
3. **Frame the cost of waiting with what is known (NE-27).** Past rate of repairs and
   what a leak in a finished room damaged last time — from the inputs. No hypothetical
   flood figures.
4. **Make disruption concrete.** By day: water-off hours, whether water is back
   overnight, rooms entered, number and size of wall or ceiling openings, furniture to
   move, dust control, inspection before closing walls. Say who patches, and whether
   painting is in or out.
5. **Separate the warranties.** Manufacturer pipe and fitting coverage with its
   conditions (installer, fitting system); your workmanship coverage; what neither
   covers (fixtures not replaced, the service line, the water heater).
6. **Mark what you cannot assert.** Material approval and installation limits, permit
   requirements and fees, hazardous-material rules for old pipe wrap — from
   `<inspection_findings>` or `[VERIFY: local code / AHJ]`. Water-quality improvement is
   stated as expected, with the other possible sources named.
7. **Verify before release (QA-01).** Each option's total recomputes from its lines; the
   repair-history arithmetic matches the invoices; every finding cited is in the inputs;
   the disruption schedule matches the bid's days.

## Output Format

```
# Repiping Estimate — [client] — [address]
[Date] · Valid until [date] · [plumber, license #]

## Your situation
What you told us · what we found (measured / observed) · what it means

## Your options
| Option | What it replaces | What it leaves | Price |
Repair history: [n] repairs, $[..] over [months] → $[..]/yr

## Our recommendation and why
## Scope of work (recommended option)
## Day by day: water, walls, rooms
## Investment and payment
## Exclusions
## Warranty — manufacturer vs. our workmanship
## What this will and will not change
## Next steps
```

## Verification

- [ ] The recommendation cites leak history, cut-sample or flow findings — not age alone.
- [ ] A partial or keep-repairing option is shown with what it leaves in place.
- [ ] Repair-history arithmetic matches the invoices supplied.
- [ ] Each day lists water-off hours, rooms, openings, and overnight water status.
- [ ] Painting, the service line and the water heater are explicitly in or out.
- [ ] Manufacturer and workmanship warranties are separate, each with conditions.
- [ ] Material approvals, permits and fees are sourced or carry `[VERIFY: …]`.
- [ ] Option totals recompute from their lines.

## False-Positive Prevention

1. **"Your pipes are 60 years old" as the case for repiping.** Age predicts nothing about
   this house's next leak. Cite the three leak dates, the cut sample and the flow reading;
   if you have none of those, the estimate should recommend a closer inspection first.
2. **Full repipe versus doing nothing.** Omitting a partial repipe — main trunk plus the
   worst branches — when the findings support it turns a recommendation into an
   ultimatum.
3. **"Minimal disruption".** Nine openings in three rooms and two days without water
   during working hours is the honest version; the homeowner who was told "minimal"
   remembers the nine holes.
4. **Drywall "repaired" with painting silently excluded.** Patch-and-prime versus
   patch-and-paint is the dispute at final payment. Say which.
5. **One warranty number for everything.** A long manufacturer warranty on PEX pipe
   covers the pipe under its conditions; your workmanship term covers your joints and
   labour; neither covers the old faucet you reconnected.
6. **Water quality and pressure promised.** New pipe removes corrosion from the pipe it
   replaces; it does not change municipal supply pressure, a sediment-filled water heater,
   or the unreplaced service line. Say "expected to improve" and name the other sources.
7. **Material approval from memory.** Whether PEX, CPVC or a given fitting system is
   approved for this use and location, and how it must be supported and protected, is a
   local question — `[VERIFY: local code / AHJ]`.

## Dual-Failure Prevention (QA-20)

- **Harmful direction:** warning of a ceiling collapse the findings do not suggest, or
  downplaying days without water to close the sale.
- **Unhelpful direction:** PEX-A versus PEX-B, expansion versus crimp fittings, and pipe
  schedules with no sentence about what changes in the homeowner's week.
- **Testable bar:** the homeowner can say which days they will be without water and
  when, how many holes in which rooms and who paints them, and what to do if a joint
  leaks in year three.

## Example Output

```
# Repiping Estimate — Marguerite Okafor — 2290 Ellery St
6 Oct 2026 · Valid until 5 Nov 2026 · Clearline Plumbing, Lic. [#]

## Your situation
You told us: three leaks since April 2025, rusty water first thing in the morning, weak
shower flow.
We found: (records) leaks Apr 2025 laundry, Nov 2025 hall wall, Jun 2026 crawlspace —
your invoices total $1,150; (observed) the pipe section cut out in June is narrowed by
rust to roughly half its opening (photo 2); (measured) shower flow 2.1 gpm, static
pressure 62 psi at the hose bib — pressure arriving is fine, the pipes are restricting it.
All supply piping is 1958 galvanized steel, routed through the crawlspace.

## Your options
| A Full repipe, PEX-A   | All supply to 14 fixtures; new main shutoff | Nothing galvanized | $10,040 |
| B Full repipe, copper  | Same                                        | Nothing galvanized | $14,690 |
| C Partial, PEX-A       | Main trunk + bath and kitchen branches      | Laundry and hose-bib branches (galvanized) | $6,040 |
| D Keep repairing       | The leaking section each time               | Everything else    | ~$400 per repair |
Repair history: 3 repairs, $1,150 over 18 months → about $770/yr ($1,150 ÷ 1.5), not
counting the hall-wall drywall you paid separately. Past rate is not a forecast; we cannot
tell you when or where the next leak will be.

## Our recommendation and why
Option A. All three leaks and the narrowed sample came from the same galvanized system, so
each repair replaces a foot and leaves the rest. Copper (B) is a sound choice; for a
crawlspace house the extra $4,650 buys you little here. If budget decides, C removes the
pipe behind your worst flow and two of the three leak sites; the laundry branch stays.

## Scope of work (Option A)
| 1 | PEX-A supply to 14 fixtures via crawlspace; new main shutoff; 14 new fixture valves;
     water-heater connections `[VERIFY: local code / AHJ — PEX approval and support]` | $8,450 |
| 2 | 9 wall openings, patched, textured, primed (not painted)                           | $1,350 |
| 3 | Permit and inspection `[VERIFY: city fee]`                                         | $240   |
Total: $8,450 + $1,350 + $240 = $10,040 (B: $13,100 + $1,350 + $240; C: $5,200 + $600 + $240)

## Day by day
Day 1 (Tue): water off 8:00–5:00; crawlspace and kitchen (2 openings), laundry (2).
  Water back on overnight.
Day 2 (Wed): water off 8:00–5:00; bathroom (3 openings), hall (2). Water on overnight.
Day 3 (Thu): inspection before walls close; patching. Water on all day.
Move items from under the kitchen sink, the hall closet and the laundry shelf before Day 1.
We tent each opening and vacuum daily.

## Investment and payment
Option A $10,040: 25% at permit issue, 50% after inspection passes, 25% after patching.

## Exclusions
Painting. The service line from the meter to the house (outside, not inspected). The
water heater itself (12 years old; we connect to it, not replace it). Old pipe wrap in the
crawlspace that may contain asbestos: we leave it undisturbed and abandon that pipe in
place; testing not included `[VERIFY: local rules for abandoned wrapped pipe]`.

## Warranty
| Pipe and fittings — manufacturer | Long-term limited warranty when installed with their
  fitting system by a licensed plumber `[VERIFY: manufacturer warranty document]` |
| Clearline — workmanship          | 5 years on every joint and connection we make; call us
  first, we come out |
| Drywall patches — Clearline      | 1 year against cracking |
| Not covered by either            | Faucets and fixtures we reconnect but do not replace |

## What this will and will not change
Should improve: flow at the shower and kitchen; rusty first-draw water from the pipes.
Will not change: supply pressure (already 62 psi). If discoloured water continues, the
water heater is the next suspect — we flush it on Day 3 and can test after.

## Next steps
Pick A, B or C by 20 Oct; we file the permit and confirm the Tuesday start.
```

## Techniques Used

- **RT-08 Workaround Cost Analysis** — the keep-repairing path priced from the homeowner's own invoices, beside partial and full repipe.
- **NE-27 Cost of Inaction Framing** — cost of waiting stated only from known repair history, with the explicit caveat that the past rate is not a forecast.
- **RP-02 Audience-Specific Framing** — the case is built from this house's leaks and readings, in the homeowner's terms, not pipe-material doctrine.
- **QA-01 Self-Verification** — option totals, repair arithmetic, disruption days and `[VERIFY]` markers checked before release.

## Related Prompts

- `domain-specialized-fields/trades/trades_bid_estimate_with_contingency.md` — prices the options and the unknowns (e.g. a slab run, a hidden branch) this estimate presents.
- `domain-specialized-fields/trades/trades_change_order_pricing_notice.md` — when corroded supply is found mid-job on other work, or an extra branch is found during the repipe.
- `domain-professional-writing/domain-specific/domain_writing_contractor_remodel.md` — when the repipe rides inside a general contractor's remodel estimate.
