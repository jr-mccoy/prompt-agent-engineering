---
title: "C#/.NET Core API Development Patterns Review"
category: software-engineering/dotnet
description: "Review .NET Core/ASP.NET Core API applications for architectural patterns, endpoint design, error handling, and framework best practices"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: intermediate
tags:
  - csharp
  - dotnet
  - aspnet-core
  - api-design
  - web-api
  - enterprise
  - best-practices
updated: "2026-03-19"
---

# C#/.NET Core API Development Patterns Review

**Objective:** Review a .NET Core / ASP.NET Core API application for adherence to framework best practices, correct use of C# language features, proper API design patterns, and production readiness.

---

## Inputs / Context

**Required:**
- .NET application source code (or specific projects/controllers to review)
- .NET version in use (.NET 6, 7, 8, or 9)
- Application type (Minimal API, Controller-based API, or hybrid)

**Optional:**
- Target deployment (Azure App Service, Kubernetes, AWS, IIS)
- Known pain points or areas of concern
- Team experience level with .NET
- Compliance requirements (HIPAA, SOC2, PCI)

**If any required input is missing:** Ask clarifying questions before proceeding.

---

## Constraints

**Must:**
- Distinguish between .NET version-specific features (e.g., Minimal APIs in .NET 6+, primary constructors in .NET 8+)
- Cite specific file paths and line numbers for every finding
- Respect intentional architectural choices — flag concerns as questions when intent is unclear

**Must Not:**
- Recommend migrating between Minimal API and Controller-based without explicit request
- Flag C# language features as wrong when they're version-appropriate (e.g., file-scoped namespaces, record types)
- Assume Entity Framework is the only data access option

---

## Steps

1. **Review project structure and configuration:**
   - Solution structure (`.sln`, project references, shared libraries)
   - `Program.cs` / `Startup.cs` service registration and middleware pipeline ordering
   - Configuration management (`appsettings.json`, environment-specific overrides, user secrets, `IOptions<T>` pattern)
   - `.csproj` settings (target framework, nullable reference types, implicit usings, `WarningsAsErrors`)

2. **Analyze API endpoint design:**
   - Route design (RESTful conventions, consistent naming, versioning strategy)
   - HTTP method usage correctness (GET for reads, POST for creates, etc.)
   - Request/response model design (DTOs vs. domain entities, `record` types for immutable DTOs)
   - Input validation (`DataAnnotations`, `FluentValidation`, model binding)
   - Content negotiation and response formatting
   - Pagination, filtering, and sorting patterns for collection endpoints

3. **Evaluate dependency injection and service lifetime:**
   - Service registration correctness (`AddTransient`, `AddScoped`, `AddSingleton`)
   - Captive dependency problems (scoped service injected into singleton)
   - Interface-based abstractions vs. concrete registrations
   - Factory patterns for complex service creation (`IServiceScopeFactory`)
   - Keyed services (`.NET 8+`)
   - Service registration organization (extension methods, modules)

4. **Review error handling and resilience:**
   - Global exception handling (`IExceptionHandler` in .NET 8+, middleware, or `UseExceptionHandler`)
   - Problem Details (RFC 9457) implementation for error responses
   - Validation error response consistency
   - HTTP client resilience (Polly / `Microsoft.Extensions.Http.Resilience`, retry policies, circuit breakers)
   - Cancellation token propagation through async call chains
   - Health checks (`IHealthCheck` implementations, readiness vs. liveness)

5. **Assess async/await and performance patterns:**
   - Correct async/await usage (no `async void` except event handlers, no `.Result`/`.Wait()` blocking)
   - `ValueTask` usage where appropriate (hot-path, frequently synchronous completion)
   - Response caching and output caching
   - `IAsyncEnumerable` for streaming large data sets
   - Object pooling (`ObjectPool<T>`) for expensive allocations
   - `Span<T>` / `Memory<T>` usage in performance-critical paths

6. **Check cross-cutting concerns:**
   - Logging (structured logging with `ILogger<T>`, log levels, sensitive data exclusion)
   - Authentication/Authorization middleware configuration
   - CORS policy configuration
   - Rate limiting (built-in .NET 7+ or third-party)
   - OpenAPI/Swagger documentation (`Swashbuckle` or `NSwag`)
   - Observability (OpenTelemetry, distributed tracing, metrics)

---

## Output Format

### Architecture Summary
2-3 sentence overview with overall assessment (Strong / Adequate / Needs Improvement) and the primary architectural pattern identified.

### Findings

For each finding:
```
File: [file path]
Line(s): [line numbers]
Category: [Structure | API Design | DI/Lifetime | Error Handling | Performance | Cross-Cutting]
Severity: [Critical | High | Medium | Low]
Issue: [Clear description]
Impact: [Effect on correctness, performance, or maintainability]
Recommendation: [Specific fix with C# code example]
```

### Dependency Injection Review
Table of registered services with lifetime assessment:

| Service | Lifetime | Dependencies | Issue |
|---------|----------|-------------|-------|
| `OrderService` | Scoped | `IDbContext` (Scoped) | Correct |
| `CacheManager` | Singleton | `IDbContext` (Scoped) | **Captive dependency** |

### API Design Consistency
Assessment of endpoint naming, HTTP methods, response formats, and versioning consistency across all controllers/endpoints.

### Prioritized Action Items
Numbered list ordered by impact with effort estimate (Small / Medium / Large).

---

## Verification

**Quick self-check:**
- [ ] All findings cite file paths and line numbers
- [ ] .NET version-specific features are correctly identified
- [ ] DI lifetime issues (captive dependencies) are checked
- [ ] Async/await correctness is verified (no blocking calls)
- [ ] Error handling produces consistent Problem Details responses
- [ ] Code examples use correct C# syntax for the target .NET version

**False-Positive Prevention:**
- Do NOT flag `AddSingleton` as wrong without checking what the service actually does — stateless services as singletons are fine
- Do NOT flag synchronous handlers as bugs when the operation is genuinely CPU-bound and brief
- Do NOT flag lack of `CancellationToken` in methods that complete in microseconds
- Do NOT flag Minimal API style as "missing controllers" — it's a valid pattern since .NET 6
- DO check that `async` methods actually contain `await` (otherwise they're synchronous with overhead)
- DO verify captive dependency issues by tracing the full registration chain

---

**Techniques Used:**
- ST-01 (Clear Objective Statement) — Focused on .NET Core API review
- ST-02 (Structured Sequential Instructions) — 6-step systematic review
- RT-02 (Multi-Dimensional Analysis Framework) — Multi-category analysis per finding
- RT-05 (Evidence-Based Reasoning) — File paths and code evidence required
- DS-06 (Prioritization Guidance) — Severity-based prioritization with effort estimates
