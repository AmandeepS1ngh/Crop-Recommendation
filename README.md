# Crop-Recommendation
Crop Recommendation System
This project is a web-based application that recommends suitable crops to grow based on soil and environmental parameters using a machine learning model.
Features

Predicts the best crop based on input parameters: N (Nitrogen), P (Phosphorus), K (Potassium), temperature, humidity, pH, and rainfall.
Utilizes a Random Forest Classifier trained on historical data.
Provides a simple and intuitive web interface for users to input parameters and receive recommendations.

Prerequisites

Python 3.x
Required Python libraries: Flask, joblib, numpy, scikit-learn, pandas

Installation

Clone the repository:
git clone https://github.com/AmandeepS1ngh/Crop-Recommendation.git


Navigate to the project directory:
cd Crop-Recommendation


Install the required libraries:
pip install flask joblib numpy scikit-learn pandas


Run the application:
python app.py



Usage

Open your web browser and go to http://localhost:5000 (or the port specified when running the app).
Enter the values for N, P, K, temperature, humidity, pH, and rainfall in the form.
Click on the "Predict" button to get the recommended crop.

Model Information
The recommendation model is built using a Random Forest Classifier from scikit-learn with the following parameters:

Number of estimators: 100
Random state: 42

The model achieved a training accuracy of 100% and a test accuracy of 99.32%, indicating high reliability in its predictions.
Data
The model is trained on a dataset containing historical data of crop yields based on various soil and environmental conditions. The dataset includes parameters such as N, P, K, temperature, humidity, pH, and rainfall, along with the corresponding crop labels.
Project Structure



File/Folder
Description



app.py
The Flask application script for the web interface.


model.ipynb
Jupyter notebook with code for training the machine learning model.


crop_model.pkl
Pickle file containing the trained Random Forest model.


scaler.pkl
Pickle file containing the scaler used for feature scaling.


Crop_recommendation.csv
Dataset used for training the model.


static/
Directory for static files (CSS, JavaScript, images).


templates/
Directory for HTML templates used by the Flask app.


tempCodeRunnerFile.py
Temporary file, likely not essential for the project.

