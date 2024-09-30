from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime, timedelta

# Définir les arguments de base du DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 9, 30),
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

# Initialiser le DAG
dag = DAG(
    'kedro_drugs_pipeline_dag',
    default_args=default_args,
    description='DAG pour exécuter le data pipeline du graphe de liason entre medicaments et publications',
    schedule_interval=timedelta(minutes=20),
    catchup=False,
)

# Définir l'opérateur Docker pour exécuter Kedro
run_kedro_pipeline = DockerOperator(
    task_id='run_drugs_pipeline',
    image='kedro-drugs-pipeline:latest',
    container_name='kedro_container',
    auto_remove=True,
    command='kedro run',
    dag=dag,
)