from datetime import datetime
from airflow.models import DAG
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
import random
from cwl_airflow.utilities.cwl import clean_up_dag_run
from cwl_airflow.utilities.report import dag_on_success, dag_on_failure



dag = DAG(
    dag_id="trigger_dag",
    start_date=datetime(2023, 9, 14),
    on_failure_callback=dag_on_failure,
    on_success_callback=dag_on_success,
    schedule_interval=None
)
run_this = TriggerDagRunOperator(
        task_id="tdro",
        trigger_dag_id="docker_busybox",
        dag=dag,
        conf={"job":{"message": "hello"}}
    )
