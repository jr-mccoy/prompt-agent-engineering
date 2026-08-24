---
title: "Integration Test Design and Strategy"
category: testing
description: "Design comprehensive integration tests for component, service, and system interactions"
techniques:
  - ST-01
  - ST-02
  - ST-03
  - DT-01
  - RT-02
  - QA-02
difficulty: intermediate
tags:
  - testing
  - integration-tests
  - api-testing
  - microservices
  - database
updated: "2026-01-25"
---

# Integration Test Design and Strategy

**Objective:** Design comprehensive integration tests to verify that different components, services, and systems work correctly together.

**When to Use:** Use this prompt when you need to test interactions between multiple components, microservices, APIs, databases, or external systems. Ideal for backend services, API integrations, database operations, and multi-service architectures.

**Instructions:**

1. **Analyze System Architecture**
   - Identify all components, services, and external dependencies
   - Map out the data flow and communication patterns between components
   - Document API contracts, message formats, and communication protocols
   - Identify critical integration points that require testing

2. **Design Integration Test Scenarios**
   For each integration point, create test scenarios covering:
   - **Happy Path Testing**: Verify successful communication between components
   - **Error Handling**: Test how components handle failures from dependencies
   - **Data Contract Validation**: Ensure data formats match across boundaries
   - **State Management**: Verify correct state transitions across services
   - **Transaction Boundaries**: Test distributed transactions and rollback scenarios

3. **Cover Major Testing Frameworks**
   Recommend appropriate frameworks based on the technology stack:
   - **JavaScript/TypeScript**: Jest with Supertest, Vitest, or TestContainers
   - **Python**: Pytest with pytest-integration, or unittest
   - **Java**: JUnit 5 with Spring Test, TestNG, or RestAssured
   - **Ruby**: RSpec with integration testing gems
   - **Go**: Go testing package with testcontainers-go

4. **Address Integration Testing Patterns**
   - **Database Integration**: Test CRUD operations, transactions, migrations
   - **API Integration**: Test REST/GraphQL endpoints, request/response validation
   - **Message Queue Integration**: Test async messaging, event handling
   - **External Service Integration**: Test third-party API calls, mocking strategies
   - **Cache Integration**: Test cache hit/miss scenarios, invalidation

5. **Design Test Data Strategy**
   - Define test data setup and teardown procedures
   - Use database fixtures, factories, or seeding strategies
   - Implement test data isolation to prevent test interference
   - Consider using Docker/TestContainers for reproducible environments

6. **Specify Assertions and Validations**
   - Verify response status codes and data structures
   - Validate database state after operations
   - Check side effects (emails sent, events published, logs created)
   - Assert performance characteristics (response times, throughput)

7. **Document Test Environment Requirements**
   - List required services (databases, message queues, cache servers)
   - Specify configuration and environment variables
   - Document how to run tests locally and in CI/CD
   - Include Docker Compose or containerization setup if needed

8. **CRITICAL: Verify Integration Tests Are Valid**
   - Confirm tests exercise real integration points, not just mocks
   - Verify tests fail when integration contracts change
   - Check that tests don't pass due to shared state between runs
   - **Assign confidence level:** High/Medium/Low for each integration point coverage

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Write "integration tests" that only test mocked dependencies (these are unit tests)
- Assume passing tests mean real integrations work (may only test mock behavior)
- Skip cleanup between tests, causing false passes from stale data
- Use shared test databases without proper isolation (tests may interfere)
- Test against production systems or shared environments
- Ignore flaky tests caused by timing issues in async integrations
- Mock external services without validating mock accuracy against real behavior

✅ **DO:**
- Use real databases and services in containers (TestContainers pattern)
- Verify mock contracts match production API behavior periodically
- Include cleanup/teardown that resets ALL state between tests
- Test both success AND failure paths for each integration
- Validate that changing integration contracts breaks the tests
- Document which integrations are tested with real services vs mocks
- Assign confidence: High (real services), Medium (verified mocks), Low (unvalidated mocks)

**Expected Output:** A comprehensive integration test strategy document including:
- List of critical integration points requiring testing
- Detailed test scenarios for each integration point
- Recommended testing frameworks and tools for the technology stack
- Sample test code demonstrating integration testing patterns
- Test data setup/teardown procedures
- Environment setup instructions
- CI/CD integration recommendations
- **Confidence ratings** for each integration point (Real/Mocked/Verified Mock)
- **Verification notes** confirming tests catch real integration failures

**Example Output:**

```markdown
## Integration Test Strategy for E-commerce API

### Critical Integration Points
1. User Service ↔ Order Service API
2. Order Service ↔ Payment Gateway (Stripe API)
3. Order Service ↔ PostgreSQL Database
4. Notification Service ↔ RabbitMQ Message Queue
5. Product Service ↔ Redis Cache

### Test Scenario: Order Creation Flow

**Scenario**: User creates order with payment processing

**Components Involved**:
- User Service
- Order Service
- Payment Service (Stripe)
- PostgreSQL Database
- RabbitMQ

**Test Framework**: Jest + Supertest + TestContainers

**Sample Test Code**:
```javascript
describe('Order Creation Integration', () => {
  let testContainer;
  let dbConnection;

  beforeAll(async () => {
    // Setup TestContainers for PostgreSQL and RabbitMQ
    testContainer = await new PostgreSqlContainer().start();
    dbConnection = await createConnection(testContainer.getConnectionUri());
  });

  afterAll(async () => {
    await dbConnection.close();
    await testContainer.stop();
  });

  it('should create order and process payment successfully', async () => {
    // Arrange: Create test user and product
    const user = await createTestUser({ id: 'user123' });
    const product = await createTestProduct({ id: 'prod456', price: 99.99 });

    // Act: Create order via API
    const response = await request(app)
      .post('/api/orders')
      .send({
        userId: user.id,
        items: [{ productId: product.id, quantity: 2 }]
      })
      .expect(201);

    // Assert: Verify order created in database
    const order = await Order.findById(response.body.orderId);
    expect(order).toBeDefined();
    expect(order.status).toBe('pending_payment');
    expect(order.totalAmount).toBe(199.98);

    // Assert: Verify payment was initiated
    const payment = await Payment.findByOrderId(order.id);
    expect(payment.status).toBe('processing');
    expect(payment.gateway).toBe('stripe');

    // Assert: Verify notification event was published
    const notifications = await getQueueMessages('order-notifications');
    expect(notifications).toContainEqual(
      expect.objectContaining({
        type: 'order_created',
        orderId: order.id
      })
    );
  });

  it('should rollback order when payment fails', async () => {
    // Test error handling and rollback scenarios
    // ...
  });
});
```

**Environment Setup**:
```yaml
# docker-compose.test.yml
version: '3.8'
services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_DB: testdb
      POSTGRES_USER: testuser
      POSTGRES_PASSWORD: testpass
    ports:
      - "5432:5432"

  rabbitmq:
    image: rabbitmq:3-management
    ports:
      - "5672:5672"
      - "15672:15672"
```

**CI/CD Integration**:
```yaml
# .github/workflows/integration-tests.yml
name: Integration Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Start services
        run: docker-compose -f docker-compose.test.yml up -d
      - name: Run integration tests
        run: npm run test:integration
      - name: Cleanup
        run: docker-compose -f docker-compose.test.yml down
```
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Defines purpose of testing component interactions
- ST-02 (Sequential Step-by-Step Instructions) - Guides through architecture analysis to CI/CD integration
- RT-02 (Multi-Dimensional Analysis) - Covers databases, APIs, queues, caches, and external services
- ST-03 (Structured Output Templates) - Provides consistent test strategy documentation format
- OC-04 (Comprehensive Example Outputs) - Demonstrates complete integration test implementation
- TC-03 (Framework-Based Analysis) - Recommends appropriate testing frameworks per technology
- QA-02 (Adversarial Thinking) - False-positive prevention ensures tests catch real integration failures

**Related Prompts:**
- testing_unit_test_generation.md - For component-level unit tests
- testing_e2e_test_scenario_creation.md - For full user journey testing
- testing_test_coverage_gap_analysis.md - To identify untested integration points
- performance_test_scenario_generation.md - For integration performance testing
- security_api_testing.md - For security testing of API integrations

**Customization Guide:**
- **For Microservices**: Focus on service-to-service communication patterns, include contract testing with tools like Pact
- **For Monolithic Apps**: Emphasize database integration and internal component interactions
- **For Event-Driven Systems**: Add extensive message queue and event handler testing
- **For Real-Time Apps**: Include WebSocket integration testing and connection handling
- **For GraphQL APIs**: Replace REST examples with GraphQL query/mutation testing using Apollo Testing Library
