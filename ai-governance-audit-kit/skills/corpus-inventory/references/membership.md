# Membership: how a file becomes a resource

## Precedence, in order

`classify()` applies these most-specific-first. Exactly one fires.

| # | Test | Result |
|---|---|---|
| 1 | not under any configured root | `outside_root` |
| 2 | matches an anchored non-resource prefix | `non_resource_prefix` |
| 3 | basename is a meta-document filename | `meta_document` |
| 4 | any parent segment is a component directory | `bundled_component` |
| 5 | not a `.md` file | `not_markdown` |
| 6 | first matching kind detector | that kind |
| 7 | the fallback detector | the fallback kind |

Order is the whole design. A `README.md` inside `skills/x/references/` is a
meta document (3) rather than a bundled component (4), and that is correct —
both exclude it, and the reason recorded is the more specific one.

## The invariant: anchored prefixes, never bare segments

**Enforced in `validate_config`, not left as a comment.** A
`non_resource_prefixes` entry with no `/` is rejected, and so is one without a
trailing `/`.

The worked example is from the parent repository, and it is why the rule
exists rather than being a stylistic preference:

- `domain-agentic-resources/agents/documentation/` is a category of
  documentation-**writing** agents. Six genuine first-class resources.
- `domain-agentic-resources/documentation/` is documentation **about**
  resources. Not resources.

A bare-segment blocklist on `documentation` deletes the first while intending
to remove the second. Prefixes can tell them apart; segment names cannot. The
test `test_an_anchored_prefix_excludes_only_its_own_subtree` pins exactly this
case.

The trailing slash matters for a second reason: `skills/_vendor` without it
would also match `skills/_vendored-notes.md`, a sibling whose name merely
starts the same way.

## Component directories are segments, and that is consistent

`component_dirs` is a set of bare names — `references`, `assets`, `scripts` and
so on — and that is not a contradiction of the rule above. A component
directory is recognised by being *a segment beneath a resource bundle*, which
is a structural relationship rather than a location. `skills/x/references/y.md`
is a component of `skills/x` wherever `skills/x` sits in the tree.

Exclusions are about **location**, which is why they must be anchored.
Components are about **structure**, which is why they are not.

## Kind detectors

An ordered list. Each entry names a `kind` and one test:

| Key | Test |
|---|---|
| `basename` | the file's basename equals this exactly |
| `path_prefix` | the path starts with this |
| `fallback` | matches anything remaining |

`validate_config` requires **exactly one** fallback and requires it to be
**last**. A fallback anywhere else silently shadows every detector after it,
and a corpus where everything is classified `prompt` looks like a successful
run.

## Identity

Every resource receives:

- **`uid`** — `uid_for(kind, path)` from `scripts/pae_registry/identity.py`,
  imported and not reimplemented. It is `sha256(kind + "\0" + birth_path)`
  folded to 60 bits of Crockford base32, depends only on kind and path, and
  takes two strings rather than a repository. A second implementation would
  eventually disagree with the Engine that has to open the handback.
- **`id`** — `<kind>:<scope_prefix>/<path components>/<slug>`. The shape and
  the component normalisation are the parent repository's; the scope comes from
  `handback.scope_prefix` in config, because a client tree has no `domain-`
  prefixes to strip. A skill is named by its bundle directory, every other kind
  by its filename stem.

Two artifacts normalising to the same public ID is a **Gate 0 block**, not a
warning: a handback carrying one fails `pae validate-registry` with `duplicate_public_id`,
and finding that out at the end of an engagement is the wrong time.

## Exclusion reasons, and what each one tells you

| Reason | What a high count means |
|---|---|
| `outside_root` | the roots are narrower than the corpus; check with the owner |
| `non_resource_prefix` | deliberate exclusions; every one should be defensible |
| `meta_document` | normal — READMEs and changelogs are not resources |
| `bundled_component` | normal — a skill's references and scripts belong to it |
| `not_markdown` | normal, unless the corpus keeps prompts in another format |

Read the exclusion counts **before** the resource count. A partition where most
files are excluded is a finding about the config, the tree, or both.
