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
# print(API_KEY)

client = discovery.build(
    "commentanalyzer",
    "v1alpha1",
    developerKey=API_KEY,
    discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
    static_discovery=False,
)

analyze_request = {
    'comment': { 'text': 'We are not in a trade war with China, that war was lost many years ago by the foolish, or incompetent, people who represented the U.S. Now we have a Trade Deficit of $500 Billion a year, with Intellectual Property Theft of another $300 Billion. We cannot let this continue!' },
    # 'requestedAttributes': {'TOXICITY': {}},
    # 'requestedAttributes': {'SEVERE_TOXICITY': {}},
    # 'requestedAttributes': {'IDENTITY_ATTACK': {}},
    # 'requestedAttributes': {'INSULT': {}},
    # 'requestedAttributes': {'PROFANITY': {}},
    'requestedAttributes': {'THREAT': {}},
    # 'requestedAttributes': {'SEXUALLY_EXPLICIT': {}},
    # 'requestedAttributes': {'FLIRTATION': {}},
}

response = client.comments().analyze(body=analyze_request).execute()
print(json.dumps(response, indent=2))