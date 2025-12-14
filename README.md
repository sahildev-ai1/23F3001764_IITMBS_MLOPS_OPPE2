# MLOps OPPE-2 — Heart Disease Prediction System

This repository contains an end-to-end MLOps pipeline for **Heart Disease Prediction**, developed as part of **MLOps OPPE-2 (IIT Madras BS)**.  
The project covers model training, explainability, fairness analysis, API deployment, containerization, Kubernetes orchestration, scalability testing, logging, and drift detection.

---

## 📂 Repository Structure and File Utility

### 📁 app/
Contains the **production API code**.

- **main.py**  
  FastAPI application that loads the trained model and exposes:
  - `/` → health check endpoint  
  - `/predict` → prediction endpoint  
  Includes per-request logging of:
  - input features
  - prediction
  - probability
  - inference latency

---

### 📁 artifacts/
Stores **binary artifacts generated after training**.

- **model.pkl**  
  Serialized (pickle) trained machine learning model.  
  This is the **final model artifact** used by:
  - FastAPI inference
  - Docker container
  - Kubernetes deployment

---

### 📁 data/
Contains the dataset used for training.

- **data.csv**  
  Heart Disease dataset (UCI-based).  
  Used for:
  - model training
  - explainability (SHAP)
  - fairness analysis
  - drift baseline comparison

---

### 📁 k8s/
Kubernetes manifests for deployment on **Google Kubernetes Engine (GKE)**.

- **deployment.yaml**  
  Defines the Kubernetes Deployment for the FastAPI service, including:
  - container image
  - CPU requests and limits
  - initial replica count

- **service.yaml**  
  Exposes the application using a **LoadBalancer**, enabling external access.

- **hpa.yaml**  
  Horizontal Pod Autoscaler configuration:
  - minimum pods: 1
  - maximum pods: 3
  - CPU-based autoscaling

---

### 📁 src/
Contains **training and local inference scripts**.

- **train.py**  
  Trains the heart disease classification model, performs preprocessing, evaluates performance, and saves the trained model to `artifacts/model.pkl`.

- **predict.py**  
  Script for local/offline inference using the trained model.

- **model.py**  
  Contains reusable model or preprocessing logic (if applicable).

---

## 📄 Root-Level Files

- **Dockerfile**  
  Docker configuration to containerize the FastAPI application along with the trained model.

- **requirements.txt**  
  Python dependencies required for training, inference, API, and analysis.

- **HeartDiseaseTrainingAndPrediction.ipynb**  
  Jupyter notebook covering:
  - exploratory data analysis
  - model training
  - SHAP explainability
  - fairness analysis using Fairlearn
  - input drift detection using KS-test

- **generate_and_predict.py**  
  Script that:
  - generates 100 random inference samples
  - sends them to the deployed API
  - saves inference data for drift detection

- **inference_data.csv**  
  Stores inference-time input data used for:
  - per-sample prediction
  - input drift detection

- **post.lua**  
  Lua script used by `wrk` to generate high-concurrency POST requests for performance and timeout analysis.

- **README.md**  
  Project documentation (this file).

- **MIOps_oppe_2.pdf / run_oppe2.raw**  
  Supporting documentation and notes related to OPPE submission and execution logs.

---

## 🔀 Dataset Splits Used for Training

- **Train/Test Split**  
  - 80% Training data  
  - 20% Test data  
  - Random split with fixed seed for reproducibility

- Missing values are handled during preprocessing.
- Categorical variables are encoded before training.

---

## 📦 Binary / Generated Artifacts

The following files are **generated artifacts** and not raw source code:

- `artifacts/model.pkl`  
  → Trained machine learning model (pickle format)

- `inference_data.csv`  
  → Generated inference dataset for drift analysis

These artifacts are required for:
- API inference
- deployment
- monitoring
- drift detection

---

## 🚀 Key MLOps Features Implemented

- Model explainability using **SHAP**
- Fairness analysis using **Fairlearn**
- FastAPI-based inference service
- Dockerized application
- Deployment on **Google Kubernetes Engine**
- Horizontal Pod Autoscaling (max pods = 3)
- Per-request logging and observability
- High-concurrency load testing using `wrk`
- Input drift detection using **KS-test**

---

## ✅ End-to-End Workflow

1. Train model (`src/train.py`)
2. Save trained model (`artifacts/model.pkl`)
3. Serve model via FastAPI (`app/main.py`)
4. Containerize using Docker
5. Deploy on GKE using Kubernetes manifests
6. Monitor performance, logs, scaling, and drift

---

## 📌 Notes

This repository is structured to demonstrate **production-grade MLOps practices** aligned with OPPE-2 evaluation requirements.

---
