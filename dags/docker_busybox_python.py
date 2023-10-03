#!/usr/bin/env python3
from cwl_airflow.extensions.cwldag import CWLDAG
dag = CWLDAG(
    workflow="/Path/To/Workflow.cwl",
    dag_id="docker_busybox"
)
