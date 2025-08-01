from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('model/depression_model.joblib')
scaler = joblib.load('model/scaler.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    cgpa = float(request.form['cgpa'])
    age = float(request.form['age'])
    gender = 1 if request.form['gender'].lower() == 'male' else 0
    academic_pressure = float(request.form['academic_pressure'])

    input_df = pd.DataFrame([[cgpa, age, gender, academic_pressure]],
                            columns=['CGPA', 'Age', 'Gender', 'Academic Pressure'])
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)[0]

    result = "Likely to have Depression" if prediction == 1 else "Not Likely to have Depression"
    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
