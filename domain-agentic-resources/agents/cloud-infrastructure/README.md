# Cloud Infrastructure Agents

> Specialized agents for cloud architecture, Kubernetes, Terraform, networking, and multi-cloud infrastructure.

## Available Agents

| Agent | Model | Description |
|-------|-------|-------------|
| [cloud-architect](cloud_architect.md) | OPUS | Expert cloud architect specializing in AWS/Azure/GCP multi-cloud infrastructure design, advanced IaC (Terraform/OpenTofu/CDK), FinOps cost optimization, and modern architectural patterns. |
| [firebase-architecture-reviewer](firebase_architecture_reviewer.md) | OPUS | Firebase architecture review agent evaluating overall Firebase project design including data model efficiency, service selection appropriateness, security posture, scalability bottlenecks, and cost trajectory. |
| [firebase-cost-analyst](firebase_cost_analyst.md) | SONNET | Firebase cost analysis agent examining usage patterns, producing cost reports with projections, optimization recommendations with estimated savings, alerts for cost anomalies, and free tier limit comparisons. |
| [firebase-security-auditor](firebase_security_auditor.md) | OPUS | Comprehensive Firebase security audit agent reviewing Firestore and RTDB security rules, exposed API keys in client code, App Check implementation, auth flow vulnerabilities, and Cloud Functions injection risks. |
| [hybrid-cloud-architect](hybrid_cloud_architect.md) | OPUS | Expert hybrid cloud architect specializing in complex multi-cloud solutions across AWS/Azure/GCP and private clouds (OpenStack/VMware). Masters hybrid connectivity and workload placement optimization. |
| [kubernetes-architect](kubernetes_architect.md) | OPUS | Expert Kubernetes architect specializing in cloud-native infrastructure, advanced GitOps workflows (ArgoCD/Flux), and enterprise container orchestration. |
| [network-engineer](network_engineer.md) | SONNET | Expert network engineer specializing in modern cloud networking, security architectures, and performance optimization. Masters multi-cloud connectivity and zero-trust networking. |
| [service-mesh-expert](service_mesh_expert.md) | INHERIT | Expert service mesh architect specializing in Istio, Linkerd, and cloud-native networking patterns. Masters traffic management, security policies, and observability integration. |
| [terraform-specialist](terraform_specialist.md) | OPUS | Expert Terraform/OpenTofu specialist mastering advanced IaC automation, state management, and enterprise infrastructure patterns. |

## Model Assignments

- **OPUS**: Used for critical cloud architecture decisions and complex infrastructure design
- **SONNET**: Used for networking tasks requiring careful security analysis
- **INHERIT**: Allows user to choose model based on infrastructure complexity

## Related Resources

- [Parent: Agents Overview](../README.md)
- [Skills: Cloud Infrastructure](../../skills/cloud-infrastructure/)
