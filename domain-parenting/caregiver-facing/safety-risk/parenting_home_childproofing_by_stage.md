---
title: "Home Childproofing by Stage — Severity-Ranked Hazard Audit From Newborn to School Age: Sleep, Water, Furniture Tip-Over, Poisons, Button Batteries, Windows, Firearms"
category: parenting/safety-risk
description: "Run a room-by-room childproofing audit matched to the child's current and next developmental stage (newborn, roller/crawler, cruiser/walker, climber, preschooler, school age), ranking fixes by severity × likelihood so the deadly-but-quiet hazards — unsafe sleep, water, firearms, tip-overs, button batteries and magnets, medications and edibles, window falls — are fixed before the noisy-but-minor ones."
techniques:
  - RT-02
  - ST-02
  - IT-22
  - QA-02
difficulty: beginner
intended_use: model-testing
tags:
  - parenting
  - safety-risk
  - childproofing
  - injury-prevention
  - safe-sleep
  - furniture-anchoring
  - poison-prevention
  - baby-proofing-checklist
  - toddler-getting-into-everything
updated: "2026-10-02"
related_prompts:
  - domain-parenting/caregiver-facing/ages-0-3/parenting_when_pediatrician_visit_0_3.md
  - domain-parenting/caregiver-facing/safety-risk/parenting_other_homes_safety_questions.md
  - domain-parenting/caregiver-facing/ages-0-3/parenting_starting_solids_planner.md
---

# Home Childproofing by Stage

**Objective:** Produce a prioritised childproofing plan for one home and one child:
hazards ranked by severity × likelihood for the child's current stage and the next
one, specific fixes with costs and dates, and a re-audit trigger.

**When to Use:**
- Expecting a baby, or a baby is about to roll, crawl, pull up, or climb.
- Moving into a new home, or a grandparent's home will host a young child.
- After a near miss (a fall, an ingestion, a tip-over).
- **Not this prompt if** you are vetting **someone else's** home for a visit — use
  `domain-parenting/caregiver-facing/safety-risk/parenting_other_homes_safety_questions.md`.
  If a child has already swallowed or been injured, use
  `domain-parenting/caregiver-facing/ages-0-3/parenting_when_pediatrician_visit_0_3.md`
  (or call Poison Help / 911). Choking during meals and food sizing are in
  `domain-parenting/caregiver-facing/ages-0-3/parenting_starting_solids_planner.md`.

## Safety Block — Act Now, Not on the Audit Schedule

- **Swallowed a button battery or two-plus magnets** (or suspected) → emergency
  department immediately, even with no symptoms; a lithium coin cell can burn the
  oesophagus within about two hours. For a known battery ingestion in a child 1+,
  honey (10 mL every 10 minutes, up to 6 doses) on the way is advised by Poison
  Control guidance — only if it does not delay getting there.
- **Any suspected poisoning** (medication, edible, detergent pod, nicotine liquid) →
  Poison Help 1-800-222-1222 (US); not breathing, seizing, or unresponsive → 911.
- **Unsafe sleep** found (pillows, bumpers, inclined sleeper, sleeping on a sofa with
  baby) → fix tonight.
- Outside the US, use your national poison centre and emergency number.

## Inputs / Context

1. **Child(ren):** ages and current motor stage (rolling, crawling, cruising,
   climbing, opening doors, using step stools).
2. **Home:** type, stairs, windows above ground floor, pool or water features, year
   built (pre-1978 → lead paint risk), heating, gas appliances.
3. **Hazard holders:** firearms, medications (including visitors' and grandparents'),
   cannabis edibles, vapes, button-battery devices, magnet toys, detergent pods,
   furniture and TVs, blind cords.
4. **Budget and renter/owner status** (affects anchoring and window fixes).

## Method

1. **Rank by severity × likelihood (RT-02).** Severity 1–3 (3 = death or permanent
   harm), likelihood 1–3 for this child's stage. Fix 9s and 6s first. The US leading
   causes of injury death in young children — unsafe sleep (infants), drowning
   (ages 1–4), and firearms (school age and teens) — outrank bumps and pinches, which
   are frequent but rarely severe.
2. **Apply the stage matrix (IT-22), current stage plus the next one:**
   - **Newborn (0–4 m):** safe sleep — alone, on back, firm flat surface, bare crib,
     no bumpers or inclined sleepers; smoke and CO alarms on every level; water heater
     ≤49 °C / 120 °F; rear-facing car seat installed and checked.
   - **Roller / crawler (4–9 m):** floor sweep for small objects (anything fitting
     through a toilet-paper tube); outlet covers; cordless window coverings; button
     batteries in devices with screwed-shut compartments; detergent pods locked.
   - **Cruiser / walker (9–18 m):** anchor every dresser, bookcase, and TV (US
     STURDY Act standards apply to new dressers; anchor old ones too); hardware-mounted
     gate at the top of stairs, pressure gate acceptable at the bottom; stove knob
     covers; hot drinks off low tables; toilet locks and buckets emptied.
   - **Climber (18 m–3 y):** window stops or guards (openings ≤10 cm / 4 in); move
     furniture away from windows; medications locked, not just high; magnets out;
     pool four-sided fence with self-latching gate; door-knob covers on exits.
   - **Preschooler (3–5 y):** lighters and matches locked; firearm storage audit
     (unloaded, locked, ammo separate); garage chemicals and tools locked; bike helmet
     habit; teach "don't touch, tell an adult" for guns.
   - **School age (5+):** firearms remain locked regardless of training; medication
     lockbox continues (teens included); trampoline policy; water competence
     ≠ drown-proof.
3. **Walk the house room by room (ST-02):** sleep space, bathroom, kitchen, living
   room, stairs, windows, garage/yard, guest and grandparents' rooms, car.
4. **Price and schedule each fix**, renter-friendly options where needed (adhesive
   anchors are weaker; ask the landlord to permit wall anchors).
5. **Stress-test (QA-02).** Get down to the child's eye level in each room; try to
   reach, climb, open, and pull. Test gates and latches against the child's actual
   strength.
6. **Set re-audit triggers:** each new motor milestone, a move, a holiday visit,
   new appliances or toys with batteries, a visitor's medications.

## Output Format

```
# Childproofing Plan — [home], child [age, stage]; next stage [..]

## Act-tonight items
## Ranked hazard list (hazard | room | severity | likelihood | score | fix | cost | by when)
## Stage-specific checklist (current + next)
## Room-by-room notes
## Re-audit triggers
## Emergency numbers posted (where)
```

## Verification

- [ ] Every hazard has a severity × likelihood score; top-scored fixes come first.
- [ ] Safe sleep, water, firearms, tip-overs, button batteries/magnets, and medications/edibles are each addressed or marked not applicable.
- [ ] The next developmental stage is pre-empted.
- [ ] Fixes are specific (product type, location), costed, and dated.
- [ ] Poison Help and emergency numbers are posted.

## False-Positive Prevention

| Misfire | What it looks like | Correction |
|---|---|---|
| Treating all hazards equally | 40-item list, outlets first | Rank by severity × likelihood; fix silent killers first. |
| "High up" as locked | Meds on top of the fridge | Climbers reach it; lock medications. |
| Pressure gate at stair top | Gate pops out under weight | Hardware-mount at the top. |
| Swim lessons as protection | "He can swim, the pool's fine" | Supervision and fencing still required. |
| Childproofing as a substitute for supervision | Baby left in bath "for a second" | Water and bath: always within arm's reach. |
| Buying everything | $600 kit | Many fixes are free (moving items, emptying buckets). |

## Adaptations

- **Grandparents' home:** pill organisers and loose blood-pressure medications,
  hearing-aid button batteries, unanchored furniture; bring a portable kit.
- **Autism / wandering risk:** exterior door alarms, pool alarms, ID bracelet.
- **Rentals:** request anchoring permission in writing; window stops need no drilling.
- **Multiple ages:** older children's small toys and magnet sets in a gated room.

## Example Output

```
# Childproofing Plan — 2-bed apartment, Noor 8 m (crawling); next: cruising

## Act tonight
- Crib bumper and pillow removed.
- TV remote and kitchen scale (coin cells) → tape compartments shut;
  spare coin cells into locked drawer.

## Ranked hazards
| Hazard | Room | S | L | Score | Fix | Cost | By |
| Dresser tip-over | Nursery | 3 | 3 | 9 | Wall anchors x2 | $15 | Sat |
| TV on low stand | Living | 3 | 2 | 6 | TV strap + anchor | $20 | Sat |
| Grandma's pills in handbag on floor | Living | 3 | 2 | 6 | Handbag hook by door; ask on arrival | $5 | Next visit |
| Detergent pods under sink | Kitchen | 3 | 2 | 6 | Lockbox high shelf | $18 | Sun |
| Blind cords | Nursery | 3 | 1 | 3 | Cordless shades | $40 | 2 wks |
| Outlets | All | 2 | 1 | 2 | Sliding covers | $12 | 2 wks |

## Next stage (cruising, expected ~10 m)
Stove-knob covers; toilet lock; bath never unattended; coffee table corner
guards optional (low severity).

## Re-audit triggers
Pulls to stand; Grandma's two-week stay in December; new toys at birthday.

## Posted
Poison Help 1-800-222-1222 and address on the fridge.
```

## Techniques Used

- **RT-02 Multi-Dimensional Analysis Framework** — severity × likelihood scoring per hazard.
- **ST-02 Structured Sequential Instructions** — room-by-room walk-through.
- **IT-22 Workflow Decision Matrix** — stage matrix maps motor stage to the hazards that matter.
- **QA-02 Adversarial Stress-Test** — eye-level reach-and-climb testing of fixes.

## Related Prompts

- `domain-parenting/caregiver-facing/ages-0-3/parenting_when_pediatrician_visit_0_3.md` — triage after an injury or ingestion.
- `domain-parenting/caregiver-facing/safety-risk/parenting_other_homes_safety_questions.md` — vetting homes the child visits.
- `domain-parenting/caregiver-facing/ages-0-3/parenting_starting_solids_planner.md` — choking prevention at meals.
