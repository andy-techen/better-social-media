from api import score_text
from csv import reader
import os, time, csv
from tqdm import tqdm

path = os.path.expanduser('../TwitterAPI/output.csv')

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
        try:
            results = score_text(text=tweet['text'])
            #print(tweet['text'], results)
            new_tweets.append(dict(list(tweet.items()) + list(results.items()))) #merges tweet data with scoring data
            time.sleep(1.01)
        except:
            time.sleep(10)
            continue

    return new_tweets

def write_csv(list):
    keys = list[0].keys()
    with open("scored_tweets.csv", "w", encoding='utf-8', newline='') as output_file:
        writer = csv.DictWriter(output_file, keys)
        writer.writeheader()
        writer.writerows(list)
        # writer.writerow(['created_at', 'text', 'username', 'screen_name', 'verified', 'followers_count', 'TOXICITY', 'INSULT', 'PROFANITY', 'THREAT', 'SEXUALLY_EXPLICIT'])






if __name__ == '__main__':
    # pass

    tweets = load_twitter_data()
    # print(tweets[1])
    scored_tweets = PerspectiveScorer(tweets)
    print(scored_tweets[0])
    print(scored_tweets[30])
    write_csv(scored_tweets)

    #currently taking about 33 hours to score 100K tweets
