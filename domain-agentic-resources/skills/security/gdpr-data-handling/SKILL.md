---
name: gdpr-data-handling
description: Implement GDPR-compliant data handling with consent management, data subject rights, and privacy by design. Use when building systems that process EU personal data, implementing privacy controls, or conducting GDPR compliance reviews.
metadata:
  tags:
    - compliance
    - data
    - gdpr
    - handling
    - privacy
  updated: "2026-04-11"
---
# GDPR Data Handling

Practical implementation guide for GDPR-compliant data processing, consent management, and privacy controls.

## When to Use This Skill

- Building systems that process EU personal data
- Implementing consent management
- Handling data subject requests (DSRs)
- Conducting GDPR compliance reviews
- Designing privacy-first architectures
- Creating data processing agreements

## Core Concepts

### 1. Personal Data Categories

| Category | Examples | Protection Level |
|----------|----------|------------------|
| **Basic** | Name, email, phone | Standard |
| **Sensitive (Art. 9)** | Health, religion, ethnicity | Explicit consent |
| **Criminal (Art. 10)** | Convictions, offenses | Official authority |
| **Children's** | Under 16 data | Parental consent |

### 2. Legal Bases for Processing

```
Article 6 - Lawful Bases:
├── Consent: Freely given, specific, informed
├── Contract: Necessary for contract performance
├── Legal Obligation: Required by law
├── Vital Interests: Protecting someone's life
├── Public Interest: Official functions
└── Legitimate Interest: Balanced against rights
```

### 3. Data Subject Rights

```
Right to Access (Art. 15)      ─┐
Right to Rectification (Art. 16) │
Right to Erasure (Art. 17)       │ Must respond
Right to Restrict (Art. 18)      │ within 1 month
Right to Portability (Art. 20)   │
Right to Object (Art. 21)       ─┘
```

## Implementation Patterns

### Pattern 1: Consent Management

```javascript
// Consent data model
const consentSchema = {
  userId: String,
  consents: [{
    purpose: String,         // 'marketing', 'analytics', etc.
    granted: Boolean,
    timestamp: Date,
    source: String,          // 'web_form', 'api', etc.
    version: String,         // Privacy policy version
    ipAddress: String,       // For proof
    userAgent: String        // For proof
  }],
  auditLog: [{
    action: String,          // 'granted', 'withdrawn', 'updated'
    purpose: String,
    timestamp: Date,
    source: String
  }]
};

// Consent service
class ConsentManager {
  async recordConsent(userId, purpose, granted, metadata) {
    const consent = {
      purpose,
      granted,
      timestamp: new Date(),
      source: metadata.source,
      version: await this.getCurrentPolicyVersion(),
      ipAddress: metadata.ipAddress,
      userAgent: metadata.userAgent
    };

    await this.db.consents.updateOne(
      { userId },
      {
        $push: {
          consents: consent,
          auditLog: {
            action: granted ? 'granted' : 'withdrawn',
            purpose,
            timestamp: consent.timestamp,
            source: metadata.source
          }
        }
      },
      { upsert: true }
    );

    await this.eventBus.emit('consent.changed', {
      userId,
      purpose,
      granted,
      timestamp: consent.timestamp
    });
  }

  async hasConsent(userId, purpose) {
    const record = await this.db.consents.findOne({ userId });
    if (!record) return false;

    const latestConsent = record.consents
      .filter(c => c.purpose === purpose)
      .sort((a, b) => b.timestamp - a.timestamp)[0];

    return latestConsent?.granted === true;
  }

  async getConsentHistory(userId) {
    const record = await this.db.consents.findOne({ userId });
    return record?.auditLog || [];
  }
}
```

```html
<!-- GDPR-compliant consent UI -->
<div class="consent-banner" role="dialog" aria-labelledby="consent-title">
  <h2 id="consent-title">Cookie Preferences</h2>

  <p>We use cookies to improve your experience. Select your preferences below.</p>

  <form id="consent-form">
    <!-- Necessary - always on, no consent needed -->
    <div class="consent-category">
      <input type="checkbox" id="necessary" checked disabled>
      <label for="necessary">
        <strong>Necessary</strong>
        <span>Required for the website to function. Cannot be disabled.</span>
      </label>
    </div>

    <!-- Analytics - requires consent -->
    <div class="consent-category">
      <input type="checkbox" id="analytics" name="analytics">
      <label for="analytics">
        <strong>Analytics</strong>
        <span>Help us understand how you use our site.</span>
      </label>
    </div>

    <!-- Marketing - requires consent -->
    <div class="consent-category">
      <input type="checkbox" id="marketing" name="marketing">
      <label for="marketing">
        <strong>Marketing</strong>
        <span>Personalized ads based on your interests.</span>
      </label>
    </div>

    <div class="consent-actions">
      <button type="button" id="accept-all">Accept All</button>
      <button type="button" id="reject-all">Reject All</button>
      <button type="submit">Save Preferences</button>
    </div>

    <p class="consent-links">
      <a href="/privacy-policy">Privacy Policy</a> |
      <a href="/cookie-policy">Cookie Policy</a>
    </p>
  </form>
</div>
```

### Pattern 2: Data Subject Access Request (DSAR)

```python
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import json

class DSARHandler:
    """Handle Data Subject Access Requests."""

    RESPONSE_DEADLINE_DAYS = 30
    EXTENSION_ALLOWED_DAYS = 60  # For complex requests

    def __init__(self, data_sources: List['DataSource']):
        self.data_sources = data_sources

    async def submit_request(
        self,
        request_type: str,  # 'access', 'erasure', 'rectification', 'portability'
        user_id: str,
        verified: bool,
        details: Optional[Dict] = None
    ) -> str:
        """Submit a new DSAR."""
        request = {
            'id': self.generate_request_id(),
            'type': request_type,
            'user_id': user_id,
            'status': 'pending_verification' if not verified else 'processing',
            'submitted_at': datetime.utcnow(),
            'deadline': datetime.utcnow() + timedelta(days=self.RESPONSE_DEADLINE_DAYS),
            'details': details or {},
            'audit_log': [{
                'action': 'submitted',
                'timestamp': datetime.utcnow(),
                'details': 'Request received'
            }]
        }

        await self.db.dsar_requests.insert_one(request)
        await self.notify_dpo(request)

        return request['id']

    async def process_access_request(self, request_id: str) -> Dict:
        """Process a data access request."""
        request = await self.get_request(request_id)

        if request['type'] != 'access':
            raise ValueError("Not an access request")

        user_data = {}
        for source in self.data_sources:
            try:
                data = await source.get_user_data(request['user_id'])
                user_data[source.name] = data
            except Exception as e:
                user_data[source.name] = {'error': str(e)}

        response = {
            'request_id': request_id,
            'generated_at': datetime.utcnow().isoformat(),
            'data_categories': list(user_data.keys()),
            'data': user_data,
            'retention_info': await self.get_retention_info(),
            'processing_purposes': await self.get_processing_purposes(),
            'third_party_recipients': await self.get_recipients()
        }

        await self.update_request(request_id, 'completed', response)

        return response

    async def process_erasure_request(self, request_id: str) -> Dict:
        """Process a right to erasure request."""
        request = await self.get_request(request_id)

        if request['type'] != 'erasure':
            raise ValueError("Not an erasure request")

        results = {}
        exceptions = []

        for source in self.data_sources:
            try:
                can_delete, reason = await source.can_delete(request['user_id'])

                if can_delete:
                    await source.delete_user_data(request['user_id'])
                    results[source.name] = 'deleted'
                else:
                    exceptions.append({
                        'source': source.name,
                        'reason': reason
                    })
                    results[source.name] = f'retained: {reason}'
            except Exception as e:
                results[source.name] = f'error: {str(e)}'

        response = {
            'request_id': request_id,
            'completed_at': datetime.utcnow().isoformat(),
            'results': results,
            'exceptions': exceptions
        }

        await self.update_request(request_id, 'completed', response)

        return response

    async def process_portability_request(self, request_id: str) -> bytes:
        """Generate portable data export."""
        request = await self.get_request(request_id)
        user_data = await self.process_access_request(request_id)

        portable_data = {
            'export_date': datetime.utcnow().isoformat(),
            'format_version': '1.0',
            'data': user_data['data']
        }

        return json.dumps(portable_data, indent=2, default=str).encode()
```

## Data Retention, Privacy by Design & Breach Notification

Data retention policies (RetentionBasis enum with CONSENT/CONTRACT/LEGAL_OBLIGATION/LEGITIMATE_INTEREST; DataRetentionPolicy with POLICIES dict covering user_account/transaction_records/marketing_consent/support_tickets/analytics_data; apply_retention_policies enforcing cutoffs with archive-before-delete and anonymize_instead options), privacy-by-design data model (PrivacyFirstDataModel separating user_profile/user_pii/analytics schemas with pseudonymization; DataMinimization with REQUIRED_FIELDS per purpose and IP generalization), breach notification handler (BreachSeverity enum; BreachNotificationHandler with 72-hour authority notification deadline; requires_authority_notification checking sensitive data types; generate_authority_report for supervisory authorities), and a complete GDPR Implementation Checklist covering legal basis/transparency/data subject rights/security/breach response/documentation.

See [references/data-retention-privacy-breach.md](references/data-retention-privacy-breach.md)

## Best Practices

### Do's
- **Minimize data collection** - Only collect what's needed
- **Document everything** - Processing activities, legal bases
- **Encrypt PII** - At rest and in transit
- **Implement access controls** - Need-to-know basis
- **Regular audits** - Verify compliance continuously

### Don'ts
- **Don't pre-check consent boxes** - Must be opt-in
- **Don't bundle consent** - Separate purposes separately
- **Don't retain indefinitely** - Define and enforce retention
- **Don't ignore DSARs** - 30-day response required
- **Don't transfer without safeguards** - SCCs or adequacy decisions

## Resources

- [GDPR Full Text](https://gdpr-info.eu/)
- [ICO Guidance](https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/)
- [EDPB Guidelines](https://edpb.europa.eu/our-work-tools/general-guidance/gdpr-guidelines-recommendations-best-practices_en)

---

## Reference Files

| Resource | Purpose |
|----------|---------|
| `references/data-retention-privacy-breach.md` | Data retention policies, privacy-by-design model, breach notification, compliance checklist |
