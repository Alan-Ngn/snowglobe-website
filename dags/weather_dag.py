from airflow.decorators import dag, task
from airflow.models import Variable
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
    ski_resorts=[
                    {
                        'lat': 46.92930718381659,
                        'lon':-121.50084437354852,
                        'mountain': 'Crystal Mountain'
                    },
                    {
                        'lat': 46.92930718381659,
                        'lon':-121.50084437354852,
                        'mountain': 'Summit at Snoqualmie'
                    },
                ]


    # lat = 46.92930718381659
    # lon =-121.50084437354852
    OPENWEATHERMAP_API_KEY = Variable.get("OPENWEATHERMAP_API_KEY")
    # get_weather_results_task = HttpOperator(
    #     task_id ='weather_fetch',
    #     method = 'GET',
    #     http_conn_id='openweathermap_api',
    #     endpoint=f'/data/2.5/forecast',
    #     headers={"Content-Type": "application/json"},
    #     data={
    #         'lat':lat,
    #         'lon':lon,
    #         'appid':OPENWEATHERMAP_API_KEY,
    #         'units':'metric'
    #     },
    #     do_xcom_push=True,
    # )

    @task
    def extract(api_results, mountain):
        return [mountain]+json.loads(api_results)['list']

    @task
    def transform(data):
        result=[]
        for i in data:
            for k in range(1,len(i)):
            # for k in i:
                dict_result={}
                dict_result['name'] = i[0]
                print(i[0],i[k])
                dict_result['date'] = datetime.utcfromtimestamp(i[k]['dt']).strftime('%Y-%m-%d %H:%M:%S UTC')
                dict_result['temp'] = i[k]['main']['temp']
                dict_result['weather']=i[k]['weather'][0]['main']
                result.append(dict_result)
        return result

    result_test=[]
    for i in ski_resorts:
        mountain_task = i['mountain'].replace(' ', '_').lower()
        get_weather_results_task = HttpOperator(
            task_id =f'weather_fetch_{mountain_task}',
            method = 'GET',
            http_conn_id='openweathermap_api',
            endpoint=f'/data/2.5/forecast',
            headers={"Content-Type": "application/json"},
            data={
                'lat':i['lat'],
                'lon':i['lon'],
                'appid':OPENWEATHERMAP_API_KEY,
                'units':'metric'
            },
            do_xcom_push=True,
        )
        result_test.append(extract(api_results=get_weather_results_task.output, mountain=i['mountain']))




    # extracted_data = extract(api_results=get_weather_results_task.output, mountain="Crystal Mountain")
    transformed_data = transform(result_test)

weather_etl()
