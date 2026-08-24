# SLSA Levels Explained

> Deep dive into each SLSA level, requirements, and implementation strategies.

## Overview

SLSA (Supply-chain Levels for Software Artifacts) defines four levels of increasing assurance. Each level builds on the previous, providing progressively stronger guarantees about artifact integrity.

```
Level 0: No guarantees
    ↓
Level 1: Documentation exists, provenance generated
    ↓
Level 2: Tamper-resistant (hosted builds, signed provenance)
    ↓
Level 3: Hardened (non-falsifiable provenance, isolated builds)
    ↓
Level 4: Maximum assurance (reproducible, multi-party verified)
```

---

## Level 0: No SLSA

### Definition

No SLSA compliance. This is the default state for most software projects.

### Characteristics

- Build process is undocumented or ad-hoc
- No provenance information available
- Artifacts could come from anywhere
- No verification possible

### Risks

| Risk | Impact |
|------|--------|
| Source tampering | Unknown code changes undetected |
| Build tampering | Malicious artifacts possible |
| Distribution tampering | Artifacts modified post-build |
| Attribution | Cannot determine who built what |

### Upgrading from Level 0

**Minimum steps:**
1. Document build process in README or BUILDING.md
2. Move builds to CI/CD (GitHub Actions, GitLab CI, etc.)
3. Generate basic provenance during build

---

## Level 1: Provenance Exists

### Definition

The software producer generates provenance for their artifacts, documenting how they were built.

### Requirements

| ID | Requirement | Description |
|----|-------------|-------------|
| L1.1 | Build documentation | Build process is scripted and documented |
| L1.2 | Provenance generated | Provenance output exists for artifacts |
| L1.3 | Builder identity | Provenance includes who/what did the build |
| L1.4 | Build instructions | Provenance includes how artifact was built |

### Provenance Schema (Minimum)

```json
{
  "builder": {
    "id": "https://example.com/builder"
  },
  "buildType": "https://example.com/build-type/v1",
  "invocation": {
    "configSource": {
      "uri": "git+https://github.com/org/repo@refs/heads/main"
    }
  },
  "materials": [
    {
      "uri": "git+https://github.com/org/repo",
      "digest": { "sha1": "abc123..." }
    }
  ]
}
```

### Value Provided

- **Auditability**: Can trace what went into an artifact
- **Mistake prevention**: Catches accidental issues
- **Incident response**: Know what artifacts might be affected

### Limitations

- Provenance is unsigned (can be forged)
- Build might run locally (easily compromised)
- No verification of builder integrity

### Implementation Example

```yaml
# GitHub Actions - Basic provenance
name: Build with Provenance
on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Build
        run: make build

      - name: Generate provenance
        run: |
          cat > provenance.json << EOF
          {
            "builder": {"id": "${{ github.server_url }}/${{ github.repository }}/actions"},
            "buildType": "https://example.com/Makefile",
            "invocation": {
              "configSource": {
                "uri": "git+${{ github.server_url }}/${{ github.repository }}@${{ github.ref }}"
              }
            },
            "materials": [{
              "uri": "git+${{ github.server_url }}/${{ github.repository }}",
              "digest": {"sha1": "${{ github.sha }}"}
            }]
          }
          EOF

      - uses: actions/upload-artifact@v4
        with:
          name: provenance
          path: provenance.json
```

---

## Level 2: Tamper Resistance

### Definition

Provenance is authenticated to prevent forgery, and builds run on hosted infrastructure.

### Requirements

| ID | Requirement | Description |
|----|-------------|-------------|
| L2.1 | All L1 requirements | Must satisfy Level 1 first |
| L2.2 | Version control | Source must be in VCS (Git, etc.) |
| L2.3 | Hosted build service | Builds run on hosted CI, not locally |
| L2.4 | Authenticated provenance | Provenance is signed |

### Authentication Methods

**Option 1: Traditional PKI Signing**
```bash
# Sign provenance with GPG
gpg --sign --armor provenance.json

# Sign with cosign (self-managed key)
cosign sign-blob --key cosign.key provenance.json
```

**Option 2: Keyless Signing with Sigstore**
```bash
# Keyless signing via OIDC
cosign sign-blob --oidc-issuer https://token.actions.githubusercontent.com provenance.json
```

### Value Provided

- **Forgery prevention**: Cannot fake provenance
- **Accountability**: Builder identity is verifiable
- **Tamper evidence**: Changes to artifacts detected

### Attack Surface Reduction

| Attack Vector | L1 Protection | L2 Protection |
|---------------|---------------|---------------|
| Forge provenance | None | Signature verification fails |
| Modify artifact | None | Signature mismatch |
| Spoof builder | None | Identity verification fails |
| Compromise dev machine | None | Builds on hosted infra |

### Implementation Example

```yaml
# GitHub Actions - Signed provenance
name: Signed Build
on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      id-token: write  # For keyless signing

    steps:
      - uses: actions/checkout@v4

      - uses: sigstore/cosign-installer@v3

      - name: Build
        run: make build

      - name: Sign artifact
        run: |
          sha256sum artifact.bin > checksums.txt
          cosign sign-blob --yes checksums.txt
```

---

## Level 3: Hardened Builds

### Definition

The build process itself is hardened against tampering. Provenance is non-falsifiable - even the build job cannot modify it.

### Requirements

| ID | Requirement | Description |
|----|-------------|-------------|
| L3.1 | All L2 requirements | Must satisfy Level 2 first |
| L3.2 | Hermetic builds | No network/external access during build |
| L3.3 | Non-falsifiable provenance | Build job cannot modify provenance |
| L3.4 | Isolated environment | Ephemeral, isolated build environment |
| L3.5 | Parameterless entry | Build triggered by fixed, audited config |

### Non-falsifiable Provenance

The key L3 requirement is that **the build job itself cannot modify the provenance**. This requires architectural separation:

```
┌─────────────────────────────────────────────────────────────┐
│ REPOSITORY                                                   │
│                                                             │
│  ┌─────────────────┐      ┌─────────────────┐              │
│  │   Build Job     │      │ Provenance Job  │◄── Separate  │
│  │                 │      │ (slsa-generator)│    workflow  │
│  │ - Compiles code │      │                 │              │
│  │ - Runs tests    │      │ - Isolated      │              │
│  │ - Creates hash  │────► │ - Cannot modify │              │
│  │                 │ hash │ - Signs output  │              │
│  └─────────────────┘      └─────────────────┘              │
│                                   │                         │
└───────────────────────────────────│─────────────────────────┘
                                    │
                                    ▼
                           Signed Provenance
```

### Hermetic Builds

A hermetic build:
- Has no network access during build
- Cannot access secrets not explicitly provided
- Uses only declared inputs
- Produces deterministic output

```yaml
# Bazel example of hermetic build
build --incompatible_strict_action_env
build --sandbox_default_allow_network=false
```

### Implementation with SLSA GitHub Generator

```yaml
name: SLSA Level 3
on:
  release:
    types: [published]

jobs:
  # Job 1: Build and hash
  build:
    outputs:
      hashes: ${{ steps.hash.outputs.hashes }}
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Build artifact
        run: go build -o binary ./cmd/...

      - name: Generate hash
        id: hash
        run: |
          set -euo pipefail
          echo "hashes=$(sha256sum binary | base64 -w0)" >> $GITHUB_OUTPUT

      - uses: actions/upload-artifact@v4
        with:
          name: binary
          path: binary

  # Job 2: Generate provenance (isolated, cannot be modified)
  provenance:
    needs: [build]
    permissions:
      actions: read
      id-token: write
      contents: write
    uses: slsa-framework/slsa-github-generator/.github/workflows/generator_generic_slsa3.yml@v2.0.0
    with:
      base64-subjects: "${{ needs.build.outputs.hashes }}"
      upload-assets: true
```

### Value Provided

- **Build integrity**: Even compromised build scripts can't fake provenance
- **Insider threat protection**: Malicious employees can't inject code undetected
- **Supply chain resilience**: Compromise requires attacking the platform itself

---

## Level 4: Maximum Assurance (Future)

### Definition

All changes require two-party review, and builds are reproducible and verifiable by independent parties.

### Proposed Requirements

| ID | Requirement | Description |
|----|-------------|-------------|
| L4.1 | All L3 requirements | Must satisfy Level 3 first |
| L4.2 | Two-party review | All code changes reviewed by 2+ people |
| L4.3 | Reproducible builds | Identical inputs = identical outputs |
| L4.4 | Multi-platform attestation | Verified by multiple independent builders |

### Reproducible Builds

For a build to be reproducible:

```
Same source code + Same build environment + Same build process = Identical artifact
```

Challenges:
- Timestamps embedded in artifacts
- Non-deterministic ordering (file listings, map iterations)
- Different compilers/tool versions
- Environment-specific paths

### Implementation Patterns (Preview)

```yaml
# Reproducible build verification
- name: Build on platform A
  id: build_a
  run: |
    DOCKER_BUILDKIT=1 docker build --no-cache -t app:test .
    docker save app:test | sha256sum > hash_a.txt

- name: Build on platform B
  id: build_b
  run: |
    DOCKER_BUILDKIT=1 docker build --no-cache -t app:test .
    docker save app:test | sha256sum > hash_b.txt

- name: Compare hashes
  run: diff hash_a.txt hash_b.txt
```

### Current Status

Level 4 is still being defined by the SLSA working group. Organizations should:
1. Achieve Level 3 first
2. Experiment with reproducible builds
3. Implement two-party review where possible
4. Monitor SLSA specification updates

---

## Level Comparison Matrix

| Aspect | L1 | L2 | L3 | L4 |
|--------|----|----|----|----|
| Build documented | Yes | Yes | Yes | Yes |
| Provenance exists | Yes | Yes | Yes | Yes |
| Hosted build | No | Yes | Yes | Yes |
| Signed provenance | No | Yes | Yes | Yes |
| Non-falsifiable provenance | No | No | Yes | Yes |
| Hermetic builds | No | No | Yes | Yes |
| Two-party review | No | No | No | Yes |
| Reproducible | No | No | No | Yes |

---

## Upgrade Path

### From Level 0 to Level 1

1. **Document your build**
   ```markdown
   ## Building

   Requirements:
   - Go 1.21+
   - Make

   Steps:
   1. Clone repository
   2. Run `make build`
   3. Output in `./bin/`
   ```

2. **Generate basic provenance**
   - Add provenance generation to CI
   - Include builder, source, and build info

### From Level 1 to Level 2

1. **Ensure hosted CI**
   - Move local builds to GitHub Actions/GitLab CI
   - Remove manual release processes

2. **Add signing**
   - Install cosign
   - Add `id-token: write` permission
   - Sign artifacts and provenance

### From Level 2 to Level 3

1. **Use SLSA GitHub Generator**
   - Separate build from provenance generation
   - Use reusable workflow

2. **Harden builds**
   - Minimize build-time network access
   - Use ephemeral runners
   - Pin action versions

---

## Resources

- [SLSA Specification](https://slsa.dev/spec/v1.0/)
- [SLSA GitHub Generator](https://github.com/slsa-framework/slsa-github-generator)
- [Sigstore Documentation](https://docs.sigstore.dev/)
- [in-toto Attestation Framework](https://github.com/in-toto/attestation)
