/**
 * OpenTelemetry Instrumentation Setup
 *
 * IMPORTANT: This file MUST be imported BEFORE any other application code.
 *
 * Usage:
 *   // In your entry point (e.g., src/index.ts)
 *   import './instrumentation'; // First import!
 *   import express from 'express';
 *   // ... rest of your app
 */

import { NodeSDK } from '@opentelemetry/sdk-node';
import { getNodeAutoInstrumentations } from '@opentelemetry/auto-instrumentations-node';
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-http';
import { OTLPMetricExporter } from '@opentelemetry/exporter-metrics-otlp-http';
import {
  PeriodicExportingMetricReader,
  ConsoleMetricExporter,
} from '@opentelemetry/sdk-metrics';
import { Resource } from '@opentelemetry/resources';
import {
  SEMRESATTRS_SERVICE_NAME,
  SEMRESATTRS_SERVICE_VERSION,
  SEMRESATTRS_DEPLOYMENT_ENVIRONMENT,
} from '@opentelemetry/semantic-conventions';
import {
  ParentBasedSampler,
  TraceIdRatioBasedSampler,
  AlwaysOnSampler,
} from '@opentelemetry/sdk-trace-node';
import { diag, DiagConsoleLogger, DiagLogLevel } from '@opentelemetry/api';

// Enable debug logging in development
if (process.env.OTEL_LOG_LEVEL === 'debug') {
  diag.setLogger(new DiagConsoleLogger(), DiagLogLevel.DEBUG);
}

// Service identification
const serviceName = process.env.OTEL_SERVICE_NAME ?? 'my-service';
const serviceVersion = process.env.SERVICE_VERSION ?? '1.0.0';
const environment = process.env.NODE_ENV ?? 'development';

// Resource attributes
const resource = new Resource({
  [SEMRESATTRS_SERVICE_NAME]: serviceName,
  [SEMRESATTRS_SERVICE_VERSION]: serviceVersion,
  [SEMRESATTRS_DEPLOYMENT_ENVIRONMENT]: environment,
  // Add custom attributes
  'service.team': process.env.TEAM_NAME ?? 'platform',
});

// Exporter configuration
const otlpEndpoint =
  process.env.OTEL_EXPORTER_OTLP_ENDPOINT ?? 'http://localhost:4318';

const traceExporter = new OTLPTraceExporter({
  url: `${otlpEndpoint}/v1/traces`,
  headers: process.env.OTEL_EXPORTER_OTLP_HEADERS
    ? JSON.parse(process.env.OTEL_EXPORTER_OTLP_HEADERS)
    : {},
});

const metricExporter =
  environment === 'development'
    ? new ConsoleMetricExporter()
    : new OTLPMetricExporter({
        url: `${otlpEndpoint}/v1/metrics`,
      });

// Sampling configuration
const sampler =
  environment === 'production'
    ? new ParentBasedSampler({
        root: new TraceIdRatioBasedSampler(0.1), // 10% sampling in production
      })
    : new AlwaysOnSampler(); // 100% in development

// Initialize SDK
const sdk = new NodeSDK({
  resource,
  traceExporter,
  sampler,
  metricReader: new PeriodicExportingMetricReader({
    exporter: metricExporter,
    exportIntervalMillis: environment === 'production' ? 60000 : 10000,
  }),
  instrumentations: [
    getNodeAutoInstrumentations({
      // Disable noisy instrumentations
      '@opentelemetry/instrumentation-fs': { enabled: false },
      '@opentelemetry/instrumentation-dns': { enabled: false },
      // Configure HTTP instrumentation
      '@opentelemetry/instrumentation-http': {
        ignoreIncomingPaths: ['/health', '/ready', '/metrics'],
        requestHook: (span, request) => {
          // Add custom attributes from request
          const tenantId = request.headers?.['x-tenant-id'];
          if (tenantId) {
            span.setAttribute('tenant.id', tenantId as string);
          }
        },
      },
      // Configure Express instrumentation
      '@opentelemetry/instrumentation-express': {
        ignoreLayersType: ['middleware'],
      },
    }),
  ],
});

// Start SDK
sdk.start();

console.log(`OpenTelemetry initialized for ${serviceName} (${environment})`);
console.log(`Exporting to: ${otlpEndpoint}`);

// Graceful shutdown
const shutdown = async () => {
  console.log('Shutting down OpenTelemetry SDK...');
  try {
    await sdk.shutdown();
    console.log('OpenTelemetry SDK shut down successfully');
  } catch (error) {
    console.error('Error shutting down OpenTelemetry SDK:', error);
  }
  process.exit(0);
};

process.on('SIGTERM', shutdown);
process.on('SIGINT', shutdown);

// Export for testing
export { sdk, resource };
