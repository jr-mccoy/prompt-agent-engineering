---
name: cqrs-implementation
description: Implement Command Query Responsibility Segregation for scalable architectures. Use when separating read and write models, optimizing query performance, or building event-sourced systems.
metadata:
  tags:
    - backend
    - cqrs
    - performance
  updated: "2026-04-11"
---
# CQRS Implementation

Comprehensive guide to implementing CQRS (Command Query Responsibility Segregation) patterns.

## When to Use This Skill

- Separating read and write concerns
- Scaling reads independently from writes
- Building event-sourced systems
- Optimizing complex query scenarios
- Different read/write data models needed
- High-performance reporting requirements

## Core Concepts

### 1. CQRS Architecture

```
                    ┌─────────────┐
                    │   Client    │
                    └──────┬──────┘
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
       ┌─────────────┐          ┌─────────────┐
       │  Commands   │          │   Queries   │
       │    API      │          │    API      │
       └──────┬──────┘          └──────┬──────┘
              │                         │
              ▼                         ▼
       ┌─────────────┐          ┌─────────────┐
       │  Command    │          │   Query     │
       │  Handlers   │          │  Handlers   │
       └──────┬──────┘          └──────┬──────┘
              │                         │
              ▼                         ▼
       ┌─────────────┐          ┌─────────────┐
       │   Write     │─────────►│    Read     │
       │   Model     │  Events  │   Model     │
       └─────────────┘          └─────────────┘
```

### 2. Key Components

| Component | Responsibility |
|-----------|---------------|
| **Command** | Intent to change state |
| **Command Handler** | Validates and executes commands |
| **Event** | Record of state change |
| **Query** | Request for data |
| **Query Handler** | Retrieves data from read model |
| **Projector** | Updates read model from events |

## Templates

### Template 1: Command Infrastructure

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TypeVar, Generic, Dict, Any, Type
from datetime import datetime
import uuid

# Command base
@dataclass
class Command:
    command_id: str = None
    timestamp: datetime = None

    def __post_init__(self):
        self.command_id = self.command_id or str(uuid.uuid4())
        self.timestamp = self.timestamp or datetime.utcnow()


# Concrete commands
@dataclass
class CreateOrder(Command):
    customer_id: str
    items: list
    shipping_address: dict


@dataclass
class AddOrderItem(Command):
    order_id: str
    product_id: str
    quantity: int
    price: float


@dataclass
class CancelOrder(Command):
    order_id: str
    reason: str


# Command handler base
T = TypeVar('T', bound=Command)

class CommandHandler(ABC, Generic[T]):
    @abstractmethod
    async def handle(self, command: T) -> Any:
        pass


# Command bus
class CommandBus:
    def __init__(self):
        self._handlers: Dict[Type[Command], CommandHandler] = {}

    def register(self, command_type: Type[Command], handler: CommandHandler):
        self._handlers[command_type] = handler

    async def dispatch(self, command: Command) -> Any:
        handler = self._handlers.get(type(command))
        if not handler:
            raise ValueError(f"No handler for {type(command).__name__}")
        return await handler.handle(command)


# Command handler implementation
class CreateOrderHandler(CommandHandler[CreateOrder]):
    def __init__(self, order_repository, event_store):
        self.order_repository = order_repository
        self.event_store = event_store

    async def handle(self, command: CreateOrder) -> str:
        # Validate
        if not command.items:
            raise ValueError("Order must have at least one item")

        # Create aggregate
        order = Order.create(
            customer_id=command.customer_id,
            items=command.items,
            shipping_address=command.shipping_address
        )

        # Persist events
        await self.event_store.append_events(
            stream_id=f"Order-{order.id}",
            stream_type="Order",
            events=order.uncommitted_events
        )

        return order.id
```

### Template 2: Query Infrastructure

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TypeVar, Generic, List, Optional

# Query base
@dataclass
class Query:
    pass


# Concrete queries
@dataclass
class GetOrderById(Query):
    order_id: str


@dataclass
class GetCustomerOrders(Query):
    customer_id: str
    status: Optional[str] = None
    page: int = 1
    page_size: int = 20


@dataclass
class SearchOrders(Query):
    query: str
    filters: dict = None
    sort_by: str = "created_at"
    sort_order: str = "desc"


# Query result types
@dataclass
class OrderView:
    order_id: str
    customer_id: str
    status: str
    total_amount: float
    item_count: int
    created_at: datetime
    shipped_at: Optional[datetime] = None


@dataclass
class PaginatedResult(Generic[T]):
    items: List[T]
    total: int
    page: int
    page_size: int

    @property
    def total_pages(self) -> int:
        return (self.total + self.page_size - 1) // self.page_size


# Query handler base
T = TypeVar('T', bound=Query)
R = TypeVar('R')

class QueryHandler(ABC, Generic[T, R]):
    @abstractmethod
    async def handle(self, query: T) -> R:
        pass


# Query bus
class QueryBus:
    def __init__(self):
        self._handlers: Dict[Type[Query], QueryHandler] = {}

    def register(self, query_type: Type[Query], handler: QueryHandler):
        self._handlers[query_type] = handler

    async def dispatch(self, query: Query) -> Any:
        handler = self._handlers.get(type(query))
        if not handler:
            raise ValueError(f"No handler for {type(query).__name__}")
        return await handler.handle(query)


# Query handler implementation
class GetOrderByIdHandler(QueryHandler[GetOrderById, Optional[OrderView]]):
    def __init__(self, read_db):
        self.read_db = read_db

    async def handle(self, query: GetOrderById) -> Optional[OrderView]:
        async with self.read_db.acquire() as conn:
            row = await conn.fetchrow(
                """
                SELECT order_id, customer_id, status, total_amount,
                       item_count, created_at, shipped_at
                FROM order_views
                WHERE order_id = $1
                """,
                query.order_id
            )
            if row:
                return OrderView(**dict(row))
            return None


class GetCustomerOrdersHandler(QueryHandler[GetCustomerOrders, PaginatedResult[OrderView]]):
    def __init__(self, read_db):
        self.read_db = read_db

    async def handle(self, query: GetCustomerOrders) -> PaginatedResult[OrderView]:
        async with self.read_db.acquire() as conn:
            # Build query with optional status filter
            where_clause = "customer_id = $1"
            params = [query.customer_id]

            if query.status:
                where_clause += " AND status = $2"
                params.append(query.status)

            # Get total count
            total = await conn.fetchval(
                f"SELECT COUNT(*) FROM order_views WHERE {where_clause}",
                *params
            )

            # Get paginated results
            offset = (query.page - 1) * query.page_size
            rows = await conn.fetch(
                f"""
                SELECT order_id, customer_id, status, total_amount,
                       item_count, created_at, shipped_at
                FROM order_views
                WHERE {where_clause}
                ORDER BY created_at DESC
                LIMIT ${len(params) + 1} OFFSET ${len(params) + 2}
                """,
                *params, query.page_size, offset
            )

            return PaginatedResult(
                items=[OrderView(**dict(row)) for row in rows],
                total=total,
                page=query.page,
                page_size=query.page_size
            )
```

### Template 3: FastAPI CQRS Application

```python
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Request/Response models
class CreateOrderRequest(BaseModel):
    customer_id: str
    items: List[dict]
    shipping_address: dict


class OrderResponse(BaseModel):
    order_id: str
    customer_id: str
    status: str
    total_amount: float
    item_count: int
    created_at: datetime


# Dependency injection
def get_command_bus() -> CommandBus:
    return app.state.command_bus


def get_query_bus() -> QueryBus:
    return app.state.query_bus


# Command endpoints (POST, PUT, DELETE)
@app.post("/orders", response_model=dict)
async def create_order(
    request: CreateOrderRequest,
    command_bus: CommandBus = Depends(get_command_bus)
):
    command = CreateOrder(
        customer_id=request.customer_id,
        items=request.items,
        shipping_address=request.shipping_address
    )
    order_id = await command_bus.dispatch(command)
    return {"order_id": order_id}


@app.post("/orders/{order_id}/items")
async def add_item(
    order_id: str,
    product_id: str,
    quantity: int,
    price: float,
    command_bus: CommandBus = Depends(get_command_bus)
):
    command = AddOrderItem(
        order_id=order_id,
        product_id=product_id,
        quantity=quantity,
        price=price
    )
    await command_bus.dispatch(command)
    return {"status": "item_added"}


@app.delete("/orders/{order_id}")
async def cancel_order(
    order_id: str,
    reason: str,
    command_bus: CommandBus = Depends(get_command_bus)
):
    command = CancelOrder(order_id=order_id, reason=reason)
    await command_bus.dispatch(command)
    return {"status": "cancelled"}


# Query endpoints (GET)
@app.get("/orders/{order_id}", response_model=OrderResponse)
async def get_order(
    order_id: str,
    query_bus: QueryBus = Depends(get_query_bus)
):
    query = GetOrderById(order_id=order_id)
    result = await query_bus.dispatch(query)
    if not result:
        raise HTTPException(status_code=404, detail="Order not found")
    return result


@app.get("/customers/{customer_id}/orders")
async def get_customer_orders(
    customer_id: str,
    status: Optional[str] = None,
    page: int = 1,
    page_size: int = 20,
    query_bus: QueryBus = Depends(get_query_bus)
):
    query = GetCustomerOrders(
        customer_id=customer_id,
        status=status,
        page=page,
        page_size=page_size
    )
    return await query_bus.dispatch(query)


@app.get("/orders/search")
async def search_orders(
    q: str,
    sort_by: str = "created_at",
    query_bus: QueryBus = Depends(get_query_bus)
):
    query = SearchOrders(query=q, sort_by=sort_by)
    return await query_bus.dispatch(query)
```

## Read Model Synchronization and Eventual Consistency

Projection-based read model synchronization with checkpoint tracking and rebuild support, and read-your-writes consistency using version polling with configurable timeout.

See [references/read-model-and-consistency.md](references/read-model-and-consistency.md)

## Best Practices

### Do's
- **Separate command and query models** - Different needs
- **Use eventual consistency** - Accept propagation delay
- **Validate in command handlers** - Before state change
- **Denormalize read models** - Optimize for queries
- **Version your events** - For schema evolution

### Don'ts
- **Don't query in commands** - Use only for writes
- **Don't couple read/write schemas** - Independent evolution
- **Don't over-engineer** - Start simple
- **Don't ignore consistency SLAs** - Define acceptable lag

## Resources

- [CQRS Pattern](https://martinfowler.com/bliki/CQRS.html)
- [Microsoft CQRS Guidance](https://docs.microsoft.com/en-us/azure/architecture/patterns/cqrs)
- **references/read-model-and-consistency.md**: Read model sync and eventual consistency handling
