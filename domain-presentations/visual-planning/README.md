# Visual / Frontier Planning

Prompts for the analytic work that sits upstream of visually-delivered artifacts: mapping what a new capability unlocks, designing a QA harness for visual work, routing a task to the right modality, and scanning for cascade effects. These are planning prompts — they produce structured maps and routed decisions, not finished decks.

## When to Use This Cluster

- A new capability (an AI model, tool, integration) has arrived and you need to map what it actually changes — not what the hype claims.
- You ship visuals (decks, dashboards, infographics, generated images) and the usual safety nets miss visual-specific errors.
- You're about to produce an artifact and want to route to the right modality (table vs chart vs deck vs no-visual) before investing in production.
- You need to scan the second- and third-order effects a capability adoption will trigger across roles, processes, artifacts, metrics, and norms.

## Prompts

| # | Prompt | Use When |
|---|--------|----------|
| 1 | [`visualplan_capability_frontier_map.md`](visualplan_capability_frontier_map.md) | Map a new capability into three bands: what became cheap, what became possible, what's still out of reach. Refuses hype; requires evidence per claim. |
| 2 | [`visualplan_visual_qa_harness.md`](visualplan_visual_qa_harness.md) | Design a per-artifact QA harness — checklist, reviewer protocol, drift checks — for a specific visual artifact type you ship regularly. |
| 3 | [`visualplan_modality_router.md`](visualplan_modality_router.md) | Route a communication or thinking task to the right modality (table, chart type, diagram, deck, infographic, dashboard, sketch, or text-only). |
| 4 | [`visualplan_cascade_effects_scan.md`](visualplan_cascade_effects_scan.md) | Scan for second- and third-order effects across five planes (roles / processes / artifacts / metrics / norms) with early-warning signals. |

## Cross-References

- Deck production and assembly: [`../powerpoint_board_deck_generator.md`](../powerpoint_board_deck_generator.md), [`../powerpoint_deck_assembly_and_validation.md`](../powerpoint_deck_assembly_and_validation.md)
- Image generation guide (for visual artifacts produced via image models): [`../../domain-image-generation/IMAGE_GENERATION_GUIDE.md`](../../domain-image-generation/IMAGE_GENERATION_GUIDE.md)
- AI strategy & capability evaluation (compounds with frontier mapping): [`../../domain-business-strategy/ai-strategy/`](../../domain-business-strategy/ai-strategy/)
- Bottleneck migration planning (cascade effects feed into this): [`../../domain-engineering-workflows/ai-native-rollouts/airollout_bottleneck_migration_plan.md`](../../domain-engineering-workflows/ai-native-rollouts/airollout_bottleneck_migration_plan.md)
- Prompt correctness & pre-mortem: [`../../domain-prompt-engineering/evaluation/correctness_pre_mortem.md`](../../domain-prompt-engineering/evaluation/correctness_pre_mortem.md)

### Board-deck visualizations (planned)

Image-generation prompts for specific board-deck chart types (funnel diagnostic, opportunity-solution tree, ARR revenue bridge, cohort retention heatmap, etc.) are scoped for a future session and will live in `../board-deck-visualizations/`. The prompts in this directory complement those by handling the analytic / routing / QA work that precedes image generation.

## Design Principles

- **Evidence beats hype.** Capability maps grade each claim by whether the user (or a named peer) has actually done it; hype vocabulary is banned as load-bearing.
- **Three bands, not two.** "Became cheap," "became possible," AND "still out of reach." Honest Band 3 is where strategy lives.
- **Content shape drives modality.** Routing starts from what's actually being shown, not from a favorite modality. Sometimes no visual at all is the right answer.
- **QA is artifact-specific.** Generic review checklists miss visual-specific errors. Each harness is built from the actual past failures of the actual artifact type.
- **Cascades get mechanisms.** A second-order effect without a mechanism linking it to the first-order change isn't in the map; it's just a guess.
