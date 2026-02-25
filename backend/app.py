from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import joblib
import os
from datetime import datetime

# SHAP for explainability
import shap

# Supabase integration
from supabase import create_client, Client

SUPABASE_URL = "https://pnkziwbngtddjsuusocp.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBua3ppd2JuZ3RkZGpzdXVzb2NwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzIwNTM4ODEsImV4cCI6MjA4NzYyOTg4MX0.1SufwjGNU0CkcsrI8oJEZQU0FJBjO6DFfq8P5p0hT70"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
app = Flask(__name__)
CORS(app)

# Load ML model and label encoder
MODEL_PATH = os.path.join(os.path.dirname(__file__), "rf_model.pkl")
ENCODER_PATH = os.path.join(os.path.dirname(__file__), "label_encoder.pkl")

# Check if models exist, if not train them
if not os.path.exists(MODEL_PATH) or not os.path.exists(ENCODER_PATH):
    print("Models not found. Training models...")
    os.system("python train_model.py")

rf_model = joblib.load(MODEL_PATH)
label_encoder = joblib.load(ENCODER_PATH)

# SHAP explainer setup
explainer = shap.TreeExplainer(rf_model)

def get_health_recommendations(age, bmi, blood_pressure):
    """Generate personalized health recommendations"""
    recommendations = []
    
    # BMI recommendations
    if bmi < 18.5:
        recommendations.append("[UNDERWEIGHT] BMI < 18.5 - Below healthy weight, consult nutritionist")
    elif bmi < 25:
        recommendations.append("[HEALTHY] HEALTHY BMI (18.5-24.9) - Maintain healthy diet and exercise")
    elif bmi < 30:
        recommendations.append("[WARNING] OVERWEIGHT (25-29.9) - Increase physical activity and healthy eating")
    elif bmi < 35:
        recommendations.append("[ALERT] OBESE CLASS I (30-34.9) - Consult doctor for weight management")
    elif bmi < 40:
        recommendations.append("[ALERT] OBESE CLASS II (35-39.9) - Urgent doctor consultation needed")
    else:
        recommendations.append("[CRITICAL] OBESE CLASS III (40+) - Immediate medical intervention required!")
    
    # Blood pressure recommendations
    if blood_pressure < 120:
        recommendations.append("[HEALTHY] NORMAL BP (< 120) - Excellent blood pressure")
    elif blood_pressure < 130:
        recommendations.append("[WARNING] ELEVATED BP (120-129) - Reduce salt intake, increase exercise")
    elif blood_pressure < 140:
        recommendations.append("[WARNING] STAGE 1 HYPERTENSION (130-139) - Consult doctor, lifestyle changes")
    elif blood_pressure < 180:
        recommendations.append("[ALERT] STAGE 2 HYPERTENSION (140-179) - Medication likely needed")
    else:
        recommendations.append("[CRITICAL] HYPERTENSIVE CRISIS (180+) - SEEK IMMEDIATE MEDICAL ATTENTION!")
    
    # Age-based recommendations
    if age < 18:
        recommendations.append("[INFO] YOUNG (< 18) - Focus on healthy habits, regular check-ups")
    elif age < 30:
        recommendations.append("[HEALTHY] YOUNG ADULT (18-29) - Establish healthy lifestyle")
    elif age < 40:
        recommendations.append("[INFO] ADULT (30-39) - Annual health screening important")
    elif age < 50:
        recommendations.append("[WARNING] MIDDLE-AGED (40-49) - Annual screening essential")
    elif age < 60:
        recommendations.append("[WARNING] MIDDLE-AGED (50-59) - Checkups every 6 months recommended")
    elif age < 70:
        recommendations.append("[WARNING] SENIOR (60-69) - Checkups every 3-6 months essential")
    else:
        recommendations.append("[WARNING] ELDERLY (70+) - Regular medical supervision crucial")
    
    return recommendations

def calculate_actual_risk(recommendations):
    """Calculate risk level based on health recommendations"""
    recommendations_str = ' '.join(recommendations)
    
    if '[CRITICAL]' in recommendations_str:
        return 'HIGH'
    elif '[ALERT]' in recommendations_str:
        return 'HIGH'
    elif '[WARNING]' in recommendations_str:
        return 'MEDIUM'
    else:
        return 'LOW'

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Health Risk Prediction API",
        "version": "1.0",
        "endpoint": "/predict",
        "method": "POST"
    })

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        # Extract patient data
        patient_id = data.get('patient_id', 1)
        age = float(data.get('age'))
        bmi = float(data.get('bmi'))
        blood_pressure = float(data.get('blood_pressure'))
        cholesterol = float(data.get('cholesterol', 200))
        smoking = int(data.get('smoking', 0))
        diabetes = int(data.get('diabetes', 0))
        heart_disease = int(data.get('heart_disease', 0))
        # Create feature array
        features = np.array([[patient_id, age, bmi, blood_pressure, cholesterol, smoking, diabetes, heart_disease]])
        # Make prediction
        prediction = rf_model.predict(features)[0]
        probability = rf_model.predict_proba(features)[0]
        risk_label = label_encoder.inverse_transform([prediction])[0]
        recommendations = get_health_recommendations(age, bmi, blood_pressure)
        actual_risk = calculate_actual_risk(recommendations)
        # SHAP values for explainability
        shap_values = explainer.shap_values(features)
        # Handle SHAP output shape for multiclass
        if isinstance(shap_values, list):
            shap_class_idx = prediction if prediction < len(shap_values) else 0
            shap_class_values = shap_values[shap_class_idx][0]
        else:
            shap_class_values = shap_values[0]
        # Robust scalar conversion
        shap_summary = {}
        for i in range(len(features[0])):
            val = shap_class_values[i]
            try:
                # If val is array of size 1, convert to scalar
                if hasattr(val, 'size') and val.size == 1:
                    shap_summary[str(i)] = float(val.reshape(-1)[0])
                elif hasattr(val, 'item'):
                    shap_summary[str(i)] = float(val.item())
                else:
                    shap_summary[str(i)] = float(val)
            except Exception:
                shap_summary[str(i)] = float(np.mean(val))
        # Build response
        response = {
            "status": "success",
            "timestamp": datetime.now().isoformat(),
            "patient_info": {
                "patient_id": patient_id,
                "age": age,
                "bmi": bmi,
                "blood_pressure": blood_pressure,
                "cholesterol": cholesterol,
                "smoking": smoking,
                "diabetes": diabetes,
                "heart_disease": heart_disease
            },
            "prediction": {
                "risk_level": actual_risk,
                "model_confidence": float(max(probability) * 100),
                "probabilities": {
                    label_encoder.inverse_transform([i])[0]: float(prob * 100)
                    for i, prob in enumerate(probability)
                }
            },
            "recommendations": recommendations,
            "explainability": {
                "shap_values": shap_summary,
                "feature_names": ["patient_id", "age", "bmi", "blood_pressure", "cholesterol", "smoking", "diabetes", "heart_disease"]
            }
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

# Add patient to Supabase
@app.route('/add_patient', methods=['POST'])
def add_patient():
    try:
        data = request.get_json()
        response = supabase.table("patients").insert(data).execute()
        return jsonify({"status": "success", "result": response.data}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

# Get all patients from Supabase
@app.route('/get_patients', methods=['GET'])
def get_patients():
    try:
        response = supabase.table("patients").select("*").execute()
        return jsonify({"status": "success", "patients": response.data}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "model_loaded": True
    }), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
