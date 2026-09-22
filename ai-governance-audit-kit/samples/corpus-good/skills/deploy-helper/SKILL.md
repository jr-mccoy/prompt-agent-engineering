---
name: deploy-helper
description: Prepares and validates a staged deployment, then reports what would change before anything is applied. Use this skill when the user asks to "deploy to staging", "check a release before shipping", "dry-run a deploy", or mentions release validation, rollout checks or deployment preflight.
tags:
  - deployment
  - release
  - preflight
updated: "2026-06-18"
---

<!-- SYNTHETIC TEST FIXTURE — NOT INDEPENDENT BENCHMARK EVIDENCE -->

# Deploy Helper

Prepare a staged deployment, validate it, and report the diff before applying.

## When to Use

- A release is ready and someone needs to see what will change.
- A deploy failed and you want the preflight output for the next attempt.

## When NOT to Use

- Production rollback — that has its own runbook and approval path.
- Infrastructure provisioning, which is a different tool entirely.

## Instructions

1. Read the target environment from `DEPLOY_ENV`; never hardcode it.
2. Read credentials from the environment (`DEPLOY_TOKEN`), never from a file.
3. Run `scripts/deploy.py --plan` and capture the planned change set.
4. Present the change set and stop. Applying requires explicit confirmation.

### Worked example

```
$ DEPLOY_ENV=staging python3 scripts/deploy.py --plan
plan against staging
```

## Safety

Applying a deploy is destructive and requires an explicit confirmation step.
The plan step is read-only and safe to run repeatedly. A partial apply is
reversible through the environment's own rollback path.

## Bundled Resources

- `scripts/deploy.py` — plan and apply, with `--plan` as the default.
- `references/environments.md` — the environment matrix and its owners.

## Troubleshooting

- Plan fails with no output: the environment name is unset or misspelled.
- Partial apply: re-run `--plan` to see remaining drift, then apply again.

## Related Skills

- Incident response, for when an applied deploy goes wrong.

## Verification

- [ ] The plan names every resource that would change.
- [ ] No credential appears in the output.
