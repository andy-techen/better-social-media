from flask import Flask, request, jsonify
import numpy as np
import pickle
import json


app = Flask(__name__)

@app.route('/depressive/', methods=['POST'])
def get_depressive():
    data = request.get_json()
    prediction = np.array2string(depressive.predict(data))

    return jsonify(prediction)

@app.route('/toxic/', methods=['POST'])
def get_toxic():
    data = request.get_json()
    prediction = np.array2string(toxic.predict(data))

    return jsonify(prediction)

if __name__ == '__main__':
    depressive = pickle.load(open('depressive.pickle', 'rb'))
    toxic = pickle.load(open('toxic.pickle', 'rb'))
    app.run(debug=True, host='0.0.0.0')