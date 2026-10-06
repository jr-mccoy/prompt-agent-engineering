---
title: "Generalized Anxiety / Panic Disorder Care Plan"
category: domain-healthcare-clinical/care-plans
description: "Build a care plan for generalized anxiety and panic disorder: SSRI/SNRI selection and slow titration, CBT, time-limited benzodiazepine use, and monitoring with named drugs and doses."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
  - DS-02
difficulty: intermediate
tags:
  - psychiatry
  - anxiety
  - panic
  - care-plan
updated: "2026-10-06"
---

> **Medical disclaimer — read before use.** This prompt is a decision-support and
> teaching aid for **licensed clinicians**. It is **not medical advice** and is not for
> patients to diagnose or treat themselves. Drug doses, thresholds and guideline
> references in it and in its worked example may be incomplete, outdated or wrong:
> verify each one against the current guideline, the product label and your local
> formulary, and follow your institution's protocols. It does not replace examination
> or clinical judgment. **Medical emergency: call your local emergency number (911 in
> the US).**
>
> **Review status:** AI-assisted content, reviewed by AI only (2026-10-06);
> **not yet reviewed by a licensed clinician.**

## Objective

Produce a care plan for generalized anxiety disorder and/or panic disorder: first-line pharmacotherapy with anxiety-specific titration, psychotherapy, judicious time-limited adjuncts, and monitoring. Output is a combined medication + therapy plan.

## Inputs

- Diagnosis/severity: GAD-7 score, panic frequency/severity, agoraphobic avoidance, duration, functional impairment
- Comorbidity: depression (PHQ-9), substance use, bipolar screen, medical mimics (hyperthyroidism, arrhythmia, stimulant/caffeine, pheo)
- History: prior trials, benzodiazepine use/dependence risk, response/tolerability
- Concurrent meds, pregnancy/lactation, substance use disorder history

## Role

Psychiatrist or primary care attending managing anxiety disorders.

## Reasoning Steps

1. **Confirm diagnosis and exclude mimics/comorbidity:** check TSH, review caffeine/stimulants/substances; screen depression and bipolarity; ECG if cardiac symptoms.

2. **Measurement-based care:** baseline GAD-7 (and panic diary); track response.

3. **First-line pharmacotherapy: SSRI or SNRI.** Sertraline, escitalopram, paroxetine, venlafaxine XR, duloxetine.
   - **Start lower than for depression** (e.g., sertraline 25 mg, escitalopram 5 mg) — anxious patients are sensitive to early activation/jitteriness that can mimic worsening anxiety and cause dropout. Titrate up over 1–2 weeks to therapeutic range.
   - Set expectations: full effect takes 4–6 weeks.

4. **Psychotherapy: CBT** (including exposure for panic/agoraphobia) is first-line, comparable efficacy, durable — combine with medication or as monotherapy.

5. **Adjuncts:**
   - **Buspirone** for GAD (non-dependent, slower onset).
   - **Hydroxyzine** or **propranolol** (situational/performance) as non-dependent options.
   - **Benzodiazepines:** reserve for short-term bridging during SSRI onset or severe acute distress; time-limited, scheduled rather than escalating PRN; avoid in substance use disorder; counsel dependence/tolerance/cognitive effects. Not first-line, not long-term in most.
   - **Pregabalin** for GAD where available.

6. **Non-response:** ensure adequate dose/duration (6–8 weeks), confirm adherence and CBT engagement, then switch SSRI↔SNRI or augment.

7. **Duration:** continue effective treatment ≥12 months after response (relapse-prone); taper slowly.

8. **Monitor:** GAD-7/panic frequency, emergent SI, activation, benzodiazepine use, substance use, adherence; counsel caffeine reduction, sleep, exercise.

## False-Positive Prevention

❌ **DON'T:**
- Grade panic disorder by GAD-7 alone — it is not a panic measure; track attack frequency and avoidance (diary or a panic severity scale) as their own field.
- Write a benzodiazepine "bridge" without a stop date, total quantity and taper; open PRN refills become long-term use by default, and step 5 already prefers scheduled over escalating PRN dosing — keep the plan consistent with it.
- Pick an adjunct whose evidence is for the other disorder — buspirone is a GAD option, not a panic treatment; propranolol for performance anxiety does not treat panic disorder.
- Treat "TSH normal" as excluding every mimic; arrhythmia, stimulants, caffeine, alcohol or sedative withdrawal and substance use each need their own entry.
- Prescribe propranolol without checking asthma/bradycardia history, or hydroxyzine without QT and anticholinergic burden in older adults.

✅ **DO:**
- Recompute the GAD-7 total from item scores when they are given and map it to the instrument's severity band.
- Check the low start dose against age, hepatic function and interacting drugs (CYP2D6 for paroxetine/fluoxetine, QT for citalopram/escitalopram).
- In older adults, record a benzodiazepine as a falls and cognition risk (Beers criteria) and note the non-dependent alternative that was considered.
- Start the non-response clock on the date the therapeutic dose was reached, and confirm the plan says so before calling a trial inadequate.

## Output Format

```
DIAGNOSIS / SEVERITY (GAD-7 / panic) / MIMICS EXCLUDED:
COMORBIDITY (depression / SUD / bipolar):

PHARMACOLOGIC PLAN:
- First-line SSRI/SNRI: [drug, LOW start dose, titration, target]
- Onset expectations

PSYCHOTHERAPY: CBT / exposure

ADJUNCTS:
- Buspirone / hydroxyzine / propranolol
- Benzodiazepine (if any): time-limited plan + cautions

NON-RESPONSE PATHWAY:
DURATION / TAPER:

MONITORING:
- GAD-7, SI, activation, benzo/substance use, caffeine/sleep

PITFALLS:
- [starting too high → activation dropout, long-term benzodiazepines, missing hyperthyroidism/substances, under-dosing]
```

## Worked Example

**Input:** 29 y/o M, panic disorder with early agoraphobic avoidance, ~3 panic attacks/week, GAD-7 14. TSH normal, drinks 4 cups coffee/day, no substance use disorder, no bipolar history, not on meds. Requests "something that works fast."

**Output:**

```
DIAGNOSIS / SEVERITY: panic disorder + emerging agoraphobia, GAD-7 14. Mimics excluded (TSH normal); high caffeine is a contributor.
COMORBIDITY: no SUD, no bipolar, screen depression.

PHARMACOLOGIC PLAN:
- First-line: sertraline 25 mg daily (LOW start — panic patients are activation-sensitive; a high start can trigger a panic surge and dropout). Titrate to 50 mg after 1 week, then toward 100–200 as needed.
- Set expectation: meaningful benefit at 4–6 weeks, not immediately.

PSYCHOTHERAPY: refer for CBT with interoceptive + situational exposure — first-line for panic/agoraphobia, prevents avoidance entrenchment. Highest durable benefit.

ADJUNCTS:
- Caffeine reduction is high-yield here — taper coffee.
- For the "works fast" gap during SSRI onset: short, time-limited clonazepam 0.25–0.5 mg BID, scheduled (not escalating PRN), for ≤2–4 weeks as a bridge (no SUD history) — scheduled taper, explicit dependence counseling. Prefer propranolol or hydroxyzine if any dependence concern.

NON-RESPONSE PATHWAY: if inadequate at 6–8 weeks adequate dose → switch to venlafaxine XR or augment; ensure CBT engagement first.

DURATION / TAPER: continue ≥12 months after response; slow taper.

MONITORING:
- GAD-7 + panic diary each visit; emergent SI/activation early; reassess and discontinue the benzodiazepine on schedule; caffeine, sleep, exercise.

PITFALLS:
- Do not start sertraline at 50–100 — activation can mimic/trigger panic and cause dropout.
- Keep the benzodiazepine time-limited; CBT + SSRI is the durable plan.
- Address caffeine — a reversible driver.
```
