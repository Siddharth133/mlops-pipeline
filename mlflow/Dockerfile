FROM python:3.9-slim


WORKDIR /mlflow

RUN pip install mlflow

EXPOSE 5001

ENTRYPOINT ["mlflow", "server", "--host", "0.0.0.0", "--backend-store-uri", "file:/mlflow/mlruns"]
