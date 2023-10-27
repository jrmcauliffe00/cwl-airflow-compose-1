# Use the Apache Airflow base image with Python 3.8
FROM apache/airflow:2.7.1-python3.8

WORKDIR /tmp

USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         apt-transport-https \
         ca-certificates \
         curl \
         software-properties-common \
         git nodejs

RUN pip3 install git+https://github.com/jrmcauliffe00/cwl-airflow.git
RUN pip3 install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}"

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

RUN pip3 install psycopg2-binary