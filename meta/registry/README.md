# PAE Registry

The durable, normalized catalog of this repository's **first-class AI resources**:
prompts, techniques, skills, agents, commands and personas.

Generated and validated by [`scripts/generate_registry.py`](../../scripts/generate_registry.py).

```bash
python3 scripts/generate_registry.py --dry-run   # propose and report; writes nothing
python3 scripts/generate_registry.py --write     # regenerate the generated artifacts
python3 scripts/generate_registry.py --check     # CI: current, valid, identity stable
python3 scripts/generate_registry.py --summary   # print the summary JSON
```

---

## What this is, and what it is not

The registry is **not** [`PROMPT_INDEX.json`](../../PROMPT_INDEX.json). That index is a
mixed artifact population which both **includes** things that are not resources
(bundled `references/`, `assets/`, `cards/` files) and **omits** things that are
(first-class resources in the root toolkits). See
[ADR-0007](../adr/0007-index-is-not-the-registry.md).

The registry answers a different question: *what addressable resources does this
repository actually contain, what is each one's stable identity, where did it come
from, and what may be done with it?*

---

## Files

| File | Maintained by | Purpose |
|---|---|---|
| `identity.tsv` | **hand-reviewed** | The frozen public identity of the corpus. One row per resource. |
| `aliases.tsv` | **hand-reviewed** | Retired public IDs, permanently resolvable to their UID. |
| `relationships.tsv` | **generated, reviewed** | Move history, replacement edges and copy edges, with the file each was derived from. |
| `overrides/*.yaml` | **hand-maintained** | Reviewed governance that generation must not infer on its own. |
| `schemas/*.json` | **hand-maintained** | The published contract for every artifact above and below. |
| `registry.jsonl` | *generated* | One normalized record per line, sorted by UID. |
| `registry-summary.json` | *generated* | Counts by kind, lifecycle, maturity, policy, provenance, licence, diagnostics. |
| `diagnostics.jsonl` | *generated* | Parse failures, minimal records, skipped relations. Sorted and deterministic. |

**Never hand-edit a generated file.** CI regenerates all three and fails on any
byte difference, so a manual edit is caught rather than silently kept.

---

## First-class membership

Membership needs two independent agreements: the file sits under an **approved
root**, and it matches a **shape detector** for exactly one kind. Roots are an
explicit allowlist — the 44 `domain-*` directories plus five root toolkits — never
unconstrained recursion.

**Exclusions are anchored path prefixes, never bare directory names.** This is not a
style preference. `domain-agentic-resources/agents/documentation/` is a category of
documentation-*writing* agents; `domain-agentic-resources/documentation/` is
documentation *about* resources. A blocklist on the segment name `documentation`
cannot tell them apart and silently deletes six genuine resources.

Detector precedence, first match wins:

1. anchored non-resource prefix (samples, design bundles, vendored pointer trees)
2. `SKILL.md` → **skill**
3. bundled component directory (`references/`, `assets/`, `scripts/`, …) → attachment
4. meta-doc filename (`README.md`, `ARCHITECTURE.md`, …)
5. ALL-CAPS documentation at a toolkit root
6. `personas/` → **persona**
7. `agents/` → **agent**
8. `commands/` → **command**
9. any other file inside a skill bundle → attachment of that skill
10. any remaining Markdown under an approved root → **prompt**

Techniques are not file-backed: they come from `techniques/MASTER_TECHNIQUE_INDEX.md`
through the repository's existing parser.

Discovery **fails** on a multi-kind match, a duplicate candidate path, or an approved
root that does not exist. Metadata may degrade; identity may not.

---

## UID vs public ID

Every resource carries two identifiers, and they do different jobs.

```
uid  pae_k3m9x7q2vb41                                    immutable, internal
id   prompt:reasoning-craft/reasoning-moves/inversion    human-readable, may change
```

**The UID never changes and is never recycled.** It is seeded deterministically at
birth — `sha256(kind + NUL + birth_path)`, first 60 bits, Crockford base32 — so a
pre-freeze dry run is reproducible. After the freeze commit, `identity.tsv` is
authoritative and the UID is never recomputed from a moved path.

**The public ID may change** when a resource moves to a new semantic home. The
repository has already executed 236 identity-preserving moves in one
reorganization, and domain re-carving is an ongoing activity. Under a
single-identifier scheme a moved resource would keep a name that lies about where
it lives, forever. Splitting the two lets the name be corrected without breaking
identity. See [ADR-0010](../adr/0010-uid-and-public-id.md).

`birth_path` is the path a resource was *first* recorded at, resolved through the
move map — not necessarily where it lives today.

---

## Aliases

When a public ID changes, the old value is written to `aliases.tsv` and stays
resolvable forever. A retired public ID is **never reused** by any resource, and can
never collide with a current one. CI enforces both.

---

## Tombstones

A tombstone is a historical resource that no longer exists on disk, recorded as a
`DELETED` row in [`meta/REORG_MAP.tsv`](../REORG_MAP.tsv). It keeps its own UID and
public ID, carries `maturity: deprecated` and `serving_policy: metadata_only`, and
points at whatever replaced it.

A tombstone is a **different identity** from its replacement. An old reference
resolves to an explanation, never silently to a different resource.

The four reorganization semantics stay distinct and are never flattened into one
alias relation:

| Semantics | Meaning |
|---|---|
| `previous_path` | identity preserved; the resource lives somewhere else now |
| `superseded_by` | a **different** resource replaced this one |
| `merged_into` | this content was folded into another identity |
| `split_into` | this identity dispersed across a collection |

Replacement targets are typed: `resource` (a live registry record), `document` (a
file that exists but is not a resource, such as a README that absorbed the content),
or `collection` (a directory). Every target must resolve; a dangling edge is a hard
error.

---

## Copies and canonicals

Self-contained bundles carry copies of prompts that also live in a canonical domain.
Every physical copy gets **its own record** with `copy_of` pointing at the canonical,
and the canonical carries the reverse `copies` list.

Copy relations come from [`meta/VENDORED.tsv`](../VENDORED.tsv) and from **nowhere
else**. They are never inferred from content similarity, because the repository
deliberately contains adapted near-duplicates — `childrens-book-studio/design-bundle/agents/`
and `agentic-system-factory/samples/` among them — that are genuinely different
things and must not be collapsed. See [ADR-0012](../adr/0012-one-record-per-copy.md).

---

## Quality vs maturity

They are different axes and neither implies the other
([ADR-0005](../adr/0005-quality-and-maturity-are-separate.md)).

**Maturity** is the registry's own lifecycle state: `experimental`, `candidate`,
`stable`, `deprecated`. Structural validity does not make something `stable`.

**Quality** is a list of *typed assertions*, never an ordered scale:

```json
"quality": [
  { "scheme": "intended-use", "value": "model-testing", "evidence": "frontmatter:intended_use" },
  { "scheme": "guard-level",  "value": "strong-guard",  "evidence": "body-marker:STRONG-GUARD" }
]
```

`Tier 1`, `Gold Standard`, `STRONG-GUARD` and `model-testing` are four unrelated
concepts — a rubric level, an honorific, a guard intensity and a usage disclaimer —
and nothing in this repository defines an ordering among them. Separate `scheme`
namespaces keep them un-comparable by construction.

**No quality tier is asserted for any resource.** `PROMPT_QUALITY_STANDARDS.md`
defines the tier scheme, but no resource records a value for it. Inferring one from
document structure would be fabricating a rubric score.

---

## Review and evaluation

```
review_status : unknown | unreviewed | reviewed | needs_review
eval_status   : unknown | untested | passing | failing | partial
```

Migration set every resource to **`unknown`**, never `unreviewed` or `untested`.
Absence of a review record is not evidence that no review happened; `unreviewed` and
`untested` are positive claims and must be recorded by a human, through
`overrides/`. At migration they are used zero times.

---

## Licensing and provenance

```
origin  : project_native | vendored | adapted | unknown
license : resolved | inherited | unresolved
```

Every value comes from repository evidence — frontmatter `metadata.upstream*` keys, a
`license:` field, [`THIRD_PARTY_NOTICES.md`](../../THIRD_PARTY_NOTICES.md), or the
root [`LICENSE`](../../LICENSE).

**Known limitations, recorded rather than papered over.** `THIRD_PARTY_NOTICES.md`
§3 and §4 state plainly that no per-file attribution map is maintained for the
`wshobson/agents` and `daymade/claude-code-skills` imports. Those resources are
marked `adapted` with a `notes_ref` and nothing more. A per-file upstream mapping is
**not** invented, and licensing is **never** inferred from content similarity.

Vendored files are never modified. The eight Google skills keep their upstream
`license:` pointer verbatim; the registry resolves it in metadata and leaves the
byte-identical body alone.

---

## Serving policy

```
standard        full content may be served
safety_gated    servable only whole — guard sections must never be truncated
metadata_only   title, description and ID only; body withheld
excluded        not served at all
```

**The fail-closed default is `metadata_only`.** Generation always populates the
field, so absence means a bug — and a bug must withhold content, not leak it.

Values are computed from deterministic triggers and every trigger is recorded in
`basis`. The most restrictive match wins. Triggers include
`intended_use: model-testing`, the `STRONG-GUARD` marker, a Safety Block heading,
safety-sensitive domains, authorized-offensive bug-bounty content, degraded metadata,
deprecated maturity, and unresolved third-party licensing.

Safety-gated records carry a `guard_preservation` block so a future context compiler
knows the disclaimers are load-bearing. **Nothing is `excluded` automatically** —
exclusion is a maintainer decision. No serving or truncation behaviour is implemented
in this phase.

---

## Null and unknown semantics

One rule, applied everywhere:

| State | Representation |
|---|---|
| not applicable to this kind | key omitted |
| applicable, no evidence | `"unknown"` |
| known empty collection | `[]` |
| known empty at-most-one relation | `null` |
| present but failed to parse | value omitted + a `diagnostics` entry |

A field is never both "missing because unknown" and "missing because not
applicable".

---

## Malformed and incomplete sources

| Class | Behaviour |
|---|---|
| identity cannot be trusted | **generation aborts** |
| frontmatter present, YAML invalid | degraded record, `metadata_only`, `frontmatter_parse_failed` diagnostic |
| no frontmatter at all | minimal record, title derived from the first H1 or the slug |

Degraded records do **not** fall back to the legacy index's regex scavenger: that
produces partial metadata indistinguishable from parsed metadata. Minimal records do
**not** synthesize a description from the first paragraph. Every derived value is
listed in `derived_fields` so a consumer can tell it from an authored one.

---

## ID freeze

The commit that first landed a reviewed `identity.tsv` on `main` is the freeze point.
After it:

- a UID never changes, is never deleted and is never recycled;
- a `birth_path` never changes;
- a public-ID change requires a matching row in `aliases.tsv`;
- removing a resource means `maturity: deprecated` plus a replacement edge, never
  deleting the row.

CI enforces all four, plus uniqueness, ledger↔record bijection, schema validity and
byte-identical regeneration.
