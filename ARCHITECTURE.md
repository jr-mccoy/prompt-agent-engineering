# Architecture

How **Prompt & Agent Engineering (PAE)** is built today, and where the
productization boundary sits.

Everything under *Current state* exists and is exercised by CI. Everything under
*Planned* is **not implemented**. If a claim here and the repository disagree,
the repository is right — file an issue.

---

## The two layers

| Layer | What it is | Status |
|---|---|---|
| **PAE Registry** | The governed resource corpus, its indexes, schemas, and a normalized machine-readable metadata layer | Corpus, indexes and normalized registry records **exist** (`meta/registry/`) |
| **PAE Engine** | An installable Python package: identity resolution, metadata retrieval, policy-gated content serving, and consumer-side registry validation | Package, Python API and `pae` CLI **exist** (`pae-engine/`) |

The Engine is real but early. It resolves, inspects and serves; it does **not**
search, route, compile context, or speak MCP. Those remain planned, and
documentation must not imply otherwise. The package is not published to PyPI.

---

## Current state

### Resource corpus

Resources live in `domain-*/` directories plus a set of self-contained toolkits
at the repository root (`agentic-system-factory/`, `continuity-kit/`,
`ai-investment-research-toolkit/`, `childrens-book-studio/`,
`sourced-nonfiction-studio/`, `financial-records-toolkit/`,
`portable-prompt-system/`).

Resource kinds present today: prompts, prompt-engineering techniques, skills,
agents, commands, personas, authoring guides, and whole agentic-system designs.

### Indexes

| Artifact | Generator | Contents |
|---|---|---|
| `PROMPT_INDEX.json` / `PROMPT_INDEX.md` | `scripts/generate_prompt_index.py` | Metadata for every Markdown file under the `DOMAIN_DIRS` allowlist |
| `PROMPT_INDEX_LEARNER_AUDIENCE.json` | hand-maintained | Audience enrichment joined to the index on `path` |
| `techniques/MASTER_TECHNIQUE_INDEX.md` | hand-maintained, machine-audited | The technique catalog: IDs, definitions, deprecations, merges |
| `meta/REPOSITORY_FACTS.json` | `scripts/generate_repo_facts.py` | Canonical counts plus the membership rule for each one |
| `meta/xref_baseline.json` | `scripts/check_frontmatter_references.py` | Ratchet baseline of known-bad frontmatter cross-references |
| `meta/REORG_MAP.tsv` | hand-maintained | Every file a reorganization moved or removed, and where it went |
| `meta/VENDORED.tsv` | hand-maintained | canonical → byte-identical copy pairs |

`PROMPT_INDEX.json` is **not** a clean resource registry. Its entry total is a
mixed population: domain prompts, slash commands filed inside domain
directories, agentic resources, and bundled component files (a parent
resource's `references/`, `assets/`, `cards/` and similar). Every count the
project publishes therefore comes from `meta/REPOSITORY_FACTS.json`, which
states what each category actually counts.

### Validators

All of these run in `.github/workflows/validate.yml`:

- generated indexes are current (`generate_prompt_index.py` + `git diff`);
- agentic inventory counts match the filesystem (`inventory_counts.py --check`);
- technique-index integrity (`techniques/audit_technique_index.py`);
- technique claims across the authoring docs (`scripts/validate_technique_catalog.py`);
- command frontmatter (`domain-agentic-resources/commands/validate_command_frontmatter.py`);
- naming conventions (`scripts/validate_naming_conventions.py --ci`);
- Markdown body links resolve (`scripts/check_relative_links.py`);
- frontmatter cross-references, ratcheted (`scripts/check_frontmatter_references.py --check`);
- repository facts and published count declarations (`scripts/generate_repo_facts.py --check`);
- vendored copies still match their canonicals (`scripts/check_vendored_copies.py`);
- the reorg map is fully applied (`scripts/apply_reorg_map.py --check`);
- shell and Python syntax across the repository;
- unit tests for `continuity-kit/` and `ai-investment-research-toolkit/`.

`.github/workflows/structure.yml` additionally derives an allowlist of permitted
top-level directory *shapes* from the layout and fails on anything unexpected.

`.github/workflows/engine.yml` covers the Engine: unit tests on the declared
Python floor and the current default, wheel and sdist builds, `twine check`,
licence-sync between the repository and the packaged copy, an assertion that no
registry data is bundled, a clean-environment wheel install with a
zero-runtime-dependency check, and smoke tests driving the installed `pae`
binary from outside the checkout. It triggers on changes to `pae-engine/**`,
`meta/registry/**`, `scripts/pae_registry/**` and the workflow itself, so a
registry change cannot break the runtime unnoticed.

### Routing

Routing today is **documentation**, not code. `CLAUDE.md` is the single
canonical deep routing reference; `AGENTS.md` and `START_HERE_FOR_AI.md` are
thin bootstraps that point at it and deliberately keep no routing table of their
own. This replaced three partially-contradictory routers.

### Generated-count control plane

Any repository count published in primary documentation lives inside a machine
-detectable generated block:

```text
<!-- REPO_FACTS:BEGIN name=counts -->
<!-- REPO_FACTS_DECLARATION: {"skills": 330, ...} -->
...generated prose...
<!-- REPO_FACTS:END name=counts -->
```

`scripts/generate_repo_facts.py --check` fails if a required block is missing,
if a declaration is missing, if a published value disagrees with computed
truth, or if the block body was hand-edited. A missing marker is an error, never
a pass. The design reuses the repository's existing `INVENTORY_COUNTS`
declaration pattern.

---

## Architectural constraints discovered

These are properties of the repository that any productization has to work
with, not problems to be tidied away.

**Resource schemas are heterogeneous, on purpose.** Domain prompts carry
`title`/`category`/`techniques`/`tags`; Claude-style skills carry
`name`/`description`/`metadata`; agents carry `name`/`description`/`model`;
commands carry their own shape. These are not going to be unified by rewriting
the corpus — a normalization layer will adapt them.

**Some resources are byte-identical vendored copies.** Eight Google
`android/skills` and Anthropic's `skill-creator` are vendored verbatim at pinned
upstream commits under Apache-2.0, inside an otherwise MIT repository
(`THIRD_PARTY_NOTICES.md`). They must not be edited to add project metadata, so
project-owned metadata cannot live in the source files for those resources.
Separately, `meta/VENDORED.tsv` records 154 intentional canonical → copy pairs
that keep the self-contained toolkits standalone.

**Top-level layout is gated.** `structure.yml` permits only `domain-*`, the
bundle suffixes (`*-toolkit`, `*-kit`, `*-studio`, `*-library`, `*-system`,
`*-factory`), `authoring`/`scripts`/`techniques`/`tests`/`meta`, and the one
literal `pae-engine`. A new top-level product directory requires a deliberate,
reviewed amendment — the `pae-engine` case was added as a single literal name
rather than a `pae-*` pattern, so the gate stays a contract (ADR-0001).

**Root `tests/` already means something.** It holds the prompting-technique
comparison experiments (`established/`, `experimental/`, `results/`, scoring
rubric) — not a Python test suite. Engine tests will live inside the engine
directory instead.

**Resource kind is not derivable from location.** Roughly sixty first-class
agents, skills, and commands live outside `domain-agentic-resources/` — in the
root toolkits and in `domain-deep-analysis/commands/`. Ten of those are
currently indexed as if they were prompts.

**Paths move.** `meta/REORG_MAP.tsv` records 287 relocations. Of those, 236 are
identity-preserving moves; 51 are deletions that point at a *different*
surviving resource (`superseded-by`, `merged-into`, `split-into`). Any future
identity scheme has to keep those two relations apart.

**Cross-reference debt is real and is being ratcheted, not hidden.** Of 12,190
frontmatter references, 1,231 either fail to resolve from the repository root or
use a noncanonical form. They are enumerated in `meta/xref_baseline.json`; CI
fails on new ones.

---

## PAE Registry

Built. `meta/registry/` holds a normalized, machine-readable record per
first-class resource, generated from the corpus rather than replacing it, and
regenerated by [`scripts/generate_registry.py`](scripts/generate_registry.py).

- **Identity** is an immutable `uid` plus a mutable human-readable public `id`,
  with retired public IDs kept as permanent aliases (ADR-0010). Identity is
  frozen in `meta/registry/identity.tsv` and enforced by CI.
- **Membership** is explicit approved roots plus shape detection, with
  anchored-prefix exclusions (ADR-0011).
- **Adapters** read each native frontmatter shape and emit one common schema.
  Source files are not rewritten (ADR-0004).
- **Relationships** keep identity-preserving moves distinct from
  `superseded_by` / `merged_into` / `split_into`, and copy relations come only
  from `meta/VENDORED.tsv` (ADR-0012).
- **Techniques** are generated by reusing the existing catalog parser.
- **Quality** (the corpus's own Tier 1/2/3, Gold Standard, STRONG-GUARD labels)
  and **maturity** (`experimental` / `candidate` / `stable` / `deprecated`) are
  separate axes, with `experimental` the conservative migration default
  (ADR-0005).

See [`meta/registry/README.md`](meta/registry/README.md).

---

## PAE Engine

Built. `pae-engine/` holds an installable package that reads the registry and
serves from it. It is the first executable PAE product.

```text
PAE Registry  →  pae_engine (Python API)  →  pae (CLI)
```

| | |
|---|---|
| distribution | `prompt-agent-engineering` (unpublished, `0.1.0`) |
| import | `pae_engine` |
| console | `pae` |
| Python | `>= 3.10` |
| runtime dependencies | none |

**Commands.** `pae --version`, `pae where`, `pae stats`, `pae get <ref>`
(`--content`), `pae validate-registry` (`--verify-checksums`). There is no
`pae search` yet.

**The registry is the boundary.** The Engine reads
`meta/registry/registry.jsonl` and `meta/registry/registry-summary.json`, and
nothing else. It never reads the reviewed ledgers, diagnostics, overrides,
`PROMPT_INDEX.json`, `REORG_MAP.tsv` or `VENDORED.tsv`, and never imports
`scripts/pae_registry/` — a test asserts the import boundary so it cannot
regress into a second source of truth (ADR-0020).

**A checkout is required** (ADR-0018). The wheel carries no corpus and no
registry; discovery is `--repo`, then `PAE_REPO`, then the working directory
and its ancestors, then failure. Nothing is downloaded, and an explicit source
never silently falls through to another.

**Read-only, offline, and data-not-instructions** (ADR-0019). Content is served
whole or not at all, every read verifies the registry's SHA-256 with no bypass,
unknown serving policies fail closed to `metadata_only`, and every registry
path is treated as untrusted input before a file is opened. Tests walk the
installed package's AST to assert there is no filesystem write, subprocess,
socket or `eval` anywhere in the runtime.

See [`pae-engine/README.md`](pae-engine/README.md) and
[`pae-engine/docs/getting-started.md`](pae-engine/docs/getting-started.md).

---

## Planned

### Search and routing (next)

Deterministic metadata search, task routing and ranked retrieval, built on the
`Registry` object the Engine already exposes. Search consumes
`Registry.records()`, `load_all()`, `get()`, `resolve()` and `stats()`; it does
not open `registry.jsonl` itself, so there stays one implementation of reading
the registry.

Nothing in the Engine today guesses at that shape: there are no ranking
methods, no index files and no caches, because the access patterns that would
justify them are exactly what search has yet to establish.

### Beyond search

Token-budgeted context compilation, with a serving-policy gate that refuses to
emit a bundle rather than truncate required safety material out of a
safety-gated resource. A read-only MCP surface calling the same library
functions as the CLI. Reproducible evaluation. Optional extras (`[mcp]`,
`[eval]`, `[tokenizers]`) carry anything the standard library cannot.

See [`ROADMAP.md`](ROADMAP.md) for sequencing and [`meta/adr/`](meta/adr/) for
the decisions behind these choices.
