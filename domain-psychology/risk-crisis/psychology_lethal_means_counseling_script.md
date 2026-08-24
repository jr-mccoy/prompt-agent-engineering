---
title: "Lethal Means Counseling (CALM-Style) Conversation Builder"
category: psychology/risk-crisis
description: "Generate a CALM-style lethal-means counseling conversation covering firearms, medications, and other means, with concrete time-and-distance interventions, family involvement, and documentation."
techniques:
  - ST-04
  - DT-02
  - NE-07
  - RP-04
  - ED-03
  - QA-04
  - CM-02
difficulty: advanced
tags:
  - lethal-means-counseling
  - calm
  - means-restriction
  - firearm-safety
  - medication-secure-storage
  - time-and-distance
intended_use: model-testing
updated: "2026-05-08"
related_prompts:
  - domain-psychology/risk-crisis/psychology_columbia_suicide_risk_assessment.md
  - domain-psychology/risk-crisis/psychology_stanley_brown_safety_plan.md
---

# Lethal Means Counseling (CALM-Style) Conversation Builder

## Objective

Produce a Counseling on Access to Lethal Means (CALM) conversation, scripted for the clinician, that:

1. Frames the conversation around the public-health evidence that **putting time and distance between a person at risk and lethal means substantially reduces suicide deaths**, especially during acute, ambivalent crises.
2. Conducts a structured means inventory covering **firearms, medications, and other means**.
3. Co-develops specific, agreed-upon storage / removal / reduction plans for each means.
4. Identifies a specific **trusted holder** when removal is the goal.
5. Includes the family / partner conversation when consent permits.
6. Generates documentation suitable for the chart and as a follow-on to the safety plan.

CALM is appropriate regardless of suicide intent, when access to highly lethal means is present.

## When to Use

- After a positive C-SSRS or any disclosure of SI.
- After an attempt or hospitalization, before discharge.
- During Stanley-Brown safety planning (Step 6) — this prompt expands Step 6 into a full conversation.
- During well-care visits when family member raises concern.
- At intake when access-to-means is part of the biopsychosocial.

## Inputs / Context

- Risk-assessment summary linked to this counseling encounter.
- Client's relationship to firearms (none / personal owner / household member owns / military or LE / hunting / collector / family heirloom).
- Inventory of firearms: type (handgun / long gun), number, current location, current storage (loaded? in safe? trigger lock?), current ammo storage.
- Medications: current scripts (psychotropic, opioid, benzodiazepine, anticholinergic, lithium, beta-blocker, glaucoma drops), OTC (acetaminophen quantity, NSAIDs), client's typical access pattern (bottle on counter / bedside / weekly pill organizer / pharmacy 30-day supply).
- Other means: high places at home/work, water/bridges, motor vehicles, sharps, cordage, household chemicals.
- Trusted potential holder(s): name, relationship, willingness to receive firearms or hold meds.
- State and local laws: extreme risk protection orders (red-flag laws), out-of-state transfer rules, voluntary firearm hold programs (e.g., police department, FFL dealers), pharmacy lockbox programs.
- Cultural / occupational context: client is a hunter, in law enforcement, military, lives in rural area; values around firearm ownership.

## Constraints

### Must

- Output two parallel artifacts: **(A) Conversation Script** the clinician can follow turn-by-turn, and **(B) Documentation Block** for the chart.
- Conversation Script structured in 5 phases: **Frame**, **Inventory**, **Time-and-Distance Options**, **Trusted Holder / Storage Plan**, **Confirm and Schedule Verification**.
- Frame uses public-health framing (ambivalence, time-distance, lethality differential between methods) rather than disarmament framing; honor cultural / occupational context.
- Inventory is exhaustive: firearms, every prescribed medication, OTC, other means.
- For each item, generate options on a continuum: ideal (off-site removal) → strong (lockbox + holder for key) → harm-reduction (cable lock + separated ammunition; weekly pill supply only).
- Document agreed plan per item with: action, who does it, by when, how it will be verified.
- Address state-specific options the clinician should consider raising: red-flag/ERPO, voluntary firearm hold programs, pharmacy lockbox programs.
- Family / partner involvement: when ROI permits, include a script for involving the trusted holder; when refused, document refusal and adjust risk plan.
- Document client's stated barriers ("the gun is for protection," "I'd never do that with my kids' Tylenol around") and the responses used.

### Must Not

- Do not lecture, moralize, or imply the client cannot be trusted with their own property.
- Do not promise confidentiality from family members beyond what the client has authorized.
- Do not provide legal advice; if state-law options come up, refer to local resources.
- Do not skip medications because firearms feel "more lethal" — overdose is the most common method in many populations.
- Do not document "means counseling completed" without specifics (what items, what plans, by whom, by when).
- Do not document a plan the client has not agreed to.

## Instructions

1. Frame the conversation: research-based, ambivalence-aware, non-judgmental.
2. Conduct exhaustive means inventory.
3. For each means, present options on the time-and-distance continuum, in client's language and context.
4. Identify trusted holder(s) and verify willingness.
5. For firearms, raise state-appropriate options: family transfer, voluntary hold, lock + separated ammo, ERPO if applicable.
6. For medications, plan: lockbox + key with partner, pharmacy 7-day or 14-day fills, OTC quantity reduction, return excess to drug-take-back.
7. For other means: address each.
8. Document agreed plan with action / responsible party / deadline / verification method.
9. Schedule verification (e.g., text photo of locked firearm cabinet by [date]).
10. Run verification.

## Output Format

```
=== LETHAL MEANS COUNSELING — CONVERSATION + DOCUMENTATION ===

PART A — CONVERSATION SCRIPT (Clinician-side)

Phase 1 — Frame
"Before we go further today I want to talk about something that we know makes the biggest difference for people in your situation. It's not about taking anything away from you. It's about what the research keeps showing us: when someone is having a really hard time, putting time and distance between them and the things they could use to hurt themselves dramatically lowers the chance of dying — even when nothing else changes about how they're feeling. Crises are often short and the worst impulses pass. Most people who survive an attempt do not go on to die by suicide. So I want us to walk through what's around you and look at small changes we can make together. Is that okay to talk about?"

[If client hesitates: validate, restate non-judgmental purpose, ask for the smallest piece they're willing to discuss first.]

Phase 2 — Inventory
"Let's look at three areas: firearms, medications, and anything else around the house. I'm going to ask in detail because the specifics matter for figuring out what helps."

Firearms questions:
- "Do you own or have access to firearms — yours, a partner's, a parent's, a roommate's?"
- "What kinds, how many, where are they kept right now?"
- "How are they stored — loaded, locked, ammo together or separate?"
- "Anyone else in the home know they're there?"
- "Are any of them tied to your work, hunting, family — anything important about why they're there?"

Medication questions:
- "Let's look at every prescription you take, and the OTC stuff too. How many pills do you have on hand right now of each? Where do you keep them?"
- "Any medication that someone else in the house takes and you'd have access to?"
- "Anything in the medicine cabinet from old prescriptions?"

Other means:
- "Are there other things at home or work you've thought about — high places, the car, anything else?"

Phase 3 — Time-and-Distance Options (per item)
For firearms — present continuum:
- "The strongest option is having someone else hold them off-site for now — a family member, a friend, a local police department voluntary hold program, an FFL dealer who'll store them. We'd just need to know who, and by when."
- "If off-site isn't workable, the next strongest is locked at home with the ammo locked separately, and ideally the key with someone else."
- "If we can't do either of those, even a cable lock and separated ammo adds time when seconds matter."

For medications — present continuum:
- "Strongest: someone you live with holds the bottles in a lockbox and gives you what you need."
- "Next: pharmacy fills 7 or 14 days at a time instead of 30."
- "Always: get rid of the old prescriptions — drug take-back at any pharmacy is anonymous."

For other means: address each.

Phase 4 — Trusted Holder / Storage Plan
- "Who comes to mind for holding the firearms?"
- [If no one: "What if we explored a voluntary hold with [local PD program / FFL dealer]?"]
- [If holder named: "What's a date we could realistically have that done by? Can we call them right now in session?"]
- [Address barriers: protection concerns, hunting season, work needs, family pushback. Do not skip past these.]

Phase 5 — Confirm and Schedule Verification
- "Let me read back the plan: [recap]. By [date], this gets done; you'll [text me a photo of the locked cabinet / show me the medication lockbox at next session / call me when [holder] picks up]. If something gets in the way, you'll text me by [date] and we'll figure out the next option together."
- [If any item declined: "What you're not okay with is [item]; we'll come back to that. For now, we have [items agreed]."]
- [End with reaffirmation: "This conversation is part of how we keep you alive while we work on the longer-term stuff."]

PART B — DOCUMENTATION BLOCK

ENCOUNTER METADATA
Client: [Initials/MRN]
Date: [YYYY-MM-DD]    Time: [HH:MM]    Duration: [N min]
Linked risk assessment: [Date of Columbia or comparable]
Linked safety plan: [Date]

MEANS INVENTORY
Firearms: [Type, count, current location, current storage, ammo storage, ownership/relationship.]
Medications:
| Med / OTC | Dose | On-hand quantity | Storage | Risk profile |
|-----------|------|------------------|---------|--------------|
| [...]     | [...] | [...]           | [...]   | [Lethal in OD / High / Moderate / Low] |
Other means: [...]

AGREED PLAN (per item)
| Item | Plan | Responsible | By when | Verification method |
|------|------|-------------|---------|---------------------|
| Firearms | [Off-site hold with brother / lockbox / cable+separated ammo] | [Client + brother] | [Date] | [Photo / in-person verification at next session] |
| Med #1   | [Pharmacy 7-day fills; partner holds bottle in lockbox] | [Client + partner + pharmacist] | [Date] | [Pharmacy confirmation / photo of lockbox] |
| ...      | ...  | ... | ... | ... |

DECLINED OR DEFERRED
- [Item] — declined; rationale: [...] — clinical implication: [Higher acute risk; increase contact frequency; revisit in [N days].]

STATE-LAW / PROGRAM OPTIONS DISCUSSED
- Red-flag / ERPO: [Applicable in state? raised? client response]
- Voluntary firearm hold program: [Local PD / FFL — raised? client response]
- Pharmacy lockbox / drug take-back: [Raised; location given]

FAMILY / PARTNER INVOLVEMENT
- ROI status: [Signed / Not signed]
- Trusted holder named: [Name, relationship, willingness verified Y/N — how]
- Family conversation: [Conducted in session / Scheduled / Declined]

CLIENT BARRIERS AND RESPONSES
- [Barrier raised: "...". Response used: "..."]

VERIFICATION SCHEDULED
[Specific verification at next contact: e.g., "Client will text photo of locked gun cabinet by [date]; will show medication lockbox at next session [date]; clinician will follow up by phone if not received by [date]."]

NEXT STEPS
- Next session: [Date / frequency increase if applicable]
- Coordination: [PCP / prescriber / family / pharmacy notified]

Clinician: __________________  Date/Time: ___________
```

## Verification

- [ ] Conversation script and documentation block both present.
- [ ] Frame phase uses public-health, ambivalence-aware, non-disarmament language.
- [ ] Means inventory covers firearms, medications, other.
- [ ] For every accessible means, an agreed plan is documented OR the decline is documented with clinical implications.
- [ ] Each agreed plan includes responsible party, deadline, verification method.
- [ ] State / local options (ERPO, voluntary hold, pharmacy programs) raised when applicable.
- [ ] Family / partner involvement status documented (ROI, holder verified, conversation conducted/scheduled/declined).
- [ ] Verification step is concrete (photo, in-person, pharmacy confirmation).
- [ ] Linked to risk assessment and safety plan.
- [ ] No moralizing; no promise to keep means counseling secret from a contracted holder.
- [ ] Gaps flagged; nothing fabricated.
