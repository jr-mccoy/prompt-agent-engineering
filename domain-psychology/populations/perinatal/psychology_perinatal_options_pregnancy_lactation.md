---
title: "Perinatal Treatment Options Across Pregnancy and Lactation"
category: psychology/populations/perinatal
description: "Organize psychotherapy and pharmacotherapy considerations for perinatal mood/anxiety across pregnancy and lactation using a shared risk-benefit frame, with named verification resources and no fabricated drug safety ratings."
techniques:
  - RT-02
  - RT-03
  - RT-04
  - DS-02
  - CM-01
difficulty: advanced
intended_use: model-testing
tags:
  - perinatal
  - pregnancy
  - lactation
  - breastfeeding
  - pharmacotherapy
  - psychotherapy
  - risk-benefit
  - shared-decision-making
  - LactMed
  - treatment-planning
updated: "2026-06-08"
related_prompts:
  - domain-psychology/populations/perinatal/psychology_perinatal_mood_anxiety_screen_interpretation.md
  - domain-psychology/populations/perinatal/psychology_postpartum_psychosis_referral.md
  - domain-psychology/treatment-planning/psychology_modality_selection_decision_aid.md
  - domain-psychology/documentation/psychology_initial_treatment_plan.md
---

# Perinatal Treatment Options Across Pregnancy and Lactation

## Objective

Produce a structured, balanced treatment-options analysis for a perinatal client with a mood or anxiety disorder that:

1. Organizes **psychotherapy** and **pharmacotherapy** options under a single explicit risk-benefit frame: the risk of treatment vs. the risk of **untreated maternal illness** (which is not zero — untreated perinatal depression/anxiety carries documented obstetric, fetal, and infant-attachment risks).
2. Separates the **pregnancy** decision context from the **lactation** decision context, since the exposure pathways, evidence bases, and reference resources differ.
3. References **named verification resources** for medication-in-pregnancy and medication-in-lactation data (e.g., LactMed, MotherToBaby, Reprotox) and routes every specific drug-safety question to clinician/prescriber verification — it does **not** assert drug-specific safety ratings.
4. Supports a **shared decision-making** conversation and documents the client's values and informed choice.
5. Flags when prescriber consultation, maternal-fetal medicine (MFM), or reproductive psychiatry referral is required.

This prompt is a decision-organizing aid for the treating clinician; it does not select or prescribe a medication.

## When to Use

- When a perinatal client with confirmed or probable depression/anxiety is weighing treatment options.
- When a client on an existing psychotropic becomes pregnant or is planning pregnancy and the continue/taper/switch question arises.
- When a postpartum client is deciding about pharmacotherapy in the context of breastfeeding.
- When preparing a shared decision-making conversation and the clinician needs the considerations organized.
- For supervision/training when the reasoning behind a perinatal treatment plan must be articulated.

## When NOT to Use

- To obtain a specific medication safety rating or dose — that is a prescriber decision verified against current references; this prompt routes there.
- For acute psychiatric emergencies (postpartum psychosis, acute suicidality, mania) — see `psychology_postpartum_psychosis_referral.md` and the risk-crisis prompts.
- For pure modality selection independent of the perinatal exposure question — use `psychology_modality_selection_decision_aid.md`.
- For non-perinatal adults.

## Inputs / Context Required

- **Perinatal stage:** planning pregnancy / trimester / postpartum; lactation status and feeding plan (exclusive breastfeeding, mixed, formula).
- **Diagnosis and severity:** primary diagnosis, severity anchors (EPDS/PHQ-9/GAD-7), functional impairment, suicidality status.
- **Treatment history:** prior medications (which worked, which failed, which caused adverse effects), prior psychotherapy, prior perinatal episodes.
- **Current medications:** all psychotropics and relevant non-psychotropics.
- **Client values and preferences:** stance on medication during pregnancy/lactation, feeding priorities, prior experience.
- **Care team:** OB/midwife, prescriber/psychiatrist, MFM, pediatrician — and whether reproductive psychiatry is accessible.
- `[clinician input required: prescriber identity and whether a medication question has been routed to them; current LactMed/MotherToBaby/Reprotox lookup status for any agent under consideration]`

## Constraints

### Must

- Frame every option against the **risk of untreated illness**, stated explicitly — never present treatment risk in isolation.
- Keep **pregnancy** and **lactation** as separate decision contexts with separate considerations and separate reference resources.
- For psychotherapy, identify evidence-based perinatal options (e.g., **IPT** and **CBT** have the strongest perinatal evidence; behavioral activation, mindfulness-based approaches, and couples/dyadic work as adjuncts) and note these carry no fetal/infant exposure risk.
- For pharmacotherapy, present considerations **categorically and procedurally** (continue vs. taper vs. switch; monotherapy preference; lowest effective dose; avoid abrupt discontinuation of an effective agent solely due to pregnancy) and route every **specific agent** question to the prescriber with a named verification resource.
- Name verification resources explicitly: **LactMed** (lactation), **MotherToBaby** and **Reprotox** (pregnancy/lactation exposure counseling), and the prescriber/reproductive psychiatry consult. Flag that FDA discontinued letter pregnancy categories (A/B/C/D/X) in favor of the **PLLR** narrative labeling — do not use letter categories.
- Document the shared decision-making process and the client's informed choice.
- Flag all `[clinician input required: ...]` gaps.

### Must Not

- Do not assert a specific drug is "safe" or "unsafe" in pregnancy or lactation, and do not assign any drug a numeric or letter safety rating. Route to named resources + prescriber.
- Do not recommend abruptly stopping an effective psychotropic solely because of pregnancy without prescriber involvement — discontinuation has its own relapse risk.
- Do not present medication as the only path, nor psychotherapy as universally sufficient for severe illness.
- Do not fabricate study findings, relative-infant-dose figures, or milk/plasma ratios.
- Do not omit the untreated-illness risk side of the ledger.

## Risk-Benefit Frame (the four-quadrant ledger)

| | Pregnancy context | Lactation context |
|---|---|---|
| **Risk of treating** | Fetal exposure considerations (agent-specific — route to MotherToBaby/Reprotox + prescriber); requires lowest effective dose, monotherapy preference | Infant exposure via milk (agent-specific — route to **LactMed** + prescriber); relative infant dose, sedation/feeding monitoring |
| **Risk of NOT treating** | Untreated depression/anxiety: poorer prenatal care/nutrition, obstetric and birth-outcome risks, escalating severity, suicide risk | Untreated illness: impaired bonding/attachment, feeding/caregiving capacity, maternal suicide risk, chronicity |

**Anchor:** the decision is never "exposure vs. no exposure" — it is "exposure to a treated illness pathway vs. exposure to an untreated illness pathway." Both have consequences.

## Instructions

1. **Establish the decision context.** Confirm pregnancy vs. lactation (or both, for planning), severity, suicidality, and treatment history. If acute risk or psychotic features are present, exit to the emergency/psychosis pathway.

2. **Severity-stratify.** Mild–moderate without safety concerns → psychotherapy-first is reasonable. Moderate–severe, functionally impairing, prior medication-responsive, or with safety concerns → combined treatment and prescriber involvement are typically indicated. State the stratification.

3. **Lay out psychotherapy options.** Identify perinatal-evidence-based modalities (IPT, CBT first-line; adjuncts). Note zero fetal/infant exposure risk. Address access, frequency, and dyadic/partner components.

4. **Lay out pharmacotherapy considerations — categorically.** Address the continue/taper/switch decision for clients already on medication; monotherapy and lowest-effective-dose principles; the relapse risk of discontinuation. For **any specific agent**, insert a routing block: "Verify against [LactMed / MotherToBaby / Reprotox] and confirm with prescriber — do not state a safety rating here."

5. **Apply the pregnancy context** separately: trimester-specific timing considerations are a prescriber/MFM matter; flag late-pregnancy and neonatal-adaptation monitoring as prescriber-coordinated.

6. **Apply the lactation context** separately: route milk-transfer/relative-infant-dose questions to **LactMed** + prescriber; specify infant monitoring (sedation, feeding, weight) as a pediatric-coordinated item.

7. **Run the risk-benefit ledger** (four quadrants) explicitly, including the untreated-illness side.

8. **Structure the shared decision-making conversation** and document the client's values and informed choice.

9. **Identify referrals/consults** required (prescriber, reproductive psychiatry, MFM, pediatrics, lactation).

10. Run verification.

## Output Format

```
=== PERINATAL TREATMENT OPTIONS — RISK-BENEFIT ORGANIZER ===

Client: [Initials/MRN]    Date: [YYYY-MM-DD]    Clinician: [Name, credentials]
Decision context: [Planning / Pregnancy — trimester ___ / Postpartum — lactating: Y/N — feeding plan: ___]
Diagnosis + severity: [Dx; EPDS/PHQ-9/GAD-7 anchors; functional impairment]
Suicidality: [None / Present — routed per risk protocol]
Current psychotropics: [List / None]    Prior med response: [...]

─────────────────────────────────────────
SEVERITY STRATIFICATION
─────────────────────────────────────────
Stratum: [Mild–moderate, no safety concern → psychotherapy-first reasonable
        | Moderate–severe / impairing / prior med-responsive / safety concern → combined + prescriber]
Rationale: [...]

─────────────────────────────────────────
PSYCHOTHERAPY OPTIONS (no fetal/infant exposure)
─────────────────────────────────────────
First-line (perinatal evidence): [IPT / CBT — match to presentation]
Adjuncts: [Behavioral activation / mindfulness-based / dyadic / partner-inclusive]
Access / frequency / format: [...]
Expected role: [Monotherapy for milder presentations / component of combined care]

─────────────────────────────────────────
PHARMACOTHERAPY CONSIDERATIONS (categorical — NOT agent ratings)
─────────────────────────────────────────
Continue / taper / switch decision (if already on medication):
  [Framing only — abrupt discontinuation of an effective agent carries relapse risk; route to prescriber]
Principles: [Lowest effective dose | monotherapy preference | avoid polypharmacy where possible]
SPECIFIC AGENT QUESTIONS → ROUTING:
  Agent(s) under consideration: [name(s)]
  → Verify pregnancy exposure data: [MotherToBaby / Reprotox] + prescriber/reproductive psychiatry
  → Verify lactation data: [LactMed] + prescriber + pediatrics
  → Labeling note: use PLLR narrative labeling; FDA A/B/C/D/X letter categories are discontinued — do not use
  [clinician input required: lookup status + prescriber confirmation for each agent]

─────────────────────────────────────────
PREGNANCY CONTEXT
─────────────────────────────────────────
Timing considerations: [Trimester-specific — prescriber/MFM coordinated]
Late-pregnancy / neonatal-adaptation monitoring: [Prescriber + OB coordinated — describe plan]
MFM referral indicated: [Yes/No — rationale]

─────────────────────────────────────────
LACTATION CONTEXT
─────────────────────────────────────────
Milk-transfer / relative-infant-dose questions: → LactMed + prescriber (do not state figures here)
Infant monitoring plan: [Sedation / feeding / weight — pediatrics coordinated]
Feeding-plan alignment with maternal treatment: [...]

─────────────────────────────────────────
RISK-BENEFIT LEDGER
─────────────────────────────────────────
Risk of treating (pregnancy): [...]      Risk of treating (lactation): [...]
Risk of NOT treating (pregnancy): [...]  Risk of NOT treating (lactation): [...]
Net clinical framing: [Treated-illness pathway vs. untreated-illness pathway — summary]

─────────────────────────────────────────
SHARED DECISION-MAKING + INFORMED CHOICE
─────────────────────────────────────────
Client values / priorities: [...]
Options presented and understood: [Yes — summarize]
Client's informed choice: [...]
[clinician input required: documentation of risks/benefits/alternatives discussed]

─────────────────────────────────────────
REFERRALS / CONSULTS
─────────────────────────────────────────
[ ] Prescriber / psychiatry   [ ] Reproductive psychiatry   [ ] MFM
[ ] Pediatrics   [ ] Lactation consultant   [ ] OB/midwife notified

─────────────────────────────────────────
RISK-REASSESSMENT HOOK
─────────────────────────────────────────
Re-assess if: worsening symptoms/scores, emergent suicidality, medication adverse effect,
rapid-onset confusion/mood lability/unusual beliefs (→ postpartum psychosis screen).
[clinician input required: client-specific tripwires + follow-up interval]

─────────────────────────────────────────
BILLING
─────────────────────────────────────────
Service rendered: [Psychotherapy 90832/90834/90837 | E/M | care coordination as applicable]
[clinician input required]
```

## Verification

- [ ] Every option framed against the explicit risk of UNTREATED illness, not in isolation.
- [ ] Pregnancy and lactation kept as separate decision contexts with separate considerations.
- [ ] Psychotherapy options identified as evidence-based (IPT/CBT first-line) and noted as zero exposure.
- [ ] Pharmacotherapy presented categorically (continue/taper/switch, lowest dose, monotherapy); no specific agent given a safety rating.
- [ ] Every specific-agent question routed to named resources (LactMed for lactation; MotherToBaby/Reprotox for pregnancy) + prescriber.
- [ ] PLLR narrative labeling noted; FDA letter categories explicitly not used.
- [ ] Severity stratification stated and drives the recommendation.
- [ ] Risk-benefit four-quadrant ledger completed including untreated-illness quadrants.
- [ ] Shared decision-making and client informed choice documented.
- [ ] Required referrals/consults identified (prescriber, repro psych, MFM, pediatrics, lactation).
- [ ] Risk-reassessment hook present, including postpartum-psychosis tripwires.
- [ ] No fabricated study findings, relative-infant-dose figures, or milk/plasma ratios.
- [ ] All gaps flagged with `[clinician input required: ...]`.
