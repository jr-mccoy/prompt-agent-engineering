# ADR-0017 — The Engine is `prompt-agent-engineering` / `pae_engine` / `pae`

## Status

Accepted. Implemented in Phase 3. Amends the illustrative layout in
[ADR-0001](0001-engine-location.md).

## Context

The Engine needs three names, and they do not have to match:

- a **distribution** name, for PyPI and `pip install`;
- an **import** name, for `import ...`;
- a **console** name, for the shell.

The obvious choice was `pae` for all three. It is short, it is what people
already call this project, and a single name is easier to remember than three.

It is not available. An unrelated project on PyPI owns the `pae` import
namespace, so `import pae` in an environment holding both packages is
ambiguous at best and silently wrong at worst — the kind of failure that
surfaces as a confusing `AttributeError` inside somebody else's code. Package
inspection during the Phase 3A design checkpoint confirmed that project does
not, however, install a `pae` console entry point.

## Decision

Split the three names:

```text
distribution: prompt-agent-engineering
import:       pae_engine
console:      pae
version:      0.1.0
python:       >= 3.10
```

`import pae` is rejected outright rather than attempted and worked around.

The short console command is kept, because that is where the name actually
buys something — an agent or a person types `pae get ...` constantly and
imports the package once.

Python 3.9 is not supported. It reaches end of life, and the code uses 3.10
syntax (`X | Y` unions, `Path.is_relative_to` behaviour relied on throughout
the path-containment checks).

Nothing is published in Phase 3. `0.1.0` is an in-tree pre-release version, and
the README says so. Distribution-name availability is rechecked immediately
before any future publication step, never assumed from this record.

## Consequences

- The Engine can be installed alongside the unrelated `pae` project without
  either shadowing the other.
- Documentation must be explicit that the import name differs from the command
  name, because that is genuinely surprising.
- The three names are public API from `0.1.0` onwards — the full pre-release
  surface is listed in [`pae-engine/README.md`](../../pae-engine/README.md) —
  so changing any of them later is a breaking change and needs its own ADR.
- A future publication step must re-verify that `prompt-agent-engineering` is
  still free on PyPI. This ADR is not evidence that it is.
