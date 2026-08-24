---
title: "ASP.NET Core Middleware and Dependency Injection Review"
category: software-engineering/dotnet
description: "Review ASP.NET Core middleware pipeline ordering, custom middleware implementation, and dependency injection configuration for correctness and performance"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: advanced
tags:
  - csharp
  - dotnet
  - aspnet-core
  - middleware
  - dependency-injection
  - pipeline
  - enterprise
updated: "2026-03-19"
---

# ASP.NET Core Middleware and Dependency Injection Review

**Objective:** Review an ASP.NET Core application's middleware pipeline configuration and dependency injection setup to identify ordering errors, lifetime mismatches, performance issues, and correctness problems that can cause subtle runtime failures.

---

## Inputs / Context

**Required:**
- `Program.cs` (or `Startup.cs` for older projects) with full middleware and DI configuration
- .NET version in use (.NET 6, 7, 8, or 9)

**Optional:**
- Custom middleware classes
- Service registration extension methods
- Known issues (request processing errors, DI resolution failures, memory leaks)
- Production traffic characteristics (request volume, concurrency)

**If any required input is missing:** Ask clarifying questions before proceeding.

---

## Constraints

**Must:**
- Evaluate middleware ordering against ASP.NET Core's documented recommended order
- Verify DI lifetime correctness through the entire dependency graph
- Provide the corrected middleware order when issues are found

**Must Not:**
- Rewrite the entire pipeline when only specific ordering issues exist
- Flag framework-registered services (e.g., `ILogger<T>`, `IConfiguration`) as missing registrations
- Assume all custom middleware needs to be refactored into filters or endpoints

---

## Steps

1. **Analyze middleware pipeline ordering:**
   Compare the configured middleware order against the ASP.NET Core recommended order:
   ```
   1. UseExceptionHandler / UseDeveloperExceptionPage
   2. UseHsts
   3. UseHttpsRedirection
   4. UseStaticFiles
   5. UseRouting
   6. UseCors
   7. UseAuthentication
   8. UseAuthorization
   9. UseRateLimiter
   10. UseResponseCaching / UseOutputCache
   11. Custom middleware
   12. MapControllers / MapEndpoints
   ```
   For each deviation, determine whether it is:
   - **A bug:** Ordering causes incorrect behavior (e.g., `UseAuthorization` before `UseAuthentication`)
   - **Intentional:** Documented reason for non-standard order
   - **Unnecessary:** Middleware included but not needed

2. **Review custom middleware implementations:**
   For each custom middleware, evaluate:
   a. **Constructor vs. Invoke injection:** Constructor-injected services must be singleton; scoped services must be injected via `InvokeAsync` parameters
   b. **Request delegate invocation:** `await _next(context)` must always be called unless intentionally short-circuiting
   c. **Exception safety:** Middleware must not swallow exceptions silently
   d. **Response body access:** Check for reading/writing response body after `_next` has already started writing (causes `InvalidOperationException`)
   e. **Thread safety:** Middleware is instantiated once (singleton), so mutable instance state is a concurrency bug
   f. **Performance:** Avoid allocations in hot-path middleware, use `IMiddleware` for scoped middleware

3. **Audit dependency injection configuration:**
   - **Registration completeness:** All injected interfaces have corresponding registrations
   - **Lifetime correctness:**
     - Singleton services must not depend on Scoped or Transient services (captive dependency)
     - Scoped services must not be resolved from root `IServiceProvider`
     - `IServiceScopeFactory` usage for creating scopes in singletons/background services
   - **Registration patterns:**
     - Duplicate registrations (last-wins behavior — is this intentional?)
     - Missing `TryAdd*` where multiple registrations should be prevented
     - Decorator pattern implementation (`Scrutor` or manual decoration)
     - Open generic registrations (`AddScoped(typeof(IRepository<>), typeof(Repository<>))`)

4. **Check hosted services and background work:**
   - `IHostedService` / `BackgroundService` implementations
   - Scoped service access in background services (must create scope via `IServiceScopeFactory`)
   - Cancellation token handling in `ExecuteAsync` / `StopAsync`
   - Error handling in background services (unhandled exceptions can crash the host)
   - `IHostApplicationLifetime` usage for graceful shutdown coordination

5. **Evaluate options pattern usage:**
   - `IOptions<T>` vs. `IOptionsSnapshot<T>` vs. `IOptionsMonitor<T>` lifetime alignment
   - Options validation (`ValidateDataAnnotations`, `ValidateOnStart`)
   - Configuration binding correctness (`Configure<T>`, `Bind`, `Get<T>`)
   - Named options usage where appropriate

6. **Assess pipeline performance characteristics:**
   - Middleware that performs I/O on every request (should it be conditional?)
   - Response compression configuration
   - Request body buffering (multiple reads require `EnableBuffering()`)
   - Header propagation and correlation ID middleware

---

## Output Format

### Pipeline Assessment
Overall pipeline health (Correct / Has Ordering Issues / Significant Problems) with the most impactful finding highlighted.

### Middleware Order Analysis

**Current order:**
```
1. UseExceptionHandler     ✅
2. UseHttpsRedirection     ✅
3. UseAuthorization        ❌ (before UseAuthentication)
4. UseAuthentication       ❌ (must come before UseAuthorization)
5. UseRouting              ❌ (should come before auth middleware)
```

**Recommended order:**
```
1. UseExceptionHandler
2. UseHttpsRedirection
3. UseRouting
4. UseAuthentication
5. UseAuthorization
```

### Custom Middleware Findings

For each finding:
```
File: [file path]
Line(s): [line numbers]
Middleware: [class name]
Severity: [Critical | High | Medium | Low]
Issue: [Description of the problem]
Impact: [Runtime behavior consequence]
Fix: [Specific code change]
```

### Dependency Injection Findings

**Lifetime Dependency Graph:**
```
[Singleton] CacheService
  └─ [Scoped] DbContext  ⚠️ CAPTIVE DEPENDENCY

[Scoped] OrderService
  └─ [Scoped] DbContext  ✅ Correct
  └─ [Singleton] CacheService  ✅ Correct
```

For each issue:
```
Service: [type name]
Registered Lifetime: [Singleton | Scoped | Transient]
Issue: [Captive dependency | Missing registration | Duplicate registration | ...]
Impact: [Memory leak | Stale data | Resolution failure | ...]
Fix: [Specific registration change]
```

### Options Pattern Review
Assessment of `IOptions<T>` usage correctness and validation configuration.

### Prioritized Fixes
Numbered action items ordered by severity, with exact code changes.

---

## Verification

**Quick self-check:**
- [ ] Middleware ordering is compared against the documented recommended order
- [ ] All custom middleware handles the `_next` delegate correctly
- [ ] Captive dependency analysis traces the full dependency graph
- [ ] Background service scope creation is verified
- [ ] Options pattern lifetime alignment is checked

**High-stakes verification:**
After completing the review, explicitly answer:
1. Can any middleware silently swallow exceptions, hiding failures?
2. Are there any captive dependencies that would cause stale data in production?
3. Can any background service crash the host due to unhandled exceptions?

**False-Positive Prevention:**
- Do NOT flag middleware order deviations that are intentional (e.g., custom logging before exception handler for specific diagnostics)
- Do NOT flag `IOptions<T>` in a scoped service as wrong — it reads config once at resolution, which is often acceptable
- Do NOT flag constructor injection in middleware as wrong for services that ARE singletons
- Do NOT flag `AddTransient` as wasteful without profiling — the allocation cost is often negligible
- DO verify that duplicate service registrations use last-wins behavior intentionally
- DO check that `IMiddleware` implementations are registered as scoped (the framework requires it)

---

**Techniques Used:**
- ST-01 (Clear Objective Statement) — Focused on middleware and DI correctness
- ST-02 (Structured Sequential Instructions) — 6-step review process
- RT-02 (Multi-Dimensional Analysis Framework) — Middleware, DI, background services, options analyzed separately
- RT-05 (Evidence-Based Reasoning) — Dependency graphs and code evidence required
- DS-06 (Prioritization Guidance) — Severity-based ordering with exact fixes
