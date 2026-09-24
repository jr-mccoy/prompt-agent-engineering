---
title: "MRI Spine Report Interpretation"
category: domain-healthcare-clinical/interpretation
description: "Read an MRI spine report to separate emergencies (cord compression, cauda equina, epidural abscess) from degenerative findings, correlate levels to root and cord syndromes, and commit to surgical, steroid, antibiotic, or conservative action."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - neurosurgery
  - spine
  - radiology
  - mri-spine
  - interpretation
updated: "2026-09-24"
---

## Objective

Read an MRI spine report against the neurologic exam and produce an impression that first answers "is this a surgical or oncologic emergency?", then correlates each degenerative finding to the symptomatic root or cord level, and commits to the action. Input is the report or structured findings, not images.

## Inputs

- MRI report: region(s) imaged (cervical, thoracic, lumbar, whole spine), sequences (T1, T2, STIR, post-gadolinium), findings by level, impression
- Neurologic exam: motor by myotome, sensory level, reflexes, Babinski/Hoffmann, saddle anesthesia, bladder (post-void residual), bowel, gait
- Red flags: cancer history, fever, IV drug use, bacteremia, immunosuppression, anticoagulation, recent spinal procedure, trauma, osteoporosis
- Labs if infection/tumor considered: WBC, ESR, CRP, blood cultures
- Prior imaging

## Role

Senior spine surgeon or neurology attending reading the MRI report with the exam in hand.

## Reasoning Steps

1. **Emergency screen first.**
   - **Metastatic epidural spinal cord compression (MESCC):** epidural tumor contacting or deforming the cord; grade degree of compression (Bilsky/ESCC scale: 0–1 epidural only, 2 cord deformed with CSF visible, 3 cord compressed with no CSF visible). Cord T2 signal = myelopathic injury.
   - **Cauda equina syndrome:** large central disc or mass compressing the thecal sac below the conus with saddle anesthesia, urinary retention, or bilateral radicular deficits.
   - **Spinal epidural abscess / discitis-osteomyelitis:** T2/STIR disc hyperintensity, endplate erosion, enhancing disc and paraspinal/epidural collection; rim-enhancing epidural collection.
   - **Epidural hematoma, cord infarct, acute transverse myelitis.**

2. **Numbering check.** Transitional lumbosacral anatomy and counting errors shift the "level" by one — confirm the report's numbering against prior imaging or whole-spine localizer before planning surgery.

3. **Cord signal.** Compressive myelopathy (focal T2 signal at stenosis); longitudinally extensive lesion ≥3 vertebral segments → NMOSD (AQP4), MOGAD, sarcoid, infection; short peripheral dorsal/lateral lesion → MS; dorsal column T2 signal over multiple segments → subacute combined degeneration (B12, copper, nitrous oxide).

4. **Degenerative findings — correlate or ignore.** Disc bulge (broad, >25% circumference) vs protrusion vs extrusion vs sequestration. Paracentral L4–5 disc → traversing L5 root; foraminal/far-lateral L4–5 → exiting L4 root. Central canal and lateral recess stenosis; foraminal stenosis; spondylolisthesis and instability; Modic endplate changes. Asymptomatic disc degeneration, bulges, and protrusions are common and rise with age — a finding counts only if it matches the dermatome, myotome, and reflex.

5. **Vertebral body lesions and fractures.** T1-hypointense marrow replacement → metastasis/myeloma. Malignant compression fracture: convex posterior border, pedicle/posterior element involvement, epidural or paraspinal mass. Osteoporotic: retained fatty marrow, retropulsed fragment, fluid sign, no mass. Stability for tumor: SINS score.

6. **Action by syndrome.**
   - **MESCC with deficit:** dexamethasone 10 mg IV load, then 4 mg q6h (with PPI and glucose monitoring); spine surgery and radiation oncology the same day; decompression + stabilization then RT for high-grade compression with deficit in a surgical candidate; RT alone for radiosensitive tumors without instability or for non-surgical candidates (NOMS framework). Image the whole spine — multi-level disease is common.
   - **Cauda equina:** emergent decompression; do not wait for morning.
   - **Epidural abscess:** blood cultures ×2 then vancomycin (weight-based, AUC-guided) + cefepime 2 g IV q8h (or ceftriaxone 2 g IV q12h); surgical decompression for neurologic deficit or failure; CT-guided biopsy if cultures negative and stable.
   - **Radiculopathy without red flags:** 6 weeks of conservative care; surgical referral for progressive motor deficit or intractable pain.
   - **Cervical myelopathy with cord signal:** surgical referral — degenerative myelopathy tends to progress.

7. **Pitfalls before signing.** Treating the MRI instead of the patient (surgery for incidental bulges); missing a second level of epidural disease by imaging one region; omitting gadolinium when infection or tumor is suspected; "mild stenosis" read with severe bladder symptoms — exam wins; a normal lumbar MRI does not exclude a thoracic or cervical cord lesion causing leg symptoms.

## Output Format

```
STUDY: [regions, sequences, contrast, numbering confirmed Y/N]
EMERGENCY: [MESCC grade / cauda equina / abscess / hematoma / none]
CORD: [signal, compression, level]
BY LEVEL: [level — disc/stenosis/root affected — concordant with exam Y/N]
VERTEBRAE: [marrow, fracture — benign vs malignant features]

IMPRESSION:
1. [finding + syndrome] — [action with doses and timing]
2. [next] — [action]
3. [non-concordant degenerative findings] — [no intervention]
```

## Worked Example

**Input:** 66 y/o M, metastatic prostate cancer diagnosed 1 year ago, on enzalutamide; not on ADT (declined). Two weeks of worsening mid-back pain, now 2 days of bilateral leg weakness (hip flexion 4/5 bilaterally), sensory level at T8, brisk knee reflexes, bilateral Babinski. PVR 180 mL. MRI whole spine with contrast: "T6 vertebral body and left pedicle metastasis with ventral and left epidural extension compressing the spinal cord; no CSF visible around the cord at T6. Cord T2 hyperintensity at T6. No pathologic fracture. Additional metastases at L2 and L4 without epidural disease. Mild L4–5 disc bulge."

**Output:**

```
STUDY: Whole spine with gadolinium; numbering per report — confirm against prior staging CT before OR.
EMERGENCY: MESCC at T6, high-grade (cord compressed, no CSF visible — ESCC grade 3) with myelopathic cord signal.
CORD: Compressed at T6 with T2 signal change — concordant with T8 sensory level (level of sensory loss is often below the lesion), bilateral UMN signs.
BY LEVEL: L4–5 bulge — not concordant (patient has an upper motor neuron syndrome); ignore.
VERTEBRAE: T6 (body + pedicle), L2, L4 metastases; no collapse.

IMPRESSION:
1. Metastatic epidural spinal cord compression at T6 with motor deficit and retention.
   - Dexamethasone 10 mg IV now, then 4 mg IV q6h; pantoprazole 40 mg daily; fingerstick glucose q6h.
   - Neurosurgery and radiation oncology now — goal of decompression within 24–48 h of deficit onset. Pedicle involvement → calculate SINS; posterior decompression + stabilization followed by RT favored for high-grade compression with deficit in an ambulatory-potential patient with reasonable prognosis.
   - Foley catheter for retention; bowel regimen; mechanical VTE prophylaxis until surgical plan clear, then enoxaparin 40 mg daily post-op.
   - Log-roll precautions pending stability assessment.
   - Castration: testosterone level now; start ADT urgently — degarelix 240 mg SC (two 120 mg injections) avoids the testosterone flare that an LHRH agonist alone would cause with active cord compression.
   - Oncology informed; systemic therapy re-planned after local control.
2. L2 and L4 metastases without epidural disease — include in RT planning if painful; no surgical action.
3. L4–5 disc bulge — incidental, not concordant, no action.
```
