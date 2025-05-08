from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the saved model and scaler
model = joblib.load('crop_model.pkl')
scaler = joblib.load('scaler.pkl')

# Home route to display the input form
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route to handle form submission
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from the form and convert to floats
        features = [
            float(request.form['N']),
            float(request.form['P']),
            float(request.form['K']),
            float(request.form['temperature']),
            float(request.form['humidity']),
            float(request.form['ph']),
            float(request.form['rainfall'])
        ]
        
        # Convert to 2D array and scale the input
        features_array = np.array([features])
        scaled_features = scaler.transform(features_array)
        
        # Make prediction
        prediction = model.predict(scaled_features)[0]
        
        # Get top 3 predictions with probabilities
        probas = model.predict_proba(scaled_features)[0]
        top_indices = probas.argsort()[-3:][::-1]  # Top 3 indices in descending order
        top_crops = model.classes_[top_indices]
        top_probs = probas[top_indices]
        
        # Prepare result for display
        result = {
            'predicted_crop': prediction,
            'top_predictions': [
                {'crop': crop, 'probability': f"{prob:.2%}"}
                for crop, prob in zip(top_crops, top_probs)
            ]
        }
        
        return render_template('result.html', result=result)
    except ValueError:
        return "Error: Please enter valid numeric values for all fields."
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)