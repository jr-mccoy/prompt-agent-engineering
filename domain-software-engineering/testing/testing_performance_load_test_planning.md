---
title: "Performance and Load Test Planning"
category: testing
description: "Design performance and load testing strategies to verify requirements and identify bottlenecks"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-03
  - QA-01
difficulty: intermediate
tags:
  - testing
  - performance
  - load-testing
  - scalability
  - benchmarking
updated: "2026-03-19"
---

# Performance and Load Test Planning

**Objective:** Design comprehensive performance and load testing strategies to verify that the application meets performance requirements under various load conditions and identify performance bottlenecks.

**When to Use:** Use this prompt when you need to validate application performance, scalability, and reliability under different load scenarios. Essential before production launches, major releases, or when performance issues are suspected. Ideal for APIs, web applications, databases, and distributed systems.

**Instructions:**

1. **Define Performance Requirements and SLAs**
   - Identify key performance metrics (response time, throughput, latency, error rate)
   - Establish performance baselines and targets
   - Define Service Level Agreements (SLAs) and Service Level Objectives (SLOs)
   - Example targets: 95th percentile response time < 500ms, throughput > 1000 req/s, error rate < 0.1%

2. **Identify Critical Performance Scenarios**
   - List the most performance-critical operations and endpoints
   - Prioritize based on user frequency and business impact
   - Consider: API endpoints, database queries, file uploads, report generation, search operations
   - Map expected user load patterns (daily/weekly peaks, seasonal variations)

3. **Design Load Test Scenarios**
   Create tests for different load patterns:
   - **Baseline Test**: Minimal load to establish performance baseline
   - **Load Test**: Expected normal and peak load conditions
   - **Stress Test**: Push system beyond normal capacity to find breaking points
   - **Spike Test**: Sudden large increases in load
   - **Soak Test**: Sustained load over extended period to detect memory leaks and degradation
   - **Scalability Test**: Verify horizontal and vertical scaling capabilities

4. **Select Performance Testing Tools**
   Recommend appropriate tools based on requirements:
   - **k6**: Modern, developer-friendly, JavaScript-based (excellent for APIs)
   - **JMeter**: Enterprise-grade, GUI-based, extensive protocol support
   - **Gatling**: Scala-based, great reporting, ideal for continuous testing
   - **Locust**: Python-based, distributed load generation, flexible scripting
   - **Artillery**: Node.js-based, simple YAML config, good for CI/CD
   - **wrk/wrk2**: Lightweight HTTP benchmarking for simple scenarios

5. **Define Virtual User Profiles and Load Models**
   - Create realistic user behavior models (think time, session duration)
   - Define ramp-up and ramp-down strategies
   - Specify concurrent users, requests per second, and duration
   - Include user pacing and randomization for realistic simulation

6. **Plan Test Data Strategy**
   - Identify data requirements for load tests (size, variety, distribution)
   - Use production-like data volumes
   - Handle data parameterization and correlation
   - Plan for data cleanup and reset between test runs

7. **Design Monitoring and Metrics Collection**
   - Define what to measure: response times, throughput, error rates, resource utilization
   - Set up application performance monitoring (APM)
   - Monitor infrastructure metrics: CPU, memory, disk I/O, network
   - Plan for distributed tracing in microservices architectures

8. **Establish Success Criteria and Failure Thresholds**
   - Define pass/fail criteria for each test scenario
   - Set performance budgets and thresholds
   - Specify acceptable degradation under load
   - Plan for automated alerting on threshold violations

9. **Plan CI/CD Integration**
   - Design performance testing in CI/CD pipeline
   - Configure automated performance regression detection
   - Set up performance trend tracking over time
   - Define when to block deployments based on performance

10. **CRITICAL: Validate Performance Results Before Reporting**
    - Verify test environment is representative of production
    - Confirm test data volume and distribution matches production
    - Check for external factors affecting results (shared infrastructure, network variability)
    - **Confidence level** for each finding:
      - **High Confidence:** Reproduced across multiple test runs, production-like environment
      - **Medium Confidence:** Single test run, or non-production environment, may need validation
      - **Low Confidence:** Test environment significantly different from production

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Report performance issues from tests run on undersized/overloaded test infrastructure
- Compare results across different test environments without normalization
- Ignore warm-up effects (first requests always slower due to JIT, caches, connection pools)
- Report bottlenecks without verifying they occur under realistic load patterns
- Assume test data characteristics match production (smaller data = faster queries)
- Attribute performance issues to code when infrastructure is the limiting factor
- Report "degradation" based on noisy metrics without statistical significance

✅ **DO:**
- Run warm-up iterations before measuring (exclude from results)
- Verify test infrastructure matches production capacity (or normalize accordingly)
- Use production-representative data volumes and query patterns
- Run multiple test iterations and report statistical aggregates (p95, p99)
- Identify whether bottleneck is CPU, memory, I/O, network, or external dependency
- Compare results against established baselines, not arbitrary expectations
- Account for time-of-day effects if testing against shared services
- Validate findings with profiling tools before recommending expensive fixes

**Expected Output:** A comprehensive performance testing plan including:
- Performance requirements and SLAs
- 5-7 load test scenarios with detailed specifications
- Recommended performance testing tool with configuration
- Sample test scripts demonstrating load patterns
- Virtual user profiles and load models
- Monitoring and metrics collection strategy
- Success criteria and performance budgets
- CI/CD integration approach
- Performance test execution schedule

**Example Output:**

```markdown
## Performance Test Plan for E-commerce API

### Performance Requirements

| Metric | Target | Critical Threshold |
|--------|--------|-------------------|
| API Response Time (p95) | < 300ms | < 500ms |
| API Response Time (p99) | < 500ms | < 1000ms |
| Throughput | > 5000 req/s | > 3000 req/s |
| Error Rate | < 0.1% | < 1% |
| Database Query Time | < 50ms | < 100ms |
| Concurrent Users | 10,000 | 5,000 minimum |

### Critical Endpoints to Test

1. **GET /api/products** (High frequency, 40% of traffic)
2. **GET /api/products/:id** (High frequency, 25% of traffic)
3. **POST /api/orders** (Business critical, 15% of traffic)
4. **POST /api/payments** (Business critical, 10% of traffic)
5. **GET /api/search** (Resource intensive, 10% of traffic)

---

### Results Confidence Assessment

| Test Scenario | Confidence | Environment Match | Data Representativeness |
|---------------|------------|-------------------|-------------------------|
| Normal Peak Load | High | Staging = 80% of prod capacity | Production data snapshot |
| Stress Test | High | Same as above | Same as above |
| Spike Test | Medium | May not have prod-level auto-scaling | Simulated traffic pattern |
| Soak Test | High | Dedicated test window | Full data volume |

**Environment Validation:**
- ✅ Database size matches production (4.2TB vs 4.5TB)
- ✅ Cache configuration identical to production
- ⚠️ Auto-scaling configured but limits lower than production
- ✅ Network latency simulated for geographically distributed users

---

### Load Test Scenario 1: Normal Peak Load

**Objective**: Verify system performs under expected peak traffic
**Confidence**: High - Environment validated, results consistent across 3 runs

**Load Pattern**:
- Ramp-up: 0 to 5000 virtual users over 5 minutes
- Sustain: 5000 virtual users for 30 minutes
- Ramp-down: 5000 to 0 over 2 minutes

**Virtual User Distribution**:
- 40% browsing products (GET /api/products, GET /api/products/:id)
- 30% searching (GET /api/search?q=...)
- 20% viewing cart (GET /api/cart)
- 10% checking out (POST /api/orders, POST /api/payments)

**Success Criteria**:
- P95 response time < 300ms for all endpoints
- Error rate < 0.1%
- No memory leaks or resource exhaustion
- Database connection pool stable

**Tool**: k6

**Sample Test Script**:

```javascript
// k6-normal-peak-load.js
import http from 'k6/http';
import { check, sleep } from 'k6';
import { Rate, Trend } from 'k6/metrics';

// Custom metrics
const errorRate = new Rate('errors');
const productListDuration = new Trend('product_list_duration');
const checkoutDuration = new Trend('checkout_duration');

// Test configuration
export const options = {
  stages: [
    { duration: '5m', target: 5000 },  // Ramp-up to 5000 users
    { duration: '30m', target: 5000 }, // Stay at 5000 users
    { duration: '2m', target: 0 },     // Ramp-down to 0
  ],
  thresholds: {
    'http_req_duration': ['p(95)<300', 'p(99)<500'],
    'http_req_failed': ['rate<0.001'], // Less than 0.1% errors
    'errors': ['rate<0.001'],
  },
};

const BASE_URL = __ENV.BASE_URL || 'https://api.example.com';

// User behavior scenarios
const scenarios = [
  { name: 'browse_products', weight: 40, fn: browseProducts },
  { name: 'search_products', weight: 30, fn: searchProducts },
  { name: 'view_cart', weight: 20, fn: viewCart },
  { name: 'checkout', weight: 10, fn: checkout },
];

export default function() {
  // Randomly select scenario based on weight
  const totalWeight = scenarios.reduce((sum, s) => sum + s.weight, 0);
  let random = Math.random() * totalWeight;

  for (const scenario of scenarios) {
    random -= scenario.weight;
    if (random <= 0) {
      scenario.fn();
      break;
    }
  }

  // Think time: simulate user reading/interaction time
  sleep(Math.random() * 3 + 2); // 2-5 seconds
}

function browseProducts() {
  // Get product list
  const listRes = http.get(`${BASE_URL}/api/products?page=1&limit=20`);

  const success = check(listRes, {
    'product list status 200': (r) => r.status === 200,
    'product list has data': (r) => r.json('data').length > 0,
  });

  errorRate.add(!success);
  productListDuration.add(listRes.timings.duration);

  if (success) {
    // View random product detail
    const products = listRes.json('data');
    const productId = products[Math.floor(Math.random() * products.length)].id;

    sleep(1); // Think time

    const detailRes = http.get(`${BASE_URL}/api/products/${productId}`);
    check(detailRes, {
      'product detail status 200': (r) => r.status === 200,
    });
  }
}

function searchProducts() {
  const searchTerms = ['laptop', 'phone', 'headphones', 'camera', 'watch'];
  const term = searchTerms[Math.floor(Math.random() * searchTerms.length)];

  const searchRes = http.get(`${BASE_URL}/api/search?q=${term}&page=1`);

  check(searchRes, {
    'search status 200': (r) => r.status === 200,
    'search response time < 500ms': (r) => r.timings.duration < 500,
  });
}

function viewCart() {
  const headers = {
    'Authorization': `Bearer ${__ENV.AUTH_TOKEN}`,
  };

  const cartRes = http.get(`${BASE_URL}/api/cart`, { headers });

  check(cartRes, {
    'cart status 200 or 401': (r) => [200, 401].includes(r.status),
  });
}

function checkout() {
  const headers = {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${__ENV.AUTH_TOKEN}`,
  };

  // Create order
  const orderPayload = {
    items: [
      { productId: 'TEST-001', quantity: 1 },
      { productId: 'TEST-002', quantity: 2 },
    ],
    shippingAddress: {
      street: '123 Test St',
      city: 'Test City',
      state: 'CA',
      zip: '90210',
    },
  };

  const orderRes = http.post(
    `${BASE_URL}/api/orders`,
    JSON.stringify(orderPayload),
    { headers }
  );

  const orderSuccess = check(orderRes, {
    'order creation status 201': (r) => r.status === 201,
    'order has id': (r) => r.json('orderId') !== undefined,
  });

  checkoutDuration.add(orderRes.timings.duration);

  if (orderSuccess) {
    const orderId = orderRes.json('orderId');

    sleep(1); // Think time

    // Process payment
    const paymentPayload = {
      orderId: orderId,
      paymentMethod: 'credit_card',
      cardToken: 'tok_test_4242424242424242',
    };

    const paymentRes = http.post(
      `${BASE_URL}/api/payments`,
      JSON.stringify(paymentPayload),
      { headers }
    );

    check(paymentRes, {
      'payment status 200': (r) => r.status === 200,
      'payment successful': (r) => r.json('status') === 'success',
    });
  }
}

// Handle test lifecycle
export function setup() {
  console.log('Starting performance test...');
  // Could initialize test data here
}

export function teardown(data) {
  console.log('Performance test completed');
  // Could cleanup test data here
}
```

---

### Load Test Scenario 2: Stress Test - Find Breaking Point

**Objective**: Determine maximum system capacity and failure modes
**Confidence**: High - Results verified against production metrics during actual traffic spike

**Load Pattern**:
- Ramp-up: 0 to 15,000 virtual users over 10 minutes
- Continue increasing until system breaks or reaches 20,000 users

**Success Criteria**:
- Identify exact breaking point (user count where errors exceed 5%)
- System degrades gracefully without crashes
- System recovers after load reduction
- Document failure symptoms

---

### Load Test Scenario 3: Spike Test - Black Friday Simulation

**Objective**: Verify system handles sudden traffic spikes
**Confidence**: Medium - Auto-scaling behavior may differ in production (higher limits)

**Load Pattern**:
- Normal: 2000 users
- Spike: Jump to 15,000 users instantly
- Sustain spike: 5 minutes
- Return to normal: 2000 users

**Success Criteria**:
- System handles spike without downtime
- Response times recover within 2 minutes
- No data corruption or lost requests

---

### Load Test Scenario 4: Soak Test - 24-Hour Stability

**Objective**: Detect memory leaks and performance degradation over time
**Confidence**: High - Full 24-hour run on production-equivalent infrastructure

**Load Pattern**:
- Constant: 3000 users for 24 hours

**Success Criteria**:
- Memory usage remains stable (no continuous growth)
- Response times don't degrade over time
- No resource exhaustion (connections, file handles)
- Error rate remains below 0.1% throughout

---

### Monitoring Setup

**Application Metrics** (via New Relic/Datadog):
- Request rate and response time distributions
- Error rates by endpoint
- Apdex score
- Transaction traces for slow requests

**Infrastructure Metrics** (via Prometheus/CloudWatch):
- CPU utilization across all instances
- Memory usage and garbage collection
- Network I/O and bandwidth
- Disk I/O and storage capacity

**Database Metrics**:
- Query execution times
- Connection pool usage
- Lock contention and deadlocks
- Cache hit ratios

**Sample Monitoring Dashboard**:
```
┌─────────────────────────────────────────────────────┐
│ Performance Test Dashboard                          │
├─────────────────────────────────────────────────────┤
│ Active VUs: 5000        RPS: 4850                   │
│ Avg Response: 245ms     P95: 385ms   P99: 520ms     │
│ Error Rate: 0.08%       Success Rate: 99.92%        │
├─────────────────────────────────────────────────────┤
│ CPU Usage: 65%          Memory: 8.2GB / 16GB        │
│ DB Connections: 142/200 Cache Hit Rate: 87%         │
└─────────────────────────────────────────────────────┘
```

---

### CI/CD Integration

**GitHub Actions Workflow**:

```yaml
name: Performance Tests
on:
  schedule:
    - cron: '0 2 * * *'  # Run nightly at 2 AM
  workflow_dispatch:     # Allow manual trigger

jobs:
  performance-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Run k6 Load Test
        uses: grafana/k6-action@v0.3.0
        with:
          filename: tests/performance/k6-normal-peak-load.js
        env:
          BASE_URL: ${{ secrets.STAGING_URL }}
          AUTH_TOKEN: ${{ secrets.TEST_AUTH_TOKEN }}

      - name: Check Performance Thresholds
        run: |
          # k6 will exit with non-zero if thresholds failed
          echo "Performance test completed"

      - name: Upload Results
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: k6-results
          path: summary.json

      - name: Comment PR with Results
        if: github.event_name == 'pull_request'
        uses: actions/github-script@v6
        with:
          script: |
            // Parse k6 results and post summary comment
            // Include comparison to baseline
```

---

### Performance Budget

| Endpoint | Max P95 Response Time | Max P99 Response Time | Min Throughput |
|----------|----------------------|-----------------------|----------------|
| GET /api/products | 200ms | 400ms | 2000 req/s |
| GET /api/products/:id | 150ms | 300ms | 3000 req/s |
| POST /api/orders | 500ms | 1000ms | 500 req/s |
| POST /api/payments | 800ms | 1500ms | 400 req/s |
| GET /api/search | 400ms | 800ms | 1000 req/s |

**Automated Enforcement**: Tests fail if any endpoint exceeds performance budget

```

**Techniques Used:**
- ST-01 (Clear Objective Statement)
- ST-02 (Sequential Step-by-Step Instructions)
- ST-07 (Prioritization and Ranking)
- RT-01 (Requirement Analysis)
- RT-02 (Multi-Dimensional Analysis)
- ST-03 (Structured Output Templates)
- OC-04 (Comprehensive Example Outputs)
- TC-02 (Metrics and Quantification)

**Related Prompts:**
- performance_bottleneck_identification.md - For analyzing performance issues
- performance_scalability_analysis.md - For evaluating scaling capabilities
- testing_integration_test_design.md - For testing component performance
- code-analysis/database/database_query_optimization.md - For optimizing slow queries
- code-analysis/performance/performance_memory_leak_detection.md - For memory analysis

**Customization Guide:**
- **For APIs**: Focus on endpoint response times, throughput, and rate limiting behavior
- **For Web Applications**: Include browser-based metrics (First Contentful Paint, Time to Interactive, Core Web Vitals)
- **For Microservices**: Add service mesh metrics, inter-service latency, and circuit breaker testing
- **For Databases**: Include connection pool testing, query performance under load, and replication lag
- **For Real-Time Systems**: Test WebSocket connections, message throughput, and concurrent connection limits
- **For Batch Processing**: Measure job completion times, resource utilization, and throughput (records/second)
