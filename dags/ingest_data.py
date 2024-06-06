from airflow.decorators import dag, task
from airflow.utils.dates import days_ago
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from airflow.models.baseoperator import chain

USER_BEHAVIOUR_CONN_ID = 'b32b2325-6353-4735-bddb-6846397c24a1'
PRODUCT_INFORMATION_CONN_ID = 'e34ac1f0-5492-429d-9faa-d1b398edca4c'
USER_INFORMATION_CONN_ID = 'b6be7aa3-fd80-4a63-844d-6b97ff214a93'

@dag(
    start_date=days_ago(1),
    schedule='@daily',
    catchup=False,
    tags=['airbyte', 'ingest_csv'],
)

def ingest_raw_data():
    ingest_user_behaviour = AirbyteTriggerSyncOperator(
        task_id='ingest_user_behaviour',
        airbyte_conn_id='airbyte_conn',
        connection_id=USER_BEHAVIOUR_CONN_ID,
        asynchronous=False,
        timeout=3600,
        wait_seconds=3
    )

    ingest_product_information=AirbyteTriggerSyncOperator(
        task_id='ingest_product_information',
        airbyte_conn_id='airbyte_conn',
        connection_id=PRODUCT_INFORMATION_CONN_ID,
        asynchronous=False,
        timeout=3600,
        wait_seconds=3
    )

    ingest_user_information=AirbyteTriggerSyncOperator(
        task_id='ingest_user_information',
        airbyte_conn_id='airbyte_conn',
        connection_id=USER_INFORMATION_CONN_ID,
        asynchronous=False,
        timeout=3600,
        wait_seconds=3
    )

    @task
    def airbyte_job_done():
        return True 
    
    chain(
        [ingest_user_behaviour >> ingest_product_information >>  ingest_user_information],
        airbyte_job_done()
    )

ingest_raw_data()