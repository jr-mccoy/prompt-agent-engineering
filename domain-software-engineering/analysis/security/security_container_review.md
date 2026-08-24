---
title: "Container and Docker Security Review"
category: code-analysis
description: "Container and Docker Security Review"
tags:
  - code-analysis
  - review
  - security
updated: "2026-03-19"
---

# Container and Docker Security Review

**Objective:** Analyze Docker containers, Dockerfiles, and container orchestration configurations to identify security vulnerabilities, misconfigurations, and best practice violations that could lead to container escapes, privilege escalation, or system compromise.

**Instructions:**

1. **Analyze Dockerfile security:**

   **A. Base Image Security**
   - [ ] Review base image source and trustworthiness
   - [ ] Check for official or verified images
   - [ ] Analyze base image size and bloat
   - [ ] Identify base image vulnerabilities (CVEs)
   - [ ] Review base image update frequency
   - [ ] Check for minimal/distroless base images (Alpine, scratch, distroless)
   - [ ] Verify image digest pinning (not just tags)
   - [ ] Check for outdated base images

   For each base image issue:
   - Document image source and version
   - Identify known vulnerabilities
   - Recommend secure alternatives

   **B. Dockerfile Build Security**
   - [ ] Review secret handling (no hardcoded secrets)
   - [ ] Check for secrets in build arguments
   - [ ] Analyze secret mounting using BuildKit secrets
   - [ ] Verify multi-stage builds for sensitive operations
   - [ ] Check for credential caching in layers
   - [ ] Review .dockerignore completeness
   - [ ] Analyze unnecessary file inclusion
   - [ ] Check for exposed sensitive files

   **C. Layer Optimization and Security**
   - [ ] Review layer count and optimization
   - [ ] Check for secret removal in same layer
   - [ ] Analyze cache utilization
   - [ ] Verify sensitive data not in intermediate layers
   - [ ] Check for unnecessary tools in final image (compilers, debuggers)
   - [ ] Review package manager cache cleanup

   **D. User and Permissions**
   - [ ] Check if running as non-root user
   - [ ] Verify USER directive usage
   - [ ] Review file ownership and permissions
   - [ ] Analyze sudo/setuid usage
   - [ ] Check for capability dropping
   - [ ] Verify no privileged container requirements

   **E. Package and Dependency Security**
   - [ ] Review installed packages necessity
   - [ ] Check for package vulnerabilities
   - [ ] Verify package signature validation
   - [ ] Analyze package manager update strategy
   - [ ] Check for unnecessary development dependencies
   - [ ] Review package pinning to specific versions

2. **Analyze Container Runtime Configuration:**

   **A. Docker Run / Docker Compose Security**
   - [ ] Review privileged mode usage (--privileged)
   - [ ] Check capability additions (--cap-add)
   - [ ] Analyze unnecessary capabilities granted
   - [ ] Verify read-only root filesystem (--read-only)
   - [ ] Check volume mounting security
   - [ ] Review host path mounting (avoid /var/run/docker.sock)
   - [ ] Analyze network mode (avoid host network)
   - [ ] Check PID namespace isolation
   - [ ] Review IPC namespace isolation
   - [ ] Verify user namespace remapping
   - [ ] Check resource limits (memory, CPU)
   - [ ] Analyze security options (seccomp, AppArmor, SELinux)

   **B. Environment Variables**
   - [ ] Check for secrets in environment variables
   - [ ] Review sensitive data exposure
   - [ ] Analyze environment variable injection risks
   - [ ] Verify secrets management solution usage (Docker Secrets, Kubernetes Secrets)

   **C. Network Security**
   - [ ] Review exposed ports necessity
   - [ ] Check for unnecessary port exposure
   - [ ] Analyze network isolation
   - [ ] Verify custom bridge networks
   - [ ] Check for host network mode misuse
   - [ ] Review inter-container communication

3. **Analyze Kubernetes Security (if applicable):**

   **A. Pod Security**
   - [ ] Review Pod Security Standards (Restricted, Baseline, Privileged)
   - [ ] Check runAsNonRoot enforcement
   - [ ] Analyze readOnlyRootFilesystem setting
   - [ ] Verify allowPrivilegeEscalation: false
   - [ ] Check securityContext configuration
   - [ ] Review privileged pod usage
   - [ ] Analyze hostPID, hostIPC, hostNetwork usage
   - [ ] Check capability dropping (drop: ALL)
   - [ ] Verify seccomp profile usage
   - [ ] Review AppArmor/SELinux profiles

   **B. Resource Management**
   - [ ] Review resource requests and limits
   - [ ] Check for missing resource limits (DoS risk)
   - [ ] Analyze CPU and memory allocations
   - [ ] Verify ephemeral storage limits

   **C. Network Policies**
   - [ ] Review NetworkPolicy definitions
   - [ ] Check for default deny policies
   - [ ] Analyze ingress/egress rules
   - [ ] Verify pod-to-pod communication restrictions
   - [ ] Check namespace isolation

   **D. Secrets and ConfigMaps**
   - [ ] Review secrets management
   - [ ] Check for secrets in ConfigMaps (should be in Secrets)
   - [ ] Analyze secrets encryption at rest
   - [ ] Verify secrets mounting (not env vars)
   - [ ] Review RBAC access to secrets
   - [ ] Check for external secrets manager integration (Vault, AWS Secrets Manager)

   **E. RBAC (Role-Based Access Control)**
   - [ ] Review ServiceAccount usage
   - [ ] Check for default ServiceAccount usage
   - [ ] Analyze Role and ClusterRole permissions
   - [ ] Verify principle of least privilege
   - [ ] Check for overly permissive RBAC
   - [ ] Review cluster-admin usage

   **F. Admission Controllers**
   - [ ] Verify PodSecurityPolicy or Pod Security Admission
   - [ ] Check for OPA (Open Policy Agent) usage
   - [ ] Review admission webhook configuration
   - [ ] Analyze image scanning enforcement
   - [ ] Check for policy enforcement

4. **Analyze Container Image Vulnerabilities:**

   **A. Vulnerability Scanning**
   - [ ] Scan for known CVEs (Trivy, Clair, Anchore)
   - [ ] Review critical and high severity vulnerabilities
   - [ ] Analyze exploitability in application context
   - [ ] Check for available patches
   - [ ] Verify vulnerability scanning in CI/CD

   **B. Image Composition Analysis**
   - [ ] Review installed packages inventory
   - [ ] Analyze unnecessary binaries (shells, compilers)
   - [ ] Check for development tools in production images
   - [ ] Verify minimal attack surface
   - [ ] Review package provenance

5. **Analyze Container Registry Security:**
   - [ ] Review registry authentication
   - [ ] Check for registry vulnerability scanning
   - [ ] Analyze image signing and verification (Docker Content Trust, Notary, Cosign)
   - [ ] Review access controls on registries
   - [ ] Check for webhook integration for scanning
   - [ ] Verify registry encryption in transit and at rest

6. **Analyze Container Runtime Security:**
   - [ ] Review container runtime (Docker, containerd, CRI-O)
   - [ ] Check runtime security updates
   - [ ] Analyze runtime configuration
   - [ ] Verify runtime security monitoring
   - [ ] Review seccomp profiles
   - [ ] Check AppArmor/SELinux enforcement

7. **For each identified issue, provide:**
   - Security issue type (image vulnerability, misconfiguration, privilege issue)
   - Location (Dockerfile line, K8s manifest, docker-compose)
   - Severity rating (Critical, High, Medium, Low)
   - CVE IDs (if applicable)
   - Exploitation scenario
   - Potential impact (container escape, privilege escalation, data breach)
   - Remediation guidance with secure examples
   - Best practice recommendations

**Expected Output:** A comprehensive container security analysis including:

- **Executive Summary:**
  - Total containers analyzed
  - Vulnerability count by severity
  - Critical misconfigurations
  - Overall container security posture
  - High-priority remediation items

- **Dockerfile Security Analysis:**
  For each Dockerfile:
  - Base image security assessment
  - Vulnerabilities in base image
  - Build security issues
  - User and permission issues
  - Secrets exposure risks
  - Optimization recommendations
  - Secure Dockerfile example

- **Container Runtime Configuration:**
  - Privileged container usage
  - Capability analysis
  - Volume mount security
  - Network isolation
  - Resource limits
  - Security options (seccomp, AppArmor)
  - Recommendations

- **Kubernetes Security Assessment (if applicable):**
  - Pod Security Standard compliance
  - RBAC evaluation
  - Network Policy review
  - Secrets management
  - Resource management
  - Admission control
  - Recommendations

- **Vulnerability Scan Results:**
  - Critical vulnerabilities requiring immediate patching
  - High severity vulnerabilities
  - Exploitable vs non-exploitable CVEs
  - Update recommendations
  - Alternative base images

- **Container Registry Security:**
  - Registry configuration review
  - Image signing status
  - Access control assessment
  - Vulnerability scanning integration

- **Remediation Roadmap:**

  **Immediate (Critical):**
  - Patch critical CVEs
  - Remove privileged container usage
  - Fix secret exposure
  - Implement non-root users

  **Short-term (High):**
  - Update vulnerable base images
  - Implement seccomp/AppArmor profiles
  - Configure NetworkPolicies
  - Enhance RBAC
  - Implement image scanning in CI/CD

  **Medium-term:**
  - Migrate to minimal base images
  - Implement Pod Security Standards
  - Deploy runtime security monitoring
  - Set up vulnerability management process

  **Long-term:**
  - Implement zero-trust container security
  - Deploy service mesh
  - Implement supply chain security (SBOM, provenance)
  - Continuous compliance monitoring

- **Best Practices and Tools:**
  - Secure Dockerfile patterns
  - Container scanning tools (Trivy, Snyk, Aqua)
  - Runtime security tools (Falco, Sysdig)
  - Policy enforcement (OPA, Kyverno)
  - Image hardening guides

**Example Output Format:**

```
CRITICAL: Running Container as Root User
Location: Dockerfile:15 (no USER directive)
Severity: HIGH

Issue:
  Container runs all processes as root (UID 0), violating principle
  of least privilege and increasing risk of container escape.

Vulnerable Dockerfile:
  FROM node:18
  WORKDIR /app
  COPY package*.json ./
  RUN npm install
  COPY . .
  EXPOSE 3000
  CMD ["node", "server.js"]

Risk:
  - If application is compromised, attacker has root privileges
  - Container escape vulnerability provides root on host
  - Increased attack surface
  - Non-compliance with security standards (PCI-DSS, SOC2)

Exploitation Scenario:
  1. Attacker exploits application vulnerability (RCE)
  2. Attacker has root privileges in container
  3. Attacker exploits kernel vulnerability for container escape
  4. Attacker gains root on host system

Remediation:
  FROM node:18
  WORKDIR /app

  # Copy files and install dependencies as root
  COPY package*.json ./
  RUN npm install --production

  # Create non-root user
  RUN groupadd -r appuser && useradd -r -g appuser appuser

  # Copy application files
  COPY --chown=appuser:appuser . .

  # Switch to non-root user
  USER appuser

  EXPOSE 3000
  CMD ["node", "server.js"]

Kubernetes Additional Security:
  apiVersion: v1
  kind: Pod
  metadata:
    name: myapp
  spec:
    securityContext:
      runAsNonRoot: true
      runAsUser: 1000
      fsGroup: 1000
    containers:
    - name: myapp
      image: myapp:1.0
      securityContext:
        allowPrivilegeEscalation: false
        readOnlyRootFilesystem: true
        capabilities:
          drop:
          - ALL

Testing:
  # Verify container runs as non-root
  docker run myapp id
  # Should output: uid=1000(appuser) gid=1000(appuser)

Priority: HIGH
Timeline: 1 week
```

**Related Prompts:**
- security_owasp_top_10_analysis.md - Application security
- security_dependency_vulnerability_analysis.md - Dependency vulnerabilities
- security_infrastructure_analysis.md - Infrastructure security
- security_compliance_analysis.md - Compliance requirements

**When to Use:**
Use this prompt when reviewing Dockerfiles, before deploying containers to production, during security audits, when migrating to containers, as part of CI/CD security gates, or when investigating container security incidents. Essential for securing containerized applications and Kubernetes clusters.

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Opens with concise, unambiguous objective
- ST-02 (Structured Sequential Instructions) - Numbered steps with detailed checklists
- DT-02 (Specific Focus Areas with Examples) - Comprehensive Docker and Kubernetes categories
- RT-02 (Multi-Dimensional Analysis Framework) - Issue, Location, Severity, Risk, Remediation
- DS-06 (Prioritization and Severity Guidance) - Severity ratings and remediation timelines
- ST-03 (Output Format Templates) - Detailed vulnerability output with Dockerfile examples
- AG-05 (Concrete Deliverable Templates) - Complete secure Dockerfile and K8s examples
- DS-03 (Tool and Methodology Suggestions) - Recommends Trivy, Snyk, Falco, OPA
