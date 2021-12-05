from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import pickle
import re
import nltk
import xgboost
from gensim.parsing.porter import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)
vectorizer_depressive = pickle.load(open("data/ModelAPI/vectorizers/vectorizer_depressive.pickle", "rb"))
vectorizer_perspective = pickle.load(open("data/ModelAPI/vectorizers/PerspectiveAPI_vectorizer.pickle", "rb"))
p = PorterStemmer()

def preprocess(tweet):
    processed_punc = re.sub(r'[^@a-zA-Z ]', '', tweet)
    processed = re.sub('https\S+|@\S+|\b\w{,1}\b', '', processed_punc)
    tokens = word_tokenize(processed)
    tokens_sw = [token for token in tokens if not token in stopwords.words()]
    sentence = ' '.join(tokens_sw)
    stemmed_sentence = p.stem_sentence(sentence)

    return stemmed_sentence

@app.route('/depressive', methods=['POST'])
def get_depressive():
    tweet = request.get_json()
    x_train = preprocess(tweet['tweet'])
    x_train_tokenized = vectorizer_depressive.transform([x_train])
    prediction = depressive.predict_proba(x_train_tokenized)[0][1]

    return jsonify(prediction=str(prediction))



if __name__ == '__main__':
    depressive = pickle.load(open('data/ModelAPI/models/depressive_xgb.pickle', 'rb'))
    # toxic = pickle.load(open('toxic.pickle', 'rb'))
    app.run(debug=True)