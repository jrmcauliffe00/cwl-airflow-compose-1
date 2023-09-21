#!/usr/bin/env python3
from cwl_airflow.extensions.cwldag import CWLDAG
dag = CWLDAG(
    workflow="./dags/workflow.cwl",
    dag_id="my_dag"
)
