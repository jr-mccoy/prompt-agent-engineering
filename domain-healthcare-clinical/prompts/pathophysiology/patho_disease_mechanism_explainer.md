---
title: "Disease Mechanism Explainer"
category: domain-healthcare-clinical/pathophysiology
description: "Explain the pathophysiology of any named disease as a causal chain from trigger through molecular, cellular, tissue, organ, and clinical levels."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - CR-01
  - CR-02
difficulty: advanced
tags:
  - pathophysiology
  - mechanism
  - teaching
  - reasoning
updated: "2026-05-08"
---

## Objective

Produce a complete pathophysiologic explanation of a named disease as a causal chain. Each link in the chain must be specific (named molecule, cell, channel, mediator) and must causally connect to the next link. The output explains why every clinical finding occurs, not just what occurs.

## Inputs

- Disease name (specific entity, e.g., "diabetic ketoacidosis," "primary biliary cholangitis," "tetralogy of Fallot," "acute promyelocytic leukemia")
- Optional: depth (resident-level vs subspecialty fellow-level), specific finding to focus on (e.g., "explain why this disease causes hyponatremia"), or known patient variant (e.g., "in a patient with G6PD deficiency")

## Role

Senior subspecialty attending teaching a resident on rounds. Direct, mechanistic, no hedging. The bar is: every "because" links to a named molecule or process; nothing handwaved.

## Reasoning Steps

1. **Define the entity.** One-line operating definition with the diagnostic anchor (e.g., "DKA = ketoacidosis with hyperglycemia and anion gap acidosis from absolute or relative insulin deficiency").

2. **Trigger.** What initiates the pathologic process. Genetic mutation, environmental exposure, infection, autoimmune trigger, structural defect, pharmacologic insult, metabolic stressor.

3. **Molecular level.** Specific molecules involved:
   - Affected proteins, channels, receptors (with names)
   - Signaling pathways disrupted (named pathways: JAK-STAT, PI3K-Akt-mTOR, RAS-MAPK, etc.)
   - Enzymes deficient or inhibited
   - Cytokines / chemokines / autoantibodies driving the process

4. **Cellular level.** What happens to specific cell populations:
   - Which cells gain or lose function
   - Apoptosis vs necrosis vs senescence vs dysplasia
   - Cell-cell signaling disrupted

5. **Tissue / microanatomic level.** Which tissue compartments are affected and how:
   - Inflammation pattern (acute, granulomatous, chronic, autoimmune)
   - Architectural changes (fibrosis, hyperplasia, atrophy, neoplasia)
   - Vascular changes (thrombosis, vasculitis, congestion, ischemia)

6. **Organ level.** How the tissue-level change produces organ dysfunction. Connect mechanism to function (e.g., "loss of nephron mass reduces filtration surface area → reduced GFR → urea and creatinine retention").

7. **Systemic / clinical level.** Walk every major clinical feature and explain it from the chain you just built:
   - Symptoms (why this symptom?)
   - Physical exam findings (why this sign?)
   - Lab abnormalities (why this lab pattern?)
   - Imaging findings (why this radiographic appearance?)
   - Complications (why these specific downstream problems?)

8. **Distinguishing features.** Briefly contrast with one or two diseases that share clinical features but differ mechanistically. This forces sharper definitions.

9. **Therapeutic targeting.** Map each major treatment back to which step in the chain it interrupts. This validates the chain — if you cannot explain why a treatment works using the mechanism you built, the mechanism is incomplete.

## Output Format

```
DEFINITION: [one line]

TRIGGER: [initiating event]

CAUSAL CHAIN:

Molecular level:
- [specific molecule/pathway] → [next event]
- [...]

Cellular level:
- [cell type and what happens to it] → [...]

Tissue level:
- [microanatomic change] → [...]

Organ level:
- [organ dysfunction] → [...]

Clinical manifestations (each explained from the chain):
- [Symptom/sign 1]: because [mechanistic link]
- [Symptom/sign 2]: because [mechanistic link]
- [Lab abnormality 1]: because [mechanistic link]
- [Imaging finding]: because [mechanistic link]
- [Complication]: because [mechanistic link]

DISTINGUISHING FROM SIMILAR ENTITIES:
- vs [related disease 1]: differs because [specific mechanism]
- vs [related disease 2]: differs because [specific mechanism]

THERAPEUTIC TARGETS (each mapped to a chain step):
- [Drug/intervention] → interrupts [specific step]
- [...]
```

## Worked Example

**Input:** Explain the pathophysiology of diabetic ketoacidosis.

**Output:**

```
DEFINITION: Anion gap metabolic acidosis from beta-hydroxybutyrate and acetoacetate accumulation due to absolute or relative insulin deficiency, with concurrent hyperglycemia from unopposed counter-regulatory hormones.

TRIGGER: Absolute insulin deficiency (T1DM diagnosis, missed insulin dose, pump failure) or relative insulin deficiency from a stressor that raises counter-regulatory hormones beyond what existing insulin can suppress (infection, MI, pancreatitis, steroids, cocaine, surgery, pregnancy).

CAUSAL CHAIN:

Molecular level:
- Insulin absent at adipocyte → hormone-sensitive lipase no longer suppressed → triglyceride hydrolysis releases free fatty acids (FFA) into circulation
- Insulin absent + glucagon rising → acetyl-CoA carboxylase activity falls → malonyl-CoA falls → CPT-1 disinhibited → FFA enter mitochondria for beta-oxidation
- Beta-oxidation produces acetyl-CoA in excess of TCA cycle capacity → acetyl-CoA shunted to ketogenesis (HMG-CoA synthase, HMG-CoA lyase) producing acetoacetate, beta-hydroxybutyrate, and acetone in hepatocyte mitochondria
- In peripheral tissues, insulin absent at GLUT4-bearing cells (muscle, adipose) → glucose uptake fails → hyperglycemia
- Counter-regulatory hormones (glucagon, cortisol, catecholamines, GH) drive hepatic gluconeogenesis (PEPCK, glucose-6-phosphatase) and glycogenolysis → adds to hyperglycemia

Cellular level:
- Hepatocytes export beta-hydroxybutyrate and acetoacetate into circulation as anionic ketoacids
- Skeletal muscle proteolysis accelerates (insulin normally suppresses ubiquitin-proteasome) → amino acid release fueling further gluconeogenesis
- Renal tubular cells: glucose load exceeds SGLT2 reabsorption capacity → glucosuria → osmotic diuresis with obligate Na, K, Mg, phosphate loss

Tissue level:
- Vascular: osmotic shifts pull intracellular water out (hyperglycemia raises serum osm); volume depletion reduces tissue perfusion
- Neuronal: cells can use ketones, so brain function preserved until acidosis severe; cerebral edema risk in pediatric DKA from rapid osmolar correction

Organ level:
- Kidney: osmotic diuresis → profound volume depletion → prerenal AKI on top of glucosuria
- Liver: shifted into ketogenic mode; cannot return until insulin resumes
- Pancreas: alpha-cells unopposed → glucagon excess maintains the catabolic state

Clinical manifestations (each explained from the chain):
- Polyuria: glucosuria draws water (osmotic diuresis)
- Polydipsia: extracellular hyperosmolality stimulates hypothalamic thirst centers
- Kussmaul respirations (deep, fast): respiratory compensation for metabolic acidosis (Winter's: PaCO2 = 1.5 × HCO3 + 8)
- Fruity breath: acetone (volatile, exhaled) from spontaneous decarboxylation of acetoacetate
- Abdominal pain: ileus from acidosis and electrolyte derangement; sometimes pancreatitis as trigger or consequence
- Anion gap acidosis: ketoacids dissociate to ketone anions + H+; H+ titrates HCO3 → HCO3 falls, AG rises by amount of ketoanions
- Hyperkalemia (often) on initial labs despite total-body K depletion: insulin absent → no Na/K-ATPase drive into cells; acidosis shifts K out (less than once thought, but contributes); osmotic shift drags K out with water
- Hyponatremia (corrected upward for glucose): high glucose pulls water from ICF to ECF, diluting serum Na; correct by adding 2.4 mEq Na per 100 glucose >100
- Elevated BUN/Cr: prerenal AKI from osmotic diuresis volume depletion
- Leukocytosis without infection: stress response, catecholamines, demargination — does not by itself indicate infection in DKA

DISTINGUISHING FROM SIMILAR ENTITIES:
- vs Hyperosmolar Hyperglycemic State (HHS): HHS has residual insulin sufficient to suppress ketogenesis but inadequate to handle glucose; therefore very high glucose (often >600), high osm (often >320), but minimal ketosis and minimal acidosis. Mechanism diverges at "is there enough insulin to keep CPT-1 inhibited?" — yes in HHS, no in DKA.
- vs Alcoholic Ketoacidosis (AKA): AKA from NADH excess (ethanol metabolism via ADH and ALDH) blocking gluconeogenesis and pushing acetoacetate toward beta-hydroxybutyrate. Glucose is usually normal or low in AKA (depleted glycogen, blocked gluconeogenesis), distinguishing from DKA's hyperglycemia.
- vs Starvation Ketoacidosis: same lipolysis-ketogenesis chain but moderate ketonemia, mild acidosis, normal-to-low glucose, slow onset over days. Insulin still functional and rises after eating.

THERAPEUTIC TARGETS (each mapped to a chain step):
- IV insulin → restores GLUT4 glucose uptake, suppresses lipolysis (HSL) and ketogenesis at the source. The single most important intervention.
- IV fluids → reverses osmotic-diuresis volume loss, dilutes hyperglycemia, restores tissue perfusion, lowers counter-regulatory hormone surge
- Potassium replacement → replaces total-body K deficit unmasked once insulin drives K back into cells; failing to replace → fatal arrhythmia mid-treatment
- Trigger management → infection workup and treatment, MI workup, etc., because the trigger continues driving counter-regulatory hormones until controlled
- Bicarbonate is rarely indicated → the acidosis self-corrects as ketoacids are metabolized once insulin resumes; bicarbonate adds risk of paradoxical CSF acidosis and hypokalemia. Reserve for pH <6.9 with hemodynamic compromise.
```
