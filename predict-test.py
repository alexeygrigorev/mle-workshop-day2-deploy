import requests

url = 'http://localhost:9696/predict'

ride = {
    "PULocationID": 100,
    "DOLocationID": 102,
    "trip_distance": 30
}

response = requests.post(url, json=ride)
prediction = response.json()

print(prediction)