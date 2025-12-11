import streamlit as st
import pickle
import numpy as np

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Autism Risk Prediction",
    page_icon="🧩",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Load Model
# -----------------------------
model = pickle.load(open("model/autism_model.pkl", "rb"))

# -----------------------------
# Sidebar Tabs / Menu
# -----------------------------
st.sidebar.title("Autism Risk Prediction")
menu = st.sidebar.radio("Navigation", ["Prediction", "About", "Instructions"])

# -----------------------------
# Tabs / Pages
# -----------------------------
if menu == "About":
    st.title("🧩 Autism Risk Prediction Web App")
    st.write("""
        This web app predicts the **Autism Risk (Class/ASD)** based on user inputs.
        It is powered by a **Random Forest Classifier** trained on the Autism Screening dataset.
    """)
    st.image("assets/autism_logo.png", width=300)  # Optional image/logo in assets folder

elif menu == "Instructions":
    st.title("📖 Instructions")
    st.markdown("""
    1. Go to the **Prediction** tab.  
    2. Fill out all the required fields in the sidebar.  
    3. Click the **Predict** button.  
    4. The model will display a **risk prediction** with confidence.  
    """)

elif menu == "Prediction":
    st.title("🧩 Predict Autism Risk")
    st.write("Enter the features in the sidebar and click **Predict**.")

    # -----------------------------
    # User Inputs in Sidebar
    # -----------------------------
    st.sidebar.header("User Input Features")

    # Columns for scores
    col1, col2, col3, col4, col5 = st.sidebar.columns(5)
    A1_Score = col1.radio("A1", [0,1])
    A2_Score = col2.radio("A2", [0,1])
    A3_Score = col3.radio("A3", [0,1])
    A4_Score = col4.radio("A4", [0,1])
    A5_Score = col5.radio("A5", [0,1])
    A6_Score = col1.radio("A6", [0,1])
    A7_Score = col2.radio("A7", [0,1])
    A8_Score = col3.radio("A8", [0,1])
    A9_Score = col4.radio("A9", [0,1])
    A10_Score = col5.radio("A10", [0,1])

    # Other features
    age = st.sidebar.slider("Age", 0, 60, 25)
    gender = st.sidebar.selectbox("Gender", ["Male","Female"])
    ethnicity = st.sidebar.selectbox("Ethnicity", ["White-European","Indian","Others","?"])
    jaundice = st.sidebar.selectbox("Jaundice", ["Yes","No"])
    austim = st.sidebar.selectbox("Austim", ["Yes","No"])
    country = st.sidebar.selectbox("Country", ["India","USA","Austria","Others"])
    used_app_before = st.sidebar.selectbox("Used App Before", ["Yes","No"])
    relation = st.sidebar.selectbox("Relation", ["Self","Parent","Others"])
    result = st.sidebar.number_input("Result", 0.0, 20.0, 6.0)

    # -----------------------------
    # Encode categorical features
    # -----------------------------
    gender = 1 if gender=="Male" else 0
    jaundice = 1 if jaundice=="Yes" else 0
    austim = 1 if austim=="Yes" else 0
    used_app_before = 1 if used_app_before=="Yes" else 0

    ethnicity_map = {"White-European":0,"Indian":1,"Others":2,"?":3}
    country_map = {"India":1,"USA":2,"Austria":3,"Others":0}
    relation_map = {"Self":0,"Parent":1,"Others":2}

    input_data = np.array([[A1_Score,A2_Score,A3_Score,A4_Score,A5_Score,
                            A6_Score,A7_Score,A8_Score,A9_Score,A10_Score,
                            age, gender, ethnicity_map[ethnicity], jaundice, austim,
                            country_map[country], used_app_before, relation_map[relation], result]])

    # -----------------------------
    # Predict button
    # -----------------------------
    if st.button("Predict"):
        prediction = model.predict(input_data)
        pred_proba = model.predict_proba(input_data)[0][1] if hasattr(model, "predict_proba") else None

        if prediction[0] == 0:
            result_text = "✅ Low Risk / Not Autistic"
            st.success(result_text)
        else:
            result_text = "⚠️ High Risk / Likely Autistic"
            st.error(result_text)

        if pred_proba is not None:
            st.info(f"Prediction Confidence: {pred_proba*100:.2f}%")
