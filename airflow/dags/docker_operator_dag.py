from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
# from airflow.operators.dummy import DummyOperator
from airflow.operators.empty import EmptyOperator


default_args = {
'owner'                 : 'docker operator',
'description'           : 'Use of the DockerOperator',
'depend_on_past'        : False,
'start_date'            : datetime(2025, 7, 6),
'email_on_failure'      : False,
'email_on_retry'        : False,
'retries'               : 0,
}

with DAG('docker_operator_dag', default_args=default_args, schedule="* * * * *", catchup=True) as dag:
    start_dag = EmptyOperator(
        task_id='start_dag'
        )

    end_dag = EmptyOperator(
        task_id='end_dag'
        )        

    t1 = DockerOperator(
        task_id='docker_command_sleep',
        image="europe-west4-docker.pkg.dev/gp2-code-test-env/airflow-gtserver/test-apps/hello-app:latest",
        # image='centos:latest',
        # api_version='auto',
        # auto_remove='force',
        # command="/bin/sleep 30",
        # docker_url='tcp://localhost:2375',
        # network_mode="bridge",
        # mount_tmp_dir=False # added in docker provider 2.1.0rc1
            arguments=["load-data"],
            name=f"load_data",
            # task_id=f"load_data",
            retries=5,
            retry_delay=timedelta(minutes=5)
        
        )

start_dag >> t1 >> end_dag
