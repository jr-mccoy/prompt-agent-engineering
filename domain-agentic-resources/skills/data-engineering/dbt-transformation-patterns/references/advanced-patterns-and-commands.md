# dbt Transformation Patterns — Advanced Patterns and Commands

## Pattern 5: Testing and Documentation

```yaml
# models/marts/core/_core__models.yml
version: 2

models:
  - name: dim_customers
    description: Customer dimension with payment and order metrics
    columns:
      - name: customer_key
        description: Surrogate key for the customer dimension
        tests:
          - unique
          - not_null

      - name: customer_id
        description: Natural key from source system
        tests:
          - unique
          - not_null

      - name: email
        description: Customer email address
        tests:
          - not_null

      - name: customer_tier
        description: Customer value tier based on lifetime value
        tests:
          - accepted_values:
              values: ['high', 'medium', 'low']

      - name: lifetime_value
        description: Total amount paid by customer
        tests:
          - dbt_utils.expression_is_true:
              expression: ">= 0"

  - name: fct_orders
    description: Order fact table with all order transactions
    tests:
      - dbt_utils.recency:
          datepart: day
          field: created_at
          interval: 1
    columns:
      - name: order_id
        tests:
          - unique
          - not_null
      - name: customer_key
        tests:
          - not_null
          - relationships:
              to: ref('dim_customers')
              field: customer_key
```

## Pattern 6: Macros and DRY Code

```sql
-- macros/cents_to_dollars.sql
{% macro cents_to_dollars(column_name, precision=2) %}
    round({{ column_name }} / 100.0, {{ precision }})
{% endmacro %}

-- macros/generate_schema_name.sql
{% macro generate_schema_name(custom_schema_name, node) %}
    {%- set default_schema = target.schema -%}
    {%- if custom_schema_name is none -%}
        {{ default_schema }}
    {%- else -%}
        {{ default_schema }}_{{ custom_schema_name }}
    {%- endif -%}
{% endmacro %}

-- macros/limit_data_in_dev.sql
{% macro limit_data_in_dev(column_name, days=3) %}
    {% if target.name == 'dev' %}
        where {{ column_name }} >= dateadd(day, -{{ days }}, current_date)
    {% endif %}
{% endmacro %}

-- Usage in model
select * from {{ ref('stg_orders') }}
{{ limit_data_in_dev('created_at') }}
```

## Pattern 7: Incremental Strategies

```sql
-- Delete+Insert (default for most warehouses)
{{
    config(
        materialized='incremental',
        unique_key='id',
        incremental_strategy='delete+insert'
    )
}}

-- Merge (best for late-arriving data)
{{
    config(
        materialized='incremental',
        unique_key='id',
        incremental_strategy='merge',
        merge_update_columns=['status', 'amount', 'updated_at']
    )
}}

-- Insert Overwrite (partition-based)
{{
    config(
        materialized='incremental',
        incremental_strategy='insert_overwrite',
        partition_by={
            "field": "created_date",
            "data_type": "date",
            "granularity": "day"
        }
    )
}}

select
    *,
    date(created_at) as created_date
from {{ ref('stg_events') }}

{% if is_incremental() %}
where created_date >= dateadd(day, -3, current_date)
{% endif %}
```

---

## dbt Commands

```bash
# Development
dbt run                          # Run all models
dbt run --select staging         # Run staging models only
dbt run --select +fct_orders     # Run fct_orders and its upstream
dbt run --select fct_orders+     # Run fct_orders and its downstream
dbt run --full-refresh           # Rebuild incremental models

# Testing
dbt test                         # Run all tests
dbt test --select stg_stripe     # Test specific models
dbt build                        # Run + test in DAG order

# Documentation
dbt docs generate                # Generate docs
dbt docs serve                   # Serve docs locally

# Debugging
dbt compile                      # Compile SQL without running
dbt debug                        # Test connection
dbt ls --select tag:critical     # List models by tag
```
