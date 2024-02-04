from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from datetime import datetime, timedelta
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash import BashOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
import psycopg2 as psy




def test_connection():
    connection_params = {
        'host': 'postgres_target',
        'port': 5600,
        'user': 'adam',
        'password': 'Adam1234',
        'database': 'db_prod',
    }

    # Create a connection
    connection = psy.connect(**connection_params)
    return connection


with DAG(
    dag_id='dag_final_project',
    schedule_interval=None,
    start_date=datetime(2021, 12, 13),
    catchup=False,
    tags=['de'],
) as dag:

    start = DummyOperator(
        task_id='start'
    )

    test_connect = PythonOperator(
        task_id = 'test_connection',
        python_callable=test_connection,
    )


    start>>test_connect