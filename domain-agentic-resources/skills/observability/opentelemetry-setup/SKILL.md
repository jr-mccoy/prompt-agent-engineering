---
name: opentelemetry-setup
description: Master OpenTelemetry for implementing distributed tracing, metrics, and logging in cloud-native applications. Use this skill when setting up observability infrastructure, debugging distributed systems, or when users mention "OpenTelemetry", "OTel", "distributed tracing", "spans", "traces", "telemetry", "OTLP", or "observability".
metadata:
  tags:
    - debugging
    - logging
    - monitoring
    - observability
    - opentelemetry
    - setup
  updated: "2026-04-11"
---
# OpenTelemetry Setup

OpenTelemetry (OTel) is the industry-standard observability framework for instrumenting, generating, collecting, and exporting telemetry data (traces, metrics, logs) from cloud-native software.

## Purpose

This skill provides comprehensive guidance for implementing OpenTelemetry in applications and infrastructure, including SDK setup, automatic instrumentation, custom spans, metrics collection, log correlation, and integration with observability backends (Jaeger, Prometheus, Grafana). Mastery enables building fully observable distributed systems.

## When to Use This Skill

Use this skill when you need to:
- Implement distributed tracing across microservices
- Set up unified observability (traces + metrics + logs)
- Debug performance issues in distributed systems
- Integrate with observability backends (Jaeger, Zipkin, Grafana Tempo)
- Add custom instrumentation to application code
- User mentions: OpenTelemetry, OTel, distributed tracing, spans, OTLP, observability

## When NOT to Use This Skill

Do NOT use this skill when:
- Building monolithic applications with simple logging → basic logging is sufficient
- Using vendor-specific APM tools → use their SDKs directly
- Need only basic metrics → use `prometheus-configuration` skill
- Setting up Grafana dashboards → use `grafana-dashboards` skill

## Prerequisites

- **Language:** Node.js 18+, Python 3.8+, Go 1.19+, Java 11+
- **Knowledge:** Basic understanding of distributed systems
- **Infrastructure:** Backend for telemetry (Jaeger, Prometheus, etc.)

**Verify installation (Node.js):**
```bash
npm list @opentelemetry/sdk-node
# Expected: @opentelemetry/sdk-node@1.x.x
```

---

## Quick Reference

### Most Common Operations

| Task | Command/Pattern | Notes |
|------|-----------------|-------|
| Install SDK (Node.js) | `npm i @opentelemetry/sdk-node @opentelemetry/auto-instrumentations-node` | Core + auto instrumentation |
| Start tracing | Initialize SDK before app imports | Must be first |
| Create span | `tracer.startSpan('name')` | Manual instrumentation |
| Add attributes | `span.setAttribute('key', value)` | Enrich spans |
| Export to Jaeger | Configure OTLP exporter | Standard protocol |

### OpenTelemetry Signals

| Signal | Purpose | Example |
|--------|---------|---------|
| Traces | Request flow across services | API call → DB → cache → response |
| Metrics | Numerical measurements | Request count, latency histogram |
| Logs | Structured event records | Correlated with trace context |

### Core Concepts

| Concept | Description |
|---------|-------------|
| Span | Single unit of work (operation) |
| Trace | Collection of spans forming a request path |
| Context | Propagation of trace info across boundaries |
| Exporter | Sends telemetry to backends |
| Sampler | Controls what data is collected |

---

## Core Operations

### Operation: Install and Initialize (Node.js)

**Purpose:** Set up OpenTelemetry SDK with automatic instrumentation

**Install dependencies:**
```bash
npm install @opentelemetry/sdk-node \
  @opentelemetry/auto-instrumentations-node \
  @opentelemetry/exporter-trace-otlp-http \
  @opentelemetry/exporter-metrics-otlp-http \
  @opentelemetry/resources \
  @opentelemetry/semantic-conventions
```

**Create instrumentation file (MUST be imported first):**
```typescript
// src/instrumentation.ts
import { NodeSDK } from '@opentelemetry/sdk-node';
import { getNodeAutoInstrumentations } from '@opentelemetry/auto-instrumentations-node';
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-http';
import { OTLPMetricExporter } from '@opentelemetry/exporter-metrics-otlp-http';
import { PeriodicExportingMetricReader } from '@opentelemetry/sdk-metrics';
import { Resource } from '@opentelemetry/resources';
import {
  SEMRESATTRS_SERVICE_NAME,
  SEMRESATTRS_SERVICE_VERSION,
  SEMRESATTRS_DEPLOYMENT_ENVIRONMENT,
} from '@opentelemetry/semantic-conventions';

const resource = new Resource({
  [SEMRESATTRS_SERVICE_NAME]: 'my-service',
  [SEMRESATTRS_SERVICE_VERSION]: '1.0.0',
  [SEMRESATTRS_DEPLOYMENT_ENVIRONMENT]: process.env.NODE_ENV ?? 'development',
});

const traceExporter = new OTLPTraceExporter({
  url: process.env.OTEL_EXPORTER_OTLP_ENDPOINT ?? 'http://localhost:4318/v1/traces',
});

const metricExporter = new OTLPMetricExporter({
  url: process.env.OTEL_EXPORTER_OTLP_ENDPOINT ?? 'http://localhost:4318/v1/metrics',
});

const sdk = new NodeSDK({
  resource,
  traceExporter,
  metricReader: new PeriodicExportingMetricReader({
    exporter: metricExporter,
    exportIntervalMillis: 10000,
  }),
  instrumentations: [
    getNodeAutoInstrumentations({
      '@opentelemetry/instrumentation-fs': { enabled: false },
    }),
  ],
});

sdk.start();

process.on('SIGTERM', () => {
  sdk.shutdown()
    .then(() => console.log('SDK shut down'))
    .catch((error) => console.error('Error shutting down', error))
    .finally(() => process.exit(0));
});

export { sdk };
```

**Import before application code:**
```typescript
// src/index.ts
import './instrumentation'; // MUST be first import

import express from 'express';
// ... rest of application
```

---

### Operation: Manual Span Creation

**Purpose:** Add custom instrumentation to code

**Basic span:**
```typescript
import { trace, SpanStatusCode } from '@opentelemetry/api';

const tracer = trace.getTracer('my-service', '1.0.0');

async function processOrder(orderId: string) {
  const span = tracer.startSpan('process-order');

  try {
    span.setAttribute('order.id', orderId);

    const result = await executeOrder(orderId);

    span.setAttribute('order.status', result.status);
    span.setStatus({ code: SpanStatusCode.OK });

    return result;
  } catch (error) {
    span.setStatus({
      code: SpanStatusCode.ERROR,
      message: error.message,
    });
    span.recordException(error);
    throw error;
  } finally {
    span.end();
  }
}
```

**Nested spans (child spans):**
```typescript
async function processOrder(orderId: string) {
  return tracer.startActiveSpan('process-order', async (span) => {
    try {
      span.setAttribute('order.id', orderId);

      await tracer.startActiveSpan('validate-order', async (childSpan) => {
        await validateOrder(orderId);
        childSpan.end();
      });

      await tracer.startActiveSpan('charge-payment', async (childSpan) => {
        await chargePayment(orderId);
        childSpan.end();
      });

      span.setStatus({ code: SpanStatusCode.OK });
    } catch (error) {
      span.setStatus({ code: SpanStatusCode.ERROR, message: error.message });
      throw error;
    } finally {
      span.end();
    }
  });
}
```

**Span events:**
```typescript
span.addEvent('cache-hit', {
  'cache.key': cacheKey,
  'cache.ttl': ttl,
});

span.addEvent('retry-attempt', {
  'retry.count': attemptNumber,
  'retry.reason': 'timeout',
});
```

---

### Operation: Custom Metrics

**Purpose:** Record application-specific measurements

**Setup metrics:**
```typescript
import { metrics, ValueType } from '@opentelemetry/api';

const meter = metrics.getMeter('my-service', '1.0.0');

// Counter (monotonically increasing)
const requestCounter = meter.createCounter('http.requests.total', {
  description: 'Total HTTP requests',
  unit: '1',
});

// Histogram (distribution of values)
const requestDuration = meter.createHistogram('http.request.duration', {
  description: 'HTTP request duration',
  unit: 'ms',
});

// UpDownCounter (can increase or decrease)
const activeConnections = meter.createUpDownCounter('connections.active', {
  description: 'Active connections',
});

// Observable (async) gauge
const memoryUsage = meter.createObservableGauge('process.memory.usage', {
  description: 'Process memory usage',
  unit: 'bytes',
});

memoryUsage.addCallback((result) => {
  result.observe(process.memoryUsage().heapUsed, {
    'memory.type': 'heap',
  });
});
```

**Recording metrics:**
```typescript
requestCounter.add(1, {
  'http.method': 'GET',
  'http.route': '/api/users',
  'http.status_code': 200,
});

const startTime = Date.now();
// ... do work
requestDuration.record(Date.now() - startTime, {
  'http.method': 'GET',
  'http.route': '/api/users',
});

activeConnections.add(1);  // Connection opened
activeConnections.add(-1); // Connection closed
```

---

## Configuration Reference

### Environment Variables

```bash
# Exporter endpoint
OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318

# Service identification
OTEL_SERVICE_NAME=my-service
OTEL_RESOURCE_ATTRIBUTES=deployment.environment=production,service.version=1.0.0

# Trace configuration
OTEL_TRACES_SAMPLER=parentbased_traceidratio
OTEL_TRACES_SAMPLER_ARG=0.1

# Propagators
OTEL_PROPAGATORS=tracecontext,baggage

# Log level
OTEL_LOG_LEVEL=info
```

### Docker Compose with Jaeger

```yaml
version: '3.8'
services:
  app:
    build: .
    environment:
      - OTEL_EXPORTER_OTLP_ENDPOINT=http://jaeger:4318
      - OTEL_SERVICE_NAME=my-service
    depends_on:
      - jaeger

  jaeger:
    image: jaegertracing/all-in-one:latest
    ports:
      - '16686:16686'  # Jaeger UI
      - '4317:4317'    # OTLP gRPC
      - '4318:4318'    # OTLP HTTP
    environment:
      - COLLECTOR_OTLP_ENABLED=true
```

---

## Best Practices

### Do

- **Set meaningful span names:**
  ```typescript
  // Good: Descriptive, follows conventions
  tracer.startSpan('HTTP GET /api/users/:id');
  tracer.startSpan('db.query SELECT users');

  // Bad: Too generic
  tracer.startSpan('request');
  tracer.startSpan('database');
  ```

- **Use semantic conventions for attributes:**
  ```typescript
  import { SEMATTRS_HTTP_METHOD, SEMATTRS_HTTP_URL } from '@opentelemetry/semantic-conventions';

  span.setAttribute(SEMATTRS_HTTP_METHOD, 'GET');
  span.setAttribute(SEMATTRS_HTTP_URL, 'https://api.example.com/users');
  ```

- **Always end spans:**
  ```typescript
  const span = tracer.startSpan('operation');
  try {
    // work
  } finally {
    span.end(); // Always end, even on error
  }
  ```

### Don't

- **Don't create spans for every function:** Only for significant operations
- **Don't log sensitive data in spans:** Avoid PII, passwords, tokens
- **Don't forget to handle errors:** Record exceptions, set error status
- **Don't block on telemetry export:** Use async exporters

### Performance Tips

1. **Use sampling in production** - 10-20% is often sufficient
2. **Batch exports** - Reduce network overhead
3. **Limit attribute count** - Max 128 per span
4. **Use async exporters** - Don't block application code
5. **Disable noisy auto-instrumentations** - fs, dns if not needed

---

## Troubleshooting

### Common Issues

| Symptom | Cause | Solution |
|---------|-------|----------|
| No traces appearing | SDK not initialized first | Import instrumentation.ts before app |
| Missing child spans | Context not propagated | Use `startActiveSpan` |
| High memory usage | Too many spans | Enable sampling |
| Traces not linked | Different trace IDs | Check context propagation |
| Attributes missing | Set after span.end() | Set attributes before ending |

### Diagnostic Commands

```bash
# Check OTLP endpoint
curl -X POST http://localhost:4318/v1/traces \
  -H "Content-Type: application/json" \
  -d '{}'

# View Jaeger traces
open http://localhost:16686

# Check exporter logs
OTEL_LOG_LEVEL=debug node app.js
```

### Debug Mode

```typescript
import { diag, DiagConsoleLogger, DiagLogLevel } from '@opentelemetry/api';

// Enable debug logging
diag.setLogger(new DiagConsoleLogger(), DiagLogLevel.DEBUG);
```

---

## Advanced Configuration

Context propagation (W3C traceparent/tracestate headers; manual inject/extract for message queues via propagation.inject/extract and context.with), log correlation with Pino (mixin adding trace_id/span_id/trace_flags) and Winston (format middleware injecting span context), sampling configuration (AlwaysOnSampler/AlwaysOffSampler/TraceIdRatioBasedSampler/ParentBasedSampler with remote parent handling), integration patterns (Express middleware for custom user/tenant attributes; Grafana Stack docker-compose with Tempo/Prometheus/Grafana), and version compatibility table (1.x stable vs 0.x deprecated).

See [references/advanced-configuration.md](references/advanced-configuration.md)

---

## Reference Files

| Resource | Purpose |
|----------|---------|
| `scripts/validate_setup.sh` | Verify OTel configuration |
| `references/semantic_conventions.md` | Attribute naming standards |
| `references/exporters.md` | Backend-specific setup |
| `references/advanced-configuration.md` | Context propagation, log correlation, sampling, integration patterns |
| `assets/docker-compose.example.yml` | Local development stack |
| `assets/instrumentation.example.ts` | Complete Node.js setup |

## Related Skills

- `prometheus-configuration` - Metrics-only setup
- `grafana-dashboards` - Visualization setup
- `distributed-tracing` - Deep dive on tracing patterns
- `slo-implementation` - Service level objectives
