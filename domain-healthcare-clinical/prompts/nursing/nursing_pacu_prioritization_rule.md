---
title: "PACU Phase 1 Prioritization Rule Card"
category: nursing
description: "Default clinical-priority hierarchy and collision rules for a Phase 1 PACU orientee — a decision scaffold for when two or more demands compete for attention simultaneously."
techniques:
  - DS-06
  - ST-40
  - ST-42
  - DS-02
difficulty: beginner
tags:
  - nursing
  - PACU
  - orientation
  - prioritization
  - clinical-decision
  - cognitive-load
  - pocket-card
updated: "2026-04-16"
related_prompts:
  - domain-healthcare-clinical/prompts/nursing_pacu_shift_structure.md
  - domain-healthcare-clinical/prompts/nursing_preceptor_daily_debrief.md
  - domain-healthcare-clinical/prompts/nursing_sbar_clinical_escalation.md
  - domain-decision-making/decisioning_resource_constrained_solver.md
---

# PACU Phase 1 Prioritization Rule Card

**Objective:** Give a PACU orientee a default decision hierarchy for when two or more clinical demands compete for her attention at the same time. The card replaces the paralysis of "everything is urgent" with a repeatable stack: handle the higher-tier item first, delegate or defer the lower-tier item, and never let documentation displace clinical care.

**Important Disclaimer:** This card reflects general Phase 1 PACU clinical priorities. Facility-specific protocols, standing orders, and provider direction supersede this hierarchy. Clinical judgment always overrides a card.

---

## Your Role

You are generating a personalized prioritization rule card for a PACU orientee. The card encodes a tiered priority hierarchy with specific collision rules — if/then decision points for the most common situations where two demands hit at the same time.

---

## Input Required

- **Unit staffing model:** {{1:1 / 1:2 / variable — affects delegation options}}
- **Delegation resources available:** {{second RN, tech, charge nurse, anesthesia at bedside}}
- **Common collision scenarios on this unit:** {{e.g., "new patient arriving while current patient has uncontrolled pain," "two patients desatting," "surgeon calling while patient is nauseated"}}
- **Unit-specific standing orders or protocols that affect priority:** {{e.g., "PONV protocol allows RN to administer ondansetron without calling," "all regional blocks get q15 neuro checks"}}

---

## Framework

### The Priority Stack

Tier 1 through Tier 6, highest to lowest. When two demands from different tiers collide, the higher tier wins. When two demands are in the same tier, the collision rules apply.

---

**TIER 1 — LIFE THREAT (act immediately, nothing waits)**
- Airway obstruction or loss of airway patency
- Apnea or respiratory arrest
- Cardiac arrest / pulseless
- Anaphylaxis
- Massive hemorrhage with hemodynamic instability

*Rule: Call for help while you act. Do not finish anything else first. Do not document first.*

---

**TIER 2 — ACUTE INSTABILITY (act within minutes)**
- Significant desaturation (SpO₂ trending below unit threshold despite intervention)
- Hemodynamic instability (hypotension, bradycardia, tachycardia outside recovery norms)
- Acute mental status change (not explained by expected emergence)
- Laryngospasm (partial or complete)
- Suspected malignant hyperthermia signs

*Rule: Stabilize before anything else. Delegate Tier 3–6 tasks. Call anesthesia or rapid response per unit protocol.*

---

**TIER 3 — ACTIVE SYMPTOM MANAGEMENT (act within 5–10 minutes)**
- Uncontrolled pain (patient reporting ≥7/10 or exhibiting distress)
- Active vomiting or severe nausea unresponsive to initial treatment
- Significant hypothermia or shivering
- Acute urinary retention causing distress
- New bleeding at surgical site (not hemodynamically significant)

*Rule: Treat before documenting. If a Tier 3 and a Tier 4 collide, treat the Tier 3 and defer the Tier 4.*

---

**TIER 4 — ROUTINE RECOVERY MANAGEMENT (act within 15–30 minutes)**
- Scheduled vitals (q5, q15 per standard)
- Routine pain reassessment after intervention
- Mild nausea (controlled, patient not distressed)
- Family communication / visitor updates
- IV fluid rate adjustments (non-urgent)
- Routine post-op teaching

*Rule: Can be briefly deferred for Tier 1–3 demands. Should not be skipped entirely — set a mental timer or write a sticky note.*

---

**TIER 5 — DOCUMENTATION (do after clinical care is stable)**
- Charting assessments, interventions, and responses
- Completing medication administration records
- Updating handoff notes
- Entering I&O

*Rule: Documentation is critical — but never at the expense of Tiers 1–4. Chart after you've stabilized, treated, and reassessed. A late-but-accurate chart is better than a timely chart written while the patient was ignored.*

---

**TIER 6 — ANCILLARY (do when everything else is done)**
- Restocking supplies
- Cleaning / organizing bay
- Returning calls to non-urgent consults
- Coordinating transport for stable discharge

*Rule: These fill gaps. They never displace clinical care or documentation.*

---

### Collision Rules: Common Same-Tier and Cross-Tier Scenarios

| Scenario | Rule |
|----------|------|
| **New patient arriving + current patient needs pain med** | If pain med takes ≤2 min (push dose), medicate first, then receive. If it requires titration, delegate receipt to backup RN, manage pain, then take over. |
| **Two patients: one desatting, one in pain** | Desaturation wins (Tier 2 > Tier 3). Call for help for the pain patient, manage the airway. |
| **Surgeon calling + patient is actively vomiting** | Patient wins. Tell the surgeon you'll call back in 5 minutes, or ask charge to take the call. |
| **New patient arriving + you haven't finished charting the last one** | Receive the new patient (Tier 2–3 potential). Chart the prior patient in the gap after initial assessment. |
| **Two patients need scheduled vitals at the same time** | The less stable patient first. If both stable, the one closest to discharge first (completes the cycle faster). |
| **Family asking questions + you need to do a neuro check** | Neuro check first (clinical > communication). Brief the family: "Give me 2 minutes, then I'm all yours." |
| **You're unsure which tier something belongs to** | Assume one tier higher than you think. Over-prioritizing is safer than under-prioritizing. If still unsure, ask your preceptor or charge nurse — that's not weakness, that's safety. |

---

## Output Format

```
PACU PRIORITIZATION RULE — POCKET CARD
========================================

TIER 1 — LIFE THREAT → Act NOW. Call for help while acting.
  Airway loss | Apnea | Arrest | Anaphylaxis | Massive hemorrhage
  → Nothing else happens until this is resolved.

TIER 2 — ACUTE INSTABILITY → Act within minutes. Delegate everything else.
  Desaturation | Hemodynamic instability | Acute MS change | Laryngospasm
  → Stabilize. Call anesthesia / rapid response.

TIER 3 — ACTIVE SYMPTOMS → Act within 5–10 min. Treat before charting.
  Uncontrolled pain | Active vomiting | Hypothermia/shivering
  → Treat. Then document. Don't chart while they suffer.

TIER 4 — ROUTINE RECOVERY → Within 15–30 min. Defer briefly if needed.
  Scheduled vitals | Routine reassessment | Mild nausea | Family updates
  → Can wait for T1–T3. Don't skip — set a reminder.

TIER 5 — DOCUMENTATION → After clinical care is stable.
  Charting | MAR | Handoff notes | I&O
  → Critical but never displaces T1–T4. Accurate > timely.

TIER 6 — ANCILLARY → When everything else is done.
  Restocking | Bay cleanup | Non-urgent calls | Transport coordination
  → Fills gaps. Never displaces clinical care.

COLLISION QUICK-RULES
---------------------
  Different tiers collide → Higher tier wins. Always.
  Same tier collide     → Less stable patient first.
  Unsure which tier?    → Assume one tier higher. Ask if still unsure.
  Can I delegate?       → Yes. Charge, backup RN, tech. Delegating is not failing.

THE ONE RULE
------------
  Clinical care > Documentation > Everything else.
  A patient who is safe and undocumented is recoverable.
  A patient who is documented and unsafe is not.
```

---

## Must / Must Not

**Must:**
- Present tiers in numbered descending priority (1 = highest)
- Include at least 4 collision scenarios relevant to Phase 1 PACU
- Include the decision rule for "unsure which tier" — defaults to escalate, not defer
- Include explicit permission to delegate and explicit naming of who can be delegated to
- Fit on a single printed page (front and back) in pocket-card format

**Must Not:**
- Include drug doses or specific medications — those belong in unit protocols
- Override facility-specific escalation protocols or standing orders
- Imply that the orientee should handle Tier 1 events alone — calling for help is always the first action
- Treat documentation as unimportant — it is Tier 5, not optional; the hierarchy is about sequencing, not value
- Include more than 6 tiers — cognitive load increases with tier count, and 6 is the practical ceiling

---

## Special Considerations

**The documentation trap:** Orientees who came from settings where documentation was concurrent with care (hospice, clinic, jail) may default to charting during active management. The card explicitly names documentation as Tier 5 to interrupt this pattern — not because documentation is unimportant, but because PACU acuity demands a different sequencing than lower-acuity settings.

**The "everything is Tier 1" perception:** Anxiety makes everything feel urgent. The card's primary function is to break that perception by giving concrete criteria for each tier. If the orientee is classifying routine vitals as Tier 2, that's a signal to the preceptor that anxiety is compressing the hierarchy — address it in the daily debrief.

**Delegation discomfort:** Orientees — especially those from settings where they worked alone (jail nursing, home hospice) — may be uncomfortable delegating. The card explicitly names delegation as a tool, not a failure. Reinforce this in preceptor conversations.

**When two Tier 1 events happen simultaneously:** Call a code / rapid response. This is not a prioritization problem — it is a staffing problem. The card does not solve staffing; it tells the orientee to get help.

---

## Verification / Self-Check

- [ ] Six tiers present, numbered and named
- [ ] Each tier includes 3–5 specific clinical examples
- [ ] Each tier includes a timing rule (act now / within minutes / within 5–10 min / etc.)
- [ ] At least 4 collision scenarios with explicit decision rules
- [ ] "Unsure which tier" defaults to escalation
- [ ] Delegation explicitly permitted and named
- [ ] Pocket-card format fits one printed page (front/back)
- [ ] No drug doses or facility-specific protocols embedded
- [ ] Documentation explicitly positioned as important but sequenced after clinical care

---

**Critical Reminder:** Prioritization paralysis in new PACU nurses is almost never a knowledge problem — she knows airway matters more than charting. It is a working-memory problem: under load, the brain cannot hold competing demands and rank them simultaneously. The card offloads the ranking to paper so the brain can focus on executing. When the ranking becomes reflexive, the card retires. Until then, it is the external working memory she doesn't have to build.
