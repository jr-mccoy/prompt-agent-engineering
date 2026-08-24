---
title: "Massive Transfusion Protocol"
category: domain-healthcare-clinical/acute-care
description: "Activate and run a massive transfusion protocol with balanced ratios, calcium replacement, hemodynamic targets, and damage-control goals."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - trauma
  - hemorrhage
  - transfusion
  - critical-care
updated: "2026-05-08"
---

## Objective

Activate massive transfusion protocol (MTP), deliver balanced products, treat trauma-induced coagulopathy, replace calcium, and target damage-control endpoints. Output is a sequenced order set with named ratios, doses, and laboratory triggers.

## Inputs

- Mechanism / source: trauma (blunt, penetrating), GI bleed, postpartum hemorrhage, ruptured AAA, surgical bleeding
- Vitals: HR, BP, MAP, mental status
- Estimated blood loss, response to initial resuscitation
- Initial labs: CBC (Hgb, platelets), INR, fibrinogen, lactate, base deficit, calcium, K
- Anticoagulant exposure: warfarin, DOAC, antiplatelet
- ROTEM/TEG availability

## Reasoning Steps

1. **Activate MTP early.**
   - Triggers: ABC score ≥2 (penetrating, SBP <90, HR >120, positive FAST), shock index >1.0 (HR/SBP), >4 units pRBC anticipated, ongoing hemorrhage with hemodynamic instability.
   - One phone call to blood bank activates pre-packed coolers (pRBC : FFP : platelets in 1:1:1 ratio per PROPPR).

2. **Damage-control resuscitation principles.**
   - **Permissive hypotension** until hemorrhage controlled: SBP target 80–90 (MAP 65) in penetrating trauma without TBI; higher targets in TBI (SBP ≥110, MAP ≥80) or blunt trauma with potential head injury.
   - **Limit crystalloid** — dilutes clotting factors, worsens coagulopathy and edema. After initial 1 L max, switch to blood products.
   - **Balanced products 1:1:1** — pRBC : FFP : platelets in equal ratio (per PROPPR trial).
   - **Treat the lethal triad:** acidosis, hypothermia, coagulopathy. Each worsens the others; correct all in parallel.

3. **Components per pack (typical):**
   - **Pack 1:** 6 units pRBC + 6 units FFP + 1 dose apheresis platelets (or 6-pack random donor).
   - **Subsequent packs:** same composition. Continue until hemorrhage controlled or transition to goal-directed (TEG/ROTEM-based) replacement once labs available.

4. **Tranexamic acid (TXA).**
   - **1 g IV over 10 min, then 1 g over 8 h** if within 3 hours of trauma onset (CRASH-2). Beyond 3 hours, TXA may worsen outcomes — check timing.
   - Postpartum hemorrhage (WOMAN trial): 1 g IV within 3 hours; repeat 1 g if bleeding continues at 30 min.
   - GI bleed: HALT-IT did not show benefit; do not give routinely.

5. **Calcium replacement (often missed; hugely important).**
   - Citrate in stored blood chelates ionized calcium → hypocalcemia → vasoplegia, coagulopathy, cardiac dysfunction.
   - Check ionized Ca after every 4 units pRBC.
   - Replace: calcium chloride 1 g IV (preferred via central line, more elemental Ca per dose) OR calcium gluconate 2–3 g IV (peripheral acceptable). Repeat to keep ionized Ca >1.1 mmol/L.

6. **Anticoagulant reversal.**
   - **Warfarin:** vitamin K 10 mg IV + 4-factor PCC (25–50 units/kg by weight and INR; per package insert).
   - **Dabigatran:** idarucizumab 5 g IV (two 2.5 g vials). If unavailable, 4F-PCC and dialysis.
   - **Rivaroxaban / apixaban / edoxaban:** andexanet alfa (low or high dose by drug, dose, time since last dose) OR 4F-PCC 50 units/kg if andexanet unavailable.
   - **Heparin:** protamine 1 mg per 100 units of heparin given in last hour (max 50 mg).
   - **LMWH:** protamine partial reversal if within ~8 hours of dose.
   - **Antiplatelet:** platelet transfusion not routinely beneficial in TBI or ICH (PATCH trial showed harm). Reserve for active bleeding with documented platelet dysfunction.

7. **Goal-directed transfusion once labs / TEG available.**
   - **TEG/ROTEM** guides specific component replacement:
     - Prolonged R time / CT (clotting time) → factor deficiency → FFP (or PCC).
     - Reduced K time / CFT or alpha angle → fibrinogen deficiency → cryoprecipitate or fibrinogen concentrate (target fibrinogen >150–200 in active bleeding, >200 in obstetric hemorrhage).
     - Reduced MA / MCF → platelet deficiency or dysfunction → platelets.
     - Lysis at 30 min (LY30) >3% → fibrinolysis → TXA.
   - Lab-based targets when TEG unavailable:
     - Fibrinogen <150 → cryoprecipitate 10 units (or fibrinogen concentrate).
     - Platelets <50 → 1 dose apheresis platelets.
     - INR >1.8 → FFP 10–15 mL/kg.

8. **Source control is the actual treatment.**
   - Trauma: surgery / IR (REBOA in selected aortic emergencies, angioembolization for splenic/pelvic).
   - GI bleed: endoscopy, IR embolization, surgery.
   - Postpartum: uterotonics (oxytocin, methergine, hemabate, misoprostol), Bakri balloon, embolization, hysterectomy.
   - Ruptured AAA: vascular surgery / endovascular.

9. **Hypothermia prevention.**
   - Warm fluids and blood products through fluid warmer.
   - Patient warming: forced air, warm blankets.
   - Hypothermia <34°C → coagulopathy worsens dramatically, citrate metabolism impaired.

10. **Endpoints to deactivate MTP.**
    - Hemorrhage controlled (surgical or angio).
    - Hemodynamic stability without ongoing transfusion.
    - Lactate trending down, base deficit improving.
    - Switch to goal-directed replacement based on labs/TEG.

## Output Format

```
ACTIVATION TRIGGER: [criteria met]
SOURCE: [bleeding location, control plan]

INITIAL ORDERS:
- Activate MTP
- Two large-bore IVs (16G or 18G) and/or rapid infuser line
- Type and crossmatch (use uncrossmatched O-neg/O-pos if needed in extremis)
- Labs: CBC, INR/PTT, fibrinogen, ABG, lactate, BMP, ionized Ca, [TEG/ROTEM if available]
- Foley, NG if appropriate
- Telemetry, art line

PRODUCTS:
- 1:1:1 (pRBC : FFP : platelets) per pack
- TXA 1 g IV over 10 min + 1 g over 8 h (if within 3 h of trauma)

CALCIUM:
- Check ionized Ca after every 4 units pRBC
- Replace [agent, dose] to keep iCa >1.1 mmol/L

ANTICOAGULANT REVERSAL (if applicable):
- [drug, dose, mechanism]

HEMODYNAMIC TARGETS:
- SBP [80–90 / 110+ if TBI]
- MAP [65 / 80 if TBI]

GOAL-DIRECTED THRESHOLDS:
- Fibrinogen <150 → cryo
- Platelets <50 → platelets
- INR >1.8 → FFP
- TEG-guided if available

SOURCE CONTROL:
- [specific procedure, team]

WARMING:
- Fluid warmer, forced air

DEACTIVATION CRITERIA:
- Hemorrhage controlled, hemodynamics stable, lactate clearing
```

## Worked Example

**Input:** 34 y/o M, motorcycle vs car, GCS 14, hypotensive on arrival. Vitals: BP 78/42, HR 138, RR 28, T 35.6, GCS 14. FAST positive in RUQ and pelvis. Pelvic radiograph shows open-book pelvic fracture. Initial labs: Hgb 8.4, platelets 220, INR 1.4, fibrinogen 180, lactate 6.2, ionized Ca 1.05. Weight 80 kg. No anticoagulants.

**Output:**

```
ACTIVATION TRIGGER: ABC ≥2 (penetrating not present, but SBP <90, HR >120, positive FAST = 3 criteria). Hemodynamic instability with positive FAST and pelvic fracture = clear MTP indication.
SOURCE: Likely intraabdominal (RUQ FAST positive — liver/spleen) AND pelvic (open-book fracture, retroperitoneal). Multiple sources require parallel control plans.

INITIAL ORDERS:
- Activate MTP via blood bank — pack 1 (6 pRBC + 6 FFP + 1 platelets) en route now.
- Pelvic binder placed at the iliac crests (most common error: placed too high).
- Two 16G PIVs minimum; place IO if delay. Consider central access (IJ or subclavian) for ongoing volume and pressors if needed.
- O-negative pRBC ×2 immediately if crossmatched not yet ready (this patient is male — O-positive is acceptable to conserve O-neg supply).
- Type and crossmatch sent.
- Labs already drawn; add ABG, BMP, repeat CBC q1h initially, ionized Ca now and after every 4 units pRBC.
- TEG/ROTEM if available — at 1.4 INR with low fibrinogen, expect early need for cryo.
- Foley placed (output marker, exclude urethral injury first if blood at meatus or scrotal hematoma).
- NG after intubation if not yet performed.
- Telemetry + arterial line.

PRODUCTS:
- Pack 1 in bolus: 6 units pRBC + 6 units FFP + 1 apheresis platelets.
- TXA 1 g IV over 10 min NOW (within 3 h of injury) + 1 g infusion over 8 h.
- Anticipate pack 2 within 20–30 minutes if bleeding continues.

CALCIUM:
- Ionized Ca 1.05 already low. Calcium chloride 1 g IV via central line now (or 3 g calcium gluconate peripheral).
- Recheck after every 4 units of pRBC; expect to need 1 g calcium chloride per 4 units.

ANTICOAGULANT REVERSAL: not applicable.

HEMODYNAMIC TARGETS:
- SBP 80–90, MAP 65 — permissive hypotension since GCS 14 and no signs of severe TBI yet.
- If GCS drops or pupillary changes develop, raise SBP target ≥110 to maintain CPP and obtain head CT urgently.
- Avoid crystalloid beyond initial 1 L if any. Switch fully to blood products.

GOAL-DIRECTED THRESHOLDS:
- Fibrinogen 180 borderline; with ongoing bleeding, will fall fast. Pre-empt with cryo 10 units in pack 2.
- Platelets 220 currently fine; will fall with dilution.
- INR 1.4 will worsen; FFP at 1:1 will partly correct.
- Recheck CBC, INR, fibrinogen, ionized Ca q1h while transfusing.

SOURCE CONTROL:
- Trauma surgery activated for damage-control laparotomy (intraabdominal source, RUQ FAST positive).
- Interventional radiology activated in parallel for pelvic angioembolization (pelvic fracture with hemodynamic instability).
- Sequence depends on what surgery prefers: many centers do laparotomy first, then to IR. Some use REBOA (zone 3 for pelvic, zone 1 for abdominal) as bridge.
- Orthopedics for definitive pelvic fixation later (binder + IR for now).

WARMING:
- All fluids and blood products through Belmont or Level 1 rapid infuser with warmer.
- Forced air warming blanket; warm room.
- Hypothermia <34°C to be avoided; check temp continuously.

DEACTIVATION CRITERIA:
- Hemorrhage controlled by laparotomy + IR (or evidence of surgical control).
- Hemodynamic stability off uncrossmatched products and on patient-specific crossmatched blood.
- Lactate trending down (recheck q1–2h), base deficit improving.
- Transition to goal-directed transfusion once labs allow precise replacement.

PITFALLS TO AVOID:
- Crystalloid resuscitation beyond 1 L → coagulopathy worsening.
- Forgetting calcium → vasoplegic, coagulopathic.
- Pelvic binder over hips instead of greater trochanters → ineffective.
- Aggressive BP target → blows off clots, worsens bleeding.
- Hypothermia from cold blood and exposed patient → coagulopathy.
- Missing concurrent injuries — repeat exam after stabilization, secondary survey, CT pan-scan when stable.
```
