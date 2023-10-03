# CWL Airflow with Docker Compose

Use this repository to quickly run Airflow, using a local executor, with CWL-Airflow. The Dockerfile extension adds CWL-Airflow to Airflow (2.7.1).

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
  - [Executor](#executor)
  - [airflow cfg](#airflow-cfg)



## Getting Started




### Prerequisites

Clone this repository to your local machine where Python 3.8.10 is installed. Additionally, make sure Docker and Docker Compose are downloaded and ready to use. Specifying cwltool and Airflow versions can be done at runtime. [Dockerfile]{./Dockerfile} is used as a basis for this Docker Compose environment (the extended image used include CWL-Airflow and node.js).

### Installation

To start the containers, use the following command below.
</pre>
```bash
docker compose up --build
```
</pre>


## Usage

After installation, to use Airflow with CWL, follow these simple steps.
1. Add your dag to the ./dag folder in your directory.
2. Use the following my_dag.py format to import your workflow


  ```
  #!/usr/bin/env python3
  from cwl_airflow.extensions.cwldag import CWLDAG
  dag = CWLDAG(
      workflow="./dags/workflows/workflow.cwl",
      dag_id="my_dag_name"
  )
  # Now, the scheduler should automatically load this dag into the ./dags folder (next to clean_dag_run.py)
  ```


3. Included in ./dags is a python file that utilizes the TriggerDagRunOperator to trigger another DAG in the same directory. Using this python file, you can pass configuration parameters in a .json format. More details about the TriggerDagRunOperator [here]{https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/operators/trigger_dagrun/index.html}.
  
  ```
  {"job":{"message": "hello"}}
 ```

## Configuration

### Executor

This configuration uses a "Local Executor".


### airflow cfg

This file is included in the repository as a point of reference. No changes need to be added to this file. Changes to airflow configuration will happen in the Docker-Compose yml. See under "airflow-common-env" section of [docker-compose file](/docker-compose.yaml) where some changes are made to airflow configuration.
