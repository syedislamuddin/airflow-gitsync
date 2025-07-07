from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.docker import DockerOperator
from airflow.operators.dummy_operator import DummyOperator

default_args = {
'owner'                 : 'airflow',
'description'           : 'Use of the DockerOperator',
'depend_on_past'        : False,
'start_date'            : datetime(2025, 7, 6),
'email_on_failure'      : False,
'email_on_retry'        : False,
'retries'               : 0,
}

with DAG('docker_operator_dag', default_args=default_args, schedule="5 * * * *", catchup=True) as dag:
    start_dag = DummyOperator(
        task_id='start_dag'
        )

    end_dag = DummyOperator(
        task_id='end_dag'
        )        

    t1 = DockerOperator(
        task_id='docker_command_sleep',
        image='centos:latest',
        api_version='auto',
        auto_remove=True,
        command="/bin/sleep 30",
        docker_url='tcp://docker-proxy:2375',
        network_mode="bridge",
        mount_tmp_dir=False # added in docker provider 2.1.0rc1
        )

start_dag >> t1 >> end_dag
