import random
import requests
import pandas as pd

API_URL = "http://136.119.155.126/predict"

rows = []

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
    rows.append(sample)
    requests.post(API_URL, json=sample)

# Save inference data
df_inf = pd.DataFrame(rows)
df_inf.to_csv("inference_data.csv", index=False)

print("Saved inference_data.csv")
