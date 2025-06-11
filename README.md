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

## 🌐 Live Demo

[Click here to view the deployed app on Streamlit Cloud](https://your-deployment-url)

## ✍️ Author

- Ishwari Wankhade
- Email: irwankhade05@gmail.com


