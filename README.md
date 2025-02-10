# EarlyMed - Diabetes Prediction System

![Logo](https://i.postimg.cc/8cfd458T/logo.png)

**EarlyMed** is a Senior Design Project developed by a passionate team of students from VIT-AP University. This system predicts the likelihood of diabetes based on health parameters using machine learning. It is designed to assist users in early diagnosis and encourage them to seek professional medical advice.

---

## Table of Contents

1. [Overview](#overview)
2. [Dataset Details](#dataset-details)
3. [Features](#features)
4. [Technologies Used](#technologies-used)
5. [Project Structure](#project-structure)
6. [Setup Instructions](#setup-instructions)
7. [Usage](#usage)
8. [Deployment](#deployment)
9. [Dependencies](#dependencies)
10. [Acknowledgments](#acknowledgments)
11. [Contributors](#contributors)
12. [License](#license)

---

## Overview

The **Diabetes Prediction System** uses a trained machine learning model (XGBoost) to predict whether a patient is likely to have diabetes based on their health parameters. The system is built using Flask for the backend and HTML/CSS/JavaScript for the frontend. It also includes feature engineering to improve prediction accuracy.

---

## Dataset Details

### Context
This dataset originates from the **National Institute of Diabetes and Digestive and Kidney Diseases (NIDDK)**. The objective of the dataset is to diagnostically predict whether or not a patient has diabetes, based on certain diagnostic measurements included in the dataset. Several constraints were placed on the selection of these instances from a larger database. In particular, all patients here are females aged at least 21 years old of Pima Indian heritage, a population known to be at higher risk for diabetes.

### Content
The dataset consists of **768 observations** and **9 variables**, including both predictor features and a target variable. 

#### Key Features in the Dataset:
- **Pregnancies**: Number of times the patient has been pregnant.
- **Glucose**: Plasma glucose concentration measured during an oral glucose tolerance test.
- **BloodPressure**: Diastolic blood pressure in mm Hg.
- **SkinThickness**: Triceps skin fold thickness in mm, an indicator of body fat.
- **Insulin**: Serum insulin level in mu U/ml after 2 hours.
- **BMI**: Body Mass Index, calculated as weight in kilograms divided by height in meters squared.
- **DiabetesPedigreeFunction**: A score indicating the likelihood of diabetes based on family history.
- **Age**: Patient’s age in years.
- **Outcome**: The target variable, where `0` indicates no diabetes and `1` indicates diabetes.

This structured dataset provides a robust foundation for building predictive models that can identify individuals at risk of diabetes.

### Acknowledgements
The dataset was originally published in the following paper:

Smith, J.W., Everhart, J.E., Dickson, W.C., Knowler, W.C., & Johannes, R.S. (1988).  
**Using the ADAP learning algorithm to forecast the onset of diabetes mellitus.**  
In *Proceedings of the Symposium on Computer Applications and Medical Care* (pp. 261–265). IEEE Computer Society Press.

---

## Features

- **User-Friendly Interface**: A clean and intuitive frontend for entering health parameters.
- **Machine Learning Model**: Trained XGBoost model for accurate predictions.
- **Feature Engineering**: Automatically generates additional features (e.g., BMI categories, glucose levels).
- **Scalability**: Designed to handle large datasets and can be deployed on cloud platforms like Render.
- **Error Handling**: Provides meaningful error messages for invalid inputs or server issues.

Live Link of the web app: https://earlymed-diabetes-prediction-system.onrender.com/
---

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning**: XGBoost, Scikit-Learn, Pandas
- **Deployment**: Gunicorn, Render
- **Tools**: VS Code, Postman, Curl

---

## Project Structure

```
EarlyMed-Diabetes-Prediction-System/
│
├── app.py                # Flask backend
├── xgb_tuned_model.pkl   # Trained XGBoost model
├── scaler.pkl            # Pre-trained scaler
├── requirements.txt      # List of dependencies            
└── templates/            # Folder for HTML templates
    └── index.html        # Frontend
```

---

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Pip (Python package manager)
- Virtual environment (optional but recommended)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Mahatir-Ahmed-Tusher/EarlyMed-Diabetes-Prediction-System.git
   cd EarlyMed-Diabetes-Prediction-System
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the App Locally**:
   ```bash
   python app.py
   ```
   - Open your browser and navigate to `http://127.0.0.1:5000/`.

---

## Usage

1. Open the app in your browser.
2. Fill out the form with the following health parameters:
   - Pregnancies
   - Glucose
   - Blood Pressure
   - Skin Thickness
   - Insulin
   - BMI
   - Diabetes Pedigree Function
   - Age
3. Click the **Predict** button.
4. The app will display the prediction (`Diabetic` or `Not Diabetic`) below the form.

---

## Deployment

### Deploying to Render

1. **Push Your Code to GitHub**:
   - Commit your code and push it to a GitHub repository.

2. **Create a New Web Service on Render**:
   - Go to [Render](https://render.com/) and create a new **Web Service**.
   - Link your GitHub repository.

3. **Configure Build and Start Commands**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn --workers=1 --bind 0.0.0.0:$PORT app:app`

4. **Deploy**:
   - Render will automatically deploy your app. Once deployed, you’ll get a public URL.

---

## Dependencies

The project requires the following Python libraries:

- `flask`: Web framework for building the backend.
- `gunicorn`: Production-ready WSGI server.
- `pandas`: Data manipulation and analysis.
- `scikit-learn`: Machine learning library for preprocessing and scaling.
- `xgboost`: Gradient boosting library for the predictive model.

You can install all dependencies using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

---

## Acknowledgments

We express our gratitude to the following:

- **Dataset Contributors**:  
  Smith, J.W., Everhart, J.E., Dickson, W.C., Knowler, W.C., & Johannes, R.S. (1988).  
  *Using the ADAP learning algorithm to forecast the onset of diabetes mellitus.*  
  Proceedings of the Symposium on Computer Applications and Medical Care (pp. 261–265). IEEE Computer Society Press.

- **Team Members**:  
  - **Saket Choudary Kongara**: For his valuable feedback and contributions to the project.  
  - **Sivamani Vangapalli**: For his insights and support during development.

- **Faculty and Mentors**:  
  Special thanks to the faculty and mentors at VIT-AP University for their guidance and encouragement throughout the project.

---

## Contributors

This project was developed by the following contributors:

- **Mahatir Ahmed Tusher** ([GitHub Profile](https://github.com/Mahatir-Ahmed-Tusher))
- **Saket Choudary Kongara**
- **Sivamani Vangapalli**



---

Feel free to contribute to this project or report issues via GitHub. Let’s make healthcare more accessible together! 🌟


