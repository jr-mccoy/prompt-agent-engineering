# INTEGRATION Skill Template

> **For external API and service connections.** Use this template when the skill connects to external APIs, services, or systems to perform operations.

---

## When to Use This Template

**Use INTEGRATION when:**
- The skill interacts with external APIs or services
- Authentication and authorization are required
- Operations involve API calls with specific patterns
- Rate limits and error handling are important

**Examples:**
- GitHub API operations
- Stripe payment integration
- Slack messaging
- AWS service integration
- Database connections
- Third-party SaaS APIs

---

## Directory Structure

```
{skill-name}/
├── SKILL.md                     # Required: integration instructions
├── scripts/                     # Integration automation
│   ├── authenticate.sh         # Authentication helpers
│   ├── api_client.py           # API wrapper
│   └── batch_operations.py     # Bulk operations
├── references/                  # API documentation
│   ├── api_reference.md        # Endpoint documentation
│   ├── authentication.md       # Auth methods and setup
│   ├── rate_limits.md          # Rate limit details
│   └── error_codes.md          # Error code reference
└── assets/                      # Configuration
    ├── config.example.yaml     # Configuration template
    ├── env.example             # Environment variables
    └── schemas/                # Request/response schemas
        ├── request.json
        └── response.json
```

---

## SKILL.md Template

Copy everything below the line and customize:

---

```yaml
---
name: {skill-name}
description: Integrates with {service/API name} for {operations}. Provides {capabilities} with proper authentication, error handling, and rate limit management. Use this skill when connecting to {service}, calling {API name}, automating {operations}, or when users mention "{service name}", "{API name}", or "integrate with {service}".
---
```

```markdown
# {Service/API} Integration

{Brief 1-2 sentence overview of what this integration provides and why it's valuable.}

## Purpose

{Explain what external service this connects to, what operations it enables, and what value it provides. 2-3 sentences maximum.}

## When to Use This Skill

Use this skill when you need to:
- {Use case 1 - specific operation with this service}
- {Use case 2 - automation involving this API}
- {Use case 3 - data sync with this service}
- {User mentions: service-name, API operations, integration keywords}

## When NOT to Use This Skill

Do NOT use this skill when:
- {Exclusion 1 - different service needed}
- {Exclusion 2 - local operation, no API needed}
- {Exclusion 3 - redirect to appropriate skill}

---

## Prerequisites

### Required Access

- [ ] **{Service} account** with {permissions}
- [ ] **API credentials:** {credential type - API key, OAuth token, etc.}
- [ ] **Required scopes/permissions:** {list of required permissions}

### Environment Setup

```bash
# Required environment variables
export {SERVICE}_API_KEY="{your-api-key}"
export {SERVICE}_BASE_URL="{api-base-url}"  # Optional, defaults to production

# Or use configuration file
cp assets/config.example.yaml ~/.config/{skill-name}/config.yaml
```

### Credential Storage

**Recommended (secure):**
```bash
# Use system keychain or secrets manager
{secrets-manager} set {SERVICE}_API_KEY
```

**Alternative (environment):**
```bash
# Add to shell profile (be cautious with this approach)
echo 'export {SERVICE}_API_KEY="..."' >> ~/.bashrc
```

**Never:**
- Commit credentials to version control
- Hardcode credentials in scripts
- Share credentials in plain text

---

## Authentication

### Auth Method: {Primary Method, e.g., API Key}

**Setup:**
```bash
# Generate API key at: {URL}
# Required permissions: {list}
```

**Usage:**
```bash
# Header authentication
curl -H "Authorization: Bearer $API_KEY" {endpoint}

# Or query parameter (if supported)
curl "{endpoint}?api_key=$API_KEY"
```

### Auth Method: {Alternative Method, e.g., OAuth 2.0}

**Setup:**
1. Register application at {URL}
2. Configure redirect URI: `{redirect-uri}`
3. Obtain client credentials

**Authorization flow:**
```bash
# Step 1: Get authorization code
{authorization-url}?client_id={CLIENT_ID}&scope={SCOPES}&redirect_uri={REDIRECT}

# Step 2: Exchange for token
curl -X POST {token-url} \
  -d "grant_type=authorization_code" \
  -d "code={AUTH_CODE}" \
  -d "client_id={CLIENT_ID}" \
  -d "client_secret={CLIENT_SECRET}"
```

**Token refresh:**
```bash
curl -X POST {token-url} \
  -d "grant_type=refresh_token" \
  -d "refresh_token={REFRESH_TOKEN}" \
  -d "client_id={CLIENT_ID}"
```

### Verify Authentication

```bash
# Test credentials
{test-auth-command}
# Expected output: {success indicator}
```

For detailed auth setup, see `references/authentication.md`.

---

## Core Operations

### Operation: {Operation Name 1}

**Purpose:** {What this operation does}

**Endpoint:** `{HTTP_METHOD} {endpoint-path}`

**Request:**
```bash
curl -X {METHOD} "{BASE_URL}/{endpoint}" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "{param1}": "{value1}",
    "{param2}": "{value2}"
  }'
```

**Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `{param1}` | string | Yes | {Description} |
| `{param2}` | integer | No | {Description} |
| `{param3}` | array | No | {Description} |

**Response:**
```json
{
  "id": "{resource-id}",
  "status": "success",
  "{field}": "{value}"
}
```

**Response codes:**
| Code | Meaning | Action |
|------|---------|--------|
| 200 | Success | Process response |
| 201 | Created | Resource created successfully |
| 400 | Bad Request | Check request parameters |
| 401 | Unauthorized | Refresh credentials |
| 429 | Rate Limited | Wait and retry |

**Example:**
```bash
# {Description of this example}
curl -X {METHOD} "{BASE_URL}/{endpoint}" \
  -H "Authorization: Bearer $API_KEY" \
  -d '{"name": "example"}'
```

---

### Operation: {Operation Name 2}

**Purpose:** {What this operation does}

**Endpoint:** `{HTTP_METHOD} {endpoint-path}`

**Request:**
```bash
{request example}
```

**Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `{param1}` | string | Yes | {Description} |

**Response:**
```json
{response example}
```

---

### Operation: {Operation Name 3}

{Continue pattern for additional operations...}

---

## Pagination

### Pattern: {Pagination Type, e.g., Cursor-based}

**Request:**
```bash
# First page
curl "{endpoint}?limit=100"

# Subsequent pages
curl "{endpoint}?limit=100&cursor={next_cursor}"
```

**Response:**
```json
{
  "data": [...],
  "pagination": {
    "next_cursor": "{cursor-value}",
    "has_more": true
  }
}
```

**Iteration pattern:**
```python
cursor = None
while True:
    response = api_call(cursor=cursor)
    process(response.data)

    if not response.pagination.has_more:
        break
    cursor = response.pagination.next_cursor
```

---

## Rate Limits

### Limits

| Endpoint | Limit | Window | Notes |
|----------|-------|--------|-------|
| {endpoint1} | {N} requests | per {time} | {notes} |
| {endpoint2} | {N} requests | per {time} | {notes} |
| Global | {N} requests | per {time} | Across all endpoints |

### Rate Limit Headers

```
X-RateLimit-Limit: {max-requests}
X-RateLimit-Remaining: {remaining}
X-RateLimit-Reset: {timestamp}
```

### Handling Rate Limits

```python
def make_request_with_retry(url, max_retries=3):
    for attempt in range(max_retries):
        response = requests.get(url, headers=headers)

        if response.status_code == 429:
            retry_after = int(response.headers.get('Retry-After', 60))
            time.sleep(retry_after)
            continue

        return response

    raise Exception("Max retries exceeded")
```

### Best Practices

1. **Implement exponential backoff** for retries
2. **Cache responses** where appropriate
3. **Batch requests** when the API supports it
4. **Monitor usage** against limits
5. **Use webhooks** instead of polling when available

For complete rate limit details, see `references/rate_limits.md`.

---

## Error Handling

### Error Response Format

```json
{
  "error": {
    "code": "{ERROR_CODE}",
    "message": "{Human-readable message}",
    "details": {
      "{field}": "{Additional info}"
    }
  }
}
```

### Common Errors

| Code | Error | Cause | Resolution |
|------|-------|-------|------------|
| `{ERR_001}` | {Error name} | {Why it happens} | {How to fix} |
| `{ERR_002}` | {Error name} | {Why it happens} | {How to fix} |
| `{ERR_003}` | {Error name} | {Why it happens} | {How to fix} |
| `{ERR_004}` | {Error name} | {Why it happens} | {How to fix} |

### Error Handling Pattern

```python
try:
    response = api.call_endpoint(params)
except AuthenticationError:
    # Refresh token and retry
    refresh_token()
    response = api.call_endpoint(params)
except RateLimitError as e:
    # Wait and retry
    time.sleep(e.retry_after)
    response = api.call_endpoint(params)
except ValidationError as e:
    # Log and handle bad input
    logger.error(f"Validation failed: {e.details}")
    raise
except APIError as e:
    # General API error
    logger.error(f"API error: {e.code} - {e.message}")
    raise
```

For complete error reference, see `references/error_codes.md`.

---

## Webhooks

### Setting Up Webhooks

**Register webhook:**
```bash
curl -X POST "{BASE_URL}/webhooks" \
  -H "Authorization: Bearer $API_KEY" \
  -d '{
    "url": "{your-webhook-url}",
    "events": ["{event1}", "{event2}"]
  }'
```

**Available events:**
| Event | Trigger | Payload |
|-------|---------|---------|
| `{event1}` | {When it fires} | {Key fields} |
| `{event2}` | {When it fires} | {Key fields} |

### Webhook Security

**Verify signature:**
```python
import hmac
import hashlib

def verify_webhook(payload, signature, secret):
    expected = hmac.new(
        secret.encode(),
        payload.encode(),
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(signature, expected)
```

### Webhook Handler Example

```python
@app.post("/webhook/{service}")
async def handle_webhook(request: Request):
    payload = await request.body()
    signature = request.headers.get("X-Signature")

    if not verify_webhook(payload, signature, WEBHOOK_SECRET):
        raise HTTPException(401, "Invalid signature")

    event = json.loads(payload)

    if event["type"] == "{event1}":
        handle_event1(event)
    elif event["type"] == "{event2}":
        handle_event2(event)

    return {"status": "ok"}
```

---

## Batch Operations

### Batch Request Pattern

```bash
# Batch multiple operations
curl -X POST "{BASE_URL}/batch" \
  -H "Authorization: Bearer $API_KEY" \
  -d '{
    "requests": [
      {"method": "GET", "path": "/{resource}/1"},
      {"method": "GET", "path": "/{resource}/2"},
      {"method": "GET", "path": "/{resource}/3"}
    ]
  }'
```

### Bulk Processing

```python
# Process in batches to respect rate limits
BATCH_SIZE = 100
DELAY_BETWEEN_BATCHES = 1  # seconds

for i in range(0, len(items), BATCH_SIZE):
    batch = items[i:i + BATCH_SIZE]
    results = process_batch(batch)
    time.sleep(DELAY_BETWEEN_BATCHES)
```

---

## Testing & Sandbox

### Sandbox Environment

```bash
# Use sandbox/test environment
export {SERVICE}_BASE_URL="https://sandbox.{service}.com/api"
export {SERVICE}_API_KEY="{test-api-key}"
```

### Test Credentials

```bash
# Test mode card (for payment APIs)
{test-credentials-example}
```

### Mocking for Tests

```python
# Mock API responses for unit tests
@responses.activate
def test_api_call():
    responses.add(
        responses.GET,
        "{BASE_URL}/{endpoint}",
        json={"status": "success"},
        status=200
    )

    result = api.call_endpoint()
    assert result["status"] == "success"
```

---

## Configuration Reference

### Configuration File

```yaml
# ~/.config/{skill-name}/config.yaml
api:
  base_url: "{base-url}"  # Optional, defaults to production
  version: "v1"           # API version

authentication:
  method: "{api_key|oauth}"
  # For API key
  api_key_env: "{SERVICE}_API_KEY"
  # For OAuth
  client_id_env: "{SERVICE}_CLIENT_ID"
  client_secret_env: "{SERVICE}_CLIENT_SECRET"

rate_limiting:
  max_retries: 3
  retry_delay: 1.0  # seconds
  exponential_backoff: true

logging:
  level: "INFO"
  include_response_bodies: false  # Security: don't log sensitive data
```

### Environment Variables

| Variable | Required | Description | Default |
|----------|----------|-------------|---------|
| `{SERVICE}_API_KEY` | Yes | API authentication key | - |
| `{SERVICE}_BASE_URL` | No | API base URL | `{production-url}` |
| `{SERVICE}_TIMEOUT` | No | Request timeout (seconds) | `30` |
| `{SERVICE}_DEBUG` | No | Enable debug logging | `false` |

---

## Reference Files

| Resource | Purpose |
|----------|---------|
| `scripts/authenticate.sh` | Authentication helpers |
| `scripts/api_client.py` | Python API wrapper |
| `scripts/batch_operations.py` | Bulk operation helpers |
| `references/api_reference.md` | Complete endpoint documentation |
| `references/authentication.md` | Auth setup and flows |
| `references/rate_limits.md` | Rate limit details |
| `references/error_codes.md` | Error code reference |
| `assets/config.example.yaml` | Configuration template |
| `assets/env.example` | Environment variable template |
| `assets/schemas/` | Request/response JSON schemas |

## Related Skills

- `{related-skill-1}` - {Related service integration}
- `{related-skill-2}` - {Skill that uses data from this service}
- `{related-skill-3}` - {Alternative service for same purpose}
```

---

## Key Patterns for INTEGRATION Skills

| Pattern | Implementation | Example |
|---------|----------------|---------|
| **IP-01: API Documentation** | Endpoint-by-endpoint docs | Core Operations section with full details |
| **IP-02: CLI Pattern Templates** | Consistent request format | Endpoint → Parameters → Response → Errors |
| **IP-03: Error Handling** | Complete error reference | Error codes table + handling pattern |
| **IP-04: Rate Limits** | Rate limit management | Limits table + retry logic |
| **IP-05: Webhook Handling** | Webhook setup and security | Webhook section with verification |
| **QP-06: Safety Constraints** | Credential security | Never commit credentials, use secrets managers |

---

## Quality Checklist

Before releasing an INTEGRATION skill:

- [ ] Authentication methods are documented with setup steps
- [ ] Credentials storage follows security best practices
- [ ] Core operations have complete request/response examples
- [ ] Rate limits are documented with handling patterns
- [ ] Error codes are mapped to causes and resolutions
- [ ] Pagination pattern is documented if applicable
- [ ] Webhooks include signature verification
- [ ] Sandbox/test environment is documented
- [ ] Configuration reference is complete

---

## Example Skills to Study

Production INTEGRATION skills in the repository:
- `github-ops` - GitHub API operations
- `stripe-integration` - Stripe payment API
- `slack-messaging` - Slack API integration
- `aws-sdk-operations` - AWS service integration

---

**Last Updated:** 2026-01-29
