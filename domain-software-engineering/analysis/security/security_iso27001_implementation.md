---
title: "ISO 27001 Implementation Checklist"
category: code-analysis/security
description: "ISO 27001 ISMS implementation assessment covering Annex A controls, risk treatment, Statement of Applicability, internal audit readiness, and certification preparation for software organizations"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-06
  - CM-01
  - DT-01
difficulty: advanced
tags:
  - compliance
  - iso-27001
  - isms
  - information-security
  - risk-management
  - certification
  - annex-a
updated: "2026-03-19"
---

# ISO 27001 Implementation Checklist

**Objective:** Assess the organization's readiness for ISO 27001 certification by evaluating the Information Security Management System (ISMS), reviewing Annex A control implementation, identifying gaps in risk treatment and documentation, and producing a certification preparation plan.

**Context:**
- ISO/IEC 27001:2022 is the current version (updated from 2013)
- Annex A contains 93 controls organized in 4 themes (was 114 controls in 14 domains in 2013 version)
- Certification requires an accredited certification body (Stage 1: documentation review, Stage 2: implementation audit)
- The ISMS must be operational before the Stage 2 audit (typically 3+ months of evidence)

**Instructions:**

1. **Assess ISMS core requirements (Clauses 4-10):**

   **Clause 4: Context of the Organization**
   - [ ] Interested parties identified (customers, regulators, employees, partners)
   - [ ] Internal and external issues documented
   - [ ] ISMS scope defined (organizational units, locations, assets, technologies)
   - [ ] Scope boundaries and applicability documented

   **Clause 5: Leadership**
   - [ ] Information security policy established and communicated
   - [ ] Management commitment demonstrated (resources, reviews, decisions)
   - [ ] Roles and responsibilities assigned (ISMS owner, risk owners, asset owners)
   - [ ] Security objectives aligned with business objectives

   **Clause 6: Planning**
   - [ ] Risk assessment methodology defined (likelihood × impact, qualitative/quantitative)
   - [ ] Risk assessment conducted with documented results
   - [ ] Risk treatment plan developed
   - [ ] Statement of Applicability (SoA) completed — all 93 Annex A controls addressed
   - [ ] Information security objectives established (measurable, monitored, communicated)
   - [ ] Risk acceptance criteria defined and approved by management

   **Clause 7: Support**
   - [ ] Resources allocated for ISMS operation
   - [ ] Competency requirements defined for security roles
   - [ ] Security awareness program active
   - [ ] Internal and external communication procedures documented
   - [ ] Documented information control (creation, approval, version, access, retention, disposal)

   **Clause 8: Operation**
   - [ ] Risk assessment performed at planned intervals and on significant changes
   - [ ] Risk treatment plan implemented
   - [ ] Operational controls functioning as designed
   - [ ] Outsourced processes controlled

   **Clause 9: Performance Evaluation**
   - [ ] Monitoring, measurement, analysis, and evaluation program
   - [ ] Internal audit program (planned, conducted, reported)
   - [ ] Management review conducted (inputs: audit results, incidents, risks, improvement opportunities)
   - [ ] Management review outputs documented (decisions, resource allocations)

   **Clause 10: Improvement**
   - [ ] Nonconformities identified and corrected
   - [ ] Corrective actions address root causes
   - [ ] Continual improvement process demonstrated

2. **Assess Annex A controls (ISO 27001:2022 — 4 themes, 93 controls):**

   **Theme A.5: Organizational Controls (37 controls)**

   *Policies and Governance:*
   - [ ] A.5.1: Policies for information security — defined, approved, communicated, reviewed
   - [ ] A.5.2: Information security roles and responsibilities — assigned and communicated
   - [ ] A.5.3: Segregation of duties — conflicting duties separated
   - [ ] A.5.4: Management responsibilities — ensuring personnel follow security policies

   *Threat Intelligence and Asset Management:*
   - [ ] A.5.7: Threat intelligence — collected, analyzed, and acted upon
   - [ ] A.5.9: Inventory of information and associated assets
   - [ ] A.5.10: Acceptable use of information and associated assets
   - [ ] A.5.11: Return of assets (upon termination)
   - [ ] A.5.12: Classification of information
   - [ ] A.5.13: Labeling of information

   *Access Control:*
   - [ ] A.5.15: Access control policy
   - [ ] A.5.16: Identity management
   - [ ] A.5.17: Authentication information (password policy, MFA)
   - [ ] A.5.18: Access rights — provisioned, reviewed, revoked

   *Supplier Management:*
   - [ ] A.5.19: Information security in supplier relationships
   - [ ] A.5.20: Addressing security within supplier agreements
   - [ ] A.5.21: Managing security in the ICT supply chain
   - [ ] A.5.22: Monitoring, review, and change management of supplier services
   - [ ] A.5.23: Information security for use of cloud services

   *Incident and Continuity:*
   - [ ] A.5.24: Incident management planning and preparation
   - [ ] A.5.25: Assessment and decision on information security events
   - [ ] A.5.26: Response to information security incidents
   - [ ] A.5.27: Learning from information security incidents
   - [ ] A.5.28: Collection of evidence
   - [ ] A.5.29: Information security during disruption
   - [ ] A.5.30: ICT readiness for business continuity

   *Compliance:*
   - [ ] A.5.31: Legal, statutory, regulatory, and contractual requirements identified
   - [ ] A.5.32: Intellectual property rights
   - [ ] A.5.33: Protection of records
   - [ ] A.5.34: Privacy and protection of PII
   - [ ] A.5.35: Independent review of information security
   - [ ] A.5.36: Compliance with policies, rules, and standards
   - [ ] A.5.37: Documented operating procedures

   **Theme A.6: People Controls (8 controls)**
   - [ ] A.6.1: Screening — background verification
   - [ ] A.6.2: Terms and conditions of employment
   - [ ] A.6.3: Information security awareness, education, and training
   - [ ] A.6.4: Disciplinary process
   - [ ] A.6.5: Responsibilities after termination or change of employment
   - [ ] A.6.6: Confidentiality or non-disclosure agreements
   - [ ] A.6.7: Remote working security
   - [ ] A.6.8: Information security event reporting

   **Theme A.7: Physical Controls (14 controls)**
   - [ ] A.7.1: Physical security perimeters
   - [ ] A.7.2: Physical entry controls
   - [ ] A.7.3: Securing offices, rooms, and facilities
   - [ ] A.7.4: Physical security monitoring
   - [ ] A.7.5: Protecting against physical and environmental threats
   - [ ] A.7.6: Working in secure areas
   - [ ] A.7.7: Clear desk and clear screen
   - [ ] A.7.8: Equipment siting and protection
   - [ ] A.7.9: Security of assets off-premises
   - [ ] A.7.10: Storage media lifecycle
   - [ ] A.7.11: Supporting utilities
   - [ ] A.7.12: Cabling security
   - [ ] A.7.13: Equipment maintenance
   - [ ] A.7.14: Secure disposal or re-use of equipment

   **Theme A.8: Technological Controls (34 controls)**
   - [ ] A.8.1: User endpoint devices
   - [ ] A.8.2: Privileged access rights
   - [ ] A.8.3: Information access restriction
   - [ ] A.8.4: Access to source code
   - [ ] A.8.5: Secure authentication
   - [ ] A.8.6: Capacity management
   - [ ] A.8.7: Protection against malware
   - [ ] A.8.8: Management of technical vulnerabilities
   - [ ] A.8.9: Configuration management
   - [ ] A.8.10: Information deletion
   - [ ] A.8.11: Data masking
   - [ ] A.8.12: Data leakage prevention
   - [ ] A.8.13: Information backup
   - [ ] A.8.14: Redundancy of information processing facilities
   - [ ] A.8.15: Logging
   - [ ] A.8.16: Monitoring activities
   - [ ] A.8.17: Clock synchronization
   - [ ] A.8.18: Use of privileged utility programs
   - [ ] A.8.19: Installation of software on operational systems
   - [ ] A.8.20: Networks security
   - [ ] A.8.21: Security of network services
   - [ ] A.8.22: Segregation of networks
   - [ ] A.8.23: Web filtering
   - [ ] A.8.24: Use of cryptography
   - [ ] A.8.25: Secure development life cycle
   - [ ] A.8.26: Application security requirements
   - [ ] A.8.27: Secure system architecture and engineering principles
   - [ ] A.8.28: Secure coding
   - [ ] A.8.29: Security testing in development and acceptance
   - [ ] A.8.30: Outsourced development
   - [ ] A.8.31: Separation of development, test, and production environments
   - [ ] A.8.32: Change management
   - [ ] A.8.33: Test information
   - [ ] A.8.34: Protection of information systems during audit testing

3. **Evaluate Statement of Applicability (SoA):**
   - [ ] All 93 controls addressed (implemented, justification for exclusion, or planned)
   - [ ] Exclusion justifications are defensible and risk-based
   - [ ] Control implementation status matches actual implementation
   - [ ] SoA version controlled and approved by management

4. **Assess internal audit readiness:**
   - [ ] Internal audit program planned (covering all ISMS areas over cycle)
   - [ ] Auditor independence ensured (auditors don't audit their own work)
   - [ ] Audit criteria, scope, and methods defined
   - [ ] Audit findings documented with nonconformities classified
   - [ ] Corrective actions tracked to closure with root cause analysis
   - [ ] At least one full internal audit cycle completed before certification

**False-Positive Prevention (MUST follow):**
- ❌ Do NOT assess against the 2013 version control structure (14 domains) — use the 2022 version (4 themes)
- ❌ Do NOT flag controls as gaps when they are legitimately excluded in the SoA with risk-based justification
- ❌ Do NOT require physical controls for organizations that are fully remote/cloud-based (but verify exclusion justification)
- ❌ Do NOT treat ISO 27001 and ISO 27002 as the same — 27001 is the certifiable standard, 27002 is guidance
- ✅ DO verify that implemented controls are not just documented but actually operating
- ✅ DO check if the organization is transitioning from 2013 to 2022 (transition deadline was October 2025)
- ✅ DO consider the organization's risk context when evaluating control adequacy

**Expected Output:**

1. **ISMS Maturity Assessment:**
   - Clause-by-clause status (4-10)
   - Documentation completeness
   - Operational evidence availability

2. **Annex A Control Status:**
   | Control | Description | Status | Evidence | SoA Status |
   |---|---|---|---|---|
   | A.5.1 | Policies for information security | Implemented | Policy doc v3.2 | Applicable |
   | A.7.1 | Physical security perimeters | Excluded | N/A | Excluded — fully remote |

3. **Gap Analysis:**
   For each gap:
   - Control reference and theme
   - Current state
   - Required state
   - Risk if unaddressed
   - Remediation steps
   - Effort and timeline

4. **Certification Preparation Plan:**
   - Month 1-2: Close ISMS documentation gaps, complete SoA
   - Month 3-5: Implement missing controls, begin operational evidence collection
   - Month 6: Internal audit
   - Month 7: Management review, corrective actions
   - Month 8: Stage 1 audit (documentation review)
   - Month 9-10: Address Stage 1 findings
   - Month 11: Stage 2 audit (implementation audit)
   - Ongoing: Surveillance audits (annual), recertification (3-year cycle)

**Related Prompts:**
- security_compliance_analysis.md - Multi-framework compliance overview
- security_soc2_type2_preparation.md - SOC 2 (complementary for US market)
- security_fedramp_authorization.md - FedRAMP (leverages NIST controls)
- security_audit_trail_design.md - Logging controls (A.8.15, A.8.16)

**When to Use:**
Use this prompt when implementing an ISMS from scratch, preparing for ISO 27001 certification, transitioning from 2013 to 2022 version, conducting gap analyses for existing ISMS, preparing for surveillance or recertification audits, or when customers/contracts require ISO 27001 compliance evidence.

**Techniques Used:**
- ST-01 (Clear Objective Statement) - ISO 27001 certification readiness focus
- ST-02 (Structured Sequential Instructions) - Organized by clauses and Annex A themes
- RT-02 (Multi-Dimensional Analysis Framework) - ISMS maturity, control implementation, documentation, and evidence
- DS-06 (Prioritization and Severity Guidance) - Certification preparation timeline
- CM-01 (Explicit Context Framing) - 2013 vs 2022 version distinction, certification process
- DT-01 (Hierarchical Task Breakdown) - 93 controls broken into themes and individual items
