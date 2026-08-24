---
title: PACU Obstetric Considerations (Post-Cesarean, Post-OB-Anesthesia)
category: pacu/population-specialty
task_type: LEARN
audience: PACU orientee or preceptor rotating into (or being cross-trained on) obstetric PACU recovery
updated: "2026-04-16"
tags:
  - pacu
  - obstetric
  - cesarean
  - population-specialty
  - hemorrhage
  - neuraxial
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-02
  - ED-02
  - DS-06
difficulty: advanced
related_prompts:
  - prompts/pacu_topic_primer.md
  - prompts/pacu_complication_deep_dive.md
  - prompts/pacu_medication_profile.md
  - prompts/pacu_handoff_script.md
  - prompts/pacu_simulation_scenario_builder.md
  - prompts/pacu_unfolding_case_study.md
references:
  - Drain's PeriAnesthesia Nursing Practice (7th ed.) — OB chapters
  - ASPAN Standards of Perianesthesia Nursing Practice — obstetric population
  - ACOG / SMFM guidance on postpartum hemorrhage (for awareness; facility protocol governs)
  - AWHONN Standards for Professional Registered Nurse Staffing
---

# PACU Obstetric Considerations

> Safety reminder: Obstetric PACU recovery involves rapid hemodynamic shifts, hemorrhage surveillance, neuraxial block recovery, and mother-baby communication. All doses and thresholds are per provider order and facility protocol. Postpartum hemorrhage pathways and uterotonic dosing vary by facility and patient — never invent; defer to facility OB / obstetric anesthesia protocols.

## Objective

Produce an **obstetric-specific PACU considerations teaching artifact** for a PACU nurse recovering post-cesarean, post-other-OB-surgery, or post-labor-epidural-complication patients. Covers what differs from general post-op PACU: hemorrhage surveillance (including postpartum-specific patterns), neuraxial block recovery, post-dural-puncture headache (PDPH) recognition, breastfeeding-compatible analgesia framing, and handoff to mother-baby / postpartum unit.

## When to use

- Orientation or cross-training for a PACU nurse covering obstetric recovery (dedicated OB PACU, mixed-surgical PACU that accepts cesarean recoveries, or overflow coverage).
- Pre-read before an OB-focused simulation.
- Refresher for preceptors mentoring on OB cases.

## When not to use

- For antepartum or intrapartum labor management — those are L&D-scope and outside PACU.
- For neonatal care — neonate goes to nursery / NICU per facility, not PACU.
- For general post-op — use `pacu_topic_primer.md`.

## Inputs

- **Rotation context:** {{dedicated OB PACU | mixed PACU accepting post-cesarean | overflow coverage}}
- **Case type focus:** {{scheduled cesarean | emergent cesarean | post-spinal / post-epidural complication recovery (non-surgical) | post-other-OB-surgery (D&E, hysterectomy, etc.)}}
- **Learner's PACU experience level:** {{Phase 1 orientee | experienced PACU RN cross-training}}
- **Source chapters available:** {{Drain's OB chapters, ASPAN OB module, facility OB protocols}}

## Audience / Scope

- **Primary:** PACU nurse recovering post-OB-surgical / post-OB-anesthesia patients.
- **Scope:** Differences from general post-op PACU. Not a comprehensive L&D orientation; not a substitute for facility OB-specific training or AWHONN-aligned postpartum nursing orientation.

## Output requirements

```markdown
# Obstetric PACU Considerations — {case type}

> Safety reminder: Hemorrhage surveillance, uterotonic doses, anticoagulation thresholds, and neuraxial recovery parameters all per provider order and facility OB protocol. Postpartum hemorrhage is time-critical — escalate early and by role.

## What's different from general PACU (at a glance)
| Domain | General PACU default | Obstetric PACU difference |
|---|---|---|
| Hemorrhage surveillance | Surgical site + vitals + I/O trending | **Fundal assessment + lochia + vitals + I/O** — postpartum hemorrhage can be occult; vitals compensate longer in healthy peripartum patients |
| Hemodynamics | BP trend recognizable early | Peripartum patients tolerate significant volume loss before vitals shift ("young and healthy" masks early loss) |
| Neuraxial recovery | Block resolves; monitor for residual | Post-spinal / post-epidural motor and sensory recovery tracked; anticoagulation timing matters for catheter removal |
| Pain | Multimodal per order | Breastfeeding-compatibility considered; often NSAID + acetaminophen scheduled, opioids rescue (per order) |
| Communication | Patient + family | Patient + partner + sometimes extended family + coordination with mother-baby unit for infant status |
| Emotional state | Post-op fatigue common | Emotional spectrum wider: exhaustion, euphoria, disappointment, grief (depending on outcome); postpartum blues / depression risk on radar |
| Handoff destination | Floor / ICU / home | Often mother-baby unit with concurrent infant in nursery / rooming-in — handoff requires mother status + infant status awareness |
| Special populations | Standard | Preeclampsia / HELLP recovery, VBAC failure, placenta accreta / previa, obstetric hemorrhage cases require specific attention |

## Hemorrhage surveillance (the central OB PACU skill)

**Postpartum hemorrhage (PPH)** is defined by facility protocol (commonly volume + symptom thresholds, per current ACOG / SMFM guidance). PACU nurses assess:

- **Fundus:** firm + midline + at expected height (per provider guidance; typically ~umbilicus post-delivery, involuting over hours). A **boggy fundus** is the classic early sign of uterine atony — massage per facility protocol + notify OB anesthesia / surgeon by role.
- **Lochia:** color, volume, clot size. Saturation of pad / soaking-through is a quantitative cue — per facility protocol for volume estimation (pad count, pad weight if used).
- **Vitals trend:** peripartum patients tolerate significant volume loss before BP / HR shift. Rising HR at the edge of normal is the early cue; by the time BP drops, loss is significant.
- **Symptoms:** dizziness, thirst, shoulder-tip pain (intraperitoneal blood), apprehension.

**Red-flag pattern:** boggy fundus + increasing lochia + HR rising at edge of normal + patient says "something feels off" — escalate immediately to OB / obstetric anesthesia / rapid-transfusion per facility PPH protocol.

## Neuraxial recovery

- **Spinal (for cesarean):** typically T4 block; expect motor and sensory recovery across ~1–3 hours depending on agent. Monitor level recession, motor return (Bromage scale or facility equivalent), and readiness for ambulation per order.
- **Epidural (post-labor or post-cesarean):** catheter may be in place for post-op analgesia — monitor insertion site, dose/infusion per order, neurologic status. Catheter removal timing is coordinated with anticoagulation per facility neuraxial policy (removal with respect to LMWH / heparin dosing is a facility-specific protocol — never guess; confirm with OB anesthesia).
- **Combined spinal-epidural (CSE):** both patterns in sequence.

**Red-flag neuraxial patterns:**
- New onset motor weakness after expected recovery window → urgent OB anesthesia eval (epidural hematoma / abscess is rare but time-critical).
- Severe positional headache worsening with upright position → suspect post-dural-puncture headache (PDPH); OB anesthesia evaluates.
- Back pain + fever + neurologic change → suspect epidural infection; urgent eval.

## Post-dural-puncture headache (PDPH)
- **Classic pattern:** positional headache (worse upright, better supine), often occipital / frontal; may radiate to neck; onset typically 24–72 hours post-procedure but can appear earlier.
- **PACU role:** recognize, position patient supine for comfort, hydrate per order, escalate to OB anesthesia — the decision on conservative management vs. epidural blood patch is OB anesthesia.
- **Differentiate from:** preeclampsia / eclampsia headache (hypertension + other symptoms), caffeine withdrawal, tension headache, intracranial pathology.

## Breastfeeding-compatible analgesia framing (per order — do not invent)
- **General principle:** acetaminophen and ibuprofen (NSAIDs) are typically considered compatible with breastfeeding; short-acting opioids have limited transfer but sedation of mother / infant requires monitoring; certain agents are avoided per current lactation guidance.
- **Specific agent decisions are per provider order** — PACU nurses do not make independent analgesia selection. Confirm with OB anesthesia or the prescribing provider.
- **Non-pharmacologic:** ice packs, position changes, ambulation per order, and skin-to-skin / breastfeeding itself can reduce pain and anxiety.
- **Counsel per facility lactation resources** — if patient has a lactation-related question, route to facility lactation consultant rather than guessing.

## Emotional and psychosocial awareness
- **Expect a wide emotional range.** Tearfulness is common and often benign. Persistent or severe depressive symptoms, thought of self-harm, or thoughts about infant well-being are **escalations** — notify OB, social work, or facility mental-health resource per protocol.
- **Birth outcome matters.** NICU admission, stillbirth, emergent cesarean, separation from infant — tailor communication.
- **Screen per facility policy** for postpartum depression / anxiety (often initiated on mother-baby unit, not PACU — but PACU-visible distress triggers notification).

## Handoff to mother-baby unit (or floor)
- Mother status (VS trend, fundal status, lochia, pain, mobility, voiding, oral intake).
- Infant status (where, who is with infant, feeding plan, any clinical notes from nursery).
- Procedures and anesthesia summary (cesarean type, neuraxial details, reversal as applicable, catheter status).
- Medications given in PACU + next doses due (per order).
- Any escalation concerns flagged during recovery.
- Family coordination (partner's location, infant coordination, interpreter needs).

Use `pacu_handoff_script.md` SBAR structure with mother-baby context layered in.

## Common general-PACU habits that miss in obstetric PACU
- **Treating BP trend as the primary hemodynamic cue.** Fundus and lochia are earlier in PPH than BP. HR at edge of normal is the BP-independent early cue.
- **Delaying fundal check because "the patient just got here."** Fundal + lochia assessment belongs in the admission assessment, not 30 minutes later.
- **Treating post-op headache as "probably just tension."** Post-cesarean or post-epidural headache is PDPH until proven otherwise by OB anesthesia — and preeclampsia headache is a separate escalation.
- **Forgetting breastfeeding compatibility when prepping pain meds.** Always confirm order + breastfeeding status before administration.
- **Handing off without infant-status awareness.** Mother-baby handoff is two-patient handoff in effect — know where the infant is and who is with them.
- **Minimizing emotional presentation.** "She's just tired" may mask PPD risk — escalate per facility protocol if persistent or concerning.

## When to call (escalation by role)
- **OB / obstetric anesthesia** for any neuraxial concern, atypical headache, or neurologic change.
- **OB / surgeon on call** for boggy fundus not responding to massage per protocol, increasing lochia, suspected PPH.
- **Rapid-transfusion / massive-transfusion protocol** per facility OB hemorrhage pathway.
- **Charge nurse + mother-baby unit** for infant coordination concerns.
- **Social work / mental-health resource** per facility for significant emotional distress.

## Sources / reference
- *Drain's PeriAnesthesia Nursing*, OB chapters.
- ASPAN *Standards of Perianesthesia Nursing Practice* — obstetric population.
- ACOG / SMFM — postpartum hemorrhage guidance (framework awareness; facility protocol governs).
- AWHONN — postpartum nursing standards.
- Facility OB / obstetric anesthesia protocols: {{per facility protocol}}.
- Facility lactation resources: {{per facility}}.
```

## Must / Must not

**Must:**
- Treat hemorrhage surveillance as the central OB PACU skill — fundus + lochia + vitals + symptoms integrated.
- Name PDPH recognition and differentiate from preeclampsia / tension headache.
- Defer all doses (uterotonics, analgesia, reversal) to provider order.
- Frame breastfeeding compatibility as "per order + facility lactation resources" rather than inventing specific agents.
- Include emotional / psychosocial awareness with escalation pathway.
- Handle handoff as two-patient (mother + infant) in effect.
- Cross-reference `pacu_handoff_script.md`.

**Must not:**
- State specific uterotonic doses, infusion rates, or maximum thresholds — all per order + facility protocol.
- Invent PPH activation thresholds or massive-transfusion cutoffs — facility-specific.
- Invent specific breastfeeding-compatible or incompatible agents by name without citing a current lactation reference — compatibility lists update.
- Invent facility protocols, pager numbers, or OB-specific activation codes.
- Reference the patient's age, marital status, parity, or pregnancy history as performance signals in orientee evaluation — these are clinical variables, not rater inputs.
- Speculate on patient's emotional state in a way that labels them ("she's being dramatic") — describe behavior, escalate per protocol.
- Include patient-identifying information (MRN, full name, full DOB, room).
- Substitute for facility OB orientation or AWHONN-aligned postpartum training.
- Assume PACU nurses perform procedures outside scope (e.g., intrauterine balloon placement is OB provider scope).

## Quality signals

- A PACU nurse reading this knows fundus + lochia + HR-at-edge is an earlier cue than BP drop for PPH.
- PDPH is distinguished from preeclampsia and tension headache.
- Breastfeeding compatibility is framed as per-order + facility lactation resource.
- Emotional spectrum is acknowledged without minimization.
- Handoff is two-patient (mother + infant status).

## Verification

Before returning, verify:

- [ ] General-vs-OB contrast table covers hemorrhage, hemodynamics, neuraxial, pain, emotional, handoff.
- [ ] Fundal + lochia + vitals + symptoms hemorrhage framework present.
- [ ] PDPH recognition included with differentials.
- [ ] Neuraxial recovery section addresses spinal, epidural, and catheter removal + anticoagulation timing deferral.
- [ ] Breastfeeding-compatibility framing uses "per order + facility lactation resource" — no invented agent list.
- [ ] Emotional / psychosocial awareness with escalation.
- [ ] Handoff includes mother + infant status.
- [ ] Common general-PACU habits that fail named.
- [ ] Escalation by role throughout.

## False-Positive Prevention

Do **not** fabricate:

- **No invented uterotonic doses, infusion rates, concentrations, or max thresholds.** All per order.
- **No invented PPH volume thresholds or massive-transfusion activation triggers.** Per facility protocol + current ACOG / SMFM framework.
- **No invented breastfeeding-compatibility lists of specific agents.** Compatibility updates; reference current facility lactation resource.
- **No invented PDPH incidence rates or blood-patch criteria.** Reference OB anesthesia.
- **No invented neuraxial-anticoagulation timing specifics** (LMWH / heparin / DOAC intervals for catheter removal) — facility neuraxial anticoagulation policy governs.
- **No invented facility OB protocols, pager codes, or rapid-transfusion activation specifics.**
- **No invented ASPAN / Drain's citations.**
- **No patient-identifying information.**
- **No protected-characteristic references** (including marital status, parity, pregnancy-history) used as performance signals in orientee evaluation.

## Worked Example

<details>
<summary>Example: "Common general-PACU habits that miss in obstetric PACU" list (click to expand)</summary>

```markdown
## Common general-PACU habits that miss in obstetric PACU

1. **Waiting for BP to drop before escalating.** In a 28-year-old post-cesarean, healthy baseline peripartum circulation masks volume loss. The earlier cue is: boggy fundus + saturating lochia + HR rising at the edge of normal + subjective "something feels off." Escalate when the pattern emerges, not when the BP catches up.

2. **Doing the fundal check "when you get a minute."** Fundal + lochia is admission assessment, not a later-in-shift task. Check on admission, at 15-min intervals per facility, and with any vital-sign shift.

3. **Treating a post-op headache as "probably just tension."** Post-spinal or post-epidural headache, especially positional (worse upright, better supine), is PDPH until OB anesthesia says otherwise — and hypertensive headache in this population is preeclampsia escalation.

4. **Prepping pain medication without confirming breastfeeding status.** Confirm order + breastfeeding intent / status before administration; route lactation-specific questions to the facility lactation consultant.

5. **Handing off mother without knowing where baby is.** Mother-baby handoff is effectively a two-patient handoff. Partner location, infant location + clinical status, feeding plan — all in the SBAR.

6. **Minimizing emotional presentation as "just tired."** Persistent tearfulness, flat affect, or concerning statements about the infant warrant escalation to OB / social work / mental-health resource per facility protocol.
```

Notes: each item contrasts general-PACU habit with OB correction; escalation by role; no invented doses or protocols; bias-free framing (no "dramatic," no marital-status or parity inferences).
</details>

## Self-check

- [ ] Contrast table with general PACU present.
- [ ] Fundus + lochia + vitals + symptoms framework covered.
- [ ] PDPH + preeclampsia differentiation included.
- [ ] Neuraxial recovery + anticoagulation deferral noted.
- [ ] Breastfeeding compatibility framed as per-order + lactation resource.
- [ ] Emotional / psychosocial awareness with escalation.
- [ ] Two-patient (mother + infant) handoff framing.
- [ ] Common general-PACU habit failures named.
- [ ] Escalation by role.
- [ ] No invented doses, protocols, activation thresholds, or compatibility lists.
- [ ] No patient-identifying information.
- [ ] No protected-characteristic references as performance signals.
- [ ] Safety reminder at top.
- [ ] Verification section passed.
- [ ] False-Positive Prevention section passed.
