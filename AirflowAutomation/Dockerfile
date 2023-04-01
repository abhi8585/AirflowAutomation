FROM apache/airflow:2.5.1
USER root
RUN apt-get update \ 
  && apt-get install -y --no-install-recommends \
         vim \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* 

RUN apt-get install -y curl gnupg && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    echo "deb https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    apt-get update && \
    apt-get install -y google-cloud-sdk

USER airflow
RUN pip install --no-cache-dir tweepy
# Set up credentials
ENV GOOGLE_APPLICATION_CREDENTIALS /opt/airflow/dags/credentials.json


