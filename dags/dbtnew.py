from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

# Define default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    'dbt_dag',
    default_args=default_args,
    description='A simple dbt DAG',
    schedule_interval='@daily',
    start_date=datetime(2022, 1, 1),
    catchup=False,
) as dag:

    # Define the dbt run task
    run_dbt = BashOperator(
        task_id='run_dbt',
        bash_command='dbt run --profiles-dir /opt/airflow/include/dbt/project/profiles.yml --project-dir /opt/airflow/include/dbt/project/'
    )

   
    run_dbt 
