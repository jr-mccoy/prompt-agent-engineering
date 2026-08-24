# Data Quality Frameworks — Data Contracts and Automated Pipeline

## Pattern 5: Data Contracts

```yaml
# contracts/orders_contract.yaml
apiVersion: datacontract.com/v1.0.0
kind: DataContract
metadata:
  name: orders
  version: 1.0.0
  owner: data-platform-team
  contact: data-team@company.com

info:
  title: Orders Data Contract
  description: Contract for order event data from the ecommerce platform
  purpose: Analytics, reporting, and ML features

servers:
  production:
    type: snowflake
    account: company.us-east-1
    database: ANALYTICS
    schema: CORE

terms:
  usage: Internal analytics only
  limitations: PII must not be exposed in downstream marts
  billing: Charged per query TB scanned

schema:
  type: object
  properties:
    order_id:
      type: string
      format: uuid
      description: Unique order identifier
      required: true
      unique: true
      pii: false

    customer_id:
      type: string
      format: uuid
      description: Customer identifier
      required: true
      pii: true
      piiClassification: indirect

    total_amount:
      type: number
      minimum: 0
      maximum: 100000
      description: Order total in USD

    created_at:
      type: string
      format: date-time
      description: Order creation timestamp
      required: true

    status:
      type: string
      enum: [pending, processing, shipped, delivered, cancelled]
      description: Current order status

quality:
  type: SodaCL
  specification:
    checks for orders:
      - row_count > 0
      - missing_count(order_id) = 0
      - duplicate_count(order_id) = 0
      - invalid_count(status) = 0:
          valid values: [pending, processing, shipped, delivered, cancelled]
      - freshness(created_at) < 24h

sla:
  availability: 99.9%
  freshness: 1 hour
  latency: 5 minutes
```

---

## Pattern 6: Automated Quality Pipeline

```python
# quality_pipeline.py
from dataclasses import dataclass
from typing import List, Dict, Any
import great_expectations as gx
from datetime import datetime

@dataclass
class QualityResult:
    table: str
    passed: bool
    total_expectations: int
    failed_expectations: int
    details: List[Dict[str, Any]]
    timestamp: datetime

class DataQualityPipeline:
    """Orchestrate data quality checks across tables"""

    def __init__(self, context: gx.DataContext):
        self.context = context
        self.results: List[QualityResult] = []

    def validate_table(self, table: str, suite: str) -> QualityResult:
        """Validate a single table against expectation suite"""

        checkpoint_config = {
            "name": f"{table}_validation",
            "config_version": 1.0,
            "class_name": "Checkpoint",
            "validations": [{
                "batch_request": {
                    "datasource_name": "warehouse",
                    "data_asset_name": table,
                },
                "expectation_suite_name": suite,
            }],
        }

        result = self.context.run_checkpoint(**checkpoint_config)

        # Parse results
        validation_result = list(result.run_results.values())[0]
        results = validation_result.results

        failed = [r for r in results if not r.success]

        return QualityResult(
            table=table,
            passed=result.success,
            total_expectations=len(results),
            failed_expectations=len(failed),
            details=[{
                "expectation": r.expectation_config.expectation_type,
                "success": r.success,
                "observed_value": r.result.get("observed_value"),
            } for r in results],
            timestamp=datetime.now()
        )

    def run_all(self, tables: Dict[str, str]) -> Dict[str, QualityResult]:
        """Run validation for all tables"""
        results = {}

        for table, suite in tables.items():
            print(f"Validating {table}...")
            results[table] = self.validate_table(table, suite)

        return results

    def generate_report(self, results: Dict[str, QualityResult]) -> str:
        """Generate quality report"""
        report = ["# Data Quality Report", f"Generated: {datetime.now()}", ""]

        total_passed = sum(1 for r in results.values() if r.passed)
        total_tables = len(results)

        report.append(f"## Summary: {total_passed}/{total_tables} tables passed")
        report.append("")

        for table, result in results.items():
            status = "✅" if result.passed else "❌"
            report.append(f"### {status} {table}")
            report.append(f"- Expectations: {result.total_expectations}")
            report.append(f"- Failed: {result.failed_expectations}")

            if not result.passed:
                report.append("- Failed checks:")
                for detail in result.details:
                    if not detail["success"]:
                        report.append(f"  - {detail['expectation']}: {detail['observed_value']}")
            report.append("")

        return "\n".join(report)

# Usage
context = gx.get_context()
pipeline = DataQualityPipeline(context)

tables_to_validate = {
    "orders": "orders_suite",
    "customers": "customers_suite",
    "products": "products_suite",
}

results = pipeline.run_all(tables_to_validate)
report = pipeline.generate_report(results)

# Fail pipeline if any table failed
if not all(r.passed for r in results.values()):
    print(report)
    raise ValueError("Data quality checks failed!")
```

---

## Best Practices

### Do's
- **Test early** - Validate source data before transformations
- **Test incrementally** - Add tests as you find issues
- **Document expectations** - Clear descriptions for each test
- **Alert on failures** - Integrate with monitoring
- **Version contracts** - Track schema changes

### Don'ts
- **Don't test everything** - Focus on critical columns
- **Don't ignore warnings** - They often precede failures
- **Don't skip freshness** - Stale data is bad data
- **Don't hardcode thresholds** - Use dynamic baselines
- **Don't test in isolation** - Test relationships too

## Resources

- [Great Expectations Documentation](https://docs.greatexpectations.io/)
- [dbt Testing Documentation](https://docs.getdbt.com/docs/build/tests)
- [Data Contract Specification](https://datacontract.com/)
- [Soda Core](https://docs.soda.io/soda-core/overview.html)
