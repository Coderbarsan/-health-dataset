from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import joblib
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# SHAP for explainability
import shap

# Supabase integration
from supabase import create_client, Client

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
app = Flask(__name__)
CORS(app, origins="*", allow_headers=["Content-Type"], methods=["GET", "POST", "OPTIONS"])

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

def get_diet_chart(age, bmi, blood_pressure, cholesterol, smoking, diabetes, heart_disease):
    """Generate personalized diet chart based on patient health data"""
    diet = {
        "recommended_foods": [],
        "foods_to_avoid": [],
        "meal_plan": {
            "breakfast": [],
            "mid_morning_snack": [],
            "lunch": [],
            "evening_snack": [],
            "dinner": []
        },
        "daily_water_intake": "8 glasses (2 liters)",
        "special_notes": []
    }

    # ── BMI-based diet ──
    if bmi < 18.5:  # Underweight
        diet["recommended_foods"].extend(["🥜 Nuts & dry fruits", "🥛 Full-fat milk & dairy", "🍌 Bananas & mangoes", "🍚 Brown rice & whole grains", "🥑 Avocados", "🍳 Eggs & lean meat", "🫘 Lentils & beans"])
        diet["foods_to_avoid"].extend(["🚫 Junk food (empty calories)", "🚫 Excessive caffeine"])
        diet["meal_plan"]["breakfast"].extend(["Oatmeal with banana, nuts & honey", "Boiled eggs (2)", "Full-fat milk or smoothie"])
        diet["meal_plan"]["mid_morning_snack"].extend(["Handful of almonds & walnuts", "Fresh fruit juice"])
        diet["meal_plan"]["lunch"].extend(["Brown rice with dal & vegetables", "Grilled chicken/paneer", "Curd/yogurt"])
        diet["meal_plan"]["evening_snack"].extend(["Peanut butter toast", "Mixed fruit bowl"])
        diet["meal_plan"]["dinner"].extend(["Chapati with mixed vegetables", "Lentil soup", "Warm milk before bed"])
        diet["special_notes"].append("📈 Focus on calorie-dense nutritious foods to gain healthy weight")

    elif bmi < 25:  # Normal
        diet["recommended_foods"].extend(["🥗 Fresh salads & vegetables", "🍎 Seasonal fruits", "🐟 Fish & lean protein", "🌾 Whole grains", "🥛 Low-fat dairy", "🫘 Legumes & pulses"])
        diet["foods_to_avoid"].extend(["🚫 Excessive sugar", "🚫 Processed foods", "🚫 Deep fried items"])
        diet["meal_plan"]["breakfast"].extend(["Whole grain toast with egg whites", "Fresh fruit", "Green tea"])
        diet["meal_plan"]["mid_morning_snack"].extend(["Fresh fruits or yogurt"])
        diet["meal_plan"]["lunch"].extend(["Balanced plate: grains + protein + vegetables", "Buttermilk"])
        diet["meal_plan"]["evening_snack"].extend(["Sprout salad or nuts"])
        diet["meal_plan"]["dinner"].extend(["Light chapati with vegetables", "Dal or lean protein", "Salad"])
        diet["special_notes"].append("✅ Great BMI! Maintain your current balanced diet")

    elif bmi < 30:  # Overweight
        diet["recommended_foods"].extend(["🥬 Leafy greens (spinach, kale)", "🥒 Cucumber & celery", "🍋 Citrus fruits", "🐔 Grilled chicken/fish", "🫖 Green tea", "🥣 Oats & quinoa"])
        diet["foods_to_avoid"].extend(["🚫 White bread & refined carbs", "🚫 Sugary drinks & soda", "🚫 Fried foods", "🚫 Butter & cheese", "🚫 Sweets & desserts"])
        diet["meal_plan"]["breakfast"].extend(["Vegetable oats or poha", "Green tea", "1 fruit"])
        diet["meal_plan"]["mid_morning_snack"].extend(["Cucumber slices or buttermilk"])
        diet["meal_plan"]["lunch"].extend(["Small portion rice with dal & veggie curry", "Large salad"])
        diet["meal_plan"]["evening_snack"].extend(["Roasted chana or green tea"])
        diet["meal_plan"]["dinner"].extend(["Soup + grilled protein", "Steamed vegetables", "No carbs after 7 PM"])
        diet["daily_water_intake"] = "10-12 glasses (3 liters)"
        diet["special_notes"].append("⚠️ Reduce portion sizes gradually and increase fiber intake")

    else:  # Obese
        diet["recommended_foods"].extend(["🥦 Broccoli & cauliflower", "🫑 Bell peppers", "🍅 Tomatoes", "🐟 Fish (omega-3)", "🫖 Green/herbal tea", "🥗 Raw salads before meals"])
        diet["foods_to_avoid"].extend(["🚫 All fried foods", "🚫 Sugar in any form", "🚫 White rice & bread", "🚫 Packaged/processed food", "🚫 Alcohol", "🚫 Full-fat dairy"])
        diet["meal_plan"]["breakfast"].extend(["Vegetable smoothie", "1 boiled egg", "Green tea"])
        diet["meal_plan"]["mid_morning_snack"].extend(["Lemon water or plain buttermilk"])
        diet["meal_plan"]["lunch"].extend(["Large salad first", "Small portion dal + 1 chapati", "Steamed vegetables"])
        diet["meal_plan"]["evening_snack"].extend(["Herbal tea or warm lemon water"])
        diet["meal_plan"]["dinner"].extend(["Clear vegetable soup", "Grilled fish/chicken (small)", "Finish by 7 PM"])
        diet["daily_water_intake"] = "12-15 glasses (3.5 liters)"
        diet["special_notes"].append("🚨 Consult a nutritionist for a supervised weight loss plan")

    # ── High Blood Pressure ──
    if blood_pressure >= 130:
        diet["recommended_foods"].extend(["🍌 Potassium-rich: bananas, sweet potatoes", "🫐 Berries (blueberries, strawberries)", "🧄 Garlic & ginger"])
        diet["foods_to_avoid"].extend(["🚫 Salt (limit to 1,500 mg/day)", "🚫 Pickles & papad", "🚫 Canned/processed foods", "🚫 Red meat"])
        diet["special_notes"].append("🩸 Follow DASH diet principles: low sodium, high potassium")

    # ── High Cholesterol ──
    if cholesterol >= 240:
        diet["recommended_foods"].extend(["🐟 Omega-3 rich fish (salmon, mackerel)", "🫒 Olive oil", "🥑 Avocados", "🌰 Walnuts & flaxseeds"])
        diet["foods_to_avoid"].extend(["🚫 Egg yolks (limit to 2/week)", "🚫 Butter & ghee", "🚫 Red meat & organ meats", "🚫 Coconut oil"])
        diet["special_notes"].append("❤️ Increase soluble fiber (oats, beans) to lower LDL cholesterol")
    elif cholesterol >= 200:
        diet["special_notes"].append("⚠️ Cholesterol is borderline high — reduce saturated fats")

    # ── Diabetes ──
    if diabetes == 1:
        diet["recommended_foods"].extend(["🥒 Low glycemic foods", "🌾 Whole grains only", "🫘 Fenugreek seeds (soaked overnight)", "🍵 Bitter gourd juice"])
        diet["foods_to_avoid"].extend(["🚫 White rice (switch to brown)", "🚫 Sugar, honey, jaggery", "🚫 Fruit juices (eat whole fruits)", "🚫 Potatoes & starchy foods"])
        diet["meal_plan"]["mid_morning_snack"] = ["Soaked almonds (5-6) + fenugreek water"]
        diet["daily_water_intake"] = "10-12 glasses (3 liters)"
        diet["special_notes"].append("🩺 Eat every 2-3 hours to maintain blood sugar levels")
        diet["special_notes"].append("📊 Monitor blood sugar before and after meals")

    # ── Heart Disease ──
    if heart_disease == 1:
        diet["recommended_foods"].extend(["🫒 Extra virgin olive oil", "🐟 Fatty fish (2-3 times/week)", "🍇 Dark grapes & pomegranate", "🧅 Onion & garlic daily"])
        diet["foods_to_avoid"].extend(["🚫 Trans fats & hydrogenated oils", "🚫 Excess salt", "🚫 Energy drinks", "🚫 Smoking & alcohol"])
        diet["special_notes"].append("❤️ Follow Mediterranean diet pattern for heart health")
        diet["special_notes"].append("🏃 Combine diet with 30 min daily walking")

    # ── Smoking ──
    if smoking == 1:
        diet["recommended_foods"].extend(["🍊 Vitamin C rich foods (oranges, guava)", "🥕 Beta-carotene foods (carrots)", "🫖 Herbal teas"])
        diet["special_notes"].append("🚭 Quitting smoking is the #1 thing you can do for your health")

    # ── Age-based additions ──
    if age >= 50:
        diet["recommended_foods"].extend(["🦴 Calcium-rich foods (milk, ragi)", "☀️ Vitamin D (sunlight exposure)"])
        diet["special_notes"].append("🦴 Increase calcium & Vitamin D for bone health")
    if age >= 60:
        diet["special_notes"].append("👴 Eat soft, easily digestible foods. Smaller, frequent meals.")

    # Remove duplicates while preserving order
    diet["recommended_foods"] = list(dict.fromkeys(diet["recommended_foods"]))
    diet["foods_to_avoid"] = list(dict.fromkeys(diet["foods_to_avoid"]))
    diet["special_notes"] = list(dict.fromkeys(diet["special_notes"]))

    return diet

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
        # Generate personalized diet chart
        diet_chart = get_diet_chart(age, bmi, blood_pressure, cholesterol, smoking, diabetes, heart_disease)
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
            "diet_chart": diet_chart,
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
        # Only include fields that exist in the Supabase 'patients' table
        valid_fields = ['patient_id', 'patient_name', 'age', 'bmi', 'blood_pressure', 'cholesterol', 'smoking', 'diabetes', 'heart_disease']
        patient_record = {k: v for k, v in data.items() if k in valid_fields}
        response = supabase.table("patients").insert(patient_record).execute()
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
