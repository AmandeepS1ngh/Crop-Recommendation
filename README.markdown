# Crop Recommendation System

This project is a web-based application that recommends suitable crops to grow based on soil and environmental parameters using a machine learning model.

## Features

- Predicts the best crop based on input parameters: N (Nitrogen), P (Phosphorus), K (Potassium), temperature, humidity, pH, and rainfall.
- Utilizes a Random Forest Classifier trained on historical data.
- Provides a simple and intuitive web interface for users to input parameters and receive recommendations.

## Prerequisites

- Python 3.x
- Required Python libraries: Flask, joblib, numpy, scikit-learn, pandas

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AmandeepS1ngh/Crop-Recommendation.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Crop-Recommendation
   ```

3. Install the required libraries:
   ```bash
   pip install flask joblib numpy scikit-learn pandas
   ```

4. Run the application:
   ```bash
   python app.py
   ```

## Usage

1. Open your web browser and go to `http://localhost:5000` (or the port specified when running the app).
2. Enter the values for N, P, K, temperature, humidity, pH, and rainfall in the form.
3. Click on the "Predict" button to get the recommended crop.

## Screenshots

### Input Form
The input form allows users to enter soil and environmental parameters to get a crop recommendation.

![Input Form](https://github.com/AmandeepS1ngh/Crop-Recommendation/blob/main/screenshots/input_form.jpg)

### Prediction Result
After submitting the parameters, the app displays the recommended crop along with the top 3 predictions and their confidence scores.

![Prediction Result](https://github.com/AmandeepS1ngh/Crop-Recommendation/blob/main/screenshots/prediction_result.jpg)

## Model Information

The recommendation model is built using a Random Forest Classifier from scikit-learn with the following parameters:

- Number of estimators: 100
- Random state: 42

The model achieved a training accuracy of 100% and a test accuracy of 99.32%, indicating high reliability in its predictions.

## Data

The model is trained on a dataset containing historical data of crop yields based on various soil and environmental conditions. The dataset includes parameters such as N, P, K, temperature, humidity, pH, and rainfall, along with the corresponding crop labels.

## Project Structure

| File/Folder            | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| `app.py`               | The Flask application script for the web interface.                         |
| `model.ipynb`          | Jupyter notebook with code for training the machine learning model.         |
| `crop_model.pkl`       | Pickle file containing the trained Random Forest model.                     |
| `scaler.pkl`           | Pickle file containing the scaler used for feature scaling.                 |
| `Crop_recommendation.csv` | Dataset used for training the model.                                     |
| `static/`              | Directory for static files (CSS, JavaScript, images).                       |
| `templates/`           | Directory for HTML templates used by the Flask app.                        |
| `tempCodeRunnerFile.py`| Temporary file, likely not essential for the project.                       |

