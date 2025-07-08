from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator
# from airflow.operators.docker_operator import DockerOperator


default_args = {
    'owner'                 : 'k8s',
    'description'           : 'Use of the DockerOperator',
    'depend_on_past'        : False,
    'start_date'            : datetime(2025, 7, 6),
    'email_on_failure'      : False,
    'email_on_retry'        : False,
    'retries'               : 1,
    'retry_delay'           : timedelta(minutes=5)
}

with DAG('bash_dag_sample', default_args=default_args, schedule="* * * * *", catchup=True) as dag:
    t1 = BashOperator(
        task_id='print_hello_bash_operator',
        bash_command='echo "hello world"'
    )

t1
