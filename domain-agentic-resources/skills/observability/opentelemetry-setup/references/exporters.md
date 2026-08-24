# OpenTelemetry Exporters Reference

## OTLP (OpenTelemetry Protocol)

The standard protocol for exporting telemetry. Works with most backends.

### OTLP HTTP

```typescript
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-http';
import { OTLPMetricExporter } from '@opentelemetry/exporter-metrics-otlp-http';

const traceExporter = new OTLPTraceExporter({
  url: 'http://localhost:4318/v1/traces',
  headers: {
    'Authorization': 'Bearer token',
  },
  timeoutMillis: 30000,
});

const metricExporter = new OTLPMetricExporter({
  url: 'http://localhost:4318/v1/metrics',
});
```

### OTLP gRPC

```typescript
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-grpc';

const traceExporter = new OTLPTraceExporter({
  url: 'http://localhost:4317',
  credentials: grpc.credentials.createInsecure(),
});
```

## Jaeger

```typescript
import { JaegerExporter } from '@opentelemetry/exporter-jaeger';

const jaegerExporter = new JaegerExporter({
  endpoint: 'http://localhost:14268/api/traces',
  // Or use agent
  // host: 'localhost',
  // port: 6832,
});
```

## Zipkin

```typescript
import { ZipkinExporter } from '@opentelemetry/exporter-zipkin';

const zipkinExporter = new ZipkinExporter({
  url: 'http://localhost:9411/api/v2/spans',
  serviceName: 'my-service',
});
```

## Prometheus (Metrics)

```typescript
import { PrometheusExporter } from '@opentelemetry/exporter-prometheus';

const prometheusExporter = new PrometheusExporter({
  port: 9464,
  endpoint: '/metrics',
  preventServerStart: false,
});

// Access metrics at http://localhost:9464/metrics
```

## Console (Development)

```typescript
import { ConsoleSpanExporter } from '@opentelemetry/sdk-trace-base';
import { ConsoleMetricExporter } from '@opentelemetry/sdk-metrics';

// Prints spans to console
const consoleTraceExporter = new ConsoleSpanExporter();

// Prints metrics to console
const consoleMetricExporter = new ConsoleMetricExporter();
```

## Cloud Providers

### Google Cloud Trace

```typescript
import { TraceExporter } from '@google-cloud/opentelemetry-cloud-trace-exporter';

const gcpExporter = new TraceExporter({
  projectId: 'my-project',
});
```

### AWS X-Ray

```typescript
import { AWSXRayIdGenerator } from '@opentelemetry/id-generator-aws-xray';
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-http';

const sdk = new NodeSDK({
  idGenerator: new AWSXRayIdGenerator(),
  traceExporter: new OTLPTraceExporter({
    url: 'http://localhost:4318/v1/traces', // AWS Distro collector
  }),
});
```

### Azure Monitor

```typescript
import { AzureMonitorTraceExporter } from '@azure/monitor-opentelemetry-exporter';

const azureExporter = new AzureMonitorTraceExporter({
  connectionString: process.env.APPLICATIONINSIGHTS_CONNECTION_STRING,
});
```

### Datadog

```typescript
// Via OTLP to Datadog Agent
const datadogExporter = new OTLPTraceExporter({
  url: 'http://localhost:4318/v1/traces',
  headers: {
    'DD-API-KEY': process.env.DD_API_KEY,
  },
});
```

## Batching Configuration

```typescript
import { BatchSpanProcessor } from '@opentelemetry/sdk-trace-base';

const batchProcessor = new BatchSpanProcessor(traceExporter, {
  maxQueueSize: 2048,
  maxExportBatchSize: 512,
  scheduledDelayMillis: 5000,
  exportTimeoutMillis: 30000,
});
```

## Multiple Exporters

```typescript
import { SimpleSpanProcessor, BatchSpanProcessor } from '@opentelemetry/sdk-trace-base';

const sdk = new NodeSDK({
  spanProcessors: [
    // Console for development
    new SimpleSpanProcessor(new ConsoleSpanExporter()),
    // OTLP for production
    new BatchSpanProcessor(new OTLPTraceExporter()),
  ],
});
```
