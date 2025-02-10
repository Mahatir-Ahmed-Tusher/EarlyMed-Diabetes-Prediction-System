from flask import Flask, request, render_template
import pandas as pd
import pickle

# Initialize Flask app
app = Flask(__name__)

# Load the trained model and scaler
try:
    with open('xgb_tuned_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    with open('scaler.pkl', 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
except Exception as e:
    print("Error loading model or scaler:", str(e))
    raise

# Define the feature columns used during training
feature_columns = [
    'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI',
    'DiabetesPedigreeFunction', 'Age', 'NewBMI_Obesity_1', 'NewBMI_Obesity_2',
    'NewBMI_Obesity_3', 'NewBMI_Overweight', 'NewBMI_Underweight',
    'NewInsulinScore_Normal', 'NewGlucose_Low', 'NewGlucose_Normal',
    'NewGlucose_Overweight', 'NewGlucose_Secret'
]

# Function to create BMI categories
def create_bmi_categories(input_df):
    input_df['NewBMI_Underweight'] = (input_df['BMI'] < 18.5).astype(int)
    input_df['NewBMI_Overweight'] = ((input_df['BMI'] >= 25) & (input_df['BMI'] < 30)).astype(int)
    input_df['NewBMI_Obesity_1'] = ((input_df['BMI'] >= 30) & (input_df['BMI'] < 35)).astype(int)
    input_df['NewBMI_Obesity_2'] = ((input_df['BMI'] >= 35) & (input_df['BMI'] < 40)).astype(int)
    input_df['NewBMI_Obesity_3'] = (input_df['BMI'] >= 40).astype(int)
    return input_df

# Function to create glucose categories
def create_glucose_categories(input_df):
    input_df['NewGlucose_Low'] = (input_df['Glucose'] < 70).astype(int)
    input_df['NewGlucose_Normal'] = ((input_df['Glucose'] >= 70) & (input_df['Glucose'] < 140)).astype(int)
    input_df['NewGlucose_Overweight'] = ((input_df['Glucose'] >= 140) & (input_df['Glucose'] < 200)).astype(int)
    input_df['NewGlucose_Secret'] = (input_df['Glucose'] >= 200).astype(int)
    return input_df

# Function to create insulin score
def create_insulin_score(input_df):
    input_df['NewInsulinScore_Normal'] = ((input_df['Insulin'] >= 16) & (input_df['Insulin'] <= 166)).astype(int)
    return input_df

# Route for the home page (renders the frontend)
@app.route('/')
def home():
    return render_template('index.html')

# Route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the form
        pregnancies = float(request.form['pregnancies'])
        glucose = float(request.form['glucose'])
        blood_pressure = float(request.form['blood_pressure'])
        skin_thickness = float(request.form['skin_thickness'])
        insulin = float(request.form['insulin'])
        bmi = float(request.form['bmi'])
        diabetes_pedigree = float(request.form['diabetes_pedigree'])
        age = float(request.form['age'])

        # Create a DataFrame from the input data
        input_data = {
            'Pregnancies': [pregnancies],
            'Glucose': [glucose],
            'BloodPressure': [blood_pressure],
            'SkinThickness': [skin_thickness],
            'Insulin': [insulin],
            'BMI': [bmi],
            'DiabetesPedigreeFunction': [diabetes_pedigree],
            'Age': [age]
        }
        input_df = pd.DataFrame(input_data)

        # Create BMI, glucose, and insulin categories
        input_df = create_bmi_categories(input_df)
        input_df = create_glucose_categories(input_df)
        input_df = create_insulin_score(input_df)

        # Ensure the input data has the correct feature columns
        input_df = input_df[feature_columns]

        # Scale the input data using the pre-trained scaler
        scaled_data = scaler.transform(input_df)

        # Make a prediction using the loaded model
        prediction = model.predict(scaled_data)

        # Convert the prediction to a human-readable response
        result = 'Diabetic' if prediction[0] == 1 else 'Not Diabetic'

        # Return the prediction as plain text
        return result

    except KeyError as ke:
        # Handle missing form fields
        error_message = f"Missing input field: {str(ke)}"
        print(error_message)
        return error_message, 400

    except ValueError as ve:
        # Handle invalid numeric values
        error_message = f"Invalid input value: {str(ve)}"
        print(error_message)
        return error_message, 400

    except Exception as e:
        # Handle any other errors
        error_message = f"Error during prediction: {str(e)}"
        print(error_message)
        return error_message, 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)