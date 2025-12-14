import joblib
import pandas as pd

MODEL_PATH = "../artifacts/model.pkl"

def load_model():
    return joblib.load(MODEL_PATH)

def predict(input_df: pd.DataFrame):
    model = load_model()
    predictions = model.predict(input_df)
    probabilities = model.predict_proba(input_df)[:, 1]
    return predictions, probabilities

if __name__ == "__main__":
    # Example usage
    df = pd.read_csv("data/heart.csv").drop(columns=["target", "sno"], errors="ignore")
    preds, probs = predict(df.head())
    print(preds)
    print(probs)
