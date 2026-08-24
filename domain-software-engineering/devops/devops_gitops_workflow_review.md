---
title: "GitOps Workflow Review (ArgoCD / Flux)"
category: devops
description: "Review a GitOps deployment setup (ArgoCD or Flux) for repo structure, sync configuration, drift handling, secret management, progressive delivery, and multi-cluster / multi-tenant patterns."
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
  - devops
  - gitops
  - argocd
  - flux
  - kubernetes
  - continuous-delivery
  - progressive-delivery
  - drift-detection
updated: "2026-04-17"
related_prompts:
  - devops_cicd_pipeline_analysis.md
  - devops_kubernetes_manifest_review.md
  - devops_helm_chart_review.md
---

# GitOps Workflow Review (ArgoCD / Flux)

**Objective:** Review a GitOps deployment pipeline (ArgoCD or Flux) end-to-end — repo structure, sync policy, drift handling, secret management, promotion flow, progressive delivery, and multi-cluster governance — and produce a prioritized improvement plan.

## When to Use

- Adopting GitOps and unsure about repo layout (app-of-apps, monorepo, repo-per-tenant).
- After a production incident caused by manual `kubectl apply` overriding declared state.
- When scaling from 1 cluster to many with differing team ownership.
- When secrets in Git are a concern and you haven't chosen a strategy (Sealed Secrets, External Secrets Operator, SOPS, Vault).
- When promotion from dev → staging → prod is ad hoc and needs structure.

**Do NOT use this prompt for:**
- General K8s manifest review (use `devops_kubernetes_manifest_review.md`).
- Helm chart specifics (use `devops_helm_chart_review.md`).
- CI pipeline design (use `devops_cicd_pipeline_analysis.md`).

## Inputs / Context

Collect:
- **Tool**: ArgoCD / Flux v2 / custom.
- **Repo shape**: monorepo / repo-per-app / app-of-apps / config-repo separate from code-repo.
- **Cluster topology**: single / multi-cluster, single / multi-tenant.
- **Promotion model**: branch-per-env / folder-per-env / overlay-per-env (Kustomize) / values-per-env (Helm).
- **Secret strategy**: in-cluster (Sealed Secrets / SOPS) / external (ESO + Vault/AWS SM/GCP SM).
- **Progressive delivery**: Argo Rollouts / Flagger / none.
- **Observability**: Argo CD notifications / Flux notifications / custom.

## Must / Must Not

**Must:**
- Separate **code repo** (app source) from **config repo** (deployment manifests) for clear ownership and promotion; OR justify a monorepo approach explicitly.
- Pin every source: Git revision (commit SHA, not `HEAD`), Helm chart version, image digest (not `:latest`).
- Specify **sync policy** per app: auto-sync vs manual, prune on/off, self-heal on/off.
- Handle **drift** explicitly: either prevent it (no manual `kubectl apply`) or allow it with clear override policy.
- Define **promotion flow**: how does a change move dev → staging → prod? PRs? Automated? What signs off?
- Include **secret strategy** with a no-plain-text-in-Git rule. Sealed Secrets OR External Secrets Operator OR SOPS — pick one and justify.
- Classify findings: **Critical** (secrets in plain text, no drift detection, manual prod changes), **High** (no image digest pinning, no promotion gates), **Medium**, **Low**.

**Must Not:**
- Recommend monorepo or polyrepo without considering team topology.
- Allow `:latest` image tags in production.
- Allow manual `kubectl apply` / `helm upgrade` alongside GitOps — pick one.
- Recommend Sealed Secrets for multi-cluster without acknowledging the key-management complexity.
- Treat ArgoCD UI access as a trust boundary — it's not; it's a convenience.
- Forget the **cluster bootstrap** question: how does ArgoCD / Flux itself get installed and upgraded?

## Instructions

Work through seven dimensions:

1. **Repo structure**: ownership, separation of concerns, promotion path visibility.
2. **Source pinning**: commit SHA / chart version / image digest; no floating references.
3. **Sync configuration**: auto vs manual, prune, self-heal; exclusions for PDBs / jobs.
4. **Drift handling**: what happens when cluster state diverges from Git? Detected? Reconciled? Alerting?
5. **Secret management**: chosen tool, rotation story, key custody, cross-cluster strategy.
6. **Progressive delivery**: canary / blue-green via Argo Rollouts or Flagger; rollback on SLO breach.
7. **Multi-cluster & RBAC**: who can deploy where; ApplicationSet / Kustomize Component patterns; tenant isolation.

## Output Format

```
# GitOps Review — <Organization / Platform>

## Summary
- Tool: <ArgoCD / Flux>
- Repo shape: <monorepo / app-of-apps / ...>
- Cluster count: <N>
- Tenants / teams: <N>
- Overall posture: <Sound / Concerns / Critical Gaps>

## Findings by Dimension

### 1. Repo Structure
- **State**: <evidence>
- **Gaps**: <list>
- **Recommendation**: <specific>
- **Effort**: S / M / L

### 2. Source Pinning
...

## Prioritized Remediation
1. <Critical / < 1 week>
2. <High / 1-4 weeks>
3. <Medium / next quarter>

## Reference Topology (if changes recommended)
<Proposed repo / cluster / app layout diagram or description>

## Verification Hook (Post-Fix)
<how the team will confirm each fix took effect — drift reports, sync status, etc.>
```

## Verification (Self-Check)

Before emitting:

1. All 7 dimensions addressed explicitly.
2. Repo-structure recommendation matches team topology.
3. Every pinning recommendation is specific (commit SHA, chart version, image digest).
4. Drift-handling behavior is described — not left implicit.
5. Secret strategy is one chosen path, not a menu.
6. Multi-cluster scaling story is stated even if today's scope is small.
7. Confidence per finding (High if inspected live state; Medium if inferred from manifests).

## False-Positive Prevention

Rule out:

- **"App-of-apps is best"** — It's one pattern; Flux's multi-tenant Kustomization or ArgoCD ApplicationSets may fit better for large orgs.
- **"Sealed Secrets solves secrets"** — Only in-cluster decryption; multi-cluster key rotation is hard. ESO + external KMS often better at scale.
- **"Auto-sync always"** — Prod may want manual sync or approval gates; stage can be auto.
- **"Prune always"** — Prune on PDBs / PVCs can cause outages; namespace-scope prune with exceptions is safer.
- **"Image digest is overkill"** — No — semantic tags are mutable; only digests are immutable.
- **"ArgoCD/Flux is the source of truth"** — Git is the source of truth; the controller is the reconciler.

Cap confidence at **Medium** if live cluster state was not inspected.

## Techniques Applied

ST-01, ST-02, ST-03, RT-02 (7-dimension), RT-05, CM-02, QA-01.
