from airflow.utils.dates import days_ago
from airflow.decorators import dag
from cosmos.airflow.task_group import DbtTaskGroup
from cosmos.constants import LoadMode
from cosmos.config import RenderConfig
from include.dbt.project.cosmos_config import DBT_CONFIG, DBT_PROJECT_CONFIG

@dag(
    start_date=days_ago(1),
    schedule='@daily',
    catchup=False,
    tags=['dbt', 'transform_data'],
)
def tranform_data():

    project_capstone = DbtTaskGroup(
        group_id="dbt_task",
        project_config=DBT_PROJECT_CONFIG,
        profile_config=DBT_CONFIG,
        render_config=RenderConfig(
            load_method=LoadMode.DBT_LS,
            select=['path:models']
        )
    )

    project_capstone

tranform_data()
