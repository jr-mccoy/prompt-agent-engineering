# Prompt Engineering Techniques

**Purpose:** Reference documentation for 327 active prompt engineering techniques across 18 categories.

This directory contains the technique catalog, use case patterns, and reference materials for building effective prompts.

## Key Files

| File | Purpose |
|------|---------|
| `MASTER_TECHNIQUE_INDEX.md` | Complete catalog of 327 active techniques across 18 categories |
| `USE_CASE_LOOKUP.md` | Pre-built technique combinations by task type |
| `new-techniques/` | Detail files for selected techniques |

## Technique Categories

All 16 categories, by ID prefix:

- **ST** Structural · **RT** Reasoning · **OC** Output Control · **QA** Quality Assurance
- **CM** Context Management · **RP** Role & Perspective · **DT** Decomposition · **ED** Educational
- **MP** Meta-Prompting · **DS** Domain-Specific · **AG** Agentic · **NE** Non-Engineering
- **IT** Interaction · **SV** Specialized Visual & Interview · **DD** Done Definition · **DP** Delegation & Productivity

## Validation

Counts, technique-ID references, and links across the catalog and authoring
docs are checked by:

```bash
python3 scripts/validate_technique_catalog.py           # all checks (exit 1 on drift)
python3 scripts/validate_technique_catalog.py --counts  # print current canonical numbers
```

Run it after editing `MASTER_TECHNIQUE_INDEX.md` or any doc that states
technique counts. If counts legitimately changed, update the claims using the
`--counts` output.

## Quick Start

1. **Know your task type?** Start with `USE_CASE_LOOKUP.md`
2. **Need technique details?** Reference `MASTER_TECHNIQUE_INDEX.md`
3. **Building new prompts?** See [`../authoring/`](../authoring/)

## Related Resources

- [`domain-software-engineering/`](../domain-software-engineering/) - Apply techniques in software engineering prompts
- [`domain-business-strategy/`](../domain-business-strategy/) - Apply techniques in business strategy prompts
- [`domain-agentic-resources/`](../domain-agentic-resources/) - Apply techniques in coding agent resources
- [`authoring/`](../authoring/) - Guides for creating new resources
