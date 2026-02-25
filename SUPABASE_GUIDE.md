# FREE PATIENT DATA STORAGE: Supabase Guide

## Steps to Store Patient Data in Supabase (Free Tier)

1. **Create a Supabase Account**
   - Go to https://supabase.com
   - Sign up for a free account

2. **Create a New Project**
   - Click "New Project"
   - Choose a name, password, and region
   - Wait for the project to initialize

3. **Get Database Connection Details**
   - Go to "Project Settings" > "Database"
   - Copy the connection string (PostgreSQL URI)
   - Also note your API keys (for REST/GraphQL access)

4. **Create a Table for Patients**
   - Go to "Table Editor"
   - Click "New Table"
   - Name: `patients`
   - Add columns: patient_id (int), age (int), bmi (float), blood_pressure (float), cholesterol (float), smoking (int), diabetes (int), heart_disease (int)

5. **Install Supabase Python Client**
   - In your project folder, run:
     ```
     pip install supabase
     ```

6. **Sample Python Integration**
   - Add this to your backend/app.py or a new script:
     ```python
     from supabase import create_client, Client

     url = "https://<your-project-ref>.supabase.co"
     key = "<your-anon-key>"
     supabase: Client = create_client(url, key)

     # Insert a patient record
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
     supabase.table("patients").insert(patient_data).execute()

     # Query patient records
     result = supabase.table("patients").select("*").execute()
     print(result.data)
     ```

7. **Store and Retrieve Data**
   - Use `.insert()` and `.select()` to manage patient data.

---

For more details, see the official Supabase docs: https://supabase.com/docs
