# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added
- **PAE Engine `0.2.0.dev0` — deterministic search and task routing.** `pae search "<query>"` ranks registry resources against a natural-language description and `pae route "<task>"` decides which scope and resource kind should handle it. Both are offline, read-only, deterministic and standard-library-only; runtime dependencies remain empty. **Ranking reads registry metadata only** — neither module calls `Registry.content()`, enforced by a source-level check and by a behavioural test that makes the call fail loudly, so what a resource says can never influence where it ranks and search can never become a way to read something serving policy withholds. Ranking is **BM25F with uniform field weights** (`k1=1.2`, `b=0.75`) over ten fields (title, public-ID path, aliases, description, category, tags, technique IDs, source path, kind, native name), chosen against measured alternatives rather than intuition: over a committed 120-case regression set, weighted token overlap scored 56.1% top-1 and flat BM25 75.8% against BM25F's 77.3%, and **every hand-tuned field weighting and every relevance-bonus layer measured worse than uniform** — an additive technique-ID bonus was structurally wrong, rewarding the ~3,900 prompts that *cite* `ST-01` and burying the technique record plain BM25F already ranks first. One shared normalizer serves indexing and querying (NFKC → casefold → split on non-`[0-9a-z]` → stopwords → one-rule depluralization, itself worth ~10 points of top-1). The index is **in-memory, immutable and lazily built** on first lexical search; an exact UID, public ID or retired alias resolves at rank 1 without building it at all. There is no committed index artifact, no cache directory, no database and nothing written at runtime. Routing aggregates by **maximum, never sum** — with 4,196 prompts against 53 personas a summing router scored 58.5% on kind against maximum's 97.6%, and maximum is structurally immune to a registered copy voting twice for its toolkit. Certainty is expressed as **coverage** and **margin**, never as confidence: `matched` / `ambiguous` / `weak` / `no_route`, with `selected_scope` and `selected_kind` populated only when `matched`, and **every status exiting 0** because ambiguity is a result rather than a failure. A `score` is an unbounded ranking number with no `confidence` field anywhere in the output. New public models `SearchHit`, `SearchResults`, `RouteCandidate` and `RouteDecision`, all carrying durable UIDs rather than file paths and all owning `to_json_obj()`. See [`pae-engine/docs/search-routing.md`](pae-engine/docs/search-routing.md), ADR-0021, ADR-0022 and ADR-0023.
- **`pae-engine/tests/data/search_routing_regression.v1.json` + `tests/run_search_routing_diagnostics.py`** — a committed 120-case internal regression corpus (40 natural-language task retrieval, 20 non-prompt-kind, 20 routing, 15 ambiguous cross-domain, 10 acronym/format/typo, 10 weak/no-route, 5 copy/dedup) with per-case label provenance, machine-validated against the live registry, plus a runner that reports search and routing metrics broken out by class and can re-score the two rejected baselines through the same index. **It is labelled prominently, in the data file and in the runner's output, as an internal tuning and regression set — not an independently authored benchmark and not evidence of general search quality** — because its labels were written by the same process that selected the algorithm and the router's thresholds were fitted on it. Conservative regression floors are asserted in CI.
- **`scripts/compare_router_to_claude_md.py`** — migration diagnostics comparing the executable router against the 1,512 hand-written `"user phrase" → resource` mappings already in `CLAUDE.md` (887 unique phrases resolve to registry records): resource@1 83.4%, resource@3 91.0%, scope@1 92.2%, scope@3 96.1%. Those figures are **flattered** — the phrases are documentation labels that often share vocabulary with their target's title — and are recorded as migration evidence, not evaluation.

### Changed
- **`meta/adr/0012-one-record-per-copy.md` amended.** Its Phase 2 suggestion that search should "hide `copy_of != null` by default" is superseded by **canonical-cluster deduplication**: a canonical and its registered copies form one cluster and search returns the highest-scoring eligible member, so a toolkit-local copy can win a toolkit-scoped query. Retrieval metrics did not decide this — all three copy policies landed within one query, and under the shipped ranker deduplication and no deduplication scored identically — so the deciding argument is the one ADR-0012 already made: a user usually wants the copy the toolkit ships. Every hit exposes `canonical_uid` and `copy_uids`, and `--include-copies` returns the physical members. The identity decision is unchanged, and clusters are still built only from explicit `VENDORED.tsv`-sourced edges, never hashes or filenames. One safety refinement: a copy whose canonical is **excluded** reports its own UID, because surfacing the excluded record's UID would let a caller enumerate excluded resources by collecting cluster pointers that resolve to nothing.
- **Stale bootstrap claims corrected.** `AGENTS.md` and `START_HERE_FOR_AI.md` asserted that the Engine was "planned, not implemented" and that "there is no `pae` command" — both false since Phase 3 merged. They now describe the Engine that exists and point at `pae route` / `pae search` first, while keeping the prose routing guidance as the fallback and as the authority for authoring policy and safety semantics. `CLAUDE.md` gains an executable-router pointer at its routing entry; **none of its routing tables, conventions or policy prose were deleted** (ADR-0023). `ARCHITECTURE.md`, `ROADMAP.md`, the root `README.md`, `pae-engine/README.md` and `pae-engine/docs/getting-started.md` updated to match.

### Added (earlier, unreleased)
- **`domain-psy-ops/` (32 prompts + README + EXPANSION_ROADMAP)** — new cognitive-security domain covering the recognition, analysis, and defense of psychological influence, across six subdirectories: `technique-analysis/` (7), `influence-operations/` (7), `personal-defense/` (7), `organizational-red-team/` (4), `counter-messaging/` (4), `case-studies-taxonomies/` (3). Fills a genuine repository gap — nothing previously covered influence operations, propaganda analysis, or manipulation defense. **The domain is built on an output-side constraint rather than a permission gate**, because the `domain-software-engineering/bug-bounty/` dual-use precedent does not transfer: a bounty program is a verifiable, scoped grant of permission from a consenting target, whereas an influence operation's targets by definition do not know it is happening, so no authorization would make campaign-generation legitimate. Every prompt's deliverable is therefore an assessment, a defense, or a resilience plan; red-team prompts emit findings and countermeasures only. Five supporting rules: **no manufactured accusations** (confidence-graded assessments with a mandatory alternative-explanation pass, attached to behavior and content, never naming a private individual as a covert operative), **no fabricated evidence** (`[VERIFY]`, never a plausible fill-in), **attribution humility** (low/moderate/high with stated basis; "unattributed" is the default and a valid result), **safety routing** (Safety Blocks on all five `personal-defense/` prompts touching fear, abuse, danger, or active fraud; no prompt in the domain ever states a hotline number or service name from memory — all instruct verification from an official source), and **counter-messaging stays overt** (named sender, truthful, attributed). The characteristic failure mode the domain is designed against is paranoid over-attribution — organic convergence read as coordination, sincere belief read as a script, incompetence read as deception — which every False-Positive Prevention block targets. All prompts are Tier-1 in the `domain-reasoning-craft/`/`domain-negotiation/` house style (8-field frontmatter with the machine-readable `reasoning:` block, exactly six `##` headings, ~8 instruction steps, 8-item False-Positive Prevention, locked Output Format, 10-item Verification closing on negative assertions). One deliberate deviation from that house style: analysis prompts end in an adversarial check arguing against their own finding, but the seven `personal-defense/` prompts do not — adversarially challenging someone working through suspected coercive control, or a parent frightened for their child, is harmful rather than rigorous, so those prompts carry their skepticism in the mandatory alternative reading and close on a next step the user chooses. `uncertainty: ambiguity` is a domain invariant and `psyops_` is the single filing prefix. `scripts/generate_prompt_index.py` `DOMAIN_DIRS` updated; `PROMPT_INDEX.json`/`PROMPT_INDEX.md` regenerated (+33, total 5337); `CLAUDE.md` (domain tree, routing section, 31 quick-reference rows), root `README.md`, and `REPO_MAP.md` updated; reverse cross-links added from `domain-reasoning-craft/README.md` and `domain-negotiation/craft/negotiation_ethics_line.md`. The roadmap carries an "Explicitly not gaps" boundary table and a permanently-out-of-scope list.
- **`domain-biblical-studies/` (31 prompts + 5 READMEs)** — new Bible-study & biblical-research domain serving four audiences (laypeople/devotional, small-group & Sunday-school leaders, pastors/preachers, seminary/academic) across four subdirectories: `exegesis-interpretation/` (9), `study-methods-teaching/` (8), `sermon-devotional/` (7), `theology-research/` (7). Two load-bearing conventions: (1) **tradition-neutral** — prompts describe rather than endorse, attributing contested readings to identifiable interpretive streams (Protestant/Catholic/Orthodox/Jewish/academic-critical) without ruling, with an optional user-declared-tradition hook that still preserves alternatives; (2) **anti-fabrication first** — every prompt forbids invented citations, misquotes, fabricated scholar/commentary attributions, invented cross-references, and made-up original-language or historical data, referencing verses by address and routing to named real resources for verification. Eleven higher-risk prompts (original-language word study, translation/variant comparison, historical-cultural context, multi-view interpretation, thematic study, sermon illustrations, topical/systematic synthesis, doctrine study, cross-reference/typology, difficult-passage analysis, background research brief) carry heavier STRONG-GUARD language. All prompts are Tier-1 (frontmatter, When to Use / NOT, Constraints, Instructions, Output Format, Verification, False-Positive Prevention). `scripts/generate_prompt_index.py` `DOMAIN_DIRS` updated (26→27 domains); `PROMPT_INDEX.json`/`PROMPT_INDEX.md` regenerated (+31, total 3758); `CLAUDE.md` (domain tree, routing prose, quick-reference table) and root `README.md` updated.
- **`domain-legal/family-self-advocacy/` (21 prompts + README)** — litigant-facing divorce/custody legal-*preparation* set for self-represented or self-organizing laypeople putting together their own side for a lawyer and family court. This is the sole `domain-legal/` subsection that inverts the attorney-only, disclaimer-free convention: strong not-legal-advice boundary, mandatory Safety Block, required jurisdiction, no fact fabrication; the prompts organize/document/prepare only (no advice, outcome prediction, statute citation, filings, or characterizing the other party — all routed to counsel). Covers case chronology, evidence/exhibit index, communication/incident records, witness/source map, financial-disclosure organizer, asset/debt inventory, budget worksheet, financial-document checklist, allegation-response organizer, neutral factual account, concerns-about-other-party organizer, hearing/deposition/custody-evaluation/mediation prep, court-process explainer, consultation-question builder, best-interests self-map, and the flagship attorney handoff brief. Complements (does not duplicate) the emotional/relational `domain-parenting/caregiver-facing/` sets, which now back-point to it. Index regenerated; `CLAUDE.md` and `domain-legal/README.md` routing updated.

### Changed
- **Perianesthesia content consolidated under the healthcare domain.** The two
  standalone PACU trees that previously sat at the repository root were folded into
  the umbrella domains they belong to, with no prompts lost: clinical, educator, and
  staged-learner artifacts now live under
  `domain-healthcare-clinical/prompts/perianesthesia/`; the visual meta-prompts under
  `domain-image-generation/healthcare/`; the authoring skills under
  `domain-agentic-resources/skills/non-coding/healthcare/`; and the routing command and
  educator persona under their respective agentic-resource trees. A side effect worth
  noting: these ~155 prompts sat outside every indexed domain and so had never appeared
  in `PROMPT_INDEX`; they are now discoverable.
- **Public repository initialized from a reviewed clean snapshot.** This repository
  begins at a deliberately prepared public snapshot rather than inheriting an earlier
  development history. Internal development history, working branches, and
  release-preparation artifacts are intentionally not included.
- **Content review pass.** Prompts across the collection were reviewed and, where
  required, reauthored as original, Tier-1, anti-fabrication-compliant material.
  Roughly 85 older prompts were migrated to the current Tier-1 template (frontmatter,
  Must/Must Not, False-Positive Prevention, Verification).
- **Repository made portable.** `.claude/settings.json` is reduced to the portable
  subset (`env`, `enabledPlugins`, `extraKnownMarketplaces`); the `bypassPermissions`
  default and a `SessionStart` hook that seeded a plugin cache from a hardcoded
  absolute path were both removed. Maintenance scripts resolve the repository root
  relative to their own location rather than a hardcoded path.
- **Documentation counts reconciled** against the repository's own generators and
  validators. See *Repository Statistics* below.

### Removed
- Internal release-preparation tooling, build-process session reports, and
  repository-development tracking documents.
- Vendored third-party plugin cache (`.claude/plugins/cache/`) and per-machine plugin
  state (`installed_plugins.json`, `known_marketplaces.json`, `settings.local.json`)
  are untracked and gitignored — plugins named in `enabledPlugins` install themselves
  from the marketplace on first run.
- Legacy metadata scripts that scanned a pre-`domain-*` directory layout and therefore
  validated nothing (`scripts/validate-metadata.sh`, `scripts/generate-metadata-index.sh`),
  along with the workflow that ran them and pushed generated files to `main`.

### Planned
- Phase 1.2: Skill templates for all 6 skill types (WORKFLOW, TOOL, DOMAIN, CREATION, ANALYSIS, INTEGRATION)
- Phase 1.3: LLM Application Development category setup
- Phase 2: High-priority skills (LangChain optimization, RAG pipeline patterns, SLSA compliance)
- Phase 3: Frontend domain expansion with React, Vue, accessibility, and performance prompts
- Phase 4: Extended coverage (Solid, Hono, OpenTelemetry skills)

---

## [2026-04-20]

### Removed
- Source material that could not be redistributed was removed, and the prompts that had been derived from it were replaced with original content.
- Cleaned up documentation (CLAUDE.md, README.md, REPO_MAP.md) to reflect new state.
- Regenerated `PROMPT_INDEX.json` and `PROMPT_INDEX.md` against the updated corpus.

---

## [2026-01-29]

### Added
- Phased implementation plan for new content recommendations (#193)
  - 4-phase plan spanning 6-8 weeks
  - 21 new items: 8 prompts, 8 skills, 5 documentation pieces
  - Dependencies and critical path mapping

---

## [2026-01-28]

### Added
- `domain-frontend-development/` with 15 Tier 4 prompts (#190)
  - React patterns, hooks, state management, testing, performance
  - Vue Composition API, Pinia state, testing
  - Accessibility: WCAG audit, ARIA patterns, screen reader testing
  - Performance: Core Web Vitals, bundle optimization
  - Testing: Jest unit testing, Playwright E2E
- Firebase account & group system validation prompt (#184)
- Science core research prompts (Session S1): 3 literature and hypothesis tools (#183)
- Psychology prompts suite (Sessions P1-P4): 12 prompts covering assessment, clinical support, behavior change, and organizational tools (#179-#182)
- Comprehensive repository review report with 15 findings and 21 recommendations (#186)
- Repository review reflection prompt v2.0 (#185)

### Changed
- Enforced naming conventions across repository (Initiative 5) (#192)
  - Standardized to snake_case for prompts
  - Standardized to kebab-case for skill directories
- Consolidated 22 duplicate agent names across repository (#189)
- Added standardized YAML frontmatter to all 72 commands (#188)
- Added README.md to 73 subdirectories for improved navigation (#191)
- Implemented quick wins from repository review report (#187)

---

## [2026-01-27]

### Added
- Image generation guide and techniques for visual content prompts (#177)
  - 8 core techniques: Terminology Steering, Grid Forcing, Constraint Redundancy, etc.
  - Templates for badge buddies, infographics, worksheets
- Nursing badge buddy prompt for critical care drips (#176)

### Changed
- **Migration Phase 8:** Final cleanup and field guide migration (#178)
- **Migration Phase 7:** Updated documentation for domain-* structure (#175)
- **Migration Phase 6:** Consolidated prompts into existing domain directories (#174)
- **Migration Phase 5:** Moved remaining prompts to domain directories (#173)
- **Migration Phase 4:** Renamed coding-agents to domain-agentic-resources (#172)
- **Migration Phase 3:** Moved meta-prompts to domain-prompt-engineering/ (#171)

### Removed
- Deleted archived analysis documents (COMPREHENSIVE_REPOSITORY_ANALYSIS, RESTRUCTURE_BRAINSTORM)

---

## [2026-01-26]

### Changed
- **Migration Phase 2:** Moved image generation prompts to domain-image-generation/ (#170)
- **Migration Phase 1:** Created new domain directory structure (#169)
  - Established domain-* naming convention
  - Created 20 domain directories

---

## [2026-01-25]

### Added
- Comprehensive migration plan for domain-based reorganization (#168)
- NON_CODING_QUICK_START.md and integration into documentation (#164)
  - 6 task type patterns: CREATE, LEARN, DECIDE, COMMUNICATE, IMPROVE, SIMULATE
  - 5 universal elements for non-coding prompts
- 7 domain appendices for non-coding prompting guide system (#165)
- Complete integration and testing for non-coding prompting guide system (#166)
- Implementation plan for non-coding prompting guide system (#163)

### Changed
- Upgraded 5 customer/market analysis prompts to Tier 1 quality (#162)
- Upgraded 5 additional business/analysis prompts to Tier 1 quality (#161)
- Upgraded 4 strategic business analysis prompts to Tier 1 quality (#160)
- Complete testing category upgrade to Tier 1 quality (#159)
- Section 9 (Integrate Archive Content) marked as completed (#167)

### Removed
- Deleted archived implementation plans and analysis reports from _archive/

---

## [2026-01-24]

### Added
- Phase 4: Documentation & Cleanup (#153)

### Changed
- Upgraded 5 additional testing prompts to Tier 1 quality (#158)
- Upgraded testing and business prompts to Tier 1 quality (#157)
- Addressed quality hierarchy across prompt categories (Finding 2.1) (#156)
- Standardized technique counts across documentation (Finding 3.2) (#155)
- Standardized naming conventions to snake_case (Finding 1.4) (#154)

### Removed
- Deleted claude-code-skills-main.zip and agents-main.zip archives

---

## Repository Statistics

### Current Totals

Counts below are produced by the repository's own generators and enforced in CI
(`scripts/generate_prompt_index.py`, `scripts/validate_technique_catalog.py`,
`domain-agentic-resources/inventory_counts.py`, `techniques/audit_technique_index.py`).

| Metric | Count |
|---|---:|
| Prompts indexed | 5,643 |
| Domains indexed | 44 |
| Prompts with frontmatter | 4,671 |
| Techniques (active) | 327 across 18 categories |
| Agentic resources (total) | 641 |
| — Skills | 330 |
| — Agents | 143 |
| — Commands | 115 |
| — Personas | 53 |

### Domain Directories

The authoritative, always-current list of domains and their prompt counts lives in
[`PROMPT_INDEX.md`](PROMPT_INDEX.md), regenerated by `scripts/generate_prompt_index.py`
and checked in CI. It is not duplicated here, where it would drift.

---

## Version History Notes

Entries dated before this repository's first public commit describe work carried out
during private development and are retained for context. Because the public repository
starts from a reviewed snapshot, those entries do not correspond to commits in this
repository's history, and the issue/PR numbers they cite refer to the private
development repository rather than to this one.

### Versioning Approach
- Dates are used instead of semantic versions since this is a documentation/prompt repository
- Major structural changes are tracked as migration phases
- Quality upgrades and new content additions are documented separately

---
