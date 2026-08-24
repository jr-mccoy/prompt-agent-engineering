---
title: "ML Supply Chain Audit"
category: AI-ML/model-security
description: "Audit the provenance and integrity of everything that enters a model — pretrained weights, datasets, serialization formats, and framework dependencies — establishing what is actually verified versus merely trusted, and what the load path can execute."
techniques:
  - RT-02
  - ST-02
  - CM-02
  - QA-12
  - DS-06
difficulty: advanced
tags:
  - supply-chain
  - model-provenance
  - deserialization
  - dependency-integrity
  - artifact-signing
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/model-security/mlsec_data_poisoning_backdoor_defense.md
  - domain-AI-ML/model-security/mlsec_ml_threat_model.md
  - domain-AI-ML/agentic-ai-systems/aiagent_supply_chain_aibom.md
  - domain-AI-ML/mlops-infrastructure/mlops_model_packaging_strategy.md
---

# ML Supply Chain Audit

**Objective:** Establish what a model is actually made of and which parts of it are verified rather than merely trusted — tracing pretrained weights, datasets, serialization formats, and framework dependencies to a provenance claim you could defend, and identifying where loading an artifact executes code.

**When to Use:**
- Adopting pretrained weights, an embedding model, or a dataset you did not produce.
- Before promoting a model to production, or before a compliance or customer-security review asks what it contains.
- After any incident involving a package registry, a model hub, or a dependency, when you need to know your exposure.

**When NOT to Use:**
- The concern is adversarial manipulation of *your own* training data — use `mlsec_data_poisoning_backdoor_defense.md`.
- The subject is an agent's tools, connectors, and delegated privileges — use `../agentic-ai-systems/aiagent_supply_chain_aibom.md`.
- You need general application dependency scanning rather than the ML-specific artifact path — use `domain-software-engineering/analysis/security/`.

## Inputs / Context

- **Model lineage** — every pretrained checkpoint, adapter, or embedding model in the final artifact, and where each came from.
- **Dataset lineage** — every external dataset, its licence, and its distribution channel.
- **Serialization formats** — the on-disk format of every artifact loaded at train or serve time.
- **Load path** — what process loads each artifact, with what privileges, in what environment.
- **Dependency inventory** — ML frameworks, data libraries, and their transitive dependencies, with lockfile state.
- **Registry and transport** — where artifacts are stored, how they are fetched, and what integrity checks exist in transit and at rest.

## Constraints

**Must:**
- Distinguish **verified** from **trusted** for every component: verified means a checked signature, a pinned hash, or a reproducible build; trusted means it came from somewhere reputable. Most inventories collapse the two, and the collapse is the finding.
- Identify every artifact whose **loading executes code**, and treat loading an unverified one as running unverified code with the loader's privileges.
- Trace to an origin, not to a mirror — a hash pinned against a mirror proves the mirror was consistent, not that the artifact is what its author published.
- Cover datasets as well as weights; an adopted dataset is a training-integrity dependency.
- State for each unverified component what an attacker would need to compromise in order to reach you.

**Must Not:**
- Assert CVEs, incident counts, specific malicious-package findings, or platform statistics from memory; mark any needed figure `[verify against a primary source]`.
- Treat a popular or well-known source as verification; popularity is not provenance.
- Report a lockfile as integrity when the lock covers versions but not content hashes.
- Recommend "scan for malware" as the control for a poisoned checkpoint — scanners detect known-bad files, and a backdoored weight tensor is not a known-bad file.
- Conclude a checkpoint is clean because it behaves correctly on the evaluation set; a targeted backdoor is built to leave that intact.

**Instructions:**

1. **Build the artifact bill of materials.** Enumerate every component in the final model: base checkpoints, adapters, tokenizers, embedding models, external datasets, and the frameworks that load them. Anything you cannot enumerate is the first finding.

2. **Classify each component verified vs trusted.** For every entry record: source, transport, integrity mechanism actually in force (signature checked, hash pinned to origin, reproducible build, or none), and who could have modified it in transit or at rest. Be strict — "downloaded from the official hub over TLS" is trusted, not verified.

3. **Map the load path and its privileges.** For each artifact: which process loads it, with what user, in what network position, and with what filesystem access. This determines the blast radius if the artifact is hostile.

4. **Flag code-executing formats.** Identify formats whose deserialization can execute arbitrary code, and every place one is loaded. For each, decide: convert to a non-executing format, load only under verification, or isolate the load in a sandbox with no credentials and no network. Note that conversion must happen in a context where you already accept the execution risk once.

5. **Audit dataset provenance.** For each external dataset: origin, licence, distribution channel, integrity mechanism, and whether the copy you hold matches what the publisher released. Note that a dataset adopted without content verification is a training-integrity dependency, not just a licensing one.

6. **Audit dependency integrity.** Check that lockfiles pin content hashes rather than version numbers alone; that private and public registries cannot be confused for the same package name; and that build and training environments resolve from the same locked state.

7. **Assess backdoor exposure for adopted weights.** Where a checkpoint's training data and process are not yours, state plainly that evaluation-set behaviour does not establish absence of a targeted backdoor. Record what you can do instead: restrict what the model's output authorizes, monitor for trigger-like input distributions, and prefer checkpoints whose training process is documented and reproducible.

8. **Rank by blast radius.** Order findings by what a compromise of each component would reach — training pipeline, production inference, credentials, or lateral network access — rather than by how easy each is to fix.

9. **Produce the remediation and re-verification plan.** For each finding: the control, who owns it, and the check that confirms it holds on the next build rather than only today.

**Output Format:**

A markdown audit:
- **Artifact Bill of Materials** — table: Component | Type | Source | Transport | Integrity in force | Verified or trusted.
- **Load Path & Privileges** — table: Artifact | Loading process | User/privileges | Network position | Blast radius.
- **Code-Executing Formats** — every instance, with the decision taken.
- **Dataset Provenance** — table: Dataset | Origin | Licence | Integrity | Content-verified?
- **Dependency Integrity** — lockfile content-hash state, registry-confusion exposure, environment parity.
- **Adopted-Weights Backdoor Exposure** — what cannot be established and what compensates.
- **Findings Ranked by Blast Radius** — with the compromise path for each.
- **Remediation & Re-verification** — control, owner, and the recurring check.
- **INSUFFICIENT EVIDENCE** — the required value in the `Verified or trusted` column wherever no integrity check was actually performed. This is the audit's central distinction: an artifact whose hash nobody compared is trusted, not verified, and the two must never share a cell value. Name the unblocking datum: the publisher-side digest or signature to compare against.

## Verification

- [ ] Every component is enumerated; anything unenumerable is recorded as a finding.
- [ ] Each component is classified verified or trusted against a stated integrity mechanism.
- [ ] Integrity is traced to origin rather than to a mirror.
- [ ] Every code-executing load is identified and has a decision attached.
- [ ] Datasets are audited for content verification, not only licensing.
- [ ] Lockfiles are checked for content hashes rather than version pins alone.
- [ ] The report states that evaluation behaviour cannot establish backdoor absence in adopted weights.
- [ ] Findings are ranked by blast radius, not by ease of fix.
- [ ] Each remediation has a recurring check, not a one-time action.
- [ ] No CVEs, incident counts, or platform statistics are asserted from memory.
- [ ] Every component with no performed integrity check reads INSUFFICIENT EVIDENCE rather than verified, with the publisher digest or signature named as what would settle it.

## False-Positive Prevention

❌ **DON'T:**
- Mark a checkpoint verified because it came from a well-known hub over TLS — that establishes the transport, not the artifact.
- Treat a lockfile as integrity when it pins versions but not content hashes; the same version string can resolve to different bytes.
- Record a hash as provenance when it was computed against your own mirror — it proves internal consistency, nothing about the publisher.
- Rely on malware scanning for a poisoned model file; a backdoor lives in weights, not in a signature database.
- Conclude an adopted checkpoint is clean from strong evaluation results — a targeted backdoor is designed to preserve exactly those.
- Rank findings by how quickly they can be closed; a trivial fix on an isolated component outranks nothing.

✅ **DO:**
- Apply the verified-vs-trusted distinction strictly and expect most of the inventory to land in "trusted" on the first pass — that is the honest starting picture.
- Trace each artifact to what its publisher actually released, and say where you cannot.
- Treat every code-executing load as running that publisher's code with the loader's privileges, and decide accordingly.
- Audit datasets for content match, since an adopted dataset is a training-integrity dependency.
- State plainly what cannot be established about adopted weights, and compensate by bounding what the model's output is allowed to authorize.
- Rank by what a compromise reaches, and attach a recurring check so the fix survives the next build.

## Example Output

```markdown
## ML Supply Chain Audit: Document-Classification Service
Fine-tuned open checkpoint + adapter, served in the payments VPC.

### Artifact Bill of Materials
| Component | Type | Source | Transport | Integrity in force | Verdict |
|---|---|---|---|---|---|
| Base encoder checkpoint | weights | public model hub | HTTPS at build | none — no hash pin | **Trusted** |
| Fine-tune adapter | weights | internal registry | HTTPS | SHA-256 pinned in manifest | **Verified** |
| Tokenizer | config + vocab | same hub, separate repo | HTTPS | none | **Trusted** |
| Sentence-embedding model | weights | public hub | HTTPS | none | **Trusted** |
| Legal-clause dataset | dataset | vendor SFTP | SFTP | vendor-supplied checksum, **never checked** | **Trusted** |
| ML framework + 214 transitive deps | packages | public index | HTTPS | lockfile pins **versions only** | **Trusted** |

Four of six components are trusted rather than verified, including everything whose loading
executes code. This is the audit's headline.

### Load Path & Privileges
| Artifact | Loading process | User | Network | Blast radius |
|---|---|---|---|---|
| Base checkpoint | training job | `mlbuild` (CI) | egress to internet + artifact registry write | **CI credentials + published artifacts** |
| Adapter | inference server | `svc-infer` | payments VPC, DB read | **payments VPC + document DB** |
| Tokenizer | both | as above | as above | as above |
| Embedding model | inference server | `svc-infer` | payments VPC | payments VPC |

### Code-Executing Formats
- **Base checkpoint** and **embedding model** are in a pickle-based format. Loading them
  executes arbitrary code as `mlbuild` (internet egress + registry write) and `svc-infer`
  (payments VPC). Both are unverified.
  **Decision:** convert both to a non-executing tensor format. Perform the one-time conversion
  in an isolated container with no credentials and no network, then hash-pin the converted
  artifact and load only that from then on.
- **Adapter** is already stored in a non-executing format. No change.

### Dataset Provenance
| Dataset | Origin | Licence | Integrity | Content-verified |
|---|---|---|---|---|
| Legal-clause corpus | vendor | commercial, redistribution prohibited | checksum supplied | **No** — never compared |
| Internal documents | internal | n/a | pipeline-managed | Yes |

The vendor checksum exists and has simply never been checked. Closing this is a one-line
build-step change and moves the dataset from trusted to verified.

### Dependency Integrity
Lockfile pins **versions only**, so the same lock can resolve to different bytes. Two internal
package names are also resolvable from the public index, so a public package published under
either name could be preferred at build time. Training and serving environments are built from
**separate** lockfiles that have drifted by 11 packages — the model is trained against one
dependency set and served against another.

### Adopted-Weights Backdoor Exposure
The base encoder's training data and process are not ours and are not documented in a
reproducible form. **Evaluation performance cannot establish the absence of a targeted
backdoor** — a backdoor is built to leave evaluation intact. We cannot close this by testing.
Compensating controls: the classifier's output authorizes routing only, never a payment or an
irreversible action; and input distribution is monitored for trigger-like clustering. Where a
documented, reproducible checkpoint exists as an alternative, prefer it at the next refresh.

### Findings Ranked by Blast Radius
1. **Unverified pickle load in the training job** — arbitrary code as `mlbuild`, which holds
   internet egress and artifact-registry write. A compromise here publishes poisoned artifacts
   downstream. *(Highest reach, regardless of likelihood.)*
2. **Unverified pickle load in the inference server** — arbitrary code inside the payments VPC
   with document-DB read.
3. **Registry-confusion exposure on two internal package names** — a build-time code path.
4. **Train/serve lockfile drift (11 packages)** — correctness and reproducibility risk as much
   as a security one.
5. **Unverified vendor dataset** — training-integrity dependency; cheapest to close.

### Remediation & Re-verification
| Finding | Control | Owner | Recurring check |
|---|---|---|---|
| 1, 2 | Convert to non-executing format; hash-pin; fail the load on mismatch | ML platform | CI gate on every build; alert on hash mismatch |
| 3 | Scope internal names to the private index; disable public fallback | Platform eng | Build fails if resolution source is not the private index |
| 4 | Single lockfile shared by train and serve | ML platform | CI diff gate; build fails on divergence |
| 5 | Verify vendor checksum at ingest | Data eng | Ingest step fails on mismatch |
```

**Techniques Used:**
- **RT-02 (Multi-Dimensional Analysis Framework):** component × provenance × load privilege × blast radius is the audit grid.
- **ST-02 (Structured Sequential Instructions):** the bill of materials is built before any component is judged, so nothing is assessed that was never enumerated.
- **CM-02 (Constraint Specification):** the verified-vs-trusted distinction and the trace-to-origin rule are hard constraints on what may be recorded.
- **QA-12 (False Positives Identification):** rejects popularity, TLS, and version-only lockfiles as evidence of integrity.
- **DS-06 (Prioritization and Severity Guidance):** blast-radius ranking drives remediation order.

**Related Prompts:**
- `mlsec_data_poisoning_backdoor_defense.md` — when the training data rather than the artifact is the exposure.
- `mlsec_ml_threat_model.md` — establishes whether the supply chain is a ranked threat for this deployment.
- `../agentic-ai-systems/aiagent_supply_chain_aibom.md` — the agent-side counterpart covering tools and connectors.
- `../mlops-infrastructure/mlops_model_packaging_strategy.md` — where format and signing decisions get implemented.
