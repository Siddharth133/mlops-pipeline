from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess
import logging

def retrain_model():
    logging.info("Starting model retraining...")
    result = subprocess.run(["python", "retrain.py"], capture_output=True, text=True)
    if result.returncode != 0:
        logging.error(f"Retraining failed: {result.stderr}")
        raise Exception("Retraining process failed.")
    logging.info(f"Retraining completed successfully: {result.stdout}")

def validate_model():
    logging.info("Validating the model...")
    result = subprocess.run(["python", "validate_model.py"], capture_output=True, text=True)
    if result.returncode != 0:
        logging.error(f"Model validation failed: {result.stderr}")
        raise Exception("Validation process failed.")
    logging.info(f"Model validated successfully: {result.stdout}")

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'start_date': datetime(2024, 12, 21),
}

dag = DAG(
    'model_retraining',
    default_args=default_args,
    description='Automate retraining and validation of the ML model',
    schedule_interval='@daily',
)

retrain_task = PythonOperator(
    task_id='retrain_model_task',
    python_callable=retrain_model,
    dag=dag,
)

validate_task = PythonOperator(
    task_id='validate_model_task',
    python_callable=validate_model,
    dag=dag,
)

retrain_task >> validate_task
