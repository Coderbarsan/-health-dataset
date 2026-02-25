import requests
import json

def test_predict():
    url = "http://127.0.0.1:5000/predict"
    payload = {
        "patient_id": 1,
        "age": 45,
        "bmi": 28.5,
        "blood_pressure": 130,
        "cholesterol": 210,
        "smoking": 0,
        "diabetes": 0,
        "heart_disease": 0
    }
    response = requests.post(url, json=payload)
    print("Status Code:", response.status_code)
    print("Response:", json.dumps(response.json(), indent=2))

if __name__ == "__main__":
    test_predict()
