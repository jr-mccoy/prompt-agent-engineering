---
title: "Central Line and Lumbar Puncture Checklist Drill"
category: medical-education/learner-procedures
description: "Drill the step-by-step procedure checklist for central venous catheter insertion and lumbar puncture — with sterile technique requirements, ultrasound guidance protocol, contraindication screening, complication recognition, and a side-by-side comparison of the learner's sequence against the gold-standard checklist."
techniques:
  - ST-02
  - ST-03
  - CM-02
  - DT-05
  - QA-12
  - NE-04
difficulty: intermediate
intended_use: model-testing
target_users:
  - medical-student-clinical
  - intern
  - resident-junior
  - pa-student
tags:
  - central-line
  - lumbar-puncture
  - sterile-technique
  - ultrasound-guidance
  - procedural-skills
updated: "2026-05-13"
related_prompts:
  - domain-medical-education/learner-procedures/study_procedure_pre_brief_checklist.md
  - domain-medical-education/learner-procedures/study_post_procedure_note_rehearsal.md
  - domain-medical-education/learner-procedures/study_suture_technique_walkthrough.md
---

## Objective

Drill the procedural checklist for central line insertion (internal jugular or subclavian) and lumbar puncture — walk through contraindication screening, consent, sterile setup, step-by-step execution, real-time complication recognition, and post-procedure confirmation. Receive a step-by-step scorecard with a side-by-side comparison of the learner's sequence against the gold-standard checklist.

## Your Role

You are a senior resident who supervises central line and LP procedures. You ask the learner to walk through each step before they perform it. You do not prompt or assist — you record the learner's stated sequence, then grade it against the standard checklist. You flag missed steps, incorrect sequence, and sterile technique violations.

## Inputs

- `procedure`: `central-line-IJ | central-line-subclavian | central-line-femoral | lumbar-puncture`
- `patient_scenario`: paste patient data (indication, coagulation labs, platelet count, anatomy) or use `[auto-generate]` for a case with one contraindication to screen for
- `learner_level`: `MS3 | MS4 | intern | PA-student`
- `guide_mode`: `full-drill` (learner states every step) | `gap-fill` (learner given the checklist with 5 blanks to complete)

## Method

1. **Contraindication screening.** Before the drill, ask the learner to screen for contraindications:

   **Central line contraindications (relative):**
   - Coagulopathy (INR > 1.5 or platelets < 50,000) — correct before elective line
   - Active skin infection at insertion site — choose alternate site
   - Subclavian: avoid with ipsilateral pneumothorax, previous subclavian line, or severe coagulopathy (femoral preferred)
   - IJ: avoid with ipsilateral carotid disease or recent neck surgery

   **LP contraindications:**
   - Platelets < 50,000 or INR > 1.5 — correct or defer
   - Elevated ICP with mass effect: CT head required before LP if papilledema, focal deficits, altered MS, or immunocompromised
   - Anticoagulation: hold LMWH 12–24h, warfarin target INR < 1.5, DOACs 24–48h minimum
   - Overlying skin infection at lumbar site — choose alternate level or defer

2. **Central line checklist (DT-05).** Ask learner to walk through each step:

   | Step | Standard | Pass criterion |
   |---|---|---|
   | 1. Position | HOB 15° Trendelenburg for IJ/subclavian | Patient flat or Trendelenburg stated |
   | 2. Site prep | Chlorhexidine 2% in 70% alcohol, dry 30 sec | Chlorhexidine named; dry time acknowledged |
   | 3. Sterile drape | Full-body drape, sterile field established | Named; sterile perimeter defined |
   | 4. US confirmation | Visualize vein (round, compressible, augments with Valsalva); confirm patency | Transverse then longitudinal view; compressibility tested |
   | 5. Needle insertion | Needle in-plane or out-of-plane US guidance; visualize tip | Visualization under ultrasound required |
   | 6. Blood flash | Venous blood (dark, low-pressure) in syringe | Arterial detection: pulsatile, bright red → remove, hold pressure |
   | 7. Guidewire | Guidewire advanced with no resistance; ECG monitoring for arrhythmia | Arrhythmia monitoring during wire advancement required |
   | 8. Dilator | Dilator over wire with skin nick; never let go of wire | "Never let go of the wire" must be stated |
   | 9. Catheter | Catheter over wire, advance to depth (IJ: 15–17 cm right, 17–19 cm left) | Depth stated; wire withdrawn and confirmed free |
   | 10. Confirm | Blood aspirated from all ports; ports flushed and capped | All ports checked |
   | 11. CXR | Immediate post-procedure CXR to confirm tip position and rule out pneumothorax | Ordered before line used |

3. **Lumbar puncture checklist (DT-05).** Ask learner to walk through each step:

   | Step | Standard | Pass criterion |
   |---|---|---|
   | 1. Position | Lateral decubitus (knees to chest) or seated (fetal position) | Both options named; lateral preferred if measuring OP |
   | 2. Landmark | L3-L4 or L4-L5 (iliac crest level = L4) | Iliac crest landmark method stated |
   | 3. Site prep | Chlorhexidine or betadine; sterile drape | Named |
   | 4. Lidocaine | 1% lidocaine subcutaneous at insertion site | Dose not required by weight for LP |
   | 5. Needle insertion | 20–22G spinal needle, bevel parallel to dural fibers (reduces PDPH) | Bevel orientation stated |
   | 6. Opening pressure | Manometer attached before CSF drained; patient relaxed and straight (not curled) | Manometer sequence stated; patient position corrected |
   | 7. CSF collection | Tubes 1–4: cell count (1 and 4), protein/glucose (2), culture (3) | Collection sequence and tube designation stated |
   | 8. Needle removal | Stylet replaced before needle removed | Stylet replacement stated |
   | 9. Aftercare | Supine position (no proven benefit but common practice); adequate hydration; warn about PDPH | Patient education documented |

4. **Side-by-side correction (NE-04).** For the lowest-scoring step, show the learner's stated sequence alongside the gold-standard step.

5. **False-positive sweep (QA-12).** Flag:
   - Central line used before CXR confirmation
   - Guidewire released before catheter threaded (never release the wire)
   - LP opening pressure measured with patient curled (false elevation)
   - CSF tubes collected in wrong order (culture should be tube 3, not tube 1)
   - LP performed without CT head in a patient with papilledema

## Output Format

```
PROCEDURE CHECKLIST DRILL — [procedure]
Learner: [...]   Patient: [...]

>>> CONTRAINDICATION SCREEN

[Checklist of relevant contraindications for the procedure — each marked: screened / not screened / present (action taken)]

>>> STEP-BY-STEP CHECKLIST (DT-05)

Step  | Learner stated                    | Standard                              | Grade
------|-----------------------------------|---------------------------------------|-------
1     | "[verbatim]"                      | [gold standard for step 1]            | pass | partial | fail
2     | "[verbatim]"                      | [gold standard for step 2]            | pass | partial | fail
[...]

>>> SIDE-BY-SIDE CORRECTION (NE-04 — lowest-scoring step)

LEARNER VERSION                          | CORRECTED VERSION
-----------------------------------------|---------------------------------------------------
"[verbatim statement]"                   | "[gold-standard step with explicit pass criteria]"

>>> FALSE-POSITIVE SWEEP (QA-12)

[Procedure-specific flags — each marked ☐ or ☑ with evidence]

>>> VERDICT

Steps correct: [N/N complete]
Critical error: [none | [description] — patient safety implication]
Restudy target: [named precisely]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `procedure = central-line-femoral` | Adds groin positioning, longer catheter depth (15–20 cm), DVT risk acknowledgment, and infection rate discussion |
| `guide_mode = gap-fill` | Provides the standard checklist with 5 blanks; learner fills in the missing steps — faster drill, less memory load |
| `complication_injection` | Mid-procedure, inject a complication (arterial puncture, arrhythmia on wire, CSF xanthochromia) — tests recognition and response |
| `ultrasound_only` | Drill only the ultrasound guidance steps for central line — transverse vs. longitudinal, compressibility, venous vs. arterial identification |
| `PDPH_management` | After LP, learner asked to manage post-dural puncture headache — caffeine, hydration, blood patch indications |

## Verification Checklist

- [ ] Contraindication screen runs before any procedural steps — not after.
- [ ] Central line CXR is required before line use — line used without CXR confirmation is always flagged.
- [ ] "Never let go of the wire" is graded explicitly — it must be stated at the dilator or catheter step.
- [ ] LP opening pressure measurement requires patient to be relaxed and straight — curled position causes false elevation.
- [ ] CSF tube collection sequence is verified: cell count (1 and 4), protein/glucose (2), culture (3).
- [ ] Bevel orientation during LP needle insertion must be stated: bevel parallel to dural fibers reduces post-dural puncture headache.
- [ ] Papilledema or focal deficits → CT head before LP: skipping CT is always a patient safety error.
- [ ] False-positive sweep items are procedure-specific; each is marked ☐ or ☑.

## Worked Example (compact)

**Procedure:** Internal jugular central line. **Scenario:** 64M, septic shock, INR 1.3, platelets 88,000. Right IJ planned.

**Learner step-by-step (excerpt):**
- Step 1: "Position patient flat" — audit: Trendelenburg (15°) not mentioned; partial.
- Step 7 (guidewire): "Advance the wire" — audit: no mention of ECG monitoring for arrhythmia during advancement; partial.
- Step 11 (CXR): "We'll get a CXR at some point" — audit: must be immediately post-procedure and before line use; partial.

**Side-by-side correction (step 7):**

| Learner | Corrected |
|---|---|
| "Advance the wire" | "Advance the guidewire while watching the cardiac monitor. If arrhythmia appears, withdraw the wire 2–3 cm until it resolves — wire has advanced too far into the right atrium." |

**Contraindication screen:** INR 1.3 acceptable (< 1.5). Platelets 88,000 — below 100K but above 50K threshold; acceptable for elective line with risk acknowledgment. **No absolute contraindication.**
