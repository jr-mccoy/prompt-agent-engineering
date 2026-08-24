---
title: "HIPAA Compliance for Software Teams"
category: code-analysis/security
description: "Technical HIPAA compliance analysis for software engineering teams covering PHI handling, ePHI safeguards, audit logging, BAA requirements, minimum necessary standard, and breach notification"
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
  - hipaa
  - healthcare
  - phi
  - ephi
  - audit-logging
  - baa
  - encryption
updated: "2026-03-19"
---

# HIPAA Compliance for Software Teams

**Objective:** Perform a detailed technical HIPAA compliance assessment of the codebase and infrastructure, focusing on Protected Health Information (PHI) handling, electronic PHI (ePHI) safeguards, audit logging, Business Associate Agreement (BAA) requirements, the minimum necessary standard, and breach notification capabilities.

**Instructions:**

1. **Identify and classify all PHI in the system:**

   **A. PHI Inventory (18 HIPAA Identifiers)**
   Map every occurrence of these identifiers in the codebase, database schemas, logs, and third-party integrations:
   - [ ] Names
   - [ ] Geographic data smaller than a state
   - [ ] Dates (birth, admission, discharge, death) except year
   - [ ] Phone numbers
   - [ ] Fax numbers
   - [ ] Email addresses
   - [ ] Social Security numbers
   - [ ] Medical record numbers
   - [ ] Health plan beneficiary numbers
   - [ ] Account numbers
   - [ ] Certificate/license numbers
   - [ ] Vehicle identifiers and serial numbers
   - [ ] Device identifiers and serial numbers
   - [ ] Web URLs
   - [ ] IP addresses
   - [ ] Biometric identifiers
   - [ ] Full-face photographs
   - [ ] Any other unique identifying number or code

   **B. PHI Data Flow Mapping**
   - Document every path PHI takes: input → processing → storage → transmission → output
   - Identify all systems, services, and databases that touch PHI
   - Map PHI exposure in logs, error messages, debug output, and analytics
   - Identify all third parties receiving PHI

2. **Assess Technical Safeguards (§164.312):**

   **A. Access Control (§164.312(a)(1))**
   - [ ] Unique user identification: Every user has unique credentials
   - [ ] Emergency access procedures: Documented break-glass process
   - [ ] Automatic logoff: Session timeout after inactivity (recommended: 15 minutes for clinical, 30 minutes for administrative)
   - [ ] Encryption and decryption: ePHI encrypted at rest using AES-256 or equivalent

   ```
   Access control verification checklist:
   - Role-based access control (RBAC) implemented
   - PHI access limited to minimum necessary roles
   - No shared accounts or credentials
   - Service accounts have restricted PHI access
   - API endpoints serving PHI require authentication + authorization
   - PHI queries filtered by user's authorized scope
   ```

   **B. Audit Controls (§164.312(b))**
   - [ ] All PHI access events logged: who, what, when, where, how
   - [ ] Audit logs include: user ID, timestamp, action, resource accessed, patient ID (or record reference), success/failure
   - [ ] Logs are tamper-evident (append-only, signed, or write-once storage)
   - [ ] Log retention meets requirements (minimum 6 years recommended)
   - [ ] Regular audit log review process in place
   - [ ] Alerts for anomalous PHI access patterns

   ```
   Example audit log entry structure:
   {
     "event_id": "uuid",
     "timestamp": "ISO-8601",
     "user_id": "authenticated_user",
     "user_role": "clinician",
     "action": "READ",
     "resource_type": "patient_record",
     "resource_id": "record_id",
     "patient_id": "patient_id",
     "ip_address": "source_ip",
     "result": "SUCCESS",
     "phi_fields_accessed": ["diagnosis", "medications"],
     "reason": "treatment"
   }
   ```

   **C. Integrity Controls (§164.312(c)(1))**
   - [ ] Mechanisms to verify ePHI has not been improperly altered
   - [ ] Checksums or digital signatures on PHI records
   - [ ] Database integrity constraints on PHI fields
   - [ ] Version history for PHI modifications

   **D. Transmission Security (§164.312(e)(1))**
   - [ ] TLS 1.2+ for all ePHI in transit
   - [ ] Certificate validation enforced (no certificate pinning bypasses in production)
   - [ ] ePHI in API responses uses encrypted channels only
   - [ ] Email containing ePHI is encrypted (S/MIME, PGP, or secure portal)
   - [ ] HL7/FHIR interfaces use encrypted transport

3. **Assess Administrative Safeguards (§164.308):**

   **A. Security Management Process**
   - [ ] Risk analysis conducted and documented
   - [ ] Risk management plan implemented
   - [ ] Sanction policy for workforce violations
   - [ ] Information system activity review process

   **B. Workforce Security**
   - [ ] Authorization procedures for PHI access
   - [ ] Workforce clearance procedures
   - [ ] Termination procedures (immediate access revocation)

   **C. Information Access Management**
   - [ ] Access authorization policies
   - [ ] Access establishment and modification procedures
   - [ ] Principle of least privilege enforced
   - [ ] Regular access reviews (quarterly recommended)

   **D. Security Incident Procedures**
   - [ ] Incident identification and response process
   - [ ] Incident documentation requirements
   - [ ] Escalation procedures

   **E. Contingency Plan**
   - [ ] Data backup plan (with encryption of backup media)
   - [ ] Disaster recovery plan
   - [ ] Emergency mode operation plan
   - [ ] Testing and revision procedures
   - [ ] Applications and data criticality analysis

4. **Evaluate minimum necessary standard (§164.502(b)):**
   - [ ] Each PHI access point returns only the minimum data needed for the purpose
   - [ ] API responses don't include unnecessary PHI fields
   - [ ] Database queries are scoped to required PHI elements
   - [ ] Role-based data filtering: different roles see different PHI subsets
   - [ ] Bulk data operations justify the scope of PHI accessed
   - [ ] Analytics and reporting use de-identified or aggregated data where possible

5. **Assess Business Associate Agreement (BAA) coverage:**
   - [ ] All third-party services that handle PHI identified
   - [ ] BAA in place with each business associate (cloud providers, SaaS tools, APIs)
   - [ ] BAA terms cover: permitted uses, safeguards required, breach notification obligations, subcontractor requirements, return/destruction of PHI at termination
   - [ ] Subcontractor chain of BAAs verified
   - [ ] Common services requiring BAAs checked:
     - Cloud providers (AWS, GCP, Azure)
     - Email services
     - Analytics platforms
     - Error tracking / logging services
     - Communication tools (chat, video)
     - Payment processors
     - Backup and disaster recovery providers

6. **Evaluate de-identification capabilities (§164.514):**
   - [ ] Safe Harbor method: All 18 identifiers removed
   - [ ] Expert Determination method: Statistical verification available
   - [ ] De-identification applied to: analytics, reporting, research datasets, test/staging environments
   - [ ] Re-identification risk assessment performed
   - [ ] De-identified data not combined with other data in ways that enable re-identification

7. **Assess breach notification readiness (§164.400-414):**
   - [ ] Breach detection mechanisms in place
   - [ ] Breach risk assessment process (four-factor test: nature/extent, unauthorized person, whether PHI was actually acquired/viewed, extent of risk mitigation)
   - [ ] Individual notification within 60 days of discovery
   - [ ] HHS notification: without unreasonable delay (>500 individuals: within 60 days; <500: annual log)
   - [ ] Media notification for breaches affecting >500 individuals in a state
   - [ ] Breach log maintained regardless of size
   - [ ] Breach notification templates prepared

**False-Positive Prevention (MUST follow):**
- ❌ Do NOT flag PHI exposure in systems that only handle de-identified data
- ❌ Do NOT assume missing BAAs without checking procurement/legal documentation
- ❌ Do NOT report encryption gaps without verifying infrastructure-level encryption (e.g., AWS RDS encryption, EBS encryption)
- ❌ Do NOT flag test/development environments unless they contain real PHI
- ✅ DO verify whether data that looks like PHI is actually synthetic/test data
- ✅ DO check cloud provider HIPAA compliance configurations (e.g., AWS HIPAA eligible services)
- ✅ DO trace PHI through the complete data lifecycle, including logs and error messages

**Expected Output:**

1. **PHI Inventory:**
   - Complete mapping of PHI identifiers by system component
   - Data flow diagrams showing PHI paths
   - Third-party PHI exposure points

2. **Technical Safeguard Assessment:**
   - Status for each §164.312 requirement (Compliant / Partial / Non-Compliant)
   - Specific code locations where gaps exist
   - Remediation with code examples

3. **Administrative Safeguard Assessment:**
   - Policy and procedure gaps
   - Process improvement recommendations

4. **BAA Coverage Report:**
   - All third-party services handling PHI
   - BAA status for each (Covered / Missing / Needs Update)
   - Risk assessment for uncovered services

5. **Compliance Gap Report:**
   For each gap:
   - HIPAA section reference (e.g., §164.312(b))
   - Gap description with affected code/system
   - Risk severity (Critical/High/Medium/Low)
   - Specific remediation steps
   - Implementation effort estimate

6. **Remediation Roadmap:**
   - Phase 1 (0-30 days): Critical ePHI exposure, missing encryption, PHI in logs
   - Phase 2 (1-3 months): Audit logging, access controls, BAA gaps
   - Phase 3 (3-6 months): Full minimum necessary enforcement, de-identification, breach response testing

**Related Prompts:**
- security_compliance_analysis.md - Broad multi-framework compliance overview
- security_gdpr_implementation_guide.md - GDPR compliance (overlapping data protection concepts)
- security_audit_trail_design.md - Audit logging patterns for PHI access
- security_cryptography_encryption_review.md - Encryption implementation review

**When to Use:**
Use this prompt when building or auditing healthcare software, health-tech applications, systems handling PHI, preparing for HIPAA audits, onboarding new third-party services in healthcare contexts, or conducting risk analyses required under the HIPAA Security Rule.

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Specific HIPAA technical compliance focus
- ST-02 (Structured Sequential Instructions) - Organized by HIPAA rule sections
- RT-02 (Multi-Dimensional Analysis Framework) - Technical, administrative, BAA, and breach dimensions
- RT-05 (Evidence-Based Reasoning) - Requires tracing actual PHI flows and code paths
- DS-06 (Prioritization and Severity Guidance) - Phased remediation roadmap
- CM-02 (Constraint Specification) - False-positive prevention for healthcare contexts
