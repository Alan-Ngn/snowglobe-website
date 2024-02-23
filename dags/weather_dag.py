from airflow.decorators import dag, task
from airflow.models import Variable
# from airflow.operators.http_operator import SimpleHttpOperator
from airflow.providers.http.operators.http import HttpOperator
from datetime import datetime, timedelta
import json
default_args = {
    'owner':'snowglobe',
    'start_date': datetime(2023, 2, 14, 7, 0, 0),  # datetime(year, month, day, hour, minute, second)
    'retries': 1,
    'retries_delay': timedelta(minutes=15)
}
@dag(
    dag_id='openweathermap',
    default_args=default_args,
    schedule_interval=timedelta(days=1)
)
def weather_etl():
    OPENWEATHERMAP_API_KEY = Variable.get("OPENWEATHERMAP_API_KEY")
    get_weather_results_task = HttpOperator(
        task_id ='weather_fetch',
        method = 'GET',
        http_conn_id='openweathermap_api',
        endpoint=f'/data/2.5/forecast?lat={46.92930718381659}&lon={-121.50084437354852}&appid={OPENWEATHERMAP_API_KEY}&units=metric',
        headers={"Content-Type": "application/json"},
        do_xcom_push=True,
    )

    @task
    def extract(api_results):
        return json.loads(api_results)['list']

    @task
    def transform(data):
        result=[]
        for i in data:
            dict_result={}
            dict_result['name'] = "Crystal Mountain"
            dict_result['date'] = datetime.utcfromtimestamp(i['dt']).strftime('%Y-%m-%d %H:%M:%S UTC')
            dict_result['temp'] = i['main']['temp']
            dict_result['weather']=i['weather'][0]['main']
            result.append(dict_result)
        return result
        # x=data['list']
        # result = {}
        # result['name'] = "Crystal Mountain"
        # result['date'] = datetime.utcfromtimestamp(x[0]['dt']).strftime('%Y-%m-%d %H:%M:%S UTC')
        # print(result)
        # return data['list']


    extracted_data = extract(api_results=get_weather_results_task.output)
    transformed_data = transform(extracted_data)

weather_etl()
# from airflow import DAG
# from airflow.models import Variable
# from airflow.operators.http_operator import SimpleHttpOperator
# from datetime import datetime, timedelta

# OPENWEATHERMAP_API_KEY = Variable.get("OPENWEATHERMAP_API_KEY")

# default_args = {
#     'owner':'snowglobe',
#     'start_date': datetime(2023, 2, 14, 7, 0, 0),  # datetime(year, month, day, hour, minute, second)
#     'retries': 1,
#     'retries_delay': timedelta(minutes=15)
# }

# dag = DAG(
#     'openweathermap',
#     default_args=default_args,
#     schedule_interval=timedelta(days=1)
# )

# weather_fetch_task = SimpleHttpOperator(
#     task_id ='weather_fetch',
#     method = 'GET',
#     http_conn_id='openweathermap_api',
#     endpoint=f'/data/2.5/forecast?lat={46.9282}&lon={}&appid={OPENWEATHERMAP_API_KEY}',
#     headers={"Content-Type": "application/json"},
#     dag=dag
# )


# weather_fetch_task
