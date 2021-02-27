from datetime import timedelta, datetime
import json

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator

from operators import run_notebook_operator

# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}

curr_date = datetime.today().strftime('%Y-%m-%d')

dag = DAG(
    'tutorial',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(1),
    tags=['example'],
)

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
)

t2 = run_notebook_operator(
    input_nb="test-base-notebook.ipynb",
    output_nb="output-test-nav-test2.ipynb",
    dag=dag,
)

t3 = run_notebook_operator(
    input_nb="write-to-database.ipynb",
    output_nb="write-to-database-output-{}.ipynb".format(curr_date),
    dag=dag,
)

t4 = run_notebook_operator(
    input_nb="web_scraper_example.ipynb",
    output_nb="web_scraper_example-output-{}.ipynb".format(curr_date),
    dag=dag,
)

t1 >> [t2, t3]
t3 >> t4
