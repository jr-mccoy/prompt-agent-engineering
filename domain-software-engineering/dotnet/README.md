# .NET Prompts

Prompts for reviewing and improving .NET applications — ASP.NET Core, Entity Framework, NuGet dependencies, and API patterns.

**Total Prompts:** 4

---

## Prompts

| Prompt | When to Use |
|--------|-------------|
| `dotnet_aspnet_middleware_di.md` | Review ASP.NET Core middleware pipeline and DI container usage |
| `dotnet_entity_framework_optimization.md` | Review EF Core queries, change tracking, migrations, N+1 issues |
| `dotnet_api_development_patterns.md` | Review ASP.NET Core API design, controllers, minimal APIs, validation |
| `dotnet_nuget_dependency_management.md` | Audit NuGet package graph, transitive versions, vulnerable deps |

---

## Quick Selection Guide

**"Review our ASP.NET Core middleware / DI setup"** → `dotnet_aspnet_middleware_di.md`

**"EF Core is slow / generates bad SQL"** → `dotnet_entity_framework_optimization.md`

**"Review our .NET API surface"** → `dotnet_api_development_patterns.md`

**"NuGet dependency cleanup / audit"** → `dotnet_nuget_dependency_management.md`

---

## Related Categories

- **[Analysis/Architecture](../analysis/architecture/)** — Cross-language architecture review prompts
- **[Analysis/Performance](../analysis/performance/)** — Generic performance analysis
- **[Analysis/Security](../analysis/security/)** — Generic security analysis
- **[Analysis/Database](../analysis/database/)** — Schema design, query optimization, migrations
- **[DevOps](../devops/)** — CI/CD, Docker, Kubernetes for .NET services
- **[API](../api/)** — REST / GraphQL / OpenAPI design prompts

---

## Coverage Notes

These prompts assume .NET 8+ and ASP.NET Core conventions. For language-agnostic reviews, prefer the generic prompts in `../analysis/`. Use these .NET-specific prompts when your codebase uses ASP.NET Core middleware, EF Core, NuGet, or relies on .NET-specific runtime behavior.
