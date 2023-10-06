#!/usr/bin/env python3
from cwl_airflow.extensions.cwldag import CWLDAG
dag = CWLDAG(
    workflow="./dags/workflows/docker_busybox.cwl",
    dag_id="docker_busybox"
)
