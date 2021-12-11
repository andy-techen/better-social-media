import numpy as np
import pandas as pd
import pickle
import re
import nltk
import xgboost
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from gensim.parsing.porter import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)
CORS(app)

vectorizer_depressive = pickle.load(open("vectorizers/vectorizer_depressive.pickle", "rb"))
vectorizer_perspective = pickle.load(open("vectorizers/PerspectiveAPI_vectorizer.pickle", "rb"))
depressive = pickle.load(open('models/depressive_xgb.pickle', 'rb'))
toxicity = pickle.load(open('models/toxicity_xgb.pickle', 'rb'))
sexually = pickle.load(open('models/sexually_explicit_xgb.pickle', 'rb'))
profanity = pickle.load(open('models/profanity_xgb.pickle', 'rb'))
p = PorterStemmer()

def preprocess(tweet):
    processed_punc = re.sub(r'[^@a-zA-Z ]', '', tweet)
    processed = re.sub('https\S+|@\S+|\b\w{,1}\b', '', processed_punc)
    tokens = word_tokenize(processed)
    tokens_sw = [token for token in tokens if not token in stopwords.words()]
    sentence = ' '.join(tokens_sw)
    stemmed_sentence = p.stem_sentence(sentence)

    return stemmed_sentence

@app.route('/api/depressive', methods=['POST'])
def get_depressive():
    tweet = json.loads(request.get_data())
    x_train = preprocess(tweet['tweet'])
    x_train_tokenized = vectorizer_depressive.transform([x_train])
    prediction = depressive.predict_proba(x_train_tokenized)[0][1]

    return jsonify(prediction=str(prediction))

@app.route('/api/perspective', methods=['POST'])
def get_perspective():
    tweet = json.loads(request.get_data())
    x_train = preprocess(tweet['tweet'])
    x_train_tokenized = vectorizer_perspective.transform([x_train])
    toxicity_pred = toxicity.predict(x_train_tokenized)[0]
    sexually_pred = sexually.predict(x_train_tokenized)[0]
    profanity_pred = profanity.predict(x_train_tokenized)[0]

    return jsonify(toxicity=str(toxicity_pred), sexually=str(sexually_pred), profanity=str(profanity_pred))

if __name__ == '__main__':
    app.run(debug=True)