---
name: slsa-compliance
description: Expert knowledge for SLSA (Supply-chain Levels for Software Artifacts) framework compliance. Provides guidance on SBOM generation, provenance attestation, and supply chain security levels. Use this skill when implementing SLSA requirements, generating SBOMs, creating provenance attestations, securing CI/CD pipelines, or when users mention "SLSA", "SBOM", "software supply chain", "provenance", "build attestation", "Sigstore", or "in-toto".
metadata:
  tags:
    - ci/cd
    - compliance
    - security
    - slsa
  updated: "2026-04-11"
---
# SLSA Compliance

Expert guidance for implementing the SLSA (Supply-chain Levels for Software Artifacts) framework to protect against supply chain attacks.

## Purpose

Supply chain attacks are increasingly common and devastating (SolarWinds, Codecov, Log4j). SLSA provides a security framework with progressive levels that help organizations verify the integrity of their software artifacts. This skill provides actionable guidance for assessing, implementing, and verifying SLSA compliance.

## When to Use This Skill

Use this skill when you need to:
- Assess current SLSA compliance level
- Generate Software Bill of Materials (SBOM)
- Create and verify build provenance attestations
- Secure CI/CD pipelines against supply chain attacks
- Implement dependency verification and scanning
- Prepare for security audits involving supply chain requirements
- User mentions: SLSA, SBOM, supply chain security, provenance, attestation, Sigstore

## When NOT to Use This Skill

Do NOT use this skill when:
- General application security (use `stride-analysis-patterns` or `sast-configuration`)
- Runtime security monitoring (use observability/monitoring skills)
- Container image scanning without supply chain context (use container-security skills)
- Compliance frameworks unrelated to supply chain (PCI-DSS, SOC2 use respective skills)

## Expertise Level

This skill assumes:
- **Familiarity with:** CI/CD pipelines, build systems, package managers
- **No requirement for:** Deep cryptography knowledge (explained inline)

---

## Core Concepts

### SLSA Framework Overview

**Definition:** SLSA (pronounced "salsa") is a security framework for ensuring the integrity of software artifacts throughout the software supply chain.

**Why it matters:** Supply chain attacks can compromise thousands of downstream users through a single point of failure. SLSA provides a common language and checklist for supply chain security.

**Key principles:**
- Trust must be verified, not assumed
- Build processes should be hermetic and reproducible
- Provenance (origin) of artifacts must be cryptographically verifiable
- Security improves incrementally through defined levels

### Software Bill of Materials (SBOM)

**Definition:** A comprehensive inventory of all components, libraries, and dependencies in a software artifact.

**Why it matters:** You cannot secure what you cannot see. SBOMs enable vulnerability tracking, license compliance, and supply chain transparency.

**Key formats:**
- **SPDX** - Linux Foundation standard, ISO/IEC 5962:2021
- **CycloneDX** - OWASP standard, optimized for security use cases
- **SWID** - ISO/IEC 19770-2, software identification tags

### Build Provenance

**Definition:** Verifiable metadata about how an artifact was produced, including source, builder, and build process.

**Why it matters:** Provenance answers "Who built this? From what source? Using what process?" - enabling verification that artifacts weren't tampered with.

**Key components:**
- **Subject:** The artifact being described (hash, name)
- **Predicate:** The provenance metadata
- **Builder:** Identity of the build system
- **Materials:** Inputs to the build (source, dependencies)

### Attestation

**Definition:** A cryptographically signed statement about an artifact's properties or origin.

**Why it matters:** Unsigned claims can be forged. Attestations provide cryptographic proof of provenance.

**Key formats:**
- **in-toto:** Attestation framework (SLSA uses in-toto Attestation Framework)
- **Sigstore:** Keyless signing infrastructure for attestations

---

## SLSA Levels Overview

### Level 0: No Guarantees

No SLSA compliance. Build process is undocumented, provenance is unavailable or unverifiable.

### Level 1: Documentation + Provenance Exists

**Requirements:**
| ID | Requirement | Verification |
|----|-------------|--------------|
| L1.1 | Build process is documented | Review build documentation |
| L1.2 | Provenance is generated (unsigned OK) | Check for provenance file existence |
| L1.3 | Provenance contains builder identity | Verify builder field populated |
| L1.4 | Provenance contains build instructions | Verify invocation/config fields |

**Value:** Prevents most accidental mistakes, provides basic auditability.

### Level 2: Tamper Resistance

**Requirements:**
| ID | Requirement | Verification |
|----|-------------|--------------|
| L2.1 | All Level 1 requirements | Level 1 checklist |
| L2.2 | Version control for source | Check VCS usage |
| L2.3 | Hosted build service (not local) | Verify CI/CD usage |
| L2.4 | Authenticated provenance | Verify signature exists |

**Value:** Prevents tampering after code review, attacker must compromise build service.

### Level 3: Hardened Builds

**Requirements:**
| ID | Requirement | Verification |
|----|-------------|--------------|
| L3.1 | All Level 2 requirements | Level 2 checklist |
| L3.2 | Hermetic builds (no network during build) | Review build isolation |
| L3.3 | Non-falsifiable provenance | Verify builder cannot be spoofed |
| L3.4 | Isolated build environment | Check ephemeral builders |
| L3.5 | Parameterless entry point | Verify fixed build commands |

**Value:** Attacker must compromise build platform itself, not just a single project.

### Level 4: Maximum Assurance (Future)

**Requirements:**
| ID | Requirement | Verification |
|----|-------------|--------------|
| L4.1 | All Level 3 requirements | Level 3 checklist |
| L4.2 | Two-party review for all changes | Check code review policies |
| L4.3 | Reproducible builds | Verify build determinism |
| L4.4 | Multi-platform attestation | Check cross-builder verification |

**Value:** Extremely high assurance, suitable for critical infrastructure.

---

## Implementation Patterns

### Pattern: SBOM Generation

**When to use:** Every release, as part of CI/CD pipeline.

**Tools:**
| Tool | Languages/Ecosystems | Format Output |
|------|---------------------|---------------|
| `syft` | Multi-language | SPDX, CycloneDX |
| `cdxgen` | Multi-language | CycloneDX |
| `trivy` | Containers, filesystems | SPDX, CycloneDX |
| `spdx-sbom-generator` | Multi-language | SPDX |

**Implementation (GitHub Actions):**

```yaml
name: Generate SBOM
on:
  release:
    types: [published]

jobs:
  sbom:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Generate SBOM with Syft
        uses: anchore/sbom-action@v0
        with:
          path: .
          format: spdx-json
          output-file: sbom.spdx.json

      - name: Upload SBOM as release asset
        uses: softprops/action-gh-release@v1
        with:
          files: sbom.spdx.json
```

**Why it works:** Automated SBOM generation ensures every release has an accurate inventory. Syft analyzes package manifests across ecosystems.

### Pattern: Provenance Generation with SLSA GitHub Generator

**When to use:** For achieving SLSA Level 2-3 provenance on GitHub Actions.

**Implementation:**

```yaml
name: SLSA Provenance
on:
  release:
    types: [published]

jobs:
  build:
    runs-on: ubuntu-latest
    outputs:
      hashes: ${{ steps.hash.outputs.hashes }}
    steps:
      - uses: actions/checkout@v4

      - name: Build artifact
        run: |
          # Your build commands here
          go build -o my-binary ./cmd/...

      - name: Generate hash
        id: hash
        run: |
          set -euo pipefail
          sha256sum my-binary > checksums.txt
          echo "hashes=$(cat checksums.txt | base64 -w0)" >> "$GITHUB_OUTPUT"

      - uses: actions/upload-artifact@v4
        with:
          name: my-binary
          path: my-binary

  provenance:
    needs: build
    permissions:
      actions: read
      id-token: write
      contents: write
    uses: slsa-framework/slsa-github-generator/.github/workflows/generator_generic_slsa3.yml@v2.0.0
    with:
      base64-subjects: ${{ needs.build.outputs.hashes }}
      upload-assets: true
```

**Why it works:** The SLSA GitHub Generator runs in an isolated workflow that cannot be modified by the repository, ensuring non-falsifiable provenance.

### Pattern: Sigstore Signing for Containers

**When to use:** Signing container images without managing keys.

**Implementation:**

```yaml
name: Sign Container
on:
  push:
    tags: ['v*']

jobs:
  build-and-sign:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
      id-token: write  # Required for Sigstore
    steps:
      - uses: actions/checkout@v4

      - name: Set up cosign
        uses: sigstore/cosign-installer@v3

      - name: Login to GHCR
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Build and push
        id: build
        uses: docker/build-push-action@v5
        with:
          push: true
          tags: ghcr.io/${{ github.repository }}:${{ github.ref_name }}

      - name: Sign with Sigstore
        env:
          DIGEST: ${{ steps.build.outputs.digest }}
        run: |
          cosign sign --yes ghcr.io/${{ github.repository }}@${DIGEST}
```

**Why it works:** Cosign with Sigstore uses keyless signing via OIDC identity, eliminating key management while providing verifiable signatures.

### Pattern: Provenance Verification

**When to use:** Before deploying or using any external artifact.

**Implementation:**

```bash
#!/bin/bash
# Verify SLSA provenance for a binary

# Install slsa-verifier
go install github.com/slsa-framework/slsa-verifier/v2/cli/slsa-verifier@latest

# Verify provenance
slsa-verifier verify-artifact my-binary \
  --provenance-path my-binary.intoto.jsonl \
  --source-uri github.com/org/repo \
  --source-tag v1.0.0

# Verify container image provenance
cosign verify-attestation \
  --type slsaprovenance \
  --certificate-identity-regexp '^https://github.com/slsa-framework/slsa-github-generator/.github/workflows/generator_container_slsa3.yml@refs/tags/v[0-9]+\.[0-9]+\.[0-9]+$' \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com \
  ghcr.io/org/image:tag
```

**Why it works:** Verification ensures the artifact was built from the expected source by an authorized builder, catching supply chain compromises.

---

## Evaluation Criteria

### Assessment Framework

When evaluating SLSA compliance:

| Criterion | Weight | Scoring |
|-----------|--------|---------|
| Provenance generation | 25% | 0=None, 1=Unsigned, 2=Signed |
| Build isolation | 25% | 0=Local, 1=Hosted, 2=Hermetic |
| Source integrity | 20% | 0=None, 1=VCS, 2=Protected branches |
| SBOM availability | 15% | 0=None, 1=Manual, 2=Automated |
| Verification process | 15% | 0=None, 1=Manual, 2=Enforced |

**Score interpretation:**
- **90-100%:** SLSA Level 3 ready
- **70-89%:** SLSA Level 2 compliant
- **50-69%:** SLSA Level 1 achievable
- **<50%:** Significant gaps, prioritize remediation

### Red Flags

**Immediate failures (cannot achieve compliance):**
- Builds run with elevated/admin privileges unnecessarily
- Provenance can be modified by build job itself
- No version control for build configurations
- Secrets exposed in build logs

### Quality Indicators

**Signs of strong implementation:**
- Provenance generated automatically for all artifacts
- SBOM integrated into release process
- Dependency updates automated with verification
- Build reproducibility tested regularly

**Warning signs:**
- Manual build steps outside CI/CD indicates process gaps
- Unsigned provenance suggests incomplete implementation
- Missing SBOM for production releases indicates visibility gap

---

## Common Mistakes

### Mistake: Provenance from Same Workflow as Build

**What it looks like:**
```yaml
# DON'T: Provenance in same job can be tampered with
jobs:
  build:
    steps:
      - run: make build
      - run: generate-provenance  # Can be modified!
```

**Why it's wrong:** Attackers who compromise the build can also modify provenance.

**Correct approach:**
```yaml
# DO: Use reusable workflow with separate permissions
jobs:
  build:
    outputs:
      hash: ${{ steps.hash.outputs.hash }}
  provenance:
    needs: build
    uses: slsa-framework/slsa-github-generator/.github/workflows/generator_generic_slsa3.yml@v2.0.0
```

### Mistake: SBOM Generated After Build

**What it looks like:** Running SBOM tools against deployment environment instead of build environment.

**Why it's wrong:** Runtime environment may differ from build; SBOM won't accurately reflect what was built.

**Correct approach:** Generate SBOM during build process, from the same environment that produces the artifact.

### Mistake: Ignoring Transitive Dependencies

**What it looks like:** SBOM only includes direct dependencies.

**Why it's wrong:** Vulnerabilities often exist in transitive dependencies (Log4j affected many projects indirectly).

**Correct approach:** Use tools that resolve full dependency trees: `syft`, `cdxgen`, `trivy`.

---

## Supply Chain Attack Vectors

Understanding attack vectors helps prioritize SLSA requirements:

| Attack Vector | Description | SLSA Mitigation |
|---------------|-------------|-----------------|
| Compromised source | Malicious code in repository | L2: Version control, L4: Two-party review |
| Compromised build | Modified during build | L3: Hermetic builds, isolated environment |
| Compromised dependencies | Malicious package uploaded | SBOM + scanning, provenance verification |
| Compromised distribution | Modified after build | Signed provenance, checksum verification |
| Typosquatting | Similar package names | Dependency pinning, lockfiles |
| Account takeover | Maintainer credentials stolen | MFA, signing keys rotation |

---

## Glossary

| Term | Definition |
|------|------------|
| SLSA | Supply-chain Levels for Software Artifacts - security framework |
| SBOM | Software Bill of Materials - component inventory |
| Provenance | Verifiable metadata about artifact origin and build process |
| Attestation | Cryptographically signed statement about artifact properties |
| Hermetic build | Build that cannot access network or modify external state |
| in-toto | Framework for software supply chain integrity |
| Sigstore | Keyless signing infrastructure for software artifacts |
| Cosign | Container signing tool from Sigstore project |
| Rekor | Transparency log for attestations (part of Sigstore) |
| Fulcio | Certificate authority for keyless signing (part of Sigstore) |

---

## Reference Files

| Resource | Purpose |
|----------|---------|
| `scripts/sbom_generator.sh` | Generate SBOM from current project |
| `scripts/slsa_level_checker.py` | Assess current SLSA compliance level |
| `references/slsa_levels_explained.md` | Deep dive on each SLSA level |
| `references/sbom_formats.md` | SPDX vs CycloneDX comparison |
| `references/provenance_guide.md` | Detailed provenance implementation |
| `references/ci_integration.md` | GitHub Actions and GitLab CI examples |
| `assets/slsa_checklist.md` | Complete level-by-level compliance checklist |

## Related Skills

- `stride-analysis-patterns` - Threat modeling methodology
- `sast-configuration` - Static analysis for vulnerability detection
- `attack-tree-construction` - Visualize attack paths
- `threat-mitigation-mapping` - Map threats to controls
