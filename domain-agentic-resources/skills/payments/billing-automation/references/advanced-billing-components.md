# Billing Automation — Advanced Billing Components

## Proration

```python
class ProrationCalculator:
    """Calculate prorated charges for plan changes."""

    @staticmethod
    def calculate_proration(old_plan, new_plan, period_start, period_end, change_date):
        """Calculate proration for plan change."""
        # Days in current period
        total_days = (period_end - period_start).days

        # Days used on old plan
        days_used = (change_date - period_start).days

        # Days remaining on new plan
        days_remaining = (period_end - change_date).days

        # Calculate prorated amounts
        unused_amount = (old_plan.amount / total_days) * days_remaining
        new_plan_amount = (new_plan.amount / total_days) * days_remaining

        # Net charge/credit
        proration = new_plan_amount - unused_amount

        return {
            'old_plan_credit': -unused_amount,
            'new_plan_charge': new_plan_amount,
            'net_proration': proration,
            'days_used': days_used,
            'days_remaining': days_remaining
        }

    @staticmethod
    def calculate_seat_proration(current_seats, new_seats, price_per_seat, period_start, period_end, change_date):
        """Calculate proration for seat changes."""
        total_days = (period_end - period_start).days
        days_remaining = (period_end - change_date).days

        # Additional seats charge
        additional_seats = new_seats - current_seats
        prorated_amount = (additional_seats * price_per_seat / total_days) * days_remaining

        return {
            'additional_seats': additional_seats,
            'prorated_charge': max(0, prorated_amount),  # No refund for removing seats mid-cycle
            'effective_date': change_date
        }
```

## Tax Calculation

```python
class TaxCalculator:
    """Calculate sales tax, VAT, GST."""

    def __init__(self):
        # Tax rates by region
        self.tax_rates = {
            'US_CA': 0.0725,  # California sales tax
            'US_NY': 0.04,    # New York sales tax
            'GB': 0.20,       # UK VAT
            'DE': 0.19,       # Germany VAT
            'FR': 0.20,       # France VAT
            'AU': 0.10,       # Australia GST
        }

    def calculate_tax(self, amount, customer):
        """Calculate applicable tax."""
        # Determine tax jurisdiction
        jurisdiction = self.get_tax_jurisdiction(customer)

        if not jurisdiction:
            return 0

        # Get tax rate
        tax_rate = self.tax_rates.get(jurisdiction, 0)

        # Calculate tax
        tax = amount * tax_rate

        return {
            'tax_amount': tax,
            'tax_rate': tax_rate,
            'jurisdiction': jurisdiction,
            'tax_type': self.get_tax_type(jurisdiction)
        }

    def get_tax_jurisdiction(self, customer):
        """Determine tax jurisdiction based on customer location."""
        if customer.country == 'US':
            # US: Tax based on customer state
            return f"US_{customer.state}"
        elif customer.country in ['GB', 'DE', 'FR']:
            # EU: VAT
            return customer.country
        elif customer.country == 'AU':
            # Australia: GST
            return 'AU'
        else:
            return None

    def get_tax_type(self, jurisdiction):
        """Get type of tax for jurisdiction."""
        if jurisdiction.startswith('US_'):
            return 'Sales Tax'
        elif jurisdiction in ['GB', 'DE', 'FR']:
            return 'VAT'
        elif jurisdiction == 'AU':
            return 'GST'
        return 'Tax'

    def validate_vat_number(self, vat_number, country):
        """Validate EU VAT number."""
        # Use VIES API for validation
        # Returns True if valid, False otherwise
        pass
```

## Invoice Generation

```python
class Invoice:
    def __init__(self, customer_id, subscription_id=None):
        self.id = generate_invoice_number()
        self.customer_id = customer_id
        self.subscription_id = subscription_id
        self.status = 'draft'
        self.line_items = []
        self.subtotal = 0
        self.tax = 0
        self.total = 0
        self.created_at = datetime.now()

    def add_line_item(self, description, amount, quantity=1):
        """Add line item to invoice."""
        line_item = {
            'description': description,
            'unit_amount': amount,
            'quantity': quantity,
            'total': amount * quantity
        }
        self.line_items.append(line_item)
        self.subtotal += line_item['total']

    def finalize(self):
        """Finalize invoice and calculate total."""
        self.total = self.subtotal + self.tax
        self.status = 'open'
        self.finalized_at = datetime.now()

    def mark_paid(self):
        """Mark invoice as paid."""
        self.status = 'paid'
        self.paid_at = datetime.now()

    def to_pdf(self):
        """Generate PDF invoice."""
        from reportlab.pdfgen import canvas

        # Generate PDF
        # Include: company info, customer info, line items, tax, total
        pass

    def to_html(self):
        """Generate HTML invoice."""
        template = """
        <!DOCTYPE html>
        <html>
        <head><title>Invoice #{invoice_number}</title></head>
        <body>
            <h1>Invoice #{invoice_number}</h1>
            <p>Date: {date}</p>
            <h2>Bill To:</h2>
            <p>{customer_name}<br>{customer_address}</p>
            <table>
                <tr><th>Description</th><th>Quantity</th><th>Amount</th></tr>
                {line_items}
            </table>
            <p>Subtotal: ${subtotal}</p>
            <p>Tax: ${tax}</p>
            <h3>Total: ${total}</h3>
        </body>
        </html>
        """

        return template.format(
            invoice_number=self.id,
            date=self.created_at.strftime('%Y-%m-%d'),
            customer_name=self.customer.name,
            customer_address=self.customer.address,
            line_items=self.render_line_items(),
            subtotal=self.subtotal,
            tax=self.tax,
            total=self.total
        )
```

## Usage-Based Billing

```python
class UsageBillingEngine:
    """Track and bill for usage."""

    def track_usage(self, customer_id, metric, quantity):
        """Track usage event."""
        UsageRecord.create(
            customer_id=customer_id,
            metric=metric,
            quantity=quantity,
            timestamp=datetime.now()
        )

    def calculate_usage_charges(self, subscription, period_start, period_end):
        """Calculate charges for usage in billing period."""
        usage_records = UsageRecord.get_for_period(
            subscription.customer_id,
            period_start,
            period_end
        )

        total_usage = sum(record.quantity for record in usage_records)

        # Tiered pricing
        if subscription.plan.pricing_model == 'tiered':
            charge = self.calculate_tiered_pricing(total_usage, subscription.plan.tiers)
        # Per-unit pricing
        elif subscription.plan.pricing_model == 'per_unit':
            charge = total_usage * subscription.plan.unit_price
        # Volume pricing
        elif subscription.plan.pricing_model == 'volume':
            charge = self.calculate_volume_pricing(total_usage, subscription.plan.tiers)

        return charge

    def calculate_tiered_pricing(self, total_usage, tiers):
        """Calculate cost using tiered pricing."""
        charge = 0
        remaining = total_usage

        for tier in sorted(tiers, key=lambda x: x['up_to']):
            tier_usage = min(remaining, tier['up_to'] - tier['from'])
            charge += tier_usage * tier['unit_price']
            remaining -= tier_usage

            if remaining <= 0:
                break

        return charge
```
