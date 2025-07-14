### Code 1

from airflow import models
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator
from airflow.operators.python import BranchPythonOperator, PythonOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime

DAG_NAME = 'test-idat-params'

params = {
  'study': ''
}

with models.DAG(DAG_NAME, start_date=days_ago(1), schedule_interval=None,
params=params) as dag:

  bash_task = BashOperator(
    task_id='idat_params_task',
    bash_command='echo {{ params.study }}'
  )
  
  bash_task
