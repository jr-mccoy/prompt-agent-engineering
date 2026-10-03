---
title: "First-Time DIY Repair Triage — Can I Fix This Myself, What Will It Take, and When to Call a Licensed Pro"
category: productivity/home-life
description: "Help a homeowner or renter with little repair experience sort each household problem into emergency now, call a licensed professional, DIY with care, or straightforward DIY — using hard stops that are never DIY (gas, electrical panel and service work, structural signs, suspected asbestos or lead paint, work at height on roofs, carbon-monoxide alarms), a cost-of-a-mistake test, permit, warranty and lease checks, and for each DIY item the skills, tools and shut-offs it needs; for each pro item, which trade to call and how to describe the problem."
techniques:
  - DP-28
  - DP-05
  - DS-26
  - DP-13
  - QA-12
difficulty: beginner
tags:
  - home-repair
  - diy
  - homeowner
  - renter
  - when-to-hire-a-pro
  - home-safety
  - can-i-fix-this-myself
  - first-home-repairs
  - do-i-need-an-electrician
updated: "2026-10-03"
related_prompts:
  - domain-productivity/home-life/home_small_repair_walkthrough.md
  - domain-productivity/home-life/home_seasonal_maintenance_calendar.md
  - domain-productivity/home-life/home_appointment_prep.md
---

# First-Time DIY Repair Triage

**Objective:** For each problem in the house, give a clear verdict — emergency, call a
pro, DIY with care, or simple DIY — with the reason, what doing it yourself would take,
what a mistake would cost, and, where a pro is needed, which one and what to tell them.

**When to Use:**
- You have just moved into your first home or flat and things are breaking.
- You have a list of small problems and do not know which you can handle.
- Something looks or smells wrong and you are not sure whether it is urgent.
- You want to avoid both paying a pro for a five-minute fix and making a small problem worse.
- **Not this prompt if** you have already decided to do a specific fix and want the steps —
  `home_small_repair_walkthrough.md`. For a recurring maintenance calendar,
  `home_seasonal_maintenance_calendar.md`. If you are a contractor pricing a job, that is
  trade-side work in `domain-specialized-fields/trades/trades_bid_estimate_with_contingency.md`.
  If a contractor's work was defective, `domain-written-advocacy/products-and-warranty/advocacy_service_nonperformance_demand.md`.

**Audience:** Homeowners and renters with little or no repair experience. Codes, permits and
licensing rules vary by place; every such point is marked for local verification.

## Inputs / Context

1. **Each problem:** what you see, hear or smell; where; since when; getting worse or stable.
2. **Active signs:** water actively leaking, sparks, burning smell, warm switch plates or
   outlets, gas smell, alarms sounding, cracks that are new or growing.
3. **The home:** owner or renter; approximate build year (affects asbestos and lead risk);
   house, flat or condo (shared systems may belong to the building).
4. **Your experience and tools:** what you have done before; what tools you own.
5. **Warranty and insurance:** new appliances, home warranty, recent contractor work.
6. **Budget and time pressure.**

## Method

1. **Emergency screen first.** Before anything else:
   - **Smell of gas** → do not switch anything on or off; leave; call the gas utility's
     emergency line or emergency services from outside `[VERIFY: your local number]`.
   - **Carbon-monoxide alarm** → get everyone out into fresh air; call emergency services.
   - **Sparks, smoke, burning smell, a hot outlet or switch** → switch off at the breaker if
     safe to reach, otherwise leave and call; then an electrician.
   - **Water near electrics, or a burst pipe** → shut off the main water valve and power to the
     affected area if safe; then call.
2. **Apply the hard stops (DP-05).** Never DIY, whatever your confidence:
   - Any gas line, gas appliance connection or venting.
   - Electrical panel, service entrance, new circuits, or aluminium/knob-and-tube wiring.
   - Structural signs: sagging ceilings or beams, doors that suddenly stick across a whole
     wall, foundation cracks wider than about ¼ inch (6 mm), stair-step cracks in masonry, or
     any crack that is growing; any change to a possibly load-bearing wall.
   - Suspected asbestos (common in homes built before the 1980s — textured "popcorn" ceilings,
     old vinyl tiles, pipe and boiler insulation): do not drill, sand or scrape; have it tested.
   - Lead paint (US homes built before 1978 are the usual flag): no sanding, scraping or heat
     stripping; use lead-safe certified contractors `[VERIFY locally]`.
   - Roof work and anything needing a ladder above a single storey.
   - Mould covering more than about 10 square feet (roughly 1 m²), or mould with water damage
     you cannot trace.
3. **Score the rest (DP-28).** For each remaining problem, rate four things: risk to people if
   done wrong; cost of a mistake (a flooded floor costs far more than a new faucet); whether it
   needs a permit or licence `[VERIFY locally]`; and whether you have the skill and tools.
   Verdicts: **Call a pro** (any high-risk or high-mistake-cost item, or a permit you cannot
   pull) · **DIY with care** (needs a shut-off and a test — e.g. swapping a light fixture
   like-for-like with power off at the breaker and verified dead) · **Simple DIY** (low risk,
   reversible — running toilet, clogged sink, sticking door, small drywall hole, re-caulking).
4. **Check the paperwork.** Renters: most repairs are the landlord's — report in writing.
   Warranties: DIY can void them — claim first. Condos: pipes and wiring may be the building's.
5. **Set safe defaults for DIY items (DS-26).** Shut-off located and tested before starting;
   power verified off with a non-contact tester; photos before you take anything apart; one
   job at a time; stop by early evening so a pro or shop is still reachable.
6. **Name the stop signals (DP-13).** For each DIY item, what means "stop and call": a valve
   that won't turn or starts leaking, wiring that doesn't match what you expected, a fix that
   needs "just a bit of force", or a problem that comes back within a week.
7. **Brief the pro.** For each pro item: which trade (plumber, electrician, gas engineer,
   structural engineer, roofer, asbestos surveyor), what to tell them (symptoms, since when,
   photos, what you tried), and questions to ask (licence, insurance, permit, written quote);
   `home_appointment_prep.md` prepares the visit.
8. **Check for false confidence (QA-12).** A video making it look easy is not evidence you
   can do it; a fix that "worked" may have hidden the symptom.

## Output Format

```
# Repair triage — [home], [owner/renter], built ~[year], [date]
## Emergency screen: [clear / ACTION NOW: …]
## Triage table
| Problem | Verdict | Why | Cost of a mistake | Permit/warranty/lease | Next step |
## DIY items: skills · tools to buy/borrow · shut-offs · stop signals
## Pro items: trade · what to tell them · questions to ask
## Renter/warranty items: who to notify, in writing
```

## Verification

- [ ] Emergency screen completed before any DIY advice.
- [ ] Every hard-stop category checked and none given a DIY verdict.
- [ ] Each DIY item has its shut-off, verification step and stop signals.
- [ ] Cost of a mistake is stated, not just cost of the fix.
- [ ] Permits, codes and licensing marked [VERIFY locally]; renter and warranty items routed.
- [ ] Each pro item names the trade and a problem description.

## False-Positive Prevention

1. **"It's just a switch."** A warm switch plate or flicker across a room is a wiring fault
   signal, not a bulb problem.
2. **Cheap fix, expensive failure.** A $15 faucet cartridge done wrong can mean a $3,000 floor;
   weigh the downside.
3. **Hairline vs. growing cracks.** A stable hairline crack above a door is usually settling;
   mark its ends with a pencil and date — if it grows, call.
4. **Old house, invisible hazards.** Asbestos and lead look like ordinary materials.
5. **Renters fixing landlord problems.** You may bear the cost and lose the record.
6. **Video confidence.** Watching is not doing; start with the simplest items.

## Example Output

```
# Repair triage — 1962 bungalow, owner (first home), 2026-10-04
## Emergency screen: clear (no gas smell, no alarms, no active water)

| Running toilet, hall bath | Simple DIY | flapper or fill valve; water off at the toilet
  valve | low — at worst a wet floor | none | home_small_repair_walkthrough (flapper) |
| Kitchen lights flicker; switch plate warm | Call a pro — electrician | heat at a switch =
  loose or failing connection; 1962 wiring may be aluminium | fire | permit likely
  [VERIFY] | stop using the switch; book this week |
| Bathroom ceiling: textured, cracked near fan | Call a pro — asbestos test first | pre-1980s
  texture; fan replacement would disturb it | health | — | lab test before any work |
| Slow bathroom sink | Simple DIY | hair clog; plunger or drain snake, no chemical drain cleaners
  with a plunger | low | none | this weekend |
| Hairline crack above bedroom door | Monitor | likely settling | low now | — | pencil ends,
  date; re-check monthly; call a structural engineer if it lengthens |
| Back door sticks at top | Simple DIY | tighten top hinge screws (longer screw into frame) | low |
  none | 15 minutes |

## Pro brief — electrician: "Kitchen ceiling lights flicker for 2 weeks; the 3-way switch plate
  by the back door feels warm; house built 1962. Ask: licensed? permit needed? check for
  aluminium branch wiring?"
```

## Techniques Used

- **DP-28 Traffic-Light Verdict System** — four verdicts with explicit criteria.
- **DP-05 Stakes-Based Gate Policy** — hard stops that no confidence level overrides.
- **DS-26 Safe Defaults Pattern** — shut-off, verify-dead and photo-first defaults.
- **DP-13 Kill Signal Definition** — observable signs to stop and call a pro.
- **QA-12 False Positives Identification** — easy-looking fixes and hidden-symptom "successes".

## Related Prompts

- `home_small_repair_walkthrough.md` — step-by-step for one DIY item from this triage.
- `home_seasonal_maintenance_calendar.md` — preventive tasks so fewer things break.
- `home_appointment_prep.md` — preparing for a contractor's visit and estimate.
