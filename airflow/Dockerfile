FROM apache/airflow:2.7.0

WORKDIR /app

# Copy the DAGs into the Airflow container
COPY dags/ /opt/airflow/dags/
COPY plugins/ /opt/airflow/plugins/ 

ENV AIRFLOW_HOME=/opt/airflow

# Initialize the Airflow DB
RUN airflow db init
EXPOSE 8081
# Set the default entrypoint for Airflow
ENTRYPOINT ["airflow"]

# Set the default command to run the webserver
CMD ["webserver"]
