from flask import Flask, request, render_template,jsonify
import pickle

application = Flask(__name__)
app = application

# Load models
standard_scaler = pickle.load(open('/Users/anirudhsharma/Desktop/Machine Learning/Projects/Diabetes_Predictor/models/standard_scaler.pkl', 'rb'))
predictor = pickle.load(open('/Users/anirudhsharma/Desktop/Machine Learning/Projects/Diabetes_Predictor/models/prediction_model.pkl', 'rb'))
encoder = pickle.load(open('/Users/anirudhsharma/Desktop/Machine Learning/Projects/Diabetes_Predictor/models/encoder.pkl', 'rb'))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['POST','GET'])
def predict_datapoint():
    if request.method == 'POST':
        gender = request.form.get('gender')
        age = int(request.form.get('age'))
        hypertension = int(request.form.get('hypertension'))
        heart_disease = int(request.form.get('heart_disease'))
        smoking_history = request.form.get('smoking_history')
        bmi = float(request.form.get('bmi'))
        HbA1c = float(request.form.get('HbA1c'))
        blood_glucose_level = float(request.form.get('blood_glucose_level'))

        # Encoding the New Data
        smoking_history_encoded = encoder.transform([[smoking_history]])
        print(smoking_history_encoded)
        # Encoding gender
        if gender == 'male':
            encoded_gender = 1
        elif gender == 'female':
            encoded_gender = 0
        else:
           encoded_gender=2

        # Standardization of the data
        new_data = standard_scaler.transform(
            [[encoded_gender, age, hypertension, heart_disease, *smoking_history_encoded[0].toarray()[0], bmi, HbA1c, blood_glucose_level]])
        print(new_data)
        # Prediction using the model
        result = predictor.predict(new_data)

        if result == 0:
            prediction = "Based on the provided data, it is predicted that you are not diabetic. However, it's important to maintain a healthy lifestyle and regular medical check-ups to ensure your well-being."
        else:
            prediction = "Based on the provided data, it is predicted that you are diabetic. It's crucial to consult with a healthcare professional for proper diagnosis and management of your condition."


        # Render prediction template with the result
        return jsonify({'prediction':prediction})

    else:
        return render_template('prediction.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
