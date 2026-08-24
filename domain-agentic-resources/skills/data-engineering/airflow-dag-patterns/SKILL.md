---
name: airflow-dag-patterns
description: Build production Apache Airflow DAGs with best practices for operators, sensors, testing, and deployment. Use when creating data pipelines, orchestrating workflows, or scheduling batch jobs.
metadata:
  tags:
    - airflow
    - dag
    - data-engineering
    - deployment
    - testing
  updated: "2026-04-11"
---
# Apache Airflow DAG Patterns

Production-ready patterns for Apache Airflow including DAG design, operators, sensors, testing, and deployment strategies.

## When to Use This Skill

- Creating data pipeline orchestration with Airflow
- Designing DAG structures and dependencies
- Implementing custom operators and sensors
- Testing Airflow DAGs locally
- Setting up Airflow in production
- Debugging failed DAG runs

## Core Concepts

### 1. DAG Design Principles

| Principle | Description |
|-----------|-------------|
| **Idempotent** | Running twice produces same result |
| **Atomic** | Tasks succeed or fail completely |
| **Incremental** | Process only new/changed data |
| **Observable** | Logs, metrics, alerts at every step |

### 2. Task Dependencies

```python
# Linear
task1 >> task2 >> task3

# Fan-out
task1 >> [task2, task3, task4]

# Fan-in
[task1, task2, task3] >> task4

# Complex
task1 >> task2 >> task4
task1 >> task3 >> task4
```

## Quick Start

```python
# dags/example_dag.py
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator

default_args = {
    'owner': 'data-team',
    'depends_on_past': False,
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'retry_exponential_backoff': True,
    'max_retry_delay': timedelta(hours=1),
}

with DAG(
    dag_id='example_etl',
    default_args=default_args,
    description='Example ETL pipeline',
    schedule='0 6 * * *',  # Daily at 6 AM
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['etl', 'example'],
    max_active_runs=1,
) as dag:

    start = EmptyOperator(task_id='start')

    def extract_data(**context):
        execution_date = context['ds']
        # Extract logic here
        return {'records': 1000}

    extract = PythonOperator(
        task_id='extract',
        python_callable=extract_data,
    )

    end = EmptyOperator(task_id='end')

    start >> extract >> end
```

## Patterns

### Pattern 1: TaskFlow API (Airflow 2.0+)

```python
# dags/taskflow_example.py
from datetime import datetime
from airflow.decorators import dag, task
from airflow.models import Variable

@dag(
    dag_id='taskflow_etl',
    schedule='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['etl', 'taskflow'],
)
def taskflow_etl():
    """ETL pipeline using TaskFlow API"""

    @task()
    def extract(source: str) -> dict:
        """Extract data from source"""
        import pandas as pd

        df = pd.read_csv(f's3://bucket/{source}/{{ ds }}.csv')
        return {'data': df.to_dict(), 'rows': len(df)}

    @task()
    def transform(extracted: dict) -> dict:
        """Transform extracted data"""
        import pandas as pd

        df = pd.DataFrame(extracted['data'])
        df['processed_at'] = datetime.now()
        df = df.dropna()
        return {'data': df.to_dict(), 'rows': len(df)}

    @task()
    def load(transformed: dict, target: str):
        """Load data to target"""
        import pandas as pd

        df = pd.DataFrame(transformed['data'])
        df.to_parquet(f's3://bucket/{target}/{{ ds }}.parquet')
        return transformed['rows']

    @task()
    def notify(rows_loaded: int):
        """Send notification"""
        print(f'Loaded {rows_loaded} rows')

    # Define dependencies with XCom passing
    extracted = extract(source='raw_data')
    transformed = transform(extracted)
    loaded = load(transformed, target='processed_data')
    notify(loaded)

# Instantiate the DAG
taskflow_etl()
```

### Pattern 2: Dynamic DAG Generation

```python
# dags/dynamic_dag_factory.py
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable
import json

# Configuration for multiple similar pipelines
PIPELINE_CONFIGS = [
    {'name': 'customers', 'schedule': '@daily', 'source': 's3://raw/customers'},
    {'name': 'orders', 'schedule': '@hourly', 'source': 's3://raw/orders'},
    {'name': 'products', 'schedule': '@weekly', 'source': 's3://raw/products'},
]

def create_dag(config: dict) -> DAG:
    """Factory function to create DAGs from config"""

    dag_id = f"etl_{config['name']}"

    default_args = {
        'owner': 'data-team',
        'retries': 3,
        'retry_delay': timedelta(minutes=5),
    }

    dag = DAG(
        dag_id=dag_id,
        default_args=default_args,
        schedule=config['schedule'],
        start_date=datetime(2024, 1, 1),
        catchup=False,
        tags=['etl', 'dynamic', config['name']],
    )

    with dag:
        def extract_fn(source, **context):
            print(f"Extracting from {source} for {context['ds']}")

        def transform_fn(**context):
            print(f"Transforming data for {context['ds']}")

        def load_fn(table_name, **context):
            print(f"Loading to {table_name} for {context['ds']}")

        extract = PythonOperator(
            task_id='extract',
            python_callable=extract_fn,
            op_kwargs={'source': config['source']},
        )

        transform = PythonOperator(
            task_id='transform',
            python_callable=transform_fn,
        )

        load = PythonOperator(
            task_id='load',
            python_callable=load_fn,
            op_kwargs={'table_name': config['name']},
        )

        extract >> transform >> load

    return dag

# Generate DAGs
for config in PIPELINE_CONFIGS:
    globals()[f"dag_{config['name']}"] = create_dag(config)
```

### Pattern 3: Branching and Conditional Logic

```python
# dags/branching_example.py
from airflow.decorators import dag, task
from airflow.operators.python import BranchPythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.utils.trigger_rule import TriggerRule

@dag(
    dag_id='branching_pipeline',
    schedule='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
)
def branching_pipeline():

    @task()
    def check_data_quality() -> dict:
        """Check data quality and return metrics"""
        quality_score = 0.95  # Simulated
        return {'score': quality_score, 'rows': 10000}

    def choose_branch(**context) -> str:
        """Determine which branch to execute"""
        ti = context['ti']
        metrics = ti.xcom_pull(task_ids='check_data_quality')

        if metrics['score'] >= 0.9:
            return 'high_quality_path'
        elif metrics['score'] >= 0.7:
            return 'medium_quality_path'
        else:
            return 'low_quality_path'

    quality_check = check_data_quality()

    branch = BranchPythonOperator(
        task_id='branch',
        python_callable=choose_branch,
    )

    high_quality = EmptyOperator(task_id='high_quality_path')
    medium_quality = EmptyOperator(task_id='medium_quality_path')
    low_quality = EmptyOperator(task_id='low_quality_path')

    # Join point - runs after any branch completes
    join = EmptyOperator(
        task_id='join',
        trigger_rule=TriggerRule.NONE_FAILED_MIN_ONE_SUCCESS,
    )

    quality_check >> branch >> [high_quality, medium_quality, low_quality] >> join

branching_pipeline()
```

---

Patterns 4–6 (Sensors and External Dependencies, Error Handling and Alerts, Testing DAGs) and the recommended Project Structure are in the reference file.

See [references/advanced-patterns-and-project-structure.md](references/advanced-patterns-and-project-structure.md)

---

## Best Practices

### Do's
- **Use TaskFlow API** - Cleaner code, automatic XCom
- **Set timeouts** - Prevent zombie tasks
- **Use `mode='reschedule'`** - For sensors, free up workers
- **Test DAGs** - Unit tests and integration tests
- **Idempotent tasks** - Safe to retry

### Don'ts
- **Don't use `depends_on_past=True`** - Creates bottlenecks
- **Don't hardcode dates** - Use `{{ ds }}` macros
- **Don't use global state** - Tasks should be stateless
- **Don't skip catchup blindly** - Understand implications
- **Don't put heavy logic in DAG file** - Import from modules

## Resources

- [Airflow Documentation](https://airflow.apache.org/docs/)
- [Astronomer Guides](https://docs.astronomer.io/learn)
- [TaskFlow API](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/taskflow.html)

## Reference Files

| Resource | Purpose |
|----------|---------|
| `references/advanced-patterns-and-project-structure.md` | Pattern 4 (Sensors/ExternalTaskSensor/custom sensor), Pattern 5 (Error Handling callbacks/trigger rules), Pattern 6 (Testing DAGs with DagBag/pytest), and recommended project directory structure |
