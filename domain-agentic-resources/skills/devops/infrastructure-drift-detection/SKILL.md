---
name: infrastructure-drift-detection
description: Detects, classifies and reconciles drift between infrastructure-as-code and live state using scheduled read-only plans, noise suppression, triage by cause, and a reviewed decision per item (revert, codify, import, hand ownership to a controller, or treat as a security event). Covers Terraform/OpenTofu, Pulumi, CloudFormation and GitOps-managed Kubernetes. Use when asked to "detect drift", "someone changed prod in the console", "terraform plan shows unexpected changes", or "set up a drift check".
metadata:
  tags:
    - devops
    - drift
    - infrastructure-as-code
    - terraform
    - gitops
    - compliance
  updated: "2026-10-04"
---
# Infrastructure Drift Detection

A procedure for finding where live infrastructure no longer matches its code, deciding
what each difference means, and reconciling it without destroying something that was
changed for a good reason.

## Purpose

Drift accumulates through console hotfixes during incidents, controllers that own fields
the IaC also declares, provider upgrades that change defaults, and occasionally
unauthorised changes. Undetected, it turns the next routine `apply` into an outage, because
the plan silently reverts the hotfix. Detected but untriaged, it trains the team to ignore
plan output. This skill sets up detection, removes perpetual noise, and gives every
drifted item an explicit decision.

## When to Use This Skill

- Setting up a scheduled drift check for Terraform/OpenTofu, Pulumi, CloudFormation or
  GitOps-managed Kubernetes
- A plan shows changes nobody made in code
- Someone changed production by hand (during an incident or otherwise) and the change
  must be reconciled
- Bringing resources created outside IaC under management
- Preparing for an audit that asks how out-of-band changes are detected

## When NOT to Use This Skill

- **Reviewing IaC code quality or module design.** Use the prompts
  `domain-software-engineering/devops/devops_infrastructure_as_code_review.md` and
  `devops_terraform_best_practices.md`, or the `terraform-module-library` skill.
- **Reviewing a GitOps setup end to end** (repo layout, promotion, secrets). Use the
  prompt `domain-software-engineering/devops/devops_gitops_workflow_review.md`; this
  skill handles the drift-detection and reconciliation part in depth.
- **Building a GitOps pipeline from scratch.** Use `gitops-workflow` (cloud-infrastructure).
- **Application configuration drift** between environments (feature flags, app config
  files). The triage approach transfers, but the tooling here is for infrastructure.
- **An active security incident.** If drift looks unauthorised, stop and follow the
  incident process (Step 5, class G).

## Prerequisites

- IaC with remote state and state locking
- A **read-only** identity for the drift job, separate from the identity that applies
  changes
- Access to the cloud provider's audit log (for example AWS CloudTrail, Azure Activity
  Log, Google Cloud Audit Logs) to see who changed what and when

## Workflow

### Step 1: Establish a clean baseline

Run a plan for every workspace or stack and list every difference that exists today.
Either reconcile each one (Steps 4–6) or record it as known, with an owner. Detection is
only useful once "no changes" is the normal result.

### Step 2: Choose the detection command per tool

All commands below are read-only. Verify flags against the current docs for your tool
version.

| Tool | Detection command | Drift signal |
|---|---|---|
| Terraform / OpenTofu | `terraform plan -detailed-exitcode -input=false -lock=false` (`tofu` for OpenTofu) | Exit code 2 = changes; 0 = none; 1 = error |
| Terraform / OpenTofu (state vs reality only) | `terraform plan -refresh-only -detailed-exitcode -input=false` | Shows what changed in real infrastructure since the last apply, without proposing config changes |
| Pulumi | `pulumi preview --expect-no-changes` (or `pulumi refresh --preview-only` to see what refresh would change) | Non-zero exit when changes are present |
| CloudFormation | `aws cloudformation detect-stack-drift --stack-name <stack>`, then `describe-stack-drift-detection-status` and `describe-stack-resource-drifts` | Resources with status `MODIFIED` or `DELETED` |
| Kubernetes (plain manifests) | `kubectl diff -f <dir>` | Exit code 1 = differences |
| Argo CD | `argocd app diff <app>`; application sync status `OutOfSync` | Non-empty diff |
| Flux | `flux diff kustomization <name> --path <dir>` | Non-empty diff |

**Treat exit code 1 (error) as a failed check, never as "no drift".** Expired credentials
and provider outages otherwise read as a clean bill of health.

For machine-readable output in Terraform, save the plan (`-out=drift.tfplan`) and read
`terraform show -json drift.tfplan`; resource-level changes are listed under
`resource_changes`, and the plan's `resource_drift` section lists differences detected
during refresh (verify the JSON format for your version).

### Step 3: Schedule it

- Frequency by criticality: production networking, IAM and data stores daily or more
  often; everything else at least weekly.
- One job per workspace or stack, so one failure does not hide the others.
- Do not run the drift job concurrently with apply pipelines on the same state. If
  you use `-lock=false` to avoid blocking applies, accept that a plan taken during an
  apply may show transient differences, and re-run before acting.
- Output goes to a ticket or a channel, not to a pager, except for security-relevant
  resources (IAM policies, security groups or firewall rules opened to the internet,
  public storage buckets, disabled logging). Those page.

### Step 4: Remove perpetual noise before triage

Differences that appear on every run are configuration bugs, not drift. Fix them so real
drift stands out:

| Noise pattern | Fix |
|---|---|
| Provider default differs from unset attribute | Set the attribute explicitly in code |
| List or map order differences | Use the provider's set types or sort inputs (check the provider docs) |
| Tags added by an organisation policy | Declare them in code, or configure the provider to ignore those tag keys if it supports that |
| Field owned by another controller (autoscaler replica count, desired capacity) | `lifecycle { ignore_changes = [<attribute>] }` with a comment naming the owning controller |
| Kubernetes fields mutated by admission controllers or operators | Configure the GitOps tool's ignore-differences setting for that field (verify against current docs) |

Every `ignore_changes` or ignore rule needs a comment with the reason and an owner. An
ignore rule without a reason is how real drift gets hidden.

### Step 5: Classify each drifted item

Use the audit log to find who changed it, when, and how.

| Class | Description | Default decision |
|---|---|---|
| A. Incident hotfix | Changed by hand during an incident to restore service | **Codify** in code, reviewed, before the next apply |
| B. Unreviewed manual change | Console or CLI change outside the process | **Revert** or **codify** after review with the person who made it |
| C. Controller-owned field | Autoscaler, operator or service manages the value | **Hand ownership** to the controller (Step 4 ignore rule) |
| D. Provider or API change | New defaults or computed attributes after an upgrade | **Codify** explicit values, or pin the provider until reviewed |
| E. Deleted out of band | Resource exists in code and state but not in reality | **Recreate** via apply, or **remove** from code if no longer needed |
| F. Created out of band | Resource exists in reality but not in code | **Import** into code, or delete after confirming it is unused |
| G. Suspicious | No matching change request, unexpected identity, or weakens security | **Security incident**: preserve evidence, escalate, do not silently revert |

### Step 6: Reconcile, one decision per item

All reconciliation goes through the normal reviewed change process.

- **Revert:** run the standard plan and apply through a pull request. Read the plan for
  replacements (`-/+` or "must be replaced") and destroys before approving; drift on an
  immutable attribute can force a replacement.
- **Codify:** change the code to match reality, then plan. The target is "no changes".
- **Import (Terraform/OpenTofu):** prefer declarative `import` blocks (Terraform 1.5+;
  verify OpenTofu support for your version) in a reviewed change. `terraform plan
  -generate-config-out=<file>` can draft configuration for imported resources; review it
  before committing. Pulumi offers `pulumi import`.
- **Accept real values into state only:** `terraform apply -refresh-only` updates state
  to match reality without changing infrastructure. Use it only when reality is correct
  and code already agrees; it will also accept an unauthorised change into state, so
  never use it on class G.
- **Remove from management:** prefer a reviewed `removed` block (newer Terraform
  versions; verify) over `terraform state rm`. Back up state first
  (`terraform state pull > state-backup-<date>.tfstate`).

After reconciling, re-run the detection command; it must exit 0 (no changes).

### Step 7: Prevent recurrence

- Restrict console write access in production to a break-glass role that is logged and
  time-limited.
- Add a postmortem action item for every class A drift: "codify within N days".
- Track drift count per stack over time; a rising trend indicates a process problem, not
  an individual one.
- Allow automatic reconciliation (for example GitOps self-heal) only for classes where
  reverting is always safe, and not for stateful resources.

## Verification

- [ ] Every workspace/stack has a scheduled read-only detection job
- [ ] The job fails loudly on tool errors (exit code 1), not only on drift
- [ ] Perpetual noise removed; every ignore rule has a reason and an owner
- [ ] Each drifted item has a class and a recorded decision
- [ ] Detection re-run after reconciliation returns no changes
- [ ] Security-relevant drift pages; the rest creates tickets

## Common Failure Modes

| Symptom | Cause | Fix |
|---|---|---|
| Drift job always green, but drift exists | Errors (exit 1) treated as success; or job scoped to one workspace | Fail on exit 1; one job per workspace |
| Routine apply reverts an incident fix | Hotfix never codified | Class A rule: codify before the next apply; block applies with open class A items |
| Team ignores drift reports | Perpetual noise | Step 4 before anything else |
| Real drift hidden for months | Broad `ignore_changes` | Narrow to specific attributes; review ignore rules quarterly |
| Drift job blocks deployments | Job takes the state lock | `-lock=false` for detection, scheduled outside apply windows |
| Unauthorised change quietly absorbed | `apply -refresh-only` or auto-sync used on a class G item | Triage before reconciling; class G goes to the security process |

## Safety & Constraints

**NEVER:**
- Give the drift job apply or write credentials
- Reconcile production with `-auto-approve` or an unreviewed plan
- Run `terraform state rm`, `apply -refresh-only` or a revert on a suspicious change before
  the security owner has seen it
- Edit state files by hand

**ALWAYS:**
- Back up state before any state operation
- Read the plan for destroys and replacements before approving a revert
- Record each reconciliation decision, with its class, in the ticket

## Related Skills

- `executable-runbook-authoring`: runbooks that make manual changes should end with a
  "codify or revert" step that feeds this procedure
- `terraform-module-library` (cloud-infrastructure): module structure that reduces drift-prone defaults
- `gitops-workflow` (cloud-infrastructure): GitOps setup whose sync status is the Kubernetes drift signal
- `postmortem-writing`: incident hotfixes become codify action items
