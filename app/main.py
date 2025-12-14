from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI(title="Heart Disease Prediction API")

model = joblib.load("artifacts/model.pkl")

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    return {
        "prediction": prediction,
        "probability": float(probability)
    }
