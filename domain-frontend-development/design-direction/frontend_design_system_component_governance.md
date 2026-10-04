---
title: "Design System Component Governance — API Review Rules, What Counts as Breaking, Deprecation Policy, and the Contribution Model"
category: frontend-development/design-direction
description: "Set the rules that keep a shared component library coherent as many teams use and extend it: an API review checklist, a written definition of breaking change for UI components (props, defaults, DOM, visuals, behaviour, tokens), a deprecation policy with removal criteria and codemods, a contribution model with tiered paths and decision rights, and health metrics that show whether governance helps or blocks."
techniques:
  - QA-09
  - IT-22
  - DP-13
  - AG-12
difficulty: advanced
tags:
  - design-system
  - component-api
  - semantic-versioning
  - deprecation-policy
  - contribution-model
  - design-system-governance
  - component-library
  - teams-keep-building-their-own
  - upgrade-broke-our-app
updated: "2026-10-03"
related_prompts:
  - domain-frontend-development/design-direction/frontend_design_system_audit.md
  - domain-software-engineering/api/api_versioning_strategy.md
  - domain-frontend-development/typescript/frontend_typescript_component_typing.md
---

# Design System Component Governance

**Objective:** Write the governance a component library runs on — how a component API is
reviewed, what version bump each kind of change requires, how components are deprecated
and removed, how other teams contribute, and who decides — so the library can change
without breaking consumers and without becoming a bottleneck.

**When to Use:**
- Consumers complain that a "minor" upgrade broke layouts or tests.
- Product teams build their own components because contributing takes too long or the
  path is unclear.
- The library carries several deprecated components nobody has removed.
- A design system is moving from one maintainer team to a federated model.
- **Not this prompt if** you are versioning an **HTTP or service API** — use
  `domain-software-engineering/api/api_versioning_strategy.md`; that prompt has no notion of
  visual, DOM, or accessibility-behaviour compatibility. For typing an individual
  component's props, use
  `domain-frontend-development/typescript/frontend_typescript_component_typing.md`; for
  measuring whether teams adopt the library, use `frontend_design_system_audit.md`. To make
  team-wide engineering process decisions beyond the library (sprints, definition of done),
  use `domain-engineering-workflows/`.

## Inputs / Context

1. **Library facts**: package(s), current version, release cadence, consumer count.
2. **Recent incidents**: upgrades that broke consumers, with what changed.
3. **Current deprecations** with usage counts per consumer, if measured.
4. **Team model today**: central team size, who reviews, how proposals arrive.
5. **Public surface**: is DOM structure, class names, or `data-` attributes documented as
   stable? Do consumers snapshot-test or select on library markup?
6. **Accessibility baseline** the library promises (e.g. WCAG 2.2 AA, keyboard patterns).

## Method

1. **Define the public API explicitly.** Props and their defaults, events/callbacks, slots
   or children contracts, exported tokens, keyboard and focus behaviour, ARIA semantics,
   and — decided deliberately — whether DOM structure and class names are public. Anything
   undocumented is private, and the docs say so.
2. **API review checklist.** Composition over boolean-prop explosion (more than ~3 mutually
   exclusive booleans → a `variant` or a slot); consistent naming across components
   (`size`, `variant`, `onOpenChange`); controlled and uncontrolled modes; a stated escape
   hatch policy (`className` pass-through yes/no); accessibility contract written before
   build; no product-specific props.
3. **Classify changes by reversibility for consumers (QA-09).** For each change type
   decide patch/minor/major. A change is **breaking** if a consumer's working code, test,
   or accessible behaviour can stop working without them editing anything: removing or
   renaming a prop; changing a default; changing documented DOM; changing focus or keyboard
   behaviour; renaming or removing a token; changing component box size in a way that
   reflows layouts. Visual refinements within the same token roles are minor with a
   release note. An accessibility fix that changes behaviour is shipped promptly as a
   minor, announced, and never held for the next major.
4. **Deprecation policy with kill signals (DP-13).** Deprecate in a minor with a
   development-mode warning, docs banner, migration guide, and codemod where mechanical.
   Remove only in a major, and only when a stated signal is met: usage below a threshold,
   or a minimum period elapsed, or both. Track usage per consumer on a deprecation board.
5. **Contribution paths (IT-22).** Tier by change type: *fix* (bug, docs) → fast path,
   one maintainer review; *extension* (variant, prop) → proposal with use cases from at
   least two products, API review; *new component* → proposal, evidence of need in two or
   more products, design + a11y spec, built with or by the central team, staged as
   experimental before stable. State the artefacts required, reviewers, and target
   response time for each tier. Name the model (centralised, federated, hybrid) and who
   holds the final decision.
6. **Governance health metrics (AG-12).** Time from proposal to decision; share of
   proposals accepted, redirected, or declined with reasons; share of breaking releases
   with a codemod; consumers on the current major; age of open deprecations. Governance
   that slows every decision produces the duplication it is meant to prevent.

## Output Format

```
# Component governance — [library]   Model: [centralised | federated | hybrid]

## Public API definition (what is and is not public)
## API review checklist
## Change classification
| Change type | Example | Bump | Required with release |
## Deprecation policy
Notice · warning · migration aid · removal signal · board
## Current deprecations
| Component/prop | Deprecated in | Usage now | Removal signal | Status |
## Contribution paths
| Tier | Entry criteria | Artefacts | Reviewers | Response target | Decision owner |
## Decision rights
## Health metrics and targets
```

## Verification

- [ ] The public surface is written down, including an explicit DOM/class-name decision.
- [ ] Default changes and keyboard/focus changes are classified as breaking.
- [ ] Every deprecation has a removal signal, not just a date or intent.
- [ ] Each contribution tier has entry criteria, artefacts, reviewer, and response target.
- [ ] A named owner holds the final decision for new components.
- [ ] Health metrics include time-to-decision, not only output counts.

## False-Positive Prevention

1. **"No props changed, so it's a patch."** A changed default or focus behaviour breaks
   consumers with identical props.
2. **DOM as accidental API.** If consumers select on library markup and the docs never
   said it was private, a restructure is breaking in practice; decide and document.
3. **Deprecation as removal.** A warning with no usage tracking and no codemod becomes a
   permanent second component.
4. **Accessibility fixes held for majors.** Waiting for a major to fix a keyboard trap
   leaves users blocked; ship and announce.
5. **Contribution rules nobody can meet.** Requiring full design specs for a bug fix
   pushes teams to fork.
6. **Single-product components promoted.** A component needed by one product belongs in
   that product until a second product needs it.
7. **Merge count as health.** Many merged contributions with a 40-day decision time is a
   bottleneck, not success.

## Example Output

```
# Component governance — "Harbor" (React, 14 consuming repos)   Model: hybrid

Trigger: v3.3 changed Dialog's default closeOnOverlayClick true → false as a "minor";
two products lost unsaved form data handling; 3 teams pinned to v3.2.

## Public API definition
Public: props + defaults, callbacks, slot contracts, tokens, keyboard/focus/ARIA behaviour.
Private: DOM structure and class names (stated in docs; consumers use data-testid on
their own wrappers). Transitional: DOM changes announced one minor ahead until v4.0.

## Change classification
| Remove/rename prop       | Button.isPrimary → variant | major | codemod + guide |
| Change a default         | Dialog closeOnOverlayClick | major | (v3.3 should have been major) |
| Focus/keyboard behaviour | Menu typeahead added       | minor + announce | a11y note |
| Add variant/prop         | Button variant="ghost-danger" | minor | docs |
| Token role change        | border.subtle → border.default in Input | minor | visual diff |
| Box-size change          | Input height 36 → 40px     | major | layout note |
| Bug / a11y fix           | Tooltip not announced      | patch | — |

## Current deprecations
| Modal (→ Dialog) | 3.2 (2026-04) | 1,140 inst. in 9 repos | <5% of Apr usage or 2027-01-31,
  whichever later; codemod covers 92% | on track |
| Button.isPrimary | 3.0 | 310 inst. | codemod 100%; remove in 4.0 | ready |

## Contribution paths
| Fix | issue + failing case | PR + test | 1 maintainer | 3 business days | maintainer |
| Extension | use cases from ≥2 products | API proposal, a11y note, docs | 2 maintainers +
  1 designer | 10 business days | DS lead |
| New component | need in ≥2 products; no existing composition works | proposal, design +
  a11y spec, experimental release ≥1 minor | API council (DS lead, 2 product reps) |
  15 business days | DS lead (final) |
SegmentedControl proposal (Analytics + Admin) → accepted as experimental in 3.6.
"BillingSummaryCard" proposal (Billing only) → redirected to Billing's local library.

## Health metrics and targets
Median proposal→decision: 23 days now → ≤10. Breaking releases with codemod: 1 of 3 → 100%.
Consumers on current major: 43% → 70% within two quarters of v4.0. No deprecation >12 months old.
```

## Techniques Used

- **QA-09 Reversibility Assessment** — changes classified by whether consumers can keep working without edits.
- **IT-22 Workflow Decision Matrix** — contribution tier maps change type to path, artefacts, and reviewer.
- **DP-13 Kill Signal Definition** — usage and time thresholds that permit removal of a deprecated component.
- **AG-12 Quantitative Success Metrics** — time-to-decision and codemod coverage as governance health.

## Related Prompts

- `frontend_design_system_audit.md` — measuring adoption and duplication that governance should reduce.
- `domain-software-engineering/api/api_versioning_strategy.md` — versioning for service APIs rather than UI components.
- `domain-frontend-development/typescript/frontend_typescript_component_typing.md` — typing the props the API review defines.
