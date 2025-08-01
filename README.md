# pred_depression_model

# 🧠 Student Depression Prediction Using Machine Learning

This project is a **Flask web app** that uses **Multinomial Logistic Regression** to predict whether a student is likely to have depression based on input features such as **CGPA, Age, Gender, and Academic Pressure**.

---

## 🚀 Features

- Predict student depression likelihood from basic academic and demographic data
- User-friendly HTML form for input
- Machine learning model built using:
  - pandas, scikit-learn, seaborn, matplotlib, numpy
- Deployable locally or on a server

---

## 🗂️ Folder Structure

```text
ML_project/
├── app.py                                 # Flask backend
├── DataSet/
│   └── student_depression_dataset.csv
├── model/                                 # Flask backend
│   ├── depression_model.joblib            # Trained model
│   └── scaler.joblib                      # Scaler used to preprocess input
├── templates/
│   └── index.html                         # HTML form interface
├── requirements.txt                       # Python dependencies
└── README.md                              # Project description
```


---

## 📊 Input Features

| Feature            | Type     | Description                          |
|--------------------|----------|--------------------------------------|
| CGPA               | float    | Cumulative GPA of the student        |
| Age                | float    | Age of the student                   |
| Gender             | string   | 'Male' or 'Female'                   |
| Academic Pressure  | float    | Scale of academic stress (1 to 5)    |

---

