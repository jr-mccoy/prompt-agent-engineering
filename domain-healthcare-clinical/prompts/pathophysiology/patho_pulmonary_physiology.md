---
title: "Pulmonary Physiology Reasoning"
category: domain-healthcare-clinical/pathophysiology
description: "Reason through ventilation, perfusion, gas exchange, V/Q matching, hypoxic vasoconstriction, lung compliance, and pulmonary vascular resistance to explain a pulmonary or critical-care presentation and predict the response to oxygen, PEEP, position, and pulmonary vasodilators."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - CR-01
difficulty: advanced
tags:
  - pulmonology
  - critical-care
  - physiology
  - mechanism
  - gas-exchange
updated: "2026-05-12"
---

## Objective

Reason through a pulmonary or critical-care presentation by separating the five mechanisms of hypoxemia (hypoventilation, V/Q mismatch, shunt, diffusion limitation, low FiO2), assessing lung mechanics (compliance, resistance, dead space) and pulmonary vascular tone, and predicting the physiologic response to increases in FiO2, PEEP, positioning (prone), and inhaled or systemic pulmonary vasodilators. Tie reasoning to specific ventilator and clinical actions.

## Inputs

- Clinical scenario (e.g., severe ARDS, COPD exacerbation, massive PE, hepatopulmonary syndrome, ILD with PHTN, high-altitude pulmonary edema)
- ABG (pH, PaCO2, PaO2, HCO3, FiO2)
- Vent settings or O2 device (mode, Vt, RR, PEEP, FiO2; or NC L/min, NRB, HFNC flow + FiO2)
- Mechanics: plateau pressure, driving pressure (Pplat − PEEP), static compliance, peak airway pressure
- Imaging (chest X-ray, CT) and echo if available

## Role

Senior pulmonary / critical-care physician reasoning at the bedside. Names the mechanism, computes the gas exchange parameters, and predicts response to specific interventions.

## Reasoning Steps

1. **Compute oxygenation indices.**
   - **A–a gradient:** A–a = PAO2 − PaO2; PAO2 = FiO2 × (760 − 47) − PaCO2/0.8 (sea level, RA: PAO2 ≈ 150 − PaCO2/0.8).
     - Normal A–a ≈ (age/4) + 4 (room air).
     - Elevated A–a with hypoxemia narrows mechanism to V/Q mismatch, shunt, or diffusion limitation; normal A–a hypoxemia = hypoventilation or low FiO2.
   - **PaO2/FiO2 (P/F ratio):** marker of oxygenation efficiency; <300 = ARDS-spectrum, <200 moderate, <100 severe (Berlin definition uses ≥5 cm H2O PEEP).
   - **Oxygenation index (OI) = (mean airway pressure × FiO2 × 100) / PaO2** — used in pediatrics and severe ARDS.
   - **Shunt fraction (Qs/Qt):** at FiO2 1.0, persistent hypoxemia with PaO2 not rising = shunt physiology. Rule of thumb: every 1% increase in shunt drops PaO2 by ~3 torr on 100% O2.

2. **Identify the dominant mechanism(s) of hypoxemia.**
   - **Hypoventilation:** elevated PaCO2 drives PAO2 down. A–a *normal*. PaO2 corrects with raising FiO2 modestly. Etiologies: CNS depression, neuromuscular weakness, severe airflow obstruction with CO2 retention.
   - **V/Q mismatch (most common cause of clinically significant hypoxemia):** units with low V/Q ratio (ventilation < perfusion) produce blood with low O2 saturation. Corrects readily with supplemental O2 because raising alveolar O2 in poorly ventilated units still oxygenates the blood flowing through. Etiologies: asthma/COPD exacerbation, atelectasis, pneumonia (lobar with surrounding mismatch), PE (high V/Q dead space + low V/Q remodeling), pulmonary edema (mixed).
   - **Shunt:** alveoli with V/Q = 0 (no ventilation, full perfusion). Examples: lobar pneumonia consolidation, ARDS alveolar flooding, atelectasis (no aerated unit), AVM, intracardiac R→L (PFO with PHTN, Eisenmenger), hepatopulmonary syndrome (intrapulmonary vascular dilatations bypassing alveolar gas exchange). Does *not* correct with high FiO2 because the blood flowing through never sees alveolar gas. Hallmark: P/F ratio low + minimal response to FiO2 escalation.
   - **Diffusion limitation:** thickened alveolar–capillary membrane or shortened capillary transit time. Examples: ILD, pulmonary fibrosis, emphysema (loss of capillary bed → reduced transit time). Usually mild at rest but profound on exertion (transit time shortens).
   - **Low FiO2:** altitude — partial pressure of inspired O2 falls.

3. **Map V/Q distribution and the role of hypoxic pulmonary vasoconstriction (HPV).**
   - Normal lung: gravity creates a V/Q gradient (V/Q higher in apex, lower in base in upright); shunt fraction normally ~5% from bronchial circulation and Thebesian veins.
   - HPV: alveolar hypoxia (PAO2 <60 torr) → constriction of upstream pulmonary arterioles → blood diverted away from poorly ventilated units → improves V/Q matching.
   - Anesthesia, supraphysiologic FiO2, and pulmonary vasodilators *blunt* HPV → worsen V/Q mismatch (paradoxical drop in PaO2 sometimes seen with sodium nitroprusside, milrinone, dihydropyridines, isoflurane).
   - Atelectasis worsens V/Q mismatch; HPV partially compensates. Reopening (recruitment, PEEP) restores ventilation. Excess PEEP overdistends aerated units → diverts blood to non-aerated regions → worsens V/Q.

4. **Assess lung mechanics.**
   - **Compliance (C):** ΔV / ΔP. Static compliance = Vt / (Pplat − PEEP). Low compliance ("stiff lung") in ARDS, pulmonary edema, pulmonary fibrosis. Normal ~70–100 mL/cm H2O; severe ARDS often <30.
   - **Resistance (R):** (Ppeak − Pplat) / flow. High in airway obstruction (asthma/COPD), bronchospasm, secretions, ET tube obstruction.
   - **Driving pressure (ΔP = Pplat − PEEP):** strong predictor of mortality in ARDS. Target ≤15 cm H2O.
   - **Dead space (Vd/Vt):** ventilated but not perfused units. Elevated in PE (massive PE) and high PEEP (overdistension). Calculated by Bohr-Enghoff: Vd/Vt = (PaCO2 − PetCO2) / PaCO2. PE patients have characteristically wide PaCO2–PetCO2 gradient.
   - **Auto-PEEP (intrinsic PEEP):** dynamic hyperinflation; failure to fully exhale before next breath. Common in obstructive disease on mechanical ventilation; raises Ppeak, worsens hemodynamics (high intrathoracic pressure compresses venous return → hypotension). End-expiratory hold maneuver measures auto-PEEP.

5. **Map pulmonary vascular biology where relevant.**
   - **Pulmonary vascular resistance (PVR):** governed by lung volume (U-shaped, minimum at FRC; rises at low volumes via small-vessel compression and at high volumes via alveolar-vessel compression), alveolar oxygen (HPV), pH (acidosis raises PVR), endothelin (vasoconstrictor; bosentan, macitentan, ambrisentan block ETA receptor), NO / cGMP (sildenafil, tadalafil, riociguat enhance), prostacyclin (epoprostenol, treprostinil, iloprost, selexipag).
   - **Pulmonary hypertension classification (WHO):**
     - Group 1: PAH — primary, connective tissue, HIV, portopulmonary, drug-induced, congenital heart, schistosomiasis. Targeted by PAH drugs.
     - Group 2: left heart disease — most common; treat the LV problem.
     - Group 3: lung disease and hypoxia — COPD, ILD, OSA. Treat lung disease and hypoxia; PAH-targeted therapy only when group-1-pattern hemodynamics (mPAP elevated out of proportion to lung disease, PVR markedly elevated, normal/low PCWP).
     - Group 4: CTEPH — chronic thromboembolic. Surgical PEA when accessible; balloon pulmonary angioplasty for distal disease; riociguat.
     - Group 5: miscellaneous (sarcoid, hemoglobinopathy, metabolic).
   - **Acute pulmonary hypertension in ICU** (e.g., RV failure in massive PE): inhaled NO 5–40 ppm (selective pulmonary vasodilator — delivered to ventilated alveoli, vasodilates adjacent vessels, improves V/Q; inactivated quickly by hemoglobin so minimal systemic effect); inhaled epoprostenol / treprostinil; systemic milrinone or dobutamine for inotropic support.

6. **Predict response to intervention.**
   - **Increase FiO2:** corrects V/Q mismatch and diffusion limitation. Limited effect in shunt (>30% shunt → minimal PaO2 response to 100%).
   - **PEEP:** recruits atelectatic alveoli → reduces shunt → improves oxygenation; redistributes lung water in cardiogenic pulmonary edema; reduces preload + afterload effects (lowers LV transmural pressure); excess PEEP overdistends and worsens dead space, may impair venous return / RV function.
   - **Prone positioning:** redistributes ventilation to dorsal regions where perfusion is naturally greater (especially in supine ARDS where dorsal lung is consolidated); improves V/Q matching; reduces pleural pressure gradient → more homogenous lung stress and strain; PROSEVA trial showed mortality benefit when applied early in severe ARDS (P/F <150) for ≥16 h/day.
   - **Inhaled NO / inhaled epoprostenol:** selective pulmonary vasodilator delivered only to ventilated alveoli → vasodilates adjacent vessels → improves V/Q matching → rescue for severe hypoxemia in ARDS and RV failure. Does not reduce mortality in ARDS but useful as bridge.
   - **Neuromuscular blockade (cisatracurium):** reduces patient–ventilator asynchrony, reduces oxygen consumption, controls intra-thoracic pressure profile. Older data (ACURASYS) suggested mortality benefit in severe ARDS; ROSE trial did not replicate — use selectively for severe asynchrony or refractory hypoxemia, not routinely.
   - **Recruitment maneuver:** temporary high CPAP / sustained inflation to reopen atelectatic regions. ART trial showed harm with aggressive recruitment + decremental PEEP titration — generally avoid; gentle recruitment may help individual patients but not standard.
   - **ECMO (VV-ECMO):** for refractory hypoxemia despite optimal lung-protective ventilation, prone, NMB, and inhaled vasodilators. EOLIA / Bayesian re-analysis support VV-ECMO in severe ARDS. VV bypasses lung gas exchange; allows ultra-protective ventilation; VA for combined cardiac failure.

## Output Format

```
GAS EXCHANGE ASSESSMENT:
- PaO2 / FiO2 (P/F): [value]
- A–a gradient: [computed] (normal for age: [...])
- PaCO2: [value]; pH: [value]; HCO3: [value]
- Acid-base interpretation: [respiratory acid/alkalosis, metabolic compensation, mixed]
- Shunt response prediction: [estimate]

DOMINANT MECHANISM(S) OF HYPOXEMIA: [hypoventilation / V/Q mismatch / shunt / diffusion limitation / low FiO2; with relative weight]

LUNG MECHANICS:
- Static compliance: [Vt / (Pplat − PEEP)]
- Driving pressure: [Pplat − PEEP]
- Resistance: [Ppeak − Pplat / flow if available]
- Auto-PEEP / dead space concerns: [...]

PULMONARY VASCULAR ASSESSMENT (if relevant):
- Evidence of PHTN / RV strain
- HPV intact or blunted by current therapy

PREDICTED RESPONSE TO:
- ↑ FiO2: [...]
- ↑ PEEP: [recruitment vs overdistension; effect on shunt vs dead space]
- Prone: [V/Q redistribution prediction]
- iNO / inhaled epoprostenol: [selective vasodilation, V/Q effect]
- Diuresis: [if cardiogenic component]
- Bronchodilation: [if obstruction component]

SPECIFIC NEXT ACTIONS:
1. [Vent setting change with rationale]
2. [Pharmacologic adjustment]
3. [Diagnostic next step — POCUS, repeat ABG, CT, RHC]
4. [Goal physiology and target metric to reassess]

REASONS THE PATTERN IS NOT [alternative diagnosis]:
[Discriminating physiology/imaging that excludes adjacent mechanism]
```

## Worked Example

**Input:** 52-year-old previously healthy man, day 5 of COVID-19, intubated and ventilated. Settings: VC-AC, Vt 6 mL/kg PBW = 380 mL, RR 28, PEEP 14, FiO2 0.80. ABG: pH 7.31, PaCO2 52, PaO2 62, HCO3 25. Pplat 32, Ppeak 36. Chest X-ray: bilateral dense infiltrates. P/F = 78. Now hour 18 of mechanical ventilation. Explain the gas-exchange physiology and the next 4 actions.

**Output:**

```
GAS EXCHANGE ASSESSMENT:
- P/F = 62 / 0.80 = 78. Severe ARDS (Berlin).
- A–a gradient: PAO2 ≈ 0.80 × (760 − 47) − 52/0.8 = 570 − 65 = 505. A–a = 505 − 62 = 443 (massively widened).
- pH 7.31, PaCO2 52 — uncompensated respiratory acidosis; bicarb 25 not yet elevated → acute respiratory acidosis from permissive hypercapnia.
- Shunt-dominant physiology: P/F <100 with high FiO2 strongly suggests substantial shunt fraction. Estimated shunt ~30–40% (each 1% shunt ~3 torr drop on 100% O2; 100% O2 expected PaO2 ~673 in normal lung; current PaO2 62 on 80% suggests true shunt fraction near 35–40%).

DOMINANT MECHANISM(S) OF HYPOXEMIA:
- Shunt (alveolar flooding / consolidation from COVID-ARDS) — dominant; minimally responsive to further FiO2 increase.
- V/Q mismatch (heterogeneously injured lung) — secondary contributor.
- Permissive hypercapnia from low Vt strategy contributing to respiratory acidosis but not to hypoxemia.

LUNG MECHANICS:
- Static compliance = 380 / (32 − 14) = 380 / 18 = 21.1 mL/cm H2O — severely reduced (normal ~70–100; severe ARDS often <30).
- Driving pressure = Pplat − PEEP = 32 − 14 = 18 cm H2O — *above* target ≤15; associated with higher mortality. Must reduce.
- Resistance = (Ppeak − Pplat) / flow ≈ low/normal (Ppeak − Pplat = 4 with reasonable flow). Airway obstruction is *not* the main problem.
- No evidence of auto-PEEP at RR 28 with VC-AC; expiratory hold would confirm.

PULMONARY VASCULAR ASSESSMENT:
- Acute COR pulmonale common in severe COVID-ARDS at this severity. Recommend echo / POCUS to assess RV size, septal motion, TAPSE, RV function. Acidemia and high PEEP both raise PVR.
- HPV likely active but overwhelmed by extent of consolidation.

PREDICTED RESPONSE TO:
- ↑ FiO2 from 0.80 → 1.0: minimal PaO2 gain (shunt dominant). Will buy small margin but exposes patient to oxygen toxicity over time and does not address underlying problem.
- PEEP: Pplat already 32, driving pressure 18. Increasing PEEP alone without reducing Vt would overdistend and could worsen dead space and hemodynamics. PEEP titration to optimize compliance / driving pressure (esophageal balloon if available; transpulmonary pressure target end-inspiratory <20–25 cm H2O, end-expiratory positive).
- Prone positioning: high-yield. Will redistribute ventilation toward dorsal lung (where most perfusion lies), recruit dependent atelectatic lung, improve V/Q matching, reduce shunt fraction. PROSEVA mortality benefit in P/F <150 with prone ≥16 h/day.
- iNO 10–20 ppm: selective pulmonary vasodilation in ventilated alveoli → improves V/Q matching; rescue for refractory hypoxemia or RV strain. Not mortality-modifying in ARDS but functional bridge.
- Diuresis: if positive fluid balance, conservative fluid strategy improves oxygenation and lung-free days (FACTT trial). Net even-to-negative balance after initial resuscitation.

SPECIFIC NEXT ACTIONS:
1. **Reduce driving pressure NOW**: Vt is already 6 mL/kg PBW — confirm PBW is correctly calculated from height (males: 50 + 2.3 × (height_in − 60)). If PBW miscalculation has set Vt high, reduce. Reduce Vt to 5 mL/kg if needed to bring Pplat ≤30 and driving pressure ≤15; permissive hypercapnia targeting pH ≥7.20 acceptable (current 7.31 is acceptable). Recheck Pplat after change.
2. **Prone position for ≥16 h** within next 1–2 h. P/F 78 with severe ARDS — clear indication. Confirm contraindications absent (no unstable spine, abdominal compartment issues, unstable airway). Prepare team, secure lines and tube, document pre-prone metrics.
3. **Deep sedation + cisatracurium infusion** if patient–vent asynchrony or persistent hypoxemia after vent optimization — short course (24–48 h), particularly to facilitate proning and prevent dyssynchrony-related volutrauma.
4. **Bedside echo / POCUS** for RV function and septal motion (acute cor pulmonale assessment). If RV strain present: optimize ventilator to reduce PVR (avoid acidemia, avoid PEEP creep, target FiO2 to minimum needed), consider iNO 10–20 ppm. If hemodynamic instability persists: VV-ECMO referral conversation (P/F <80 on FiO2 ≥0.80 with optimized vent and prone × 24 h meets EOLIA-like criteria).

REASONS THE PATTERN IS NOT:
- *Pure airway obstruction*: Ppeak − Pplat = 4 (normal). Resistance not elevated.
- *Pure cardiogenic edema*: clinically COVID with bilateral diffuse infiltrates; absence of cardiac history; echo will help quantify LV function and assess PCWP estimate (E/e′). If significant LV dysfunction present, diuresis + afterload reduction in addition to ARDS-strategy.
- *Massive PE*: would expect normal or high compliance (not 21), and Vd/Vt elevated with wide PaCO2–PetCO2 gradient. Compliance 21 supports parenchymal disease (ARDS) as dominant mechanism.
```
