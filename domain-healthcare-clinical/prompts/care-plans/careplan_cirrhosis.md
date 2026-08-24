---
title: "Cirrhosis Longitudinal Care Plan"
category: domain-healthcare-clinical/care-plans
description: "Manage compensated and decompensated cirrhosis: variceal prophylaxis, ascites/SBP, hepatic encephalopathy, HCC surveillance, and transplant timing with named drugs and doses."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
  - DS-02
difficulty: advanced
tags:
  - hepatology
  - cirrhosis
  - care-plan
  - chronic-disease
updated: "2026-06-19"
---

## Objective

Produce a cirrhosis care plan: stage compensated vs decompensated, treat the etiology, and manage each complication (varices, ascites, SBP, hepatic encephalopathy, HCC surveillance) plus transplant evaluation timing. Output is a problem-oriented hepatology plan.

## Inputs

- Severity: Child-Pugh class, MELD-Na, compensated vs decompensated, etiology (alcohol, MASH, viral hepatitis, autoimmune, etc.)
- Complications: varices status (endoscopy), ascites, prior SBP, encephalopathy grade, prior variceal bleed, hepatorenal/hepatopulmonary
- Labs: bilirubin, INR, albumin, creatinine/Na, platelets, AFP
- Imaging: ultrasound/elastography, HCC surveillance status
- Meds, alcohol use, nutrition, vaccination status

## Role

Hepatologist or internist managing cirrhosis.

## Reasoning Steps

1. **Stage and treat etiology.** Alcohol cessation (the single most important step in alcohol-related cirrhosis), antiviral therapy for HBV/HCV, weight loss/metabolic control for MASH, immunosuppression for autoimmune. Treating the cause can recompensate.

2. **Varices / bleeding prophylaxis.** Risk-stratify (Baveno: low-risk compensated patients with platelets >150k and liver stiffness <20 may defer endoscopy). 
   - **Primary prophylaxis** for medium/large varices or clinically significant portal hypertension: non-selective beta-blocker — carvedilol 6.25 mg BID (preferred) or propranolol/nadolol titrated to HR; or endoscopic band ligation if beta-blocker intolerant.
   - **Post-bleed (secondary):** NSBB + serial band ligation; consider TIPS.

3. **Ascites.**
   - Sodium restriction <2 g/day; diuretics spironolactone 100 mg + furosemide 40 mg (100:40 ratio), titrate.
   - Refractory: large-volume paracentesis with albumin 6–8 g/L removed (>5 L); consider TIPS.
   - Avoid NSAIDs, ACEi/ARB (drop renal perfusion); avoid nephrotoxins.

4. **Spontaneous bacterial peritonitis (SBP).**
   - Diagnostic paracentesis on every admission/new ascites; SBP = ascitic PMN ≥250.
   - Treat: cefotaxime/ceftriaxone; **albumin 1.5 g/kg day 1, 1 g/kg day 3** (reduces hepatorenal syndrome).
   - **Secondary prophylaxis after SBP:** daily norfloxacin/ciprofloxacin or TMP-SMX. Primary prophylaxis if low ascitic protein + advanced disease.

5. **Hepatic encephalopathy.**
   - Identify precipitant (infection, GI bleed, constipation, dehydration, electrolytes, sedatives).
   - Lactulose titrated to 2–3 soft stools/day; add rifaximin 550 mg BID for recurrence prevention.

6. **HCC surveillance:** abdominal ultrasound ± AFP every 6 months for all cirrhotics.

7. **Transplant evaluation:** refer when decompensated or MELD-Na ≥15 (or earlier for HCC within criteria, refractory complications, quality-of-life). Manage MELD exceptions.

8. **General:** nutrition (avoid protein restriction; high-protein, frequent meals, treat sarcopenia), bone health, vaccinate (hepatitis A/B, pneumococcal, influenza, COVID), avoid hepatotoxins, cap acetaminophen ≤2 g/day, manage coagulopathy (do not over-correct INR routinely).

## Output Format

```
SEVERITY: Child-Pugh / MELD-Na / compensated vs decompensated
ETIOLOGY + TREATMENT:

COMPLICATION PLAN:
- Varices: [screening + prophylaxis agent/dose]
- Ascites: [sodium, diuretics, paracentesis/albumin, avoid-list]
- SBP: [diagnostic tap rule, treatment + albumin dosing, prophylaxis]
- Encephalopathy: [precipitant search, lactulose, rifaximin]

HCC SURVEILLANCE: [US ± AFP q6 mo]

TRANSPLANT: [referral trigger]

GENERAL:
- Nutrition, vaccines, hepatotoxin avoidance, acetaminophen cap

MONITORING:
- MELD/labs cadence, surveillance imaging

PITFALLS:
- [NSAIDs/ACEi in ascites, missing SBP albumin, protein restriction, beta-blocker in refractory ascites/hypotension]
```

## Worked Example

**Input:** 55 y/o M, alcohol-related cirrhosis, abstinent 3 months. Child-Pugh B, MELD-Na 16. Moderate ascites, no prior SBP. EGD: medium esophageal varices, no prior bleed. No encephalopathy. Platelets 88k, bilirubin 2.4, INR 1.5, Cr 0.9, Na 134, AFP 6. Last ultrasound 8 months ago.

**Output:**

```
SEVERITY: Child-Pugh B, MELD-Na 16, decompensated (ascites).
ETIOLOGY + TREATMENT: alcohol — reinforce abstinence (addiction support, the highest-yield intervention; recompensation possible). Nutrition optimization.

COMPLICATION PLAN:
- Varices: medium varices → primary prophylaxis with carvedilol 6.25 mg BID (preferred NSBB; also lowers portal pressure). If intolerant or contraindicated, band ligation program. Avoid NSBB if it causes hypotension with worsening ascites.
- Ascites: sodium <2 g/day; spironolactone 100 mg + furosemide 40 mg daily, titrate by weight/Na/K. Avoid NSAIDs and ACEi/ARB. Diagnostic paracentesis now to exclude subclinical SBP.
- SBP: none currently; check ascitic protein — if low, primary prophylaxis warranted given Child-Pugh B. Diagnostic tap on every admission. (If SBP arises: ceftriaxone + albumin 1.5 g/kg day 1, 1 g/kg day 3; then daily fluoroquinolone prophylaxis.)
- Encephalopathy: none now; counsel precipitant avoidance; have lactulose available.

HCC SURVEILLANCE: overdue — order abdominal ultrasound + AFP now, then q6 months.

TRANSPLANT: MELD-Na 16 (≥15) + decompensated → refer for transplant evaluation; document 3 months abstinence and continue.

GENERAL:
- High-protein diet, frequent meals, no protein restriction; treat sarcopenia.
- Vaccinate hepatitis A/B, pneumococcal, influenza, COVID.
- Acetaminophen ≤2 g/day; avoid other hepatotoxins/alcohol.
- Do not routinely correct INR 1.5 (not a true anticoagulant state).

MONITORING:
- MELD-Na/CMP/INR periodically; weight and renal function on diuretics; surveillance US q6 mo; EGD surveillance per protocol.

PITFALLS:
- No NSAIDs or ACEi/ARB with ascites (precipitate HRS).
- Don't miss the overdue HCC surveillance.
- If ascites becomes refractory or hypotension develops, reassess NSBB.
```
