Autism Prediction System

Author: Govind

A machine-learning–based autism screening tool that predicts the likelihood of Autism Spectrum Disorder (ASD) using questionnaire responses and demographic information.
This project includes data preprocessing pipelines, model training notebooks, the final saved model, and an interactive interface for running predictions.

Note: This is an educational screening tool, not a medical diagnostic system.

1. Overview

The Autism Prediction System is designed to classify individuals as Low Risk or High Risk of Autism Spectrum Disorder (ASD).
It demonstrates end-to-end ML development, including:

Dataset analysis

Preprocessing and encoding

Model training and evaluation

Exporting and loading ML models

Building a simple application interface

2. Features

End-to-end ML workflow

Handles both categorical and numerical features

Produces binary ASD risk predictions

Includes a pretrained model (autism_model.pkl)

Streamlit interface for interactive use

Well-organized notebook analysis

3. Dataset

The dataset includes:

Ten ASD screening question scores (binary)

Age

Gender

Ethnicity

Jaundice history

Family autism history

Relation to child

Country of residence

ASD risk label: 0 (Low Risk), 1 (High Risk)

Preprocessing includes:

Label encoding of categorical values

Normalizing numeric inputs

Cleaning and validating entries

Constructing the final feature vector

4. Model Development
4.1 Preprocessing

Encoding categorical features

Normalization

Handling missing or inconsistent entries

4.2 Algorithms Explored

Multiple supervised learning algorithms were evaluated, such as:

Logistic Regression

Random Forest

Support Vector Classifier

Gradient Boosting

The final model is stored as:

autism_model.pkl

4.3 Evaluation Metrics

Model performance is assessed using:

Accuracy

Precision

Recall

F1 Score

Confusion Matrix

Detailed results are available in the accompanying notebooks.

5. Usage Guide
Input Fields

The application collects:

Age

Gender

Ethnicity

Jaundice (Yes/No)

Family autism history

Relation to the child

Ten ASD screening questions

Country of residence

Output

The model returns:

Prediction: Low Risk or High Risk

Optional: Probability of the prediction

6. Future Improvements

Planned enhancements:

Replacing Streamlit with a complete web frontend (HTML/CSS/JS)

Backend API using Flask or FastAPI

Improved UI/UX

Optional database integration

Deployment on cloud platforms

Adding SHAP/feature-importance visualizations

7. Limitations

Not suitable for clinical diagnosis

Dataset size is limited

Depends heavily on self-reported questionnaire data

Model accuracy varies with demographic encoding

8. License

This project is licensed under the MIT License.

9. Acknowledgements

Public ASD Screening Dataset

scikit-learn and Streamlit open-source communities

10. Contact

Govind
B.Tech CSE, Bennett University
