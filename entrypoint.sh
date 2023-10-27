#!/bin/bash

# Activate your virtual environment (if applicable)
# source /path/to/your/virtualenv/bin/activate

CWL_AIRFLOW_EXECUTABLE=/root/.local/bin/cwl-airflow
# Run the cwl-airflow command
"$CWL_AIRFLOW_EXECUTABLE" api "$@"