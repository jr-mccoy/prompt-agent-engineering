# Airflow DAG Patterns — Advanced Patterns and Project Structure

## Pattern 4: Sensors and External Dependencies

```python
# dags/sensor_patterns.py
from datetime import datetime, timedelta
from airflow import DAG
from airflow.sensors.filesystem import FileSensor
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor
from airflow.sensors.external_task import ExternalTaskSensor
from airflow.operators.python import PythonOperator

with DAG(
    dag_id='sensor_example',
    schedule='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    # Wait for file on S3
    wait_for_file = S3KeySensor(
        task_id='wait_for_s3_file',
        bucket_name='data-lake',
        bucket_key='raw/{{ ds }}/data.parquet',
        aws_conn_id='aws_default',
        timeout=60 * 60 * 2,  # 2 hours
        poke_interval=60 * 5,  # Check every 5 minutes
        mode='reschedule',  # Free up worker slot while waiting
    )

    # Wait for another DAG to complete
    wait_for_upstream = ExternalTaskSensor(
        task_id='wait_for_upstream_dag',
        external_dag_id='upstream_etl',
        external_task_id='final_task',
        execution_date_fn=lambda dt: dt,  # Same execution date
        timeout=60 * 60 * 3,
        mode='reschedule',
    )

    # Custom sensor using @task.sensor decorator
    @task.sensor(poke_interval=60, timeout=3600, mode='reschedule')
    def wait_for_api() -> PokeReturnValue:
        """Custom sensor for API availability"""
        import requests

        response = requests.get('https://api.example.com/health')
        is_done = response.status_code == 200

        return PokeReturnValue(is_done=is_done, xcom_value=response.json())

    api_ready = wait_for_api()

    def process_data(**context):
        api_result = context['ti'].xcom_pull(task_ids='wait_for_api')
        print(f"API returned: {api_result}")

    process = PythonOperator(
        task_id='process',
        python_callable=process_data,
    )

    [wait_for_file, wait_for_upstream, api_ready] >> process
```

---

## Pattern 5: Error Handling and Alerts

```python
# dags/error_handling.py
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.trigger_rule import TriggerRule
from airflow.models import Variable

def task_failure_callback(context):
    """Callback on task failure"""
    task_instance = context['task_instance']
    exception = context.get('exception')

    # Send to Slack/PagerDuty/etc
    message = f"""
    Task Failed!
    DAG: {task_instance.dag_id}
    Task: {task_instance.task_id}
    Execution Date: {context['ds']}
    Error: {exception}
    Log URL: {task_instance.log_url}
    """
    # send_slack_alert(message)
    print(message)

def dag_failure_callback(context):
    """Callback on DAG failure"""
    # Aggregate failures, send summary
    pass

with DAG(
    dag_id='error_handling_example',
    schedule='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    on_failure_callback=dag_failure_callback,
    default_args={
        'on_failure_callback': task_failure_callback,
        'retries': 3,
        'retry_delay': timedelta(minutes=5),
    },
) as dag:

    def might_fail(**context):
        import random
        if random.random() < 0.3:
            raise ValueError("Random failure!")
        return "Success"

    risky_task = PythonOperator(
        task_id='risky_task',
        python_callable=might_fail,
    )

    def cleanup(**context):
        """Cleanup runs regardless of upstream failures"""
        print("Cleaning up...")

    cleanup_task = PythonOperator(
        task_id='cleanup',
        python_callable=cleanup,
        trigger_rule=TriggerRule.ALL_DONE,  # Run even if upstream fails
    )

    def notify_success(**context):
        """Only runs if all upstream succeeded"""
        print("All tasks succeeded!")

    success_notification = PythonOperator(
        task_id='notify_success',
        python_callable=notify_success,
        trigger_rule=TriggerRule.ALL_SUCCESS,
    )

    risky_task >> [cleanup_task, success_notification]
```

---

## Pattern 6: Testing DAGs

```python
# tests/test_dags.py
import pytest
from datetime import datetime
from airflow.models import DagBag

@pytest.fixture
def dagbag():
    return DagBag(dag_folder='dags/', include_examples=False)

def test_dag_loaded(dagbag):
    """Test that all DAGs load without errors"""
    assert len(dagbag.import_errors) == 0, f"DAG import errors: {dagbag.import_errors}"

def test_dag_structure(dagbag):
    """Test specific DAG structure"""
    dag = dagbag.get_dag('example_etl')

    assert dag is not None
    assert len(dag.tasks) == 3
    assert dag.schedule_interval == '0 6 * * *'

def test_task_dependencies(dagbag):
    """Test task dependencies are correct"""
    dag = dagbag.get_dag('example_etl')

    extract_task = dag.get_task('extract')
    assert 'start' in [t.task_id for t in extract_task.upstream_list]
    assert 'end' in [t.task_id for t in extract_task.downstream_list]

def test_dag_integrity(dagbag):
    """Test DAG has no cycles and is valid"""
    for dag_id, dag in dagbag.dags.items():
        assert dag.test_cycle() is None, f"Cycle detected in {dag_id}"

# Test individual task logic
def test_extract_function():
    """Unit test for extract function"""
    from dags.example_dag import extract_data

    result = extract_data(ds='2024-01-01')
    assert 'records' in result
    assert isinstance(result['records'], int)
```

---

## Project Structure

```
airflow/
├── dags/
│   ├── __init__.py
│   ├── common/
│   │   ├── __init__.py
│   │   ├── operators.py    # Custom operators
│   │   ├── sensors.py      # Custom sensors
│   │   └── callbacks.py    # Alert callbacks
│   ├── etl/
│   │   ├── customers.py
│   │   └── orders.py
│   └── ml/
│       └── training.py
├── plugins/
│   └── custom_plugin.py
├── tests/
│   ├── __init__.py
│   ├── test_dags.py
│   └── test_operators.py
├── docker-compose.yml
└── requirements.txt
```
