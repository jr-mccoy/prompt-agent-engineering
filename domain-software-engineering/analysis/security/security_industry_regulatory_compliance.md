---
title: "Industry-Specific Regulatory Compliance (FINRA, PSD2, CCPA, ADA)"
category: code-analysis/security
description: "Industry-specific regulatory compliance analysis covering financial services (FINRA, PSD2/SCA), consumer privacy (CCPA/CPRA), and digital accessibility (ADA/Section 508) for software teams"
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
  - finra
  - psd2
  - ccpa
  - cpra
  - ada
  - section-508
  - financial
  - accessibility
  - privacy
updated: "2026-03-19"
---

# Industry-Specific Regulatory Compliance

**Objective:** Analyze the codebase and system architecture for compliance with industry-specific regulations including financial services (FINRA, PSD2/SCA), consumer privacy (CCPA/CPRA), and digital accessibility (ADA/Section 508), identifying implementation gaps and producing targeted remediation guidance.

**Context:**
- These regulations apply to specific industries or jurisdictions but have broad software implications
- Many organizations must comply with multiple overlapping regulations simultaneously
- Non-compliance penalties vary significantly: CCPA fines up to $7,500/violation, PSD2 enforcement by national authorities, ADA lawsuits averaging $25,000+ settlements, FINRA fines up to millions

**Instructions:**

1. **Determine applicable regulations based on business context:**
   - [ ] **FINRA:** Broker-dealers, investment advisors, securities trading platforms
   - [ ] **PSD2/SCA:** Payment services in the European Economic Area
   - [ ] **CCPA/CPRA:** Businesses collecting California residents' personal information (thresholds: $25M+ revenue, 100K+ consumers' data, or 50%+ revenue from selling data)
   - [ ] **ADA/Section 508:** US businesses with public-facing digital services (ADA Title III); federal agencies and contractors (Section 508)

---

2. **FINRA Compliance Assessment (Financial Services):**

   **A. Books and Records (Rules 4511, 3110)**
   - [ ] All customer communications (email, chat, social media) captured and retained
   - [ ] Electronic communications archivable in WORM (Write Once Read Many) format
   - [ ] Retention periods met: general records (6 years), customer account records (6 years), communications (3 years)
   - [ ] Records are readily accessible and searchable for regulatory examination
   - [ ] Supervisory review system for communications

   **B. Cybersecurity and Data Protection (Rule 3110, Reg S-P)**
   - [ ] Written supervisory procedures for cybersecurity
   - [ ] Customer data protection (Regulation S-P: privacy notices, opt-out, safeguards)
   - [ ] Incident response plan aligned with FINRA guidance
   - [ ] Annual cybersecurity risk assessment
   - [ ] Vendor due diligence for technology providers

   **C. Business Continuity (Rule 4370)**
   - [ ] Business continuity plan (BCP) documented
   - [ ] BCP addresses: data backup, mission-critical systems, communication with regulators and customers
   - [ ] Annual BCP review and testing
   - [ ] Alternate processing site capability

   **D. Anti-Money Laundering (Rule 3310)**
   - [ ] Customer Identification Program (CIP) implemented
   - [ ] Know Your Customer (KYC) procedures
   - [ ] Transaction monitoring for suspicious activity
   - [ ] Suspicious Activity Report (SAR) filing capability
   - [ ] AML compliance program with designated officer

   **E. Best Execution and Trade Reporting**
   - [ ] Order execution quality monitoring
   - [ ] Trade reporting within required timeframes
   - [ ] Audit trail for all order handling decisions

---

3. **PSD2 / Strong Customer Authentication (SCA) Compliance:**

   **A. Strong Customer Authentication (Article 97)**
   - [ ] SCA applied to: electronic payments, remote account access, actions with risk of fraud
   - [ ] Two of three authentication factors required:
     - Knowledge (password, PIN)
     - Possession (phone, hardware token)
     - Inherence (biometric)
   - [ ] Dynamic linking: authentication code linked to specific amount and payee
   - [ ] Independence of elements: breach of one factor doesn't compromise others

   **B. SCA Exemptions (properly implemented)**
   - [ ] Low-value transactions (< €30, cumulative < €100 or 5 transactions)
   - [ ] Trusted beneficiaries (whitelisted by customer)
   - [ ] Recurring transactions (same amount, same payee after initial SCA)
   - [ ] Merchant-initiated transactions
   - [ ] Transaction Risk Analysis (TRA) exemption with fraud rate monitoring
   - [ ] Exemption logic documented and auditable

   **C. Open Banking / API Access (Articles 66-67)**
   - [ ] Dedicated interface (API) for authorized third-party providers (TPPs)
   - [ ] TPP identification and authentication (eIDAS certificates)
   - [ ] Account Information Service Provider (AISP) access implemented
   - [ ] Payment Initiation Service Provider (PISP) access implemented
   - [ ] Consent management for TPP access
   - [ ] Fallback mechanism if dedicated interface unavailable
   - [ ] API performance and availability monitoring (99.5%+ uptime)

   **D. Security Requirements**
   - [ ] Secure communication channels for all payment data
   - [ ] Session management with appropriate timeouts
   - [ ] Transaction limits and velocity checks
   - [ ] Fraud monitoring and reporting

---

4. **CCPA/CPRA Compliance (California Consumer Privacy):**

   **A. Consumer Rights Implementation**

   - [ ] **Right to Know (§1798.100, §1798.110):**
     - Categories of personal information collected
     - Specific pieces of personal information collected
     - Sources of collection
     - Business/commercial purposes for collecting
     - Categories of third parties shared with
     - Verifiable consumer request process (identity verification)
     - Response within 45 days (with 45-day extension)

   - [ ] **Right to Delete (§1798.105):**
     - Deletion of personal information upon request
     - Direction to service providers to delete
     - Exceptions documented (legal, security, internal use)
     - Verification of identity before deletion

   - [ ] **Right to Opt-Out of Sale/Sharing (§1798.120, CPRA §1798.121):**
     - "Do Not Sell or Share My Personal Information" link on homepage
     - Mechanism to opt out of sale AND sharing (CPRA addition)
     - Global Privacy Control (GPC) signal honored
     - Opt-out preference persisted and respected across sessions
     - No selling data of consumers under 16 without opt-in (under 13: parental consent)

   - [ ] **Right to Correct (CPRA §1798.106):**
     - Mechanism for consumers to correct inaccurate personal information
     - Commercially reasonable efforts to correct across systems

   - [ ] **Right to Limit Use of Sensitive Personal Information (CPRA §1798.121):**
     - "Limit the Use of My Sensitive Personal Information" link
     - Sensitive PI defined: SSN, financial accounts, geolocation, race/ethnicity, religion, biometrics, health, sexual orientation, mail/email/text contents
     - Use limited to what is necessary and expected

   **B. Privacy Notice Requirements**
   - [ ] At-or-before-collection notice
   - [ ] Comprehensive privacy policy with all required disclosures
   - [ ] Updated annually
   - [ ] Categories of PI collected, purposes, retention periods
   - [ ] Financial incentive disclosures (if applicable)

   **C. Service Provider / Contractor Requirements**
   - [ ] Contracts restrict use of PI to specified purposes
   - [ ] Service providers don't sell or share received PI
   - [ ] Flow-down requirements to subcontractors
   - [ ] Notification obligations for consumer requests

   **D. Data Minimization (CPRA Addition)**
   - [ ] Collection limited to what is reasonably necessary and proportionate
   - [ ] Retention limited to what is reasonably necessary for stated purpose
   - [ ] Retention schedule documented and enforced

---

5. **ADA / Section 508 Digital Accessibility Compliance:**

   **A. WCAG 2.1 AA Conformance (Section 508 references WCAG 2.0 AA; ADA courts increasingly require WCAG 2.1 AA)**

   *Perceivable:*
   - [ ] 1.1.1: Non-text content has text alternatives (alt text, labels, descriptions)
   - [ ] 1.2.1-1.2.5: Audio/video has captions, transcripts, audio descriptions
   - [ ] 1.3.1-1.3.5: Information structure conveyed programmatically (headings, lists, tables, landmarks)
   - [ ] 1.4.1: Color is not the only means of conveying information
   - [ ] 1.4.3: Contrast ratio minimum 4.5:1 for normal text, 3:1 for large text
   - [ ] 1.4.4: Text resizable to 200% without loss of content
   - [ ] 1.4.10: Content reflows at 320px width (no horizontal scrolling)
   - [ ] 1.4.11: Non-text contrast minimum 3:1 (UI components, graphical objects)

   *Operable:*
   - [ ] 2.1.1-2.1.2: All functionality available from keyboard, no keyboard traps
   - [ ] 2.2.1: Timing adjustable (session timeouts, auto-advancing content)
   - [ ] 2.3.1: No flashing content >3 times per second
   - [ ] 2.4.1-2.4.7: Skip navigation, page titles, focus order, link purpose, headings, visible focus
   - [ ] 2.5.1-2.5.4: Pointer gestures, pointer cancellation, label in name, motion actuation

   *Understandable:*
   - [ ] 3.1.1-3.1.2: Language of page and parts identified
   - [ ] 3.2.1-3.2.2: No unexpected context changes on focus or input
   - [ ] 3.3.1-3.3.4: Error identification, labels/instructions, error suggestions, error prevention

   *Robust:*
   - [ ] 4.1.1: Valid HTML parsing (well-formed markup)
   - [ ] 4.1.2: Name, role, value for all UI components
   - [ ] 4.1.3: Status messages available to assistive technology

   **B. Technical Implementation Checks**
   - [ ] ARIA roles and attributes used correctly (not overriding native semantics)
   - [ ] Form inputs have associated labels (`<label>` or `aria-labelledby`)
   - [ ] Dynamic content changes announced to screen readers (live regions)
   - [ ] Custom components follow WAI-ARIA Authoring Practices
   - [ ] Focus management for SPAs (route changes, modals, dynamic content)
   - [ ] Touch targets minimum 44x44 CSS pixels
   - [ ] Error messages programmatically associated with inputs

   **C. Testing and Documentation**
   - [ ] Automated accessibility testing integrated in CI/CD (axe-core, Lighthouse, pa11y)
   - [ ] Manual testing with screen readers (NVDA, JAWS, VoiceOver)
   - [ ] Keyboard-only navigation testing
   - [ ] Accessibility statement published
   - [ ] Known issues documented with remediation timeline (VPAT/ACR for Section 508)
   - [ ] User testing with people with disabilities (recommended, not required)

---

**False-Positive Prevention (MUST follow):**
- ❌ Do NOT flag FINRA requirements for companies that are not broker-dealers or registered investment advisors
- ❌ Do NOT apply PSD2/SCA requirements to payment flows outside the EEA
- ❌ Do NOT report CCPA violations for businesses below the applicability thresholds
- ❌ Do NOT flag WCAG issues based solely on automated scanning — automated tools catch only ~30% of real accessibility issues
- ❌ Do NOT assume ADA digital compliance is required only for government sites (Title III applies to private businesses)
- ✅ DO verify business context and jurisdictional applicability before reporting gaps
- ✅ DO check if PSD2 exemptions legitimately apply before flagging missing SCA
- ✅ DO manually verify automated accessibility scan results before reporting
- ✅ DO check for Global Privacy Control (GPC) support when assessing CCPA opt-out

**Expected Output:**

1. **Applicability Assessment:**
   - Applicable regulations with justification
   - Non-applicable regulations with exclusion rationale

2. **Compliance Assessment by Regulation:**
   For each applicable regulation:
   | Requirement | Status | Gap Description | Risk Level | Remediation |
   |---|---|---|---|---|
   | CCPA Right to Delete | Partial | No service provider flow-down | High | Update contracts, add deletion API |

3. **Cross-Regulation Overlap Analysis:**
   - Common controls that satisfy multiple regulations
   - Conflicting requirements and resolution approach

4. **Gap Report:**
   For each gap:
   - Regulation and section reference
   - Current vs. required state
   - Risk severity and potential penalty
   - Remediation steps
   - Effort estimate

5. **Remediation Roadmap:**
   - Phase 1 (0-30 days): Consumer-facing compliance (opt-out links, consent, critical accessibility)
   - Phase 2 (1-3 months): Technical implementation (SCA, audit trails, rights fulfillment)
   - Phase 3 (3-6 months): Full compliance (VPAT, accessibility remediation, training)

**Related Prompts:**
- security_compliance_analysis.md - Broad multi-framework compliance overview
- security_gdpr_implementation_guide.md - GDPR (overlapping with CCPA on privacy)
- security_hipaa_software_compliance.md - Healthcare (may overlap with financial health data)
- testing_accessibility_wcag.md - Detailed WCAG testing (complements ADA section)
- frontend_accessibility_wcag_audit.md - Frontend accessibility audit

**When to Use:**
Use this prompt when entering regulated industries (financial services, payments), serving California consumers, building public-facing web applications, responding to ADA demand letters, preparing for FINRA examination, implementing PSD2 APIs for European payments, or conducting cross-regulation compliance assessments.

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Multi-regulation compliance focus
- ST-02 (Structured Sequential Instructions) - Organized by regulation
- RT-02 (Multi-Dimensional Analysis Framework) - Per-regulation requirements with cross-cutting analysis
- DS-06 (Prioritization and Severity Guidance) - Risk-based remediation roadmap
- CM-01 (Explicit Context Framing) - Applicability thresholds and jurisdictional context
- DT-01 (Hierarchical Task Breakdown) - Regulations broken into requirement groups
