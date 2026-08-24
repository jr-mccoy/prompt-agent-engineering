# Domain-Personal-Development Expansion Roadmap

**Status as of 2026-07-23:** Wave 1 shipped — **70 net-new prompts** (96 → **166**) plus two new subdirectories, bringing every themed subfolder to a ~10-prompt floor. All new prompts follow the domain's modern Tier-1 house style (exemplar: `prompts/identity/identity_values_clarification.md`): 8-field frontmatter, Objective → When to use → Audience → Inputs Required → Instructions (fixed taxonomies) → Constraints (Must/Must Not) → False-Positive Prevention → Output Format → Verification. House rules: one decisive move over a menu, evidence-or-drop, anti-moralizing, non-clinical distress routed to `domain-psychology/` + professional help.

Filing convention: `{folder-prefix}_{specific_function}.md` inside the relevant subfolder (e.g. `goals_*`, `lifetransition_*`, `emotionalfitness_*`, `personal_*` for `major-decisions/`, `career_*` for `career-transformation/`).

---

## Wave 1 Status — Shipped

```
domain-personal-development/            166 prompts
├── prompts/
│   ├── agency/                 17   (+2)   accountability-partner, project-scope-creep
│   ├── goals/                  10   (+6)   annual-planning, conflict-resolver, anti-goals, values→goals, stall-diagnostic, scope-right-sizer
│   ├── habits/                 10   (+4)   identity-based, implementation-intentions, tracking-system, temptation-bundling
│   ├── identity/               11   (+4)   strengths-inventory, narrative-reframe, authenticity-audit, memento-mori
│   ├── resilience/             11   (+5)   rejection-recovery, criticism-processing, confidence-rebuild, uncertainty-tolerance, comeback-after-dip
│   ├── relationships/          11   (+5)   friends-as-adult, deepening, difficult-family, apology, loneliness-diagnostic
│   ├── thinking/               12   (+3)   decision-journal, mental-models-application, assumption-surfacing
│   ├── productivity/            8   (+3)   overcommitment/saying-no, energy-by-task-type, focus-ritual (cross-links domain-productivity/)
│   ├── solo-dev/               10   (+5)   pricing-confidence, deciding-alone, accountability, sustainable-pace, isolation-motivation
│   ├── stakeholder/             7   (+5)   managing-up, manager-relationship, visibility-credit, mentor-sponsor, cross-team-alliance
│   ├── career/                 17   ( 0)   AI-role assessment set — left as-is (coherent legacy interview/verdict format)
│   ├── life-transitions/       10   (NEW)  new-role, relocation, new-parenthood, empty-nest, retirement, job-loss, breakup, return-from-leave, identity-after-change, transition-map
│   └── emotional-fitness/      10   (NEW)  emotion-labeling, disappointment, jealousy-channeling, worry-vs-action, reactivity-audit, ambivalence, self-compassion, reset-ritual, shame-vs-guilt, charged-event-debrief
├── career-transformation/       8   (+4)   ai-era-skill-moat, positioning-statement, internal-vs-external-move, reskilling-roadmap
└── major-decisions/            14   (+4)   marriage-commitment, aging-parent-care, sabbatical, start-business-vs-employment
```

### Two new subdirectories — design boundaries

- **`life-transitions/`** — Navigating a change **during/after** it happens. Clean split from `major-decisions/`: that folder is about making the choice *before*; this is about living through the change. Non-clinical; grief/depression/trauma route to `domain-psychology/` (higher-risk transitions — job loss, breakup, postpartum, identity loss — carry crisis-line language).
- **`emotional-fitness/`** — Everyday **non-clinical** self-regulation skills for the general population. **Load-bearing boundary:** this is NOT therapy and does not clone the clinical prompts in `domain-psychology/client-self-use/` (no PHQ-9/GAD-7 scoring, no CBT/ERP protocols). Angles were chosen to complement, not duplicate, the clinical set; every prompt routes persistent/intense/safety-relevant distress to `domain-psychology/` + a licensed professional.

---

## Wave 2 — Candidate future work (not yet built)

- **`career/` template refresh** — the 17 AI-role assessments use the older interview/verdict template. A future wave could convert them to the rigorous Tier-1 template, or extend the set to non-AI roles.
- **Money mindset (behavioral)** — relationship-with-money, spending-values, scarcity-vs-abundance framing (behavioral only; specifics stay in `domain-finance/`).
- **Deepen thin cross-links** — add backlinks from existing prompts into `life-transitions/` and `emotional-fitness/`; a few Wave-1 files linked to nearest-equivalents before the new folders existed.
- **`stakeholder/` growth** — org-navigation set is still the smallest themed folder (7); room for peer-conflict, promotion-case, and reorg-navigation prompts.
- **Meaning & purpose depth** — expand `identity/` toward legacy, vocation, and spirituality-neutral meaning-making.

---

## Conventions (for future authors)

1. Match the exemplar structure exactly; target ~120–180 lines.
2. Technique IDs must exist in `techniques/MASTER_TECHNIQUE_INDEX.md`. Typical spine: `ST-01, ST-02, RT-02, DS-06, QA-12/QA-20`.
3. Non-duplication: cross-link (don't clone) `domain-productivity/`, `domain-psychology/`, `domain-negotiation/`, `domain-reasoning-craft/`, `domain-decision-making/`.
4. Every emotional/transition prompt carries the non-clinical routing line in its Audience block.
5. After adding files, regenerate the index: `python3 scripts/generate_prompt_index.py`.
