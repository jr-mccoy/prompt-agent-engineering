---
title: "Grant Innovation Section Drafter"
category: science/grants-funding
description: "Draft a grant Innovation section as a set of specific, checkable delta claims against the state of the art — each naming what it departs from, why the departure matters, and the evidence it is feasible."
techniques:
  - ST-01
  - ST-03
  - RT-03
  - QA-01
  - CM-02
difficulty: advanced
tags:
  - grant-writing
  - innovation
  - state-of-the-art
  - nih
  - nsf
  - delta-claims
  - peer-review
  - substantiation
updated: "2026-06-26"
related_prompts:
  - domain-science/grants-funding/science_specific_aims_drafter.md
  - domain-science/grants-funding/science_grant_significance_section_drafter.md
  - domain-science/grants-funding/science_grant_approach_section_drafter.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
---

# Grant Innovation Section Drafter

**Objective:** Draft the Innovation section so it reads as a set of specific delta claims against the current state of the art: what the proposal does differently (in concept, method, tool, model, or application), why that departure matters, and the evidence that it is feasible. The draft must distinguish genuine innovation from mere newness, and forbid empty filler. Each innovation claim names what it departs FROM and the concrete benefit.

**When to use:** After Significance establishes importance, when you need an Innovation narrative that survives a reviewer asking "innovative compared to what, exactly?"

**Required inputs:**
- **Discipline.** The scientific field.
- **Study type.** Observational / experimental / computational / mixed.
- **Funder and mechanism.** e.g., NIH R01, NSF, ERC — Innovation expectations differ by mechanism.
- **State of the art.** How the problem is currently addressed (standard methods, prevailing models, existing tools) — supplied by the user with references.
- **Proposed departures.** What the proposal will do differently.

**Optional inputs:**
- Preliminary data demonstrating feasibility of a departure (with source).
- Competing or adjacent approaches the reviewers will know.
- Significance and Aims text (to ensure innovation is in service of the problem, not novelty for its own sake).

**Constraints — Must:**
- Map to the funder's innovation expectation (NIH "Innovation" criterion; NSF transformative/creative potential under Intellectual Merit; ERC ground-breaking nature). Name it explicitly.
- Express each innovation as a delta: state the current practice it departs from, the specific change, the benefit, and the feasibility evidence.
- Distinguish conceptual, methodological, technical, and application innovation, and label which type each claim is.
- Tie each innovation to the problem/gap so it advances the aims rather than decorating them.

**Constraints — Must Not:**
- Do not invent citations, DOIs, preliminary data, impact statistics, or funder-specific rules. If needed and not supplied, mark `[user-supplied]` and ask; quantitative impact claims must trace to a user-supplied source.
- Do not use "novel," "first-ever," "groundbreaking," "unprecedented," or "gold standard" as standalone descriptors in the drafted text — each innovation must name what it departs from and the benefit.
- Do not present mere newness (untested for its own sake) as innovation; require a benefit argument.
- Do not claim a departure is feasible without naming the evidence (preliminary data, established precedent, or a reasoned argument flagged as such).

**Instructions:**

1. **Confirm scope.** Restate discipline, study type, funder/mechanism, and the named innovation criterion. If unknown, mark `[user-supplied]` and ask.
2. **Inventory the state of the art.** From user input, list how the problem is currently solved and the limits of those approaches. If the state of the art is not supplied, flag `[user-supplied]` — do not assume it.
3. **Extract candidate departures.** For each proposed change, draft a delta: departs-from → specific change → benefit → type (conceptual/methodological/technical/application).
4. **Test newness vs innovation.** For each candidate, ask whether the change yields a benefit the field cannot currently get. Drop or downgrade claims that are merely new.
5. **Attach feasibility evidence.** For each surviving claim, name the evidence it can work (preliminary data `[user-supplied]`, established precedent, or a reasoned-but-unproven argument explicitly labeled).
6. **Draft the prose.** Write the section so each innovation appears as a substantiated delta, ordered by strength, in service of the aims.
7. **Build the substantiation check table.** Tabulate claim → departs-from → benefit → evidence, exposing any claim missing a column.
8. **Calibrate and finalize.** Remove empty superlatives; ensure every claim is checkable; confirm coherence with Significance and Aims.

**Output format (locked):**

```
## Innovation (drafted)
[Innovation claim 1 as a delta vs the state of the art — type labeled]
[Innovation claim 2 ...]
[Innovation claim 3 ...]
[How these departures advance the aims]

## Substantiation Check
| Claim | Departs from (state of the art) | Benefit | Evidence of feasibility |
|---|---|---|---|
| [claim 1] | [current practice] | [concrete benefit] | [prelim data [user-supplied] / precedent / labeled argument] |
| [claim 2] | ... | ... | ... |

## Calibration Notes
- Claims downgraded from "innovation" to "newness": [list]
- Superlatives removed: [list]
- Claims missing evidence: [list]
```

**Reporting-standard alignment:** NIH review criterion Innovation; NSF transformative/creative potential (Intellectual Merit); ERC ground-breaking nature. The drafted claims must be departures a reviewer can verify against the cited state of the art.

**Verification checklist (before delivering):**
- [ ] Discipline, study type, and funder/mechanism confirmed; innovation criterion named.
- [ ] State of the art is user-supplied and referenced, not assumed.
- [ ] Each innovation is expressed as a delta with departs-from, change, benefit, and type.
- [ ] Mere-newness claims are downgraded or dropped.
- [ ] Each claim names feasibility evidence; unproven arguments are labeled as such.
- [ ] No fabricated citations, preliminary data, or funder rules.
- [ ] No standalone "novel/first-ever/groundbreaking/gold standard" in the drafted text.
- [ ] Substantiation check table has no empty cells; gaps are flagged.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Newness as innovation | "We are the first to use X" with no benefit | Require a benefit the field cannot currently obtain; else downgrade |
| Unanchored delta | "Innovative approach" with no baseline named | Force a departs-from column citing the state of the art |
| Assumed state of the art | Confidently describing current practice from memory | Require user-supplied, referenced baseline; else flag `[user-supplied]` |
| Feasibility hand-wave | "This will work" with no basis | Require named evidence or an explicitly labeled reasoned argument |
| Superlative inflation | "Groundbreaking/unprecedented" reads strong | Ban empty descriptors; replace with checkable deltas |
