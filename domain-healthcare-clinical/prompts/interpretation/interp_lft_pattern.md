---
title: "Liver Function Test Pattern Interpretation"
category: domain-healthcare-clinical/interpretation
description: "Read LFTs, classify hepatocellular vs cholestatic vs mixed pattern, calculate R factor, assess synthetic function, and direct workup."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: intermediate
tags:
  - hepatology
  - liver
  - lfts
  - jaundice
  - interpretation
updated: "2026-05-08"
---

## Objective

Read a set of liver function tests and produce a structured interpretation: classify the pattern (hepatocellular, cholestatic, mixed, isolated hyperbilirubinemia), assess synthetic function and severity, list the differential in order of likelihood given context, and commit to next workup steps.

## Inputs

- Aminotransferases: AST, ALT
- Cholestatic markers: ALP, GGT
- Bilirubin: total, direct (and indirect calculated)
- Synthetic function: albumin, INR/PT, total protein
- Patient context: age, sex, alcohol use, medications (acetaminophen, statins, antibiotics, herbals, anabolic steroids, methotrexate, isoniazid, anti-epileptics), risk factors (IVDU, tattoos, transfusions, sexual exposures, travel), comorbidities (DM/obesity → NAFLD; right heart failure → congestive hepatopathy; iron overload, autoimmune)
- Prior LFTs for trending
- Imaging if available (RUQ US, MRCP, CT)

## Role

Senior internist or hepatologist reading the panel with the chart open.

## Reasoning Steps

1. **Pattern classification (R factor).**
   - R = (ALT / ULN_ALT) / (ALP / ULN_ALP)
   - **R > 5: Hepatocellular** — AST/ALT predominantly elevated
   - **R < 2: Cholestatic** — ALP predominantly elevated
   - **R 2–5: Mixed**
   - Confirm cholestatic ALP is hepatic (not bone) with GGT. ALP up + GGT up → hepatic. ALP up + GGT normal → bone (Paget, mets, growing children, vitamin D deficiency).

2. **Magnitude pattern.**
   - **ALT/AST <5× ULN:** chronic — NAFLD/NASH (most common cause in 2026), chronic viral hepatitis B/C, hemochromatosis, autoimmune hepatitis, A1AT deficiency, Wilson, celiac, thyroid disease, drug-induced.
   - **ALT/AST 5–15× ULN:** acute viral hepatitis, autoimmune flare, drug-induced (acetaminophen, INH, antibiotics), alcoholic hepatitis (but rarely >300; AST:ALT >2 with both <300 is the classic ratio).
   - **ALT/AST >15× ULN (often >1000):** four classic causes —
     - Acetaminophen toxicity (AST/ALT often >3000, dose history, NAC indicated; King's College criteria for transplant)
     - Acute viral hepatitis (HAV, HBV, HCV acute, HEV in pregnancy/immunocompromised, HSV in immunocompromised or pregnancy)
     - Ischemic hepatitis ("shock liver") — sudden rise in setting of hypotension, often LDH disproportionately elevated, recovers fast with hemodynamic stabilization
     - Autoimmune hepatitis flare

3. **Cholestatic pattern.**
   - **Intrahepatic:** primary biliary cholangitis (middle-aged women, AMA+, pruritus), primary sclerosing cholangitis (associated with IBD, MRCP shows beading), drug-induced cholestasis (estrogens, augmentin, anabolic steroids), infiltrative disease (sarcoid, lymphoma, amyloid, mets), sepsis cholestasis, TPN cholestasis.
   - **Extrahepatic:** common bile duct stone, malignant stricture (cholangiocarcinoma, pancreatic head mass, ampullary), benign stricture, AIDS cholangiopathy.
   - **Imaging is essential:** RUQ ultrasound first (rules in/out ductal dilation). If dilated → MRCP or ERCP. If not dilated and AMA negative → liver biopsy.

4. **Isolated hyperbilirubinemia.**
   - **Indirect (unconjugated) >85%:** hemolysis (high LDH, low haptoglobin, indirect predominance, smear), ineffective erythropoiesis, Gilbert syndrome (mild fluctuating jaundice, otherwise normal LFTs, fasting/illness triggers).
   - **Direct (conjugated) >50%:** Dubin-Johnson, Rotor, or biliary obstruction with otherwise normal aminotransferases (early or partial obstruction).

5. **Synthetic function.**
   - **Albumin:** chronic synthetic function. <3 in liver disease suggests cirrhosis or chronic illness.
   - **INR:** acute synthetic function. Elevated INR in liver disease that does not correct with vitamin K = significant hepatic synthetic failure.
   - **Acute liver failure (ALF):** INR ≥1.5 + any degree of encephalopathy + no preexisting liver disease + duration <26 weeks. Transfer to transplant center; do not wait.

6. **Severity stratification.**
   - **MELD-Na** for chronic liver disease prognosis and transplant listing.
   - **Maddrey discriminant function** for alcoholic hepatitis steroid decision (>32 = severe).
   - **King's College criteria** for acetaminophen ALF transplant listing.
   - **Child-Pugh** for cirrhosis severity (bilirubin, albumin, INR, ascites, encephalopathy).

7. **Trends.** Aminotransferases that suddenly drop in a patient with rising INR and worsening encephalopathy = ominous (hepatocyte loss, not recovery).

8. **Workup commit.**
   - Hepatocellular acute: acetaminophen level, viral hepatitis serologies (HAV IgM, HBsAg, anti-HBc IgM, anti-HCV with reflex RNA, HEV IgM), autoimmune panel (ANA, ASMA, anti-LKM, IgG), ceruloplasmin (Wilson — under 40), iron studies + ferritin (hemochromatosis), A1AT level, drug history including supplements.
   - Hepatocellular chronic: same minus acute serologies; add fasting lipid panel + glucose + HbA1c + abdominal ultrasound for NAFLD.
   - Cholestatic: RUQ ultrasound first. AMA (PBC), MRCP (PSC). Tumor markers if mass concerns. ERCP if therapeutic intent.

## Output Format

```
PATTERN: [hepatocellular / cholestatic / mixed / isolated hyperbili — type]
R FACTOR: [calculated]
MAGNITUDE: [<5×, 5–15×, >15× ULN]
SYNTHETIC FUNCTION: [albumin, INR — preserved or impaired]
SEVERITY (if applicable): [MELD-Na, Maddrey, Child-Pugh, ALF criteria]

DIFFERENTIAL (in order):
1. [most likely given context]
2. [next]
3. [next]

ACTION:
- [imaging]
- [serologies / drug levels]
- [treatment now if specific etiology supported]
- [transfer / consult criteria]
```

## Worked Example

**Input:** 28 y/o F, found obtunded by roommate. Empty acetaminophen bottle nearby; estimated ingestion ~28 hours ago. Vitals: BP 102/64, HR 102, RR 18, T 37.1, alert but confused (oriented x1). Today: AST 4820, ALT 5210, ALP 110, total bili 3.8 (direct 2.6), albumin 3.4, INR 3.2, glucose 62, Cr 1.7, lactate 4.0. Acetaminophen level 18 (28 hours post-ingestion). No prior liver disease.

**Output:**

```
PATTERN: Hepatocellular (markedly).
R FACTOR: (5210 / 40) / (110 / 120) = 130 / 0.92 ≈ 142 → far above 5.
MAGNITUDE: >100× ULN aminotransferases — classic massive hepatocellular injury.
SYNTHETIC FUNCTION: INR 3.2 (impaired), albumin 3.4 (preserved acutely as expected). Hypoglycemia (62) is a synthetic-failure marker — gluconeogenic capacity gone.
SEVERITY: Acute liver failure — INR ≥1.5 + encephalopathy + no preexisting disease.
  - King's College criteria for acetaminophen: arterial pH <7.30 OR (INR >6.5 + Cr >3.4 + grade III–IV encephalopathy). Currently does not meet, but trajectory is what matters; reassess every 4–6 hours.

DIFFERENTIAL:
1. Acetaminophen-induced acute liver failure — ingestion history, time course, magnitude of aminotransferases, hypoglycemia, coagulopathy, encephalopathy. Acetaminophen level 18 at 28 hours is misleadingly low because it is post-distribution; use Rumack-Matthew nomogram only for single acute ingestion <24 hours, not here.
2. Less likely: acute viral hepatitis, ischemic hepatitis (no documented hypotension), autoimmune flare. Check anyway given severity.

ACTION:
- N-acetylcysteine immediately, do not wait for additional labs. IV NAC 21-hour protocol: 150 mg/kg loading over 1 hour, 50 mg/kg over 4 hours, 100 mg/kg over 16 hours. Continue NAC beyond 21 hours if INR remains >2 or AST/ALT still rising — extend until improvement or liver failure resolution.
- Call regional transplant center NOW. Do not wait for King's College criteria to formally trigger — these patients can deteriorate over hours and transfer windows close.
- D10W infusion to maintain glucose >70; check finger-stick q1h. Hypoglycemia is the single most reversible immediate threat to brain function.
- Coagulopathy management: do NOT correct INR with FFP unless actively bleeding or invasive procedure required — INR is the prognostic marker the transplant team needs. Vitamin K 10 mg IV once is reasonable.
- Monitor ICP indirectly: serial neuro exams, head CT if rapid decline. Grade III–IV encephalopathy → intubate, head of bed 30°, hypertonic saline if cerebral edema suspected.
- Labs q4–6h: BMP, INR, AST/ALT, bilirubin, ammonia, lactate, ABG. Also: hepatitis serologies (HAV IgM, HBsAg, anti-HBc IgM, anti-HCV, HEV IgM), ANA, ASMA, ceruloplasmin (less likely at this age but cheap), pregnancy test, salicylate level (co-ingestion possible), urine tox.
- Avoid all hepatotoxic and renally cleared drugs. AKI is now part of the picture; no more contrast, no NSAIDs.
- Psychiatric consult once medically stable — intentional ingestion needs safety planning.
```
