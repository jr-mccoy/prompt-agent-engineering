---
title: "OpenTelemetry Instrumentation Review"
category: devops
description: "Review or design OpenTelemetry instrumentation: signal coverage (traces, metrics, logs), SDK vs auto-instrumentation, collector architecture, sampling, cardinality control, and backend integration."
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
  - observability
  - opentelemetry
  - tracing
  - metrics
  - logs
  - collector
  - sampling
  - cardinality
updated: "2026-04-17"
related_prompts:
  - devops_monitoring_observability.md
  - monitoring_solo_dev_alerting.md
  - ../analysis/architecture/architecture_context_observability.md
---

# OpenTelemetry Instrumentation Review

**Objective:** Review or design an OpenTelemetry (OTel) instrumentation plan covering traces, metrics, and logs: SDK configuration, auto-instrumentation coverage, collector topology, sampling strategy, cardinality control, and backend (Jaeger / Tempo / Datadog / Honeycomb / Grafana Cloud) integration.

## When to Use

- Starting observability from zero and choosing a vendor-neutral foundation.
- Migrating from vendor-specific agents (Datadog APM, New Relic, Dynatrace) to OTel.
- When distributed-tracing coverage has gaps (orphan spans, missing parent context).
- When metric costs are runaway due to high-cardinality labels.
- When log-trace correlation doesn't work end to end.

**Do NOT use this prompt for:**
- Monitoring strategy / alerting design (use `devops_monitoring_observability.md`).
- SLO definition.
- Vendor-specific APM tuning (without OTel as the base).

## Inputs / Context

Collect:
- **Languages / runtimes**: Python, Node, Go, JVM, .NET, Rust.
- **Deployment**: VMs / K8s / serverless / edge.
- **Current state**: which signals exist, which vendor backends, whether OTel SDK/collector is already used.
- **Throughput scale**: RPS, span count, metric series count.
- **Cost constraints**: backend pricing model (cardinality-based, ingest-based, retention-based).
- **Regulatory**: any restrictions on log/trace content (PII redaction required?).

## Must / Must Not

**Must:**
- Cover all **three signals** (traces, metrics, logs) — state the coverage and gap explicitly.
- Prefer **auto-instrumentation** where available (JVM, Node, Python, .NET) and supplement with manual instrumentation for business-critical spans.
- Specify **context propagation**: W3C `traceparent` + `tracestate` (default in OTel v1+); note any legacy Zipkin B3 or Jaeger propagator needs.
- Define **sampling strategy**:
  - **Head-based** (deterministic, probabilistic) for simple cases.
  - **Tail-based** (in collector) for retention of interesting traces (errors, slow).
  - State sampling rate and escape hatches (always-on for specific routes).
- Include a **collector topology**:
  - **Agent (sidecar / DaemonSet)** for collection and lightweight processing.
  - **Gateway** for batching, routing, tail-sampling, multi-backend fan-out.
  - Processors: batch, memory_limiter, resource, attributes, redaction.
- Control **cardinality** on metrics: cap labels (HTTP status code bucketed, tenant ID hashed, user ID NEVER a label).
- Correlate **logs ↔ traces** via `trace_id` / `span_id` injection at log-record time.

**Must Not:**
- Export **high-cardinality labels** (user ID, request ID, full URL path) as metric attributes — use traces for that.
- Ship SDK direct-to-backend from pods in production — always go through a collector (for batching, fallback, redaction).
- Rely on head-based sampling alone when you need to retain all errors / slow traces — use tail-sampling in the collector.
- Instrument without a **schema_url** — makes schema migration painful.
- Use OTLP/HTTP when OTLP/gRPC is available and stable — gRPC is more efficient.
- Skip the **resource** attributes (`service.name`, `service.version`, `deployment.environment`, `k8s.pod.name`) — they're the backbone of correlation.

## Instructions

Work through six phases:

1. **Signal inventory**: what's instrumented, by which library, with which coverage.
2. **SDK + auto-instrumentation**: version pinning, supported libraries, required manual spans.
3. **Context propagation**: headers, legacy propagators, cross-boundary (HTTP / gRPC / messaging).
4. **Collector topology**: agent → gateway → backend; processors; redundancy; backpressure.
5. **Sampling & cardinality**: head vs tail, percentage, high-value traces retained, metric label hygiene.
6. **Backend integration & cost**: ingestion format (OTLP preferred), retention, cost controls, dashboards.

## Output Format

```
# OpenTelemetry Review — <Service / Platform>

## Signal Coverage
| Signal | Coverage | Gaps |
|--------|----------|------|
| Traces | 80% of HTTP paths auto-instrumented | DB driver not auto-instrumented; manual spans needed |
| Metrics | Runtime metrics only | No business metrics |
| Logs | Not OTel-formatted | Logs not correlated with traces |

## Collector Topology
- **Agent**: <sidecar / DaemonSet / host agent>
- **Gateway**: <deployment; replicas; resources>
- **Processors**: <ordered list>
- **Exporters**: <backends>

## Sampling Strategy
- **Head-based**: <10% default>
- **Tail-based**: <always sample errors, p99 > SLO, specific business-critical traces>
- **Escape hatch**: <routes always sampled>

## Cardinality Policy
- Allowed labels: <list>
- Forbidden labels: <list — user ID, request ID, full URL>
- Hashing rules: <e.g., tenant_id hashed at ingest>

## Findings
### [Critical] Direct-to-backend export from prod pods
- **Evidence**: <config file>
- **Risk**: no batching, no fallback, per-pod vendor auth — outage = lost signals.
- **Fix**: deploy OTel Collector as sidecar + gateway.

...

## Remediation Plan
1. <Critical, < 1 week>
2. <High, 1–4 weeks>
3. <Medium, next quarter>
```

## Verification (Self-Check)

Before emitting:

1. All three signals addressed (trace, metric, log) — not just traces.
2. Collector topology is concrete (diagram / YAML pointers).
3. Sampling is specified per signal type.
4. Cardinality rules list forbidden labels explicitly.
5. Log-trace correlation path is stated.
6. Schema_url and resource attributes referenced.
7. Confidence (High if inspected live config; Medium if inferred from code).

## False-Positive Prevention

Rule out:

- **"High cardinality is inherent"** — Metrics should be bounded-cardinality; traces carry the high-cardinality context. Don't mix them.
- **"Auto-instrumentation is enough"** — No — business-critical spans (payment authorized, order placed) must be manual.
- **"Tail-sampling is always needed"** — Only if head-sampling drops too many interesting traces; head is simpler at low scale.
- **"OTel SDK direct export is fine in dev"** — Fine for dev, not prod. Never mix the two configs.
- **"Logs don't need correlation"** — They do, for any distributed system.
- **"One collector is enough"** — Multi-replica gateway for resilience; backpressure matters at scale.

Cap confidence at **Medium** if collector config was not inspected; Low if only docs were read.

## Techniques Applied

ST-01, ST-02, ST-03, RT-02 (6-phase), RT-05, CM-02, QA-01.
