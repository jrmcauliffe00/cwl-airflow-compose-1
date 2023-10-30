#!/bin/bash

CWL_AIRFLOW_EXECUTABLE=/root/.local/bin/cwl-airflow
# Run the cwl-airflow command
"$CWL_AIRFLOW_EXECUTABLE" api "$@"
