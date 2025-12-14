import random
import requests
import json

API_URL = "http://136.119.155.126/predict"

def random_sample():
    return {
        "age": random.randint(29, 77),
        "gender": random.choice(["male", "female"]),
        "cp": random.randint(0, 3),
        "trestbps": random.randint(90, 180),
        "chol": random.randint(150, 350),
        "fbs": random.randint(0, 1),
        "restecg": random.randint(0, 2),
        "thalach": random.randint(100, 200),
        "exang": random.randint(0, 1),
        "oldpeak": round(random.uniform(0, 4), 2),
        "slope": random.randint(0, 2),
        "ca": random.randint(0, 3),
        "thal": random.randint(0, 2)
    }

for i in range(100):
    sample = random_sample()
    response = requests.post(API_URL, json=sample)
    print(f"{i+1}: {response.json()}")
