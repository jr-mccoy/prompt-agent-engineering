---
title: "Design System Audit — Component Inventory, Duplication Clusters, Token Coverage, and Measured Adoption"
category: frontend-development/design-direction
description: "Audit an existing design system as a product that teams either adopt or route around: inventory library and product-local components, cluster duplicates and separate gap-driven duplication from neglect, measure token coverage per property, compute adoption and version currency per consuming team with stated formulas, and return a prioritised, confidence-rated plan."
techniques:
  - RT-02
  - AG-12
  - QA-24
  - DS-06
difficulty: intermediate
tags:
  - design-system
  - component-inventory
  - design-tokens
  - adoption-metrics
  - ui-consistency
  - component-library
  - teams-not-using-our-components
  - too-many-button-styles
  - is-our-design-system-working
updated: "2026-10-03"
related_prompts:
  - domain-frontend-development/design-direction/frontend_design_token_architecture.md
  - domain-frontend-development/design-direction/frontend_design_system_component_governance.md
  - domain-frontend-development/styling/frontend_styling_tailwind_design_system.md
---

# Design System Audit

**Objective:** Establish, with numbers, whether a design system is doing its job — which
components exist, where product teams have rebuilt them and why, how much styling flows
through tokens, and how adoption and version currency differ by team — and turn that into
a short, prioritised plan whose every finding carries its evidence and a confidence level.

**When to Use:**
- A component library has existed for a year or more and leadership asks whether it is
  paying off, or whether to fund it further.
- Product UIs have drifted: several modals, several button styles, near-identical greys.
- You are about to plan a major version and need to know what teams actually use.
- A team is suspected of "going its own way" and you need evidence rather than anecdote.
- **Not this prompt if** you are reviewing a **Tailwind configuration** as the token source
  — use `domain-frontend-development/styling/frontend_styling_tailwind_design_system.md`; if
  the problem is specificity, cascade layers, or CSS methodology, use
  `domain-frontend-development/styling/frontend_styling_css_architecture.md`; for a native
  Android app's visual consistency, use
  `domain-software-engineering/mobile/android/analysis/android_compose_ui_consistency_audit.md`.
  This prompt audits the **system and its adoption across teams**, independent of styling
  technology. Designing the token tiers themselves is
  `frontend_design_token_architecture.md`; contribution and versioning rules are
  `frontend_design_system_component_governance.md`.

## Inputs / Context

1. **Library manifest**: component list, current version, package name(s), docs site.
2. **Consuming codebases**: repo list with owning team, and the design-system version each
   pins (lockfiles are the source of truth, not team recollection).
3. **Code-search access or exports**: import counts of library components, and local
   component definitions whose names or markup resemble library components.
4. **Style declarations**: counts by property (colour, spacing, radius, font-size, shadow,
   z-index), split into token references vs raw values.
5. **Token list** with resolved values, so raw values can be matched to nearest tokens.
6. **Design-side signals** if available: design-tool library usage or detach analytics,
   open issues/requests against the library and their age.
7. **What the system is for**: the outcomes it was funded to deliver (consistency, speed,
   accessibility baseline), so findings are judged against purpose, not aesthetics.

## Method

1. **Inventory both sides (RT-02).** List library components; then list product-local
   components that perform the same job. Classify each local one: *wrapper* (composes a
   library component — counts as adoption), *duplicate* (re-implements an existing library
   component), *gap* (no library equivalent exists), or *legitimate one-off*. Exclude tests,
   stories, and generated code.
2. **Cluster duplicates and ask why.** Group duplicates by job (all modals, all date
   pickers). For each cluster record count, teams, and the stated or inferable cause:
   missing variant, missing capability, performance, unawareness, or preference. A cluster
   caused by a library gap is a library backlog item, not a team compliance problem.
3. **Measure token coverage per property.** `coverage = tokenised declarations ÷ all
   declarations of that property`. For raw values, match to the nearest token (colour by
   ΔE2000, spacing by grid step) and classify: *snap candidate* (within threshold — safe to
   codemod), *missing token family* (e.g. data-visualisation palettes), *genuine outlier*.
4. **Compute adoption with stated formulas (AG-12).**
   - `component adoption = library instances ÷ (library instances + duplicate instances)`;
     gap components are excluded from the denominator.
   - `version currency = consuming repos on current major ÷ all consuming repos`.
   - Report per team and overall; never only overall — averages hide the team that matters.
5. **Record what you checked and cleared (QA-24).** For every suspected duplication or
   drift you dismissed, give the reason (it is a wrapper, the library lacks the capability,
   it is a sanctioned one-off) so "found nothing" is distinguishable from "did not look".
6. **Prioritise (DS-06).** Rank by reach (instances × teams) × cost of the inconsistency
   (accessibility defects, bug duplication, brand drift) ÷ effort. Gap-driven clusters
   usually rank first: one library addition retires many local copies.
7. **Rate confidence.** High = measured from code; Medium = sampled or inferred from
   names; Low = from interviews or design-tool data alone.

## Output Format

```
# Design system audit — [system name] v[x]   Date: [..]   Scope: [repos/teams]

## Purpose the system is judged against
## Inventory
| Library components | Local equivalents | Wrappers | Duplicates | Gaps | One-offs |
## Duplication clusters
| Job | Local copies | Teams | Cause (gap / variant / perf / unaware / preference) | Confidence |
## Token coverage
| Property | Declarations | Tokenised | Coverage | Snap candidates | Missing families | Outliers |
## Adoption and currency
| Team | Library inst. | Duplicate inst. | Adoption | DS version | Current major? |
Overall adoption: [..]   Version currency: [..]
## Checked and cleared
| Candidate | Why dismissed | Evidence |
## Prioritised plan
| # | Action | Reach | Cost of inconsistency | Effort | Confidence |
## Metrics to re-measure next quarter (with targets)
```

## Verification

- [ ] Every number states its formula and its source (lockfile, code search, export).
- [ ] Wrappers are counted as adoption; gap components are excluded from the denominator.
- [ ] Adoption is shown per team as well as overall.
- [ ] Each duplication cluster has a cause, and gap-caused clusters become library work.
- [ ] Raw values are classified (snap / missing family / outlier), not just counted.
- [ ] A checked-and-cleared table exists.
- [ ] Every finding carries a confidence level.

## False-Positive Prevention

1. **Wrappers counted as duplicates.** `BillingButton` that renders the library `Button`
   with a preset is adoption. Read the implementation before counting.
2. **Gaps counted as defiance.** Six local data tables when the library has none is a
   missing component, not six non-compliant teams.
3. **Name-matching as evidence.** A local `Card` may be a domain object, not a UI card.
   Name matches are Medium confidence until the markup is checked.
4. **Raw values that are correct.** Data-visualisation palettes, third-party embeds, and
   brand-mandated assets may need their own token family rather than a snap.
5. **Instance counts as usage.** A component imported in 400 files of a dead admin area
   inflates adoption. Weight by routes in use where traffic data exists.
6. **Design-tool data as code truth.** Detach rates describe designers' files, not shipped
   UI. Keep the two adoption views separate.
7. **One average for the whole org.** 76% overall can hide one team at 52%.

## Example Output

```
# Design system audit — "Harbor" v3.4   Date: 2026-10-01   Scope: 14 repos, 6 teams

## Purpose: consistent UI across the B2B suite; WCAG 2.2 AA baseline built into components.

## Inventory
Library: 46 components. Local equivalents found: 187 → 61 wrappers, 92 duplicates,
29 gaps, 5 sanctioned one-offs (marketing hero blocks).

## Duplication clusters
| Modal/Dialog | 9 | Analytics (4), Admin (3), Mobile web (2) | variant: library Dialog
  has no full-screen size; 2 copies lack focus trap | High |
| Date picker  | 5 | Analytics, Billing, Admin | variant: library DatePicker has no range mode | High |
| Data table   | 6 | Analytics (3), Admin (2), Billing | gap: no library table (excluded from adoption) | High |
| Button       | 14 | all teams | unaware: older copies predate v2 Button | Medium |

## Token coverage
| Colour    | 4,920 | 3,150 | 64.0% | 138 hexes within ΔE<3 of a token | 31 data-viz | 43 |
| Spacing   | 6,300 | 5,040 | 80.0% | 940 on the 4px grid | — | 320 off-grid |
| Font size | 1,100 | 1,045 | 95.0% | 41 | — | 14 |
(212 unique raw colours = 138 snap + 31 data-viz + 43 outliers.)

## Adoption and currency
| Billing    | 1,480 |   220 | 87.1% | v3.4 | yes |
| Onboarding | 1,150 |   160 | 87.8% | v3.2 | yes |
| Analytics  | 1,010 |   930 | 52.1% | v2.9 | no  |
| Admin      | 1,720 |   410 | 80.8% | v3.1 | yes |
| Mobile web |   960 |   300 | 76.2% | v2.6 | no  |
| Marketing  |   500 |   120 | 80.6% | v1.8 | no  |
Overall adoption: 6,820 ÷ 8,960 = 76.1%. Version currency: 6 of 14 repos on v3 = 43%.

## Checked and cleared
| BillingButton, AdminButton | wrappers of Harbor Button with presets | source read |
| Marketing hero blocks | sanctioned one-offs per brand team | DS charter §4 |
| "Card" in Analytics | domain model class, not UI | source read |

## Prioritised plan
| 1 | Add DataTable + date-range to library; migrate 11 local copies | 4 teams | 2 copies
     fail keyboard nav | L | High |
| 2 | Full-screen Dialog variant; retire 9 modals (2 lack focus trap) | 3 teams | a11y | M | High |
| 3 | Codemod 138 colour snaps; add data-viz token family (31) | all | brand drift | S | High |
| 4 | Upgrade path v1/v2 → v3 for Analytics, Mobile web, Marketing | 8 repos | patches
     not reaching them | M | Medium (effort unverified) |

## Metrics to re-measure (Q1)
Adoption ≥85% overall and ≥75% for every team; colour coverage ≥85%;
version currency ≥70%; zero modal implementations without focus trap.
```

## Techniques Used

- **RT-02 Multi-Dimensional Analysis Framework** — inventory, duplication, tokens, adoption and currency measured as separate dimensions.
- **AG-12 Quantitative Success Metrics** — adoption, coverage and currency defined by formula, with next-quarter targets.
- **QA-24 Dismissed-Candidates Coverage Table** — wrappers and one-offs recorded as checked and cleared.
- **DS-06 Prioritization and Severity Guidance** — reach × cost of inconsistency ÷ effort ranking.

## Related Prompts

- `frontend_design_token_architecture.md` — designing the token tiers the coverage numbers measure against.
- `frontend_design_system_component_governance.md` — the contribution and versioning rules that keep duplication from returning.
- `domain-frontend-development/styling/frontend_styling_tailwind_design_system.md` — when the tokens live in a Tailwind config.
