# Java / Spring Prompts

Prompts for reviewing and improving Java applications and the Spring / Spring Boot ecosystem — architecture, security, performance, and build tooling.

**Total Prompts:** 4

---

## Prompts

| Prompt | When to Use |
|--------|-------------|
| `java_spring_boot_architecture_review.md` | Review Spring Boot application layering, bean wiring, config hygiene |
| `java_spring_security_review.md` | Review Spring Security configuration, filter chain, auth flows |
| `java_jvm_performance_tuning.md` | Tune JVM flags, GC selection, heap/metaspace sizing, profiling |
| `java_maven_gradle_optimization.md` | Optimize Maven / Gradle builds, multi-module layout, caching |

---

## Quick Selection Guide

**"Review my Spring Boot service"** → `java_spring_boot_architecture_review.md`

**"Audit Spring Security config"** → `java_spring_security_review.md`

**"App is slow / GC-thrashing under load"** → `java_jvm_performance_tuning.md`

**"Speed up / clean up our build"** → `java_maven_gradle_optimization.md`

---

## Related Categories

- **[Analysis/Architecture](../analysis/architecture/)** — Cross-language architecture review prompts
- **[Analysis/Performance](../analysis/performance/)** — Generic performance analysis
- **[Analysis/Security](../analysis/security/)** — Generic security analysis
- **[DevOps](../devops/)** — CI/CD, Docker, Kubernetes for JVM services
- **[API](../api/)** — REST / GraphQL / OpenAPI design prompts

---

## Coverage Notes

These prompts cover modern Java (17+) and Spring Boot 3.x conventions. If you need language-agnostic reviews, prefer the generic prompts in `../analysis/`. Use these Java/Spring-specific prompts when your codebase uses Spring annotations, Spring config, JVM-specific tuning, or Maven/Gradle build tooling.
