---
title: "Privacy-by-Design Architecture Patterns"
category: code-analysis/security
description: "Privacy-by-design architecture assessment covering data minimization, purpose limitation, consent-driven data flows, pseudonymization, privacy-preserving analytics, and privacy engineering patterns for software systems"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
  - CM-02
difficulty: advanced
tags:
  - compliance
  - privacy
  - privacy-by-design
  - data-minimization
  - pseudonymization
  - anonymization
  - architecture
  - gdpr
updated: "2026-03-19"
---

# Privacy-by-Design Architecture Patterns

**Objective:** Assess the system architecture for privacy-by-design and privacy-by-default implementation, evaluating data minimization, purpose limitation, consent-driven data flows, pseudonymization/anonymization, privacy-preserving computation, and structural privacy patterns, with actionable recommendations for embedding privacy into the system's core design.

**Context:**
- Privacy-by-design is a legal requirement under GDPR Article 25 and a best practice across all privacy regulations
- The 7 foundational principles (Ann Cavoukian): Proactive, Default, Embedded, Full Functionality, End-to-End Security, Visibility/Transparency, Respect for User Privacy
- Privacy architecture decisions made early are 10-100x cheaper than retrofitting

**Instructions:**

1. **Assess data minimization architecture:**

   **A. Collection Minimization**
   - [ ] Each data field collected has a documented purpose
   - [ ] No "nice to have" fields without active use
   - [ ] Forms collect only required fields (optional fields justified)
   - [ ] API request payloads don't require unnecessary personal data
   - [ ] Third-party SDKs/libraries reviewed for hidden data collection
   - [ ] Analytics events don't contain unnecessary identifiers

   **B. Processing Minimization**
   - [ ] Personal data processed only for stated purposes
   - [ ] Derived data (scores, classifications) used instead of raw personal data where possible
   - [ ] Batch processing operates on aggregated/anonymized data when individual records aren't needed
   - [ ] Machine learning models trained on minimized or synthetic datasets

   **C. Storage Minimization**
   - [ ] Retention policies enforced automatically (TTL, scheduled cleanup jobs)
   - [ ] Different retention periods for different data categories
   - [ ] Temporary data (session, cache) has aggressive expiration
   - [ ] Backups follow retention policies (not indefinite)
   - [ ] Test/staging environments use synthetic data, not production copies

   ```
   Data minimization assessment template:
   | Data Field | Purpose | Collected By | Stored In | Retention | Minimization Opportunity |
   |---|---|---|---|---|---|
   | Full name | Account display | Registration | users table | Account lifetime | Could use display name only |
   | IP address | Fraud detection | All requests | logs | 90 days | Could hash after 7 days |
   | DOB | Age verification | Registration | users table | Account lifetime | Could store age bracket only |
   ```

2. **Evaluate purpose limitation architecture:**

   **A. Purpose Binding**
   - [ ] Data collection tied to specific, documented purposes
   - [ ] Purpose tracked in data model (metadata linking data to processing purpose)
   - [ ] Purpose checks enforced at access time (not just policy)
   - [ ] Secondary use requires additional consent or compatible purpose assessment
   - [ ] Marketing use of transactional data requires separate consent

   **B. Purpose Separation**
   - [ ] Data silos by purpose (operational vs. analytics vs. marketing)
   - [ ] Database views or access policies scoped by purpose
   - [ ] API endpoints organized by data purpose (service-oriented privacy)
   - [ ] Cross-purpose data joining requires explicit authorization

   ```
   Purpose limitation architecture pattern:

   [User Data Store] ──purpose: "service"──→ [Service Layer]
          │
          ├──purpose: "analytics"──→ [Analytics Pipeline] (pseudonymized)
          │
          └──purpose: "marketing"──→ [Marketing System] (consent-gated)

   Each purpose boundary enforces:
   - Consent verification
   - Data field filtering (minimum necessary)
   - Access logging
   ```

3. **Assess consent-driven data flow architecture:**

   **A. Consent as a First-Class Architectural Concept**
   - [ ] Consent state stored separately from user profile
   - [ ] Consent checks integrated into data access layer (middleware, interceptors)
   - [ ] Data flows gated by real-time consent state (not cached/stale consent)
   - [ ] Consent changes propagate to all downstream systems immediately
   - [ ] Default state is "no consent" (privacy by default)

   **B. Consent Propagation**
   - [ ] Consent state available to all services that process personal data
   - [ ] Event-driven consent updates (consent change → event → downstream enforcement)
   - [ ] Third-party data sharing gated by consent
   - [ ] Consent withdrawal triggers data flow cessation (not just flagging)

   **C. Granular Consent**
   - [ ] Per-purpose consent granularity
   - [ ] Per-channel consent (email, push, SMS, in-app)
   - [ ] Third-party-specific consent (which partners receive data)
   - [ ] Consent version tracking (what exactly was consented to)

4. **Evaluate pseudonymization and anonymization:**

   **A. Pseudonymization Patterns**
   - [ ] Pseudonymization applied at collection or ingestion
   - [ ] Pseudonymous identifiers used for processing (replacing direct identifiers)
   - [ ] Re-identification key stored separately with strict access controls
   - [ ] Pseudonymization resistant to rainbow table attacks (keyed hashing, encryption)
   - [ ] Appropriate technique selected:
     - Tokenization (reversible, for operational use)
     - Keyed hashing (one-way, for analytics linkage)
     - Encryption (reversible with key, for storage)
     - Key-coded references (lookup table, for cross-system linkage)

   **B. Anonymization Assessment**
   - [ ] k-anonymity achieved for published datasets (k ≥ 5 recommended)
   - [ ] l-diversity for sensitive attributes
   - [ ] t-closeness for distribution similarity
   - [ ] Re-identification risk assessment performed
   - [ ] Techniques applied: generalization, suppression, noise addition, aggregation
   - [ ] Anonymized data verified as irreversibly de-identified

   **C. Privacy-Preserving Analytics**
   - [ ] Aggregation applied before personal data leaves secure boundary
   - [ ] Differential privacy implemented for statistical queries (ε budget managed)
   - [ ] Federated learning considered for ML use cases (model goes to data, not data to model)
   - [ ] Secure multi-party computation evaluated for cross-organization analytics
   - [ ] Homomorphic encryption assessed for computation on encrypted data (if applicable)

5. **Assess architectural privacy patterns:**

   **A. Data Separation Patterns**
   - [ ] Identifier separation: personal identifiers stored separately from behavioral/transactional data
   - [ ] Encryption separation: different keys for different data categories
   - [ ] Service separation: privacy-sensitive services isolated from general services
   - [ ] Network separation: PII processing in isolated network segments

   **B. Data Flow Patterns**
   - [ ] Privacy proxy: intermediary that strips/pseudonymizes PII before forwarding
   - [ ] Data minimization gateway: API gateway that filters fields based on purpose/consent
   - [ ] Consent-aware message broker: events filtered based on consumer consent state
   - [ ] Privacy-preserving logging: PII stripped or masked in application logs

   **C. Deletion Patterns**
   - [ ] Crypto-shredding: encrypt personal data per-user, delete key to "delete" data
   - [ ] Cascading delete: propagated deletion across all data stores and services
   - [ ] Soft-delete with hard-delete schedule: grace period then permanent removal
   - [ ] Backup exclusion: mechanism to exclude deleted users from future backup restores

   **D. Default Privacy Patterns**
   - [ ] Privacy-protective defaults for all user settings
   - [ ] Opt-in (not opt-out) for data sharing, analytics, marketing
   - [ ] Minimum data exposure in APIs (explicit field selection, not full objects)
   - [ ] No personal data in URLs, referrer headers, or client-side storage without necessity

6. **Evaluate privacy engineering infrastructure:**
   - [ ] Privacy impact assessment (PIA/DPIA) integrated into development lifecycle
   - [ ] Privacy threat modeling conducted (LINDDUN methodology or equivalent)
   - [ ] Privacy-aware testing: test for data leaks, unnecessary logging, over-collection
   - [ ] Data catalog with privacy metadata (classification, owner, purpose, retention)
   - [ ] Privacy monitoring: alerts for unusual data access patterns, bulk exports, new data flows

**False-Positive Prevention (MUST follow):**
- ❌ Do NOT flag all personal data storage as a privacy violation — storage is fine when purpose-justified and minimized
- ❌ Do NOT require anonymization when pseudonymization is appropriate (pseudonymization is often the right balance)
- ❌ Do NOT assume that not using differential privacy is a gap — it's needed for specific use cases, not universally
- ❌ Do NOT flag data collection that serves a clear, documented user benefit as over-collection
- ✅ DO assess whether data collection is proportionate to the purpose (not just whether it exists)
- ✅ DO verify that pseudonymization implementations actually prevent casual re-identification
- ✅ DO check infrastructure-level privacy controls (network segmentation, encryption) before flagging gaps
- ✅ DO consider the full data lifecycle, including logs, caches, CDN, and third-party services

**Expected Output:**

1. **Privacy Architecture Assessment:**
   - Data minimization maturity (scored 1-5 per dimension)
   - Purpose limitation enforcement status
   - Consent architecture evaluation
   - Pseudonymization/anonymization coverage

2. **Data Flow Privacy Map:**
   - Personal data flows annotated with privacy controls at each stage
   - Gaps where personal data flows without adequate privacy controls
   - Third-party data sharing with privacy assessment

3. **Pattern Recommendations:**
   For each recommended pattern:
   - Pattern name and description
   - Where to apply in the current architecture
   - Implementation approach
   - Effort estimate
   - Privacy impact (what risk it mitigates)

4. **Privacy-by-Default Assessment:**
   - Current default settings audit
   - Recommended default changes
   - User-facing privacy control gaps

5. **Remediation Roadmap:**
   - Phase 1 (0-30 days): Privacy-preserving logging, default settings, consent checks
   - Phase 2 (1-3 months): Pseudonymization layer, purpose-based access controls, data minimization
   - Phase 3 (3-6 months): Privacy-preserving analytics, crypto-shredding, automated retention enforcement

**Related Prompts:**
- security_gdpr_implementation_guide.md - GDPR compliance (privacy-by-design is Article 25)
- security_audit_trail_design.md - Privacy-aware audit logging
- security_compliance_analysis.md - Multi-framework compliance overview
- architecture_layer_identification.md - General architecture assessment

**When to Use:**
Use this prompt when designing new systems that handle personal data, retrofitting privacy into existing architectures, preparing for privacy audits (GDPR Article 25), evaluating data architecture for privacy risk, implementing privacy engineering programs, or assessing third-party integrations for privacy impact.

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Privacy architecture assessment focus
- ST-02 (Structured Sequential Instructions) - Organized by privacy engineering dimensions
- RT-02 (Multi-Dimensional Analysis Framework) - Minimization, purpose, consent, pseudonymization, patterns
- RT-05 (Evidence-Based Reasoning) - Requires tracing actual data flows for privacy assessment
- DS-06 (Prioritization and Severity Guidance) - Phased remediation roadmap
- CM-02 (Constraint Specification) - False-positive prevention for privacy assessments
