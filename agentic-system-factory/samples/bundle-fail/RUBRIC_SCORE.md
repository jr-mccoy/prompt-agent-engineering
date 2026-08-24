# RUBRIC SCORE — deep-research-fleet (INTENTIONALLY INCOMPLETE SAMPLE)

The safety half of Gate B is missing, so the eval category is halved and the load-bearing Gate B fails — `score_rubric.py` returns FAIL and caps the tier at "Needs work" even though the other categories are strong.

| Category | Score | Notes |
|----------|-------|-------|
| 1. Agent justification | 14/15 | unchanged from the worked design |
| 2. Topology fit | 14/15 | unchanged |
| 3. Security gate | 19/20 | unchanged |
| 4. Eval validity + real-tool safety | 10/20 | **capability only; no real-tool safety eval** |
| 5. Durability / observability / cost | 9/10 | unchanged |
| 6. Documentation completeness | 9/10 | unchanged |
| 7. Cross-link hygiene | 9/10 | unchanged |
| **Total** | **84/100** | High total, but **Gate B fails → Needs work** (load-bearing override). |

<!-- RUBRIC
cat1_justification: 14
cat2_topology: 14
cat3_security: 19
cat4_eval: 10
cat5_durability: 9
cat6_documentation: 9
cat7_crosslink: 9
-->
