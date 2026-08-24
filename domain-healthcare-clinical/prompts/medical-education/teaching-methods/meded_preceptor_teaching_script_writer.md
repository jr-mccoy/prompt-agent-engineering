---
title: "Preceptor Teaching Script Writer"
category: healthcare-clinical/medical-education
description: "Write specific, level-calibrated teaching scripts for clinical preceptors using One-Minute Preceptor, SNAPPS, and teaching moment formats for common clinical presentations."
techniques:
  - RP-02
  - ST-02
  - CM-02
  - OC-01
  - ED-01
difficulty: beginner
tags:
  - preceptor
  - omp
  - snapps
  - clinical-teaching
  - teaching-scripts
  - ambulatory
updated: "2026-05-15"
related_prompts:
  - domain-healthcare-clinical/prompts/medical-education/teaching-methods/meded_small_group_facilitation_guide.md
  - domain-healthcare-clinical/prompts/medical-education/feedback-remediation/meded_learner_feedback_composer.md
  - domain-healthcare-clinical/prompts/medical-education/meded_faculty_development_module_designer.md
---

# Preceptor Teaching Script Writer

**Objective:** Generate verbatim, level-calibrated teaching scripts for clinical preceptors using structured teaching models—One-Minute Preceptor, SNAPPS, Think Aloud, and Teaching Moment Cards—so the preceptor can focus on facilitation rather than improvisation.

## When to Use
- ✅ Preceptor preparing to teach a specific learner level in a defined clinical setting (clinic, rounds, ED)
- ✅ New faculty or preceptor who wants concrete scripted language before their first teaching encounter
- ✅ Faculty development workshop where real-world scripts are needed as teaching exemplars
- ✅ Program director building a preceptor toolkit for a specific rotation or specialty
- ❌ Do NOT use to generate clinical management plans or patient care recommendations—scripts probe and coach; the learner generates all clinical answers
- ❌ Do NOT use when no specific clinical presentation has been identified; scripts require a concrete clinical scenario

## Inputs Required
- **Learner level:** M1 / M2 / M3 / M4 / Resident PGY-X / Fellow
- **Clinical specialty / rotation:** (e.g., Internal Medicine, Family Medicine, Emergency Medicine, Surgery)
- **Encounter type:** Outpatient clinic visit / Inpatient rounds presentation / Emergency department consult / Procedural supervision
- **Clinical presentation:** (e.g., undifferentiated dyspnea, acute low back pain, new-onset hypertension, chest pain)
- **Time available for teaching interaction:** < 5 minutes / 5-10 minutes / > 10 minutes
- **Teaching model preference:** OMP / SNAPPS / Think Aloud / Teaching Moment Card / Auto-select

## Constraints

**Must:**
- Produce verbatim scripted language for each step of the selected teaching model
- Calibrate vocabulary, probing depth, and clinical expectations to the specified learner level
- Limit teaching points to 1-3 per encounter (cognitive load cap)
- Include at least one level-appropriate time-pressure adaptation for encounters < 5 minutes

**Must Not:**
- Provide clinical answers or management recommendations—scripts must probe and elicit, never instruct toward a clinical conclusion
- Apply the same script verbatim to a different learner level without re-calibration
- Generate more than 3 discrete teaching points regardless of encounter length
- Use OMP in situations where SNAPPS is the better fit (see model selector below) without flagging the mismatch

## Instructions

### Step 1: Collect Context Inputs
Ask the educator to specify all six inputs listed above before generating any script. If the educator does not specify a teaching model, apply the Auto-select logic in Step 2.

### Step 2: Select the Teaching Model
Apply the following selection logic:

| Scenario | Best Model |
|---|---|
| Learner gives brief, unstructured presentation; preceptor needs to initiate teaching | **One-Minute Preceptor (OMP)** |
| Learner is trained to use SNAPPS and initiates structured self-presentation | **SNAPPS coaching moves** |
| Preceptor wants to model expert clinical reasoning aloud for a novice | **Think Aloud** |
| Single abnormal finding at bedside; teaching must happen in < 2 minutes | **Teaching Moment Card** |
| Time < 5 minutes and encounter is complex | **Compressed OMP (Steps 1-3 only)** |

State the selected model and rationale before generating the script.

### Step 3: Generate the OMP Script (if OMP selected)
For each of the five OMP steps, produce 2-3 scripted questions or statements the preceptor can use verbatim. Calibrate to learner level as follows:

**Step 3a — Get a Commitment**
Elicit a specific diagnostic or management commitment. Do not accept vague answers.
- M3: "What do you think is the most likely diagnosis for this patient?"
- Resident PGY1-2: "What's your leading diagnosis and what's your one diagnosis you can't miss?"
- Resident PGY3+: "Walk me through your differential hierarchy and where you want to start on the workup."

**Step 3b — Probe for Supporting Evidence**
Ask the learner to justify their commitment with clinical data, not just intuition.
- M3: "What finding from the history made you think of that?"
- Resident PGY1-2: "What about the exam supports that diagnosis over the others on your differential?"
- Resident PGY3+: "Walk me through the pathophysiology that connects this presentation to that diagnosis."

**Step 3c — Teach a General Rule**
State one transferable teaching point in a "When X, always think Y" or "The key principle here is Z" format. Limit to one concept.

**Step 3d — Reinforce What Was Right**
Name the specific thing the learner did well. Generic praise ("Good job") does not count.
- Script: "You correctly identified that the onset pattern was the pivot point in the history—that's exactly the right instinct for undifferentiated dyspnea."

**Step 3e — Correct Mistakes Gently**
Use a non-shaming redirection. Deliver in private when possible.
- Script: "One thing I'd add—when you're thinking about X, it's worth also considering Y because of Z. Let's talk about that."

### Step 4: Generate SNAPPS Coaching Moves (if SNAPPS selected)
For each of the six SNAPPS steps, produce scripted preceptor response moves—what to say when the learner completes each step. The learner drives; the preceptor responds.

| SNAPPS Step | Scripted Preceptor Response Move |
|---|---|
| **S** — Summarize history/exam | "Good summary. Tell me the one finding that most changed your thinking." |
| **N** — Narrow differential to 2-3 | "Why did you leave [diagnosis] off the list?" |
| **A** — Analyze by comparing/contrasting | "What's the clinical feature that best distinguishes [Dx A] from [Dx B] in this patient?" |
| **P** — Probe preceptor with a question | [Preceptor answers, then asks: "What made you think to ask that question?"] |
| **P** — Plan management | "What would make you revise the plan in the next 24 hours?" |
| **S** — Select self-study issue | "Good choice. Let's reconnect tomorrow with what you found—two minutes is enough." |

### Step 5: Generate Think Aloud Script (if Think Aloud selected)
Produce a 6-8 sentence monologue the preceptor delivers while reviewing the case or examining the patient, narrating expert reasoning transparently:

Structure:
1. Name what you are attending to ("I'm noticing the JVD and bilateral crackles together...")
2. Name your hypothesis generation ("That combination immediately makes me think of...")
3. Name your uncertainty explicitly ("What I'm not sure about is whether...")
4. Name your next move and why ("So my next step is X because Y...")
5. Invite the learner in ("What would you prioritize next and why?")

### Step 6: Generate Teaching Moment Card (if Teaching Moment Card selected)
Produce a 2-minute bedside script structured as:
1. **Orient** (15 sec): "Before we leave the room, I want to teach you one thing about what we just found."
2. **Name** (15 sec): State the finding clearly. "This patient has a diastolic murmur at the left sternal border."
3. **Explain** (45 sec): Mechanism or clinical significance in plain language, calibrated to learner level.
4. **Connect** (30 sec): Link to a transferable rule. "Whenever you hear a diastolic murmur, it's pathological until proven otherwise—there's no benign diastolic murmur."
5. **Check** (15 sec): One retrieval question. "So where would you place this on the differential?"

### Step 7: Apply Time-Pressure Adaptation
If time available is < 5 minutes, specify which steps to compress or cut:
- **OMP < 5 min**: Steps 1 (commitment) + 2 (evidence probe) + 3 (one rule). Skip steps 4-5; deliver reinforcement/correction during sign-out.
- **SNAPPS < 5 min**: Steps S + N + P (plan) only; defer self-study selection.
- **Teaching Moment Card**: Already designed for < 2 minutes; use as-is.

### Step 8: Flag Cognitive Load Cap
After generating the script, audit it and confirm it contains no more than 3 teaching points. If more were generated, strike the lower-priority points and note them for a follow-up encounter.

### Step 9: Output the Complete Script
Present the script in a preceptor-usable format with:
- Model name and rationale
- Verbatim scripted language for each step, labeled by step name
- Learner level calibration note
- Teaching point(s) identified (1-3)
- Time-pressure adaptation (if applicable)

---

## Worked Example

**Inputs:** PGY2 Internal Medicine resident / Inpatient rounds / Undifferentiated dyspnea / 10 minutes available / OMP

**Output:**

**Model:** One-Minute Preceptor — selected because the learner gave a brief unstructured presentation and the preceptor needs to initiate teaching.

**Learner level note:** PGY2 — probe for evidence-based reasoning and differential prioritization; do not stop at "I think it's CHF." Push to the evidence and the can't-miss diagnoses.

---

**OMP Step 1 — Get a Commitment**
- "Before we look at the chart, tell me your leading diagnosis right now."
- "Walk me through your top two—what's most likely and what's the diagnosis you can't afford to miss?"
- "If you had to commit to a diagnosis in the next 60 seconds, what would it be and why?"

**OMP Step 2 — Probe for Supporting Evidence**
- "What specific finding on exam made you favor CHF over pneumonia in this patient?"
- "The creatinine is elevated. How does that change your differential?"
- "You mentioned orthopnea. Walk me through how you weighted that against the other historical features."

**OMP Step 3 — Teach a General Rule**
*Teaching point (1 of 1):* "Here's the rule I use for undifferentiated dyspnea: organize your differential by time course first. Acute onset in minutes points to PE, pneumothorax, flash pulmonary edema. Hours to days shifts you toward pneumonia, AECOPD, or decompensated heart failure. The time course is the pivot before the exam or any test."

**OMP Step 4 — Reinforce What Was Right**
- "You correctly anchored to the exam—the JVD and S3 together are high-yield and you named them both. That's the right instinct."
- "Your differential was appropriately prioritized. Putting PE on the list even though it felt less likely shows good clinical discipline."

**OMP Step 5 — Correct Gently (in private at sign-out)**
- "One thing to add to your toolkit—when dyspnea is acute and the SpO2 is dropping faster than expected for the degree of distress, that asymmetry is worth flagging as a red flag for PE or pneumothorax even if the presentation looks like CHF. Worth adding to your mental checklist."

**Teaching points generated: 1** (time-course pivot for dyspnea). Cognitive load cap satisfied.

---

## False-Positive Prevention

| ❌ Common Mistake | ✅ Correct Approach |
|---|---|
| Scripts that answer the clinical question ("The diagnosis here is CHF, so you should...") | Scripts probe and coach; the learner generates all clinical conclusions. Preceptor language stays in question mode until the teach-a-rule step |
| Using the same script for M3 and PGY3 | M3 probing targets foundational pattern recognition ("What finding made you think of that?"); PGY3 probing targets edge cases, synthesis, and uncertainty management ("What would change your management if the troponin came back borderline positive?") |
| More than 3 teaching points per encounter | Cognitive load research (Miller, van Merriënboer) consistently shows 1-3 points per encounter. If you generate more, strike the lowest-priority ones and save them for a follow-up |
| Using OMP when SNAPPS would fit better | OMP: preceptor-initiated after a brief, unstructured learner presentation. SNAPPS: learner-initiated structured self-presentation. If the learner is trained in SNAPPS and uses it, switch to SNAPPS coaching moves—don't override the learner's structure with OMP |
| Generic praise ("Good job, nice work") | Name the specific behavior reinforced: "You identified the time-course asymmetry—that's the key pivot in undifferentiated dyspnea." Behavioral specificity drives learning |

## Output Format

**Section 1 — Teaching Context Summary**
- Learner level, specialty, encounter type, time available, model selected, rationale

**Section 2 — Complete Teaching Script**
- One subsection per OMP/SNAPPS/Think Aloud/Teaching Moment Card step
- Each subsection contains 2-3 verbatim scripted options (choose the one that fits the moment)
- Teaching points labeled and numbered

**Section 3 — Time-Pressure Adaptation**
- Steps to cut/compress if time shrinks unexpectedly

**Section 4 — Teaching Points Audit**
- List of all teaching points generated; confirm ≤ 3; flag any removed for follow-up encounter

## Verification Checklist
- [ ] Learner level specified and all script language calibrated to that level
- [ ] Teaching model selected with rationale stated before script generation begins
- [ ] No more than 3 teaching points present in the final script
- [ ] All scripted questions probe and elicit—none deliver clinical answers
- [ ] Time-pressure adaptation included for encounters under 5 minutes
- [ ] At least one verbatim reinforcement statement names a specific behavior (not generic praise)
- [ ] Correction script is non-shaming and suitable for private delivery
