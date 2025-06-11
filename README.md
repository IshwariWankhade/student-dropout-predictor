# 🎓 Student Dropout Predictor

This project is an ML-powered Streamlit web app that predicts the likelihood of a student dropping out based on various features such as academic engagement, parental involvement, and student activity.

## 🚀 Features

- User-friendly web interface built with Streamlit
- Predicts student dropout risk: High Risk or Likely to Continue
- Trained using a dataset from Kaggle (xAPI-Edu-Data)

## 📊 Dataset

- **Source**: [xAPI-Edu-Data - Kaggle](https://www.kaggle.com/datasets/aljarah/xAPI-Edu-Data)
- **Attributes Used**: Gender, Nationality, Stage, Topic, Semester, Raised Hands, Absence Days, etc.

## 🧠 Model

- Model trained using **RandomForestClassifier** / **XGBoost**
- Categorical data encoded using `category` codes
- Model serialized using `joblib`

## 🛠 How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/YourUsername/student-dropout-predictor.git
    cd student-dropout-predictor
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the app:
    ```bash
    streamlit run app.py
    ```

## 📊 Model Evaluation

The model was evaluated using a test dataset (20% split). Below are the performance metrics:

- **Accuracy:** 89.58%
- **Precision (Dropout):** 83%
- **Recall (Dropout):** 68%
- **F1-score (Dropout):** 75%

## 🌐 Live Demo

👉 [Click here to view the deployed app](https://student-dropout-predictor-czgvv7gvr8x3kvpir6brbz.streamlit.app/)

## ✍️ Author

- Ishwari Wankhade
- Email: irwankhade05@gmail.com


