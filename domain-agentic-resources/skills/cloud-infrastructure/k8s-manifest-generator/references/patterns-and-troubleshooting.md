# Kubernetes Manifest Generator — Common Patterns and Troubleshooting

## Common Patterns

### Pattern 1: Simple Stateless Web Application

**Use case:** Standard web API or microservice

**Components needed:**
- Deployment (3 replicas for HA)
- ClusterIP Service
- ConfigMap for configuration
- Secret for API keys
- HorizontalPodAutoscaler (optional)

**Reference:** See `assets/deployment-template.yaml`

### Pattern 2: Stateful Database Application

**Use case:** Database or persistent storage application

**Components needed:**
- StatefulSet (not Deployment)
- Headless Service
- PersistentVolumeClaim template
- ConfigMap for DB configuration
- Secret for credentials

### Pattern 3: Background Job or Cron

**Use case:** Scheduled tasks or batch processing

**Components needed:**
- CronJob or Job
- ConfigMap for job parameters
- Secret for credentials
- ServiceAccount with RBAC

### Pattern 4: Multi-Container Pod

**Use case:** Application with sidecar containers

**Components needed:**
- Deployment with multiple containers
- Shared volumes between containers
- Init containers for setup
- Service (if needed)

---

## Troubleshooting

**Pods not starting:**
- Check image pull errors: `kubectl describe pod <pod-name>`
- Verify resource availability: `kubectl get nodes`
- Check events: `kubectl get events --sort-by='.lastTimestamp'`

**Service not accessible:**
- Verify selector matches pod labels: `kubectl get endpoints <service-name>`
- Check service type and port configuration
- Test from within cluster: `kubectl run debug --rm -it --image=busybox -- sh`

**ConfigMap/Secret not loading:**
- Verify names match in Deployment
- Check namespace
- Ensure resources exist: `kubectl get configmap,secret`

---

## Next Steps After Creating Manifests

1. Store in Git repository
2. Set up CI/CD pipeline for deployment
3. Consider using Helm or Kustomize for templating
4. Implement GitOps with ArgoCD or Flux
5. Add monitoring and observability
