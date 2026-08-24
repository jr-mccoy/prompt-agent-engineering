---
title: "High-Conflict Parenting Coordination Provisions"
category: legal/custody
description: "Draft high-conflict co-parenting provisions for a parenting plan: a parenting-coordinator appointment and authority, a structured communication protocol (approved app, business-like tone, response windows), detailed exchange logistics with neutral locations and check-in, a decision tie-breaker and escalation ladder, documentation rules, and graduated enforcement — designed to reduce conflict exposure for the child and minimize return trips to court, sized to the controlling state's PC authority."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - custody
  - family-law
  - high-conflict
  - parenting-coordinator
  - communication-protocol
updated: "2026-06-01"
related_prompts:
  - domain-legal/custody/legal_parenting_plan_drafter.md
  - domain-legal/custody/legal_holiday_and_vacation_schedule_builder.md
  - domain-legal/custody/legal_parenting_time_enforcement_and_contempt_motion.md
  - domain-legal/custody/legal_supervised_visitation_and_safety_plan.md
  - domain-legal/custody/legal_custody_modification_analysis_and_motion.md
---

**Purpose:** Draft the provisions a high-conflict co-parenting arrangement needs to function — a parenting coordinator, a tightly structured communication and exchange protocol, a decision tie-breaker, and graduated enforcement — so conflict is contained, the child is insulated, and disputes are resolved without constant court intervention. Output is a set of plan provisions for incorporation, not a memo.

**When to use:** Chronic co-parenting conflict, repeated disputes or enforcement motions, communication breakdown, or a case where a standard parenting plan keeps failing; designing the parenting plan for a known high-conflict pair.

---

## Your Input

- **Jurisdiction:** [State; whether/how parenting coordinators are authorized, their permitted authority, and any required consent `[CITE: …]`]
- **Conflict history:** [Patterns — late exchanges, communication hostility, unilateral decisions, disparagement, repeated motions]
- **Child(ren):** [Names, ages, sensitivity to conflict, special needs]
- **Decision categories:** [Where disagreements recur — schedule changes, medical, school, activities]
- **Exchange issues:** [Specific recurring problems at exchanges]
- **Communication tools:** [Whether a co-parenting app is in use or proposed]
- **Safety overlay:** [Any DV/abuse limiting direct contact]
- **Prior orders:** [Existing plan terms that have failed]

---

## Constraints

**Must:**
- Confirm the **state's authority for a parenting coordinator** — scope of decisions a PC may make, whether binding, the appointment mechanism, and any **consent** requirement `[CITE: …]`; do not assign a PC authority the state does not allow (e.g., changing legal custody).
- Provide a **structured communication protocol**: a single approved channel (e.g., a co-parenting app with a record), **business-like/BIFF tone**, defined **response windows**, and topics limited to the child.
- Provide **detailed exchange logistics**: neutral/public or curbside locations, exact times, a grace period, a no-show protocol, and check-in/documentation — minimizing direct contact where conflict or safety requires.
- Include a **decision tie-breaker and escalation ladder** (direct → app → PC/mediation → court) so disputes have a path short of litigation.
- Include **documentation rules** (records via the app), an **anti-disparagement** clause, and **graduated enforcement** (make-up time, fees, PC referral, contempt).
- Keep provisions **child-centered** — explicitly insulating the child from conflict and messenger duty.
- Where a **safety overlay** exists, coordinate with supervised exchange/visitation rather than direct contact.
- Use placeholders `[CITE: ...]`, `[NEED: ...]` for unsupplied PC authority or facts.

**Must Not:**
- Give a PC authority to modify legal/physical custody where the state reserves that to the court.
- Create a protocol so rigid it is unworkable or invites new disputes.
- Use the child as a messenger or require child involvement in conflict.
- Ignore a DV/safety dynamic by mandating direct communication/exchanges.
- Invent the state's PC statute or authority.
- Insert generic "consult counsel" disclaimers.

---

## Instructions

1. **PC authority.** State the state's PC framework; define the PC's scope, term, cost-sharing, and the consent basis `[CITE: …]`.
2. **Communication protocol.** Approved channel, tone rules, response windows, child-only topics, emergency exception.
3. **Exchange logistics.** Locations, exact times, grace period, no-show protocol, documentation, minimized contact.
4. **Decision tie-breaker & escalation.** Ladder from direct discussion to PC/mediation to court; specify which decisions go where.
5. **Documentation & anti-disparagement.** Records via the app; no disparagement; no child as messenger.
6. **Graduated enforcement.** Make-up time, fee-shifting, PC referral, contempt — in escalating order.
7. **Safety coordination.** Integrate supervised exchange/visitation where a safety overlay exists.

---

## Output Format

```markdown
HIGH-CONFLICT CO-PARENTING PROVISIONS — {Child(ren)}

1. PARENTING COORDINATOR. The parties {appoint/stipulate to} a PC under {state authority [CITE: …]}. Scope: {resolve day-to-day disputes within the plan; recommend on {categories}}; the PC may not modify legal or physical custody. Term: {…}; cost: {split/allocated}; consent: {…}.

2. COMMUNICATION. All co-parenting communication occurs via {approved app}. Tone is business-like (BIFF: brief, informative, friendly, firm). Response within {N hours} for non-urgent, {immediately} for child emergencies. Topics limited to the child. No disparagement; the child is never a messenger.

3. EXCHANGES. Location: {neutral/curbside/public}; times: {exact}; grace period {N min}; no-show protocol {…}; documented via {app/check-in}. {Supervised/neutral exchange if safety overlay.}

4. DECISION TIE-BREAKER & ESCALATION. (1) Direct discussion → (2) app proposal/response → (3) PC/mediation → (4) Court. {Which decisions route to PC vs. court.}

5. DOCUMENTATION & CONDUCT. Records maintained in {app}; anti-disparagement; no involving the child in disputes.

6. ENFORCEMENT (graduated). {Make-up time → fee-shifting → PC referral → contempt}.

7. SAFETY COORDINATION. {Supervised exchange/visitation terms; no direct contact where ordered.}
```

---

## Verification

- [ ] PC authority conforms to the state's framework; PC cannot modify custody.
- [ ] Communication protocol: single channel, tone rules, response windows, child-only topics.
- [ ] Exchange logistics specify location, exact times, grace period, no-show protocol, documentation.
- [ ] Decision tie-breaker and escalation ladder defined with routing.
- [ ] Documentation, anti-disparagement, and no-messenger rules included.
- [ ] Graduated enforcement specified.
- [ ] Safety overlay integrated where applicable.
- [ ] Provisions child-centered and workable; no invented PC authority.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Giving the PC power to change custody | Limit PC authority to what the state allows; custody stays with the court |
| Vague communication rules | Specify channel, tone, response windows, and child-only topics |
| Exchanges that require hostile direct contact | Use neutral/curbside locations and minimize contact; supervise if needed |
| No escalation path short of court | Provide a tie-breaker ladder (direct → app → PC → court) |
| Using the child as a messenger | Prohibit it explicitly; route all communication through the adults' channel |
| Ignoring a DV/safety dynamic | Integrate supervised exchange/visitation; do not mandate direct contact |
| Protocol so rigid it breeds new disputes | Keep it workable; include grace periods and reasonable exceptions |
| Inventing the state's PC statute | Use [CITE]/[NEED] placeholders |
| One-step enforcement (straight to contempt) | Provide graduated remedies before contempt |
| No documentation method | Require records via the approved app |
