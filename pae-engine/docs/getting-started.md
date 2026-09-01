# Getting started with the PAE Engine

A copy-paste walkthrough, from an empty directory to a verified resource body.

The Engine is not on PyPI. Version `0.1.0` is the in-tree pre-release version,
so every step below installs from a checkout.

## 1. Clone and install

```bash
git clone https://github.com/jr-mccoy/prompt-agent-engineering.git
cd prompt-agent-engineering

python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

pip install -e ./pae-engine
```

Nothing else is downloaded: the Engine declares no runtime dependencies.

```bash
pip check                          # no requirements to satisfy
pae --version
# pae 0.1.0 (registry contract pae-registry-record/1)
```

## 2. Point the Engine at a checkout

The wheel ships no corpus and no registry, so every command that touches the
catalogue needs to know which checkout to read.

```bash
pae where                          # from inside the checkout: found via ancestors
pae where --repo /path/to/checkout # explicit
PAE_REPO=/path/to/checkout pae where
```

`--repo` beats `PAE_REPO`, which beats the working directory and its ancestors.
An explicit source that holds no registry is an error (exit 3), never a reason
to quietly try the next one — otherwise an agent could believe it had queried
the checkout it named.

## 3. See what is in the registry

```bash
pae stats
```

Counts are reported by lifecycle, kind, maturity, serving policy and metadata
completeness. There is no single "prompt count": the registry holds six kinds,
and a bare total would misinform.

```bash
pae stats --json | python3 -m json.tool | head -30
pae stats --verify                 # recount the records; fails on drift
```

## 4. Resolve a resource

Three kinds of reference work: a UID, a current public ID, and a retired alias.

```bash
pae get technique:ST-01
pae get pae_014jhyq0rdyb
pae get technique:ST-01 --json
```

A retired public ID still resolves, and the answer says so — `ref_kind` comes
back as `alias`, with the alias that matched and the current ID beside it.
Silently answering a renamed resource as though nothing had changed would hide
the rename from you.

```bash
pae get some:retired/identifier --json | python3 -c \
  'import json,sys; r=json.load(sys.stdin)["resolution"]; print(r["ref_kind"], r["current_id"])'
```

## 5. Read a body

```bash
pae get <ref> --content            # raw bytes, byte-for-byte
pae get <ref> --content --json     # JSON envelope, strict UTF-8
```

Every content read verifies the registry's SHA-256 over the raw source bytes.
There is no way to skip that:

```bash
pae get <ref> --content | sha256sum
# matches the record's source.content_sha256
```

If you have edited a source file locally without regenerating the registry, the
read fails with exit 7 and tells you the file differs from what the registry
describes. No bytes are returned.

Bodies come back whole or not at all. There is no excerpt, head, tail or
byte-limit mode — many resources here carry guards and authorization gates that
stop working when they are cut in half.

## 6. Check the registry itself

```bash
pae validate-registry
pae validate-registry --verify-checksums   # also hashes every live source
```

This is the *consumer's* check: identity shape and uniqueness, aliases
disjoint from live IDs, relationship targets that resolve, source paths that
stay inside the repository, and a summary that agrees with the records. It is
not a second copy of `python3 scripts/generate_registry.py --check`, which is
the *producer's* check and re-derives the corpus.

Failures are collected rather than reported one at a time, and the command
exits 9.

## 7. Use it from Python

```python
from pae_engine import Repository

registry = Repository.discover().registry()

record = registry.get("technique:ST-01")
print(record.kind, record.serving_policy, record.has_body)

if record.content_available:
    print(registry.content(record.id).text())
```

Streaming keeps memory bounded; opening the registry reads nothing until you
ask a question:

```python
for record in registry.records():
    if record.kind == "skill" and record.content_available:
        print(record.id)
```

## Scripting against it

Exit codes are the contract, and they distinguish cases that need different
responses:

```bash
pae get "$REF" --json > record.json
case $? in
  0) echo "got it" ;;
  2) echo "that reference is malformed — fix the string" ;;
  4) echo "no such resource — search for the right one" ;;
  5) echo "withheld by serving policy" ;;
  6) echo "real resource, but it has no body of its own" ;;
  7) echo "source integrity problem — do not trust this checkout" ;;
esac
```

On any nonzero exit, stdout is empty and the explanation is on stderr — as one
JSON object when `--json` is set.

## What is not here yet

`pae search`, task routing, ranking, context compilation, token counting and
MCP are later phases. Nothing in this release stubs them out or guesses at
their shape.
