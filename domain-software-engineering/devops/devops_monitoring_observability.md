---
title: "Monitoring and Observability Setup Guide"
category: devops
description: "Design monitoring and observability systems for operational visibility and incident response"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-03
difficulty: intermediate
tags:
  - monitoring
  - observability
  - logging
  - metrics
  - alerting
  - sre
updated: "2026-03-19"
---

# Monitoring and Observability Setup Guide

**Objective:** Design and implement comprehensive monitoring, logging, and observability systems for cloud-native applications to ensure operational visibility, rapid incident response, and proactive performance optimization.

**When to Use:** Use this prompt when setting up monitoring for new applications, improving observability coverage, implementing SLO-based alerting, troubleshooting production issues, or establishing monitoring standards for your organization.

**Instructions:**

1. **Metrics Collection Strategy**
   - Define key performance indicators (KPIs) and Service Level Indicators (SLIs)
   - Design metric collection for infrastructure, application, and business layers
   - Review metric naming conventions and cardinality management
   - Analyze metric aggregation and retention strategies
   - Check for proper instrumentation coverage

2. **Logging Architecture**
   - Review log collection and aggregation patterns
   - Analyze log levels and structured logging implementation
   - Check for correlation IDs and distributed tracing integration
   - Review log retention and lifecycle management
   - Analyze log search and analysis capabilities

3. **Distributed Tracing**
   - Design trace collection strategy
   - Review context propagation implementation
   - Analyze sampling strategies for high-volume systems
   - Check for service mesh integration
   - Review trace analysis and visualization

4. **Alerting and Incident Response**
   - Design SLO-based alerting strategies
   - Review alert routing and escalation policies
   - Analyze runbook integration
   - Check for alert fatigue prevention
   - Review incident management integration

5. **Dashboard Design**
   - Review dashboard hierarchy (executive, team, service levels)
   - Analyze USE/RED metrics coverage
   - Check for proper visualization selection
   - Review drill-down capabilities
   - Analyze real-time vs. historical views

6. **Infrastructure Monitoring**
   - Review container and orchestration monitoring
   - Analyze cloud service monitoring coverage
   - Check for infrastructure health indicators
   - Review capacity planning metrics
   - Analyze cost monitoring integration

7. **Security and Compliance Monitoring**
   - Review audit logging implementation
   - Analyze security event detection
   - Check for compliance monitoring requirements
   - Review access and authentication logging

**Expected Output:** A comprehensive observability implementation guide including:
- Metric, logging, and tracing strategy documents
- SLI/SLO definitions with alerting thresholds
- Dashboard specifications
- Tool configuration examples
- Implementation checklist

**Example Output:**

```markdown
## Observability Implementation Guide

### Application: E-commerce Platform

#### Observability Stack
- **Metrics**: Prometheus + Grafana
- **Logging**: Loki + Promtail
- **Tracing**: Jaeger / Tempo
- **Alerting**: Alertmanager + PagerDuty

---

### Service Level Objectives (SLOs)

#### API Gateway Service

| SLI | Target | Error Budget (30 days) |
|-----|--------|------------------------|
| Availability | 99.9% | 43.2 minutes |
| Latency (p99) | < 200ms | N/A |
| Error Rate | < 0.1% | N/A |

**Prometheus Recording Rules**:
```yaml
groups:
  - name: api-gateway-slos
    rules:
      # Availability SLI
      - record: sli:api_gateway:availability
        expr: |
          sum(rate(http_requests_total{job="api-gateway",code!~"5.."}[5m]))
          /
          sum(rate(http_requests_total{job="api-gateway"}[5m]))

      # Latency SLI (% of requests under 200ms)
      - record: sli:api_gateway:latency_200ms
        expr: |
          sum(rate(http_request_duration_seconds_bucket{job="api-gateway",le="0.2"}[5m]))
          /
          sum(rate(http_request_duration_seconds_count{job="api-gateway"}[5m]))

      # Error budget remaining
      - record: sli:api_gateway:error_budget_remaining
        expr: |
          1 - (
            (1 - sli:api_gateway:availability)
            /
            (1 - 0.999)  # 99.9% target
          )
```

**Alerting Rules**:
```yaml
groups:
  - name: api-gateway-alerts
    rules:
      # Alert when burning error budget too fast
      - alert: APIGatewayErrorBudgetBurn
        expr: |
          (
            sli:api_gateway:error_budget_remaining < 0.5
            and
            predict_linear(sli:api_gateway:error_budget_remaining[6h], 3600*24) < 0
          )
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "API Gateway error budget burning fast"
          description: "Error budget at {{ $value | humanizePercentage }}, projected to exhaust within 24h"
          runbook_url: "https://runbooks.example.com/api-gateway/error-budget"

      # Critical: SLO breach imminent
      - alert: APIGatewayAvailabilityCritical
        expr: sli:api_gateway:availability < 0.995
        for: 2m
        labels:
          severity: critical
        annotations:
          summary: "API Gateway availability critical"
          description: "Availability at {{ $value | humanizePercentage }}, below 99.5%"

      # High latency alert
      - alert: APIGatewayHighLatency
        expr: |
          histogram_quantile(0.99,
            rate(http_request_duration_seconds_bucket{job="api-gateway"}[5m])
          ) > 0.2
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "API Gateway p99 latency high"
          description: "p99 latency is {{ $value | humanizeDuration }}"
```

---

### Metrics Instrumentation

#### Application Metrics (RED Method)

```python
# Python/FastAPI example with prometheus-client
from prometheus_client import Counter, Histogram, generate_latest
from functools import wraps
import time

# Request metrics
REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status_code']
)

REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'HTTP request latency',
    ['method', 'endpoint'],
    buckets=[.005, .01, .025, .05, .1, .25, .5, 1, 2.5, 5, 10]
)

REQUEST_IN_PROGRESS = Gauge(
    'http_requests_in_progress',
    'HTTP requests currently in progress',
    ['method', 'endpoint']
)

def track_requests(method: str, endpoint: str):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            REQUEST_IN_PROGRESS.labels(method=method, endpoint=endpoint).inc()
            start_time = time.time()
            try:
                response = await func(*args, **kwargs)
                status_code = response.status_code
                return response
            except Exception as e:
                status_code = 500
                raise
            finally:
                REQUEST_COUNT.labels(
                    method=method,
                    endpoint=endpoint,
                    status_code=status_code
                ).inc()
                REQUEST_LATENCY.labels(
                    method=method,
                    endpoint=endpoint
                ).observe(time.time() - start_time)
                REQUEST_IN_PROGRESS.labels(method=method, endpoint=endpoint).dec()
        return wrapper
    return decorator
```

#### Infrastructure Metrics

```yaml
# Prometheus ServiceMonitor for Kubernetes
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: api-gateway
  namespace: monitoring
spec:
  selector:
    matchLabels:
      app: api-gateway
  namespaceSelector:
    matchNames:
      - production
  endpoints:
    - port: metrics
      interval: 15s
      path: /metrics
      scheme: http
      relabelings:
        - sourceLabels: [__meta_kubernetes_pod_name]
          targetLabel: pod
        - sourceLabels: [__meta_kubernetes_namespace]
          targetLabel: namespace
```

---

### Structured Logging

#### Log Format Specification

```json
{
  "timestamp": "2024-01-15T10:30:00.123Z",
  "level": "INFO",
  "service": "api-gateway",
  "version": "1.2.3",
  "environment": "production",
  "trace_id": "abc123def456",
  "span_id": "789xyz",
  "user_id": "user-12345",
  "request_id": "req-67890",
  "message": "Request processed successfully",
  "http": {
    "method": "POST",
    "path": "/api/v1/orders",
    "status_code": 201,
    "duration_ms": 145,
    "client_ip": "10.0.0.1",
    "user_agent": "Mozilla/5.0..."
  },
  "context": {
    "order_id": "order-abc123",
    "total_amount": 99.99
  }
}
```

#### Python Logging Configuration

```python
import structlog
import logging

def configure_logging():
    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.JSONRenderer()
        ],
        wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
        context_class=dict,
        logger_factory=structlog.PrintLoggerFactory(),
    )

# Usage
logger = structlog.get_logger()

async def process_order(order_id: str, user_id: str):
    # Bind context that will appear in all subsequent logs
    log = logger.bind(order_id=order_id, user_id=user_id)

    log.info("Processing order started")

    try:
        result = await create_order(order_id)
        log.info("Order created successfully", total_amount=result.total)
        return result
    except PaymentError as e:
        log.error("Payment processing failed", error=str(e), error_type="PaymentError")
        raise
```

#### Loki Configuration

```yaml
# Promtail configuration for Kubernetes
server:
  http_listen_port: 9080
  grpc_listen_port: 0

positions:
  filename: /tmp/positions.yaml

clients:
  - url: http://loki:3100/loki/api/v1/push

scrape_configs:
  - job_name: kubernetes-pods
    kubernetes_sd_configs:
      - role: pod
    pipeline_stages:
      - cri: {}
      - json:
          expressions:
            level: level
            service: service
            trace_id: trace_id
            message: message
      - labels:
          level:
          service:
          trace_id:
      - output:
          source: message
    relabel_configs:
      - source_labels: [__meta_kubernetes_pod_label_app]
        target_label: app
      - source_labels: [__meta_kubernetes_namespace]
        target_label: namespace
      - source_labels: [__meta_kubernetes_pod_name]
        target_label: pod
```

---

### Distributed Tracing

#### OpenTelemetry Instrumentation

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor

def configure_tracing(service_name: str):
    # Set up the tracer provider
    provider = TracerProvider(
        resource=Resource.create({
            "service.name": service_name,
            "service.version": os.getenv("APP_VERSION", "unknown"),
            "deployment.environment": os.getenv("ENVIRONMENT", "development"),
        })
    )

    # Configure OTLP exporter
    otlp_exporter = OTLPSpanExporter(
        endpoint=os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", "http://tempo:4317"),
        insecure=True
    )

    provider.add_span_processor(BatchSpanProcessor(otlp_exporter))
    trace.set_tracer_provider(provider)

    # Auto-instrument frameworks
    FastAPIInstrumentor.instrument()
    HTTPXClientInstrumentor().instrument()
    SQLAlchemyInstrumentor().instrument()

# Custom span example
tracer = trace.get_tracer(__name__)

async def process_payment(order_id: str, amount: float):
    with tracer.start_as_current_span("process_payment") as span:
        span.set_attribute("order.id", order_id)
        span.set_attribute("payment.amount", amount)

        try:
            result = await payment_gateway.charge(amount)
            span.set_attribute("payment.transaction_id", result.transaction_id)
            return result
        except Exception as e:
            span.record_exception(e)
            span.set_status(Status(StatusCode.ERROR, str(e)))
            raise
```

---

### Dashboard Specifications

#### Executive Dashboard
- **Purpose**: High-level business and system health
- **Refresh**: 1 minute
- **Time Range**: Last 24 hours default

| Panel | Visualization | Query |
|-------|---------------|-------|
| Availability | Stat | `sli:api_gateway:availability` |
| Error Budget | Gauge | `sli:api_gateway:error_budget_remaining * 100` |
| Request Rate | Graph | `sum(rate(http_requests_total[5m]))` |
| Revenue Impact | Stat | Custom business metric |

#### Service Dashboard (RED Method)
```json
{
  "dashboard": {
    "title": "API Gateway - RED Metrics",
    "panels": [
      {
        "title": "Request Rate",
        "type": "graph",
        "targets": [{
          "expr": "sum(rate(http_requests_total{job=\"api-gateway\"}[5m])) by (endpoint)",
          "legendFormat": "{{endpoint}}"
        }]
      },
      {
        "title": "Error Rate",
        "type": "graph",
        "targets": [{
          "expr": "sum(rate(http_requests_total{job=\"api-gateway\",code=~\"5..\"}[5m])) / sum(rate(http_requests_total{job=\"api-gateway\"}[5m])) * 100",
          "legendFormat": "Error %"
        }]
      },
      {
        "title": "Duration (p50, p95, p99)",
        "type": "graph",
        "targets": [
          {
            "expr": "histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{job=\"api-gateway\"}[5m]))",
            "legendFormat": "p50"
          },
          {
            "expr": "histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{job=\"api-gateway\"}[5m]))",
            "legendFormat": "p95"
          },
          {
            "expr": "histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{job=\"api-gateway\"}[5m]))",
            "legendFormat": "p99"
          }
        ]
      }
    ]
  }
}
```

#### Infrastructure Dashboard (USE Method)
- **Utilization**: CPU, Memory, Disk, Network usage
- **Saturation**: Queue depths, thread pool usage
- **Errors**: Hardware errors, dropped packets

---

### Alert Routing

```yaml
# Alertmanager configuration
global:
  resolve_timeout: 5m
  slack_api_url: 'https://hooks.slack.com/services/xxx'
  pagerduty_url: 'https://events.pagerduty.com/v2/enqueue'

route:
  group_by: ['alertname', 'service']
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 4h
  receiver: 'default-receiver'
  routes:
    # Critical alerts go to PagerDuty
    - match:
        severity: critical
      receiver: 'pagerduty-critical'
      continue: true

    # Warning alerts go to Slack
    - match:
        severity: warning
      receiver: 'slack-warnings'

    # Team-specific routing
    - match:
        team: payments
      receiver: 'payments-team'

receivers:
  - name: 'default-receiver'
    slack_configs:
      - channel: '#alerts'
        send_resolved: true

  - name: 'pagerduty-critical'
    pagerduty_configs:
      - service_key: '<pagerduty-service-key>'
        severity: critical

  - name: 'slack-warnings'
    slack_configs:
      - channel: '#alerts-warnings'
        send_resolved: true
        title: '{{ .Status | toUpper }}: {{ .CommonLabels.alertname }}'
        text: '{{ range .Alerts }}{{ .Annotations.description }}{{ end }}'

  - name: 'payments-team'
    slack_configs:
      - channel: '#payments-alerts'
    email_configs:
      - to: 'payments-team@example.com'
```

---

### Implementation Checklist

| Component | Priority | Status | Owner |
|-----------|----------|--------|-------|
| Prometheus deployment | High | Done | Platform |
| Service instrumentation | High | In Progress | App Teams |
| SLO definitions | High | Pending | SRE |
| Loki deployment | Medium | Done | Platform |
| Structured logging | Medium | In Progress | App Teams |
| Tracing setup | Medium | Pending | Platform |
| Alerting rules | High | In Progress | SRE |
| Dashboards | Medium | Pending | SRE |
| Runbooks | Medium | Pending | All Teams |
```

**Techniques Used:**
- ST-01 (Clear Objective Statement)
- ST-02 (Sequential Step-by-Step Instructions)
- RT-02 (Multi-Dimensional Analysis)
- ST-03 (Structured Output Templates)
- OC-03 (Markdown Table Specification)
- DS-03 (Tool and Methodology Suggestions)
- DS-02 (Metric Specification)
- DT-01 (Hierarchical Task Breakdown)

**Related Prompts:**
- devops_kubernetes_manifest_review.md - For infrastructure monitoring setup
- devops_cicd_pipeline_analysis.md - For CI/CD observability
- code-analysis/performance/performance_analysis.md - For application performance
- devops_infrastructure_as_code_review.md - For monitoring IaC

**Customization Guide:**
- **For Serverless**: Focus on cold start metrics, invocation counts, cloud-native monitoring
- **For Event-Driven Systems**: Add queue depth monitoring, event processing latency, dead letter metrics
- **For Microservices**: Emphasize distributed tracing, service mesh observability, inter-service latency
- **For High-Traffic Systems**: Focus on sampling strategies, metric cardinality, efficient storage
