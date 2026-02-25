# FREE PATIENT DATA STORAGE: MongoDB Atlas Guide

## Steps to Store Patient Data in MongoDB Atlas (Free Tier)

1. **Create a MongoDB Atlas Account**
   - Go to https://www.mongodb.com/cloud/atlas
   - Sign up for a free account

2. **Create a Free Cluster**
   - Click "Build a Database" > Choose "Free" tier (M0)
   - Select AWS, Azure, or GCP (any region)
   - Name your cluster (e.g., HealthCareCluster)

3. **Configure Database Access**
   - Add a database user (username & password)
   - Set IP Whitelist to `0.0.0.0/0` for open access (or restrict to your IP)

4. **Get Connection String**
   - Click "Connect" > "Connect your application"
   - Copy the connection string (e.g., `mongodb+srv://<username>:<password>@<cluster-url>/test`)

5. **Install Python MongoDB Driver**
   - In your project folder, run:
     ```
     pip install pymongo
     ```

6. **Sample Python Integration**
   - Add this to your backend/app.py or a new script:
     ```python
     from pymongo import MongoClient

     # Replace with your connection string
     client = MongoClient("mongodb+srv://<username>:<password>@<cluster-url>/test")
     db = client['healthcare']
     patients = db['patients']

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
     patients.insert_one(patient_data)

     # Query patient records
     for patient in patients.find():
         print(patient)
     ```

7. **Store and Retrieve Data**
   - Use `insert_one`, `find`, `update_one`, etc. to manage patient data.

---

For more details, see the official MongoDB Atlas docs: https://www.mongodb.com/docs/atlas/
