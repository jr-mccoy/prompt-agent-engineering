# License Compatibility Matrix

## Quick Reference

### License Categories

**Permissive** — Minimal restrictions, compatible with most projects:
- MIT, BSD-2-Clause, BSD-3-Clause, Apache-2.0, ISC, Unlicense, 0BSD

**Weak Copyleft** — Must share modifications to the library itself:
- LGPL-2.1, LGPL-3.0, MPL-2.0

**Strong Copyleft** — Must share the entire combined work:
- GPL-2.0, GPL-3.0

**Network Copyleft** — Must share even for network/SaaS usage:
- AGPL-3.0

## Compatibility Matrix

Can the **row** license depend on the **column** license?

| Your Project ↓ / Dependency → | MIT | Apache-2.0 | LGPL-2.1 | MPL-2.0 | GPL-2.0 | GPL-3.0 | AGPL-3.0 |
|-------------------------------|-----|-----------|----------|---------|---------|---------|----------|
| **Proprietary/Commercial** | Yes | Yes | Yes* | Yes* | No | No | No |
| **MIT** | Yes | Yes | Yes* | Yes* | No | No | No |
| **Apache-2.0** | Yes | Yes | Yes* | Yes* | No | Yes** | No |
| **LGPL-2.1** | Yes | Yes | Yes | Yes* | No | No | No |
| **GPL-2.0** | Yes | Yes | Yes | Yes | Yes | No | No |
| **GPL-3.0** | Yes | Yes | Yes | Yes | Yes*** | Yes | No |
| **AGPL-3.0** | Yes | Yes | Yes | Yes | Yes*** | Yes | Yes |

*\* Dynamic linking only; static linking triggers copyleft for LGPL. MPL requires sharing modifications to MPL-licensed files only.*
*\*\* Apache-2.0 is compatible with GPL-3.0 but NOT GPL-2.0 due to patent clause.*
*\*\*\* GPL-2.0 code can be used in GPL-3.0 projects only if licensed as "GPL-2.0-or-later".*

## Decision Flowchart

```
Is your project proprietary/commercial?
├── Yes → Only use: MIT, BSD, Apache-2.0, ISC, Unlicense
│         Carefully review: LGPL (dynamic linking OK), MPL (file-level copyleft)
│         Avoid: GPL, AGPL
│
└── No (open source) → What license is your project?
    ├── Permissive (MIT/BSD/Apache) → Can use any permissive dependency
    │   Avoid GPL/AGPL dependencies (they would force relicensing)
    │
    ├── GPL-3.0 → Can use almost anything except AGPL-3.0
    │
    └── AGPL-3.0 → Can use anything
```

## Common Gotchas

### 1. "No License" Is Not "Free to Use"
If a dependency has no LICENSE file, copyright law defaults to "all rights reserved." Contact the maintainer or avoid the package.

### 2. Apache-2.0 + GPL-2.0 Incompatibility
Apache-2.0's patent grant clause is incompatible with GPL-2.0 (but compatible with GPL-3.0). Check GPL version carefully.

### 3. AGPL-3.0 in SaaS
AGPL-3.0 requires source disclosure for network interactions. If your SaaS backend uses an AGPL dependency, you may need to open-source your server code.

### 4. Dual-Licensed Dependencies
Some packages offer dual licensing (e.g., "MIT OR Apache-2.0"). You choose which license to accept.

### 5. Transitive License Contamination
A permissive dependency that itself depends on a GPL package makes your project subject to GPL terms. Always check the full dependency tree.

## Audit Commands

```bash
# Node.js — full license report
npx license-checker --json --production --out licenses.json

# Node.js — find problematic licenses
npx license-checker --production --failOn "GPL-2.0;GPL-3.0;AGPL-3.0"

# Python
pip-licenses --format json --with-urls --with-description

# Go
go-licenses report ./... 2>/dev/null

# Rust
cargo license --json
```
