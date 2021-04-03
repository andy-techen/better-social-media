import json
import os
from dotenv import load_dotenv
load_dotenv()

from tweepy import API, OAuthHandler
import pandas as pd

# HOME_API = "https://api.twitter.com/1.1/statuses/home_timeline.json"

auth = OAuthHandler(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET'))
auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_SECRET'))

api = API(auth)

statuses = api.home_timeline(tweet_mode="extended")

for status in statuses:
    print(status.user.name)
    print(f"@{status.user.screen_name}")
    print(status.user.profile_image_url)
    print(status.full_text)
    print(status.created_at)
    print("------")
    


