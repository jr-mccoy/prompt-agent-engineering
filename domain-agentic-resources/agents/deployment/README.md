# Deployment Agents

> Specialized agents for CI/CD pipelines, GitOps workflows, deployment automation, release gating, and rollout monitoring.

## Available Agents

| Agent | Model | Description |
|-------|-------|-------------|
| [deployment-engineer](deployment_engineer.md) | HAIKU | Expert deployment engineer specializing in modern CI/CD pipelines, GitOps workflows, and advanced deployment automation. Masters GitHub Actions, ArgoCD/Flux, and progressive delivery. |
| [release-readiness-gatekeeper](release_readiness_gatekeeper.md) | OPUS | Read-only go/no-go gate for a server-side or web release candidate: test evidence, change scope, migration safety, rollback plan (including what cannot roll back), config/secrets, observability, operational readiness. Defaults to NO-GO when a blocker lacks evidence. |
| [progressive-delivery-controller](progressive_delivery_controller.md) | SONNET | Canary and feature-flag rollout monitor: pre-registered abort/hold/promote criteria, canary-vs-baseline comparison with minimum soak and sample per stage. Advisory; every traffic or flag change needs explicit human confirmation. |

## Model Assignments

- **HAIKU**: Used for fast, efficient deployment automation tasks
- **OPUS**: Used for the release go/no-go gate, where a wrong GO is expensive
- **SONNET**: Used for stage-by-stage rollout evaluation against fixed criteria

## Which agent?

| Situation | Agent |
|-----------|-------|
| Build or fix the pipeline, GitOps, or rollout tooling | deployment-engineer |
| Decide whether a release candidate may go to production | release-readiness-gatekeeper |
| Watch a canary or flag rollout and decide abort / hold / promote | progressive-delivery-controller |

Mobile store releases are out of scope here — see `agents/frontend-mobile/android_release_manager.md`.

## Related Resources

- [Parent: Agents Overview](../README.md)
- [Skills: DevOps](../../skills/devops/)
