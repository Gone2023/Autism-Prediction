#  Autism Prediction System

**Author:** Govind  

A machine learning–based screening tool that predicts the likelihood of Autism Spectrum Disorder (ASD) using questionnaire responses and demographic data.

>  **Disclaimer:** This is an educational screening tool and **not a medical diagnostic system**.

---

##  Overview

The Autism Prediction System classifies individuals into:

- **Low Risk (0)**
- **High Risk (1)**

This project demonstrates a complete end-to-end machine learning pipeline, including:

- Data preprocessing  
- Feature engineering  
- Model training and evaluation  
- Model serialization  
- Interactive application interface  

---

##  Features

- End-to-end ML workflow  
- Handles both categorical and numerical features  
- Binary ASD risk prediction  
- Pretrained model included (`autism_model.pkl`)  
- Interactive UI using Streamlit  
- Well-structured notebooks  

---

##  Dataset

### Features
- 10 ASD screening question scores (binary)  
- Age  
- Gender  
- Ethnicity  
- Jaundice history (Yes/No)  
- Family autism history  
- Relation to the individual  
- Country of residence  

### Target
- `0 → Low Risk`  
- `1 → High Risk`  

---

##  Data Preprocessing

- Label encoding of categorical features  
- Normalization of numerical values  
- Handling missing or inconsistent data  
- Feature vector construction  

---

##  Model Development

### Algorithms Explored
- Logistic Regression  
- Random Forest  
- Support Vector Classifier (SVC)  
- Gradient Boosting  

### Final Model
- autism_model.pkl


---

##  Evaluation Metrics

- Accuracy  
- Precision  
- Recall  
- F1 Score  
- Confusion Matrix  

Detailed results are available in the notebooks.

---

##  Usage Guide

### Input Fields
- Age  
- Gender  
- Ethnicity  
- Jaundice (Yes/No)  
- Family autism history  
- Relation  
- Country of residence  
- 10 ASD screening question responses  

### Output
- Prediction: **Low Risk / High Risk**  
- Optional: Probability score  

---

##  How to Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/autism-prediction-system.git
cd autism-prediction-system
``` 
### 2. Install dependencies
```bash    
pip install -r requirements.txt
```
### 3. Run Streamlit app
```bash
streamlit run app.py
```
### Future Improvements
- Full frontend (HTML, CSS, JavaScript)
- Backend API using Flask or FastAPI
- Improved UI/UX
- Database integration
- Cloud deployment
- SHAP / feature importance visualization

###  License
This project is licensed under the MIT License.

###  Contact
Govind
B.Tech CSE, Bennett University
