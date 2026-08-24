# Technique Analysis: security-auditor

**Resource Type:** Agent (Opus 4.5)
**Path:** `claude-code-resources/agents/architecture/security-auditor.md`
**Date Analyzed:** 2025-12-23
**Category:** Architecture, Security, Orchestration (appears in 3 categories)
**Lines:** 139

---

## Summary

The security-auditor agent is one of the most comprehensive Opus agents, demonstrating **expert persona engineering** with deep domain specialization in DevSecOps and cybersecurity. It showcases **capability enumeration at scale** (9 major capability domains, 50+ specific capabilities) and uses **proactive activation patterns** for security-first development. This agent exemplifies how to structure expert knowledge for maximum coverage while maintaining coherent identity.

---

## Identified Techniques

### Technique 1: Expert Persona with Domain Depth

- **Category:** ST (Structural Techniques)
- **Pattern:** Define specialist identity with comprehensive domain coverage
- **Example from resource:**
  ```
  You are a security auditor specializing in DevSecOps, application security,
  and comprehensive cybersecurity practices.

  ## Purpose
  Expert security auditor with comprehensive knowledge of modern cybersecurity
  practices, DevSecOps methodologies, and compliance frameworks.
  ```
- **Maps to existing:** ST-01 (Role Assignment) + ST-02 (Persona Definition)
- **Effectiveness:** Establishes clear identity that constrains responses to security domain while providing comprehensive coverage

### Technique 2: Hierarchical Capability Enumeration

- **Category:** ST (Structural Techniques)
- **Pattern:**
  ```
  ## Capabilities

  ### Domain 1: [Major Category]
  - **Subdomain A**: specific capabilities, tools, techniques
  - **Subdomain B**: specific capabilities, tools, techniques

  ### Domain 2: [Major Category]
  ...
  ```
- **Example from resource:** 9 major domains (DevSecOps, Authentication, OWASP, Security Testing, Cloud Security, Compliance, Secure Coding, Network Security, Monitoring) each with 5-8 specific subdomains
- **Maps to existing:** ST-04 (Structured Prompts) - but at **agent architecture level**
- **Effectiveness:** Provides searchable, comprehensive reference for all security capabilities

### Technique 3: Tool Integration Patterns

- **Category:** DS (Domain-Specific)
- **Pattern:** Enumerate specific tools for each capability category
- **Example from resource:**
  ```
  ### Application Security Testing
  - **Static analysis (SAST)**: SonarQube, Checkmarx, Veracode, Semgrep, CodeQL
  - **Dynamic analysis (DAST)**: OWASP ZAP, Burp Suite, Nessus, web application scanning
  - **Dependency scanning**: Snyk, WhiteSource, OWASP Dependency-Check, GitHub Security
  ```
- **Maps to existing:** DS-05 (Tool Integration) - significantly expanded with 50+ tools
- **Effectiveness:** Provides actionable tool recommendations, enables Claude to suggest specific tools for specific problems

### Technique 4: Proactive Activation Trigger

- **Category:** IT (Interaction Techniques)
- **Pattern:** "Use PROACTIVELY for [specific scenarios]" in description
- **Example from resource:**
  ```
  description: ... Use PROACTIVELY for security audits, DevSecOps, or compliance implementation.
  ```
- **Maps to existing:** IT-08 (Activation Criteria) - but with **proactive emphasis**
- **Effectiveness:** Tells orchestration systems WHEN to invoke this agent, reduces need for explicit user request

### Technique 5: Behavioral Traits as Guardrails

- **Category:** AG (Agentic)
- **Pattern:** Define behavioral principles that constrain agent actions
- **Example from resource:**
  ```
  ## Behavioral Traits
  - Implements defense-in-depth with multiple security layers and controls
  - Applies principle of least privilege with granular access controls
  - Never trusts user input and validates everything at multiple layers
  - Fails securely without information leakage or system compromise
  - Focuses on practical, actionable fixes over theoretical security risks
  ```
- **Maps to existing:** NEW - AG-23 (Behavioral Guardrails)
- **Effectiveness:** Ensures consistent security-first behavior regardless of task

### Technique 6: Step-by-Step Response Protocol

- **Category:** RT (Reasoning Techniques)
- **Pattern:** Numbered steps defining how agent should approach any task
- **Example from resource:**
  ```
  ## Response Approach
  1. **Assess security requirements** including compliance and regulatory needs
  2. **Perform threat modeling** to identify potential attack vectors and risks
  3. **Conduct comprehensive security testing** using appropriate tools and techniques
  4. **Implement security controls** with defense-in-depth principles
  5. **Automate security validation** in development and deployment pipelines
  6. **Set up security monitoring** for continuous threat detection and response
  7. **Document security architecture** with clear procedures and incident response plans
  8. **Plan for compliance** with relevant regulatory and industry standards
  9. **Provide security training** and awareness for development teams
  ```
- **Maps to existing:** RT-01 (Chain of Thought) - but as **agent methodology**
- **Effectiveness:** Ensures comprehensive coverage and consistent approach to any security task

### Technique 7: Example Interactions as Training Data

- **Category:** IT (Interaction Techniques)
- **Pattern:** Provide 7-8 diverse example prompts that trigger the agent
- **Example from resource:**
  ```
  ## Example Interactions
  - "Conduct comprehensive security audit of microservices architecture with DevSecOps integration"
  - "Implement zero-trust authentication system with multi-factor authentication and risk-based access"
  - "Design security pipeline with SAST, DAST, and container scanning for CI/CD workflow"
  ```
- **Maps to existing:** RT-07 (Few-Shot Examples) - but for **agent activation**
- **Effectiveness:** Shows the range of tasks the agent handles, enables pattern matching for orchestration

### Technique 8: Framework-Based Knowledge Organization

- **Category:** DS (Domain-Specific)
- **Pattern:** Organize knowledge around industry frameworks
- **Example from resource:**
  ```
  ### OWASP & Vulnerability Management
  - **OWASP Top 10 (2021)**: Broken access control, cryptographic failures, injection, insecure design
  - **OWASP ASVS**: Application Security Verification Standard, security requirements
  - **OWASP SAMM**: Software Assurance Maturity Model, security maturity assessment
  ```
- **Maps to existing:** DS-06 (Domain Standards) - with **comprehensive framework mapping**
- **Effectiveness:** Aligns agent knowledge with industry standards, enables compliance-focused responses

### Technique 9: Emerging Technology Section

- **Category:** DS (Domain-Specific)
- **Pattern:** Include forward-looking section on emerging technologies
- **Example from resource:**
  ```
  ### Emerging Security Technologies
  - **AI/ML security**: Model security, adversarial attacks, privacy-preserving ML
  - **Quantum-safe cryptography**: Post-quantum cryptographic algorithms, migration planning
  - **Zero-knowledge proofs**: Privacy-preserving authentication, blockchain security
  - **Homomorphic encryption**: Privacy-preserving computation, secure data processing
  - **Confidential computing**: Trusted execution environments, secure enclaves
  ```
- **Maps to existing:** NEW - DS-103 (Future-Proofing Expertise)
- **Effectiveness:** Keeps agent relevant for cutting-edge scenarios, demonstrates comprehensive knowledge

### Technique 10: Multi-Category Deployment

- **Category:** AG (Agentic)
- **Pattern:** Same agent appears in multiple category directories for discoverability
- **Example from resource:** security-auditor appears in:
  - `agents/architecture/security-auditor.md`
  - `agents/security/security-auditor.md`
  - `agents/orchestration/security-auditor.md`
- **Maps to existing:** NEW - AG-24 (Multi-Category Indexing)
- **Effectiveness:** Increases discoverability, enables categorization by function OR domain

---

## Novel Patterns (Not in MASTER_TECHNIQUE_INDEX)

### Pattern 1: AG-23 - Behavioral Guardrails for Agents

- **Description:** Define explicit behavioral constraints that apply to all agent actions
- **Implementation:**
  ```markdown
  ## Behavioral Traits
  - [Positive behavior 1]: [specific implementation]
  - [Positive behavior 2]: [specific implementation]
  - [Negative behavior]: "Never [undesired action]"
  - [Priority behavior]: "Prioritizes [value] over [trade-off]"
  ```
- **Use case:** Any agent needing consistent behavioral patterns
- **Example:**
  ```markdown
  ## Behavioral Traits
  - Implements defense-in-depth with multiple security layers
  - Never trusts user input and validates at multiple layers
  - Fails securely without information leakage
  - Prioritizes practical fixes over theoretical risks
  ```
- **Proposed category:** AG (Agentic)
- **Proposed code:** AG-23
- **Integration:** Add to MASTER_TECHNIQUE_INDEX under Agentic Techniques

### Pattern 2: DS-103 - Future-Proofing Expertise

- **Description:** Include emerging technologies section to maintain agent relevance
- **Implementation:**
  ```markdown
  ### Emerging [Domain] Technologies
  - **[Tech 1]**: [applications, use cases]
  - **[Tech 2]**: [applications, use cases]
  - **[Tech 3]**: [applications, use cases]
  ```
- **Use case:** Expert agents that need to handle cutting-edge scenarios
- **Example:**
  ```markdown
  ### Emerging Security Technologies
  - **AI/ML security**: Model security, adversarial attacks
  - **Quantum-safe cryptography**: Post-quantum algorithms
  - **Zero-knowledge proofs**: Privacy-preserving authentication
  ```
- **Proposed category:** DS (Domain-Specific)
- **Proposed code:** DS-103
- **Integration:** Recommend for all domain expert agents

### Pattern 3: AG-24 - Multi-Category Indexing

- **Description:** Deploy same agent in multiple category directories for enhanced discoverability
- **Implementation:**
  - Create symlinks or copies in relevant category directories
  - Maintain single source of truth for agent content
  - Index agent under all relevant categories (function, domain, workflow)
- **Use case:** Agents that serve multiple domains or functions
- **Example:**
  - `agents/architecture/security-auditor.md` (architecture focus)
  - `agents/security/security-auditor.md` (security domain)
  - `agents/orchestration/security-auditor.md` (workflow integration)
- **Proposed category:** AG (Agentic)
- **Proposed code:** AG-24
- **Integration:** Document as best practice for agent organization

---

## Multi-Technique Combinations

### Combination 1: Expert Persona + Hierarchical Capabilities + Tool Integration

- **Technique Stack:** ST-01 + ST-04 + DS-05
- **Combination Purpose:** Create comprehensive domain expert agent
- **Flow:**
  1. Define expert identity (ST-01)
  2. Enumerate capabilities hierarchically (ST-04)
  3. Provide specific tools for each capability (DS-05)
- **Synergies:** Creates authoritative expert that can recommend specific tools

### Combination 2: Behavioral Guardrails + Response Protocol + Example Interactions

- **Technique Stack:** AG-23 (novel) + RT-01 + RT-07
- **Combination Purpose:** Ensure consistent, high-quality agent behavior
- **Flow:**
  1. Define behavioral constraints (AG-23)
  2. Provide step-by-step methodology (RT-01)
  3. Demonstrate with diverse examples (RT-07)
- **Synergies:** Agent behaves consistently across all interaction types

### Combination 3: Framework Knowledge + Proactive Activation + Multi-Category Indexing

- **Technique Stack:** DS-06 + IT-08 + AG-24 (novel)
- **Combination Purpose:** Maximize agent utility and discoverability
- **Flow:**
  1. Organize knowledge around industry frameworks (DS-06)
  2. Define proactive triggers (IT-08)
  3. Index under multiple categories (AG-24)
- **Synergies:** Agent found easily and invoked appropriately

---

## Notes for Integration

### Add to MASTER_TECHNIQUE_INDEX:
1. **AG-23: Behavioral Guardrails** - Explicit behavioral constraints for agents
2. **DS-103: Future-Proofing Expertise** - Emerging technology sections
3. **AG-24: Multi-Category Indexing** - Deploy agents in multiple directories

### Cross-reference with prompts:
- **code-analysis/security/security_vulnerability_analysis.md** - One-time version
- **code-analysis/security/security_sql_injection_detection.md** - Specific security focus
- **devops/devops_security_hardening.md** - DevSecOps alignment

### Documentation improvements:
1. **AI_AGENT_QUICK_START.md** - Add section on agent behavioral traits
2. **CLAUDE.md** - Reference security-auditor for security workflows
3. **agency-agents/README.md** - Document multi-category pattern

---

## Analysis Metadata

**Analyzer:** Claude (Task 2.2 Priority 3 - Opus Agent Analysis)
**Analysis Duration:** 25 minutes
**Confidence Level:** High
**Review Status:** Draft
**Priority for Integration:** **High** (critical security patterns, 3 novel techniques)

---

## Technique Complexity Score

**Score: 5/5** (Maximum Complexity)

**Rationale:**
- Uses 10+ distinct techniques
- 3 novel patterns not in existing index
- Comprehensive domain coverage (50+ capabilities)
- Multi-category deployment pattern
- Proactive activation with behavioral guardrails
- This is a reference implementation for Opus-level agents

---

## Key Insights

1. **Opus agents are comprehensive**: The 139-line security-auditor covers more ground than most prompt files, demonstrating how agents can encapsulate deep expertise.

2. **Behavioral guardrails are essential**: The "Behavioral Traits" section ensures consistent security-first behavior regardless of the specific task.

3. **Tool enumeration enables action**: By listing 50+ specific security tools, the agent can provide immediately actionable recommendations.

4. **Proactive triggers change interaction model**: "Use PROACTIVELY" shifts from user-initiated to agent-initiated security reviews.

5. **Multi-category indexing maximizes utility**: Deploying in 3 directories (architecture, security, orchestration) ensures the agent is found for any relevant workflow.

6. **Framework alignment ensures credibility**: Organizing knowledge around OWASP, NIST, and compliance frameworks establishes authority and enables standard-compliant responses.

---

## Recommendations

1. **Document AG-23 (Behavioral Guardrails)** as high-priority technique - essential for agent consistency
2. **Document DS-103 (Future-Proofing)** for maintaining agent relevance
3. **Document AG-24 (Multi-Category Indexing)** as best practice for agent organization
4. **Create mapping**: security-auditor → existing security prompts
5. **Use as template**: This agent should be the reference for other Opus-level security experts
