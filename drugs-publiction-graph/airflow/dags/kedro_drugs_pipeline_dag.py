from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 9, 30),
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}


dag = DAG(
    'kedro_drugs_pipeline_dag',
    default_args=default_args,
    description='DAG to run Kedro drugs pipeline in Docker',
    schedule_interval=timedelta(minutes=20),
    catchup=False,
)

run_kedro_pipeline = DockerOperator(
    task_id='run_drugs_pipeline',
    image='kedro-drugs-pipeline:latest',
    container_name='kedro_container',
    auto_remove=True,
    command='kedro run',
    docker_url='unix://var/run/docker.sock',
    network_mode='bridge',
    dag=dag,
)