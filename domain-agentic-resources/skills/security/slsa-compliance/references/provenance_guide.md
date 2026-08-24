# Provenance Generation Guide

> Complete guide to generating, signing, and verifying software provenance attestations.

## What is Provenance?

Provenance is **verifiable metadata** about how a software artifact was produced. It answers:

- **Who** built it? (Builder identity)
- **What** source was used? (Git commit, repository)
- **How** was it built? (Build commands, configuration)
- **When** was it built? (Timestamp)

```
┌─────────────────────────────────────────────────────────────┐
│                        PROVENANCE                            │
│                                                             │
│  Subject:  artifact.bin (sha256:abc123...)                 │
│                                                             │
│  Builder:  github.com/actions/runner                       │
│  Source:   github.com/org/repo@v1.0.0                      │
│  Built:    2024-01-15T10:30:00Z                            │
│  Config:   .github/workflows/release.yml                   │
│                                                             │
│  Signature: ✓ Verified (Sigstore)                          │
└─────────────────────────────────────────────────────────────┘
```

---

## Attestation Formats

### in-toto Attestation Framework

SLSA uses the [in-toto attestation format](https://github.com/in-toto/attestation):

```json
{
  "_type": "https://in-toto.io/Statement/v1",
  "subject": [
    {
      "name": "artifact.bin",
      "digest": {
        "sha256": "abc123..."
      }
    }
  ],
  "predicateType": "https://slsa.dev/provenance/v1",
  "predicate": {
    // SLSA Provenance content
  }
}
```

### SLSA Provenance Predicate

```json
{
  "buildDefinition": {
    "buildType": "https://slsa-framework.github.io/github-actions-buildtypes/workflow/v1",
    "externalParameters": {
      "workflow": {
        "ref": "refs/tags/v1.0.0",
        "repository": "https://github.com/org/repo",
        "path": ".github/workflows/release.yml"
      }
    },
    "internalParameters": {
      "github": {
        "event_name": "release",
        "repository_id": "123456789",
        "repository_owner_id": "987654321"
      }
    },
    "resolvedDependencies": [
      {
        "uri": "git+https://github.com/org/repo@refs/tags/v1.0.0",
        "digest": {
          "gitCommit": "abc123def456..."
        }
      }
    ]
  },
  "runDetails": {
    "builder": {
      "id": "https://github.com/slsa-framework/slsa-github-generator/.github/workflows/generator_generic_slsa3.yml@refs/tags/v2.0.0"
    },
    "metadata": {
      "invocationId": "https://github.com/org/repo/actions/runs/123456789/attempts/1",
      "startedOn": "2024-01-15T10:30:00Z",
      "finishedOn": "2024-01-15T10:35:00Z"
    }
  }
}
```

---

## Generation Methods

### Method 1: SLSA GitHub Generator (Recommended for L3)

The official way to achieve SLSA Level 3 on GitHub Actions.

**For generic artifacts:**

```yaml
name: SLSA Provenance
on:
  release:
    types: [published]

jobs:
  build:
    outputs:
      hashes: ${{ steps.hash.outputs.hashes }}
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Build
        run: |
          # Your build commands
          go build -o my-artifact ./cmd/...

      - name: Generate hashes
        id: hash
        run: |
          set -euo pipefail
          # Generate SHA256 hash and encode as base64
          echo "hashes=$(sha256sum my-artifact | base64 -w0)" >> "$GITHUB_OUTPUT"

      - uses: actions/upload-artifact@v4
        with:
          name: my-artifact
          path: my-artifact

  provenance:
    needs: [build]
    permissions:
      actions: read      # Read workflow info
      id-token: write    # OIDC token for signing
      contents: write    # Upload provenance to release
    uses: slsa-framework/slsa-github-generator/.github/workflows/generator_generic_slsa3.yml@v2.0.0
    with:
      base64-subjects: "${{ needs.build.outputs.hashes }}"
      upload-assets: true  # Upload to GitHub release
```

**For containers:**

```yaml
name: Container Provenance
on:
  push:
    tags: ['v*']

jobs:
  build:
    outputs:
      image: ${{ steps.build.outputs.image }}
      digest: ${{ steps.build.outputs.digest }}
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
    steps:
      - uses: actions/checkout@v4

      - uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - uses: docker/build-push-action@v5
        id: build
        with:
          push: true
          tags: ghcr.io/${{ github.repository }}:${{ github.ref_name }}

  provenance:
    needs: [build]
    permissions:
      actions: read
      id-token: write
      packages: write
    uses: slsa-framework/slsa-github-generator/.github/workflows/generator_container_slsa3.yml@v2.0.0
    with:
      image: ${{ needs.build.outputs.image }}
      digest: ${{ needs.build.outputs.digest }}
      registry-username: ${{ github.actor }}
    secrets:
      registry-password: ${{ secrets.GITHUB_TOKEN }}
```

**For Go binaries:**

```yaml
name: Go SLSA
on:
  release:
    types: [published]

permissions: read-all

jobs:
  build:
    permissions:
      id-token: write
      contents: write
      actions: read
    uses: slsa-framework/slsa-github-generator/.github/workflows/builder_go_slsa3.yml@v2.0.0
    with:
      go-version: "1.21"
      evaluated-envs: "VERSION:${{ github.ref_name }}"
```

### Method 2: Sigstore Cosign (Manual Signing)

For more control or non-GitHub environments:

```yaml
name: Cosign Provenance
on:
  release:
    types: [published]

jobs:
  sign:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      id-token: write  # For keyless signing
    steps:
      - uses: actions/checkout@v4

      - uses: sigstore/cosign-installer@v3

      - name: Build artifact
        run: make build

      - name: Create provenance
        run: |
          cat > provenance.json << 'EOF'
          {
            "_type": "https://in-toto.io/Statement/v1",
            "subject": [
              {
                "name": "artifact",
                "digest": {
                  "sha256": "$(sha256sum artifact | cut -d' ' -f1)"
                }
              }
            ],
            "predicateType": "https://slsa.dev/provenance/v1",
            "predicate": {
              "buildDefinition": {
                "buildType": "https://example.com/Makefile",
                "externalParameters": {
                  "repository": "${{ github.repository }}",
                  "ref": "${{ github.ref }}"
                }
              },
              "runDetails": {
                "builder": {
                  "id": "https://github.com/actions/runner"
                }
              }
            }
          }
          EOF
          # Substitute actual hash
          HASH=$(sha256sum artifact | cut -d' ' -f1)
          sed -i "s/\$(sha256sum artifact | cut -d' ' -f1)/$HASH/" provenance.json

      - name: Sign provenance
        run: |
          cosign attest --yes --predicate provenance.json artifact
```

### Method 3: Container Signing with Cosign

```bash
# Build and push container
docker build -t ghcr.io/org/image:v1.0.0 .
docker push ghcr.io/org/image:v1.0.0

# Get digest
DIGEST=$(docker inspect --format='{{index .RepoDigests 0}}' ghcr.io/org/image:v1.0.0 | cut -d'@' -f2)

# Sign the image (keyless)
cosign sign --yes ghcr.io/org/image@$DIGEST

# Attach provenance attestation
cosign attest --yes \
  --predicate provenance.json \
  --type slsaprovenance \
  ghcr.io/org/image@$DIGEST
```

### Method 4: GitLab CI

```yaml
# .gitlab-ci.yml
stages:
  - build
  - sign

build:
  stage: build
  script:
    - make build
    - sha256sum artifact > checksums.txt
  artifacts:
    paths:
      - artifact
      - checksums.txt

sign:
  stage: sign
  image: gcr.io/projectsigstore/cosign:v2.2.0
  script:
    - |
      cat > provenance.json << EOF
      {
        "_type": "https://in-toto.io/Statement/v1",
        "subject": [{"name": "artifact", "digest": {"sha256": "$(cat checksums.txt | cut -d' ' -f1)"}}],
        "predicateType": "https://slsa.dev/provenance/v1",
        "predicate": {
          "buildDefinition": {
            "buildType": "https://gitlab.com/build",
            "externalParameters": {
              "repository": "$CI_PROJECT_URL",
              "ref": "$CI_COMMIT_REF_NAME"
            }
          },
          "runDetails": {
            "builder": {"id": "https://gitlab.com/runner"},
            "metadata": {"invocationId": "$CI_PIPELINE_URL"}
          }
        }
      }
      EOF
    - cosign sign-blob --yes --output-signature provenance.sig provenance.json
  artifacts:
    paths:
      - provenance.json
      - provenance.sig
```

---

## Signing Options

### Keyless Signing (Sigstore)

Uses OIDC identity instead of long-lived keys:

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   CI/CD      │────►│    Fulcio    │────►│    Rekor     │
│  (GitHub)    │     │  (cert auth) │     │ (transparency│
│              │     │              │     │     log)     │
└──────────────┘     └──────────────┘     └──────────────┘
       │                    │                    │
       │   1. OIDC token    │   2. Short-lived   │   3. Entry
       │                    │      certificate   │      logged
       ▼                    ▼                    ▼
    Identity            Signing              Verifiable
    proven              enabled               record
```

**Advantages:**
- No key management
- Short-lived certificates (10 minutes)
- Tied to identity (not key possession)
- Transparent audit log

**Configuration:**
```yaml
permissions:
  id-token: write  # Required for OIDC token
```

### Key-based Signing

Traditional approach with managed keys:

```bash
# Generate key pair
cosign generate-key-pair

# Sign with key
cosign sign --key cosign.key ghcr.io/org/image:tag

# Store public key for verification
# cosign.pub should be distributed to verifiers
```

**Advantages:**
- Works offline
- No dependency on Sigstore infrastructure
- Familiar PKI model

**Disadvantages:**
- Key management burden
- Key rotation complexity
- Compromise = revocation needed

---

## Verification

### Verifying Generic Artifacts

```bash
# Install slsa-verifier
go install github.com/slsa-framework/slsa-verifier/v2/cli/slsa-verifier@latest

# Verify artifact provenance
slsa-verifier verify-artifact my-artifact \
  --provenance-path my-artifact.intoto.jsonl \
  --source-uri github.com/org/repo \
  --source-tag v1.0.0

# Expected output:
# Verified signature against tlog entry index 12345678 at URL: https://rekor.sigstore.dev
# Verified build using builder "https://github.com/slsa-framework/slsa-github-generator/.github/workflows/generator_generic_slsa3.yml@refs/tags/v2.0.0" at commit abc123...
# Verifying artifact my-artifact: PASSED

# SLSA verification level
slsa-verifier verify-artifact my-artifact \
  --provenance-path my-artifact.intoto.jsonl \
  --source-uri github.com/org/repo \
  --print-provenance
```

### Verifying Container Images

```bash
# Verify image signature
cosign verify \
  --certificate-identity-regexp '^https://github.com/org/repo/.github/workflows/.*\.yml@.*$' \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com \
  ghcr.io/org/image:tag

# Verify SLSA provenance attestation
cosign verify-attestation \
  --type slsaprovenance \
  --certificate-identity-regexp '^https://github.com/slsa-framework/slsa-github-generator/.github/workflows/generator_container_slsa3.yml@refs/tags/v[0-9]+\.[0-9]+\.[0-9]+$' \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com \
  ghcr.io/org/image@sha256:abc123...

# Extract and view provenance
cosign download attestation ghcr.io/org/image@sha256:abc123... | jq -r '.payload' | base64 -d | jq .
```

### Kubernetes Admission Control

Use Sigstore Policy Controller or Kyverno:

```yaml
# Kyverno policy for SLSA verification
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: verify-slsa-provenance
spec:
  validationFailureAction: Enforce
  background: false
  rules:
    - name: check-slsa-attestation
      match:
        any:
          - resources:
              kinds:
                - Pod
      verifyImages:
        - imageReferences:
            - "ghcr.io/org/*"
          attestations:
            - predicateType: "https://slsa.dev/provenance/v1"
              conditions:
                - all:
                    - key: "{{ builder.id }}"
                      operator: Equals
                      value: "https://github.com/slsa-framework/slsa-github-generator/.github/workflows/generator_container_slsa3.yml@refs/tags/v2.0.0"
```

---

## Provenance Storage

### Where to Store Provenance

| Location | Pros | Cons |
|----------|------|------|
| **GitHub Release Assets** | Discoverable, versioned | GitHub-specific |
| **OCI Registry** | With image, standard | Container images only |
| **Rekor Transparency Log** | Immutable, searchable | Depends on Sigstore |
| **Package Registry** | With package | Registry-specific |
| **Dedicated Storage** | Flexible | Self-managed |

### Rekor Transparency Log

All keyless signatures are logged to Rekor:

```bash
# Search Rekor for attestations
rekor-cli search --email user@example.com

# Get entry by UUID
rekor-cli get --uuid 24296fb24b8ad77abc123...

# Verify entry inclusion
rekor-cli verify --artifact artifact --signature sig
```

---

## Troubleshooting

### Common Issues

**1. "id-token: write permission required"**
```yaml
# Solution: Add permission to job
jobs:
  build:
    permissions:
      id-token: write
```

**2. "OIDC token not available"**

Ensure workflow runs from trusted context (not fork PRs):
```yaml
on:
  push:
    branches: [main]
  release:
    types: [published]
  # NOT: pull_request (forks can't get id-token)
```

**3. "Provenance verification failed: source mismatch"**

Verify source URI matches exactly:
```bash
# Check what's in provenance
slsa-verifier verify-artifact artifact \
  --provenance-path provenance.intoto.jsonl \
  --print-provenance | jq '.predicate.buildDefinition.externalParameters'

# Use matching source URI
slsa-verifier verify-artifact artifact \
  --source-uri github.com/EXACT/REPO  # Case-sensitive!
```

**4. "Certificate has expired"**

Sigstore certificates are short-lived (10 min). Verify within validity window or use Rekor timestamp:
```bash
# Rekor provides timestamp proof
cosign verify --certificate-identity-regexp '...' --certificate-oidc-issuer '...' image
# ✓ Uses Rekor entry timestamp, not current time
```

---

## Best Practices

### Do's

- **Use reusable workflows** for provenance generation (non-falsifiable)
- **Pin action versions** with full SHA, not tags
- **Verify provenance** before deploying artifacts
- **Store provenance** with artifacts (same lifecycle)
- **Use keyless signing** when possible (less key management)

### Don'ts

- **Don't generate provenance in the same job as build** (can be tampered)
- **Don't use mutable tags** for verification (v2 vs v2.0.0)
- **Don't skip verification** in deployment pipelines
- **Don't hardcode verification expectations** (use policy engines)

---

## Resources

- [SLSA Provenance Specification](https://slsa.dev/spec/v1.0/provenance)
- [in-toto Attestation Framework](https://github.com/in-toto/attestation)
- [Sigstore Documentation](https://docs.sigstore.dev/)
- [SLSA GitHub Generator](https://github.com/slsa-framework/slsa-github-generator)
- [slsa-verifier](https://github.com/slsa-framework/slsa-verifier)
