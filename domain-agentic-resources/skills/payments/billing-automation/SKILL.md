---
name: billing-automation
description: Build automated billing systems for recurring payments, invoicing, subscription lifecycle, and dunning management. Use when implementing subscription billing, automating invoicing, or managing recurring payment systems.
metadata:
  tags:
    - automation
    - billing
    - fintech
    - payments
  updated: "2026-04-11"
---
# Billing Automation

Master automated billing systems including recurring billing, invoice generation, dunning management, proration, and tax calculation.

## When to Use This Skill

- Implementing SaaS subscription billing
- Automating invoice generation and delivery
- Managing failed payment recovery (dunning)
- Calculating prorated charges for plan changes
- Handling sales tax, VAT, and GST
- Processing usage-based billing
- Managing billing cycles and renewals

## Core Concepts

### 1. Billing Cycles
**Common Intervals:**
- Monthly (most common for SaaS)
- Annual (discounted long-term)
- Quarterly
- Weekly
- Custom (usage-based, per-seat)

### 2. Subscription States
```
trial → active → past_due → canceled
              → paused → resumed
```

### 3. Dunning Management
Automated process to recover failed payments through:
- Retry schedules
- Customer notifications
- Grace periods
- Account restrictions

### 4. Proration
Adjusting charges when:
- Upgrading/downgrading mid-cycle
- Adding/removing seats
- Changing billing frequency

## Quick Start

```python
from billing import BillingEngine, Subscription

# Initialize billing engine
billing = BillingEngine()

# Create subscription
subscription = billing.create_subscription(
    customer_id="cus_123",
    plan_id="plan_pro_monthly",
    billing_cycle_anchor=datetime.now(),
    trial_days=14
)

# Process billing cycle
billing.process_billing_cycle(subscription.id)
```

## Subscription Lifecycle Management

```python
from datetime import datetime, timedelta
from enum import Enum

class SubscriptionStatus(Enum):
    TRIAL = "trial"
    ACTIVE = "active"
    PAST_DUE = "past_due"
    CANCELED = "canceled"
    PAUSED = "paused"

class Subscription:
    def __init__(self, customer_id, plan, billing_cycle_day=None):
        self.id = generate_id()
        self.customer_id = customer_id
        self.plan = plan
        self.status = SubscriptionStatus.TRIAL
        self.current_period_start = datetime.now()
        self.current_period_end = self.current_period_start + timedelta(days=plan.trial_days or 30)
        self.billing_cycle_day = billing_cycle_day or self.current_period_start.day
        self.trial_end = datetime.now() + timedelta(days=plan.trial_days) if plan.trial_days else None

    def start_trial(self, trial_days):
        """Start trial period."""
        self.status = SubscriptionStatus.TRIAL
        self.trial_end = datetime.now() + timedelta(days=trial_days)
        self.current_period_end = self.trial_end

    def activate(self):
        """Activate subscription after trial or immediately."""
        self.status = SubscriptionStatus.ACTIVE
        self.current_period_start = datetime.now()
        self.current_period_end = self.calculate_next_billing_date()

    def mark_past_due(self):
        """Mark subscription as past due after failed payment."""
        self.status = SubscriptionStatus.PAST_DUE
        # Trigger dunning workflow

    def cancel(self, at_period_end=True):
        """Cancel subscription."""
        if at_period_end:
            self.cancel_at_period_end = True
            # Will cancel when current period ends
        else:
            self.status = SubscriptionStatus.CANCELED
            self.canceled_at = datetime.now()

    def calculate_next_billing_date(self):
        """Calculate next billing date based on interval."""
        if self.plan.interval == 'month':
            return self.current_period_start + timedelta(days=30)
        elif self.plan.interval == 'year':
            return self.current_period_start + timedelta(days=365)
        elif self.plan.interval == 'week':
            return self.current_period_start + timedelta(days=7)
```

## Billing Cycle Processing

```python
class BillingEngine:
    def process_billing_cycle(self, subscription_id):
        """Process billing for a subscription."""
        subscription = self.get_subscription(subscription_id)

        # Check if billing is due
        if datetime.now() < subscription.current_period_end:
            return

        # Generate invoice
        invoice = self.generate_invoice(subscription)

        # Attempt payment
        payment_result = self.charge_customer(
            subscription.customer_id,
            invoice.total
        )

        if payment_result.success:
            # Payment successful
            invoice.mark_paid()
            subscription.advance_billing_period()
            self.send_invoice(invoice)
        else:
            # Payment failed
            subscription.mark_past_due()
            self.start_dunning_process(subscription, invoice)

    def generate_invoice(self, subscription):
        """Generate invoice for billing period."""
        invoice = Invoice(
            customer_id=subscription.customer_id,
            subscription_id=subscription.id,
            period_start=subscription.current_period_start,
            period_end=subscription.current_period_end
        )

        # Add subscription line item
        invoice.add_line_item(
            description=subscription.plan.name,
            amount=subscription.plan.amount,
            quantity=subscription.quantity or 1
        )

        # Add usage-based charges if applicable
        if subscription.has_usage_billing:
            usage_charges = self.calculate_usage_charges(subscription)
            invoice.add_line_item(
                description="Usage charges",
                amount=usage_charges
            )

        # Calculate tax
        tax = self.calculate_tax(invoice.subtotal, subscription.customer)
        invoice.tax = tax

        invoice.finalize()
        return invoice

    def charge_customer(self, customer_id, amount):
        """Charge customer using saved payment method."""
        customer = self.get_customer(customer_id)

        try:
            # Charge using payment processor
            charge = stripe.Charge.create(
                customer=customer.stripe_id,
                amount=int(amount * 100),  # Convert to cents
                currency='usd'
            )

            return PaymentResult(success=True, transaction_id=charge.id)
        except stripe.error.CardError as e:
            return PaymentResult(success=False, error=str(e))
```

## Dunning Management

```python
class DunningManager:
    """Manage failed payment recovery."""

    def __init__(self):
        self.retry_schedule = [
            {'days': 3, 'email_template': 'payment_failed_first'},
            {'days': 7, 'email_template': 'payment_failed_reminder'},
            {'days': 14, 'email_template': 'payment_failed_final'}
        ]

    def start_dunning_process(self, subscription, invoice):
        """Start dunning process for failed payment."""
        dunning_attempt = DunningAttempt(
            subscription_id=subscription.id,
            invoice_id=invoice.id,
            attempt_number=1,
            next_retry=datetime.now() + timedelta(days=3)
        )

        # Send initial failure notification
        self.send_dunning_email(subscription, 'payment_failed_first')

        # Schedule retries
        self.schedule_retries(dunning_attempt)

    def retry_payment(self, dunning_attempt):
        """Retry failed payment."""
        subscription = self.get_subscription(dunning_attempt.subscription_id)
        invoice = self.get_invoice(dunning_attempt.invoice_id)

        # Attempt payment again
        result = self.charge_customer(subscription.customer_id, invoice.total)

        if result.success:
            # Payment succeeded
            invoice.mark_paid()
            subscription.status = SubscriptionStatus.ACTIVE
            self.send_dunning_email(subscription, 'payment_recovered')
            dunning_attempt.mark_resolved()
        else:
            # Still failing
            dunning_attempt.attempt_number += 1

            if dunning_attempt.attempt_number < len(self.retry_schedule):
                # Schedule next retry
                next_retry_config = self.retry_schedule[dunning_attempt.attempt_number]
                dunning_attempt.next_retry = datetime.now() + timedelta(days=next_retry_config['days'])
                self.send_dunning_email(subscription, next_retry_config['email_template'])
            else:
                # Exhausted retries, cancel subscription
                subscription.cancel(at_period_end=False)
                self.send_dunning_email(subscription, 'subscription_canceled')

    def send_dunning_email(self, subscription, template):
        """Send dunning notification to customer."""
        customer = self.get_customer(subscription.customer_id)

        email_content = self.render_template(template, {
            'customer_name': customer.name,
            'amount_due': subscription.plan.amount,
            'update_payment_url': f"https://app.example.com/billing"
        })

        send_email(
            to=customer.email,
            subject=email_content['subject'],
            body=email_content['body']
        )
```

## Advanced Billing Components

Proration (`ProrationCalculator` with `calculate_proration` and `calculate_seat_proration`), Tax Calculation (`TaxCalculator` with regional rates for US/UK/EU/AU and VAT validation), Invoice Generation (`Invoice` class with `add_line_item`, `finalize`, `mark_paid`, `to_pdf`, `to_html`), and Usage-Based Billing (`UsageBillingEngine` with `track_usage`, `calculate_usage_charges`, tiered/per-unit/volume pricing models) are in the reference file.

See [references/advanced-billing-components.md](references/advanced-billing-components.md)

## Resources

- **references/billing-cycles.md**: Billing cycle management
- **references/dunning-management.md**: Failed payment recovery
- **references/proration.md**: Prorated charge calculations
- **references/tax-calculation.md**: Tax/VAT/GST handling
- **references/invoice-lifecycle.md**: Invoice state management
- **assets/billing-state-machine.yaml**: Billing workflow
- **assets/invoice-template.html**: Invoice templates
- **assets/dunning-policy.yaml**: Dunning configuration

## Best Practices

1. **Automate Everything**: Minimize manual intervention
2. **Clear Communication**: Notify customers of billing events
3. **Flexible Retry Logic**: Balance recovery with customer experience
4. **Accurate Proration**: Fair calculation for plan changes
5. **Tax Compliance**: Calculate correct tax for jurisdiction
6. **Audit Trail**: Log all billing events
7. **Graceful Degradation**: Handle edge cases without breaking

## Common Pitfalls

- **Incorrect Proration**: Not accounting for partial periods
- **Missing Tax**: Forgetting to add tax to invoices
- **Aggressive Dunning**: Canceling too quickly
- **No Notifications**: Not informing customers of failures
- **Hardcoded Cycles**: Not supporting custom billing dates

---

## Reference Files

| Resource | Purpose |
|----------|---------|
| `references/advanced-billing-components.md` | Proration (plan + seat), Tax Calculation (US/EU/AU with VAT validation), Invoice Generation (PDF + HTML), Usage-Based Billing (tiered/per-unit/volume pricing) |
