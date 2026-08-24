# OpenTelemetry Semantic Conventions

Semantic conventions define standard attribute names for consistent telemetry data across services.

## Resource Attributes

Identify the service producing telemetry:

```typescript
import {
  SEMRESATTRS_SERVICE_NAME,
  SEMRESATTRS_SERVICE_VERSION,
  SEMRESATTRS_SERVICE_NAMESPACE,
  SEMRESATTRS_DEPLOYMENT_ENVIRONMENT,
  SEMRESATTRS_HOST_NAME,
  SEMRESATTRS_CONTAINER_ID,
  SEMRESATTRS_K8S_POD_NAME,
  SEMRESATTRS_K8S_NAMESPACE_NAME,
} from '@opentelemetry/semantic-conventions';

const resource = new Resource({
  [SEMRESATTRS_SERVICE_NAME]: 'user-service',
  [SEMRESATTRS_SERVICE_VERSION]: '2.1.0',
  [SEMRESATTRS_SERVICE_NAMESPACE]: 'ecommerce',
  [SEMRESATTRS_DEPLOYMENT_ENVIRONMENT]: 'production',
});
```

## HTTP Attributes

For HTTP client and server spans:

```typescript
import {
  SEMATTRS_HTTP_METHOD,
  SEMATTRS_HTTP_URL,
  SEMATTRS_HTTP_TARGET,
  SEMATTRS_HTTP_HOST,
  SEMATTRS_HTTP_SCHEME,
  SEMATTRS_HTTP_STATUS_CODE,
  SEMATTRS_HTTP_REQUEST_CONTENT_LENGTH,
  SEMATTRS_HTTP_RESPONSE_CONTENT_LENGTH,
  SEMATTRS_HTTP_USER_AGENT,
  SEMATTRS_HTTP_ROUTE,
} from '@opentelemetry/semantic-conventions';

span.setAttributes({
  [SEMATTRS_HTTP_METHOD]: 'GET',
  [SEMATTRS_HTTP_URL]: 'https://api.example.com/users/123',
  [SEMATTRS_HTTP_ROUTE]: '/users/:id',
  [SEMATTRS_HTTP_STATUS_CODE]: 200,
  [SEMATTRS_HTTP_USER_AGENT]: 'Mozilla/5.0...',
});
```

## Database Attributes

For database operations:

```typescript
import {
  SEMATTRS_DB_SYSTEM,
  SEMATTRS_DB_NAME,
  SEMATTRS_DB_STATEMENT,
  SEMATTRS_DB_OPERATION,
  SEMATTRS_DB_USER,
  SEMATTRS_DB_CONNECTION_STRING,
} from '@opentelemetry/semantic-conventions';

span.setAttributes({
  [SEMATTRS_DB_SYSTEM]: 'postgresql',
  [SEMATTRS_DB_NAME]: 'users_db',
  [SEMATTRS_DB_OPERATION]: 'SELECT',
  [SEMATTRS_DB_STATEMENT]: 'SELECT * FROM users WHERE id = $1',
});
```

## Messaging Attributes

For message queue operations:

```typescript
import {
  SEMATTRS_MESSAGING_SYSTEM,
  SEMATTRS_MESSAGING_DESTINATION,
  SEMATTRS_MESSAGING_DESTINATION_KIND,
  SEMATTRS_MESSAGING_MESSAGE_ID,
  SEMATTRS_MESSAGING_OPERATION,
} from '@opentelemetry/semantic-conventions';

span.setAttributes({
  [SEMATTRS_MESSAGING_SYSTEM]: 'kafka',
  [SEMATTRS_MESSAGING_DESTINATION]: 'orders-topic',
  [SEMATTRS_MESSAGING_DESTINATION_KIND]: 'topic',
  [SEMATTRS_MESSAGING_OPERATION]: 'publish',
  [SEMATTRS_MESSAGING_MESSAGE_ID]: message.id,
});
```

## RPC Attributes

For RPC calls (gRPC, etc.):

```typescript
import {
  SEMATTRS_RPC_SYSTEM,
  SEMATTRS_RPC_SERVICE,
  SEMATTRS_RPC_METHOD,
  SEMATTRS_RPC_GRPC_STATUS_CODE,
} from '@opentelemetry/semantic-conventions';

span.setAttributes({
  [SEMATTRS_RPC_SYSTEM]: 'grpc',
  [SEMATTRS_RPC_SERVICE]: 'UserService',
  [SEMATTRS_RPC_METHOD]: 'GetUser',
  [SEMATTRS_RPC_GRPC_STATUS_CODE]: 0,
});
```

## Exception Attributes

For error recording:

```typescript
import {
  SEMATTRS_EXCEPTION_TYPE,
  SEMATTRS_EXCEPTION_MESSAGE,
  SEMATTRS_EXCEPTION_STACKTRACE,
} from '@opentelemetry/semantic-conventions';

span.recordException(error);
// Automatically sets:
// - exception.type
// - exception.message
// - exception.stacktrace
```

## Custom Attributes

Follow conventions for custom attributes:

```typescript
// Use dot notation for namespacing
span.setAttributes({
  'user.id': userId,
  'user.role': userRole,
  'order.id': orderId,
  'order.total': orderTotal,
  'feature.flag': featureFlagName,
});
```

## Attribute Value Types

| Type | Example | Notes |
|------|---------|-------|
| String | `'value'` | Most common |
| Number | `123`, `3.14` | Integers or floats |
| Boolean | `true`, `false` | |
| String[] | `['a', 'b']` | Homogeneous arrays |

## Span Naming Conventions

| Type | Pattern | Example |
|------|---------|---------|
| HTTP Server | `HTTP {method}` | `HTTP GET` |
| HTTP Client | `HTTP {method}` | `HTTP POST` |
| Database | `{db.operation} {db.name}` | `SELECT users_db` |
| Messaging | `{destination} {operation}` | `orders-topic publish` |
| RPC | `{service}/{method}` | `UserService/GetUser` |
| Internal | `{operation-name}` | `process-order` |
