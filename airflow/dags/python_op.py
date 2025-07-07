from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def my_python_callable():
    """
    A simple Python function to be executed by the PythonOperator.
    """
    print("Hello from the PythonOperator!")

with DAG(
    dag_id='python_operator_example',
    start_date=datetime(2025, 7, 2),
    schedule_interval=None,  # This DAG will be triggered manually
    catchup=True,
    tags=['example'],
) as dag:
    # Define a task using the PythonOperator
    run_python_task = PythonOperator(
        task_id='execute_my_function',
        python_callable=my_python_callable,
    )
