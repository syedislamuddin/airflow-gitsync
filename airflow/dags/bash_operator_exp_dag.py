from datetime import datetime
from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

default_args = {
    'start_date': datetime(2025, 7, 6),  # start_date is required but won't affect as schedule_interval is None
    'retries': 0,                        # No retries in this case
}

with DAG(
    dag_id='bash_operator_exp_dag',
    default_args=default_args,
    catchup=True,                    # Disable backfilling or catching up
    schedule=None,           # No schedule, ad-hoc execution
) as dag:
    # Tasks are represented as operators
    hello = BashOperator(task_id="hello", bash_command="echo hello gke airflow")

    @task()
    def airflow():
        print("airflow")

    # Set dependencies between tasks
    hello >> airflow()
