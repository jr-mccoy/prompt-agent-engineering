# Design Direction & Design Systems Prompts

**Category:** Frontend Development / Design Direction
**Prompts:** 5

---

## Overview

Prompts for deciding how an interface should look and for keeping that decision coherent
once many teams build on it: finding a visual direction, pinning it into a look-and-feel
spec, structuring it as design tokens, and auditing and governing the shared component
library. These are judgement and review prompts — technology-agnostic — not tool how-to.

## Prompts

| Prompt | Description | Difficulty |
|--------|-------------|------------|
| [frontend_visual_design_direction_finder.md](frontend_visual_design_direction_finder.md) | Brand attributes → 2–3 distinct visual direction options with a recommendation | Intermediate |
| [frontend_look_and_feel_hunt.md](frontend_look_and_feel_hunt.md) | A target "vibe" → concrete look-and-feel spec (palette intent, type, density, motion) | Intermediate |
| [frontend_design_token_architecture.md](frontend_design_token_architecture.md) | Primitive / semantic / component tiers, naming grammar, theme axes, contrast-checked pairs | Advanced |
| [frontend_design_system_audit.md](frontend_design_system_audit.md) | Component inventory, duplication clusters, token coverage, adoption and version currency per team | Intermediate |
| [frontend_design_system_component_governance.md](frontend_design_system_component_governance.md) | API review rules, what counts as breaking, deprecation policy, contribution model | Advanced |

## Typical Sequence

```
Direction finder → Look-and-feel hunt → Token architecture
  → (library built) → Design system audit ⇄ Component governance
```

## Why design systems live here, not in `styling/`

`styling/` reviews a styling technology's implementation (CSS methodology, a Tailwind
config, CSS-in-JS runtime cost). The design-system prompts here judge the system as a
product — its tiers, adoption, and rules — whatever technology carries it.

## Boundaries — lives elsewhere

- Tailwind config as the token source → [../styling/frontend_styling_tailwind_design_system.md](../styling/frontend_styling_tailwind_design_system.md)
- CSS cascade, layers, specificity → [../styling/frontend_styling_css_architecture.md](../styling/frontend_styling_css_architecture.md)
- Accessibility conformance of the shipped UI → [../accessibility/](../accessibility/)
- Usability review of screens → [../ux-research/](../ux-research/)
- Service/HTTP API versioning → [../../domain-software-engineering/api/api_versioning_strategy.md](../../domain-software-engineering/api/api_versioning_strategy.md)
- Building a Tailwind component library hands-on → `domain-agentic-resources/skills/web-development/tailwind-design-system/`
