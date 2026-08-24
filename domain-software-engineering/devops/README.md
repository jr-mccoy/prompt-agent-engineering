# DevOps Prompts

Prompts for infrastructure, containerization, CI/CD pipelines, and deployment workflows.

**Total Prompts:** 21

---

## Prompts

| Prompt | When to Use |
|--------|-------------|
| `devops_dockerfile_optimization.md` | Optimize Docker images |
| `devops_kubernetes_manifest_review.md` | Review K8s configurations |
| `devops_helm_chart_review.md` | Audit Helm charts |
| `devops_container_security.md` | Container security audit |
| `devops_terraform_best_practices.md` | Terraform code review |
| `devops_infrastructure_as_code_review.md` | IaC best practices |
| `devops_cicd_pipeline_analysis.md` | CI/CD pipeline review |
| `devops_gitops_workflow.md` | GitOps implementation basics |
| `devops_gitops_workflow_review.md` | Review ArgoCD / Flux setup, repo structure, drift handling |
| `devops_opentelemetry_instrumentation.md` | Review/design OpenTelemetry traces/metrics/logs |
| `devops_monitoring_observability.md` | Monitoring setup review |
| `devops_workflow_guide.md` | Overall DevOps workflow guide (reference) |
| `llm_ops_*.md` (10) | LLM operations: model selection, RAG, vector DB, hallucination, fine-tuning, evaluation, etc. |

---

## By Area

### Containerization
- `devops_dockerfile_optimization.md` - Optimize Dockerfile builds
- `devops_container_security.md` - Container security hardening
- `devops_kubernetes_manifest_review.md` - K8s manifest review
- `devops_helm_chart_review.md` - Helm chart best practices

### Infrastructure as Code
- `devops_terraform_best_practices.md` - Terraform patterns
- `devops_infrastructure_as_code_review.md` - General IaC review

### CI/CD & Deployment
- `devops_cicd_pipeline_analysis.md` - Pipeline optimization
- `devops_gitops_workflow.md` - GitOps patterns

### Operations
- `devops_monitoring_observability.md` - Monitoring and alerting

---

## Quick Selection Guide

**"Optimize my Dockerfile"** → `devops_dockerfile_optimization.md`

**"Review K8s manifests"** → `devops_kubernetes_manifest_review.md`

**"Audit Helm charts"** → `devops_helm_chart_review.md`

**"Secure containers"** → `devops_container_security.md`

**"Review Terraform code"** → `devops_terraform_best_practices.md`

**"Improve CI/CD pipeline"** → `devops_cicd_pipeline_analysis.md`

**"Set up monitoring"** → `devops_monitoring_observability.md`

---

## Related Categories

- **[Cloud](../cloud/)** - Cloud provider-specific prompts
- **[Code Analysis/Security](../analysis/security/)** - Security analysis
- **[Testing](../testing/)** - Test pipeline integration
- **[Engineering](../../domain-agentic-resources/personas/engineering/)** - Development workflows

---

## Technology Coverage

| Technology | Prompts |
|------------|---------|
| Docker | `dockerfile_optimization`, `container_security` |
| Kubernetes | `kubernetes_manifest_review`, `helm_chart_review` |
| Terraform | `terraform_best_practices`, `infrastructure_as_code_review` |
| CI/CD | `cicd_pipeline_analysis`, `gitops_workflow` |
| Monitoring | `monitoring_observability` |

---

## Best Practices Highlights

### Container Optimization
- Multi-stage builds for smaller images
- Layer caching optimization
- Security scanning integration

### Kubernetes
- Resource limits and requests
- Health checks and probes
- RBAC configuration

### Infrastructure as Code
- Module organization
- State management
- Security hardening
