import airflow
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import timedelta
from airflow.utils.dates import days_ago
import requests
from utils.get_bq_image import Image
import os


# def my_func():
#     r = requests.get("https://flask-hello-world-phi-two.vercel.app/about")
#     print("---status code---")
#     print(r.status_code)

def download_image():
    image_client = Image()
    image_file_name = "twitter_python_keywords/BoolDataTypeKeyword_ManimCE_v0.17.2.png"
    is_downloaded = image_client.download_image_file(image_file_name=image_file_name,project_name="airflow-dev-382217")
    if is_downloaded:
        image_name = image_file_name.split("/")[1]
        IMAGE_NAME = image_name
    # image_path = image_path.split("***")
    # image_path = image_path[0] + image_path[-1]
        return image_name


def tweet_image():
    return 'IMAGE_NAME'


default_args = {
            'owner': 'airflow',    
            #'start_date': airflow.utils.dates.days_ago(2),
            # 'end_date': datetime(),
            # 'depends_on_past': False,
            #'email': ['airflow@example.com'],
            #'email_on_failure': False,
            #'email_on_retry': False,
            # If a task fails, retry it once after waiting
            # at least 5 minutes
            #'retries': 1,
            'retry_delay': timedelta(minutes=5),
        }

dag_python = DAG(
	dag_id = "pythonoperator_demo",
	default_args=default_args,
	# schedule_interval='0 0 * * *',
	schedule_interval='@once',	
	dagrun_timeout=timedelta(minutes=60),
	description='use case of python operator in airflow',
	start_date = airflow.utils.dates.days_ago(1))

dummy_task = DummyOperator(task_id='dummy_task', retries=3, dag=dag_python)
download_image = PythonOperator(task_id='download_image', python_callable=download_image, dag=dag_python)
tweet_image = PythonOperator(task_id='tweet_image', python_callable=tweet_image, dag=dag_python)
dummy_task >> download_image >> tweet_image