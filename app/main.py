from fastapi import FastAPI
import joblib
import pandas as pd
import logging
import time

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

app = FastAPI(title="Heart Disease Prediction API")

model = joblib.load("artifacts/model.pkl")

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: dict):
    start_time = time.time()

    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    probability = float(model.predict_proba(df)[0][1])

    latency = time.time() - start_time

    # Log per-sample prediction
    logging.info(
        f"INPUT={data} | PRED={prediction} | PROB={probability:.4f} | LATENCY={latency:.4f}s"
    )

    return {
        "prediction": prediction,
        "probability": probability,
        "latency_sec": latency
    }
