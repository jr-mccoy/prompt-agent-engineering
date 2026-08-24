---
title: "Terms of Service Generator"
category: mobile-development
description: "Generate Terms of Service for an Android app covering user obligations, intellectual property, limitation of liability, subscription/refund terms, content guidelines, and termination provisions"
techniques:
  - ST-01
  - ST-02
  - CM-01
  - RT-02
  - DS-06
difficulty: intermediate
tags:
  - android
  - legal
  - terms-of-service
  - compliance
  - play-store
  - solo-developer
updated: "2026-02-12"
---

# Terms of Service Generator

**Objective:** Generate a comprehensive Terms of Service (ToS) document for an Android application — covering user obligations, acceptable use policy, intellectual property rights, limitation of liability, subscription and refund terms (aligned with Google Play policies), user-generated content guidelines (if applicable), privacy references, dispute resolution, and termination provisions — producing a document that is legally substantive while remaining readable by non-lawyers.

**When to Use:** Use this prompt when launching a new Android app that needs Terms of Service, when updating ToS for new features (especially subscriptions, user content, or AI features), when Google Play review requests a ToS URL, or when you need to document the rules governing app usage.

**Important context:** Terms of Service are not legally required for all apps, but Google Play strongly encourages them for apps that collect user data, offer subscriptions, or allow user-generated content. A ToS protects the developer by defining acceptable use, limiting liability, and providing grounds for account termination. For solo developers, the ToS should be comprehensive but not overengineered — focus on the provisions that actually matter for your app's risk profile. **This prompt generates a starting template — consult a qualified attorney for your jurisdiction before publishing.**

---

## Context Gathering

1. **App Details:**
   - "What does the app do? Describe core functionality."
   - "Does the app allow user-generated content (text, images, files)?"
   - "Does the app use AI or machine learning to generate content?"
   - "What user data does the app collect?"

2. **Monetization:**
   - "Does the app offer subscriptions? If so, what tiers and prices?"
   - "Are there one-time in-app purchases?"
   - "Is there a free trial? What happens when it ends?"
   - "Do you offer refunds beyond Google Play's standard policy?"

3. **User Interaction:**
   - "Can users interact with each other (chat, comments, sharing)?"
   - "Can users create public content visible to others?"
   - "Are there age restrictions (must be 13+, 18+)?"

4. **Business:**
   - "What is your business entity (LLC, sole proprietorship, corporation)?"
   - "What jurisdiction (state/country) governs your business?"
   - "Do you have an existing privacy policy URL?"

---

## Instructions

Generate a Terms of Service document with the following sections, customized to the app's specifics:

### Section 1: Introduction and Acceptance
- App name and developer/company identity
- Effective date
- "By using this app, you agree to these Terms" language
- Minimum age requirement (13+ for COPPA, or 16+ if GDPR applies)
- Reference to Privacy Policy

### Section 2: Account Registration
- What is required to create an account
- User responsibility for account security
- One account per person (if applicable)
- Account sharing restrictions
- Accurate information requirement

### Section 3: Acceptable Use
- What users may do with the app
- Prohibited activities (abuse, fraud, reverse engineering, scraping)
- Content standards for user-generated content (if applicable)
- Intellectual property respect (don't upload copyrighted material)

### Section 4: Subscriptions and Payments (if applicable)
- Subscription tiers and pricing
- Billing cycle and auto-renewal disclosure (**Google Play requires clear disclosure**)
- Free trial terms (duration, what happens after)
- Cancellation process (link to Google Play subscription management)
- Refund policy (align with Google Play's refund policies)
- Price change notification process
- Grace period and account hold behavior

### Section 5: User-Generated Content (if applicable)
- User retains ownership of their content
- License grant to the app (necessary for displaying/processing content)
- Content moderation rights
- Takedown process for reported content
- No guarantee of content preservation
- Prohibited content types

### Section 6: Intellectual Property
- App and its content are owned by the developer
- Limited license to use the app (non-exclusive, non-transferable, revocable)
- Trademark and copyright notices
- Open source license attributions (link to licenses screen in app)

### Section 7: Privacy
- Reference to Privacy Policy (link)
- Brief summary of data practices
- User consent acknowledgment

### Section 8: Disclaimers and Limitation of Liability
- App provided "as is" without warranty
- No guarantee of availability, accuracy, or fitness for purpose
- Limitation of liability to the amount paid in the last 12 months (or a reasonable cap)
- Exclusion of consequential, incidental, and indirect damages
- Some jurisdictions do not allow liability limitations — savings clause

### Section 9: Indemnification
- User agrees to indemnify developer against claims arising from user's violation of Terms
- Keep this reasonable — not overly broad

### Section 10: Termination
- Developer may terminate or suspend accounts for Terms violations
- User may terminate by deleting their account
- Effect of termination (data deletion timeline, subscription cancellation)
- Provisions that survive termination (liability, indemnification, IP)

### Section 11: Dispute Resolution
- Governing law (your state/jurisdiction)
- Informal resolution attempt first (30 days)
- Binding arbitration clause (if desired — common in US)
- Class action waiver (if desired — common in US)
- Small claims court exception
- Jurisdiction for legal proceedings

### Section 12: Changes to Terms
- Right to modify Terms
- Notification method (in-app notification, email)
- Continued use constitutes acceptance
- Effective date of changes

### Section 13: General Provisions
- Severability (invalid provisions don't void entire agreement)
- Waiver (failure to enforce doesn't waive rights)
- Entire agreement
- Assignment
- Contact information

---

## Expected Output

1. **Complete Terms of Service document** — formatted in clear, readable language with proper section numbering
2. **Google Play compliance notes** — any areas where the ToS must align with Play Store policies
3. **Customization checklist** — sections that need specific values filled in (company name, jurisdiction, subscription details)
4. **Legal review recommendations** — specific areas where professional legal review is most important

---

## CRITICAL: Verification Requirements

- [ ] Auto-renewal terms are clearly disclosed (Google Play policy requirement)
- [ ] Cancellation instructions reference Google Play subscription management
- [ ] Privacy Policy is referenced with a URL placeholder
- [ ] Minimum age requirement is stated (13+ minimum for COPPA)
- [ ] Contact information is provided
- [ ] The effective date is included
- [ ] **Disclaimer:** Document includes a note that it should be reviewed by a qualified attorney
- [ ] Language is readable by non-lawyers (avoid unnecessary legal jargon)
