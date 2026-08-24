# `domain-science/grants-funding/`

The funding-and-grants layer for the working scientist: drafting Specific Aims, full-proposal outlines for the major funders, the individual review-criterion sections, resubmission responses, budget justifications, and letters of support. Aligned to NIH, NSF, and ERC review criteria.

**Stance:** these prompts draft *from the user's own science, data, and commitments* — they never invent preliminary data, impact statistics, collaborators, effort percentages, costs, or funder-specific rules. Funder policy and figures are `[user-supplied]` / verify against the current FOA or solicitation. Innovation is substantiated with specific deltas vs the state of the art, not hype.

## Map (Phase 2G — 10 prompts)

### Whole-proposal scaffolds

| File | Coverage |
|---|---|
| [`science_specific_aims_drafter.md`](science_specific_aims_drafter.md) | The one-page NIH Specific Aims arc; flags aim-interdependence risk |
| [`science_nih_r01_outline_drafter.md`](science_nih_r01_outline_drafter.md) | Research Strategy outline: Significance / Innovation / Approach + Rigor & Reproducibility, authentication |
| [`science_nsf_proposal_outliner.md`](science_nsf_proposal_outliner.md) | Intellectual Merit + Broader Impacts woven throughout; five merit-review elements |
| [`science_erc_grant_outliner.md`](science_erc_grant_outliner.md) | Starting/Consolidator/Advanced; ground-breaking ambition + PI identity; risk-vs-feasibility balance |

### Individual review-criterion sections

| File | Coverage |
|---|---|
| [`science_grant_significance_section_drafter.md`](science_grant_significance_section_drafter.md) | Gap framing + impact rationale; quantitative claims traced to a user source |
| [`science_grant_innovation_section_drafter.md`](science_grant_innovation_section_drafter.md) | Specific delta claims vs the state of the art; substantiation check (departs-from → benefit → evidence) |
| [`science_grant_approach_section_drafter.md`](science_grant_approach_section_drafter.md) | Per-aim design, rigor (power/controls/authentication), pitfalls + alternatives, milestones + go/no-go |

### Submission support

| File | Coverage |
|---|---|
| [`science_grant_resubmission_response.md`](science_grant_resubmission_response.md) | Responsive (not combative) Introduction-to-the-Application; each concern → response → location-of-change |
| [`science_grant_budget_justification_drafter.md`](science_grant_budget_justification_drafter.md) | Category-by-category justification tied to the aims; internal-consistency + red-flag check |
| [`science_letter_of_support_drafter.md`](science_letter_of_support_drafter.md) | Specific named commitments (resources/access/time), not boilerplate praise; signatory must approve |

## Floor (per [`../README.md`](../README.md))

Every prompt requires discipline + study type + funding mechanism; forbids fabricated citations, preliminary data, impact statistics, personnel, effort/costs, institutional commitments, or funder-specific rules (`[user-supplied]` / verify against the FOA); locks the output format; names the funder's review criteria explicitly (NIH Significance/Investigator/Innovation/Approach/Environment + Rigor & Reproducibility; NSF Intellectual Merit + Broader Impacts; ERC Excellence); surfaces rigor/pre-specification and cross-references the power, confound, and reproducibility prompts; keeps language calibrated (no empty innovation filler); defaults to the Open Science branch (DMP, authentication, sharing); and ends with a verification checklist + false-positive matrix.

See [`../EXPANSION_ROADMAP.md`](../EXPANSION_ROADMAP.md) for the remaining phases and build order.
