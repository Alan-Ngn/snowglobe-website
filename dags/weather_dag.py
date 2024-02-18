from airflow import DAG
from airflow.operators.http_operator import SimpleHttpOperator
from datetime import datetime, timedelta

default_args = {
    'owner':'snowglobe',
    'start_date': datetime(2023, 2, 14, 7, 0, 0),  # datetime(year, month, day, hour, minute, second)
    'retries': 1,
    'retries_delay': timedelta(minutes=15)
}

dag = DAG(
    'openweathermap',
    default_args=default_args,
    schedule_interval=timedelta(days=1)
)

weather_fetch_task = SimpleHttpOperator(
    task_id ='weather_fetch',
    method = 'GET',
    http_conn_id='',
    endpoint='',
    xcom_push=True,
    headers={"Content-Type": "application/json"},
    dag=dag
)
