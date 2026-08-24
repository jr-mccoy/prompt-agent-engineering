---
title: "SBOM & Software Supply Chain Security Review"
category: analysis/security
description: "Review software supply chain posture: SBOM generation, dependency provenance, build-time integrity, signing (Sigstore/Cosign), SLSA level, dependency confusion risk, and third-party/fourth-party exposure."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - RT-05
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - security
  - supply-chain
  - sbom
  - slsa
  - sigstore
  - cosign
  - dependency-confusion
  - provenance
updated: "2026-04-17"
related_prompts:
  - security_vulnerability_analysis.md
  - security_container_review.md
  - ../../devops/devops_cicd_pipeline_analysis.md
---

# SBOM & Software Supply Chain Security Review

**Objective:** Review a project's supply-chain posture end-to-end — from source to deploy — and identify gaps in SBOM generation, dependency provenance, build integrity, artifact signing, and runtime verification. Output a prioritized, SLSA-aligned improvement plan.

## When to Use

- Before shipping software to regulated customers (FedRAMP, CRA, EO 14028).
- When the team is asked to "provide an SBOM" and doesn't have a production one.
- During post-incident review of a dependency-chain compromise.
- When moving from internal-only to public / partner-facing distribution.
- Before adopting new build tooling (Bazel, Nix, reproducible builds).

**Do NOT use this prompt for:**
- Runtime vulnerability scanning alone — use `security_vulnerability_analysis.md`.
- Container-specific security — use `security_container_review.md`.
- CI/CD pipeline security isolation — use `devops_cicd_pipeline_analysis.md`.

## Inputs / Context

Collect:
- **Language / build system**: npm, pip, Maven, Gradle, Go modules, Cargo, Nix, Bazel, etc.
- **Artifact type**: container image, OS package, firmware, npm/PyPI package, mobile app, JAR.
- **Distribution channel**: public registry, private registry, app store, direct download.
- **Compliance target**: SLSA level goal (1/2/3/4), FedRAMP, CRA, EO 14028, customer contract.
- **Existing artifacts**: Is there an SBOM? In which format (SPDX / CycloneDX)? Is it generated automatically or manually? Is it signed?
- **Signing**: Do artifacts carry signatures? Sigstore / GPG / internal CA?

## Must / Must Not

**Must:**
- Evaluate the **full** chain: source → dependencies → build → artifact → distribution → runtime verification. Every phase gets a finding or an explicit "no gap" statement.
- Reference **SLSA v1.0** levels for provenance maturity. State current level and target level.
- Prefer **SPDX 2.3+** or **CycloneDX 1.5+** for SBOM format; note trade-offs (SPDX = ISO standard; CycloneDX = richer security metadata).
- Distinguish **first-party** (your code), **direct dependencies** (declared), **transitive** (pulled in), and **fourth-party** (your vendor's vendors).
- Classify findings: **Critical** (unsigned production artifacts, no SBOM for regulated shipping), **High** (manual SBOM, no provenance), **Medium** (SBOM exists but not signed), **Low** / **Info**.

**Must Not:**
- Claim "generating an SBOM solves supply chain" — it's a prerequisite, not a solution.
- Recommend Sigstore / Cosign without evaluating whether the ecosystem supports verification (some registries still don't).
- Recommend SLSA 3/4 without acknowledging the hermetic-build requirement and cost.
- Ignore **build-time** tampering (malicious GitHub Actions, compromised runners) — most sophisticated attacks land here.
- Overlook **dependency confusion** (internal packages with public registry namespaces) — one of the most exploited vectors.
- Assume package-lock / yarn.lock / Cargo.lock alone equals provenance — they don't prove the registry wasn't MITM'd.

## Instructions

Work through five phases. For each, produce findings per the Output Format.

1. **Source integrity**: branch protection, signed commits, required reviews, CODEOWNERS, secret scanning, dependency manifest integrity (lockfiles, hash pinning).
2. **Dependency provenance**: SBOM existence, format, coverage (first + transitive), dep confusion risk, internal registry scoping, vendoring policy, known-vuln scanning.
3. **Build integrity**: hermetic vs non-hermetic, build environment reproducibility, runner isolation, ephemeral credentials, build-step signing.
4. **Artifact signing and distribution**: Sigstore / Cosign / in-toto attestation, registry signing verification, mirror / proxy integrity.
5. **Runtime verification**: admission policy (Kyverno / OPA Gatekeeper / Kubewarden) checking signatures + SBOM, runtime SBOM re-validation, CVE rescan cadence.

For each phase, state:
- Current state (evidence-cited).
- SLSA level implied by current state.
- Gaps vs. target.
- Specific remediation (tool, config, policy).

## Output Format

```
# Supply Chain Security Review — <Project>

## Summary
- Artifact type: <container / package / binary>
- Distribution: <public / private / app-store>
- Current SLSA level (estimated): <1/2/3/4>
- Target SLSA level: <1/2/3/4>
- Compliance mandate: <FedRAMP / CRA / EO-14028 / none>

## Phase Findings
### Phase 1: Source Integrity
- **State**: <evidence-cited>
- **Gaps**: <list>
- **Remediation**: <specific actions>

### Phase 2: Dependency Provenance
...

## Prioritized Remediation Plan
1. <Quick Win, < 1 week>
2. <Medium, 1–4 weeks>
3. <Major, > 1 quarter>

## SLSA Gap Analysis
| Requirement | Current | Target | Gap |
|-------------|---------|--------|-----|
| Provenance exists | Yes/No | Yes | ... |
| Provenance authenticated | Yes/No | Yes | ... |
| Build service hermetic | Yes/No | Yes | ... |
...

## SBOM Recommendation
- Format: SPDX 2.3 | CycloneDX 1.5
- Generator: syft / cdxgen / sbom-tool / language-native
- Storage: attached to release / registry attestation / sigstore transparency log
- Refresh cadence: per-build
```

## Verification (Self-Check)

Before emitting:

1. All 5 phases addressed explicitly (no silent gaps).
2. Each gap references a concrete artifact (pipeline file, manifest, tool, or absence thereof).
3. SLSA level claims are justified against the v1.0 requirements, not asserted.
4. Dependency confusion risk is specifically evaluated (internal + external namespace collision).
5. Transitive dependency coverage of the SBOM is stated — not just direct deps.
6. Confidence per finding (High = inspected, Medium = inferred from config, Low = asked but not confirmed).

## False-Positive Prevention

Rule out:

- **"No SBOM = Critical"** — If the project ships internally-only and compliance doesn't require SBOM, this is Medium hardening, not Critical.
- **"Lockfile absent"** — Some ecosystems (Go modules with `go.sum`, Nix) provide integrity via different mechanisms; don't conflate with npm-style lockfiles.
- **"Dependencies are outdated"** — Age alone is not a supply-chain finding; age + known vuln + reachable code path is.
- **"Not signed"** — Signing doesn't prove supply-chain integrity if the signing key is the build runner's long-lived credential. Check key management too.
- **"Build is not hermetic"** — Hermetic builds are a SLSA 3/4 goal; demanding them at SLSA 2 is premature.
- **"No Sigstore"** — Not every ecosystem has Sigstore support; check what the registry / platform actually verifies.

Confidence must be **Medium** or higher for Critical findings; if you inferred from config without inspecting the build output, cap at Medium.

## Techniques Applied

ST-01, ST-02, ST-03, RT-02 (5-phase analysis), RT-05 (evidence-based), CM-02, QA-01.
