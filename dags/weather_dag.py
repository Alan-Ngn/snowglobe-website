import os
from airflow import DAG
from airflow.models import Variable
from airflow.operators.http_operator import SimpleHttpOperator
from datetime import datetime, timedelta
import logging
OPENWEATHERMAP_API_KEY = Variable.get("OPENWEATHERMAP_API_KEY")
# OPENWEATHERMAP_API_KEY= os.environ.get('OPENWEATHERMAP_API_KEY')
# print(OPENWEATHERMAP_API_KEY)
logging.info(f"Retrieved API key: {OPENWEATHERMAP_API_KEY}")

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
    http_conn_id='openweathermap_api',
    endpoint=f'/data/2.5/forecast?lat={46.9282}&lon={121.5045}&appid={OPENWEATHERMAP_API_KEY}',
    headers={"Content-Type": "application/json"},
    dag=dag
)
#api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}

weather_fetch_task
