import os
import json
import time
from unidecode import unidecode
from tweepy import API, Stream
from dotenv import load_dotenv
load_dotenv()

# auth = OAuthHandler(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET'))
# auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_SECRET'))

# api = API(auth)

# user timeline tweets-----------------------------------------------------------
# home_tweets = api.home_timeline(tweet_mode="extended") # returns 20 results by default, modify with "count"

# for tweet in home_tweets:
#     print(tweet.user.name)
#     print(f"@{tweet.user.screen_name}")
#     print(tweet.user.profile_image_url)
#     print(tweet.full_text)
#     print(tweet.created_at)
#     print("------")
    
# Twitter streamer---------------------------------------------------------------
class Listener(Stream):

    def on_data(self, data):
        try:
            tweet_data = json.loads(data)

            if 'retweeted_status' in tweet_data:
                if 'extended_tweet' in tweet_data['retweeted_status']:
                    tweet = unidecode(tweet_data['retweeted_status']['extended_tweet']['full_text'])
                else:
                    tweet = unidecode(tweet_data['retweeted_status']['text'])
            else:
                if 'extended_tweet' in tweet_data:
                    tweet = unidecode(tweet_data['extended_tweet']['full_text'])
                else:
                    tweet = unidecode(tweet_data['text'])
            print(f'Writing tweet: {tweet}')
        
        except KeyError as e:
            print(str(e))

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    try:
        twitter_stream = Listener(
            os.getenv('CONSUMER_KEY'),
            os.getenv('CONSUMER_SECRET'),
            os.getenv('ACCESS_TOKEN'),
            os.getenv('ACCESS_SECRET'))  # , tweet_mode='extended'
        twitter_stream.filter(languages=["en"], track=['a', 'e', 'i', 'o', 'u'])

    except Exception as e:
        print(e)
        time.sleep(3)