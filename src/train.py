import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from model import build_model

DATA_PATH = "../data/data.csv"
MODEL_PATH = "../artifacts/model.pkl"

def main():
    # Load data
    df = pd.read_csv(DATA_PATH)

    # Drop index column if present
    df = df.drop(columns=["sno"], errors="ignore")

    # Replace '?' with NaN if present
    df = df.replace("?", pd.NA)

    X = df.drop("target", axis=1)
    y = df["target"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Build and train model
    model = build_model(X_train)
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    # Save model
    joblib.dump(model, MODEL_PATH)
    print(f"Model saved at {MODEL_PATH}")

if __name__ == "__main__":
    main()
