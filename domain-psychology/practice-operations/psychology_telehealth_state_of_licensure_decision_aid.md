---
title: "Telehealth State-of-Licensure Decision Aid"
category: psychology/practice-operations
description: "Decide whether you may legally see a telehealth client based on the CLIENT's physical location at session time — covering PSYPACT (E.Passport/APIT), temporary-practice exceptions, emergency carve-outs, and required documentation of client location and a local safety contact."
techniques:
  - RT-02
  - DT-01
  - DS-02
  - CM-02
  - QA-04
difficulty: intermediate
intended_use: model-testing
tags:
  - telehealth
  - licensure
  - PSYPACT
  - cross-state-practice
  - jurisdiction
  - client-location
updated: "2026-06-08"
related_prompts:
  - domain-psychology/practice-operations/psychology_informed_consent_template_builder.md
  - domain-psychology/practice-operations/psychology_insurance_verification_intake_protocol.md
  - domain-psychology/documentation/psychology_telehealth_session_note.md
  - domain-psychology/supervision-professional/psychology_scope_of_practice_decision_aid.md
---

# Telehealth State-of-Licensure Decision Aid

## Objective

Determine whether a clinician may lawfully provide a telehealth session to a specific client at a specific time, given the controlling rule of telepractice: **licensure is determined by the client's physical location at the moment of the session, not the provider's location and not the client's "home" state.** The aid walks the licensure pathways — full licensure in the client's state, PSYPACT authority (E.Passport + APIT) for psychologists, temporary/short-term practice exceptions, and narrow emergency carve-outs — and produces a GO / CONDITIONAL / NO-GO determination plus the documentation that must appear in the record (verified client location, a local emergency contact, and a location-specific safety plan).

## When to Use

- A client tells you they will be physically in a different state (travel, relocation, college, snowbird season) for an upcoming session.
- Onboarding a new telehealth client whose physical location differs from the practice's state.
- A client moves permanently to a state where the clinician is not licensed.
- Verifying, before each session, that the client is in a state where you are authorized to practice.
- Deciding whether PSYPACT authority covers an upcoming out-of-state session.

## Inputs / Context Required

- **Provider's licenses**: profession (psychologist / LCSW / LPC / LMFT, etc.), each state of licensure, and whether the clinician holds PSYPACT authority (E.Passport + APIT) — note: PSYPACT is for **psychologists** and applies only between **PSYPACT-participating states**.
- **Client's physical location at session time**: the state (and country) the client will physically be in during the session — not their mailing address or "home" state.
- **Session type**: routine ongoing therapy vs. a one-time/crisis contact vs. initial intake.
- **Anticipated duration in that location**: a single session, a defined short trip, or a permanent move.
- **Existing therapeutic relationship**: new client vs. established client temporarily traveling.
- **Local emergency resources for the client's location**: nearest crisis line, emergency services, and a local emergency contact person.
- `[clinician input required: current participation status of the client's state in PSYPACT, and that state's specific temporary-practice / out-of-state-telehealth rule — these change and must be checked against the licensing board, ASPPB PSYPACT map, or counsel]`
- `[clinician input required: whether the client's state requires a separate telehealth registration/permit even for a PSYPACT or temporary-practice provider]`

## Constraints

### Must

- Anchor the entire analysis to the **client's physical location at session time**; restate this rule explicitly in the output.
- Evaluate, in order, the available legal pathways: (1) full licensure in the client's state; (2) PSYPACT authority (psychologists only, between participating states); (3) a temporary / short-term out-of-state practice exception in the client's state; (4) a narrow emergency carve-out.
- Treat PSYPACT correctly: it is for **psychologists**, requires an **E.Passport** and **Authority to Practice Interjurisdictional Telepsychology (APIT)**, and both the provider's home state and the client's state must be **PSYPACT-participating**.
- For non-psychologist professions (LCSW/LPC/LMFT/etc.), do **not** apply PSYPACT; route to that profession's own compact (e.g., Counseling Compact, Social Work Compact) or to full licensure / temporary-practice rules, flagged for verification.
- Require **verification and documentation of the client's physical location at the start of each session**.
- Require a **location-specific safety plan**: local crisis resources and a local emergency contact for the client's actual physical location (988 routes nationally, but local emergency services and a local contact are required).
- Output a clear determination: **GO**, **CONDITIONAL** (proceed only after a named step), or **NO-GO** (do not hold the session under current authority), with the reason.
- For NO-GO, state the alternatives: obtain licensure, refer to an in-state provider, reschedule to when the client is back in a covered state, or use an emergency carve-out only if its narrow criteria are met.

### Must Not

- Do not base authority on the provider's location or on the client's "home"/mailing state when the client is physically elsewhere.
- Do not assume PSYPACT or any compact covers a session without confirming both states participate and the provider holds the specific authority (APIT for PSYPACT).
- Do not apply PSYPACT to a non-psychologist.
- Do not treat an emergency carve-out as a routine workaround for ongoing therapy; carve-outs are narrow, time-limited, and jurisdiction-specific.
- Do not omit documentation of verified client location and local emergency resources.
- Do not fabricate a state's PSYPACT-participation status or its temporary-practice rule; flag with `[clinician input required]`.

## Instructions

1. **State the controlling rule**: licensure follows the client's physical location at session time. Record where the client will physically be.
2. **Profession gate**: identify the provider's profession. If psychologist, PSYPACT is a candidate pathway; if not, route to the relevant compact or licensure/temporary-practice analysis (PSYPACT does not apply).
3. **Pathway 1 — full licensure**: is the provider fully licensed in the client's state? If yes → likely GO (still document location + safety resources).
4. **Pathway 2 — PSYPACT** (psychologists only): does the provider hold E.Passport + APIT, and are both the provider's home state and the client's state PSYPACT-participating? Confirm both; if yes → GO under PSYPACT. If either state does not participate, or APIT not held → PSYPACT unavailable.
5. **Pathway 3 — temporary / short-term practice exception**: does the client's state offer a temporary out-of-state telehealth practice allowance (often day-limited per year, sometimes requiring registration)? If applicable and conditions met → CONDITIONAL or GO per its terms.
6. **Pathway 4 — emergency carve-out**: only if the contact is genuinely emergent and the client's state recognizes a narrow emergency exception; document the emergency and the carve-out relied upon. Not a substitute for ongoing care.
7. **If no pathway applies → NO-GO**: state the alternatives (licensure, in-state referral, reschedule when client returns to a covered state).
8. **Documentation block**: record verified client physical location at session start, the legal pathway relied upon, and a location-specific safety plan (local crisis resources + local emergency contact).
9. Run verification.

## Output Format

```
=== TELEHEALTH STATE-OF-LICENSURE DETERMINATION ===

CONTROLLING RULE
Authority is determined by the CLIENT's physical location at session time.
Client's physical location this session: [State / Country]
Provider profession: [Psychologist / LCSW / LPC / LMFT / other]
Provider licensure: [State(s) licensed]   PSYPACT authority (E.Passport + APIT): [Yes/No/N-A]

PATHWAY ANALYSIS
[ ] Pathway 1 — Full licensure in client's state: [Yes/No] → [result]
[ ] Pathway 2 — PSYPACT (psychologists only):
       Provider holds E.Passport + APIT: [Yes/No]
       Provider home state participates: [Yes/No]  [clinician input required: confirm]
       Client's state participates: [Yes/No]       [clinician input required: confirm]
       → [Available / Not available]
[ ] Pathway 3 — Temporary/short-term out-of-state practice exception:
       Client's state allows: [Yes/No/Unknown]  [clinician input required: rule + day limit + registration?]
       Conditions met: [Yes/No]
[ ] Pathway 4 — Emergency carve-out (narrow, jurisdiction-specific):
       Genuine emergency: [Yes/No]   Carve-out relied upon: [describe]  [clinician input required]

DETERMINATION
[ GO | CONDITIONAL | NO-GO ]
Pathway relied upon: [name]
Reason: [1–2 sentences]
If CONDITIONAL — required step before the session: [...]
If NO-GO — alternatives: [Obtain licensure | Refer to in-state provider | Reschedule when client returns to covered state | Emergency carve-out only if criteria met]

REQUIRED DOCUMENTATION (each session)
Verified client physical location at session start: [State, how verified]
Legal pathway documented in note: [Yes]
Location-specific safety plan:
   - Local emergency services: 911 (or local equivalent)
   - Crisis line: 988 (national) + [local crisis resource for client's location]
   - Client's local emergency contact: [name, phone]
   - Nearest ER / facility to client's location: [...]
```

## Verification

- [ ] Determination anchored to the client's physical location at session time (rule restated).
- [ ] Provider profession gate applied; PSYPACT used only for psychologists between participating states with E.Passport + APIT.
- [ ] Pathways evaluated in order (full licensure → PSYPACT → temporary-practice → emergency carve-out).
- [ ] Non-psychologist professions routed to the correct compact / licensure analysis, not PSYPACT.
- [ ] Emergency carve-out treated as narrow and time-limited, not a routine workaround.
- [ ] GO / CONDITIONAL / NO-GO determination stated with reason and (for NO-GO) alternatives.
- [ ] Documentation block requires verified client location each session.
- [ ] Location-specific safety plan includes local emergency services and a local emergency contact (not only 988).
- [ ] PSYPACT-participation status and temporary-practice rules flagged `[clinician input required]` rather than asserted.
- [ ] Nothing fabricated about any state's rules.
```
