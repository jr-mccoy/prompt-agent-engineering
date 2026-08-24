# CI/CD Integration Guide

> Complete examples for integrating SLSA compliance into GitHub Actions, GitLab CI, and other platforms.

## GitHub Actions

### Basic SLSA Level 2 Setup

Achieves Level 2 with signed provenance:

```yaml
name: SLSA Level 2 Build
on:
  push:
    tags: ['v*']

permissions:
  contents: write
  id-token: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Go
        uses: actions/setup-go@v5
        with:
          go-version: '1.21'

      - name: Build
        run: |
          CGO_ENABLED=0 go build -ldflags="-s -w" -o artifact ./cmd/...

      - name: Install cosign
        uses: sigstore/cosign-installer@v3

      - name: Sign artifact
        run: |
          sha256sum artifact > checksums.txt
          cosign sign-blob --yes --output-signature checksums.sig checksums.txt

      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: release-artifacts
          path: |
            artifact
            checksums.txt
            checksums.sig
```

### Full SLSA Level 3 Setup

Achieves Level 3 with non-falsifiable provenance:

```yaml
name: SLSA Level 3 Release
on:
  release:
    types: [published]

permissions: read-all

jobs:
  # Job 1: Build artifacts
  build:
    runs-on: ubuntu-latest
    outputs:
      hashes: ${{ steps.hash.outputs.hashes }}
    permissions:
      contents: read

    steps:
      - uses: actions/checkout@v4

      - name: Set up Go
        uses: actions/setup-go@v5
        with:
          go-version-file: go.mod
          cache: true

      - name: Build binaries
        run: |
          # Build for multiple platforms
          GOOS=linux GOARCH=amd64 go build -o dist/myapp-linux-amd64 ./cmd/...
          GOOS=linux GOARCH=arm64 go build -o dist/myapp-linux-arm64 ./cmd/...
          GOOS=darwin GOARCH=amd64 go build -o dist/myapp-darwin-amd64 ./cmd/...
          GOOS=darwin GOARCH=arm64 go build -o dist/myapp-darwin-arm64 ./cmd/...
          GOOS=windows GOARCH=amd64 go build -o dist/myapp-windows-amd64.exe ./cmd/...

      - name: Generate hashes
        id: hash
        run: |
          cd dist
          sha256sum * > checksums.txt
          echo "hashes=$(cat checksums.txt | base64 -w0)" >> "$GITHUB_OUTPUT"

      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: binaries
          path: dist/

  # Job 2: Generate SLSA provenance (isolated)
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

  # Job 3: Generate SBOM
  sbom:
    needs: [build]
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4

      - name: Generate SBOM
        uses: anchore/sbom-action@v0
        with:
          path: .
          format: spdx-json
          output-file: sbom.spdx.json

      - name: Upload SBOM to release
        uses: softprops/action-gh-release@v1
        with:
          files: sbom.spdx.json

  # Job 4: Upload binaries to release
  release:
    needs: [build, provenance, sbom]
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/download-artifact@v4
        with:
          name: binaries
          path: dist/

      - name: Upload to release
        uses: softprops/action-gh-release@v1
        with:
          files: dist/*
```

### Container Build with SLSA Provenance

```yaml
name: Container SLSA
on:
  push:
    tags: ['v*']

permissions: read-all

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
    outputs:
      image: ${{ steps.image.outputs.image }}
      digest: ${{ steps.build.outputs.digest }}

    steps:
      - uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Login to GHCR
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ghcr.io/${{ github.repository }}
          tags: |
            type=semver,pattern={{version}}
            type=semver,pattern={{major}}.{{minor}}
            type=sha

      - name: Build and push
        id: build
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max

      - name: Output image
        id: image
        run: echo "image=ghcr.io/${{ github.repository }}" >> "$GITHUB_OUTPUT"

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

  # Optional: Scan for vulnerabilities
  scan:
    needs: [build]
    runs-on: ubuntu-latest
    steps:
      - name: Scan image
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: ghcr.io/${{ github.repository }}@${{ needs.build.outputs.digest }}
          format: 'sarif'
          output: 'trivy-results.sarif'

      - name: Upload Trivy scan results
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: 'trivy-results.sarif'
```

### NPM Package with Provenance

```yaml
name: NPM Publish with Provenance
on:
  release:
    types: [published]

jobs:
  publish:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      id-token: write  # Required for npm provenance
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          registry-url: 'https://registry.npmjs.org'

      - name: Install dependencies
        run: npm ci

      - name: Build
        run: npm run build

      - name: Publish with provenance
        run: npm publish --provenance --access public
        env:
          NODE_AUTH_TOKEN: ${{ secrets.NPM_TOKEN }}
```

---

## GitLab CI

### Basic SLSA Setup

```yaml
# .gitlab-ci.yml
stages:
  - build
  - sign
  - release

variables:
  # Pin versions for reproducibility
  COSIGN_VERSION: "2.2.0"
  SYFT_VERSION: "0.98.0"

build:
  stage: build
  image: golang:1.21
  script:
    - go build -o dist/myapp ./cmd/...
    - sha256sum dist/myapp > dist/checksums.txt
  artifacts:
    paths:
      - dist/
    expire_in: 1 week

generate-sbom:
  stage: build
  image: anchore/syft:$SYFT_VERSION
  script:
    - syft scan dir:. -o spdx-json=sbom.spdx.json
  artifacts:
    paths:
      - sbom.spdx.json

sign:
  stage: sign
  image: gcr.io/projectsigstore/cosign:v$COSIGN_VERSION
  needs: [build]
  script:
    - |
      # Create provenance
      cat > provenance.json << EOF
      {
        "_type": "https://in-toto.io/Statement/v1",
        "subject": [{
          "name": "myapp",
          "digest": {"sha256": "$(cat dist/checksums.txt | cut -d' ' -f1)"}
        }],
        "predicateType": "https://slsa.dev/provenance/v1",
        "predicate": {
          "buildDefinition": {
            "buildType": "https://gitlab.com/ci",
            "externalParameters": {
              "repository": "$CI_PROJECT_URL",
              "ref": "$CI_COMMIT_REF_NAME",
              "commit": "$CI_COMMIT_SHA"
            }
          },
          "runDetails": {
            "builder": {"id": "https://gitlab.com/runner"},
            "metadata": {
              "invocationId": "$CI_PIPELINE_URL",
              "startedOn": "$CI_PIPELINE_CREATED_AT"
            }
          }
        }
      }
      EOF
    - |
      # Sign with cosign (requires OIDC or key)
      # Option 1: Keyless (GitLab OIDC)
      cosign sign-blob --yes \
        --oidc-issuer https://gitlab.com \
        --oidc-client-id $CI_PROJECT_ID \
        --output-signature provenance.sig \
        provenance.json

      # Option 2: Key-based
      # cosign sign-blob --key env://COSIGN_PRIVATE_KEY \
      #   --output-signature provenance.sig provenance.json
  artifacts:
    paths:
      - provenance.json
      - provenance.sig

release:
  stage: release
  image: registry.gitlab.com/gitlab-org/release-cli:latest
  needs: [build, sign, generate-sbom]
  rules:
    - if: $CI_COMMIT_TAG
  script:
    - echo "Creating release $CI_COMMIT_TAG"
  release:
    tag_name: $CI_COMMIT_TAG
    description: 'Release $CI_COMMIT_TAG'
    assets:
      links:
        - name: 'myapp'
          url: '$CI_PROJECT_URL/-/jobs/artifacts/$CI_COMMIT_REF_NAME/raw/dist/myapp?job=build'
        - name: 'provenance.json'
          url: '$CI_PROJECT_URL/-/jobs/artifacts/$CI_COMMIT_REF_NAME/raw/provenance.json?job=sign'
        - name: 'sbom.spdx.json'
          url: '$CI_PROJECT_URL/-/jobs/artifacts/$CI_COMMIT_REF_NAME/raw/sbom.spdx.json?job=generate-sbom'
```

### Container Build with Signing

```yaml
# .gitlab-ci.yml
stages:
  - build
  - sign

variables:
  CONTAINER_IMAGE: $CI_REGISTRY_IMAGE:$CI_COMMIT_TAG

build-container:
  stage: build
  image: docker:24
  services:
    - docker:24-dind
  before_script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
  script:
    - docker build -t $CONTAINER_IMAGE .
    - docker push $CONTAINER_IMAGE
    - |
      # Get digest
      DIGEST=$(docker inspect --format='{{index .RepoDigests 0}}' $CONTAINER_IMAGE | cut -d'@' -f2)
      echo "CONTAINER_DIGEST=$DIGEST" >> build.env
  artifacts:
    reports:
      dotenv: build.env

sign-container:
  stage: sign
  image: gcr.io/projectsigstore/cosign:v2.2.0
  needs: [build-container]
  script:
    - |
      # Login to registry
      cosign login $CI_REGISTRY -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD

      # Sign image
      cosign sign --yes $CI_REGISTRY_IMAGE@$CONTAINER_DIGEST

      # Generate and attach SBOM
      syft $CI_REGISTRY_IMAGE@$CONTAINER_DIGEST -o cyclonedx-json > sbom.cdx.json
      cosign attach sbom --sbom sbom.cdx.json $CI_REGISTRY_IMAGE@$CONTAINER_DIGEST

      # Attest provenance
      cat > provenance.json << EOF
      {
        "_type": "https://in-toto.io/Statement/v1",
        "subject": [{
          "name": "$CI_REGISTRY_IMAGE",
          "digest": {"sha256": "$(echo $CONTAINER_DIGEST | cut -d: -f2)"}
        }],
        "predicateType": "https://slsa.dev/provenance/v1",
        "predicate": {
          "buildDefinition": {
            "buildType": "https://gitlab.com/container-build",
            "externalParameters": {
              "repository": "$CI_PROJECT_URL",
              "ref": "$CI_COMMIT_TAG"
            }
          },
          "runDetails": {
            "builder": {"id": "https://gitlab.com/runner"}
          }
        }
      }
      EOF
      cosign attest --yes --predicate provenance.json --type slsaprovenance $CI_REGISTRY_IMAGE@$CONTAINER_DIGEST
```

---

## Azure DevOps

```yaml
# azure-pipelines.yml
trigger:
  tags:
    include:
      - 'v*'

pool:
  vmImage: 'ubuntu-latest'

stages:
  - stage: Build
    jobs:
      - job: BuildArtifact
        steps:
          - task: GoTool@0
            inputs:
              version: '1.21'

          - script: |
              go build -o $(Build.ArtifactStagingDirectory)/myapp ./cmd/...
              sha256sum $(Build.ArtifactStagingDirectory)/myapp > $(Build.ArtifactStagingDirectory)/checksums.txt
            displayName: 'Build'

          - task: PublishBuildArtifacts@1
            inputs:
              pathToPublish: '$(Build.ArtifactStagingDirectory)'
              artifactName: 'binaries'

  - stage: Sign
    dependsOn: Build
    jobs:
      - job: SignArtifact
        steps:
          - task: DownloadBuildArtifacts@0
            inputs:
              buildType: 'current'
              downloadType: 'single'
              artifactName: 'binaries'
              downloadPath: '$(System.ArtifactsDirectory)'

          - script: |
              # Install cosign
              curl -sSL https://github.com/sigstore/cosign/releases/latest/download/cosign-linux-amd64 -o cosign
              chmod +x cosign

              # Create provenance
              HASH=$(cat $(System.ArtifactsDirectory)/binaries/checksums.txt | cut -d' ' -f1)
              cat > provenance.json << EOF
              {
                "_type": "https://in-toto.io/Statement/v1",
                "subject": [{"name": "myapp", "digest": {"sha256": "$HASH"}}],
                "predicateType": "https://slsa.dev/provenance/v1",
                "predicate": {
                  "buildDefinition": {
                    "buildType": "https://dev.azure.com/pipeline",
                    "externalParameters": {
                      "repository": "$(Build.Repository.Uri)",
                      "ref": "$(Build.SourceBranch)"
                    }
                  },
                  "runDetails": {
                    "builder": {"id": "https://dev.azure.com/$(System.TeamProject)/_build"},
                    "metadata": {"invocationId": "$(Build.BuildUri)"}
                  }
                }
              }
              EOF

              # Sign (requires Azure OIDC or service connection)
              ./cosign sign-blob --yes --output-signature provenance.sig provenance.json
            displayName: 'Generate and sign provenance'

          - task: PublishBuildArtifacts@1
            inputs:
              pathToPublish: 'provenance.json'
              artifactName: 'provenance'
```

---

## Jenkins

```groovy
// Jenkinsfile
pipeline {
    agent any

    environment {
        COSIGN_VERSION = '2.2.0'
    }

    stages {
        stage('Build') {
            steps {
                sh 'go build -o dist/myapp ./cmd/...'
                sh 'sha256sum dist/myapp > dist/checksums.txt'
                archiveArtifacts artifacts: 'dist/*'
            }
        }

        stage('Generate SBOM') {
            steps {
                sh '''
                    curl -sSL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s -- -b /usr/local/bin
                    syft scan dir:. -o spdx-json=sbom.spdx.json
                '''
                archiveArtifacts artifacts: 'sbom.spdx.json'
            }
        }

        stage('Sign') {
            environment {
                COSIGN_PRIVATE_KEY = credentials('cosign-private-key')
                COSIGN_PASSWORD = credentials('cosign-password')
            }
            steps {
                sh '''
                    # Install cosign
                    curl -sSL https://github.com/sigstore/cosign/releases/download/v${COSIGN_VERSION}/cosign-linux-amd64 -o cosign
                    chmod +x cosign

                    # Create provenance
                    HASH=$(cat dist/checksums.txt | cut -d' ' -f1)
                    cat > provenance.json << EOF
{
  "_type": "https://in-toto.io/Statement/v1",
  "subject": [{"name": "myapp", "digest": {"sha256": "${HASH}"}}],
  "predicateType": "https://slsa.dev/provenance/v1",
  "predicate": {
    "buildDefinition": {
      "buildType": "https://jenkins.io/pipeline",
      "externalParameters": {
        "repository": "${GIT_URL}",
        "ref": "${GIT_BRANCH}",
        "commit": "${GIT_COMMIT}"
      }
    },
    "runDetails": {
      "builder": {"id": "${JENKINS_URL}"},
      "metadata": {"invocationId": "${BUILD_URL}"}
    }
  }
}
EOF

                    # Sign with key
                    ./cosign sign-blob --key env://COSIGN_PRIVATE_KEY \
                        --output-signature provenance.sig \
                        provenance.json
                '''
                archiveArtifacts artifacts: 'provenance.*'
            }
        }
    }

    post {
        success {
            echo 'Build completed with SLSA provenance'
        }
    }
}
```

---

## Verification in CI

### Verify Before Deployment

```yaml
# GitHub Actions deployment with verification
name: Deploy
on:
  workflow_dispatch:
    inputs:
      version:
        description: 'Version to deploy'
        required: true

jobs:
  verify-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Install slsa-verifier
        run: |
          go install github.com/slsa-framework/slsa-verifier/v2/cli/slsa-verifier@latest

      - name: Download artifact
        run: |
          gh release download ${{ inputs.version }} \
            --repo ${{ github.repository }} \
            --pattern 'myapp-*' \
            --pattern '*.intoto.jsonl'
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}

      - name: Verify provenance
        run: |
          slsa-verifier verify-artifact myapp-linux-amd64 \
            --provenance-path multiple.intoto.jsonl \
            --source-uri github.com/${{ github.repository }} \
            --source-tag ${{ inputs.version }}

      - name: Deploy
        if: success()
        run: |
          echo "Provenance verified, proceeding with deployment"
          # Your deployment commands here
```

### Kubernetes Admission Controller

```yaml
# Sigstore Policy Controller
apiVersion: policy.sigstore.dev/v1beta1
kind: ClusterImagePolicy
metadata:
  name: require-slsa-provenance
spec:
  images:
    - glob: "ghcr.io/myorg/**"
  authorities:
    - name: slsa-github-generator
      keyless:
        url: https://fulcio.sigstore.dev
        identities:
          - issuer: https://token.actions.githubusercontent.com
            subjectRegExp: ^https://github.com/slsa-framework/slsa-github-generator/.github/workflows/generator_.*\.yml@refs/tags/v[0-9]+\.[0-9]+\.[0-9]+$
      attestations:
        - name: slsa-provenance
          predicateType: https://slsa.dev/provenance/v1
          policy:
            type: cue
            data: |
              predicateType: "https://slsa.dev/provenance/v1"
```

---

## Resources

- [SLSA GitHub Generator Examples](https://github.com/slsa-framework/slsa-github-generator/tree/main/example-package)
- [Sigstore Policy Controller](https://docs.sigstore.dev/policy-controller/overview/)
- [GitLab OIDC for Keyless Signing](https://docs.gitlab.com/ee/ci/secrets/id_token_authentication.html)
- [npm Provenance](https://docs.npmjs.com/generating-provenance-statements)
