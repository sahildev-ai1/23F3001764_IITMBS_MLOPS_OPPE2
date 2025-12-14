# OPPE AI Usage Documentation  
## AI Tools Utilized and Conversation History

This document declares the usage of AI tools during the MLOps OPPE-2 examination, in accordance with the academic integrity and disclosure requirements.

---

## 🧠 AI Tools Utilized

### Tool Name: ChatGPT (OpenAI)
**Purpose:**  
- Understanding MLOps concepts and architecture  
- Debugging Python, Docker, Kubernetes, and GCP issues  
- Guidance on SHAP explainability, Fairlearn fairness metrics, and drift detection  
- Structuring CI/CD workflows and Kubernetes autoscaling  
- Preparing documentation, presentation structure, and demo commands  

**Shared Chat Link:**  
- Link 1: https://chatgpt.com/share/693ec251-ac5c-800d-a159-684b4cd3712d
- Link 2: https://chatgpt.com/share/693ec2ed-2b9c-800b-b308-f78dca7829be  
- Link 3: https://chatgpt.com/share/693ec31a-00a4-800d-88f5-938ccd10a093

**Notes (optional):**  
The AI tool was used strictly as an assistive aid. All final code execution, deployment, testing, and validation were performed independently by the learner.

---

## 📝 Prompts and Responses Used

### Tool Name #1: ChatGPT (OpenAI)

---

### Prompt 1:
> Explain SHAP values for false negative heart disease predictions in simple terms.

**Response Log:**  
The response explained how SHAP values indicate feature contributions, identifying factors such as cholesterol, chest pain type, and exercise-induced angina that influenced missed predictions. This helped in interpreting model behavior for explainability deliverables.

---

### Prompt 2:
> How to test model fairness using Fairlearn with age as a sensitive attribute?

**Response Log:**  
The response provided guidance on creating age buckets, using Fairlearn’s MetricFrame, demographic parity difference, and equalized odds difference to evaluate fairness across age groups.

---

### Prompt 3:
> Convert a trained ML model into a FastAPI application and deploy it using Docker and Kubernetes.

**Response Log:**  
The response outlined steps to create a FastAPI app, dockerize it, deploy it on GKE, expose it via LoadBalancer, and configure Horizontal Pod Autoscaling.

---

### Prompt 4:
> How to perform high concurrency load testing using wrk and observe Kubernetes autoscaling?

**Response Log:**  
The response explained using `wrk` with high concurrency settings, interpreting latency and timeout behavior, and monitoring pod scaling using Kubernetes commands.

---

### Prompt 5:
> How to detect input data drift between training data and inference data?

**Response Log:**  
The response suggested using statistical tests such as the Kolmogorov–Smirnov (KS) test to compare feature distributions and interpret drift results.

---

## 📌 Declaration

I declare that:
- AI tools were used responsibly and transparently
- AI assistance was limited to guidance, explanation, and debugging support
- All implementation, execution, deployment, and evaluation were performed by me

---

**Learner Name:** Sahil Raj 
**Roll Number:** 23f3001764
**Course:** IIT Madras BS — MLOps OPPE-2  
