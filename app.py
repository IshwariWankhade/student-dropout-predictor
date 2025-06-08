import streamlit as st
import pandas as pd
import joblib

# Load your trained model
model = joblib.load("model.pkl")

st.title("🎓 Student Dropout Predictor")

st.write("Enter the student details:")

# Inputs for categorical features (selectbox)
gender = st.selectbox("Gender", ["Male", "Female"])

nationality = st.selectbox("Nationality", [
    "UK", "USA", "Italy", "Egypt", "Thailand", "India", "Japan", 
    "South Korea", "Germany", "Russia", "Mexico", "SaudiArabia", "Nepal", "Australia"])

stage_id = st.selectbox("StageID", ["lowerlevel", "MiddleSchool", "HighSchool"])

topic = st.selectbox("Topic", ["Physics", "Math", "English", "Science", 
                              "History", "Biology", "Chemistry"])

semester = st.selectbox("Semester", ["First", "Second", "Third", "Fourth"])

relation = st.selectbox("Relation", ["Father", "Mother", "Other"])

absence_days = st.selectbox("Student Absence Days", ["Under-7", "Above-7", "Zero"])

parent_answering = st.selectbox("Parent Answering Survey", ["Yes", "No"])

parent_school_satisfaction = st.selectbox("Parent School Satisfaction", ["Good", "Bad"])

# Inputs for numerical features (sliders or number inputs)
raised_hands = st.slider("Raised Hands", 0, 100, 20)
visited_resources = st.slider("Visited Resources", 0, 100, 20)
announcements_view = st.slider("Announcements View", 0, 100, 20)
discussion = st.slider("Discussion Participation", 0, 100, 20)

# Build a DataFrame for model input
input_dict = {
    "gender": [gender],
    "NationalITy": [nationality],
    "StageID": [stage_id],
    "Topic": [topic],
    "Semester": [semester],
    "Relation": [relation],
    "raisedhands": [raised_hands],
    "VisITedResources": [visited_resources],
    "AnnouncementsView": [announcements_view],
    "Discussion": [discussion],
    "ParentAnsweringSurvey": [parent_answering],
    "ParentschoolSatisfaction": [parent_school_satisfaction],
    "StudentAbsenceDays": [absence_days]
}

input_df = pd.DataFrame(input_dict)

# Encode categorical variables as in training (category codes)
categorical_cols = [
    "gender", "NationalITy", "StageID", "Topic", "Semester", "Relation",
    "ParentAnsweringSurvey", "ParentschoolSatisfaction", "StudentAbsenceDays"
]

for col in categorical_cols:
    input_df[col] = input_df[col].astype('category').cat.codes

# Predict button
if st.button("Predict Dropout Risk"):
    prediction = model.predict(input_df)
    if prediction[0] == 1:
        st.error("⚠️ High Risk of Dropout")
    else:
        st.success("✅ Student Likely to Continue")
