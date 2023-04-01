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
def twitter_status_update():
    @task
    def kickOff():
        from datetime import datetime
        return datetime.today().strftime('%Y-%m-%d')

    @task()
    def tweetText(timestamp):
        """
        #### update twitter status
        """
        content = "It always seems impossible until it's done."
        ins = TwitterStatusUpdate()
        is_posted = ins.tweet_text(content)
        return is_posted

    kickoff = kickOff()
    tweetText(kickoff)
    
twitter_status_update_pipeline = twitter_status_update()