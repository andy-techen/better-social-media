from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import pickle
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)
vectorizer = TfidfVectorizer(vocabulary=pickle.load(open("feature.pickle", "rb")))

def preprocess(tweet):
    processed_punc = re.sub(r'[^@a-zA-Z ]', '', tweet)
    processed = re.sub('https:\S+|@\S+|\b\w{,1}\b', '', processed_punc)
    tokens = word_tokenize(processed)
    tokens_sw = [token for token in tokens if not token in stopwords.words()]
    return tokens_sw

@app.route('/depressive', methods=['POST'])
def get_depressive():
    tweet = request.get_json()
    print(tweet['tweet'])
    print(type(tweet['tweet']))
    x_train = preprocess(tweet['tweet'])
    x_train_tokenized = vectorizer.transform(x_train)
    prediction = depressive.predict(x_train_tokenized)

    return jsonify(prediction)

# @app.route('/toxic/', methods=['POST'])
# def get_toxic():
#     data = request.get_json()
#     prediction = np.array2string(toxic.predict(data))

#     return jsonify(prediction)

if __name__ == '__main__':
    depressive = pickle.load(open('data/ModelAPI/models/depressive_xgb.pickle', 'rb'))
    # toxic = pickle.load(open('toxic.pickle', 'rb'))
    app.run(debug=True)