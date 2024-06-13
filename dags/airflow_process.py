from airflow.utils.dates import days_ago
from airflow.decorators import dag,task, task_group
from cosmos.airflow.task_group import DbtTaskGroup
from cosmos.constants import LoadMode
from cosmos.config import RenderConfig
from include.dbt.project.cosmos_config import DBT_CONFIG, DBT_PROJECT_CONFIG
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from airflow.models.baseoperator import chain
from airflow.operators.bash_operator import BashOperator


USER_CONN_ID = 'b51d16e8-00e8-4945-8998-8ffcc6c53d97'
PRODUCT_CONN_ID = 'edb1fbff-532d-45d6-804b-09b9d0420aa2'
PURCHASED_CONN_ID = '11120be3-442a-44ec-8960-8be3067ef0f7'
CART_CONN_ID = '8d4a80f5-ba8b-41c1-a816-1e759106cfd1'
COUNTRY_CONN_ID = '404cdb27-3a5f-4f65-a940-f216dceafd09'
REVIEW_CONN_ID = '7cb9223a-b359-4f29-ac6c-d8321ee60da6'
TAGS_CONN_ID = '33148600-ddf2-4142-b5a2-69390d4a714c'
GENDER_CONN_ID = 'b0e2630a-2c18-41cc-bd37-edcb76f42bb2'


@dag(
    start_date=days_ago(1),
    schedule='@daily',
    catchup=False,
    tags=['airbyte', 'ingest_csv'],
)

def extract_load_transform():
    @task_group(group_id='airbyteTaskGroup')
    def extract_process():
        ingest_user = AirbyteTriggerSyncOperator(
            task_id='ingest_user',
            airbyte_conn_id='airbyte_conn',
            connection_id=USER_CONN_ID,
            asynchronous=False,
            timeout=3600,
            wait_seconds=3
        )

        ingest_product =AirbyteTriggerSyncOperator(
            task_id='ingest_product',
            airbyte_conn_id='airbyte_conn',
            connection_id=PRODUCT_CONN_ID,
            asynchronous=False,
            timeout=3600,
            wait_seconds=3
        )

        ingest_purchased=AirbyteTriggerSyncOperator(
            task_id='ingest_purchased',
            airbyte_conn_id='airbyte_conn',
            connection_id=PURCHASED_CONN_ID,
            asynchronous=False,
            timeout=3600,
            wait_seconds=3
        )

        ingest_cart=AirbyteTriggerSyncOperator(
            task_id='ingest_cart',
            airbyte_conn_id='airbyte_conn',
            connection_id=CART_CONN_ID,
            asynchronous=False,
            timeout=3600,
            wait_seconds=3
        )

        ingest_country=AirbyteTriggerSyncOperator(
            task_id='ingest_country',
            airbyte_conn_id='airbyte_conn',
            connection_id=COUNTRY_CONN_ID,
            asynchronous=False,
            timeout=3600,
            wait_seconds=3
        )

        ingest_review=AirbyteTriggerSyncOperator(
            task_id='ingest_review',
            airbyte_conn_id='airbyte_conn',
            connection_id=REVIEW_CONN_ID,
            asynchronous=False,
            timeout=3600,
            wait_seconds=3
        )

        ingest_tags=AirbyteTriggerSyncOperator(
            task_id='ingest_tags',
            airbyte_conn_id='airbyte_conn',
            connection_id=TAGS_CONN_ID,
            asynchronous=False,
            timeout=3600,
            wait_seconds=3
        )

        ingest_gender=AirbyteTriggerSyncOperator(
            task_id='ingest_gender',
            airbyte_conn_id='airbyte_conn',
            connection_id=GENDER_CONN_ID,
            asynchronous=False,
            timeout=3600,
           wait_seconds=3
        )
        ingest_user >> ingest_product >>  ingest_purchased >> ingest_cart >> ingest_country >> ingest_review >> ingest_tags >> ingest_gender

    @task
    def airbyte_job_done():
        return True 
    
    @task_group(group_id='DBTTaskGroup')
    def transfrom_process():
    
        dbt_run = BashOperator(
            task_id="dbt_run",
            bash_command="cd /opt/airflow/include/dbt/project; source /opt/airflow/dbt_venv/bin/activate; dbt run --profiles-dir /opt/airflow/include/dbt/project/",
            
        )

        dbt_test = BashOperator(
            task_id="dbt_test",
            bash_command="cd /opt/airflow/include/dbt/project; source /opt/airflow/dbt_venv/bin/activate; dbt test --profiles-dir /opt/airflow/include/dbt/project/",
        )
        dbt_run >> dbt_test

    chain(
        extract_process(),
        airbyte_job_done(),
        transfrom_process()
    )

extract_load_transform()