from googleapiclient import discovery
import json
import os
from dotenv import load_dotenv
load_dotenv()

# # # Testing connection
# def implicit():
#     from google.cloud import storage

#     # If you don't specify credentials when constructing the client, the
#     # client library will look for credentials in the environment.
#     storage_client = storage.Client()

#     # Make an authenticated API request
#     buckets = list(storage_client.list_buckets())
#     print(buckets)

#Test API KEY and Response Analysis
API_KEY = os.getenv('PERSPECTIVE_API_KEY')

client = discovery.build(
    "commentanalyzer",
    "v1alpha1",
    developerKey=API_KEY,
    discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
    static_discovery=False,
)

def score_text(text):
    analyze_request = {
        'comment': { 'text': text},
        'requestedAttributes': {
            'TOXICITY': {},
            'INSULT': {},
            'PROFANITY': {},
            'THREAT': {},
            'SEXUALLY_EXPLICIT': {},

            ## Additional Sentiment Analysis:
            ## - Depressive content
        },
    }

    english = 'en'
    if english in client.comments().analyze(body=analyze_request).execute()['languages']:

        response = client.comments().analyze(body=analyze_request).execute()

        results = {
            'TOXICITY': response['attributeScores']['TOXICITY']['summaryScore']['value'],
            'INSULT': response['attributeScores']['INSULT']['summaryScore']['value'],
            'PROFANITY': response['attributeScores']['PROFANITY']['summaryScore']['value'],
            'THREAT': response['attributeScores']['THREAT']['summaryScore']['value'],
            'SEXUALLY_EXPLICIT': response['attributeScores']['SEXUALLY_EXPLICIT']['summaryScore']['value'],
        }
        return results

    else:
        return {'TOXICITY': 0, 'INSULT': 0, 'PROFANITY': 0, 'THREAT': 0, 'SEXUALLY_EXPLICIT': 0}

if __name__ == '__main__':
    pass

    sample = '''We are not in a trade war with China, 
    that war was lost many years ago by the foolish, 
    or incompetent, people who represented the U.S. 
    Now we have a Trade Deficit of $500 Billion a year, 
    with Intellectual Property Theft of another $300 Billion. 
    We cannot let this continue!'''

    print(score_text(text=sample))