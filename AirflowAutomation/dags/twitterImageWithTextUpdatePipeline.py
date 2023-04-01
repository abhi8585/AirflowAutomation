import json
from datetime import datetime, timedelta

from airflow.decorators import dag, task
from utils.get_bq_image import Image
from utils.twitterImageWithTextUpdate import TwitterImagewithTextUpdate

# TODO :  call function to get the image
# 

def logData(message):
    if message is not None:
        print(message)
image_client = Image()
twitter_client = TwitterImagewithTextUpdate()




@dag(
    schedule_interval="@daily",
    start_date=datetime(2021, 1, 1),
    catchup=False,
    default_args={
        "retries": 2, 
    },
    tags=['twitter','status','update']) 

def twitter_status_with_image_update():

    @task
    def kickOff():
        from datetime import datetime
        return datetime.today().strftime('%Y-%m-%d')
        res = tweet_text("Live as if you were to die tomorrow")
        return res


    @task
    def get_folder_images(timestamp):
        folder_path = "twitter_python_keywords"
        image_names = image_client.get_file_names(folder_path,project_name="airflow-dev-382217")
        image_to_tweet = sorted(image_names)[0]
        image_to_tweet_name = image_to_tweet.split("/")[1]
        logData(f"Today's Image to upload {image_to_tweet_name}")
        return dict(image_name=image_to_tweet_name, image_path=image_to_tweet)

    @task()
    def download_image(image_details):
        image_file_name = image_details["image_path"]
        is_downloaded = image_client.download_image_file(image_file_name,project_name="airflow-dev-382217")
        logData(is_downloaded)
        image_details["is_downloaded"] = is_downloaded
        return image_details

    @task
    def tweet_image(image_details):
        image_name = image_details["image_name"]
        is_downloaded = image_details["is_downloaded"]
        if is_downloaded:
            is_posted = twitter_client.updateImageWithText(image_name)
            logData(is_posted)

    kickoff = kickOff()
    # is_posted = tweet_image(download_image(get_folder_images(kickoff)))

twitter_status_with_image_update()