---
title: "Lay Summary Translator"
category: science/writing-communication
description: "Translates a user-supplied finding into a plain-language summary for a stated non-specialist audience at a calibrated reading level, preserving uncertainty, scope, and the association-versus-causation distinction without overclaiming."
techniques:
  - ST-01
  - ST-03
  - QA-01
  - QA-02
  - CM-02
difficulty: advanced
tags:
  - lay-summary
  - plain-language
  - science-communication
  - audience-calibration
  - uncertainty-preservation
  - association-vs-causation
  - no-overclaiming
  - open-science
updated: "2026-06-26"
related_prompts:
  - domain-science/writing-communication/science_abstract_compressor.md
  - domain-science/writing-communication/science_imrad_paper_drafter.md
  - domain-science/writing-communication/science_figure_first_paper_skeleton.md
---

# Lay Summary Translator

**Objective:** Translate a user-supplied scientific finding into a plain-language summary for a specific stated non-specialist audience (e.g., patients, policymakers, funders, general public) at a calibrated reading level. The translation preserves the result's uncertainty, scope (who/what it applies to), and the difference between association and causation — and never implies a clinical or practical action the evidence does not support.

**When to use:** After a finding is settled and you need a non-specialist version — a plain-language abstract, patient summary, press-ready paragraph, funder report, or policy brief — that does not distort or overclaim.

**Required inputs:**
- **Discipline.** Field and subfield (sets which caveats and scope limits matter most).
- **Manuscript / finding context.** The actual finding, including effect direction/size, study design, and stated limitations — user-supplied; never invented.
- **Target venue or audience.** The specific non-specialist audience and, if known, the reading level, length limit, and venue (journal plain-language summary, patient handout, policy brief, press release).
- **Causal status.** Whether the design supports a causal claim or only an association/correlation.

**Optional inputs:**
- The population/setting the finding applies to (and explicitly where it does not).
- Required reading-grade target (e.g., grade 6–8 for general public).
- Known misinterpretations to pre-empt.
- Data/code availability, preprint status, and any conflict-of-interest disclosure the audience should see.

**Constraints — Must:**
- Name the exact audience and calibrate vocabulary and sentence length to the stated reading level.
- Preserve uncertainty: state what is and is not known, and the strength of the evidence.
- State the scope explicitly — who and what the finding applies to, and where it does not generalize.
- Keep association-vs-causation faithful: use associative language unless the design supports causation.
- Replace jargon with faithful plain-language equivalents (not simplified into something false).
- Include a "What this does NOT mean" guardrail block.
- Surface preprint/data availability where appropriate (Open Science default).

**Constraints — Must Not:**
- Do not invent results, numbers, citations, DOIs, author claims, or journal requirements. Draft only from user-supplied content; mark gaps `[user-supplied]` and ask.
- Do not imply a clinical, behavioral, or policy action the evidence does not support.
- Do not convert an association into a causal claim, or a single study into a settled fact.
- Do not use metaphors that induce false precision or imply a mechanism not shown.
- Do not use "novel," "groundbreaking," "first-ever," "gold standard," or "unprecedented" in drafted text.
- Do not drop the limitations or scope to make the summary cleaner or more exciting.

**Instructions:**

1. **Pin the audience and level.** Restate the exact audience, reading-grade target, length limit, and venue. Note what this audience will most likely misread.
2. **Extract the faithful core.** From user-supplied content, capture the finding, its effect direction/size, the design, the causal status, and the stated limitations. Tag missing items `[user-supplied]`.
3. **Set the causal frame.** Decide associative vs. causal language strictly from the design; lock the verb choice (e.g., "is linked to" vs. "causes") before drafting.
4. **Build a jargon map.** Replace each technical term with a faithful plain equivalent; reject any substitution that changes the meaning. Avoid metaphors that imply false precision.
5. **Draft the summary.** Lead with what was found and who/what it applies to, in calibrated language at the target level, keeping uncertainty and scope intact.
6. **Write the "What this does NOT mean" block.** List the most likely overinterpretations (causal leap, over-generalization, premature action) and correct each plainly.
7. **Add scope and Open Science line.** State the population/setting and limits; add preprint/data-availability and any disclosure the audience should see.
8. **Stress-test for overclaiming.** Read each sentence as a skeptical non-expert: does it promise more than the evidence? Does it imply an action? Fix any drift; report the reading level reached.

**Output format (locked):**

```
## Audience & Calibration
[audience; reading-grade target; length limit; venue; likely misreadings]

## Faithful Core (from user-supplied finding)
- Finding + effect direction/size: [user-supplied if missing]
- Design + causal status (association vs. causation)
- Stated limitations

## Plain-Language Summary  (target level: grade N; length: M)
[the calibrated summary]

## What This Does NOT Mean
- [overinterpretation] → [plain correction]
- [over-generalization] → [scope correction]
- [implied action] → [evidence-based limit]

## Scope
[who/what it applies to; where it does not generalize]

## Open Science / Disclosure
- Preprint / data availability / conflicts: [as appropriate]

## Checks
- Causal language matches design: yes/no
- Uncertainty and scope preserved: yes/no
- Reading level reached: [grade N]
- Outstanding [user-supplied] gaps: [...]
```

**Reporting-standard / convention alignment:** Plain-language summary conventions (e.g., journal plain-language abstracts, PCORI/patient-facing communication standards, plain-writing readability guidance such as a grade 6–8 target for general audiences); the EQUATOR reporting guideline for the study type informs which limitations and scope statements must survive translation.

**Verification checklist (before delivering):**
- [ ] The exact audience and reading-grade target are named and the draft meets them.
- [ ] Association-vs-causation language matches the study design.
- [ ] Uncertainty and the strength of evidence are preserved, not smoothed away.
- [ ] Scope (who/what it applies to and where it does not) is stated explicitly.
- [ ] A "What this does NOT mean" block addresses the likely overinterpretations.
- [ ] Jargon replacements are faithful, not simplified into falsehood.
- [ ] No metaphor implies false precision or an unshown mechanism.
- [ ] No implied clinical/behavioral/policy action beyond the evidence; no banned promotional words.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Causal leap | A clear sentence saying the intervention "improves" outcomes from observational data | Lock associative verbs in step 3 from the design |
| Over-generalization | A summary implying the finding applies to everyone | Mandatory explicit scope + "does NOT mean" block |
| Implied action | "Patients should..." derived from a single study | Forbid action language not supported by the evidence |
| False-precision metaphor | A vivid analogy that suggests an exact mechanism | Reject metaphors that add precision the data lacks |
| Dumbed-down-to-wrong | Jargon replaced by a simpler but inaccurate term | Jargon map requires meaning-preserving substitutions |
