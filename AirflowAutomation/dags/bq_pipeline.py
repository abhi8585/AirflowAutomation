import json
from datetime import datetime, timedelta
from airflow.decorators import dag, task
from utils.twitterStatusUpdate import TwitterStatusUpdate

@dag(
    schedule_interval="@hourly",
    start_date=datetime.now(),
    catchup=False,
    default_args={
        "retries": 2, 
    },
    tags=['twitter','status','update']) 
def bq_test_pipeline():
    @task
    def kickOff():
        from datetime import datetime
        return datetime.today().strftime('%Y-%m-%d')

    @task()
    def updateStatus(timestamp):
        """
        #### update twitter status
        """
        # from utils.twitterStatusUpdate import TwitterStatusUpdate
        content = "It always seems impossible until it's done."
        ins = TwitterStatusUpdate()
        is_posted = ins.tweet_text(content)
        return is_posted
        # return is_posted
        # from google.cloud import bigquery
        # client = bigquery.Client(project="airflow-dev-382217")
        # query = """
        #     select * from `airflow-dev-382217.TwitterAutomation.Tweet`
        # """
        # results = client.query(query)
        # for row in results:
        #     id = row['id']
        #     description = row['description']
        #     print(id,description)

    is_posted = updateStatus(kickOff())

bq_test_pipeline()