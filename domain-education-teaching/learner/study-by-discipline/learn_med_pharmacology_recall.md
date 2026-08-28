---
title: "Medical Pharmacology Recall"
category: education-teaching/learner/study-by-discipline
description: "Drug-class retrieval system for medical students: generates mechanism → indication → adverse effects → contraindications → monitoring recall drills for drug classes, with anti-confusion pairs for commonly confused drugs and prototype-first scaffolding."
techniques:
  - ST-01
  - ST-02
  - ED-02
  - NE-04
  - QA-01
difficulty: advanced
tags:
  - medical-education
  - pharmacology
  - USMLE
  - drug-classes
  - adverse-effects
  - mechanisms
  - retrieval-practice
updated: "2026-05-15"
related_prompts:
  - domain-education-teaching/learner/study-by-discipline/learn_med_clinical_reasoning_drill.md
  - domain-education-teaching/learner/memory-and-recall/learn_retrieval_drill_designer.md
  - domain-education-teaching/learner/memory-and-recall/learn_flashcard_quality_auditor.md
---

## Objective

Generate retrieval drills for pharmacology that go beyond "name the drug": mechanism → indication → adverse effects → contraindications → monitoring, with prototype-first scaffolding (learn the class through its best-known member), anti-confusion pairs for commonly confused drugs, and a self-scoring rubric targeting the specific knowledge gaps most tested on USMLE and shelf exams.

## When to Use

- During preclinical pharmacology study (USMLE Step 1 preparation)
- During clinical rotations when pharmacological knowledge needs reinforcement for real patient care
- When a learner knows drug names but confuses mechanisms or adverse effect profiles
- When preparing for USMLE Step 2 CK, where pharmacology appears in clinical vignette context

**Do not use** as a primary learning tool for a drug class seen for the first time — read the mechanism in a resource first, then drill. This is a retrieval and consolidation tool.

## Instructions

1. **Collect inputs.**
   - Ask: "Which drug class(es) do you want to drill? (Be specific: e.g., 'beta-blockers,' 'ACE inhibitors,' 'aminoglycosides,' 'SSRIs')"
   - Ask: "What is your level? (Preclinical/Step 1, Clinical/Step 2, Residency/In-service)"
   - Ask: "Which component is weakest: mechanism, indication, adverse effects, contraindications, or monitoring?"
   - Ask: "Any specific drug pairs you frequently confuse?"

2. **For each drug class, identify the prototype.**
   The prototype is the member of the class that is:
   - Most tested (USMLE high-yield)
   - Most representative of the class mechanism
   - Most likely to appear as the "key example" in vignettes
   Drill the prototype first. Then, after the prototype is solid, drill the class differences (how other class members differ from the prototype).

3. **Generate the 5-component drug card for each class.**

   **Component 1 — Mechanism:**
   State the mechanism at the receptor/enzyme/channel level:
   "[Drug/class] → [receptor/enzyme/channel] → [molecular effect] → [physiological consequence]"
   
   Include:
   - The specific receptor subtype if relevant (e.g., β1-selective vs. non-selective)
   - Reversible vs. irreversible binding if clinically relevant
   - Any active metabolites that alter effect duration

   **Component 2 — Indications:**
   List indications from highest to lowest USMLE yield:
   - Mark exam-favorite indications with ★
   - Note indications that are CLASS-wide vs. specific to certain members

   **Component 3 — Adverse effects:**
   Organize by system (cardiac, GI, CNS, renal, hepatic, hematologic, dermatologic):
   - ★ High-yield / most tested adverse effects
   - Flag any **Black Box Warning (BBW)** — these are USMLE favorites
   - Note which adverse effects are mechanism-based (predictable) vs. idiosyncratic (unpredictable)

   **Component 4 — Contraindications:**
   - Absolute contraindications (never use)
   - Relative contraindications (use with caution)
   - Drug-drug interactions: name the most clinically dangerous pair for this class

   **Component 5 — Monitoring:**
   - What labs/parameters to check before starting
   - What to monitor during therapy
   - What indicates toxicity and what to do

4. **Generate anti-confusion pairs.**
   For each class, identify the drug most frequently confused with it:
   - Same organ system, different mechanism
   - Same drug class, different adverse effect profile
   - Similar name, different action
   For each pair, provide the minimal distinguishing rule (one sentence or comparison table row).

5. **Build the recall drill.**
   Run the drill in two formats:

   **Format A — Free recall (cover the card):**
   "Without looking: for [class/prototype], state: (1) mechanism, (2) top indication, (3) most dangerous adverse effect, (4) main contraindication, (5) monitoring parameter."

   **Format B — Vignette-based application:**
   Provide a 2–3 sentence clinical vignette where the question is: "Which drug/class is most likely responsible for this finding?" or "Which drug is most appropriate for this patient?"

6. **Include a class-member comparison table** for classes with multiple clinically important members.

## Output Format

```
# Pharmacology Recall Drill: [Drug Class]
Level: [Step 1/2/Residency] | Weakness: [component] | Classes: N

---

## [Drug Class] — Prototype: [Drug Name]

### Mechanism
[Receptor/enzyme/channel] → [molecular effect] → [physiological effect]

### Indications ★ = High yield
★ [Top indication]
- [Other indication]

### Adverse Effects
★ [Most tested] — [Mechanism: predictable/idiosyncratic]
⚠ [Black Box Warning if applicable]
By system:
- Cardiac: ...
- GI: ...
- [etc.]

### Contraindications
Absolute: ...
Relative: ...
Key drug-drug interaction: [Drug A + Drug B = effect]

### Monitoring
Before starting: [Lab/parameter]
During therapy: [Lab/parameter]
Toxicity sign: [Finding] → Action: [Response]

---

### Anti-Confusion Pair
[This class] vs. [Commonly confused class/drug]: [Minimal distinguishing rule]

---

### Recall Drill

**Format A — Free recall:**
Cover the card above. State:
1. Mechanism: ___
2. Top indication: ___
3. Most dangerous adverse effect: ___
4. Main contraindication: ___
5. Monitoring parameter: ___

**Format B — Vignette:**
[Clinical vignette + question]

*Answer:* [Drug/class + brief explanation]

---

### Class-Member Comparison (if applicable)
| Member | vs. Prototype | Key difference |
|---|---|---|

---

[Repeat for each class]

## Session Summary
Classes drilled: N
Weakest component across this session: ___
Anti-confusion pairs to review: [list]
```

## Example Output

---

**Input:** Drug classes: ACE inhibitors, ARBs, beta-blockers — Level: Step 2 CK — Weakness: contraindications — Confusion pair: ACE inhibitors vs. ARBs

---

# Pharmacology Recall Drill: CV Medications
Level: USMLE Step 2 CK | Weakness: Contraindications | Classes: 3

---

## ACE Inhibitors — Prototype: Lisinopril

### Mechanism
**ACE inhibitors** → inhibit Angiotensin-Converting Enzyme → ↓ conversion of Angiotensin I → Angiotensin II → ↓ Ang II effects (vasoconstriction, aldosterone release, sympathetic activation) → ↓ BP, ↓ preload and afterload, ↓ aldosterone → ↑ K⁺, ↓ Na⁺ retention

Also: ↑ bradykinin (ACE also degrades bradykinin) → key mechanism of cough and angioedema adverse effects

### Indications ★ = High yield
★ Hypertension (first-line in most patients, especially with proteinuria or DM)
★ Heart failure with reduced ejection fraction (HFrEF) — reduces mortality
★ Post-MI — reduces ventricular remodeling, reduces mortality
★ Diabetic nephropathy — renoprotective (reduces proteinuria independently of BP lowering)
- Chronic kidney disease with proteinuria

### Adverse Effects
★ **Dry cough** — ↑ bradykinin → prostaglandin-mediated bronchial irritation (predictable, class effect, 5–20% of patients)
⚠ **Black Box Warning: Angioedema** — can be life-threatening; often affects lips, tongue, throat. Higher risk in Black patients. Can occur even after years of use.
⚠ **Black Box Warning: Fetal toxicity** — contraindicated in pregnancy (2nd/3rd trimester causes fetal renal failure, oligohydramnios, fetal death)
★ **Hyperkalemia** — ↓ aldosterone → ↑ K⁺; dangerous in renal failure or with K⁺-sparing diuretics
★ **First-dose hypotension** — especially in hypovolemic patients
- Acute kidney injury (↑ Cr by 10–20% is acceptable; > 30% increase → stop)

By system:
- Renal: ↑ Cr (dilate efferent arteriole → ↓ GFR → initially ↑ Cr, but renoprotective long-term)
- Electrolytes: Hyperkalemia
- Respiratory: Cough (↑ bradykinin), angioedema (same mechanism, more dangerous)

### Contraindications
**Absolute:**
- Pregnancy ⚠
- Prior angioedema from ACE inhibitor
- Bilateral renal artery stenosis (dilating efferent arteriole in a kidney with fixed afferent stenosis → drops GFR → acute renal failure)
- Concurrent use with ARB + ACE inhibitor + aliskiren triple combination (↑ adverse effects without benefit)

**Relative:**
- Hyperkalemia (K⁺ > 5.5)
- Cr > 3.0 (advanced CKD — use with caution, not absolutely contraindicated)
- Single kidney with renal artery stenosis

**Key drug-drug interaction:**
ACE inhibitor + K⁺-sparing diuretic (spironolactone/amiloride) = severe hyperkalemia risk; ACE inhibitor + NSAIDs = blunted antihypertensive effect + increased AKI risk

### Monitoring
Before starting: BMP (baseline Cr and K⁺), urinalysis for proteinuria
During therapy: Recheck BMP in 1–2 weeks after initiation, then periodically; monitor BP
Toxicity sign: K⁺ > 5.5 → reduce dose or stop; Cr increase > 30% from baseline → stop temporarily

---

### Anti-Confusion Pair: ACE Inhibitors vs. ARBs

| Feature | ACE Inhibitor (e.g., Lisinopril) | ARB (e.g., Losartan) |
|---|---|---|
| Mechanism | Blocks ACE → ↓ Ang II production | Blocks AT1 receptor → Ang II produced but can't bind |
| Cough | **Yes** — ↑ bradykinin (5–20%) | **No** — bradykinin not affected |
| Angioedema | Yes (less common than thought) | Very rare — but can cross-react |
| Use in pregnancy | ⚠ Contraindicated | ⚠ Contraindicated (same mechanism) |
| K⁺ effects | ↑ K⁺ (same) | ↑ K⁺ (same) |
| Renal protection | Yes (similar to ARB) | Yes (similar to ACE inhibitor) |

**Minimal distinguishing rule:** "ACE inhibitors cause cough (bradykinin). ARBs don't. Everything else is nearly identical. Switch to ARB when patient can't tolerate ACE inhibitor cough."

---

### Recall Drill

**Format A — Free recall (cover the card — 90 seconds):**
1. ACE inhibitor mechanism: ___
2. Top indication (most USMLE-tested): ___
3. Most dangerous adverse effect (Black Box): ___
4. Main absolute contraindication: ___
5. What to monitor before starting: ___

**Model answers:**
1. Block ACE → ↓ Ang II → ↓ BP + ↑ bradykinin
2. Hypertension with DM or proteinuria / HFrEF / post-MI
3. Angioedema (can cause airway obstruction, especially in Black patients)
4. Pregnancy / bilateral renal artery stenosis / prior angioedema
5. BMP (Cr and K⁺) and urinalysis

---

**Format B — Vignette:**
A 52-year-old Black man with hypertension and diabetes is started on lisinopril. Four days later, he presents with progressive swelling of his lips and tongue and difficulty swallowing. He denies rash or hives. What is the most likely diagnosis, and what is the next step?

*Answer:*
**Diagnosis:** ACE inhibitor-induced angioedema (bradykinin-mediated — NOT histamine, so no hives)
**Next step:** Stop lisinopril immediately; administer epinephrine if airway is compromised; supportive care; do NOT restart any ACE inhibitor. Black patients have 4–5× higher risk of ACE inhibitor angioedema.
**Future management:** Switch to ARB (losartan) — different mechanism, much lower risk of angioedema.

---

## Beta-Blockers — Prototype: Metoprolol (β1-selective)

### Mechanism
**Beta-blockers** → competitively block β-adrenergic receptors → ↓ sympathetic outflow effects

Metoprolol: **β1-selective** → ↓ HR, ↓ contractility, ↓ conduction velocity, ↓ renin secretion

Non-selective (propranolol): blocks β1 + β2 → same cardiac effects + bronchoconstriction + ↓ glycogenolysis

### Indications ★ = High yield
★ Hypertension
★ HFrEF — reduces mortality (start low dose, titrate up; do NOT give in acute decompensation)
★ Post-MI — reduces mortality, prevents remodeling
★ Angina (↓ O₂ demand by ↓ HR × ↓ contractility)
★ Rate control in AFib/AFlutter
- Hyperthyroidism (symptom control) — propranolol preferred (non-selective)
- Migraine prophylaxis — propranolol
- Essential tremor — propranolol
- Pheochromocytoma prep — **only after alpha-blocker** (see contraindication)

### Adverse Effects
★ **Bradycardia / AV block**
★ **Hypotension**
★ **Masking of hypoglycemia** — ↓ tachycardia response (the primary warning sign); sweating still intact
- **Bronchoconstriction** — β2 blockade → only a problem with non-selective beta-blockers; β1-selective (metoprolol) safer in mild asthma
- **Cold extremities** — peripheral vasoconstriction
- **Fatigue, depression, sexual dysfunction**
- **Rebound hypertension/angina** on abrupt discontinuation

### Contraindications
**Absolute:**
- Acute decompensated heart failure
- Severe bradycardia or high-degree AV block (without pacemaker)
- Reactive airway disease / significant asthma (non-selective agents; β1-selective are relative contraindication)
- Uncontrolled pheochromocytoma without prior alpha-blockade → unopposed alpha stimulation → hypertensive crisis

**Key drug-drug interaction:**
Beta-blocker + non-dihydropyridine CCB (diltiazem/verapamil) = additive AV block + bradycardia → life-threatening

### Monitoring
Before starting: HR, BP, EKG (to rule out baseline bradycardia/AV block)
During therapy: HR, BP; watch for exacerbation of reactive airway disease
Toxicity: Bradycardia → atropine or temporary pacing; severe overdose → glucagon (bypasses β-receptor)

---

### Anti-Confusion Pair: β1-selective vs. non-selective beta-blockers

| Feature | β1-Selective (Metoprolol, Atenolol) | Non-Selective (Propranolol, Carvedilol) |
|---|---|---|
| Receptor | β1 only | β1 + β2 (carvedilol also α1) |
| Asthma/COPD risk | Lower (prefer in mild asthma) | Higher — avoid |
| Hypoglycemia masking | Both mask tachycardia | Both |
| Migraine, tremor | Not preferred | Propranolol preferred |
| AFib rate control | Both effective | Both |

**Minimal distinguishing rule:** "Metoprolol/atenolol = heart-selective. Propranolol = everything. When in doubt about asthma: choose metoprolol."

---

## Session Summary

Classes drilled: 3 (ACE inhibitors, ARBs, beta-blockers)
Weakest component target: Contraindications — review bilateral renal artery stenosis (ACEI) and pheochromocytoma (beta-blocker order of operations)
Anti-confusion pairs to review next session:
- ACE inhibitor vs. ARB (cough distinction)
- β1-selective vs. non-selective beta-blocker (asthma safety)

---

## False-Positive Prevention

**❌ DON'T** drill all drugs in a class simultaneously before the prototype is solid. Learning losartan before lisinopril is mechanistically redundant and creates interference.

**✅ DO** master the prototype mechanism first, then add class-member differences as differentiating features from the established baseline.

**❌ DON'T** treat adverse effect recall as a list to memorize. Each adverse effect follows mechanistically from the drug's action — connect each effect to its mechanism.

**✅ DO** include the mechanism in parentheses next to each adverse effect: "Cough (↑ bradykinin → prostaglandin-mediated irritation)" — this makes adverse effects memorable and helps with novel vignette recognition.

**❌ DON'T** omit contraindications in recall drills — they are consistently high-yield on USMLE and are one of the components learners skip during studying.

**✅ DO** include at least one contraindication in Format A recall and at least one contraindication scenario in Format B vignettes.

**❌ DON'T** use drug names as mnemonics if they don't reveal mechanism (e.g., "lopril" = ACE inhibitor is not a mechanism memory — it's naming memory).

**✅ DO** anchor memory to mechanism ("ACE = Angiotensin Converting Enzyme; ACE inhibitors block this enzyme; result: ↑ bradykinin [cough, angioedema] and ↓ Ang II [↓ BP, ↓ aldosterone, ↑ K⁺]").

## Quality Criteria

- [ ] Each drug class has all 5 components (mechanism, indication, AE, CI, monitoring)
- [ ] Mechanism is stated at the receptor/enzyme/channel level with physiological consequence
- [ ] ★ markers identify USMLE high-yield items
- [ ] Black Box Warnings are flagged with ⚠
- [ ] Anti-confusion pair includes a comparison table and a minimal distinguishing rule
- [ ] Format B vignette tests real-world application, not just recall
- [ ] Class-member comparison table is included for classes with ≥3 clinically distinct members

## Techniques Used

- **ST-01 (Clear Objective Statement):** Objective specifies mechanism-linked recall (not list memorization) — the key distinction for USMLE vignette application
- **ST-02 (Structured Sequential Instructions):** Six-step process enforces prototype-first ordering before class-member variants
- **ED-02 (Progressive Exercise Generation):** Two recall formats escalate from free recall (Format A) to vignette application (Format B)
- **NE-04 (Good vs Bad Example Calibration):** Anti-confusion pair section shows the contrast between similar drugs explicitly — not just "don't confuse these"
- **QA-01 (Self-Verification):** Format A provides model answers for self-scoring; vignette answer reveals the reasoning, not just the drug name
