---
name: dependency-audit
description: Audits project dependencies for security vulnerabilities, license compliance, outdated packages, and supply chain risks. Activates when reviewing dependencies, checking for CVEs, analyzing package.json/requirements.txt/go.mod/Cargo.toml, or planning dependency upgrades across any language ecosystem.
metadata:
  tags:
    - audit
    - dependency
    - developer-tools
    - go
    - security
  updated: "2026-04-11"
---
# Dependency Audit

## Overview

This skill provides structured guidance for auditing project dependencies across language ecosystems. It covers vulnerability scanning, license compliance verification, update planning, and supply chain risk assessment. Use this skill when you need to evaluate the health, security, and compliance posture of a project's dependency tree.

## When to Use This Skill

This skill activates for tasks involving:
- Scanning dependencies for known CVEs and security advisories
- Checking license compatibility across the dependency tree
- Identifying outdated packages and planning upgrades
- Assessing supply chain risks (typosquatting, maintainer changes, abandoned packages)
- Generating dependency health reports
- Planning major version migrations with breaking change analysis

## Quick Start

For a basic dependency audit, follow these three steps:

1. **Identify ecosystem** — Detect package manager files in the project
2. **Run vulnerability scan** — Use ecosystem-appropriate tooling
3. **Generate report** — Summarize findings by severity

For a comprehensive audit, continue through all 8 steps below.

## Step-by-Step Workflow

### Step 1: Detect Package Ecosystem

Identify all dependency manifest files in the project:

| File | Ecosystem | Lock File |
|------|-----------|-----------|
| `package.json` | Node.js (npm/yarn/pnpm) | `package-lock.json`, `yarn.lock`, `pnpm-lock.yaml` |
| `requirements.txt` / `pyproject.toml` | Python (pip/poetry) | `poetry.lock`, `pip.lock` |
| `go.mod` | Go | `go.sum` |
| `Cargo.toml` | Rust | `Cargo.lock` |
| `Gemfile` | Ruby | `Gemfile.lock` |
| `pom.xml` / `build.gradle` | Java/Kotlin | — |
| `composer.json` | PHP | `composer.lock` |
| `Package.swift` | Swift | `Package.resolved` |

**Multi-ecosystem projects:** Audit each ecosystem independently, then cross-reference shared concerns.

### Step 2: Vulnerability Scanning

Run ecosystem-appropriate vulnerability scans:

```bash
# Node.js
npm audit --json
# or
yarn audit --json

# Python
pip-audit --format json
# or
safety check --json

# Go
govulncheck ./...

# Rust
cargo audit --json

# Ruby
bundle audit check --format json

# General (works across ecosystems)
# Use GitHub Advisory Database via gh CLI
gh api graphql -f query='
  query {
    securityVulnerabilities(first: 20, ecosystem: NPM, package: "lodash") {
      nodes {
        advisory { summary severity }
        vulnerableVersionRange
        firstPatchedVersion { identifier }
      }
    }
  }'
```

Classify findings by severity:
- **Critical** — Remote code execution, authentication bypass
- **High** — Data exposure, privilege escalation
- **Medium** — Denial of service, information disclosure
- **Low** — Minor information leaks, theoretical attacks

### Step 3: License Compliance Check

Verify all dependency licenses are compatible with project requirements:

**Permissive (generally safe):** MIT, BSD-2-Clause, BSD-3-Clause, Apache-2.0, ISC, Unlicense

**Copyleft (requires review):** GPL-2.0, GPL-3.0, LGPL-2.1, LGPL-3.0, AGPL-3.0, MPL-2.0

**Red flags:**
- No license specified (defaults to "all rights reserved")
- AGPL-3.0 in SaaS applications (viral licensing)
- GPL in proprietary/commercial projects without compliance plan
- Mixed GPL + proprietary in the same binary

```bash
# Node.js license check
npx license-checker --json --production

# Python
pip-licenses --format json

# Go
go-licenses report ./...
```

### Step 4: Outdated Package Analysis

Identify packages behind current releases:

```bash
# Node.js
npm outdated --json

# Python
pip list --outdated --format json

# Go
go list -u -m all

# Rust
cargo outdated --format json

# Ruby
bundle outdated --strict
```

Categorize updates:
- **Patch updates** (1.2.3 → 1.2.4) — Bug fixes, safe to apply
- **Minor updates** (1.2.3 → 1.3.0) — New features, backward compatible
- **Major updates** (1.2.3 → 2.0.0) — Breaking changes, requires migration plan

### Step 5: Supply Chain Risk Assessment

Evaluate each dependency for supply chain risks:

**Risk indicators:**
- **Maintainer count:** Single-maintainer packages are higher risk
- **Last publish date:** No updates in 2+ years may indicate abandonment
- **Download trends:** Sudden drops may indicate problems
- **Typosquatting:** Check for similarly-named malicious packages
- **Install scripts:** `preinstall`/`postinstall` scripts can execute arbitrary code

```bash
# Node.js — check for install scripts
npm explain <package> --json | jq '.scripts'

# Check package metadata
npm view <package> maintainers time dist-tags --json
```

**High-risk patterns:**
- Dependency with `postinstall` script that downloads binaries
- Package published by a new maintainer after long dormancy
- Package name one character off from a popular package
- Dependency pulling from non-standard registries

### Step 6: Dependency Tree Analysis

Analyze the full dependency tree for bloat and risk concentration:

```bash
# Node.js — visualize tree
npm ls --all --json | jq '.dependencies | keys | length'

# Find duplicate packages at different versions
npm ls --all 2>&1 | grep "deduped" | wc -l

# Python
pipdeptree --json
```

**Key metrics:**
- Total direct dependencies vs. transitive dependencies
- Maximum dependency depth
- Packages appearing at multiple versions
- Percentage of tree from a single vendor/org

### Step 7: Generate Audit Report

Compile findings into a structured report:

```markdown
# Dependency Audit Report

**Project:** [name]
**Date:** [date]
**Ecosystems:** [list]

## Summary
| Category | Critical | High | Medium | Low |
|----------|----------|------|--------|-----|
| Vulnerabilities | X | X | X | X |
| License Issues | X | X | X | X |
| Outdated | — | X | X | X |
| Supply Chain | X | X | X | X |

## Critical Findings
[List each critical finding with remediation]

## Recommended Actions
1. [Prioritized list of actions]

## Dependency Health Score
[Score out of 100 based on metrics]
```

### Step 8: Create Upgrade Plan

For findings requiring action, create a prioritized upgrade plan:

1. **Immediate** — Critical CVEs with known exploits
2. **This sprint** — High-severity vulnerabilities and license violations
3. **Next sprint** — Medium-severity issues and major version upgrades
4. **Backlog** — Low-severity and maintenance upgrades

For each upgrade, document:
- Current version → target version
- Breaking changes (from CHANGELOG)
- Migration steps
- Test coverage requirements

## Common Issues

### False Positives in Vulnerability Scans
Some CVEs may not apply to your usage of the package. Document and suppress with:
- npm: `.npmrc` audit settings or `overrides` in `package.json`
- Python: `safety` ignore flags
- Go: `govulncheck` already filters by call graph

### Lock File Drift
If the lock file doesn't match the manifest:
```bash
# Node.js — regenerate
rm -rf node_modules package-lock.json && npm install

# Python (poetry)
poetry lock --no-update
```

### Phantom Dependencies
Dependencies used in code but not declared in manifest (resolved through transitive deps). These break when the transitive dependency changes. Fix by adding explicit declarations.

## References

### references/vulnerability_databases.md
Reference of public vulnerability databases and advisory sources for cross-referencing scan results.

### references/license_compatibility_matrix.md
Compatibility matrix showing which open-source licenses can be combined in the same project.

## Related Skills
- `security` — Broader security audit beyond dependencies
- `github-ops` — Automating dependency PRs via GitHub
