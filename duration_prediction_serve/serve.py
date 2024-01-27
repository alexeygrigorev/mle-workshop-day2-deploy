import os
import pickle

from flask import Flask, request, jsonify

default_model_file = 'model.bin'

MODEL_FILE = os.getenv('MODEL_FILE', default_model_file)

app = Flask('duration-prediction')

VERSION = os.getenv('VERSION', 'N/A')

with open(MODEL_FILE, 'rb') as f_in:
    model = pickle.load(f_in)


def prepare_features(ride):
    features = {}
    features['PULocationID'] = str(ride['PULocationID'])
    features['DOLocationID'] = str(ride['DOLocationID'])
    features['trip_distance'] = ride['trip_distance']
    return features


def post_processing(pred):
    return pred


def predict(trip):
    prediction = model.predict(trip)
    return prediction[0]


@app.route('/predict', methods=['POST'])
def predict_endpoint():
    ride = request.get_json()

    features = prepare_features(ride)
    pred = predict(features)
    final_result = post_processing(pred)

    result = {
        'preduction': {
            'duration': final_result,
        },
        'version': VERSION,
    }

    return jsonify(result)


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=9696)