---
title: "Trip Planner"
category: productivity/home-life
description: "Plan a trip from confirmed destination to departure-day checklist — producing a pre-trip planning checklist, a trip-specific packing list, and a departure-day checklist."
techniques:
  - ST-01
  - ST-02
  - DS-02
  - CM-08
  - QA-01
  - RT-02
difficulty: beginner
tags:
  - travel
  - trip-planning
  - packing
  - vacation
  - household
updated: "2026-05-12"
related_prompts:
  - domain-productivity/deep-work/deepwork_chunk_project_to_calendar.md
  - domain-productivity/bottlenecks/bottleneck_capture_triage_system_design.md
  - domain-personal-development/prompts/agency/agency_next_action_spec.md
---

# Trip Planner

**Objective:** Convert a confirmed trip into three concrete, trip-specific artifacts: a pre-trip planning checklist (what to book and arrange before you leave), a packing list customized to the trip's destination, climate, activities, and travelers, and a departure-day checklist (what to do in the final hours before leaving the house).

**When to use:** Once a trip is confirmed with dates and a destination. Most useful 2–4 weeks before departure, but can be run 1 week out with appropriate urgency flags. Not useful for trips still in the "considering" phase — this is for execution, not deliberation.

**Audience:** Anyone taking a trip from their primary home — leisure travel, work travel, family visits, adventure trips. Works for solo travelers, couples, families with kids, and groups. Excludes: frequent travelers with established personal packing systems who don't need a prompt, corporate travel managed entirely by an assistant.

---

## Inputs Required

1. **Destination and dates.** Where you're going and when (departure date, return date). Include city/region and country if international.

2. **Trip purpose.** Leisure (beach, city tourism, hiking, road trip), family visit, work/conference, wedding or event, adventure (camping, skiing, diving). This shapes the packing list and planning tasks.

3. **Travelers.** Number of people and ages — particularly whether children are included and their ages. Adults-only vs. traveling with a 4-year-old changes packing and planning significantly.

4. **Transportation method.** Flight (domestic/international), driving, train, cruise ship. For flights: note carry-on only vs. checked bags — this changes packing constraints. For international flights: note passport status and any visa requirements you're aware of.

5. **Accommodation type.** Hotel, Airbnb/rental with kitchen, camping, staying with family/friends. Rental with kitchen changes what to pack for food. Camping changes the gear list entirely.

6. **Activities planned.** What you'll actually be doing: beach time, hiking, city sightseeing, skiing, a formal dinner, snorkeling, theme parks, a wedding, outdoor concerts. Be specific — "outdoor activities" is not useful; "half-day hike on day 3 plus mostly restaurant meals" is.

7. **Home-management items to arrange.** What needs handling while you're gone: pet care, mail and packages, plants, house security, any deliveries expected, any neighbor heads-up needed.

---

## Instructions

### Step 1 — Build the pre-trip planning checklist

Generate a timeline-organized list of tasks to complete before departure. Organize by urgency:

**Book immediately if not done (time-sensitive):**
- Flights and accommodation (if not already booked)
- Rental car (if needed — popular destinations sell out early)
- Restaurant reservations for specific meals (high-demand restaurants, special occasions)
- Event tickets, tour bookings, or attraction passes with fixed dates
- Pet boarding or pet sitter (reputable boarding fills up weeks out)
- International: visa applications, travel health appointments, prescriptions to fill

**1–2 weeks before:**
- Travel insurance (if desired — purchase before a covered event happens)
- Notify credit cards of travel dates and destinations (prevents fraud blocks)
- Check passport expiration (many countries require 6 months validity beyond return date)
- Arrange mail hold or have someone collect mail and packages
- Plant care arranged (watering schedule to a neighbor, or self-watering solutions)
- Confirm pet care arrangements
- Download offline maps, translation apps, boarding passes
- International: confirm currency situation (carry cash, ATM access, card fees)

**Day before departure:**
- Confirm all reservations (hotel, rental car, any activities booked)
- Charge all devices
- Print or download all documents (boarding passes, hotel confirmation, rental car)
- Prepare carry-on documents pouch: IDs, tickets, reservations, insurance
- Make a copy of passport and store separately from original (international)

### Step 2 — Build the packing list

Generate a packing list specific to this trip. Customize to:

**Climate and weather at destination:**
- Pull packing categories from the destination's expected weather during travel dates (cold and wet = layers and waterproof outer shell; hot and sunny = sun protection, light fabrics; variable = layering system)
- Include weather-specific items the traveler might forget: packable umbrella, sandals for beach/pool, warm layers for over-air-conditioned hotels

**Activity-specific items:**
- Hiking: appropriate footwear, moisture-wicking layers, trekking poles if needed, blister prevention
- Beach: swimwear, coverup, reef-safe sunscreen, beach bag, sandals, rash guard
- Skiing: this is usually gear-heavy — note what to rent vs. bring
- Formal event (wedding, conference dinner): specify the clothing items, include accessories
- Theme parks: comfortable walking shoes (not just sneakers — specifically comfortable ones), portable charger, small backpack
- International: plug adapters for the destination country, universal power strip if multiple devices

**Transportation-specific constraints:**
- Carry-on only: no liquids over 3.4oz in carry-on (use solid toiletries or check a bag for liquids), everything must fit in approved dimensions
- Checking bags: no prohibited items (check TSA if uncertain), lock checked bags
- Driving: no weight/size constraint, but note anything too large for the vehicle

**Travelers:**
- Children (list ages): add age-appropriate items — diapers/pull-ups if needed, specific snacks the child will eat, entertainment for transit, any medications, comfort item (stuffed animal, tablet with shows downloaded)
- International: each traveler needs their own passport, even infants

Organize the packing list into sections:
- Clothing (list specific items by count, not just "clothes")
- Footwear
- Toiletries and personal care
- Electronics and accessories
- Documents and money
- Medications and health
- Activity-specific gear
- Children's items (if applicable)
- Home comfort items for rental properties (if applicable)

### Step 3 — Build the departure-day checklist

The last things to do before walking out the door. These are the tasks that prevent the "did I leave the stove on" panic and the "I forgot to arrange dog care" disaster.

**Home security and management:**
- [ ] Lock all windows and doors (do a circuit — check back door, garage, basement)
- [ ] Unplug unnecessary electronics (coffee maker, toaster, curling iron, phone chargers not taken)
- [ ] Set thermostat to away mode
- [ ] Take out trash if it's near collection day
- [ ] Water plants if no one is handling it
- [ ] Confirm pet care is in place and leave written instructions + emergency vet contact
- [ ] Leave a key with a neighbor or trusted contact if someone needs access
- [ ] Confirm mail is on hold or someone is collecting it
- [ ] Leave a note with trip dates and emergency contact for anyone watching the house

**Documents and money:**
- [ ] Passport (if international) — check expiration
- [ ] ID (driver's license or passport) for domestic
- [ ] Boarding passes downloaded or printed
- [ ] All reservation confirmations accessible (hotel, rental car, activities)
- [ ] Credit cards and cash in wallet
- [ ] Travel insurance information accessible
- [ ] Any prescription medications packed and in original containers (carry-on, not checked, for critical medications)

**Day-of logistics:**
- [ ] Confirm transportation to airport/station: rideshare booked, parking confirmed, or driver arranged
- [ ] Allow adequate time — confirm how early to be at the airport (domestic: 1.5–2 hrs, international: 2.5–3 hrs)
- [ ] Charge all devices overnight before departure
- [ ] Pack carry-on with essentials accessible (snacks, earbuds, anything needed during transit)

---

## Constraints

### Must
- Produce all three artifacts: planning checklist, packing list, departure-day checklist
- Packing list must be trip-specific — tied to the destination climate, activities, and traveler types provided
- Planning checklist must be timeline-organized (book now vs. 1–2 weeks vs. day before)
- Children's items must be added explicitly when children are listed as travelers
- Departure-day checklist must include home-security and house-management items, not just personal documents

### Must Not
- List generic packing items without context ("bring comfortable shoes" without knowing what activities are planned)
- Tell an international traveler to "bring your passport" as if that's the insight — add the 6-month validity rule and make a copy instruction
- Include carry-on liquid rules for someone who is checking a bag
- Omit pet care arrangement from the planning checklist if the user mentioned pets
- Produce a packing list that is the same regardless of trip type

---

## False-Positive Prevention

1. **Generic packing list:** Produces the same list for a ski trip and a beach vacation — "shirts, pants, toiletries." The packing list is only useful if it accounts for the specific destination, climate, and activities. If the list could be used for any trip, it has failed.

2. **Missing children's essentials:** The traveler has a 3-year-old and the packing list doesn't mention diapers, wipes, familiar snacks, or entertainment for a 3-hour flight. Child-specific items must be age-appropriate and thorough.

3. **Departure-day checklist without home management:** Lists personal documents but doesn't prompt the traveler to check that the back door is locked, the stove is off, or that someone has the dog. Half the departure-day value is the home walkthrough.

4. **International travel without country-specific items:** Doesn't flag the plug adapter for a UK trip, doesn't mention the 6-month passport rule, doesn't mention that some cards charge foreign transaction fees. "Check country-specific requirements" is not an item — name them.

5. **Planning checklist with no urgency signal:** Lists everything as equal priority. Some items (booking accommodation, pet boarding) must happen immediately; others (downloading offline maps) can wait until the day before. Timeline structure is required.

---

## Output Format

```
## Trip Plan: [Destination] | [Dates] | [X travelers]
### Purpose: [Trip type] | Transport: [Flight/Drive/etc.] | Accommodation: [Type]

---

### ARTIFACT 1: Pre-Trip Planning Checklist

**Book / Arrange Immediately**
- [ ] [Task — note if already done]
- [ ] Pet boarding / sitter — book by [X weeks before to ensure availability]
- [ ] ...

**1–2 Weeks Before**
- [ ] Notify credit cards of travel dates (call or do in app — [Card 1], [Card 2])
- [ ] [Task]
- [ ] ...

**Day Before Departure**
- [ ] Confirm all reservations (hotel conf#, rental car conf#, restaurant reservations)
- [ ] [Task]
- [ ] ...

---

### ARTIFACT 2: Packing List
### [Destination] | [Climate: e.g., "Hot and humid, 85–95°F"] | [Activities] | [Carry-on only / Checked bags]

**Clothing**
- [ ] [Specific item × quantity] — [note: for hiking on day 3, for formal dinner on day 4]
- [ ] ...

**Footwear**
- [ ] [Item] — [activity it's for]
- [ ] ...

**Toiletries & Personal Care**
- [ ] [Item] — [note if must be in carry-on vs. can be checked / if 3.4oz rule applies]
- [ ] ...

**Electronics & Accessories**
- [ ] [Item]
- [ ] Plug adapter — [destination country plug type] [international only]
- [ ] ...

**Documents & Money**
- [ ] Passport — expires [date], valid for this trip: [yes/check] [international]
- [ ] [Other documents]
- [ ] ...

**Medications & Health**
- [ ] [Prescription medications — original containers, in carry-on]
- [ ] [OTC items specific to trip: motion sickness, altitude, sunburn]
- [ ] ...

**Activity-Specific Gear**
- [ ] [Item tied to a specific planned activity]
- [ ] ...

**Children's Items** [if applicable]
- [ ] [Age-appropriate items: diapers, snacks, entertainment, medications, comfort item]
- [ ] ...

---

### ARTIFACT 3: Departure-Day Checklist

**Home Walkthrough**
- [ ] All windows closed and locked (do a circuit: front, back, sides, basement)
- [ ] All exterior doors locked
- [ ] Stove, oven, curling iron off
- [ ] Unplug: [list applicable items]
- [ ] Thermostat set to away ([temperature])
- [ ] Trash taken out [if needed]
- [ ] Plants watered [or: watering confirmed with [person]]
- [ ] Pet care in place — written instructions left at [location], vet number: [number]
- [ ] Mail hold confirmed / neighbor collecting: [name]
- [ ] Key left with: [name] at [location]

**Documents and Money**
- [ ] Passport / ID packed
- [ ] Boarding passes — in [phone / printed]
- [ ] All confirmations accessible
- [ ] Credit cards and [amount] cash

**Departure Logistics**
- [ ] [Rideshare booked / Parking confirmed at [location]] — pickup/departure: [time]
- [ ] Devices charged
- [ ] Carry-on accessible for: [medications, snacks, boarding passes, [child's comfort item]]

---

### Notes
[Anything specific to this trip: visa status, vaccination requirements, weather forecasts, local customs, anything flagged as unusual from the inputs]
```

---

## Verification

- [ ] All three artifacts are present: planning checklist, packing list, departure-day checklist
- [ ] Packing list clothing items are specific (e.g., "2 pairs hiking pants" not "pants")
- [ ] Packing list reflects the destination climate and planned activities
- [ ] Children's items are present and age-appropriate when children are listed
- [ ] Planning checklist is organized by timeline urgency
- [ ] International travel items (passport validity, plug adapters, currency, visa) are included for international trips only
- [ ] Departure-day checklist includes home walkthrough, not just personal documents
- [ ] Pet care appears in both the planning checklist (arrange in advance) and departure-day checklist (confirm in place)
- [ ] Carry-on vs. checked bag constraints are reflected in packing list if relevant
