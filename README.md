# CWL Airflow with Docker Compose

Use this repository to quickly run Airflow, using a local executor, with CWL-Airflow. The Dockerfile extension adds CWL-Airflow to Airflow (2.1.4).

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
  - [Executor](#exectutor)
  - [airflow.cfg](#airflow.cfg)



## Getting Started




### Prerequisites

Clone this repository to your local machine where Python 3.8.10 is installed. Additionally, make sure Docker and Docker Compose are downloaded and ready to use.

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
      workflow="./dags/workflow.cwl",
      dag_id="my_dag_name"
  )
  # Now, the dag should automatically load this dag into DAGs (next to clean_dag_run.py)
  ```


3. From the UI, hit the "trigger dag w/ config" button. This will take you to an optional .json prompt. Here, make sure to specify the "job" that occampanies the CWL file you are running.


  
  ```
  {
  "job":{
    "message": "hello"
    }
  }
```

## Configuration

### Executor

This configuration uses a "Local Executor" instead of other executor options. There are options to update the Executor used. Review the documentation [here](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/executor/index.html). *Note: to use other executors, more containers (like reddis and worker) may be nescessary. For future deployments in Kubernetes, for example, Kubernetes or Celery Executors are most likely preferred.


### airflow.cfg

This file is included in the repository as a point of reference. No changes need to added to this file. Chnanges to airflow configuration will happen at the Docker Compose level. See under "airflow-common-env" section of [docker-compose file](/docker-compose.yaml) for some changes being made to airflow configuration.
