---
title: "Chronic Pain Multimodal Care Plan"
category: domain-healthcare-clinical/care-plans
description: "Build a multimodal chronic non-cancer pain plan: mechanism-based non-opioid pharmacology, non-pharmacologic therapies, functional goals, and opioid stewardship with named drugs and doses."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
  - DS-02
difficulty: advanced
tags:
  - pain-medicine
  - chronic-pain
  - opioid-stewardship
  - care-plan
updated: "2026-06-19"
---

## Objective

Produce a multimodal chronic non-cancer pain care plan: classify the pain mechanism, build mechanism-based non-opioid pharmacotherapy and non-pharmacologic therapy around functional goals, and apply opioid stewardship (risk assessment, limits, monitoring, tapering) where opioids are involved. Output is a function-focused, multimodal plan.

## Inputs

- Pain: location, mechanism (nociceptive, neuropathic, nociplastic/central, mixed), duration, severity, functional impact (work, sleep, mood, activity)
- Prior treatments: non-opioids, opioids (agent/dose/MME, duration), interventional procedures, PT, response
- Risk: opioid risk (ORT/history of SUD), mental health (depression/anxiety/PTSD), prior overdose, concurrent benzodiazepines/sedatives, PDMP review
- Comorbidities (renal/hepatic/cardiac affecting NSAID/medication choice), goals

## Role

Pain medicine or primary care attending managing chronic non-cancer pain.

## Reasoning Steps

1. **Set functional goals, not just pain scores** — improved function/quality of life is the target. Establish baseline function and realistic goals.

2. **Classify the pain mechanism** — drives drug selection:
   - **Nociceptive** (OA, mechanical): topical/systemic NSAID, acetaminophen, topical agents, exercise.
   - **Neuropathic** (radiculopathy, neuropathy, postherpetic): gabapentinoid (gabapentin, pregabalin), SNRI (duloxetine), TCA (nortriptyline), topical lidocaine/capsaicin.
   - **Nociplastic/central** (fibromyalgia): duloxetine, milnacipran, pregabalin, TCA; emphasize exercise, CBT, sleep; opioids generally ineffective/harmful.

3. **Non-opioid pharmacotherapy first**, combine across mechanisms; start low, titrate, adequate trial:
   - Duloxetine 30 → 60 mg (neuropathic, OA, fibromyalgia, comorbid depression).
   - Gabapentin titrated to 1800–3600 mg/day divided (or pregabalin 150–300+); renal dose-adjust; sedation/falls in elderly.
   - Nortriptyline 10–25 mg qhs titrated (anticholinergic/cardiac cautions).
   - Topicals: diclofenac gel, lidocaine 5% patch, capsaicin.

4. **Non-pharmacologic core (high-yield, durable):** structured exercise/physical therapy, CBT/acceptance-based therapy for pain, sleep optimization, weight management, treat comorbid depression/anxiety; interventional options (injections, RFA) for selected conditions.

5. **Opioid stewardship — opioids are not first-line for chronic non-cancer pain:**
   - If considered, risk-stratify (PDMP, SUD history, mental health, concurrent sedatives), discuss realistic benefit/harm, set functional goals and a treatment agreement.
   - Start low, use immediate-release, lowest effective dose; reassess benefit/harm; caution/justification at higher MME; avoid concurrent benzodiazepines.
   - Co-prescribe naloxone for higher-dose/risk; UDS and PDMP monitoring.

6. **Tapering** if harms outweigh benefits, no functional benefit, or by shared decision — slow, individualized taper (e.g., 5–10%/month or slower); never abrupt in long-term users (withdrawal, destabilization, transition to illicit use). Treat withdrawal and offer SUD treatment (buprenorphine) if opioid use disorder is present.

7. **Address comorbid mental health and sleep** — untreated depression/anxiety/insomnia amplify pain.

8. **Monitor:** function (not just pain), adherence, side effects, opioid metrics (MME, PDMP, UDS) when applicable, mood, goal progress; reassess regularly.

## Output Format

```
PAIN MECHANISM / FUNCTIONAL BASELINE + GOALS:

NON-OPIOID PHARMACOTHERAPY (mechanism-based):
- [agent, dose, titration by mechanism]

NON-PHARMACOLOGIC CORE:
- PT/exercise, CBT, sleep, weight, interventional, mental health

OPIOID STEWARDSHIP (if applicable):
- Risk assessment / PDMP / agreement / naloxone / limits / monitoring

TAPER PLAN (if applicable):
- Rate, withdrawal management, OUD pathway (buprenorphine)

MONITORING:
- Function, side effects, opioid metrics, mood, goals

PITFALLS:
- [chasing pain scores, opioids for nociplastic pain, opioid+benzo, abrupt taper, ignoring mental health]
```

## Worked Example

**Input:** 54 y/o F, chronic low back pain with right L5 radiculopathy (neuropathic + mechanical), 3 years. On oxycodone IR ~40 MME/day with poor functional benefit, plus lorazepam for anxiety. No SUD history. Tried PT briefly. Depressed mood, poor sleep. eGFR normal.

**Output:**

```
PAIN MECHANISM / GOALS: mixed mechanical low back + L5 neuropathic radiculopathy. Functional baseline poor; goals: return to walking program, improved sleep, reduced disability — not a zero pain score.

NON-OPIOID PHARMACOTHERAPY:
- Duloxetine 30 mg → 60 mg: covers neuropathic pain, chronic musculoskeletal pain, AND comorbid depression — high-value single agent here.
- Add gabapentin titrated (e.g., 300 mg qhs → 300 TID → up to 1800–3600/day) for the radicular/neuropathic component (renal normal). Watch sedation, especially with the opioid/benzo on board.
- Topical: lidocaine 5% patch or diclofenac gel for localized component.

NON-PHARMACOLOGIC CORE:
- Re-engage structured PT/graded exercise (the durable intervention) and a walking program tied to goals.
- CBT for chronic pain + treat depression/insomnia (sleep hygiene; the duloxetine helps mood).
- Consider epidural steroid injection / interventional eval for the radiculopathy.

OPIOID STEWARDSHIP:
- Oxycodone is providing poor functional benefit and is co-prescribed with lorazepam — a dangerous combination (respiratory depression/overdose). 
- Review PDMP; co-prescribe naloxone now.
- The plan is to taper opioid given lack of functional benefit, while building the multimodal regimen.

TAPER PLAN:
- First reduce the opioid–benzodiazepine overlap risk: coordinate a slow lorazepam taper (anxiety addressed via duloxetine/CBT) and a slow oxycodone taper ~10%/month (slower if difficult), never abrupt.
- If opioid use disorder surfaces during taper, offer buprenorphine and SUD treatment.

MONITORING: function and goal progress (not just pain score), side effects/sedation, mood/sleep, PDMP/UDS during taper, MME trend.

PITFALLS:
- The opioid + benzodiazepine combination is the priority safety issue — naloxone + coordinated taper.
- Don't escalate opioids for poorly-responsive mixed pain; build the non-opioid/multimodal base.
- Taper slowly; treat the depression and sleep that amplify the pain.
```
