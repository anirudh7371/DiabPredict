# DiabPredict

DiabPredict is an intelligent diabetes prediction system developed using machine learning techniques. It accurately predicts the likelihood of diabetes in patients based on comprehensive medical and demographic data, achieving an impressive accuracy score of 95.2%.

## About the Project

DiabPredict utilizes logistic regression to analyze a dataset containing medical and demographic features such as age, gender, body mass index (BMI), hypertension, heart disease, smoking history, HbA1c level, and blood glucose level. The project aims to assist healthcare professionals in identifying individuals at risk of developing diabetes and devising personalized treatment plans accordingly.

## Project Structure
- **notebooks/**: Directory containing Jupyter notebook for data preprocessing and model training (`LogisticRegression.ipynb`).
- **dataset/**: Contains two datasets: one raw and the other cleaned.
- **application.py**: Flask application for deploying the trained model as a web service.
- **templates/**: Directory containing HTML templates for the web interface.
- **models/**: Directory containing serialized trained models and scalers.
- **requirements.txt**: List of Python dependencies required to run the project.
- **README.md**: Documentation file providing an overview of the project and instructions for running it.

## Key Features

- Advanced Machine Learning: Harnesses the power of logistic regression to analyze and predict diabetes risk.
- Comprehensive Dataset: Utilizes a rich collection of medical and demographic data sourced from patients, enabling accurate predictions.
- User-Friendly Interface: Features an intuitive web application interface developed using Flask, HTML, CSS, and JavaScript for seamless interaction.

## Key Metrics

- Accuracy Score: 95.2%
- Precision: 99.12%
- Recall Score: 96.52%
- F Beta Score: 97.80


## Installation

To install DiabPredict and run it locally, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/DiabPredict.git
   ```

2. Navigate to the project directory:
   ```
   cd DiabPredict
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   
   For Windows System
   ```
   python application.py
   ```
   For Mac System
   ```
   python3 application.py
   ```

## Usage

1. Open your web browser and navigate to `http://localhost:5000`.
2. Input patient data including age, gender, BMI, hypertension, heart disease, smoking history, HbA1c level, and blood glucose level.
3. Click the "Predict" button to obtain the diabetes prediction result.

## Contributions

Contributions are welcome! If you'd like to contribute to DiabPredict, please submit a pull request with your proposed changes.
