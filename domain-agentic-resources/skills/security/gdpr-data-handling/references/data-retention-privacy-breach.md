# GDPR Data Handling — Data Retention, Privacy by Design & Breach Notification

## Pattern 3: Data Retention

```python
from datetime import datetime, timedelta
from enum import Enum

class RetentionBasis(Enum):
    CONSENT = "consent"
    CONTRACT = "contract"
    LEGAL_OBLIGATION = "legal_obligation"
    LEGITIMATE_INTEREST = "legitimate_interest"

class DataRetentionPolicy:
    """Define and enforce data retention policies."""

    POLICIES = {
        'user_account': {
            'retention_period_days': 365 * 3,  # 3 years after last activity
            'basis': RetentionBasis.CONTRACT,
            'trigger': 'last_activity_date',
            'archive_before_delete': True
        },
        'transaction_records': {
            'retention_period_days': 365 * 7,  # 7 years for tax
            'basis': RetentionBasis.LEGAL_OBLIGATION,
            'trigger': 'transaction_date',
            'archive_before_delete': True,
            'legal_reference': 'Tax regulations require 7 year retention'
        },
        'marketing_consent': {
            'retention_period_days': 365 * 2,  # 2 years
            'basis': RetentionBasis.CONSENT,
            'trigger': 'consent_date',
            'archive_before_delete': False
        },
        'support_tickets': {
            'retention_period_days': 365 * 2,
            'basis': RetentionBasis.LEGITIMATE_INTEREST,
            'trigger': 'ticket_closed_date',
            'archive_before_delete': True
        },
        'analytics_data': {
            'retention_period_days': 365,  # 1 year
            'basis': RetentionBasis.CONSENT,
            'trigger': 'collection_date',
            'archive_before_delete': False,
            'anonymize_instead': True
        }
    }

    async def apply_retention_policies(self):
        """Run retention policy enforcement."""
        for data_type, policy in self.POLICIES.items():
            cutoff_date = datetime.utcnow() - timedelta(
                days=policy['retention_period_days']
            )

            if policy.get('anonymize_instead'):
                await self.anonymize_old_data(data_type, cutoff_date)
            else:
                if policy.get('archive_before_delete'):
                    await self.archive_data(data_type, cutoff_date)
                await self.delete_old_data(data_type, cutoff_date)

            await self.log_retention_action(data_type, cutoff_date)

    async def anonymize_old_data(self, data_type: str, before_date: datetime):
        """Anonymize data instead of deleting."""
        if data_type == 'analytics_data':
            await self.db.analytics.update_many(
                {'collection_date': {'$lt': before_date}},
                {'$set': {
                    'user_id': None,
                    'ip_address': None,
                    'device_id': None,
                    'anonymized': True,
                    'anonymized_date': datetime.utcnow()
                }}
            )
```

---

## Pattern 4: Privacy by Design

```python
class PrivacyFirstDataModel:
    """Example of privacy-by-design data model."""

    # Separate PII from behavioral data
    user_profile_schema = {
        'user_id': str,  # UUID, not sequential
        'email_hash': str,  # Hashed for lookups
        'created_at': datetime,
        'preferences': {
            'language': str,
            'timezone': str
        }
    }

    # Encrypted at rest
    user_pii_schema = {
        'user_id': str,
        'email': str,  # Encrypted
        'name': str,   # Encrypted
        'phone': str,  # Encrypted (optional)
        'address': dict,  # Encrypted (optional)
        'encryption_key_id': str
    }

    # Pseudonymized behavioral data
    analytics_schema = {
        'session_id': str,  # Not linked to user_id
        'pseudonym_id': str,  # Rotating pseudonym
        'events': list,
        'device_category': str,  # Generalized, not specific
        'country': str,  # Not city-level
    }

class DataMinimization:
    """Implement data minimization principles."""

    @staticmethod
    def collect_only_needed(form_data: dict, purpose: str) -> dict:
        """Filter form data to only fields needed for purpose."""
        REQUIRED_FIELDS = {
            'account_creation': ['email', 'password'],
            'newsletter': ['email'],
            'purchase': ['email', 'name', 'address', 'payment'],
            'support': ['email', 'message']
        }

        allowed = REQUIRED_FIELDS.get(purpose, [])
        return {k: v for k, v in form_data.items() if k in allowed}

    @staticmethod
    def generalize_location(ip_address: str) -> str:
        """Generalize IP to country level only."""
        import geoip2.database
        reader = geoip2.database.Reader('GeoLite2-Country.mmdb')
        try:
            response = reader.country(ip_address)
            return response.country.iso_code
        except:
            return 'UNKNOWN'
```

---

## Pattern 5: Breach Notification

```python
from datetime import datetime
from enum import Enum

class BreachSeverity(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class BreachNotificationHandler:
    """Handle GDPR breach notification requirements."""

    AUTHORITY_NOTIFICATION_HOURS = 72
    AFFECTED_NOTIFICATION_REQUIRED_SEVERITY = BreachSeverity.HIGH

    async def report_breach(
        self,
        description: str,
        data_types: List[str],
        affected_count: int,
        severity: BreachSeverity
    ) -> dict:
        """Report and handle a data breach."""
        breach = {
            'id': self.generate_breach_id(),
            'reported_at': datetime.utcnow(),
            'description': description,
            'data_types_affected': data_types,
            'affected_individuals_count': affected_count,
            'severity': severity.value,
            'status': 'investigating',
            'timeline': [{
                'event': 'breach_reported',
                'timestamp': datetime.utcnow(),
                'details': description
            }]
        }

        await self.db.breaches.insert_one(breach)

        await self.notify_dpo(breach)
        await self.notify_security_team(breach)

        if self.requires_authority_notification(severity, data_types):
            breach['authority_notification_deadline'] = (
                datetime.utcnow() + timedelta(hours=self.AUTHORITY_NOTIFICATION_HOURS)
            )
            await self.schedule_authority_notification(breach)

        if severity.value in [BreachSeverity.HIGH.value, BreachSeverity.CRITICAL.value]:
            await self.schedule_individual_notifications(breach)

        return breach

    def requires_authority_notification(
        self,
        severity: BreachSeverity,
        data_types: List[str]
    ) -> bool:
        """Determine if supervisory authority must be notified."""
        sensitive_types = ['health', 'financial', 'credentials', 'biometric']
        if any(t in sensitive_types for t in data_types):
            return True

        return severity in [BreachSeverity.MEDIUM, BreachSeverity.HIGH, BreachSeverity.CRITICAL]

    async def generate_authority_report(self, breach_id: str) -> dict:
        """Generate report for supervisory authority."""
        breach = await self.get_breach(breach_id)

        return {
            'organization': {
                'name': self.config.org_name,
                'contact': self.config.dpo_contact,
                'registration': self.config.registration_number
            },
            'breach': {
                'nature': breach['description'],
                'categories_affected': breach['data_types_affected'],
                'approximate_number_affected': breach['affected_individuals_count'],
                'likely_consequences': self.assess_consequences(breach),
                'measures_taken': await self.get_remediation_measures(breach_id),
                'measures_proposed': await self.get_proposed_measures(breach_id)
            },
            'timeline': breach['timeline'],
            'submitted_at': datetime.utcnow().isoformat()
        }
```

---

## Compliance Checklist

```markdown
## GDPR Implementation Checklist

### Legal Basis
- [ ] Documented legal basis for each processing activity
- [ ] Consent mechanisms meet GDPR requirements
- [ ] Legitimate interest assessments completed

### Transparency
- [ ] Privacy policy is clear and accessible
- [ ] Processing purposes clearly stated
- [ ] Data retention periods documented

### Data Subject Rights
- [ ] Access request process implemented
- [ ] Erasure request process implemented
- [ ] Portability export available
- [ ] Rectification process available
- [ ] Response within 30-day deadline

### Security
- [ ] Encryption at rest implemented
- [ ] Encryption in transit (TLS)
- [ ] Access controls in place
- [ ] Audit logging enabled

### Breach Response
- [ ] Breach detection mechanisms
- [ ] 72-hour notification process
- [ ] Breach documentation system

### Documentation
- [ ] Records of processing activities (Art. 30)
- [ ] Data protection impact assessments
- [ ] Data processing agreements with vendors
```
