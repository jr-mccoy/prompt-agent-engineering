---
title: "Dockerfile Optimization and Best Practices Analysis"
category: devops
description: "Analyze Dockerfiles for optimization, security, and best practices compliance"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-03
  - QA-01
difficulty: intermediate
tags:
  - docker
  - containers
  - optimization
  - security
  - cicd
updated: "2026-03-19"
---

# Dockerfile Optimization and Best Practices Analysis

**Objective:** Analyze Dockerfiles for optimization opportunities, security vulnerabilities, and adherence to best practices to produce smaller, faster, and more secure container images.

**When to Use:** Use this prompt when building or reviewing Docker images, optimizing CI/CD build times, reducing container image sizes, improving container security posture, or standardizing Dockerfile practices across teams.

**Instructions:**

1. **Analyze Base Image Selection**
   - Evaluate the chosen base image for appropriateness
   - Check for official or verified publisher images
   - Assess image size and security implications
   - Consider minimal base images (Alpine, distroless, scratch)
   - Verify base image version pinning (avoid `latest` tag)

2. **Review Layer Optimization**
   - Identify opportunities to combine RUN commands
   - Analyze layer ordering for cache efficiency
   - Check for unnecessary files being copied
   - Evaluate multi-stage build opportunities
   - Identify layers that frequently invalidate cache

3. **Security Analysis**
   - Check for running as non-root user
   - Identify hardcoded secrets or credentials
   - Review exposed ports for necessity
   - Analyze installed packages for CVE exposure
   - Check for `.dockerignore` usage to prevent secret leaks
   - Evaluate use of `HEALTHCHECK` instruction

4. **Build Performance Optimization**
   - Analyze COPY/ADD instruction ordering
   - Identify dependency installation patterns
   - Review use of build arguments and caching
   - Check for unnecessary build-time dependencies in final image
   - Evaluate parallel build opportunities

5. **Runtime Configuration**
   - Review ENTRYPOINT vs CMD usage
   - Check environment variable configuration
   - Analyze volume and mount point declarations
   - Review signal handling and graceful shutdown
   - Evaluate logging configuration

6. **Best Practices Compliance**
   - Check for `.dockerignore` file presence and completeness
   - Verify use of explicit tags over `latest`
   - Review instruction ordering conventions
   - Check for proper cleanup of temporary files
   - Validate metadata labels (LABEL instruction)

7. **Size Reduction Opportunities**
   - Identify removable development dependencies
   - Check for unneeded cache directories
   - Analyze package manager cleanup patterns
   - Review static file optimization
   - Consider compression opportunities

**Expected Output:** A comprehensive Dockerfile analysis report including:
- Current image size estimate and optimization potential
- Prioritized list of issues with severity ratings
- Specific code changes with before/after examples
- Security vulnerability assessment
- Build time optimization recommendations
- Refactored Dockerfile demonstrating best practices

**Example Output:**

```markdown
## Dockerfile Analysis Report

### Summary
- **Current Image Size**: ~1.2GB (estimated)
- **Optimized Size**: ~180MB (85% reduction possible)
- **Security Issues**: 3 High, 2 Medium, 4 Low
- **Build Time Issues**: 5 cache invalidation problems

### Critical Issues

#### Issue 1: Running as Root User (HIGH)
**Location**: Line 1-end (entire Dockerfile)
**Problem**: Container runs as root, increasing attack surface
**Current**:
```dockerfile
FROM node:18
WORKDIR /app
COPY . .
RUN npm install
CMD ["node", "server.js"]
```

**Recommended**:
```dockerfile
FROM node:18-slim AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM node:18-slim
RUN groupadd -r appgroup && useradd -r -g appgroup appuser
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY --chown=appuser:appgroup . .
USER appuser
EXPOSE 3000
CMD ["node", "server.js"]
```

#### Issue 2: Cache Invalidation on Every Build (MEDIUM)
**Location**: Lines 3-4
**Problem**: Copying all files before npm install invalidates cache on any file change
**Impact**: Full npm install on every build (~2-3 minutes wasted)
**Fix**: Copy package.json first, then install, then copy source files

#### Issue 3: No .dockerignore File (MEDIUM)
**Problem**: May copy unnecessary files (node_modules, .git, tests)
**Impact**: Larger build context, slower builds, potential secret exposure
**Recommended .dockerignore**:
```
node_modules
.git
.gitignore
*.md
tests/
coverage/
.env*
.docker*
```

### Security Checklist
| Check | Status | Notes |
|-------|--------|-------|
| Non-root user | FAIL | Add USER instruction |
| Base image pinned | WARN | Using `node:18`, recommend `node:18.19.0-slim` |
| No secrets in image | PASS | No hardcoded credentials found |
| HEALTHCHECK defined | FAIL | Add health check for orchestrator integration |
| Minimal packages | WARN | Full node image includes unnecessary tools |

### Optimized Dockerfile

```dockerfile
# Build stage
FROM node:18.19.0-alpine AS builder
WORKDIR /app

# Install dependencies first for better caching
COPY package*.json ./
RUN npm ci --only=production && npm cache clean --force

# Production stage
FROM node:18.19.0-alpine

# Security: Create non-root user
RUN addgroup -g 1001 -S appgroup && \
    adduser -S appuser -u 1001 -G appgroup

WORKDIR /app

# Copy only production dependencies
COPY --from=builder --chown=appuser:appgroup /app/node_modules ./node_modules
COPY --chown=appuser:appgroup . .

# Security: Run as non-root
USER appuser

# Metadata
LABEL maintainer="team@example.com" \
      version="1.0.0" \
      description="Production Node.js application"

# Health check for orchestration
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD node healthcheck.js || exit 1

EXPOSE 3000

CMD ["node", "server.js"]
```

### Build Time Improvements
| Optimization | Before | After | Improvement |
|--------------|--------|-------|-------------|
| Layer caching | ~4 min | ~30 sec | 87% faster |
| Multi-stage build | 1.2 GB | 180 MB | 85% smaller |
| Alpine base | 950 MB | 180 MB | 81% smaller |
```

**Techniques Used:**
- ST-01 (Clear Objective Statement)
- ST-02 (Sequential Step-by-Step Instructions)
- RT-02 (Multi-Dimensional Analysis)
- ST-03 (Structured Output Templates)
- DS-06 (Prioritization and Severity Guidance)
- RT-05 (Evidence-Based Reasoning)

**Related Prompts:**
- devops_kubernetes_manifest_review.md - For deploying optimized containers
- devops_container_security.md - For deeper security analysis
- devops_cicd_pipeline_analysis.md - For build pipeline optimization
- code-analysis/security/security_container_security_analysis.md - For runtime security

**Customization Guide:**
- **For Node.js Apps**: Focus on node_modules caching, multi-stage builds with npm ci
- **For Python Apps**: Emphasize pip wheel caching, virtual environments, slim/alpine bases
- **For Go Apps**: Highlight scratch/distroless images, static binary compilation
- **For Java Apps**: Focus on JRE vs JDK, jlink custom runtimes, layered JARs
- **For Multi-Service Repos**: Add guidance on shared base images and build matrices
