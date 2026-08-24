---
title: "API Rate Limiting Patterns"
category: api-design
description: "Design and implement rate limiting, throttling, and quota management for APIs"
tags:
  - api-design
  - rate-limiting
  - security
  - performance
updated: "2026-01-29"
---

# API Rate Limiting Patterns

**Objective:** Analyze existing APIs or design new rate limiting strategies that balance protection against abuse with legitimate use cases, implementing appropriate algorithms, response patterns, and client communication mechanisms.

**When to Use:** Use this prompt when designing rate limiting for new APIs, auditing existing throttling implementations, experiencing abuse or resource exhaustion, planning multi-tenant API platforms, or implementing usage-based billing.

**Instructions:**

1. **Analyze Current State**
   - Identify existing rate limiting mechanisms (if any)
   - Review current abuse patterns or resource exhaustion issues
   - Assess traffic patterns (burst vs. sustained, geographic distribution)
   - Evaluate client diversity (browsers, mobile apps, servers, integrations)
   - Document SLAs and contractual requirements
   - Identify critical vs. non-critical endpoints

2. **Select Rate Limiting Algorithm**

   Evaluate these algorithms for your use case:

   | Algorithm | Characteristics | Best For |
   |-----------|----------------|----------|
   | **Fixed Window** | Simple, reset at intervals | Basic protection, easy to implement |
   | **Sliding Window** | Smoother distribution | Fairer limits, prevents boundary abuse |
   | **Token Bucket** | Allows bursts up to bucket size | APIs needing burst tolerance |
   | **Leaky Bucket** | Constant output rate | Smooth traffic shaping |
   | **Sliding Log** | Most accurate, higher memory | High-precision requirements |

   Consider:
   - Memory and computational overhead
   - Distributed system synchronization needs
   - Burst tolerance requirements
   - Fairness requirements

3. **Design Limit Structure**

   Define limits across multiple dimensions:

   ```
   Global Limits:
   - Requests per second (RPS) across all clients
   - Concurrent connection limits

   Per-Client Limits:
   - Requests per minute/hour/day
   - Concurrent requests
   - Bandwidth limits

   Per-Endpoint Limits:
   - Write operations (stricter)
   - Read operations (more lenient)
   - Search/expensive operations (most strict)

   Per-Tenant/Plan Limits:
   - Free tier limits
   - Paid tier limits
   - Enterprise limits
   ```

4. **Implement Response Headers**

   Standard headers to include:

   ```http
   X-RateLimit-Limit: 1000          # Max requests in window
   X-RateLimit-Remaining: 847       # Remaining requests
   X-RateLimit-Reset: 1640995200    # Unix timestamp when window resets
   X-RateLimit-Policy: 1000;w=3600  # Policy description (RFC draft)
   Retry-After: 120                 # Seconds until retry (on 429)
   ```

   Evaluate RFC 7231 (Retry-After) and draft-ietf-httpapi-ratelimit-headers compliance.

5. **Design Error Responses**

   Provide actionable 429 responses:

   ```json
   {
     "error": {
       "code": "RATE_LIMIT_EXCEEDED",
       "message": "Rate limit exceeded. Please retry after 120 seconds.",
       "details": {
         "limit": 1000,
         "remaining": 0,
         "reset_at": "2024-01-15T10:30:00Z",
         "retry_after_seconds": 120,
         "limit_type": "per_minute",
         "upgrade_url": "https://api.example.com/pricing"
       }
     }
   }
   ```

6. **Implement Identification Strategy**

   Determine how to identify clients:

   | Method | Pros | Cons |
   |--------|------|------|
   | API Key | Accurate per-client | Requires key management |
   | IP Address | No setup required | Shared IPs, proxies |
   | User ID | Accurate per-user | Requires authentication |
   | JWT Claims | Flexible, per-tenant | Token parsing overhead |
   | Composite | Most accurate | Most complex |

   Consider:
   - IPv6 address aggregation (/64 or /48)
   - Proxy/load balancer forwarded headers (X-Forwarded-For)
   - NAT and shared IP scenarios
   - Authenticated vs. unauthenticated requests

7. **Handle Edge Cases**

   Plan for:
   - Clock skew in distributed systems
   - Race conditions in limit checks
   - Graceful degradation when rate limit store fails
   - Warm-up periods for new clients
   - Burst allowances for legitimate spikes
   - Webhook retry considerations
   - Mobile app background refresh patterns

8. **Design Quota Management (for usage-based billing)**

   If implementing quotas:
   - Define quota periods (daily, monthly, billing cycle)
   - Implement quota allocation and rollover policies
   - Design overage handling (hard limit vs. overage charges)
   - Create quota notification system (80%, 90%, 100%)
   - Plan for quota purchase/upgrade flow
   - Handle grace periods for paying customers

9. **Implement Monitoring and Alerting**

   Track:
   - Rate limit hit rate by client/endpoint
   - 429 response frequency and patterns
   - Limit headroom utilization
   - Abuse detection signals
   - False positive rate (legitimate users blocked)

**Expected Output:** A comprehensive rate limiting design document including:
- Selected algorithm with justification
- Complete limit structure (global, per-client, per-endpoint)
- Header and response format specifications
- Client identification strategy
- Implementation code examples
- Monitoring and alerting recommendations
- Client SDK/documentation guidance

**Example Output:**

```markdown
## Rate Limiting Design: Payment API

### Executive Summary
Implementing sliding window rate limiting with tiered limits by plan,
using composite identification (API key + IP fallback), with Redis-backed
distributed counter storage.

### Algorithm Selection: Sliding Window

**Justification:**
- Prevents boundary abuse (requesting 2x limit across window boundaries)
- Provides fairer distribution than fixed window
- Acceptable memory overhead with Redis sorted sets
- Well-understood by clients

### Limit Structure

| Tier | Per-Minute | Per-Hour | Per-Day | Concurrent |
|------|------------|----------|---------|------------|
| Free | 60 | 1,000 | 10,000 | 5 |
| Starter | 300 | 10,000 | 100,000 | 20 |
| Growth | 1,000 | 50,000 | 500,000 | 50 |
| Enterprise | Custom | Custom | Custom | Custom |

**Endpoint-Specific Limits:**

| Endpoint | Multiplier | Reasoning |
|----------|------------|-----------|
| `GET /transactions` | 1x | Standard read |
| `POST /payments` | 0.5x | Expensive write |
| `GET /reports/*` | 0.25x | Heavy computation |
| `GET /health` | Exempt | Monitoring |

### Implementation

```python
import time
from redis import Redis

class SlidingWindowRateLimiter:
    def __init__(self, redis: Redis, window_seconds: int, max_requests: int):
        self.redis = redis
        self.window = window_seconds
        self.max_requests = max_requests

    def is_allowed(self, client_id: str) -> tuple[bool, dict]:
        now = time.time()
        window_start = now - self.window
        key = f"ratelimit:{client_id}"

        pipe = self.redis.pipeline()
        pipe.zremrangebyscore(key, 0, window_start)
        pipe.zadd(key, {str(now): now})
        pipe.zcard(key)
        pipe.expire(key, self.window)
        _, _, count, _ = pipe.execute()

        remaining = max(0, self.max_requests - count)
        reset_at = int(now + self.window)

        return count <= self.max_requests, {
            "limit": self.max_requests,
            "remaining": remaining,
            "reset": reset_at,
        }
```

### Response Headers

```http
HTTP/1.1 429 Too Many Requests
Content-Type: application/json
X-RateLimit-Limit: 60
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1705312800
Retry-After: 45

{
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Rate limit exceeded for free tier",
    "retry_after": 45,
    "upgrade_url": "https://pay.example.com/upgrade"
  }
}
```

### Monitoring

- Alert when any client exceeds 80% of their limit for 3 consecutive windows
- Dashboard showing top 10 clients by limit utilization
- Weekly report of blocked legitimate requests (false positives)
- Real-time abuse detection for sudden traffic spikes
```

**False-Positive Prevention:**

- Do NOT recommend overly aggressive limits without analyzing actual traffic patterns
- Do NOT suggest rate limiting critical paths (health checks, auth endpoints) without exemption mechanisms
- Do NOT implement rate limiting without proper Retry-After headers - clients need actionable information
- Consider webhook retry scenarios - services implementing exponential backoff need adequate limits
- Account for legitimate batch operations and data sync scenarios
- Consider time-zone differences for daily quotas
- Test with realistic traffic patterns, not just synthetic loads

**Quality Indicators:**

- Headers comply with RFC 7231 and draft-ietf-httpapi-ratelimit-headers
- 429 responses include all information clients need to retry appropriately
- Limits documented in API documentation and SDK examples
- Monitoring catches both over-limiting (blocking legitimate users) and under-limiting (abuse)
- Graceful degradation when rate limit store is unavailable


---

## Must / Must Not

**Must:**
- Distinguish rate limiting by **scope**: global, per-tenant, per-user, per-IP, per-endpoint, per-key.
- Specify the **enforcement layer**: CDN / edge, API gateway, service mesh, application code — recommendations differ.
- Cite **RFC 6585 (429 Too Many Requests)** and **draft-ietf-httpapi-ratelimit-headers** for response-header format.
- Include: burst budget, steady-state limit, backoff guidance in `Retry-After`, fairness policy, degraded-mode behavior when the rate-limit store is down.

**Must Not:**
- Recommend a strategy without knowing traffic shape (peak QPS, burstiness, request cost distribution) — ask first.
- Flat-rate-limit a write API the same way as a read API.
- Default to IP-based limits for authenticated APIs (IPs behind NAT cause collateral damage).
- Emit 429 without `Retry-After` — it's client-hostile.
- Assume Redis is always available; include a graceful fallback plan.

## Verification (Self-Check)

Before recommending a strategy:

1. **Traffic shape understood** — Have I asked about burstiness, request cost variance, tenant distribution?
2. **Scope chosen per endpoint** — Write endpoints, expensive reads, and cheap reads get different limits.
3. **Headers spec'd** — `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`, `Retry-After` all included.
4. **Store-outage behavior** — What happens if the counter store is unreachable? Open (allow)? Closed (block)? Degraded (best-effort)?
5. **Confidence labeled** — High for well-known patterns; Medium for novel trade-offs.

## False-Positive Prevention

Rule out:

- **"Should use token bucket"** — Without knowing burst tolerance, sliding-window or GCRA may be better; token bucket is not universally correct.
- **"Rate limit in the app"** — Edge / gateway enforcement is usually preferable because it protects downstream.
- **"Per-IP is fine"** — Not for authenticated APIs; use authenticated-identity scope.
- **"Just return 429"** — Also emit `Retry-After`, degrade gracefully, and ensure telemetry captures the rejected requests.
