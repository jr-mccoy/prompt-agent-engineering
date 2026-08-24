---
title: "Chaos Engineering Test Plan"
category: testing
description: "Design a chaos engineering program: hypothesis-driven experiments, blast-radius control, steady-state metrics, game-day scheduling, and tool selection (Chaos Mesh, LitmusChaos, Gremlin, AWS FIS)."
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
  - testing
  - chaos-engineering
  - resilience
  - sre
  - game-day
  - chaos-mesh
  - litmus
  - aws-fis
  - blast-radius
updated: "2026-04-17"
related_prompts:
  - testing_performance_load_test_planning.md
  - ../devops/devops_monitoring_observability.md
  - ../cloud/cloud_aws_architecture_review.md
---

# Chaos Engineering Test Plan

**Objective:** Design a hypothesis-driven chaos engineering program that validates the system's resilience claims (SLOs, recovery time, graceful degradation) through controlled fault injection, without causing production incidents.

## When to Use

- Production systems with 99.9%+ availability targets that have not been stress-tested for real failure modes.
- After a postmortem where the team said "we didn't know X could fail that way."
- Before launching multi-region / multi-AZ / microservice architectures.
- As part of SRE / resilience program establishment.

**Do NOT use this prompt for:**
- Load / stress testing (use `testing_performance_load_test_planning.md`).
- Unit or integration testing.
- First-time reliability work — establish monitoring & SLOs first (use `devops_monitoring_observability.md`).

## Inputs / Context

Collect:
- **Architecture**: monolith / microservices / serverless / hybrid; cloud provider(s).
- **Reliability targets**: documented SLOs, current SLIs, error budget.
- **Observability maturity**: metrics (yes/no), traces (yes/no), logs, dashboards, on-call runbooks.
- **Blast-radius constraints**: can we test in prod? Single-tenant? Multi-tenant?
- **Team readiness**: game-day experience, incident command, communication channels.
- **Tool fit**: Kubernetes → Chaos Mesh / LitmusChaos; cloud-agnostic → Gremlin; AWS → AWS FIS; manual → scripted fault injection.

## Must / Must Not

**Must:**
- Follow the **Principles of Chaos Engineering** (Basiri et al.): hypothesis-driven, minimize blast radius, run in production (eventually), automate.
- Define **steady-state** in measurable terms (SLI, RPS, p99 latency, error rate) BEFORE every experiment.
- Specify **blast-radius controls**: scope (canary / single-AZ / single-service), duration, user impact ceiling.
- Include **abort conditions**: auto-halt triggers on SLO breach, manual kill-switch, rollback plan.
- Progress through maturity stages:
  1. Staging-only
  2. Production canary (narrow scope)
  3. Production broader (with automated aborts)
  4. Continuous / game-day cadence
- Require a **hypothesis per experiment**: "We believe X happens when Y fails. If wrong, we learn Z."

**Must Not:**
- Run chaos without observability — you can't detect the blast radius you're supposed to control.
- Skip the hypothesis step and just "break stuff."
- Run in production without executive & customer-facing team awareness.
- Treat chaos as load testing (different goal).
- Forget the **game-day** discipline: communication, incident-commander role, scribe, post-experiment review.
- Design experiments without a **recovery-time measurement** — the goal is to verify recovery mechanisms work.

## Instructions

1. **Inventory failure domains**: dependency outages (DB, cache, queue, downstream service), infra faults (AZ loss, node loss, network partition, disk full), resource exhaustion (CPU, memory, FD), clock skew, DNS failure, TLS expiry.
2. **Rank by risk × uncertainty**: prioritize experiments where failure is most likely AND least understood.
3. **Design experiments** — for each:
   - Hypothesis ("we believe...").
   - Steady-state metric.
   - Fault to inject (latency / error / kill / partition / resource pressure).
   - Blast radius (scope, duration, user-impact ceiling).
   - Abort conditions (auto + manual).
   - Expected recovery time.
4. **Select tool per fault type**:
   - Network: Chaos Mesh (Pod/Network chaos), Toxiproxy.
   - Node/pod: Chaos Mesh, LitmusChaos, kill scripts.
   - AWS primitives: AWS FIS.
   - Cross-cloud: Gremlin, Steadybit.
   - Application-level: Chaos Monkey, custom in-process injection.
5. **Define game-day protocol**: participants, roles (conductor, scribe, comms, IC), duration, comms channels, post-review template.
6. **Automate** the stable, low-blast experiments into continuous chaos; keep novel / high-blast experiments as scheduled game-days.

## Output Format

```
# Chaos Engineering Plan — <System>

## Baseline
- SLOs: <list>
- Current SLIs & error budget: <state>
- Observability readiness: <Y/N per pillar>
- Team readiness: <game-day experience>

## Failure Domain Map
| Domain | Blast radius | Likelihood | Recovery SLA | Priority |
|--------|-------------|-----------|-------------|----------|
| DB primary loss | region | low | < 60s | P1 |
| Cache warm loss | tier | high | < 5s | P2 |
| Single-AZ network partition | AZ | low | < 2min | P1 |
...

## Experiment Catalog

### Experiment 1: Cache Tier Latency Injection
- **Hypothesis**: Frontend p99 latency stays within SLO when cache tier adds 500ms latency, because we have in-process fallback.
- **Steady-state**: p99 < 300ms, error rate < 0.1%.
- **Fault**: 500ms injected latency on Redis read (Chaos Mesh NetworkChaos).
- **Blast radius**: 1% of pods in canary; 5 min duration; max user impact 0.2% error-rate increase.
- **Abort**: auto-abort on error rate > 0.5% or p99 > 600ms.
- **Expected recovery**: immediate on fault removal.
- **Learning target**: Does fallback activate? Is there a latency cliff?

...

## Game-Day Schedule
- Frequency: <monthly / quarterly>
- Participants: <SRE, service owners, on-call, IC>
- Comms: <#channel>, <incident doc template>

## Automation Target (Stage 3)
<which experiments will run continuously once proven stable>
```

## Verification (Self-Check)

Before emitting:

1. Observability-readiness checked; if pillars missing, recommend stabilizing them first.
2. Every experiment has a falsifiable hypothesis.
3. Every experiment has an abort condition (auto + manual).
4. Blast radius is quantitative (pods, percentage, duration, user-impact ceiling).
5. Recovery-time expectation is stated per experiment.
6. Production experiments require stakeholder awareness; this is called out.
7. Confidence per experiment design (High if similar systems well-studied; Medium if novel fault).

## False-Positive Prevention

Rule out:

- **"Run chaos in prod right away"** — Only after staging validates the experiment and observability is proven.
- **"No observability, start small"** — No — establish observability first, or you can't control blast radius.
- **"Kill a pod to test resilience"** — Trivial; likely already tested by deploy/rolling updates. Aim for subtler faults (latency, partial error, slow failover).
- **"We need a tool first"** — Start with scripts for low-complexity experiments; adopt platforms as scale demands.
- **"Monthly game-day is enough"** — Depends on deploy frequency and architecture changes; high-change systems need more frequent validation.
- **"Chaos replaces postmortems"** — Complementary, not substitutes.

Cap confidence at **Medium** if you did not inspect current observability or incident-response maturity; recommend pre-requisite work in that case.

## Techniques Applied

ST-01, ST-02, ST-03, RT-02, RT-05, CM-02, QA-01.
