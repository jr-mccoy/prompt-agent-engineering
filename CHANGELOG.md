# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Fixed
- **The author packet named the collection it forbids the author to look for, and named its neighbours.** Two separate leaks in the authoring firewall, both found by scanning the *built* packet rather than by reading the templates. First: `NATURAL_TASK_BRIEF.md` ended the sentence "do not look for the library these tasks will be run against" by telling the author to record `saw_pae_metadata` — naming the collection in the same breath as forbidding them to find it, of a repository that is public. The same line also asked for a field the submission template does not accept (everything else author-facing uses `saw_collection_metadata`), so an author who followed the brief would have emitted a key the reviewer tooling does not read. Second, and larger: **the masking protocol removed a packet's own identity but left its cross-references to siblings intact.** The corpus writes those as slugs — ``- Android-specific cases (use `android-testing-patterns`)`` — so a packet scrubbed of itself still handed the author real resource names. The fourth masked-target draw made it undeniable: a referenced sibling was itself one of the 45, so one packet disclosed another packet's answer outright, and that is what tripped the full-title gate. Once fixed, **17 of the 45 packets** turned out to contain foreign references — the audit had been catching the rare visible case while the common case went through. `sanitize_body` now redacts any slug matching a known registry identifier whether or not that resource was drawn (the audit's cross-packet gate only looks at in-draw titles, so matching it exactly would have left every out-of-draw sibling name standing, including the one that started this), and separately redacts in-draw titles in whatever separator form the audit would recognise, which keeps the two halves of the firewall from disagreeing. Single-word names are excluded, as `identifying_phrases` already excluded them: a resource called "Risk" would turn every occurrence of the word into a redaction. **The operation survives the name** — ``(use `[identifier removed]`)`` still tells a reader a boundary exists and that something else handles the other case. Cost measured on the live draw: retention median **0.917** against 0.908 for the previous draw, guards preserved **45/45**. Both leaks are guarded by tests — `TestAuthorPacketNamesNothing` scans every author-facing file and filename for the collection name and asserts the provenance key matches the template, and `TestForeignReferenceRedaction` covers slug forms, public-ID tails, separator variants, the own-name exclusion and the single-word rule. **This is the second real defect the rotating-seed CI check has found**, after the guard-preservation false positive on a resource whose title reads like a safety heading; neither would have appeared in a fixed fixture. See the 2026-09-03 amendment to ADR-0041.

### Changed
- **Prompt caching is enabled on the paid path, and the token accounting it depends on is fixed.** The sealed run is 1,800 participant trials, two of whose four conditions are agentic tool loops with a 40-turn budget; a loop resends its transcript every turn, so input cost grows with the square of the turn count. Priced with no caching the run was ~$1,088 at 10 average turns and **$11,239** at the configured ceiling — inside a $2,500 budget only 17 turns fit, which would have forced `max_tool_turns` down and **handicapped the raw-repository baseline that PAE is measured against**, since Condition B needs more turns than Condition D precisely because it has no compiled bundle. The Anthropic adapter now uses the documented combination of both caching mechanisms across three of the four available breakpoint slots: explicit `cache_control` on the last tool definition (one breakpoint caches the whole catalog, because a cached prefix ends at the block the marker sits on), explicit `cache_control` on the system prompt, and the **top-level** `cache_control` field for the rolling conversation breakpoint, which the API walks forward as the conversation grows. The 5-minute TTL is used, not the 1-hour one — writes at 1.25× base input rather than 2×, and a run working through trials back to back does not need the longer window. OpenAI needs no opt-in and `prompt_cache_options.mode` is left unset. **Caching is a default rather than a recorded experimental decision because it cannot move the result**: `cache_control` is request metadata, the prompt is byte-identical with and without it, and no analysis reads a cache counter — asserted directly by sending the same request both ways and diffing the payloads, not assumed. It is recorded in the plan hash (`limits.prompt_caching`) and the run manifest anyway. Two accounting defects surfaced and are fixed. `cost_usd` computed `uncached = input_tokens - cache_read_tokens`, which assumes the provider's total *includes* the cached part — true for OpenAI, **false for Anthropic**, which reports a partition; `Usage` now specifies the three input buckets as disjoint, each adapter normalizes to that, and `cost_usd` adds them without subtracting. And the OpenAI adapter read `cached_input_tokens` off `usage` when the Responses API nests the counters under `usage.input_tokens_details` as `cached_tokens` / `cache_write_tokens` — **reading a field that does not exist returns `None` silently**, so no cache was ever recorded and every cached token was billed at full rate; found by introspecting `ResponseUsage` in the pinned interpreter rather than trusting a field name. `ModelPrice` gains `cache_write_per_million`, because a cache write costs *more* than plain input and billing it at 1.0× understated an Anthropic run by the 25% premium. `estimate_trial_cost` gains `cache_reads`, defaulting to **False** and staying that way for the cost guard: a cache entry can expire between turns, so a ceiling that assumes hits is not a ceiling. `--dry-run` now prints both figures and labels which one to size a budget from and which one enforces it. Measured on the 30-task development schedule the estimate falls from **$217.68 to $100.50** — 54% on identical token volume — and scaled to the sealed run, the full 40-turn budget costs about **$2,072** instead of $11,239. **`max_tool_turns` therefore stays at 40**: it was not moved from taste in either direction, it stays where it was because the measurement stopped arguing for moving it. **One place where caching would have moved a reported number, and did not survive the check.** `total_tokens` is a reported secondary endpoint and the efficiency claim is a function of it; both `Usage.total_tokens` and `efficiency_by_condition` computed it as `input_tokens + output_tokens`, which once the buckets are disjoint **omits every cached token** — so identical work would report fewer tokens the moment caching was switched on, and omit a *different* share per condition, since Condition B's long agentic loops cache their transcript heavily and Condition D's shorter ones do not. That is enough to move, and conceivably to reverse the sign of, the efficiency claim from a billing-only change. Both now sum all four buckets, `efficiency_by_condition` reports `cached_input_tokens` and `cache_write_tokens` separately so a reader can see rather than infer how much was cached, and caching-invariance is asserted directly — the same 101,000 tokens of work reported once as uncached and once as mostly cache reads must give the same total and a lower cost. The defect had been harmless for exactly as long as the cache counters were always zero, which is the argument for landing caching before the freeze rather than after it. Pricing is re-pinned as of 2026-09-03 with real cache read and write rates for five models, adapters re-verified against the installed SDKs by introspection, and 35 new tests cover the wire shape, both providers' usage conventions, the fallback when a snapshot omits a cache rate, caching-invariance of the efficiency endpoint, and the hand-computed arithmetic in both directions. See ADR-0042.

### Added
- **`pae_eval plan` now separates warnings from failures.** `validate_plan` answers "can this plan produce a trustworthy number at all"; the new `plan_warnings` answers "what limitation will this run's report have to carry". Collapsing the two either blocks runs that are fine or buries caveats that are not. The case that prompted it: `assert_judge_family_separation` existed and was tested but **was called from nothing in the pipeline**, and `validate_plan` checked the judge's family only against the `primary` participant. The shipped plan pairs an Anthropic primary and an OpenAI robustness arm with an OpenAI judge — so the primary arm is cross-family and passes, while **the robustness arm is graded by its own family, silently**. That is not fixable by configuration: with two participant families and one judge, no single judge is cross-family to both, the harness has no per-arm judge routing, and `judge.second_judge` is carried in the plan but **read by no part of the judging pipeline**. Every runnable configuration therefore accepts one of three costs — a self-judged secondary arm, an explicit `allow_same_family` override, or a single participant family and no family-robustness check at all. The primary-arm clash stays a hard failure; the secondary-arm clash, a `second_judge` that buys nothing, a single-family participant set, and disabled prompt caching are reported as warnings by both `plan` and `plan --check`, in text and in JSON, so the choice is made while the plan can still change rather than discovered in the write-up. Recorded as an open decision in the private benchmark repository's go-live runbook.
- **PAE Engine `0.5.0.dev0` — the query-term bound rises from 64 to 256.** Phase 8A's development benchmark found the old bound rejecting *realistic* requests: a person describing a real problem in full prose — constraints, context, what they already tried — normalizes to 90–130 terms, and three of the thirty development tasks landed at 97, 106 and 113. Worse, the rejection was not graceful. `SearchEngine._normalized_query` raised `UsageError`, and that exception propagated out of Condition C and Layer A and **ended an entire evaluation run** at whichever trial reached it first; the first attempt died after 227 of 360 trials. The new bound comes from measurement, not from taste. 256 is the smallest candidate clearing the largest realistic query measured (125 terms) by better than 2×; 128 clears it by three terms, which is not a margin. **The security case is that this bound was never the load-bearing control — `MAX_QUERY_CHARS = 2000` is, and it is unchanged.** Against the true adversarial input (terms ranked by document-frequency *per character*, maximising posting-list work per byte sent) 2000 characters hold at most **340** distinct terms, so a 512-term cap could never bind at all. Measured against the real 5217-document corpus, search and route each cost ~99 ms / 4.1 MB at 64 terms, ~153 ms / 5.7 MB at 256, and ~173 ms / 6.1 MB at the character-implied ceiling of 340 — strongly sublinear, because scoring against the corpus dominates and eight high-frequency terms already cost ~48 ms. Moving 64 → 256 therefore buys realistic requests at **+54 ms and +1.6 MB worst case**. The bound is kept rather than removed because term length is a property of this corpus's vocabulary rather than an invariant: short high-frequency tokens exist here in quantity (`md`, `st`, `01`, `qa`) and 2000 characters of those pack 555 terms. Tests pin *bound − 1*, *bound*, *bound + 1*, a realistic long request, and that the character ceiling is still checked first. Ranking is untouched — no BM25F coefficient, stopword, normalization rule or router threshold changed, and Phase 4's regression floors are unaffected because no tuning case exceeds 11 normalized terms. The version advances because the Engine's observable accepted input changed; the commit SHA remains the authoritative evaluation identity.

### Added
- **PAE Engine `0.4.0.dev0` — an optional MCP server.** `pae mcp --repo <checkout>` serves one PAE checkout to an MCP client over **stdio**, behind the new optional `[mcp]` extra (`mcp>=2.1.1,<3`, MCP specification revision `2026-07-28`). **The base install is unchanged and still resolves to nothing but the standard library** — `dependencies` stays empty, and the only permitted conditional requirement is the SDK gated by `extra == "mcp"`, which CI now asserts explicitly rather than by the old "`Requires-Dist` must be empty" check (see ADR-0029). Four read-only tools — `pae_search_resources`, `pae_route_task`, `pae_get_resource`, `pae_compose_bundle` — each validate transport input, call **one existing Engine API**, project the result and map errors; nothing in `pae_engine/mcp/` ranks, routes, packs or decides what may be served, and an AST scan asserts the core imports no adapter or third-party code. **The repository is bound once at startup and is never a tool argument**: no schema exposes `repo`, `root`, `path`, `file`, `cwd`, `directory` or `checkout`, and a test enumerates the catalog to prove it. **A body crosses the wire exactly once** — `pae_compose_bundle` text is byte-identical to `ContextBundle.render_markdown()` and its structured output is the full audit projection *minus* `included[*].content`, which cut a measured 8k bundle from 31,478 to 17,962 wire bytes and, more importantly, stopped the SDK's auto-conversion from replacing the canonical Markdown (and its authority framing) with raw JSON. `pae_get_resource` returns a body only in the text channel, verbatim and whole, behind a deterministic framing block and checksum-derived boundary markers that claim no immunity to prompt injection. Serving policy is untouched: excluded resources return the Phase 3 identity stub and nothing more, metadata-only bodies are `content_refused`, techniques and tombstones are `no_addressable_content`, safety-gated bodies stay whole-or-absent. Error details are **allowlisted per code** and messages scrubbed, so no model-facing output carries the checkout root, a home directory, a traceback or an exception repr. The SDK dispatches sync handlers onto a thread pool, which made the lexical index a race: eight concurrent cold calls built it **eight times** (~11.7 s); a background warmup plus a double-checked first-build lock makes that **one build (~17 ms)**. Schema bounds are **imported from the Engine** (`MAX_QUERY_CHARS`, `MAX_LIMIT`, `MAX_ROUTE_LIMIT`, `MAX_BUNDLE_BYTES`, `MAX_MAX_RESOURCES`) and a committed catalog snapshot asserts they match, so the advertised contract cannot drift from the core. A byte-only budget acquires **no hidden token cap**. stdio only — no HTTP, no MCP resources, no MCP prompts, no operator tools — with a raw-byte stdout purity test plus a deliberately contaminated fixture proving the checker works. See [`pae-engine/docs/mcp.md`](pae-engine/docs/mcp.md), ADR-0028, ADR-0029, ADR-0030, ADR-0031 and ADR-0032.
- **`pae-engine/tests/run_mcp_diagnostics.py`** — measures latency and both result channels for `tools/list`, search at 10 and 100, route at 5 and 25, metadata and largest-body retrieval, and bundles at 8k/16k/32k, then asserts **zero body duplication**. A local command, not a CI step; its timings are observations, not gates.

### Added
- **PAE Engine `0.3.0.dev0` — budgeted context compilation.** `pae bundle --task "<task>"` (or one or more `--ref`) compiles whole verified resource bodies into a deterministic, budget-aware `ContextBundle`. The compiler **owns no `SearchEngine` and no `Router`** — it accepts explicit references, `SearchResults` or a `RouteDecision` and cannot re-run retrieval — and every body arrives through `Registry.content()`, so serving policy and SHA-256 verification stay Registry responsibilities. **Whole resource or absent:** there is no truncation, excerpt, heading-subset or summarization path anywhere in the phase, frontmatter is retained, and all 1,319 safety-gated records keep the `must_not_truncate` guarantee they declare. Techniques (336 records, no `source_path`), skill attachments (1,021 entries carrying no per-file checksum) and relationship edges never produce a body; each becomes one of nine closed omission reasons. **The token count is an estimate and says so** — `ApproximateTokenCounterV1` is `ceil(utf8_bytes/4)` with `exact = False`, calibrated against real BPE tokenizers over all 4,888 addressable bodies (corpus mean 4.367 bytes/token) where **no fixed divisor is a safe upper bound**: `bytes/3` holds on this corpus by a 2.8% margin and breaks outright on Korean, Arabic, base64, hex and emoji. The enforced guarantee is instead an **exact UTF-8 byte ceiling** on the canonical Markdown rendering, capped at 4 MiB, with `byte_ceiling_source` reporting which of `explicit`, `derived_from_default_estimator` or `engine_safety_ceiling` applied; a caller needing exactness injects a `TokenCounter`, whose name and version enter the bundle hash. Packing is **rank-preserving greedy** — measured over the 120-case regression set at 8k it retains the top hit **99.1%** of the time against 71.6% for 0/1 knapsack and 60.3% for score-per-token, which reach to rank 15–16 to fill space — and an **ambiguous** route gets exactly one promotion from the second close scope, which removes silent single-scope collapse (of the 6.2% residue at 8k, only **1.6%** had room to avoid it) at no cost to the top hit. Route status survives compilation: `weak` warns, `ambiguous` keeps `selected_scope` null, `no_route` returns a valid empty bundle, and all exit 0. A final validation loop re-renders the complete bundle and sheds the lowest-priority body until the emitted Markdown honours what the report claims, so no fixed wrapper constant is ever used. New public models `ContextBundle`, `BundleItem`, `OmittedItem`, `BudgetReport`, `Budget`, `TokenCounter` and `ApproximateTokenCounterV1`, a `pae-context-bundle/1` schema versioned independently of the registry contract, a reproducible `bundle_sha256` with no timestamp or absolute path in its input, and `pae-context-markdown/1` rendering that delimits bodies with collision-safe markers rather than code fences. `pae bundle` writes to **stdout only**. See [`pae-engine/docs/context-compiler.md`](pae-engine/docs/context-compiler.md), ADR-0024, ADR-0025, ADR-0026 and ADR-0027.
- **`pae-engine/tests/run_context_compiler_diagnostics.py`** — packs the committed regression tasks at 2k/4k/8k/16k/32k with the production renderer and counter, reporting non-empty rate, top-1 and top-3 retention, utilization, omission mix, ambiguous scope collapse and safety-gated inclusions. It exits non-zero if a guarded body is ever shortened or a rendered bundle exceeds the budget it reported — those two columns are assertions, not measurements. Like the Phase 4 runner it is **internal packing regression, not task-quality evaluation**, and uses no external tokenizer.
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
