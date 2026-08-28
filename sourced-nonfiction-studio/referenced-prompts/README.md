# Referenced Prompts

The studio **orchestrates** these existing repo prompts — it references them in place, it does not
copy them. Each stage's prompt names the upstream prompt(s) it drives. Keep this list in sync if the
upstream paths move.

## By stage

| Stage | Upstream prompt(s) |
|-------|--------------------|
| 1 Claim extraction | `domain-reasoning-craft/epistemic/epistemic_claim_inference_separator.md` · `domain-research-academic/research_question_formulation.md` |
| 2 Source discovery | `domain-research-academic/research_search_strategy_designer.md` · `domain-research-academic/research_field_landscape_map.md` |
| 3 Match & weight | `domain-research-academic/research_source_triangulation.md` · `domain-reasoning-craft/epistemic/epistemic_evidence_quality_score.md` · `domain-reasoning-craft/epistemic/epistemic_source_credibility_triangulation.md` · `domain-research-academic/research_evidence_map.md` · `domain-prompt-engineering/rag-prompts/rag_conflict_resolution_across_sources.md` |
| 4 Disposition | **`domain-professional-writing/writing/writing_unsourced_claim_disposition.md`** (net-new) · `domain-reasoning-craft/epistemic/epistemic_uncertainty_acknowledgment_audit.md` |
| 5 Risk & integrity | `domain-legal/ip/legal_copyright_fair_use_analysis.md` · **`domain-legal/ip/legal_defamation_publicity_risk_screen.md`** (net-new) · `domain-professional-writing/writing/writing_original_expression_rewriter.md` · `domain-science/ethics-integrity/science_misconduct_self_audit.md` · `domain-prompt-engineering/hallucination-control/hallucination_citation_required_pattern.md` |
| 6 Assembly | `domain-research-academic/research_secondary_source_synthesis.md` · `domain-education-teaching/learner/writing/learn_citation_helper.md` · `domain-prompt-engineering/rag-prompts/rag_citation_format_designer.md` |
| back-end | **`domain-research-academic/research_manuscript_fact_check_reconciler.md`** (net-new — the `/fact-check-manuscript` entry) |

## Net-new prompts authored for this studio (indexed in their domains)
- `domain-professional-writing/writing/writing_unsourced_claim_disposition.md` — KEEP/SOFTEN/REFRAME/QUOTE/CUT for uncitable claims.
- `domain-research-academic/research_manuscript_fact_check_reconciler.md` — reconcile a finished draft vs its sources.
- `domain-legal/ip/legal_defamation_publicity_risk_screen.md` — defamation / right-of-publicity risk screen.

These three live in their domain directories (not in this bundle) so they're discoverable via
`PROMPT_INDEX` and reusable outside the studio.
