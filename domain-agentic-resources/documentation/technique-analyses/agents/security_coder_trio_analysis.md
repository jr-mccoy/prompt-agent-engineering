# Technique Analysis: Security-Coder Agents (Trio)

**Resource Type:** Agent (SONNET Model - 3 agents analyzed together)
**Paths:**
- `agents/backend/backend-security-coder.md` (137 lines)
- `agents/frontend-mobile/frontend-security-coder.md` (150 lines)
- `agents/frontend-mobile/mobile-security-coder.md` (164 lines)
**Date Analyzed:** 2025-12-23
**Total Lines:** 451 lines
**Model Assignment:** SONNET (balanced intelligence/speed for security coding tasks)
**Complexity:** 5/5 (Sophisticated security-first development system)

---

## Overview

These three agents form a cohesive **platform-specific security coding system** designed to implement secure coding practices across different application layers:

```
Backend → Frontend → Mobile
(Server-side) → (Client-side) → (Platform-specific)
```

This is a sophisticated multi-agent security implementation pipeline that demonstrates advanced prompting techniques for:
- Contrastive role disambiguation between similar agents
- Security-first behavioral defaults that shape all responses
- Platform-adaptive security patterns
- Privacy-security integration as unified concern
- Environment-aware security configuration

---

## Identified Techniques

### Technique 1: Contrastive Role Disambiguation
- **Category:** AG (Agentic) - NEW
- **Pattern:** Explicit "When to Use vs X" sections that contrast the agent's role with a similar agent
- **Example from resource:**
  ```markdown
  ## When to Use vs Security Auditor
  - **Use this agent for**: Hands-on backend security coding, API security implementation
  - **Use security-auditor for**: High-level security audits, compliance assessments
  - **Key difference**: This agent focuses on writing secure backend code, while
    security-auditor focuses on auditing and assessing security posture
  ```
- **Maps to existing:** Extends ST-02 (Persona Assignment) - but adds CONTRASTIVE definition
- **Effectiveness:** Clear agent selection in multi-agent workflows, prevents role confusion
- **Novelty:** NEW - **AG-31: Contrastive Role Disambiguation**

### Technique 2: Security-Default Behavioral Traits
- **Category:** DS (Domain-Specific) - NEW
- **Pattern:** Behavioral traits are security-specific defaults that automatically apply to all responses
- **Example from resource:**
  - Backend: "Validates and sanitizes all user inputs using allowlist approaches"
  - Frontend: "Always prefers textContent over innerHTML for dynamic content"
  - Mobile: "Enforces HTTPS-only communication with certificate pinning"
- **Maps to existing:** Related to behavioral traits but with SECURITY DEFAULTS
- **Effectiveness:** Ensures security-first implementation without explicit reminders
- **Novelty:** NEW - **DS-118: Security-Default Behavioral Traits**

### Technique 3: Allowlist-First Strategy Pattern
- **Category:** DS (Domain-Specific) - NEW
- **Pattern:** Consistent emphasis on allowlist/whitelist approaches as security meta-pattern
- **Example from resource:**
  ```markdown
  - **Input validation and sanitization**: Comprehensive input validation frameworks,
    allowlist approaches, data type enforcement
  - **Allowlist validation**: Whitelist-based input validation, predefined value sets
  - **URL allowlisting**: Trusted domain restrictions, URL validation, protocol enforcement
  ```
- **Maps to existing:** New security philosophy pattern
- **Effectiveness:** Systematic secure-by-default validation strategy
- **Novelty:** NEW - **DS-119: Allowlist-First Security Strategy**

### Technique 4: Environment-Aware Security Configuration
- **Category:** DS (Domain-Specific) - NEW
- **Pattern:** Security configurations that adapt based on deployment environment (dev vs prod)
- **Example from resource:**
  ```markdown
  - **Environment-specific deployment**: Apply clickjacking protection only in production
    or standalone applications, disable or relax during development when embedding in iframes
  ```
- **Maps to existing:** Related to context-awareness but for SECURITY POLICY
- **Effectiveness:** Balances security with development workflow requirements
- **Novelty:** NEW - **DS-120: Environment-Adaptive Security Policy**

### Technique 5: Platform-Specific Security Adaptation
- **Category:** DS (Domain-Specific) - NEW
- **Pattern:** Security implementations that adapt to specific platforms with platform-native patterns
- **Example from resource:**
  ```markdown
  ### Platform-Specific Security
  - **iOS security**: Keychain Services, App Transport Security, iOS permission model
  - **Android security**: Android Keystore, Network Security Config, ProGuard/R8 obfuscation
  - **Cross-platform**: React Native security, Flutter security, Xamarin security patterns
  ```
- **Maps to existing:** New platform-adaptive security pattern
- **Effectiveness:** Leverages platform-native security features appropriately
- **Novelty:** NEW - **DS-121: Platform-Adaptive Security Implementation**

### Technique 6: Authoritative Security Standards Grounding
- **Category:** DS (Domain-Specific) - EXISTING
- **Pattern:** Knowledge Base section lists authoritative security standards that ground responses
- **Example from resource:**
  ```markdown
  ## Knowledge Base
  - OWASP Top 10 and secure coding guidelines
  - OWASP MASVS (Mobile Application Security Verification Standard)
  - Common vulnerability patterns and prevention techniques
  ```
- **Maps to existing:** DS-111 (External Methodology Compliance) from C4 agents
- **Effectiveness:** Responses aligned with industry security standards

### Technique 7: Security Checklist Response Protocol
- **Category:** DS (Domain-Specific) - NEW
- **Pattern:** Response Approach as numbered security implementation checklist
- **Example from resource:**
  ```markdown
  ## Response Approach
  1. **Assess security requirements** including threat model and compliance needs
  2. **Implement input validation** with comprehensive sanitization
  3. **Configure secure authentication** with multi-factor authentication
  4. **Apply database security** with parameterized queries
  5. **Set security headers** and implement CSRF protection
  ...
  9. **Review and test security controls** with both automated and manual testing
  ```
- **Maps to existing:** Related to procedural guidance but security-specific
- **Effectiveness:** Systematic security implementation workflow
- **Novelty:** NEW - **DS-122: Security Checklist Response Protocol**

### Technique 8: Defense-in-Depth Behavioral Integration
- **Category:** DS (Domain-Specific) - NEW
- **Pattern:** Defense-in-depth security philosophy embedded as behavioral trait
- **Example from resource:**
  ```markdown
  ## Behavioral Traits
  - Implements defense-in-depth with multiple security layers
  - Applies principle of least privilege to all access controls
  - Uses secure defaults and fails securely in error conditions
  ```
- **Maps to existing:** New security architecture pattern as behavior
- **Effectiveness:** Multi-layered security automatically applied
- **Novelty:** NEW - **DS-123: Defense-in-Depth Behavioral Integration**

### Technique 9: Privacy-Security Unified Integration
- **Category:** DS (Domain-Specific) - NEW
- **Pattern:** Privacy and security treated as unified concern rather than separate domains
- **Example from resource:**
  ```markdown
  ### Privacy and Compliance
  - **Data privacy**: GDPR compliance, CCPA compliance, data minimization
  - **Location privacy**: Location data protection, precise location limiting
  - **Biometric data**: Biometric template protection, privacy-preserving authentication
  - **Personal data handling**: PII protection, data encryption, access logging
  ```
- **Maps to existing:** New privacy-security integration pattern
- **Effectiveness:** Comprehensive data protection strategy
- **Novelty:** NEW - **DS-124: Privacy-Security Unified Integration**

### Technique 10: Context-Aware Security Encoding
- **Category:** DS (Domain-Specific) - NEW
- **Pattern:** Security encoding/sanitization that adapts to output context
- **Example from resource:**
  - Backend: "Context-aware encoding, preventing injection in templates and APIs"
  - Frontend: "Context-aware encoding: HTML entity encoding, JavaScript string escaping, URL encoding"
  - Mobile: "Context-aware encoding for mobile UI, WebView content encoding"
- **Maps to existing:** New security output handling pattern
- **Effectiveness:** Prevents injection attacks across different output contexts
- **Novelty:** NEW - **DS-125: Context-Aware Security Encoding**

### Technique 11: Security Domain Capability Organization
- **Category:** OT (Output Techniques) - NEW
- **Pattern:** Capabilities organized by security domain rather than generic functionality
- **Example from resource:**
  - Backend: Input Validation → HTTP Security → CSRF → Database → API → Authentication
  - Frontend: XSS Prevention → CSP → Input Validation → Clickjacking → Redirects
  - Mobile: Data Storage → WebView → Network → Authentication → Platform-Specific
- **Maps to existing:** New domain-specific organization pattern
- **Effectiveness:** Security concerns clearly structured and findable
- **Novelty:** NEW - **OT-14: Security Domain Capability Organization**

### Technique 12: Security Scenario Example Interactions
- **Category:** OT (Output Techniques) - NEW
- **Pattern:** Example interactions are specific security implementation scenarios
- **Example from resource:**
  ```markdown
  ## Example Interactions
  - "Implement secure user authentication with JWT and refresh token rotation"
  - "Configure CSRF protection for cookie-based authentication system"
  - "Set up certificate pinning for API communication security"
  ```
- **Maps to existing:** New security-focused example pattern
- **Effectiveness:** Concrete security implementation guidance
- **Novelty:** NEW - **OT-15: Security Scenario Examples**

---

## Novel Patterns (Not in MASTER_TECHNIQUE_INDEX)

### Pattern 1: Contrastive Multi-Agent Role Definition
- **Description:** Explicit disambiguation between similar agents using contrastive role statements
- **Implementation:**
  - Define what THIS agent does ("Use this agent for:")
  - Define what SIMILAR agent does ("Use [other-agent] for:")
  - Explicit statement of key difference between agents
  - Prevents role confusion in multi-agent workflows
- **Use case:** Multi-agent systems with overlapping expertise domains
- **Proposed category:** AG (Agentic)
- **Proposed code:** AG-31
- **Pattern template:**
  ```markdown
  ## When to Use vs [Similar Agent Name]
  - **Use this agent for**: [Specific responsibilities and use cases]
  - **Use [other-agent] for**: [Other agent's responsibilities]
  - **Key difference**: [Core distinguishing factor]
  ```

### Pattern 2: Security-First Behavioral Defaults
- **Description:** Security practices embedded as automatic behavioral defaults rather than guidelines
- **Implementation:**
  - Identify critical security practices (input validation, secure defaults, etc.)
  - Define them as behavioral traits that apply to ALL responses
  - Make them DEFAULT behaviors, not conditional recommendations
  - Examples:
    - "Validates and sanitizes all user inputs using allowlist approaches"
    - "Always prefers textContent over innerHTML for dynamic content"
    - "Enforces HTTPS-only communication with certificate pinning"
- **Use case:** Security-critical coding agents, compliance-focused systems
- **Proposed category:** DS (Domain-Specific)
- **Proposed code:** DS-118
- **Pattern template:**
  ```markdown
  ## Behavioral Traits
  - [Security practice 1] always applied by default
  - [Security practice 2] automatic in all implementations
  - [Security practice 3] enforced unless explicitly overridden
  - [Defense strategy] integrated into all responses
  ```

### Pattern 3: Allowlist-First Security Philosophy
- **Description:** Consistent preference for allowlist/whitelist approaches over blocklist approaches
- **Implementation:**
  - Apply allowlist thinking to input validation
  - Apply allowlist thinking to URL validation
  - Apply allowlist thinking to API access
  - Apply allowlist thinking to resource access
  - Document allowlist as meta-security pattern
- **Use case:** Input validation, API security, access control, resource protection
- **Proposed category:** DS (Domain-Specific)
- **Proposed code:** DS-119
- **Pattern template:**
  ```markdown
  ### [Security Domain]
  - **Allowlist approach**: Define allowed values/patterns explicitly
  - **Validation**: Accept only known-good inputs, reject everything else
  - **Default deny**: Block by default, permit only allowlisted items
  ```

### Pattern 4: Environment-Adaptive Security Configuration
- **Description:** Security configurations that change based on deployment environment
- **Implementation:**
  - Identify security controls that should vary by environment
  - Define dev environment security (relaxed for development workflow)
  - Define staging environment security (production-like)
  - Define production environment security (maximum protection)
  - Document when to enable/disable specific controls
- **Use case:** Development workflow balance, staged deployment, compliance requirements
- **Proposed category:** DS (Domain-Specific)
- **Proposed code:** DS-120
- **Pattern template:**
  ```markdown
  ### [Security Control] Configuration
  - **Development**: [Relaxed configuration for dev workflow]
  - **Staging**: [Production-like configuration for testing]
  - **Production**: [Maximum security configuration]
  - **Rationale**: [Why environment-specific configuration needed]
  ```

### Pattern 5: Platform-Native Security Integration
- **Description:** Security implementations that leverage platform-specific native security features
- **Implementation:**
  - Identify target platforms (iOS, Android, Web, etc.)
  - Document platform-native security APIs and features
  - Provide platform-specific implementation guidance
  - Handle cross-platform security patterns
  - Map security requirements to platform capabilities
- **Use case:** Mobile development, cross-platform apps, platform-optimized security
- **Proposed category:** DS (Domain-Specific)
- **Proposed code:** DS-121
- **Pattern template:**
  ```markdown
  ### Platform-Specific Security
  - **[Platform 1]**: [Native security features and APIs]
  - **[Platform 2]**: [Native security features and APIs]
  - **Cross-platform**: [Unified patterns across platforms]
  - **Integration**: [How to leverage platform-native security]
  ```

### Pattern 6: Security Implementation Checklist Protocol
- **Description:** Structured security implementation workflow as numbered checklist
- **Implementation:**
  - Define security implementation steps in order
  - Include assessment, configuration, validation, testing phases
  - Make checklist comprehensive and actionable
  - Ensure checklist covers full security lifecycle
  - Include verification steps for each phase
- **Use case:** Security implementation, compliance verification, code reviews
- **Proposed category:** DS (Domain-Specific)
- **Proposed code:** DS-122
- **Pattern template:**
  ```markdown
  ## Response Approach
  1. **Assess [security aspect]** with [specific criteria]
  2. **Implement [security control]** using [specific technique]
  3. **Configure [security feature]** with [specific settings]
  4. **Validate [security implementation]** through [specific tests]
  5. **Monitor [security metrics]** for [specific indicators]
  ...
  9. **Review and test** with comprehensive validation
  ```

### Pattern 7: Defense-in-Depth as Agent Behavior
- **Description:** Multi-layered security philosophy embedded as core behavioral trait
- **Implementation:**
  - Define defense-in-depth as automatic behavior
  - Apply multiple security layers to all implementations
  - Never rely on single security control
  - Document layered security approach
  - Examples: Input validation + parameterized queries + access control
- **Use case:** High-security systems, compliance requirements, critical applications
- **Proposed category:** DS (Domain-Specific)
- **Proposed code:** DS-123
- **Pattern template:**
  ```markdown
  ## Behavioral Traits
  - Implements defense-in-depth with multiple security layers
  - Never relies on single security control for protection
  - Applies [layer 1], [layer 2], and [layer 3] security
  - Validates at input, processing, and output stages
  ```

### Pattern 8: Privacy-as-Security Integration
- **Description:** Privacy and security treated as unified concern rather than separate domains
- **Implementation:**
  - Integrate privacy requirements into security capabilities
  - Include GDPR, CCPA, data minimization in security planning
  - Treat PII protection as security requirement
  - Document privacy-preserving security patterns
  - Unified privacy-security checklist
- **Use case:** Regulated industries, consumer applications, data-sensitive systems
- **Proposed category:** DS (Domain-Specific)
- **Proposed code:** DS-124
- **Pattern template:**
  ```markdown
  ### Privacy and Security Integration
  - **Data privacy**: [Regulatory compliance requirements]
  - **PII protection**: [Security measures for personal data]
  - **Privacy-preserving**: [Privacy-first security patterns]
  - **Compliance**: [Privacy regulations as security requirements]
  ```

### Pattern 9: Context-Adaptive Security Encoding
- **Description:** Security encoding/sanitization strategies that adapt to output context
- **Implementation:**
  - Identify output contexts (HTML, JavaScript, URL, SQL, etc.)
  - Define context-specific encoding strategies
  - Apply appropriate encoding based on output destination
  - Document context-encoding mapping
  - Prevent injection attacks through context-aware encoding
- **Use case:** XSS prevention, injection attack prevention, output security
- **Proposed category:** DS (Domain-Specific)
- **Proposed code:** DS-125
- **Pattern template:**
  ```markdown
  ### Context-Aware Encoding
  - **HTML context**: [HTML entity encoding]
  - **JavaScript context**: [JavaScript string escaping]
  - **URL context**: [URL encoding]
  - **SQL context**: [Parameterized queries]
  - **Output validation**: [Context-appropriate sanitization]
  ```

### Pattern 10: Security Domain Taxonomy
- **Description:** Capability organization structured by security domain rather than generic features
- **Implementation:**
  - Organize by security concerns (Input Validation, Authentication, etc.)
  - Group related security capabilities together
  - Create clear security domain boundaries
  - Enable quick navigation to security topics
  - Structure: Domain → Capabilities → Specific Techniques
- **Use case:** Security documentation, agent capability organization, security reviews
- **Proposed category:** OT (Output Techniques)
- **Proposed code:** OT-14
- **Pattern template:**
  ```markdown
  ## Capabilities

  ### [Security Domain 1]
  - [Specific capability A]
  - [Specific capability B]

  ### [Security Domain 2]
  - [Specific capability C]
  - [Specific capability D]
  ```

### Pattern 11: Security Scenario Examples
- **Description:** Example interactions framed as specific security implementation scenarios
- **Implementation:**
  - Create examples focused on security use cases
  - Include specific security technologies and patterns
  - Make examples actionable and concrete
  - Cover common security implementation scenarios
  - Example format: "Implement [security feature] with [specific technique/technology]"
- **Use case:** Security training, implementation guidance, code review examples
- **Proposed category:** OT (Output Techniques)
- **Proposed code:** OT-15
- **Pattern template:**
  ```markdown
  ## Example Interactions
  - "Implement [security feature] with [specific technique]"
  - "Configure [security control] for [specific threat model]"
  - "Set up [security mechanism] with [specific technology]"
  ```

---

## Multi-Technique Combinations

The security-coder agents demonstrate sophisticated security technique orchestration:

### Combination 1: Contrastive Role + Security Defaults
- **AG-31** (Contrastive Role Disambiguation) + **DS-118** (Security-Default Behavioral Traits)
- Clear agent selection combined with automatic security-first implementation
- Ensures right agent used with right security practices

### Combination 2: Allowlist Strategy + Context-Aware Encoding
- **DS-119** (Allowlist-First Strategy) + **DS-125** (Context-Aware Security Encoding)
- Input validation through allowlists combined with output encoding by context
- Comprehensive injection attack prevention

### Combination 3: Platform-Adaptive + Privacy-Security Integration
- **DS-121** (Platform-Adaptive Security) + **DS-124** (Privacy-Security Integration)
- Platform-native security features combined with privacy compliance
- Mobile-specific privacy-preserving security

### Combination 4: Environment-Adaptive + Defense-in-Depth
- **DS-120** (Environment-Adaptive Security) + **DS-123** (Defense-in-Depth)
- Environment-specific security layers combined with multi-layered defense
- Balanced security across development lifecycle

### Combination 5: Security Checklist + Security Domain Organization
- **DS-122** (Security Checklist Protocol) + **OT-14** (Security Domain Taxonomy)
- Structured implementation workflow combined with organized security capabilities
- Systematic security implementation guidance

---

## Integration Notes

### How this analysis should influence existing documentation:

1. **MASTER_TECHNIQUE_INDEX.md Updates:**
   - Add **AG-31**: Contrastive Role Disambiguation
   - Add **DS-118**: Security-Default Behavioral Traits
   - Add **DS-119**: Allowlist-First Security Strategy
   - Add **DS-120**: Environment-Adaptive Security Policy
   - Add **DS-121**: Platform-Adaptive Security Implementation
   - Add **DS-122**: Security Checklist Response Protocol
   - Add **DS-123**: Defense-in-Depth Behavioral Integration
   - Add **DS-124**: Privacy-Security Unified Integration
   - Add **DS-125**: Context-Aware Security Encoding
   - Add **OT-14**: Security Domain Capability Organization
   - Add **OT-15**: Security Scenario Examples

2. **USE_CASE_LOOKUP.md Updates:**
   - Add "Security Implementation" use case section
   - Add "Secure Coding" pattern with technique combinations
   - Add "Multi-Agent Security" pattern for agent coordination
   - Add "Platform-Specific Security" pattern

3. **AI_AGENT_QUICK_START.md Updates:**
   - Add section on security-first agent design
   - Add guidance on contrastive role disambiguation
   - Add examples of security-default behavioral traits
   - Add allowlist-first strategy examples

4. **New Documentation Files:**
   - Create detailed technique documentation for each novel pattern (11 new files)
   - Create secure coding agent design guide
   - Create security-first prompting patterns guide

---

## Key Insights

### What makes these agents exceptional:

1. **Contrastive Clarity:** Explicit disambiguation from similar agents prevents confusion
2. **Security by Default:** Security practices are automatic behaviors, not recommendations
3. **Allowlist Philosophy:** Consistent allowlist-first approach across all validation
4. **Environment Awareness:** Security adapts to development vs production contexts
5. **Platform Integration:** Native platform security features properly leveraged
6. **Privacy-Security Unity:** Privacy treated as integral part of security, not separate
7. **Defense-in-Depth:** Multi-layered security automatically applied
8. **Context Adaptation:** Security encoding adapts to output context
9. **Structured Implementation:** Security checklist ensures comprehensive coverage
10. **Domain Organization:** Security capabilities clearly organized by security domain

### Novel contributions to prompting knowledge:

- **Contrastive Role Definition:** Multi-agent coordination through explicit role contrast
- **Security-Default Behaviors:** Security practices as automatic behaviors vs guidelines
- **Allowlist Meta-Pattern:** Allowlist-first as overarching security philosophy
- **Environment-Adaptive Security:** Security policy varies by deployment environment
- **Platform-Native Security:** Platform-specific security feature integration
- **Privacy-Security Fusion:** Unified privacy-security concern handling
- **Security Checklists:** Structured security implementation protocols

---

## Comparison with C4 Architecture Agents

### Similarities to C4 Findings:
- External methodology grounding (C4 Model vs OWASP/MASVS)
- Domain-specific capability organization
- Template-driven structured outputs
- Multi-agent workflow coordination

### Unique Security Contributions:
- **Contrastive role definition** (vs positional workflow definition in C4)
- **Security-default behaviors** (vs documentation-focused behaviors)
- **Allowlist-first philosophy** (vs progressive abstraction)
- **Environment-aware security** (vs abstraction-level awareness)
- **Privacy-security integration** (vs stakeholder targeting)

---

## Cross-Platform Security Matrix

The three agents form a comprehensive security coverage matrix:

| Security Domain | Backend | Frontend | Mobile |
|-----------------|---------|----------|--------|
| Input Validation | Allowlist, sanitization | DOM security, XSS prevention | Touch input, gesture validation |
| Authentication | JWT, OAuth, MFA | Token storage, session mgmt | Biometric, device binding |
| Data Protection | Database encryption, secrets | Local storage security | Keychain/Keystore, backup |
| Network Security | API security, rate limiting | HTTPS, CORS | Certificate pinning, TLS |
| Injection Prevention | SQL, NoSQL, command | XSS, script injection | WebView, deep link |
| Output Security | Context encoding, templates | CSP, sanitization | WebView content, UI encoding |
| Privacy Compliance | GDPR backend requirements | Cookie consent, tracking | GDPR, CCPA mobile requirements |

---

## Summary

The security-coder agents represent a **sophisticated platform-specific security implementation system** that demonstrates 11 novel techniques beyond the 251 already identified. Key innovations include:

- **AG-31**: Contrastive multi-agent role disambiguation
- **DS-118 through DS-125**: 8 new security-specific patterns (security defaults, allowlist strategy, environment-adaptive, platform-adaptive, security checklists, defense-in-depth, privacy-security integration, context-aware encoding)
- **OT-14 and OT-15**: 2 new security-focused output techniques

These agents show that security-first coding agents require fundamentally different prompting patterns than general-purpose coding agents. The security-coder agents prove that domain-specific security expertise can be systematically encoded through behavioral defaults, contrastive role definition, and security-first organizational patterns.

**Recommendation:** These techniques should be integrated into MASTER_TECHNIQUE_INDEX.md as they provide valuable patterns for security implementation, secure coding practices, and multi-agent security coordination.

---

**Analysis Complete**
**Novel Techniques Found:** 11
**Existing Techniques Used:** 1 (DS-111 variation)
**Total Techniques Identified:** 12
**Complexity Rating:** 5/5
