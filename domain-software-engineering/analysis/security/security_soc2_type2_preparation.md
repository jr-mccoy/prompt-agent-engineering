---
title: "SOC 2 Type II Preparation and Evidence Collection"
category: code-analysis/security
description: "Comprehensive SOC 2 Type II audit preparation covering Trust Service Criteria, control design and operating effectiveness, evidence collection, and auditor readiness for SaaS and cloud service organizations"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-06
  - CM-01
  - QA-01
difficulty: advanced
tags:
  - compliance
  - soc2
  - audit
  - trust-services
  - evidence-collection
  - controls
  - saas
updated: "2026-03-19"
---

# SOC 2 Type II Preparation and Evidence Collection

**Objective:** Assess the codebase, infrastructure, and operational processes for SOC 2 Type II readiness, evaluating control design and operating effectiveness across Trust Service Criteria, identifying evidence gaps, and producing an audit preparation plan with specific evidence collection procedures.

**Context:**
- SOC 2 Type I evaluates control **design** at a point in time
- SOC 2 Type II evaluates control **design AND operating effectiveness** over a period (typically 3-12 months)
- Type II requires demonstrating that controls operated consistently throughout the audit period
- Evidence must be systematic, timestamped, and independently verifiable

**Instructions:**

1. **Determine scope and applicable Trust Service Criteria (TSC):**

   Identify which criteria apply to your service:
   - [ ] **Security** (Common Criteria — CC) — Required for all SOC 2 reports
   - [ ] **Availability** — If SLAs or uptime commitments exist
   - [ ] **Processing Integrity** — If data processing accuracy is critical
   - [ ] **Confidentiality** — If handling confidential (non-personal) data
   - [ ] **Privacy** — If collecting/processing personal information

   Document the system boundaries:
   - Infrastructure components in scope
   - Applications and services in scope
   - Data stores in scope
   - Third-party services (sub-service organizations)
   - Personnel and roles in scope

2. **Assess Security controls (Common Criteria — always required):**

   **CC1: Control Environment**
   - [ ] Organizational structure with defined security responsibilities
   - [ ] Board/management oversight of security program
   - [ ] Code of conduct and ethics policies
   - [ ] Evidence: Org charts, job descriptions, policy acknowledgments

   **CC2: Communication and Information**
   - [ ] Internal security communication processes
   - [ ] External communication about security commitments
   - [ ] Incident reporting channels
   - [ ] Evidence: Security newsletters, status pages, incident reports

   **CC3: Risk Assessment**
   - [ ] Formal risk assessment process (annual minimum)
   - [ ] Risk register maintained and updated
   - [ ] Risk mitigation plans tracked to completion
   - [ ] Change-related risk evaluation
   - [ ] Evidence: Risk assessment reports, risk register, mitigation tracking

   **CC4: Monitoring Activities**
   - [ ] Continuous monitoring of control effectiveness
   - [ ] Internal audit or self-assessment program
   - [ ] Deficiency identification and remediation tracking
   - [ ] Evidence: Monitoring dashboards, assessment reports, remediation tickets

   **CC5: Control Activities**
   - [ ] Policies and procedures documented and current
   - [ ] Technology controls selected and deployed
   - [ ] Controls mapped to risks
   - [ ] Evidence: Policy documents with version history, control matrix

   **CC6: Logical and Physical Access Controls**
   - [ ] User provisioning and de-provisioning procedures
   - [ ] Role-based access control (RBAC)
   - [ ] Multi-factor authentication for production access
   - [ ] Quarterly access reviews completed and documented
   - [ ] Physical access controls (data centers, offices)
   - [ ] Evidence: Access review reports, MFA enrollment records, provisioning tickets

   ```
   Access review evidence format:
   - Date of review
   - Reviewer name and role
   - Systems reviewed
   - Users reviewed (total count)
   - Access modifications made (added/removed/unchanged)
   - Exceptions found and remediation actions
   - Sign-off by management
   ```

   **CC7: System Operations**
   - [ ] Change management process (dev → staging → production)
   - [ ] Change approval and documentation
   - [ ] Vulnerability management program (scanning, patching)
   - [ ] Incident detection and response procedures
   - [ ] Evidence: Change tickets, vulnerability scan reports, incident logs

   **CC8: Change Management**
   - [ ] Formal change management policy
   - [ ] Change request, approval, and testing documented
   - [ ] Emergency change procedures
   - [ ] Post-implementation review
   - [ ] Evidence: Git PR history with approvals, deployment logs, rollback records

   **CC9: Risk Mitigation**
   - [ ] Vendor risk management program
   - [ ] Business continuity planning
   - [ ] Insurance coverage assessment
   - [ ] Evidence: Vendor assessments, BCP documentation, insurance certificates

3. **Assess Availability controls (if in scope):**
   - [ ] Uptime monitoring with historical data
   - [ ] SLA definitions and measurement
   - [ ] Capacity planning and auto-scaling
   - [ ] Disaster recovery plan tested and documented
   - [ ] Backup procedures with restoration testing
   - [ ] Redundancy and failover mechanisms
   - [ ] Incident response with RTO/RPO targets
   - [ ] Evidence: Uptime reports, DR test results, backup restoration logs, capacity reports

4. **Assess Processing Integrity controls (if in scope):**
   - [ ] Input validation and error handling
   - [ ] Data processing completeness checks
   - [ ] Reconciliation procedures
   - [ ] Error detection and correction workflows
   - [ ] Quality assurance processes
   - [ ] Evidence: Reconciliation reports, QA test results, error logs and resolution records

5. **Assess Confidentiality controls (if in scope):**
   - [ ] Data classification scheme implemented
   - [ ] Encryption at rest and in transit
   - [ ] Confidential data access restricted and logged
   - [ ] Data retention and secure disposal procedures
   - [ ] NDA/confidentiality agreements with personnel and vendors
   - [ ] Evidence: Data classification inventory, encryption configurations, disposal records

6. **Assess Privacy controls (if in scope):**
   - [ ] Privacy notice provided at collection
   - [ ] Consent mechanisms and records
   - [ ] Data subject access and deletion capabilities
   - [ ] Third-party disclosure controls
   - [ ] Privacy incident response
   - [ ] Evidence: Privacy policies, consent logs, DSR fulfillment records

7. **Evaluate evidence collection readiness for Type II:**

   For each control, verify:
   - [ ] **Evidence exists** — Can you produce artifacts demonstrating the control operated?
   - [ ] **Evidence is continuous** — Does it cover the full audit period, not just a snapshot?
   - [ ] **Evidence is timestamped** — Can auditors verify when activities occurred?
   - [ ] **Evidence is independent** — Is it system-generated (not manually created after the fact)?
   - [ ] **Evidence is retrievable** — Can it be produced within a reasonable time during audit?

   Common evidence types by control:
   | Control Area | Evidence Types |
   |---|---|
   | Access control | Provisioning tickets, access review reports, MFA logs |
   | Change management | Git PRs with approvals, deployment logs, change tickets |
   | Vulnerability management | Scan reports (monthly), patching records, exception tracking |
   | Incident management | Incident tickets, postmortem reports, communication records |
   | Monitoring | Alert configurations, dashboard screenshots, on-call schedules |
   | Backup/DR | Backup success logs, restoration test records, DR test reports |
   | Training | Training completion records, phishing simulation results |
   | Vendor management | Vendor assessments, SOC 2 reports from vendors, contract reviews |

8. **Identify control gaps and remediation needs:**
   For each gap:
   - Control reference (CC#)
   - Current state
   - Required state for Type II
   - Evidence that would be needed
   - Remediation steps
   - Timeline to achieve operating effectiveness (remember: Type II requires a period of operation)

**False-Positive Prevention (MUST follow):**
- ❌ Do NOT flag controls as missing without checking if they exist in a GRC tool, wiki, or separate policy repository
- ❌ Do NOT assume lack of evidence means lack of control — the control may operate but evidence collection may not be automated
- ❌ Do NOT require controls beyond the selected Trust Service Criteria scope
- ❌ Do NOT treat Type I evidence standards as sufficient for Type II — Type II requires continuous operation evidence
- ✅ DO distinguish between control design gaps (control doesn't exist) and evidence gaps (control exists but proof is missing)
- ✅ DO account for compensating controls that achieve the same objective differently
- ✅ DO check if sub-service organizations (cloud providers) provide their own SOC 2 reports covering some controls

**Expected Output:**

1. **Scope Definition:**
   - Applicable Trust Service Criteria
   - System boundary description
   - Sub-service organizations and carve-out vs. inclusive method

2. **Control Assessment Matrix:**
   | Control ID | Description | Design Status | Evidence Available | Evidence Continuous | Gap |
   |---|---|---|---|---|---|
   | CC6.1 | User provisioning | Implemented | Yes | Partial | Access review frequency |

3. **Evidence Gap Analysis:**
   - Controls operating without evidence collection
   - Evidence that exists but isn't continuous
   - Evidence that needs automation
   - Evidence retention period gaps

4. **Remediation Plan:**
   For each gap:
   - Control reference and description
   - Gap type (design / operating effectiveness / evidence)
   - Remediation action
   - Owner
   - Timeline
   - Evidence to be produced

5. **Audit Preparation Timeline:**
   - Month 1-2: Close control design gaps, begin evidence collection
   - Month 3-8: Observation period (controls operating with evidence)
   - Month 9: Pre-audit self-assessment
   - Month 10-12: Auditor fieldwork
   - Ongoing: Continuous monitoring and evidence retention

**Related Prompts:**
- security_compliance_analysis.md - Broad multi-framework compliance overview
- security_audit_trail_design.md - Audit logging patterns for evidence collection
- security_iso27001_implementation.md - ISO 27001 (complementary framework)
- security_infrastructure_analysis.md - Infrastructure security assessment

**When to Use:**
Use this prompt when preparing for a SOC 2 Type II audit, transitioning from Type I to Type II, evaluating audit readiness, building an evidence collection program, or responding to customer/prospect requests for SOC 2 compliance. Particularly valuable for SaaS companies, cloud service providers, and any organization handling customer data.

**Techniques Used:**
- ST-01 (Clear Objective Statement) - SOC 2 Type II preparation focus
- ST-02 (Structured Sequential Instructions) - Organized by Trust Service Criteria
- RT-02 (Multi-Dimensional Analysis Framework) - Control design, operating effectiveness, and evidence dimensions
- DS-06 (Prioritization and Severity Guidance) - Phased audit preparation timeline
- CM-01 (Explicit Context Framing) - Type I vs Type II distinction, scope definition
- QA-01 (Chain-of-Verification) - Evidence verification requirements
