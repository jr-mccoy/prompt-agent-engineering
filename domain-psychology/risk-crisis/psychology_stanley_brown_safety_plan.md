---
title: "Stanley-Brown Safety Planning Intervention Builder"
category: psychology/risk-crisis
description: "Co-construct a Stanley-Brown safety plan with a client across the canonical 6 steps: warning signs, internal coping, social distractions, people for help, professionals/agencies, and means restriction."
techniques:
  - ST-04
  - DT-02
  - NE-01
  - NE-07
  - ED-04
  - QA-04
  - CM-02
difficulty: advanced
tags:
  - safety-plan
  - stanley-brown
  - safety-planning-intervention
  - means-restriction
  - 988
  - lethal-means
intended_use: model-testing
updated: "2026-05-08"
related_prompts:
  - domain-psychology/risk-crisis/psychology_columbia_suicide_risk_assessment.md
  - domain-psychology/risk-crisis/psychology_lethal_means_counseling_script.md
  - domain-psychology/risk-crisis/psychology_post_attempt_reengagement_plan.md
---

# Stanley-Brown Safety Planning Intervention Builder

## Objective

Generate a Stanley-Brown Safety Planning Intervention (SPI) collaboratively built with the client. The plan is a 6-step, hierarchical, externalizable document the client carries (paper, EHR portal, phone). It is a clinical intervention, not a "no-suicide contract."

Required steps in order:

1. **Warning signs** (personal, specific) that signal a crisis is coming.
2. **Internal coping strategies** the client can use alone.
3. **Social contacts and settings** that provide distraction (without disclosing crisis content).
4. **People** the client can ask for help and disclose crisis to.
5. **Professionals and agencies** to contact (including 988, local crisis line, mobile crisis, ED, on-call clinician).
6. **Making the environment safer** — restricting access to lethal means.

The plan must also include a **reasons for living** anchor and a **review date**.

## When to Use

- Any encounter following a positive C-SSRS or other suicide-risk indicator.
- After ED evaluation, hospital discharge, or post-attempt re-entry.
- During or immediately after the Columbia risk assessment as the matched intervention.
- Refresh whenever clinical state, supports, means, or stressors change.
- Building plan with a parent / guardian for a minor (age-adapted).

## Inputs / Context

- Risk-assessment summary linked to this plan (Columbia or comparable).
- Client's stated and observable warning signs (thoughts, feelings, situations, behaviors).
- Internal coping strategies the client is willing to try (with at least one already-used coping skill if any).
- Social contacts/settings client is willing to use as distraction (not the same as people-for-help).
- Trusted people the client is willing to disclose distress to (verify willingness with the contact when possible).
- Professionals and agencies: client's clinician contact, on-call coverage, 988, local crisis line, mobile crisis team, nearest ED.
- Means access: firearms, lethal medications, other; client and family willingness to remove/secure; specific plan for each.
- Reasons for living, in client's own words.
- Literacy / language / accessibility considerations; minor / guardian involvement.
- Storage plan: paper, phone (locked screen accessible), EHR portal, family copy.

## Constraints

### Must

- Output the safety plan in the canonical 6-step Stanley-Brown order with explicit step labels.
- Each step has 3–5 specific, client-stated items (not generic). Step 5 always includes 988 and the local emergency-services number.
- Step 6 (Means Safety) is always present and addresses every means the client has access to. If means cannot be removed, document the harm-reduction plan (e.g., gun lock, off-site storage, reduced quantities of medication, lockbox, partner-held key).
- Include the client's **Reasons for Living** as a top-of-plan anchor in client's own words.
- Include a **Review date** within 1–4 weeks (sooner for higher acute risk) and the trigger conditions for an earlier review.
- Use language and reading level appropriate for the client (default to ~8th-grade reading; adjust for minor / cognitive impairment / non-native language).
- Document the building process: how long the plan took to build; client engagement; barriers encountered; any items the client refused to include.
- Verify with client that they will carry/access the plan and will use it in order (not skip to step 5 first); the hierarchy is core to the intervention.
- Document who else has a copy (with consent and ROI for any clinical share).

### Must Not

- Do not use a "no-suicide contract" or a promise-based document; SPI replaces it.
- Do not skip Step 6 (Means Safety) under any circumstances.
- Do not list generic items ("call a friend"). Each item is specific (named friend, named coping skill, named place).
- Do not list a person without verifying client's willingness to actually contact them; if unverified, mark "[client to confirm]."
- Do not list 988 or crisis line without confirming the client knows how to access (call/text/chat) and ideally has rehearsed it.
- Do not omit the client's reasons for living.
- Do not finalize a plan the client does not believe in; document refusal/reluctance and adjust risk plan / disposition accordingly.

## Instructions

1. Anchor: ask the client for their reasons for living; record verbatim.
2. **Step 1 — Warning Signs:** elicit specific personal warning signs (e.g., "I start cleaning my apartment compulsively at 2 a.m." or "I stop returning my sister's calls"). Aim for 3–5.
3. **Step 2 — Internal Coping:** elicit 3–5 things the client can do alone, without contacting anyone. Prefer skills they've used successfully in the past.
4. **Step 3 — Social Distraction:** people and settings that take their mind off crisis without requiring disclosure (gym, grandmother's house, dog walk, specific friend who's good for normal-life talk).
5. **Step 4 — People for Help:** people the client will tell about the crisis. Verify willingness if possible (call together in session when appropriate).
6. **Step 5 — Professionals and Agencies:** primary clinician + after-hours coverage, 988 (call/text/chat), local crisis line, mobile crisis team, nearest ED, with addresses and numbers.
7. **Step 6 — Means Safety:** for each means the client has access to, document a specific reduction plan. For firearms, name a specific person who will hold them and the date by which transfer will occur, or specific lock/storage if removal not possible. For medications, document quantity reduction, lockbox, partner-held key.
8. Summarize barriers, refusals, and rehearsal status (did the client practice using the plan in session?).
9. Set the review date and trigger conditions for earlier review.
10. Document storage / who has copies.
11. Run verification.

## Output Format

```
=== SAFETY PLAN (Stanley-Brown) ===

Client: [Initials/MRN]    DOB: [age, gender, pronouns]
Date created: [YYYY-MM-DD]    Built with: [Clinician name, credentials]
Review date: [YYYY-MM-DD]    Earlier review trigger: [Specific conditions — e.g., "If PHQ-9 ≥ 15, or ED visit, or alcohol use resumes."]

REASONS FOR LIVING (in your own words)
- "[client's verbatim reason]"
- "[...]"
- "[...]"

STEP 1 — WARNING SIGNS (when I'm starting to slip)
- [Specific thought / feeling / situation / behavior]
- [...]
- [...]

STEP 2 — INTERNAL COPING (things I can do on my own)
- [Specific coping skill #1 — when and where I'll use it]
- [...]
- [...]
- [...]

STEP 3 — SOCIAL DISTRACTION (people / places that take my mind off it; I do not need to talk about the crisis)
- [Specific person, with role: "Aunt Mara — chat about the garden"]
- [Specific place: "the dog park at 6 p.m."]
- [...]

STEP 4 — PEOPLE I WILL ASK FOR HELP (people I'll tell what's going on)
- [Name — relationship — phone — willingness verified Y/N]
- [...]
- [...]

STEP 5 — PROFESSIONALS AND AGENCIES TO CONTACT
- My clinician: [Name] — [Phone] — Hours: [...]
- After-hours / on-call: [Name or service] — [Phone] — Hours: [...]
- 988 Suicide & Crisis Lifeline — Call or text **988**, chat at 988lifeline.org. I have practiced reaching it: [Y/N]
- Local crisis line / mobile crisis: [Name] — [Phone] — coverage area: [...]
- Nearest ED: [Hospital name] — [Address] — [Phone]
- 911 if life-threatening; if I want to specifically request a mental-health response, I will say: "I am having a mental health crisis."

STEP 6 — MAKING THE ENVIRONMENT SAFER (means safety)
Firearms:
- [Specific plan: e.g., "Brother John will pick up the rifle and shotgun by [date]; client signed handoff."]
- [If not removable: "Cable lock + ammunition stored separately at [location]; client agrees not to keep loaded; rationale: ..."]
Medications:
- [Specific plan: e.g., "Lockbox in closet; partner holds key; weekly pill organizer only on counter."]
- [Quantity reduction: "Pharmacy will dispense 7-day supply rather than 30."]
Other means:
- [Plan for each accessible means.]

PLAN BUILDING PROCESS
- Time spent: [N min]
- Client engagement: [Engaged / Reluctant / Refused parts — specify]
- Items declined or modified: [...]
- Rehearsal in session: [Yes / No — what was practiced]
- Plan stored: [Paper given / Phone photo / EHR portal / Copy with [trusted person] with consent]

CLINICIAN'S NOTE
- Plan completed in conjunction with risk assessment dated [YYYY-MM-DD].
- Client agrees to use the plan in order (Step 1 → Step 6).
- Means restriction follow-through: [Status; verification plan].
- Coordination: [Family member / partner / PCP / prescriber notified per ROI].
- Next session: [Date / frequency increase if applicable].
- Risk stratification at time of plan: [Low / Moderate / High] — see Columbia assessment for rationale.

Clinician: __________________  Date/Time: ___________
Client (acknowledgment): _____  Date: ___________
Guardian (if minor): __________  Date: ___________
```

## Verification

- [ ] Reasons for living anchor present in client's own words.
- [ ] All 6 steps in canonical order with specific (not generic) items.
- [ ] Step 4 (People) marks willingness verification status per contact.
- [ ] Step 5 (Professionals) includes 988, local crisis line, ED, and confirms client knows how to access.
- [ ] Step 6 (Means Safety) addresses every means client has access to, with a concrete plan.
- [ ] Review date within 1–4 weeks; earlier-review triggers specified.
- [ ] Plan-building process documented (time, engagement, rehearsal, storage).
- [ ] Cross-reference to risk assessment.
- [ ] No "no-suicide contract" or promise language.
- [ ] No generic items.
- [ ] Linked to lethal-means counseling note when relevant.
- [ ] Gaps flagged; nothing fabricated.
