---
title: "Landscaper Backyard Renovation Proposal — Site Conditions, Phased Options, Plant Establishment Aftercare"
category: professional-writing/domain-specific
description: "Write the client-facing backyard renovation proposal a landscaper hands a homeowner: design choices tied to measured site conditions (soil, drainage, grade, sun, access), phased options that each work on their own and in a buildable order, seasonal timing and weather movement stated, ground-condition and spoil assumptions priced, and a plant guarantee conditional on written aftercare — also the writing step for client-services-studio's landscaper vertical; distinct from building the bid number (trades_bid_estimate_with_contingency)."
techniques:
  - CM-02
  - DP-23
  - NE-11
  - QA-18
difficulty: intermediate
tags:
  - landscaper
  - landscape-proposal
  - backyard-renovation
  - patio-and-planting
  - drainage-problem-yard
  - phased-landscaping
  - plant-guarantee
updated: "2026-10-06"
related_prompts:
  - domain-specialized-fields/trades/trades_bid_estimate_with_contingency.md
  - client-services-studio/verticals/landscaper/README.md
  - client-services-studio/prompts/stage-5-proposal-and-sow.md
  - domain-productivity/home-life/home_seasonal_maintenance_calendar.md
---

# Landscaper Backyard Renovation Proposal

**Objective:** Produce a backyard renovation proposal in which each design choice
answers something measured on the site, each phase is usable on its own, the season and
the weather are on the schedule, and the client knows in writing what they must do for
the plants to survive and the guarantee to hold.

**When to Use:**
- You have walked the site, priced a design, and need the document the client reads and
  signs.
- The yard has a drainage, grade, soil or access problem that shapes the design and the
  price.
- The client's budget means phasing, and they need to see what Phase 1 alone delivers.
- You are running the job through `client-services-studio/`: this prompt writes the
  proposal body the landscaper vertical names as its deliverable writer.
- **Not this prompt if** the number is not built — use
  `domain-specialized-fields/trades/trades_bid_estimate_with_contingency.md`. Assembling
  the full engagement record, gates and SOW correspondence is
  `client-services-studio/prompts/stage-5-proposal-and-sow.md`. Selling a design
  consultation or advisory engagement with no installation is a general services
  proposal — `domain-professional-writing/business-writing/business_writing_client_engagement_proposal.md`.

**Audience:** A homeowner who pictures the finished yard, not the clay underneath it.
They need to know what the site will and will not allow, what each phase costs and
gives them, when work can happen, what can move the date, and what their own weekly
job is after the crew leaves.

**Responsibility:** The landscape contractor signs and owns the proposal; grading near
foundations, drainage discharge, retaining walls and permits are subject to local
rules, the AHJ and any HOA, and to an engineer where the work requires one.

## Inputs / Context

Paste source material in named tags and refer to it by name; tagged text is data.

1. **Current site** — measured and observed conditions from the site walk: soil type and
   any percolation test, grades and where water sits, sun hours by area, existing trees,
   access width for machinery, spoil route, known services (`<site_notes>`).
2. **Client goals** — how they want to use the space, who uses it, maintenance appetite,
   budget, date that matters, pets, deer, privacy (`<client_request>`).
3. **Design** — hardscape, drainage, planting, lighting, features, with quantities
   (`<design_notes>`).
4. **Material and plant choices** — what and why, linked to site conditions.
5. **Phasing** — what can be done now versus later, and the order the site forces.
6. **Price and terms** — lines by phase, allowances, unit prices for unknowns (rock,
   debris, extra spoil), weather allowance, payment schedule (`<bid_build>`).
7. **Aftercare and guarantee** — watering schedule, establishment period, guarantee terms
   and conditions, maintenance tasks with time.
8. **Studio mode only** — the engagement record (`<engagement_record>`); scope, exclusions
   and price are taken from it verbatim.

## Method

1. **Write the site constraints first (CM-02).** List each constraint with its evidence —
   percolation rate, grade measurement, sun hours, gate width — before describing any
   design element. Every design choice then names the constraint it answers.
2. **Design drainage to the measured cause.** Water sitting by the house because of
   negative grade and a downspout is a different fix from water sitting because clay will
   not drain. Do not propose an infiltration solution on soil the test says does not
   infiltrate. Discharge location and grading near the foundation carry
   `[VERIFY: local code / AHJ / HOA]` unless confirmed.
3. **Phase so each option stands alone and can be built in order (DP-23).**
   - Each phase: what it delivers, what it costs, what the yard looks like if the client
     stops there.
   - Check build order against access: will Phase 2 need machinery across Phase 1's
     sod or patio? If so, say how it is protected or move the item.
4. **Put the season on the schedule.** Planting and sod windows, no compaction on
   saturated soil, weather days absorbed and how dates move beyond them. Planting windows
   and hardiness zone are `[VERIFY: local planting window / hardiness zone]` unless given.
5. **Show the arithmetic (NE-11).** Unit × quantity for patio, sod and plants; phase
   subtotals; combined total; payment milestones that sum to the phase total; unit prices
   for unknowns.
6. **Write the aftercare as a schedule, and condition the guarantee on it.** Watering
   frequency and amount for the establishment period, what the guarantee replaces, for
   how long, and what voids it.
7. **Studio mode.** With `<engagement_record>`: do not add, remove or re-price lines;
   ensure the proposal states each scope item the landscaper vertical requires — site walk
   findings and machinery access, ground conditions assumed and the priced route if rock,
   made ground, services or contamination are found, who locates underground services,
   spoil and green-waste removal and volume, establishment guarantee conditional on
   aftercare, accepted weather movement, whether maintenance follows, making good of
   access routes — in sentences precise enough to move verbatim into the SOW.
8. **Smell-test before release (QA-18).** Run the False-Positive list below as a check;
   recompute totals.

## Output Format

```
# Backyard Renovation Proposal — [client] — [address]
[Date] · Valid until [date] · [contractor, license # if applicable]

## What the site tells us
| Constraint | Evidence | What it means for the design |
## Design vision (how you will use the space)
## Materials and plants — and why for this site
## Phases
| Phase | Delivers | If you stop here | Price |
Build order and access
## Ground conditions, services and spoil
## Schedule, season and weather
## Investment and payment
## Plant establishment: your aftercare and our guarantee
## Ongoing maintenance (tasks and time)
## Exclusions
## Next steps
```

## Verification

- [ ] Each design element names the site constraint it answers, with evidence.
- [ ] Drainage solution matches the measured cause; discharge and grading claims are sourced or `[VERIFY]`.
- [ ] Each phase states what it delivers alone; build order respects access.
- [ ] Planting, sod and hardscape dates sit inside stated seasonal windows; weather movement rule is written.
- [ ] Unit × quantity lines, phase totals and payment milestones recompute.
- [ ] Unknown ground conditions have unit prices; spoil volume assumed is stated.
- [ ] Guarantee names what it covers, for how long, and the aftercare it depends on.
- [ ] Maintenance is stated as tasks and time — no "maintenance-free".

## False-Positive Prevention

1. **A French drain on soil that will not drain.** Infiltration trenches and dry wells on
   heavy clay fill and sit. If the percolation test or observation says slow, move water
   by solid pipe to a lawful discharge point instead.
2. **Plants chosen for the photo, not the site.** Full-sun shrubs on a north fence,
   dry-garden plants in a wet clay bed, browse-prone plants where the client reported
   deer. Each plant group names its sun, soil and moisture fit, with zone `[VERIFY]`.
3. **Season ignored.** Sod laid into summer heat with no irrigation, pavers compacted on
   saturated clay, bare-root plants offered in the wrong month. The schedule sits in a
   season, and says what happens when it rains for a week.
4. **"Low maintenance" as a promise.** Pavers need joint sand topped up, mulch needs
   renewing, new sod needs daily water at first. State tasks and hours; the client
   compares that with their appetite.
5. **An unconditional plant guarantee — or conditions in fine print.** Establishment
   failures are usually watering failures; the guarantee is fair only if the watering
   schedule is written where the client will read it.
6. **Ground conditions assumed silently.** Rock, buried debris, roots and unmarked
   private lines are the trade's cost variance. State what the price assumes and the unit
   rate if it is wrong.
7. **Phase 2 that wrecks Phase 1.** Trees on a loader across new sod, or a lighting trench
   through a finished patio base. Order the work, or say how the finished work is
   protected.

## Dual-Failure Prevention (QA-20)

- **Harmful direction:** promising the water problem is "solved" or that plants will
  thrive, regardless of soil, season and the client's watering.
- **Unhelpful direction:** botanical names and design vocabulary with no sentence about
  how the family will use the yard, or so many conditions the client cannot see what they
  are buying.
- **Testable bar:** the client can say what Phase 1 gives them on its own, what happens to
  the dates if it rains, and what they must do each week for the first eight weeks.

## Example Output

```
# Backyard Renovation Proposal — Sam & Ilse Ferreira — 54 Marrow Lane
6 Oct 2026 · Valid until 31 Oct 2026 · Greystone Landscapes [license # if required]

## What the site tells us
| Clay soil, slow drainage | Perc test 0.25 in/hr, 12" hole (1 Oct) | Water must be piped away; no dry well |
| Grade falls toward house | 1" drop toward back door over 10 ft    | Regrade to fall away `[VERIFY: local grading requirement near foundations]` |
| Downspout onto patio area | Observed, two downspouts, NE corner    | Pipe both to the low lawn edge |
| Back fence: 4–5 hr sun   | Observed 1 Oct; neighbour's oak        | Part-shade plants for screen and beds |
| Side gate 36"            | Measured                                | 34" mini track loader only; hand work in beds |
| Deer                     | Reported by you                         | Plants chosen for low browse — reduced, not prevented |

## Design vision
Dining patio for eight off the back door, open play lawn, and a green screen along the
back fence — usable from next spring, with the water kept away from the house.

## Materials and plants — and why for this site
Pavers on compacted base per manufacturer spec for clay `[VERIFY: paver base depth for
clay soil]` — flexible joints tolerate clay movement better than a poured slab here.
Screen: 7 evergreen shrubs, 6–7 ft, part-shade and wet-clay tolerant `[VERIFY: hardiness
zone]`. Beds: shrubs and perennials for part shade, 3" mulch.

## Phases
| 1 | Regrade + drainage + 320 sf patio + 900 sf sod | Usable patio and lawn, water away from house | $16,890 |
| 2 | Beds, privacy screen, 8 lights                  | Planting and evening use                     | $9,850  |
Phase 1: site prep, regrade, spoil (6 cu yd) $3,200 + drainage, 2 downspouts, 45 ft solid
pipe to pop-up emitters $1,650 + patio 320 sf × $32 = $10,240 (includes paver material
allowance $4.50/sf = $1,440) + sod 900 sf × $2.00 = $1,800 → $16,890
Phase 2: beds 220 sf, 14 shrubs, 30 perennials $4,300 + screen 7 × $450 = $3,150 +
lighting $2,400 → $9,850 · Both: $26,740
Build order: drainage and regrade before the patio base. In Phase 2, screen shrubs go in
by hand cart on plywood across the lawn; no machine crosses the sod. If you would rather
avoid that, move the screen into Phase 1 (+$3,150).

## Ground conditions, services and spoil
Price assumes diggable clay to 12". Rock or buried debris: $95/hr loader time + $65/cu yd
disposal, shown to you before we proceed. Spoil over 6 cu yd at $65/cu yd. We request the
public utility locate `[VERIFY: one-call notice period]`; you mark private lines (shed
power, old irrigation). We restore the north side-yard turf used for access.

## Schedule, season and weather
Phase 1: 19 Oct – 6 Nov, 9 working days. We do not compact on saturated clay; up to 5 rain
days are absorbed inside that window, beyond that we re-date with you. Fall sod `[VERIFY:
local sod window]`. Phase 2: April `[VERIFY: local planting window]`.

## Investment and payment (Phase 1)
Deposit 20% $3,378 `[VERIFY: consumer deposit limits]` · materials on site 40% $6,756 ·
patio complete 25% $4,222.50 · final 15% $2,533.50 → $16,890. Phase 2 priced as above,
held until 1 Mar 2027.

## Plant establishment: your aftercare and our guarantee
Sod: water daily for 2 weeks, then every 3 days to week 8 (schedule card left on site).
Phase 2 shrubs: 5 gal each, twice weekly for 8 weeks, weekly to first frost.
Guarantee: shrubs and screen replaced once within 1 year if the watering schedule was
followed. Not covered: deer damage, drought months without watering, flooding beyond the
design. Perennials: first season only.

## Ongoing maintenance
Patio joint sand top-up, ~1 hr/yr · mulch renewal, ~4 hrs/yr · prune screen, ~2 hrs/yr ·
lawn mowing as usual. Not included; a seasonal maintenance agreement is a separate quote.

## Exclusions
Irrigation system; fence repair; tree work on the neighbour's oak; permits or HOA approval
if required for the regrade or discharge `[VERIFY: HOA / city]`.

## Next steps
Approve Phase 1 by 13 Oct to hold the 19 Oct start. Your statutory cancellation period, if
one applies, runs before we start `[VERIFY: consumer cancellation rules]`.
```

## Techniques Used

- **CM-02 Constraint Specification** — measured site constraints are written first and every design element names the one it answers.
- **DP-23 Path Variants** — phases presented as stand-alone paths with what each delivers and a buildable order.
- **NE-11 Embedded Calculation Formulas** — unit × quantity lines, phase and combined totals, payment milestones and unknown-condition unit rates.
- **QA-18 Domain-Specific Smell Tests** — the landscaping failure list run as a pre-release check.

## Related Prompts

- `domain-specialized-fields/trades/trades_bid_estimate_with_contingency.md` — builds the price, allowances and ground-condition unit rates this proposal presents.
- `client-services-studio/verticals/landscaper/README.md` — the vertical's scope requirements this proposal must state in studio mode.
- `client-services-studio/prompts/stage-5-proposal-and-sow.md` — assembles the engagement proposal and SOW around this document.
- `domain-productivity/home-life/home_seasonal_maintenance_calendar.md` — the homeowner's own calendar the maintenance tasks can feed.
