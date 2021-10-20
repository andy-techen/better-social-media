from api import score_text
from csv import reader
import os, time
from tqdm import tqdm

path = os.path.expanduser('~/Documents/umich/courses/si650/project/better-social-media/TwitterAPI/output.csv')

def load_twitter_data():
    '''
    Reads the output.csv file from TwitterAPI folder
    and returns a list of dictionaries for every tweet
    and their categories (created_at, text, username,
    screen_name, verified, followers_count)
    '''
    tweets = []
    with open(path, 'r', encoding='utf-8') as read_object:
        csv_reader = reader(read_object)
        for row in tqdm(csv_reader):
            tweets.append({
                'created_at': row[0],
                'text': row[1],
                'username': row[2],
                'screen_name': row[3],
                'verified': row[4],
                'followers_count': row[5]
            })
    return tweets

def PerspectiveScorer(tweets):
    print("Running Perspective API Scorer...")

    new_tweets = []
    for tweet in tqdm(tweets):
        results = score_text(text=tweet['text'])
        new_tweets.append(dict(list(tweet.items()) + list(results.items()))) #merges tweet data with scoring data
        time.sleep(1)

    return new_tweets






if __name__ == '__main__':
    # pass

    tweets = load_twitter_data()
    # print(tweets[1])
    scored_tweets = PerspectiveScorer(tweets)
