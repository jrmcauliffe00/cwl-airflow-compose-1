FROM apache/airflow:2.1.4-python3.8

USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         git nodejs \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
USER airflow

RUN pip3 install  git+https://github.com/Barski-lab/cwl-airflow.git
RUN pip3 install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}"
