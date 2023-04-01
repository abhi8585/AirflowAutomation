class TwitterStatusUpdate:

    def __init__(self,token=None):
        self.token = token
        pass

    def tweet_text(self, tweet_content):
        import requests
        url = f"https://flask-hello-world-phi-two.vercel.app/tweet_text?tweet_content=\"{tweet_content}\""
        payload={}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.status_code