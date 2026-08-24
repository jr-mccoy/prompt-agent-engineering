---
title: "Home Seasonal Maintenance Calendar"
category: productivity/home-life
description: "Build a month-by-month home maintenance calendar tailored to your home type, ownership status, climate, and installed systems — so nothing gets skipped until it becomes a costly repair."
techniques:
  - ST-01
  - ST-03
  - DS-02
  - CM-02
  - QA-01
  - OC-06
difficulty: beginner
tags:
  - home-maintenance
  - seasonal
  - homeowner
  - renter
  - calendar
  - preventive
updated: "2026-05-12"
related_prompts:
  - domain-productivity/reviews/reviews_weekly_systems_review.md
  - domain-productivity/deep-work/deepwork_chunk_project_to_calendar.md
  - domain-productivity/bottlenecks/bottleneck_capture_triage_system_design.md
---

# Home Seasonal Maintenance Calendar

**Objective:** Produce a month-by-month home maintenance schedule tailored to the user's home type, climate, ownership status, and installed systems. The output is a concrete, actionable calendar — not a generic checklist that applies to every home whether they have a pool or not.

**When to use:** When setting up a home maintenance system for the first time, when moving into a new home, or at the start of any season when you can't remember what should have been done last month. Also useful after a major system is added (new HVAC, irrigation installed).

**Audience:** Homeowners and renters who maintain their own home. Renters have a subset of responsibilities (what's inside their unit vs. what's the landlord's) — the calendar adjusts for that. Not for property managers or maintenance professionals who manage multiple properties.

---

## Inputs Required

1. **Home type.** House (detached), townhouse, condo/apartment, or manufactured home. This determines what maintenance applies — condo owners typically don't maintain the exterior, roof, or HVAC shared systems.

2. **Ownership status.** Owner or renter. Renters should note what's in their lease as their responsibility (e.g., "I'm responsible for changing HVAC filters; landlord handles everything else").

3. **Climate zone.** Choose the closest match:
   - **Cold / northern:** Freezing winters, significant snow or ice. Winterization is a major seasonal concern.
   - **Hot / southern:** Extreme summer heat, mild winters. HVAC cooling load, irrigation, and drought concerns dominate.
   - **Temperate / coastal:** Mild year-round, possible humidity or fog. Mold, moisture, and mild storm prep.
   - **Humid / subtropical:** Hot and humid summers, mild winters. Moisture management, air quality, storm season.
   - **Arid / desert:** Extreme heat, low humidity, drought. Cooling systems, sun exposure, irrigation.

4. **Installed systems.** List every system that applies. Include only what's actually in the home:
   - HVAC type: forced air, mini-split, radiator, window units
   - Water heater type: tank (gas/electric) or tankless
   - Irrigation or sprinkler system: yes/no
   - Pool or hot tub: yes/no
   - Fireplace or wood stove: yes/no
   - Sump pump: yes/no
   - Septic system (vs. municipal sewer): yes/no
   - Garage: attached/detached/none
   - Finished basement: yes/no

5. **Exterior features.** Note what applies: gutters, wood deck or patio, fence, driveway (concrete/asphalt/gravel), roof type (shingle, flat, tile), large trees near the house.

6. **Current month.** So the calendar can flag what's overdue vs. upcoming.

---

## Instructions

### Step 1 — Determine scope

Based on home type and ownership status, establish what categories of maintenance apply:

**Homeowner, detached house:** Full scope — exterior, interior, systems, safety, seasonal prep.

**Condo/apartment owner:** Interior-only scope plus any systems the owner is responsible for (typically HVAC within the unit, water heater, appliances). Exterior and shared systems are HOA/building responsibility.

**Renter:** Typically: smoke/CO detector batteries, HVAC filter changes per lease, interior appliance maintenance. Exclude: roof, gutters, exterior, plumbing, electrical, structural. Flag if lease specifies anything additional.

### Step 2 — Build the seasonal task library

Generate the task list from the installed systems and exterior features, organized by season:

**Spring (March–May):**
- Post-winter inspection: look for roof damage, cracked caulk, foundation settling
- Gutter cleaning after tree pollen/debris season
- HVAC: switch from heat to cooling, replace filter, schedule A/C service if not done in fall
- Irrigation: start up system, check heads, test for winter damage
- Exterior: inspect and touch up paint/caulk, check deck boards and railings, treat wood if needed
- Windows/screens: wash windows, repair or install screens
- Sump pump: test operation before spring rains

**Summer (June–August):**
- HVAC filter: replace monthly if running heavily
- Irrigation: check for efficient coverage, adjust schedules for heat
- Attic: check ventilation (heat buildup degrades roofing)
- Outdoor: clean and inspect deck, check for pest activity, clean dryer vent
- Pool/hot tub: maintain chemistry weekly, check equipment monthly

**Fall (September–November):**
- Gutters: clean after leaves fall (critical — before first freeze)
- HVAC: switch from cooling to heat, replace filter, schedule furnace service
- Irrigation: winterize system before first freeze
- Fireplace/wood stove: chimney inspection and cleaning before first use
- Exterior: caulk gaps before cold sets in, check weatherstripping on doors and windows
- Water heater: flush tank to remove sediment (annual)
- Dryer vent: clean if not done in summer
- Smoke/CO detectors: test and replace batteries (do both spring and fall)

**Winter (December–February):**
- Pipe insulation: protect exposed pipes before a hard freeze
- HVAC filter: replace monthly (forced air systems running heavily)
- Sump pump: keep an eye on in heavy rain
- Safety: check fire extinguisher charge, test smoke/CO detectors
- Attic/basement: check for moisture or condensation from cold weather
- For cold climates: monitor roof for ice dams, keep gutters clear of ice buildup

### Step 3 — Apply climate adjustments

Overlay the climate zone to adjust timing and emphasis:

- **Cold / northern:** Move winterization tasks earlier (gutters cleaned by October, irrigation winterized by mid-October, pipes insulated before November). Add ice dam monitoring.
- **Hot / southern:** Move A/C service to March (before summer heat). De-emphasize winterization. Add late summer exterior inspection before hurricane/storm season if coastal.
- **Humid / subtropical:** Add spring mold inspection (attic, basement, crawl space), regular dehumidifier maintenance, storm shutter prep if applicable.
- **Arid / desert:** Add summer roof inspection (intense UV degrades roofing faster), irrigation efficiency checks, exterior paint inspection for sun fade and cracking.

### Step 4 — Assign months and frequency

For each task, assign:
- **Month(s):** when to do it
- **Frequency:** annually, biannually, monthly, or seasonally
- **Duration estimate:** approximate time commitment (15 min, 1–2 hours, half a day)
- **DIY or professional:** whether this is typically a homeowner task or requires a service call

### Step 5 — Flag overdue items

Based on the current month, identify any tasks that should have been done already this year and haven't been addressed yet. Surface these as "Do Now / Catch Up" at the top of the output.

---

## Constraints

### Must
- Scope maintenance to what the user's home type and ownership status actually requires
- Adjust task timing to the user's climate zone — the same gutter-cleaning task has different urgency in Seattle vs. Phoenix
- Include only systems and features the user listed — do not include pool maintenance for a home without a pool
- Flag what's overdue based on the current month
- Include safety items (smoke detectors, CO detectors, fire extinguisher) regardless of climate or home type

### Must Not
- Apply a generic "all homes" checklist regardless of the inputs
- Include tasks that are the landlord's responsibility when the user is a renter
- Recommend professional service calls for tasks that are universally DIY (replacing an HVAC filter)
- List monthly tasks without specifying which month or season they apply to
- Omit a seasonal task because it seems obvious — if it's in the scope, include it

---

## False-Positive Prevention

1. **Climate-agnostic timing:** Recommends "winterize your irrigation by October" to someone in Phoenix with no freeze risk. Climate must change task timing and inclusion, not just add a paragraph at the end.

2. **Renter scope creep:** Tells a renter to inspect their gutters and roof — tasks that are their landlord's responsibility. Renter scope is interior-only plus lease-specified items.

3. **Missing system tasks:** The user listed a sump pump but the calendar never addresses it. Every system listed in inputs must appear in the calendar.

4. **Frequency omitted:** Lists tasks without saying how often — the user doesn't know if "clean the dryer vent" is monthly or annual. Every task must have a frequency.

5. **Overdue items buried:** If it's November and the gutters haven't been cleaned yet (listed as October task), that's urgent — it must surface at the top, not be buried in the October row.

---

## Output Format

```
## Home Maintenance Calendar
### [Home type] | [Climate zone] | [Owner/Renter]

---

### Do Now / Catch Up
[Tasks that should have been completed before [current month] and haven't been addressed — based on today's date]

- [ ] [Task] — was due [Month], urgent because [reason]
- [ ] ...

---

### Spring (March–May)

| Month | Task | Frequency | Est. Time | DIY or Pro |
|-------|------|-----------|-----------|------------|
| March | [Task] | Annual | [X min/hrs] | DIY |
| April | [Task] | Annual | [X min/hrs] | Schedule a pro |
| May   | [Task] | Biannual | [X min/hrs] | DIY |
| ...   | | | | |

---

### Summer (June–August)

| Month | Task | Frequency | Est. Time | DIY or Pro |
|-------|------|-----------|-----------|------------|
| June  | HVAC filter replacement | Monthly (summer) | 15 min | DIY |
| ...   | | | | |

---

### Fall (September–November)

| Month | Task | Frequency | Est. Time | DIY or Pro |
|-------|------|-----------|-----------|------------|
| September | [Task] | Annual | [X hrs] | DIY |
| ...   | | | | |

---

### Winter (December–February)

| Month | Task | Frequency | Est. Time | DIY or Pro |
|-------|------|-----------|-----------|------------|
| December | [Task] | Annual | [X min] | DIY |
| ...   | | | | |

---

### Monthly Tasks (Year-Round)

- HVAC filter: Replace every [1/2/3] months (more often during peak heating/cooling)
- [Other monthly task]: [Frequency note]

---

### Safety (Every 6 Months)

- [ ] Test smoke detectors (replace batteries if low) — March and October
- [ ] Test carbon monoxide detectors — March and October
- [ ] Check fire extinguisher charge — [month]

---

### Notes

[Climate-specific callouts, anything unusual about this home's maintenance needs, any task that requires scheduling a professional weeks in advance]
```

---

## Verification

- [ ] Scope matches home type and ownership status (renters don't have exterior tasks)
- [ ] Every system listed in inputs appears in the calendar
- [ ] Climate zone adjustments change task timing, not just add a note
- [ ] Overdue tasks are surfaced separately at the top
- [ ] Every task has a frequency assigned
- [ ] Safety items (smoke/CO detectors, fire extinguisher) are included
- [ ] DIY vs. professional is noted for each task
- [ ] No tasks included for systems or features not listed in inputs
