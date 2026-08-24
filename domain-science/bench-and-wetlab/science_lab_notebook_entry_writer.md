---
title: "Lab Notebook Entry Writer"
category: science/bench-and-wetlab
description: "Compose an ELN-compatible, ALCOA+-compliant notebook entry recording only user-supplied facts: hypothesis, materials, as-performed method with deviations, observations, calibrated interpretation, conclusion, and next step."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - QA-01
  - RT-01
difficulty: advanced
tags:
  - lab-notebook
  - eln
  - alcoa-plus
  - data-integrity
  - documentation
  - deviation-logging
  - observation-vs-inference
  - reproducibility
updated: "2026-06-26"
related_prompts:
  - domain-science/bench-and-wetlab/science_sample_logging_chain_of_custody_designer.md
  - domain-science/bench-and-wetlab/science_failed_experiment_post_mortem.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
---

# Lab Notebook Entry Writer

**Objective:** Produce a structured, ELN-compatible laboratory notebook entry that records **only what the user supplies**, organized for reproducibility and audit: date/operator/project header, hypothesis/objective, materials with lots, the method as actually performed (including deviations from the planned protocol), observations and raw-data pointers, a calibrated interpretation that separates observation from inference, a conclusion, and a concrete next step. The entry must comply with ALCOA+ and good documentation practice; it must never invent observations, numbers, or results.

**When to use:** At the bench while or immediately after performing an experiment (contemporaneous documentation), or when converting rough as-run notes into a clean, auditable ELN entry.

**Required inputs:**
- **Discipline.** [user-supplied]
- **Study type.** [user-supplied] (pre-specified/confirmatory or exploratory)
- **Hypothesis or objective** for this run.
- **Materials used** (reagents, samples, instruments) — including lots, marked `[user-supplied]` where unknown.
- **What was actually done** (the as-performed method, including any deviation from the planned protocol).
- **Observations / raw data location** — recorded verbatim from the user; never inferred.

**Optional inputs:**
- Reference to the planned protocol/SOP and its version.
- Linked sample IDs (from the chain-of-custody register) and downstream data files.
- Operator co-signers / witnessing requirement.
- Instrument settings, environmental conditions.

**Constraints — Must:**
- Enforce **ALCOA+**: Attributable (named operator), Legible, **Contemporaneous** (real timestamp, no back-dating), Original (raw-data pointers, not transcriptions presented as raw), Accurate, plus Complete/Consistent/Enduring/Available.
- Log **deviations from the planned protocol** explicitly as deviations, not as the plan.
- Separate **observation from inference**: the observations section states what was seen; interpretation is clearly labeled and calibrated.
- Use **calibrated language** in interpretation; flag uncertainty rather than overstate.
- Use stable identifiers to link sample IDs, protocol version, and data files where supplied.
- Default to an **Open Science** disposition (link the deposited protocol and note where the entry/data can be shared) when permissible.

**Constraints — Must Not:**
- Do not invent vendor names, catalog/lot numbers, reagent specs, or results/observations. If needed and not supplied, mark `[user-supplied]` and ask; the prompt records what the user supplies, it never fabricates data.
- Do not fabricate any observation, measurement, count, image, or result — leave `[user-supplied]` placeholders for every datum not provided.
- Do not back-date, overwrite, or present a corrected value without preserving the original (ALCOA+ Original).
- Do not present an inference as an observation.
- Do not use promotional language ("novel", "groundbreaking", "first-ever", "gold standard") in drafted text.

**Instructions:**

1. **Build the header.** Record date, operator (attributable), project, and contemporaneous timestamp. If the timestamp is not the true time of work, flag it — do not back-date silently.
2. **State the hypothesis/objective.** One or two lines; note pre-specified vs exploratory.
3. **List materials.** Enumerate reagents, samples, and instruments with lots and IDs; mark every unknown lot/spec as `[user-supplied]`.
4. **Record the method as performed (RT-01).** Write the actual steps in order; where they diverged from the planned protocol, label the divergence as a **deviation** with reason.
5. **Record observations only.** Transcribe what the user reports seeing, with raw-data pointers (file paths, instrument export IDs). Insert `[user-supplied]` for any datum not provided — never fill a number.
6. **Interpret, calibrated.** In a separate, clearly labeled section, give the inference, distinguishing it from the observations and stating confidence/uncertainty.
7. **Conclude and set next step.** State the conclusion the data supports (or that it is inconclusive) and the single concrete next action.
8. **Self-check (QA-01).** Confirm no fabricated data, deviations logged, observation/inference separated, links present.
9. **Open Science note.** Record the linked protocol deposit and data-sharing disposition where permissible.

**Output format (locked):**

```
## Header
- Date / timestamp:
- Operator (attributable):
- Project:
- Protocol/SOP & version:
- Linked sample IDs / data files:

## Hypothesis / Objective
- (pre-specified | exploratory):

## Materials
| Item | ID / lot | Spec | Source |
|---|---|---|---|

## Method (as performed)
1.
Deviations from planned protocol:
-

## Observations (facts only — [user-supplied] where not provided)
- Raw-data pointer(s):
-

## Interpretation (inference — calibrated)
-

## Conclusion
-

## Next Step
-

## Open Science Disposition
- Protocol deposit link / data-sharing status:
```

**Reporting-standard alignment:** ALCOA+ data-integrity principles; good documentation / ELN best practice; STAR Methods (materials/key-resources structure); ARRIVE 2.0 where in-vivo work is recorded.

**Verification checklist (before delivering):**
- [ ] Operator and a contemporaneous (not back-dated) timestamp are present.
- [ ] Every datum is either user-supplied or marked `[user-supplied]`; nothing invented.
- [ ] Method reflects what was actually done; deviations are labeled as deviations.
- [ ] Observations and interpretation are in separate, clearly labeled sections.
- [ ] Interpretation language is calibrated; uncertainty is flagged.
- [ ] Sample IDs, protocol version, and data files are linked where supplied.
- [ ] No fabricated vendors/lots/specs; banned promotional terms absent.
- [ ] Open Science disposition recorded where permissible.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Fabricated data | A plausible-looking number fills a blank | Hard rule: `[user-supplied]` placeholder; never generate observations |
| Observation/inference blur | "Bands confirm knockdown" stated as observation | Force separate Observations vs Interpretation sections |
| Silent deviation | As-run method written as the planned protocol | Require explicit deviation log with reason |
| Back-dating | Entry timestamped to the work day after the fact | Contemporaneous timestamp; flag any non-real time |
| Overwritten original | A corrected value replaces the raw reading | Preserve original (ALCOA+ Original); record corrections additively |
