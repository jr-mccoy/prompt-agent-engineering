---
title: "iOS Terms of Service Generator"
category: mobile-development
description: "Generate terms of service for iOS apps covering subscription terms, Apple EULA requirements, in-app purchase terms, content guidelines, and dispute resolution."
techniques:
  - ST-01
  - ST-03
difficulty: beginner
tags:
  - ios
  - legal
  - app-store
  - terms-of-service
  - mobile-development
updated: "2026-03-20"
---

# iOS Terms of Service Generator

**Objective:** Generate comprehensive terms of service for an iOS app that covers subscription and auto-renewal terms, Apple EULA requirements for licensed applications, in-app purchase terms, user-generated content guidelines, acceptable use policies, and dispute resolution mechanisms in compliance with App Store Review Guidelines.

**When to Use:** Use this prompt before initial App Store submission, when adding subscriptions or in-app purchases, when launching user-generated content features, or when updating legal terms for new functionality. Should be completed alongside the privacy policy.

**Prompt Type:** Modular (150-300 lines)

---

## Context Gathering

Before generating the terms of service, gather essential context:

1. **App & Business Details:**
   - "What is the app name, company legal name, and jurisdiction of incorporation?"
   - "What is the contact email for legal inquiries?"
   - "Is the app offered in multiple countries/regions?"

2. **Monetization:**
   - "Does the app offer subscriptions? If so, what plans and pricing?"
   - "Are there one-time in-app purchases or consumable purchases?"
   - "Does the app use Apple's Standard EULA or a custom EULA?"

3. **Content & Community:**
   - "Does the app allow user-generated content (posts, comments, images, reviews)?"
   - "Is there user-to-user messaging or social features?"
   - "What content moderation policies are in place?"

4. **Features:**
   - "Does the app integrate with third-party services the user must agree to?"
   - "Are there features restricted by age (gambling, alcohol, mature content)?"
   - "Does the app provide professional advice (medical, legal, financial)?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before generating ANY terms of service, you MUST:**

1. **Review Apple's Standard EULA** - Understand when Apple's standard EULA is sufficient vs when a custom EULA is required.
2. **Check subscription requirements** - App Store Review Guideline 3.1.2 requires specific subscription disclosure language.
3. **Verify content moderation obligations** - If UGC exists, content moderation policies must be documented.
4. **Confirm in-app purchase disclosures** - All purchases managed by Apple must reference Apple's payment processing.
5. **Legal review disclaimer** - Note that AI-generated terms should be reviewed by legal counsel.

### False-Positive Prevention

- Do NOT claim ownership of user content without specifying a license grant
- Do NOT omit Apple's required subscription auto-renewal language
- Do NOT create refund terms that conflict with Apple's refund policies (Apple handles refunds)
- Do NOT include arbitration clauses prohibited in certain jurisdictions (EU consumer protections)
- Do NOT forget to reference Apple as a third-party beneficiary (Apple EULA requirement)
- DO include Apple's required auto-renewal subscription disclosure language
- DO specify that payments are processed by Apple, not the developer
- DO include content takedown procedures if UGC is present
- DO address intellectual property rights clearly
- DO provide a clear mechanism for users to agree to the terms

---

### Phase 1: Terms Structure Planning

#### 1.1 Apple EULA Decision

```markdown
## EULA Decision Tree

Does your app need a CUSTOM EULA?

├─→ App has subscriptions with specific terms → YES, custom EULA
├─→ App has user-generated content → YES, custom EULA
├─→ App provides professional advice → YES, custom EULA with disclaimers
├─→ App has community/social features → YES, custom EULA with acceptable use
├─→ App has third-party service integrations → YES, custom EULA
└─→ Simple utility app, no UGC, no subscriptions → Apple Standard EULA may suffice

Note: If using Apple's Standard EULA, you still need Terms of Service
for your backend services. The EULA covers only the app license.
```

---

### Phase 2: Terms of Service Generation

**CHECKPOINT 1:** Confirm business model and feature scope before generating terms.

```markdown
## App Profile

| Feature | Present? | Terms Implications |
|---------|----------|-------------------|
| Subscriptions | Yes/No | Auto-renewal disclosure required |
| One-time IAP | Yes/No | Purchase terms needed |
| User accounts | Yes/No | Account terms needed |
| User-generated content | Yes/No | Content license + moderation policy |
| Social/messaging | Yes/No | Acceptable use policy |
| Professional advice | Yes/No | Disclaimer of liability |
| Third-party services | Yes/No | Service-specific terms |

**Proceed with terms generation?**
```

#### 2.1 Terms of Service Template

```markdown
# Terms of Service for [App Name]

**Effective Date:** [Date]
**Last Updated:** [Date]

These Terms of Service ("Terms") govern your use of the [App Name] mobile
application ("App") provided by [Company Legal Name] ("we," "our," or "us").

By downloading, installing, or using the App, you agree to these Terms. If you
do not agree, do not use the App.

**IMPORTANT:** This terms of service template was generated with AI assistance
and should be reviewed by qualified legal counsel before publication.

---

## 1. License Grant

Subject to these Terms, we grant you a limited, non-exclusive, non-transferable,
revocable license to use the App on Apple-branded devices that you own or control,
as permitted by the Apple Media Services Terms and Conditions.

This license does not allow you to:
- Modify, reverse engineer, or decompile the App
- Rent, lease, lend, sell, or sublicense the App
- Copy, distribute, or create derivative works of the App
- Remove or alter any proprietary notices in the App

---

## 2. Account Registration

### 2.1 Account Creation
To use certain features, you may need to create an account. You agree to:
- Provide accurate, current, and complete information
- Maintain the security of your password
- Accept responsibility for all activity under your account
- Notify us immediately of any unauthorized use

### 2.2 Account Termination
We may suspend or terminate your account if you violate these Terms. You may
delete your account at any time through [Settings > Account > Delete Account /
by contacting support@company.com].

---

## 3. Subscriptions and Purchases

### 3.1 Subscription Terms
[Include this section if the app offers subscriptions]

The App offers the following subscription plans:

| Plan | Price | Billing Cycle | Features |
|------|-------|---------------|----------|
| [Basic] | [$X.XX/month] | Monthly | [Feature list] |
| [Premium] | [$X.XX/year] | Annual | [Feature list] |

**Auto-Renewal:** Subscriptions automatically renew unless canceled at least
24 hours before the end of the current billing period. Your Apple ID account
will be charged for renewal within 24 hours prior to the end of the current
period at the rate of the selected plan.

**Managing Subscriptions:** You can manage and cancel subscriptions in your
Apple ID account settings. Go to Settings > [Your Name] > Subscriptions on
your iOS device.

**Free Trials:** If offered, free trial periods automatically convert to paid
subscriptions at the end of the trial unless canceled at least 24 hours before
the trial ends. Any unused portion of a free trial is forfeited upon purchasing
a subscription.

**Price Changes:** We may change subscription prices. You will be notified in
advance, and price changes will apply to the next billing period after notice.

### 3.2 In-App Purchases
[Include this section if the app offers IAP]

The App may offer additional features or content for purchase. All purchases
are processed by Apple through your Apple ID account. We do not directly
process payment information.

- Consumable purchases (e.g., [credits, tokens]) are used upon purchase and
  are non-refundable
- Non-consumable purchases (e.g., [premium features]) are available permanently
  on the purchasing Apple ID

### 3.3 Refunds
All purchases are made through Apple's App Store. Refund requests must be
directed to Apple following their refund process at
[https://support.apple.com/en-us/HT204084](https://support.apple.com/en-us/HT204084).

---

## 4. User-Generated Content

### 4.1 Your Content
[Include this section if the app supports UGC]

You retain ownership of content you submit through the App ("Your Content").
By submitting content, you grant us a worldwide, non-exclusive, royalty-free,
sublicensable license to use, reproduce, modify, display, and distribute Your
Content in connection with operating and improving the App.

You represent that:
- You own or have rights to submit the content
- Your content does not infringe any third party's rights
- Your content complies with these Terms and our Content Guidelines

### 4.2 Content Guidelines
You agree NOT to submit content that:
- Is illegal, harmful, threatening, abusive, or harassing
- Contains hate speech or discrimination
- Is sexually explicit or pornographic
- Infringes intellectual property rights
- Contains personal information of others without consent
- Is spam, advertising, or solicitation
- Contains malware or harmful code
- Impersonates another person or entity

### 4.3 Content Moderation
We reserve the right to remove or disable access to any content that violates
these Terms or Content Guidelines, without prior notice. We may use automated
tools and human review for content moderation.

### 4.4 Content Reporting
You can report content that violates these guidelines by [tapping the report
button / emailing abuse@company.com]. We will review reports and take
appropriate action within [timeframe].

### 4.5 DMCA / Copyright Notices
If you believe content infringes your copyright, send a notice to our
designated agent:

- **Email:** [dmca@company.com]
- **Address:** [Company Address]

Include: (1) description of the copyrighted work, (2) identification of the
infringing content, (3) your contact information, (4) a statement of good
faith belief, (5) a statement of accuracy under penalty of perjury, and
(6) your signature.

---

## 5. Acceptable Use

You agree not to:
- Violate any applicable laws or regulations
- Access the App through automated means (bots, scrapers)
- Interfere with or disrupt the App's infrastructure
- Attempt to gain unauthorized access to other accounts or systems
- Use the App for any commercial purpose not expressly permitted
- Circumvent any content filtering or security features

---

## 6. Intellectual Property

The App and its original content, features, and functionality are owned by
[Company Name] and are protected by copyright, trademark, and other
intellectual property laws. Our trademarks may not be used without prior
written consent.

---

## 7. Disclaimers

### 7.1 General Disclaimer
THE APP IS PROVIDED "AS IS" AND "AS AVAILABLE" WITHOUT WARRANTIES OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO IMPLIED WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT.

### 7.2 Professional Advice Disclaimer
[Include if the app provides health, legal, financial, or other professional information]

The App does not provide [medical/legal/financial] advice. Content is for
informational purposes only and should not replace professional consultation.
Always seek the advice of qualified professionals for your specific situation.

---

## 8. Limitation of Liability

TO THE MAXIMUM EXTENT PERMITTED BY LAW, [COMPANY NAME] SHALL NOT BE LIABLE FOR
ANY INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL, OR PUNITIVE DAMAGES, INCLUDING
LOSS OF PROFITS, DATA, OR GOODWILL, ARISING FROM YOUR USE OF THE APP.

OUR TOTAL LIABILITY SHALL NOT EXCEED THE AMOUNT YOU PAID TO US IN THE TWELVE
(12) MONTHS PRECEDING THE CLAIM, OR [AMOUNT], WHICHEVER IS LESS.

Some jurisdictions do not allow the exclusion of certain warranties or limitation
of liability. In such jurisdictions, our liability is limited to the fullest
extent permitted by law.

---

## 9. Dispute Resolution

### 9.1 Governing Law
These Terms are governed by the laws of [State/Country], without regard to
conflict of law provisions.

### 9.2 Dispute Process
[Choose one based on jurisdiction and business needs:]

**Option A: Arbitration (US apps)**
Any dispute arising from these Terms shall be resolved through binding
arbitration under the rules of [AAA/JAMS], conducted in [City, State].
You agree to waive any right to a jury trial or class action.

**Option B: Courts (EU-compliant)**
Any dispute arising from these Terms shall be submitted to the competent
courts of [Jurisdiction]. Nothing in these Terms limits your rights as a
consumer under applicable consumer protection laws.

---

## 10. Apple-Specific Terms

### 10.1 Third-Party Beneficiary
You acknowledge that Apple, Inc. is a third-party beneficiary of these Terms
and may enforce these Terms against you.

### 10.2 Apple's Responsibility
Apple has no obligation to provide maintenance, support, or warranty for the
App. To the extent any warranty exists, any claims shall be directed to us,
not to Apple.

### 10.3 Product Claims
We, not Apple, are responsible for addressing any product claims, including
product liability claims, claims that the App fails to conform to legal or
regulatory requirements, and consumer protection claims.

### 10.4 Intellectual Property Claims
We, not Apple, are responsible for investigation, defense, and settlement of
any intellectual property infringement claims.

---

## 11. Changes to Terms

We may update these Terms from time to time. We will notify you of material
changes by [updating the effective date / in-app notification / email]. Your
continued use of the App after changes constitutes acceptance.

---

## 12. Contact Us

For questions about these Terms:
- **Email:** [legal@company.com]
- **Address:** [Company Address]
```

---

### Phase 3: App Store Submission Alignment

**CHECKPOINT 2:** Review generated terms before App Store configuration.

```markdown
## Terms Review Checklist

| Requirement | Present? | Notes |
|-------------|----------|-------|
| Subscription auto-renewal language | — | Required by App Store Guideline 3.1.2 |
| Apple as third-party beneficiary | — | Required by Apple EULA |
| Refund directed to Apple | — | Cannot offer direct refunds for IAP |
| Content guidelines (if UGC) | — | Required by Guideline 1.2 |
| Professional disclaimer (if applicable) | — | Required for health/legal/financial |
| DMCA process (if UGC) | — | Required by US law for UGC platforms |

**Ready for App Store configuration?**
```

#### 3.1 App Store Connect Configuration

```markdown
## Where to Configure Custom EULA

1. App Store Connect > Your App > App Information
2. Scroll to "License Agreement"
3. Select "Custom App License Agreement"
4. Paste your terms or provide URL
5. Select territories where the custom EULA applies

## Terms of Service URL
- Host at: https://yourapp.com/terms
- Also include in-app: Settings > Terms of Service
- Must be accessible without authentication
```

---

## Expected Output

### Deliverables

```
legal/
├── TERMS_OF_SERVICE.md            # Complete terms of service document
├── CONTENT_GUIDELINES.md          # User-generated content guidelines (if applicable)
└── EULA_DECISION.md               # Documentation of Apple Standard vs Custom EULA decision
```

### Implementation Checklist

- [ ] Apple Standard vs Custom EULA decision documented
- [ ] Terms of service generated with all applicable sections
- [ ] Subscription auto-renewal language matches App Store requirements
- [ ] In-app purchase terms reference Apple's payment processing
- [ ] User-generated content guidelines included (if applicable)
- [ ] DMCA/copyright takedown process documented (if UGC)
- [ ] Professional advice disclaimers included (if applicable)
- [ ] Apple third-party beneficiary clause included
- [ ] Dispute resolution mechanism specified
- [ ] Terms hosted at accessible URL
- [ ] Custom EULA configured in App Store Connect (if applicable)
- [ ] Legal counsel review disclaimer included

---

## Techniques Used

- **ST-01** (Clear Objective): Focused on generating App Store-compliant terms of service
- **ST-03** (Output Format Templates): Structured legal template with fill-in sections

---

## Related Prompts

- [ios_privacy_policy_generator.md](../publishing/ios_privacy_policy_generator.md) - Privacy policy generation
- [ios_gdpr_compliance_audit.md](../publishing/ios_gdpr_compliance_audit.md) - GDPR compliance audit
- [ios_app_review_guidelines_check.md](../publishing/ios_app_review_guidelines_check.md) - App Store guideline compliance
- [ios_pre_submission_checklist.md](../publishing/ios_pre_submission_checklist.md) - Pre-submission requirements
