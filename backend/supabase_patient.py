from supabase import create_client, Client

SUPABASE_URL = "https://pnkziwbngtddjsuusocp.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBua3ppd2JuZ3RkZGpzdXVzb2NwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzIwNTM4ODEsImV4cCI6MjA4NzYyOTg4MX0.1SufwjGNU0CkcsrI8oJEZQU0FJBjO6DFfq8P5p0hT70"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def insert_patient(patient_data):
    response = supabase.table("patients").insert(patient_data).execute()
    return response.data

def get_patients():
    response = supabase.table("patients").select("*").execute()
    return response.data

# Example usage:
if __name__ == "__main__":
    patient_data = {
        "patient_id": 1,
        "age": 45,
        "bmi": 28.5,
        "blood_pressure": 130,
        "cholesterol": 210,
        "smoking": 0,
        "diabetes": 0,
        "heart_disease": 0
    }
    print("Insert result:", insert_patient(patient_data))
    print("All patients:", get_patients())
