# OpenTelemetry Setup — Context Propagation, Log Correlation, Sampling & Integration Patterns

## Context Propagation

**Purpose:** Pass trace context across service boundaries

**HTTP propagation (automatic with instrumentation):**
```typescript
// Outgoing requests automatically include trace headers
// W3C Trace Context headers:
// - traceparent: 00-{trace-id}-{span-id}-{flags}
// - tracestate: optional vendor-specific data
```

**Manual propagation:**
```typescript
import { context, propagation, trace } from '@opentelemetry/api';

// Inject context into carrier (e.g., message queue)
function sendMessage(message: any) {
  const carrier: Record<string, string> = {};
  propagation.inject(context.active(), carrier);

  await queue.send({
    ...message,
    headers: carrier,
  });
}

// Extract context from carrier
function handleMessage(message: any) {
  const ctx = propagation.extract(context.active(), message.headers);

  return context.with(ctx, () => {
    return tracer.startActiveSpan('process-message', async (span) => {
      // Process message
      span.end();
    });
  });
}
```

---

## Log Correlation

**Purpose:** Connect logs to traces for unified observability

**With Pino:**
```typescript
import pino from 'pino';
import { trace, context } from '@opentelemetry/api';

const logger = pino({
  mixin() {
    const span = trace.getSpan(context.active());
    if (span) {
      const spanContext = span.spanContext();
      return {
        trace_id: spanContext.traceId,
        span_id: spanContext.spanId,
        trace_flags: spanContext.traceFlags,
      };
    }
    return {};
  },
});

// Logs automatically include trace context
logger.info('Processing order'); // { trace_id: '...', span_id: '...', msg: 'Processing order' }
```

**With Winston:**
```typescript
import winston from 'winston';
import { trace, context } from '@opentelemetry/api';

const logger = winston.createLogger({
  format: winston.format.combine(
    winston.format((info) => {
      const span = trace.getSpan(context.active());
      if (span) {
        const spanContext = span.spanContext();
        info.trace_id = spanContext.traceId;
        info.span_id = spanContext.spanId;
      }
      return info;
    })(),
    winston.format.json()
  ),
  transports: [new winston.transports.Console()],
});
```

---

## Sampling Configuration

**Purpose:** Control what telemetry data is collected

```typescript
import { NodeSDK } from '@opentelemetry/sdk-node';
import {
  AlwaysOnSampler,
  AlwaysOffSampler,
  TraceIdRatioBasedSampler,
  ParentBasedSampler,
} from '@opentelemetry/sdk-trace-node';

// Always sample (development)
const alwaysOn = new AlwaysOnSampler();

// Never sample
const alwaysOff = new AlwaysOffSampler();

// Sample 10% of traces
const ratioSampler = new TraceIdRatioBasedSampler(0.1);

// Respect parent decision, with fallback to ratio
const parentBasedSampler = new ParentBasedSampler({
  root: new TraceIdRatioBasedSampler(0.1),
  remoteParentSampled: new AlwaysOnSampler(),
  remoteParentNotSampled: new AlwaysOffSampler(),
});

const sdk = new NodeSDK({
  sampler: process.env.NODE_ENV === 'production'
    ? parentBasedSampler
    : alwaysOn,
  // ...
});
```

---

## Integration Patterns

### With Express

```typescript
// Auto-instrumented with @opentelemetry/auto-instrumentations-node
// Manual middleware for custom attributes:
app.use((req, res, next) => {
  const span = trace.getSpan(context.active());
  if (span) {
    span.setAttribute('user.id', req.user?.id);
    span.setAttribute('tenant.id', req.headers['x-tenant-id']);
  }
  next();
});
```

### With Grafana Stack (Tempo + Loki + Prometheus)

```yaml
# docker-compose.yml
services:
  tempo:
    image: grafana/tempo:latest
    command: ['-config.file=/etc/tempo.yaml']
    volumes:
      - ./tempo.yaml:/etc/tempo.yaml
    ports:
      - '4317:4317'
      - '4318:4318'

  prometheus:
    image: prom/prometheus:latest
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml

  grafana:
    image: grafana/grafana:latest
    ports:
      - '3000:3000'
    environment:
      - GF_AUTH_ANONYMOUS_ENABLED=true
```

---

## Version Compatibility

| OpenTelemetry Version | Status | Notable Changes |
|----------------------|--------|-----------------|
| 1.x (2024+) | Current | Stable APIs, logs support |
| 0.x | Deprecated | Breaking changes expected |
