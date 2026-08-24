---
title: "Periprocedural Anticoagulation Bridging"
category: domain-healthcare-clinical/pharmacology
description: "Plan periprocedural management of warfarin or DOAC by stratifying thromboembolic risk vs procedural bleeding risk, deciding whether to bridge, timing hold and resume of anticoagulation, and selecting bridging agent and dose when indicated per CHEST 2022, BRIDGE, PAUSE, and ESC guidance."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
  - QA-01
difficulty: advanced
tags:
  - hematology
  - cardiology
  - perioperative
  - anticoagulation
  - bridging
updated: "2026-05-12"
---

## Objective

Plan the safe interruption and resumption of warfarin or a DOAC around a planned procedure: stratify the patient's thromboembolic risk (mechanical valve, AFib by CHA₂DS₂-VASc, VTE recency), assess procedural bleeding risk, decide whether bridging therapy is required, time the hold of the anticoagulant relative to the procedure, time the resumption based on hemostasis, and choose bridging agent and dose when indicated. Output a day-by-day plan.

## Inputs

- Indication for anticoagulation (AFib — including CHA₂DS₂-VASc score and prior stroke/TIA, mechanical valve — position and type, recent VTE — date and provoking factor, thrombophilia, LVAD, embolic stroke of undetermined source)
- Current anticoagulant (warfarin with INR trend; DOAC name + dose + frequency)
- Renal function (CrCl, especially for DOACs)
- Planned procedure: nature, bleeding risk classification, urgency, regional anesthesia, neuraxial considerations
- Other antithrombotics: aspirin, P2Y12 inhibitors (clopidogrel, ticagrelor, prasugrel), recent PCI / DES timing
- Prior bleeding or thrombotic events; prior periprocedural management
- Procedural context (in-office vs hospital, day surgery vs admission)

## Role

Senior internist / hospitalist / hematology consultant writing the periprocedural anticoagulation plan with daily steps and contingency rules.

## Reasoning Steps

1. **Classify thromboembolic risk.**
   - **High risk (annual TE risk >10%):**
     - Mechanical mitral valve, any position.
     - Mechanical aortic valve with additional risk factors (older caged-ball/tilting disc; AFib; prior stroke/TIA; LV dysfunction; ≥2 of: AFib, prior TE, hypercoagulable, EF <30, mechanical aortic valve in mitral position).
     - AFib with CHA₂DS₂-VASc ≥7, OR recent (<3 mo) stroke/TIA, OR mitral stenosis.
     - VTE within prior 3 months; active malignancy with recent VTE.
     - Antiphospholipid syndrome (triple-positive).
   - **Moderate risk (5–10% annual):**
     - Mechanical aortic valve (bileaflet, no other risk factor).
     - AFib with CHA₂DS₂-VASc 5–6 or prior stroke/TIA >3 months ago.
     - VTE 3–12 months ago, non-severe thrombophilia, recurrent VTE.
   - **Low risk (<5% annual):**
     - AFib with CHA₂DS₂-VASc ≤4 without prior stroke.
     - Single VTE >12 months ago, no other risk factors.

2. **Classify procedural bleeding risk.**
   - **Minor (proceed without interruption — DOAC sometimes held one dose):**
     - Dental cleaning, simple extractions (with local hemostatic measures).
     - Cataract surgery.
     - Minor dermatologic excisions.
     - Endoscopy without biopsy / polypectomy.
     - Joint or soft-tissue injections.
   - **Low bleeding risk:**
     - Coronary angiogram (without intervention), pacemaker/ICD placement (BRUISE-CONTROL: continue warfarin actually safer than bridging in many cases).
     - Endoscopy with biopsy.
     - Selected biopsies.
   - **High bleeding risk:**
     - Major orthopedic surgery (hip, knee replacement).
     - Cardiac, intracranial, intraspinal surgery.
     - Major abdominal/thoracic surgery.
     - Endoscopic polypectomy of large polyps, ERCP with sphincterotomy, EUS-FNA.
     - Neuraxial (spinal/epidural) anesthesia.
     - Renal/liver biopsy.

3. **Decide whether to interrupt anticoagulation at all.**
   - Many minor procedures can proceed without interruption.
   - Dental work: continue warfarin (INR <3) with local hemostatic measures (tranexamic acid mouthwash, oxidized cellulose, sutures). Continue DOACs in most cases.
   - Cataract / dermatologic: continue.
   - Pacemaker / ICD: BRUISE-CONTROL trial — continue warfarin (with INR ≤3) had lower hematoma rate than bridging with LMWH; for DOACs, holding 1–2 doses is reasonable; routine bridging not needed.
   - Endoscopy without biopsy: continue.

4. **For warfarin interruption: hold + bridge decision.**
   - **Hold warfarin 5 days before procedure** (4 days if INR target is 2.0–3.0 and the patient runs closer to 2.0; 5 days if target 2.5–3.5 or higher baseline INR; 6 days in elderly with slow clearance).
   - Check INR day of procedure: target ≤1.5 for most surgeries (often ≤1.2 for neuraxial).
   - **Bridging decision (BRIDGE trial, 2015):**
     - **High thromboembolic risk:** **bridge** with LMWH (enoxaparin 1 mg/kg SC q12h or 1.5 mg/kg q24h; some use UFH IV for mechanical mitral valves).
     - **Moderate risk:** individualize; often **do not bridge** unless additional risk factors. BRIDGE showed no benefit and ↑ bleeding from bridging in AFib without high TE risk.
     - **Low risk:** **do not bridge.**
   - **LMWH timing in bridging:**
     - Start enoxaparin 1 mg/kg q12h (or 1.5 mg/kg q24h) on day −3 (i.e., 3 days before procedure, when INR is sub-therapeutic).
     - **Last LMWH dose 24 hours before procedure** (last q12h dose 24h pre-op; last q24h dose 24h pre-op). For prophylactic doses, 12 hours suffices but for therapeutic doses, 24 hours.
     - Resume LMWH 24 hours post-procedure for low-bleeding-risk procedure, 48–72 hours for high-bleeding-risk (e.g., neurosurgery, major orthopedic). Restart warfarin same evening as procedure if hemostasis adequate; bridge with LMWH until INR therapeutic for 2 consecutive measurements.
   - **UFH IV bridging** for mechanical mitral valve or when ability to reverse rapidly is needed: 18 units/kg/h infusion; check aPTT 6h after start, target 1.5–2.5× control; stop infusion 4–6 h before procedure; aPTT normalizes quickly.

5. **For DOAC interruption: timing based on PK (PAUSE study).**
   - PAUSE simplified DOAC periprocedural management for AFib — no bridging needed for most.
   - **Apixaban / Edoxaban / Rivaroxaban** (factor Xa inhibitors):
     - **Low bleeding risk:** hold for 1 day (last dose 2 days before procedure for q12h apixaban; 1 day prior for q24h rivaroxaban/edoxaban). Many protocols simplify: omit DOAC the day before and the day of procedure.
     - **High bleeding risk:** hold for 2 days (skip 2 doses for q12h, last dose 3 days before procedure for q24h).
     - Resume **24 hours after low-bleeding-risk procedure**; **48–72 hours after high-bleeding-risk procedure**.
   - **Dabrigatran** (direct thrombin inhibitor; renal elimination 80%):
     - **CrCl ≥80:** hold 1 day for low-bleeding-risk; 2 days for high.
     - **CrCl 50–79:** hold 1–2 days low; 2–3 days high.
     - **CrCl 30–49:** hold 2 days low; 4 days high.
     - **CrCl <30:** off-label; longer holds; consider switching to alternative.
   - Resume DOAC 24h post-procedure for low bleeding risk; 48–72h for high.
   - **No bridging is needed for DOAC interruption in AFib** for most cases (PAUSE). DOAC short half-life provides its own "natural bridge."

6. **Special situations.**
   - **Mechanical mitral valve undergoing major non-cardiac surgery:** highest-risk scenario; bridge with UFH or LMWH at therapeutic dose. Pre-procedure hold 5 days warfarin, switch to UFH or LMWH on day −3, stop UFH 4–6h before (or LMWH 24h before), restart UFH/LMWH 24h post-op (or longer for high bleeding risk), restart warfarin same evening, continue heparin until INR therapeutic ×2 measurements.
   - **VTE within 3 months on warfarin:** consider IVC filter as alternative to bridging for some patients with high bleeding risk. Generally bridge.
   - **Antiphospholipid syndrome (triple-positive):** bridge with therapeutic-dose LMWH; high recurrent thrombosis risk.
   - **Recent PCI with DES:** dual antiplatelet therapy considerations override anticoagulant bridging in most cases — consult interventional cardiology; minimize elective surgery within 6–12 months of DES.
   - **Neuraxial anesthesia (epidural, spinal):** specific timing per ASRA guidelines.
     - Warfarin: INR ≤1.4 for placement; remove catheter after INR ≤1.5.
     - UFH IV: stop 4–6h before, normal aPTT.
     - LMWH therapeutic dose: hold 24h before placement / catheter removal.
     - LMWH prophylactic dose: hold 12h before.
     - DOACs: hold 3 days for therapeutic dose, 24h for prophylactic dabigatran.
   - **Emergency / urgent surgery:** reversal agents.
     - Warfarin: 4-factor PCC (Kcentra) 25–50 units/kg + IV vitamin K 5–10 mg.
     - Dabigatran: idarucizumab 5 g IV.
     - Apixaban / rivaroxaban: andexanet alfa (high dose for higher recent dose or longer interval); 4-factor PCC 50 units/kg as alternative.
   - **Atrial fibrillation patient on anticoagulant: consider AF rate / rhythm management** if hemodynamic concern around procedure.

7. **Anti-platelet management overlap.**
   - Aspirin 81 mg: usually continue for cardiovascular indication; hold for high-bleeding-risk surgery (CABG, neurosurgery, spinal).
   - P2Y12 inhibitors: clopidogrel hold 5–7 days, ticagrelor 3–5 days, prasugrel 7 days; coordinate with interventional cardiology if recent DES.
   - Coordinate with surgical and cardiology teams.

8. **Verify and write the plan.**
   - State the day-by-day schedule starting D-7 through D+7.
   - State the criteria for each step (e.g., "last enoxaparin dose at 0800 day before procedure").
   - State contingencies (urgent surgery → reversal; INR not at target → delay).

## Output Format

```
PATIENT SNAPSHOT:
- Indication: [AFib + CHA₂DS₂-VASc / mechanical valve type + position / recent VTE date / other]
- Current AC: [warfarin INR target X-Y, current INR; OR DOAC name + dose + freq]
- Renal function: [CrCl]
- Procedure: [name, date, bleeding-risk class]
- Other antithrombotics: [aspirin, P2Y12]

THROMBOEMBOLIC RISK STRATIFICATION:
- Risk class: [high / moderate / low]
- Rationale: [specific factors]

PROCEDURAL BLEEDING RISK:
- Class: [minimal / low / high]
- Rationale: [specific factors; neuraxial?]

BRIDGING DECISION:
- Bridge: [yes / no]
- Rationale: [tie to TE risk + bleeding risk + evidence; cite BRIDGE / PAUSE / CHEST 2022]

DAY-BY-DAY PLAN:

For warfarin interruption with bridging:
- D−7 to D−6: continue warfarin as usual; baseline INR check
- D−5: stop warfarin (last dose D−6 evening); inform patient
- D−4: no anticoagulation; INR will drift down
- D−3: start LMWH enoxaparin [dose] SC q[interval] starting AM
- D−2: continue LMWH BID
- D−1: morning LMWH dose; last LMWH dose at 0800 D−1 if q12h; if q24h enoxaparin, last dose D−2 morning; check INR D−1
- Day of procedure: INR target ≤1.5 (≤1.2 for neuraxial); hold all LMWH; proceed
- D0 evening or D+1: resume warfarin at maintenance dose
- D+1 (24h post-op for low-bleeding-risk procedure) OR D+2–3 for high-bleeding-risk: resume LMWH bridge
- Continue LMWH until INR therapeutic on 2 consecutive measurements; then stop LMWH

For DOAC interruption (PAUSE protocol):
- D−2 (high bleeding risk) or D−1 (low bleeding risk): last DOAC dose
- D−1 (low bleed) or D−1/0 (high bleed): no DOAC
- Day of procedure: no DOAC
- D+1 (24h post low-bleed) or D+2–3 (high-bleed): resume DOAC at usual dose
- No bridging required for most AFib

URGENT/EMERGENT REVERSAL CONTINGENCY:
- Warfarin: 4F-PCC 25–50 u/kg + vitamin K 5–10 mg IV
- Dabigatran: idarucizumab 5 g IV
- Apixaban / rivaroxaban: andexanet alfa per dosing nomogram; 4F-PCC 50 u/kg if andexanet unavailable
- Tranexamic acid 1 g IV / topical for mucosal bleeding

OTHER ANTITHROMBOTICS:
- Aspirin: [continue / hold]
- P2Y12: [continue / hold X days before]

MONITORING:
- INR (warfarin): D−1, D+3, D+5
- Bleeding watch: surgical site, GI, GU, intracranial signs
- Resumption of regular monitoring (INR weekly until stable; or DOAC compliance)

WHEN TO ESCALATE:
- Major post-op bleeding → hold AC, reversal, surgical re-exploration
- Thrombosis during interruption: emergent imaging + therapeutic AC

FOLLOW-UP:
- Post-op check-in at 1 week
- Resume baseline AC clinic visits
- Document plan and outcomes for future reference
```

## Worked Example

**Input:** 72-year-old man with AFib (CHA₂DS₂-VASc 5: HTN, DM, age, prior TIA 4 years ago, vascular disease) on apixaban 5 mg BID, CrCl 64. Scheduled for laparoscopic cholecystectomy (low-to-moderate bleeding risk) in 5 days. No recent bleeding. ASA 81 mg daily for CAD.

**Output:**

```
PATIENT SNAPSHOT:
- 72y M, AFib + CHA₂DS₂-VASc 5 (prior TIA 4 y ago, not within 3 months); apixaban 5 mg BID; CrCl 64.
- Lap chole — typically classified as low–moderate bleeding risk (single-port low; multi-port slightly higher); we will treat as low-to-moderate per PAUSE high-bleeding-risk threshold.
- ASA 81 mg for CAD.

THROMBOEMBOLIC RISK STRATIFICATION:
- AFib with CHA₂DS₂-VASc 5, but TIA was 4 years ago (not within 3 months) — **moderate** TE risk per BRIDGE/CHEST framework. Not high risk.

PROCEDURAL BLEEDING RISK:
- Laparoscopic cholecystectomy: low–moderate bleeding risk per PAUSE (high-bleed if intra-abdominal hemorrhage anticipated; standard lap chole reasonably treated as low–moderate, individual surgeon may classify higher). For this plan, treat as **moderate-to-high** to be safe given peritoneal cavity work.

BRIDGING DECISION:
- **No bridging required for DOAC interruption in AFib** per PAUSE (2021) — DOACs have short half-lives that provide adequate natural bridging.
- Apixaban half-life ~12 h; with normal renal function, 48-h hold provides >90% clearance.

DAY-BY-DAY PLAN (PAUSE protocol, high-bleeding-risk threshold for added margin):

- D−2 (Wednesday): take morning apixaban 5 mg; **skip evening dose.**
- D−1 (Thursday): **no apixaban any time of day.**
- Day of surgery (Friday): no apixaban; proceed with surgery.
- D+1 (Saturday, ~48 h post last dose, ~24 h post-op): if hemostasis adequate and no drainage / bleeding concerns, **resume apixaban 5 mg BID** with evening dose.
- D+2 onward: continue apixaban 5 mg BID as before.

ALTERNATIVE (if procedural team classifies as definitively low bleeding risk):
- D−1 morning: last apixaban dose; skip evening.
- Day of procedure: no apixaban.
- D+1 morning: resume apixaban.

ASPIRIN MANAGEMENT:
- ASA 81 mg for secondary prevention CAD: **continue** through the perioperative period (overall mortality and CV-event benefit of continued ASA outweighs small additive bleeding for most non-CNS, non-spinal surgery). Confirm with surgical team.
- If surgical team requires hold: 5 days off (ASA effect persists for platelet life, ~7–10 days), then resume D+1.

URGENT/EMERGENT REVERSAL CONTINGENCY:
- If massive intraoperative or post-op bleeding: andexanet alfa per nomogram (high-dose if last apixaban dose <8h prior and dose ≥5 mg; low-dose if last dose >8h or <5 mg). If andexanet unavailable: 4F-PCC 50 units/kg.
- Tranexamic acid 1 g IV for adjunct.
- Surgical re-exploration as needed.

MONITORING:
- Renal function (BUN/Cr) day before surgery (apixaban dosing CrCl-sensitive; baseline 64 acceptable).
- Bleeding signs post-op: surgical site, drain output, hemoglobin, urine, melena.
- Re-establish therapeutic anticoagulation by D+2 in most cases — apixaban steady state within 3 days.

WHEN TO ESCALATE:
- Bleeding requiring transfusion or reoperation: hold apixaban, andexanet/PCC, surgical management; reassess timing of resumption based on hemostasis.
- Thromboembolic event during interruption (very rare in this short hold): heparin + imaging.

FOLLOW-UP:
- 1-week post-op visit: confirm wound healing, AC adherence, no bleeding signs.
- Resume routine AFib follow-up.

DOCUMENTATION:
- Procedure date, last apixaban dose, planned resumption, ASA decision, and contact for issues recorded in EHR.
```
