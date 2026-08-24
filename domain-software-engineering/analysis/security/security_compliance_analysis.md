---
title: "Security Compliance Analysis (GDPR, SOC2, HIPAA, PCI-DSS)"
category: code-analysis
description: "Security Compliance Analysis (GDPR, SOC2, HIPAA, PCI-DSS)"
tags:
  - analysis
  - code-analysis
  - security
updated: "2026-03-19"
---

# Security Compliance Analysis (GDPR, SOC2, HIPAA, PCI-DSS)

**Objective:** Analyze the codebase for compliance with major security and privacy regulations including GDPR, SOC2, HIPAA, and PCI-DSS to identify gaps, ensure regulatory adherence, and mitigate legal and financial risks.

**Instructions:**

1. **Determine applicable compliance frameworks:**
   - GDPR: Handling EU citizen data
   - SOC2: Cloud services, SaaS applications
   - HIPAA: Healthcare information (Protected Health Information - PHI)
   - PCI-DSS: Payment card processing and storage

2. **GDPR (General Data Protection Regulation) Compliance Analysis:**

   **A. Lawful Basis and Consent**
   - [ ] Review consent collection mechanisms
   - [ ] Verify explicit consent for data processing
   - [ ] Check consent withdrawal functionality
   - [ ] Analyze consent storage and audit trail
   - [ ] Verify age verification for minors (< 16 years)
   - [ ] Review data processing purposes documented

   **B. Data Subject Rights Implementation**

   - [ ] **Right to Access (Article 15):**
     - User can request all their personal data
     - Data export functionality available
     - Response within 30 days capability

   - [ ] **Right to Rectification (Article 16):**
     - Users can update their personal data
     - Data correction propagates to all systems

   - [ ] **Right to Erasure/"Right to be Forgotten" (Article 17):**
     - User data deletion functionality
     - Deletion includes backups and archives
     - Retention only for legal requirements
     - Deletion audit logging

   - [ ] **Right to Data Portability (Article 20):**
     - Data export in machine-readable format (JSON, CSV, XML)
     - Includes all user-provided and system-generated data
     - Easy transfer to another controller

   - [ ] **Right to Object (Article 21):**
     - Users can object to data processing
     - Automated decision-making opt-out
     - Marketing communication opt-out

   **C. Privacy by Design and Default**
   - [ ] Data minimization implemented
   - [ ] Purpose limitation enforced
   - [ ] Storage limitation policies
   - [ ] Default privacy-friendly settings
   - [ ] Pseudonymization or anonymization where applicable
   - [ ] Privacy impact assessment conducted

   **D. Data Protection and Security**
   - [ ] Encryption of personal data at rest
   - [ ] Encryption of personal data in transit (TLS 1.2+)
   - [ ] Access controls on personal data
   - [ ] Data breach detection mechanisms
   - [ ] Breach notification capability (within 72 hours)
   - [ ] Regular security testing and audits

   **E. International Data Transfers**
   - [ ] Data transfer mechanisms documented
   - [ ] Standard Contractual Clauses (SCCs) implemented
   - [ ] Data processing agreements (DPAs) with third parties
   - [ ] Data localization requirements met

   **F. Documentation and Accountability**
   - [ ] Privacy policy accessible and clear
   - [ ] Data processing records maintained
   - [ ] Data retention policies documented
   - [ ] DPO (Data Protection Officer) contact available
   - [ ] Vendor/processor agreements compliant

3. **SOC2 (Service Organization Control 2) Compliance Analysis:**

   **Trust Service Criteria:**

   **A. Security (Common Criteria)**
   - [ ] Access controls based on least privilege
   - [ ] Logical and physical access restrictions
   - [ ] Multi-factor authentication for sensitive access
   - [ ] Encryption of sensitive data
   - [ ] Network security controls (firewalls, IDS/IPS)
   - [ ] System monitoring and logging
   - [ ] Vulnerability management program
   - [ ] Incident response procedures
   - [ ] Security awareness training

   **B. Availability**
   - [ ] System availability monitoring
   - [ ] Capacity planning and resource management
   - [ ] Disaster recovery plan
   - [ ] Business continuity planning
   - [ ] Redundancy and failover mechanisms
   - [ ] Performance monitoring
   - [ ] Backup and restoration procedures

   **C. Processing Integrity**
   - [ ] Data processing completeness validation
   - [ ] Data processing accuracy validation
   - [ ] Authorization for transactions
   - [ ] Error detection and correction
   - [ ] Input validation
   - [ ] Processing exception handling

   **D. Confidentiality**
   - [ ] Data classification implemented
   - [ ] Confidential data encryption
   - [ ] Secure data transmission
   - [ ] Non-disclosure agreements
   - [ ] Data disposal procedures
   - [ ] Access to confidential data logged

   **E. Privacy (If applicable)**
   - [ ] Privacy notice provided
   - [ ] Choice and consent mechanisms
   - [ ] Data retention and disposal
   - [ ] Access to personal information
   - [ ] Disclosure to third parties controlled

4. **HIPAA (Health Insurance Portability and Accountability Act) Compliance:**

   **A. Technical Safeguards (§164.312)**

   - [ ] **Access Control:**
     - Unique user identification
     - Emergency access procedures
     - Automatic logoff
     - Encryption and decryption of ePHI

   - [ ] **Audit Controls:**
     - Hardware, software, and procedural mechanisms to record and examine activity
     - PHI access logging (who, what, when)
     - Audit log protection from tampering

   - [ ] **Integrity Controls:**
     - Mechanisms to ensure ePHI is not improperly altered or destroyed
     - Electronic data integrity verification

   - [ ] **Transmission Security:**
     - Encryption of ePHI in transit (TLS 1.2+)
     - Integrity controls for transmission

   **B. Administrative Safeguards**
   - [ ] Security management process
   - [ ] Assigned security responsibility
   - [ ] Workforce security procedures
   - [ ] Information access management
   - [ ] Security awareness training
   - [ ] Security incident procedures
   - [ ] Contingency plan
   - [ ] Business associate agreements

   **C. Physical Safeguards**
   - [ ] Facility access controls
   - [ ] Workstation use policies
   - [ ] Workstation security
   - [ ] Device and media controls

   **D. Protected Health Information (PHI) Handling**
   - [ ] Minimum necessary standard
   - [ ] PHI de-identification procedures
   - [ ] Right to access PHI (within 30 days)
   - [ ] Right to amend PHI
   - [ ] Accounting of disclosures
   - [ ] Breach notification procedures (within 60 days)

5. **PCI-DSS (Payment Card Industry Data Security Standard) Compliance:**

   **Requirement 1: Install and Maintain Network Security Controls**
   - [ ] Firewall configuration
   - [ ] Network segmentation (cardholder data environment isolated)
   - [ ] Restriction of inbound and outbound traffic
   - [ ] No direct public access to cardholder data

   **Requirement 2: Apply Secure Configurations**
   - [ ] Change default passwords and security parameters
   - [ ] Remove unnecessary functionality
   - [ ] Strong cryptography for administrative access

   **Requirement 3: Protect Stored Account Data**
   - [ ] Cardholder data retention minimized
   - [ ] Sensitive authentication data not stored after authorization
   - [ ] PAN (Primary Account Number) masked when displayed
   - [ ] PAN rendered unreadable (encryption, truncation, hashing)
   - [ ] Cryptographic keys secured
   - [ ] No full PAN in logs

   **Requirement 4: Protect Cardholder Data with Strong Cryptography**
   - [ ] Strong cryptography during transmission over open, public networks
   - [ ] TLS 1.2 or higher for cardholder data transmission
   - [ ] Trusted keys and certificates
   - [ ] No unencrypted PANs via end-user messaging

   **Requirement 5: Protect Systems and Networks from Malicious Software**
   - [ ] Anti-malware solutions deployed
   - [ ] Anti-malware kept current
   - [ ] Periodic scans performed

   **Requirement 6: Develop and Maintain Secure Systems**
   - [ ] Security patches installed within one month
   - [ ] Secure software development lifecycle
   - [ ] Code reviews for custom code
   - [ ] No web application vulnerabilities (OWASP Top 10)
   - [ ] Change control processes

   **Requirement 7: Restrict Access to System Components**
   - [ ] Access to cardholder data limited by business need-to-know
   - [ ] Least privilege access
   - [ ] Default "deny-all" setting

   **Requirement 8: Identify Users and Authenticate Access**
   - [ ] Unique ID for each user
   - [ ] Strong authentication (MFA for administrative access)
   - [ ] Strong passwords (min 12 characters, complexity)
   - [ ] Account lockout after failed attempts
   - [ ] Session timeout after 15 minutes of inactivity

   **Requirement 9: Restrict Physical Access**
   - [ ] Physical access controls to cardholder data
   - [ ] Media destruction procedures

   **Requirement 10: Log and Monitor Access to Systems**
   - [ ] Audit trails for all access to cardholder data
   - [ ] Logging enabled and retained for 1 year
   - [ ] Logs reviewed daily
   - [ ] Time synchronization (NTP)
   - [ ] Audit logs protected from modification

   **Requirement 11: Test Security Systems and Networks**
   - [ ] Wireless access point inventory
   - [ ] Vulnerability scans quarterly (internal and external)
   - [ ] Penetration testing annually
   - [ ] Intrusion detection/prevention systems
   - [ ] File integrity monitoring

   **Requirement 12: Support Information Security with Policies**
   - [ ] Information security policy
   - [ ] Risk assessment process
   - [ ] Usage policies for technologies
   - [ ] Security awareness program
   - [ ] Incident response plan
   - [ ] Vendor management program

6. **For each compliance gap, provide:**
   - Regulation and specific requirement reference
   - Gap description
   - Non-compliance risk (legal, financial, reputational)
   - Affected code or system component
   - Current implementation status
   - Remediation steps with code examples
   - Implementation priority
   - Estimated effort
   - Responsible parties

**Expected Output:** A comprehensive compliance analysis report including:

- **Executive Summary:**
  - Applicable regulations identified
  - Overall compliance status by framework
  - Critical non-compliance issues
  - Legal and financial risk assessment
  - High-priority remediation items

- **GDPR Compliance Assessment:**
  - Data subject rights implementation status
  - Consent management evaluation
  - Data protection measures
  - International transfer mechanisms
  - Privacy by design assessment
  - Compliance score and gaps
  - Remediation roadmap

- **SOC2 Compliance Assessment:**
  - Trust Service Criteria evaluation
  - Security controls implementation
  - Availability measures
  - Processing integrity
  - Confidentiality protection
  - Privacy controls (if applicable)
  - Control gaps and recommendations

- **HIPAA Compliance Assessment:**
  - Technical safeguards evaluation
  - Administrative safeguards review
  - PHI handling procedures
  - Audit controls assessment
  - Encryption implementation
  - Compliance gaps and remediation

- **PCI-DSS Compliance Assessment:**
  - 12 requirements evaluation
  - Cardholder data protection
  - Encryption implementation
  - Access controls
  - Logging and monitoring
  - Network security
  - Compliance level and gaps

- **Compliance Gap Analysis:**
  For each gap:
  - Regulation and requirement
  - Gap description
  - Non-compliance risks
  - Current vs required state
  - Remediation steps
  - Priority and timeline
  - Estimated cost/effort

- **Remediation Roadmap:**

  **Phase 1: Critical Compliance (0-3 months)**
  - Critical data protection gaps
  - Mandatory security controls
  - Data breach notification capabilities
  - High-risk non-compliance items

  **Phase 2: Core Compliance (3-6 months)**
  - Complete data subject rights
  - Enhanced logging and monitoring
  - Access control improvements
  - Documentation and policies

  **Phase 3: Full Compliance (6-12 months)**
  - Advanced security measures
  - Comprehensive audit capabilities
  - Third-party risk management
  - Continuous compliance monitoring

- **Audit Readiness:**
  - Documentation requirements
  - Evidence collection procedures
  - Audit preparation checklist
  - Third-party assessment readiness

**Example Output Format:**

```
REGULATION: GDPR Article 17 - Right to Erasure
STATUS: NON-COMPLIANT
SEVERITY: HIGH

Gap: Missing User Data Deletion Functionality

Current State:
  - No API endpoint for user data deletion
  - No administrative interface for data erasure
  - Deleted users remain in database (soft delete only)
  - No backup/archive deletion process

Required State:
  - Users must be able to request complete data deletion
  - All personal data erased within 30 days
  - Deletion includes backups and archives
  - Audit trail of deletion requests
  - Exceptions documented (legal hold, contractual obligations)

Affected Components:
  - User API (src/api/users.js)
  - Database schemas (user, profile, orders)
  - Backup systems
  - Logging systems

Non-Compliance Risks:
  - GDPR fines up to €20 million or 4% of annual global turnover
  - Regulatory enforcement actions
  - User complaints to supervisory authorities
  - Reputational damage
  - Loss of user trust

Remediation Steps:

1. Implement data deletion API endpoint:
   ```javascript
   // src/api/users.js
   app.post('/api/users/delete-account', authenticate, async (req, res) => {
     const userId = req.user.id;

     // Log deletion request
     await AuditLog.create({
       userId,
       action: 'account_deletion_requested',
       timestamp: new Date()
     });

     // Schedule deletion (allow for legal review period)
     await DeletionQueue.add({
       userId,
       requestDate: new Date(),
       scheduledDate: new Date(Date.now() + 30 * 24 * 60 * 60 * 1000)
     });

     res.json({ message: 'Deletion scheduled within 30 days' });
   });
   ```

2. Implement hard delete job:
   - Delete from users table
   - Delete from all related tables (profiles, orders, sessions)
   - Remove from search indexes
   - Purge from logs (anonymize or remove)
   - Remove from backups (or mark for exclusion)

3. Create admin dashboard for reviewing deletion requests

4. Document exceptions (legal hold, ongoing investigations)

5. Test deletion process end-to-end

Priority: HIGH
Timeline: 2-3 months
Effort: 3-4 weeks development + testing
Responsible: Engineering team, Legal review
```

**Related Prompts:**
- security_owasp_top_10_analysis.md - Security vulnerability analysis
- security_cryptography_encryption_review.md - Encryption compliance
- security_authentication_authorization_review.md - Access control compliance
- quality_code_documentation_coverage_analysis.md - Documentation requirements

**When to Use:**
Use this prompt when preparing for compliance audits, before handling regulated data (PII, PHI, payment cards), when expanding to new markets (EU for GDPR), for SaaS product launches, during due diligence, or annually to maintain compliance. Essential for avoiding regulatory fines and legal risks.

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Opens with concise, unambiguous objective
- ST-02 (Structured Sequential Instructions) - Organized by compliance framework
- DS-01 (Framework Application) - Applies GDPR, SOC2, HIPAA, PCI-DSS frameworks
- DT-02 (Specific Focus Areas with Examples) - Comprehensive compliance checklists
- RT-02 (Multi-Dimensional Analysis Framework) - Requirement, Gap, Risk, Remediation structure
- DS-06 (Prioritization and Severity Guidance) - Phased remediation roadmap
- ST-03 (Output Format Templates) - Detailed compliance gap output format
- AG-05 (Concrete Deliverable Templates) - Code examples for compliance implementation
