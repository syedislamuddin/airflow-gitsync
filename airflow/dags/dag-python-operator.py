from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.operators.bash import BashOperator

def helloWorld():
    print('Hello World')

def done():
    print('Done')

with DAG(dag_id="hello_world_dag",
         start_date=datetime(2025,7,7),
         schedule_interval="@hourly",
         catchup=True) as dag:

    task1 = PythonOperator(
        task_id="hello_world",
        python_callable=helloWorld
    )

    sleepTask = BashOperator(
        task_id='sleep',
        bash_command='sleep 10s'
    )

    task2 = PythonOperator(
        task_id="done",
        python_callable=done
    )


task1 >> sleepTask >> task2 
