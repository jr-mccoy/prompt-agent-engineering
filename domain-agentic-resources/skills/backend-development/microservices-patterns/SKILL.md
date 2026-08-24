---
name: microservices-patterns
description: Design microservices architectures with service boundaries, event-driven communication, and resilience patterns. Use when building distributed systems, decomposing monoliths, or implementing microservices.
metadata:
  tags:
    - backend
    - microservices
  updated: "2026-04-11"
---
# Microservices Patterns

Master microservices architecture patterns including service boundaries, inter-service communication, data management, and resilience patterns for building distributed systems.

## When to Use This Skill

- Decomposing monoliths into microservices
- Designing service boundaries and contracts
- Implementing inter-service communication
- Managing distributed data and transactions
- Building resilient distributed systems
- Implementing service discovery and load balancing
- Designing event-driven architectures

## Core Concepts

### 1. Service Decomposition Strategies

**By Business Capability**
- Organize services around business functions
- Each service owns its domain
- Example: OrderService, PaymentService, InventoryService

**By Subdomain (DDD)**
- Core domain, supporting subdomains
- Bounded contexts map to services
- Clear ownership and responsibility

**Strangler Fig Pattern**
- Gradually extract from monolith
- New functionality as microservices
- Proxy routes to old/new systems

### 2. Communication Patterns

**Synchronous (Request/Response)**
- REST APIs
- gRPC
- GraphQL

**Asynchronous (Events/Messages)**
- Event streaming (Kafka)
- Message queues (RabbitMQ, SQS)
- Pub/Sub patterns

### 3. Data Management

**Database Per Service**
- Each service owns its data
- No shared databases
- Loose coupling

**Saga Pattern**
- Distributed transactions
- Compensating actions
- Eventual consistency

### 4. Resilience Patterns

**Circuit Breaker** — Fail fast on repeated errors, prevent cascade failures

**Retry with Backoff** — Transient fault handling with exponential backoff

**Bulkhead** — Isolate resources, limit impact of failures

## Service Decomposition Patterns

### Pattern 1: By Business Capability

```python
# E-commerce example

class OrderService:
    """Handles order lifecycle."""

    async def create_order(self, order_data: dict) -> Order:
        order = Order.create(order_data)

        await self.event_bus.publish(
            OrderCreatedEvent(
                order_id=order.id,
                customer_id=order.customer_id,
                items=order.items,
                total=order.total
            )
        )

        return order

class PaymentService:
    """Handles payment processing."""

    async def process_payment(self, payment_request: PaymentRequest) -> PaymentResult:
        result = await self.payment_gateway.charge(
            amount=payment_request.amount,
            customer=payment_request.customer_id
        )

        if result.success:
            await self.event_bus.publish(
                PaymentCompletedEvent(
                    order_id=payment_request.order_id,
                    transaction_id=result.transaction_id
                )
            )

        return result

class InventoryService:
    """Handles inventory management."""

    async def reserve_items(self, order_id: str, items: List[OrderItem]) -> ReservationResult:
        for item in items:
            available = await self.inventory_repo.get_available(item.product_id)
            if available < item.quantity:
                return ReservationResult(
                    success=False,
                    error=f"Insufficient inventory for {item.product_id}"
                )

        reservation = await self.create_reservation(order_id, items)

        await self.event_bus.publish(
            InventoryReservedEvent(
                order_id=order_id,
                reservation_id=reservation.id
            )
        )

        return ReservationResult(success=True, reservation=reservation)
```

### Pattern 2: API Gateway

```python
from fastapi import FastAPI, HTTPException, Depends
import httpx
from circuitbreaker import circuit

app = FastAPI()

class APIGateway:
    """Central entry point for all client requests."""

    def __init__(self):
        self.order_service_url = "http://order-service:8000"
        self.payment_service_url = "http://payment-service:8001"
        self.inventory_service_url = "http://inventory-service:8002"
        self.http_client = httpx.AsyncClient(timeout=5.0)

    @circuit(failure_threshold=5, recovery_timeout=30)
    async def call_order_service(self, path: str, method: str = "GET", **kwargs):
        response = await self.http_client.request(
            method, f"{self.order_service_url}{path}", **kwargs
        )
        response.raise_for_status()
        return response.json()

    async def create_order_aggregate(self, order_id: str) -> dict:
        """Aggregate data from multiple services."""
        order, payment, inventory = await asyncio.gather(
            self.call_order_service(f"/orders/{order_id}"),
            self.call_payment_service(f"/payments/order/{order_id}"),
            self.call_inventory_service(f"/reservations/order/{order_id}"),
            return_exceptions=True
        )

        result = {"order": order}
        if not isinstance(payment, Exception):
            result["payment"] = payment
        if not isinstance(inventory, Exception):
            result["inventory"] = inventory

        return result

@app.post("/api/orders")
async def create_order(order_data: dict, gateway: APIGateway = Depends()):
    try:
        order = await gateway.call_order_service("/orders", method="POST", json=order_data)
        return {"order": order}
    except httpx.HTTPError:
        raise HTTPException(status_code=503, detail="Order service unavailable")
```

## Communication Patterns

### Pattern 1: Synchronous REST Communication

```python
import httpx
from tenacity import retry, stop_after_attempt, wait_exponential

class ServiceClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = httpx.AsyncClient(
            timeout=httpx.Timeout(5.0, connect=2.0),
            limits=httpx.Limits(max_keepalive_connections=20)
        )

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10)
    )
    async def get(self, path: str, **kwargs):
        response = await self.client.get(f"{self.base_url}{path}", **kwargs)
        response.raise_for_status()
        return response.json()

payment_client = ServiceClient("http://payment-service:8001")
result = await payment_client.get("/payments/order/123")
```

### Pattern 2: Asynchronous Event-Driven

```python
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
import json
from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class DomainEvent:
    event_id: str
    event_type: str
    aggregate_id: str
    occurred_at: datetime
    data: dict

class EventBus:
    def __init__(self, bootstrap_servers: List[str]):
        self.bootstrap_servers = bootstrap_servers
        self.producer = None

    async def start(self):
        self.producer = AIOKafkaProducer(
            bootstrap_servers=self.bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode()
        )
        await self.producer.start()

    async def publish(self, event: DomainEvent):
        await self.producer.send_and_wait(
            event.event_type,
            value=asdict(event),
            key=event.aggregate_id.encode()
        )

    async def subscribe(self, topic: str, handler: callable):
        consumer = AIOKafkaConsumer(
            topic,
            bootstrap_servers=self.bootstrap_servers,
            value_deserializer=lambda v: json.loads(v.decode()),
            group_id="my-service"
        )
        await consumer.start()

        try:
            async for message in consumer:
                await handler(message.value)
        finally:
            await consumer.stop()
```

## Saga Pattern & Resilience Patterns

Saga orchestration for distributed transactions with compensating actions, circuit breaker implementation, retry with exponential backoff, and bulkhead pattern.

See [references/saga-and-resilience-patterns.md](references/saga-and-resilience-patterns.md)

## Resources

- **references/saga-and-resilience-patterns.md**: Saga + circuit breaker patterns
- **assets/circuit-breaker.py**: Production circuit breaker
- **assets/event-bus-template.py**: Kafka event bus implementation
- **assets/api-gateway-template.py**: Complete API gateway

## Best Practices

1. **Service Boundaries**: Align with business capabilities
2. **Database Per Service**: No shared databases
3. **API Contracts**: Versioned, backward compatible
4. **Async When Possible**: Events over direct calls
5. **Circuit Breakers**: Fail fast on service failures
6. **Distributed Tracing**: Track requests across services
7. **Service Registry**: Dynamic service discovery
8. **Health Checks**: Liveness and readiness probes

## Common Pitfalls

- **Distributed Monolith**: Tightly coupled services
- **Chatty Services**: Too many inter-service calls
- **Shared Databases**: Tight coupling through data
- **No Circuit Breakers**: Cascade failures
- **Synchronous Everything**: Poor resilience
- **Premature Microservices**: Starting with microservices before you need them
- **Ignoring Network Failures**: Assuming reliable network
- **No Compensation Logic**: Can't undo failed transactions
