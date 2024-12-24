FROM python:3.9-slim
WORKDIR /app
RUN pip install flask pandas scikit-learn apache-airflow mlflow numpy joblib flask-cors
COPY . .
EXPOSE 5000
CMD ["python", "app.py"] 