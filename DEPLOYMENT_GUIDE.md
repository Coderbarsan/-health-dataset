# 🏥 Health Risk Prediction System - Complete Setup & Deployment Guide

## 📋 Project Structure

```
Health_Care_Predict_Group/
├── backend/
│   ├── app.py                              # Flask API application
│   ├── train_model.py                      # Model training script
│   ├── healthcare_risk_classification_dataset.csv  # Training dataset
│   ├── requirements.txt                    # Python dependencies
│   ├── .env.example                        # Environment variables template
│   ├── rf_model.pkl                        # Trained ML model (generated)
│   └── label_encoder.pkl                   # Label encoder (generated)
├── frontend/
│   ├── index.html                          # Main HTML file
│   ├── styles.css                          # CSS styling
│   └── script.js                           # Frontend JavaScript
├── .gitignore                              # Git ignore file
└── README.md                               # This file
```

---

## 🚀 STEP-BY-STEP DEPLOYMENT GUIDE

### **PART 1: LOCAL DEVELOPMENT SETUP**

#### **Step 1: Install Python & Dependencies**

1. Ensure Python 3.8+ is installed:
   ```bash
   python --version
   ```

2. Navigate to the backend directory:
   ```bash
   cd backend
   ```

3. Create a virtual environment:
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   
   # On macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

4. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

#### **Step 2: Train the ML Model**

1. Still in the backend directory, run the training script:
   ```bash
   python train_model.py
   ```

   Expected output:
   ```
   First 5 rows:
   ...
   Random Forest Accuracy: XX.XX%
   Classification Report...
   Model saved to backend/rf_model.pkl
   Label encoder saved to backend/label_encoder.pkl
   ```

2. This creates two files:
   - `rf_model.pkl` - Trained Random Forest model
   - `label_encoder.pkl` - Label encoder for predictions

#### **Step 3: Start the Backend API**

1. In the backend directory, run:
   ```bash
   python app.py
   ```

   Expected output:
   ```
   WARNING in app.run_simple
    Running on http://0.0.0.0:5000
   ```

2. Test the API by visiting: `http://localhost:5000`

   You should see:
   ```json
   {
     "message": "Health Risk Prediction API",
     "version": "1.0",
     "endpoint": "/predict",
     "method": "POST"
   }
   ```

#### **Step 4: Run the Frontend Locally**

1. Open a new terminal (keep backend running)

2. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

3. Start a simple HTTP server:

   **On Windows (Python 3):**
   ```bash
   python -m http.server 8000
   ```

   **On macOS/Linux:**
   ```bash
   python -m http.server 8000
   ```

4. Open your browser and visit: `http://localhost:8000`

5. You should see the Health Risk Prediction interface

#### **Step 5: Test the Application**

1. Fill in the form with sample data:
   - Age: 45
   - BMI: 28.5
   - Blood Pressure: 130
   - Cholesterol: 210
   - Smoking: Yes
   - Diabetes: No
   - Heart Disease: No

2. Click "Analyze Risk"

3. You should see the prediction results with recommendations

---

### **PART 2: PREPARE FOR PRODUCTION DEPLOYMENT**

#### **Step 6: Update Environment Configuration**

1. In the backend directory, copy the example env file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` for production settings (optional):
   ```
   FLASK_ENV=production
   DEBUG=False
   ```

#### **Step 7: Create Production Requirements File**

The `requirements.txt` already includes gunicorn for production. Verify it contains:
- gunicorn==21.2.0

#### **Step 8: Prepare Frontend for Production**

1. The frontend is ready as-is (static HTML/CSS/JS)
2. For better optimization, you can minify CSS and JS (optional)

---

### **PART 3: DEPLOYMENT OPTIONS**

## **Option A: Deploy on Heroku (Recommended for Beginners)**

### Backend Deployment:

1. **Install Heroku CLI**
   - Download from: https://devcenter.heroku.com/articles/heroku-cli

2. **Create a Procfile** (in backend directory):
   ```
   web: gunicorn app:app
   ```

3. **Initialize Git and Heroku**
   ```bash
   cd backend
   git init
   git add .
   git commit -m "Initial commit"
   heroku login
   heroku create your-app-name
   ```

4. **Deploy**
   ```bash
   git push heroku main
   ```

5. **Your backend URL**: `https://your-app-name.herokuapp.com`

### Frontend Deployment:

1. **Update API URL in script.js**
   ```javascript
   const API_BASE_URL = 'https://your-app-name.herokuapp.com';
   ```

2. **Deploy to GitHub Pages or Netlify**

   **GitHub Pages:**
   - Push frontend folder to GitHub
   - Enable Pages in Settings
   - Visit: `https://yourusername.github.io/repo-name/frontend/`

   **Netlify:**
   - Visit netlify.com
   - Connect your GitHub repo
   - Deploy (automatic)

---

## **Option B: Deploy on AWS (Scalable)**

### Backend on EC2:

1. **Launch an EC2 instance** (Ubuntu 20.04)

2. **SSH into the instance**
   ```bash
   ssh -i your-key.pem ubuntu@your-instance-ip
   ```

3. **Install dependencies**
   ```bash
   sudo apt update
   sudo apt install python3-pip python3-venv nginx
   ```

4. **Clone or upload your code**
   ```bash
   git clone your-repo-url
   cd Health_Care_Predict_Group/backend
   ```

5. **Setup Python environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python train_model.py
   ```

6. **Configure Gunicorn**
   Create `/etc/systemd/system/healthapp.service`:
   ```ini
   [Unit]
   Description=Health Risk Prediction API
   After=network.target

   [Service]
   User=ubuntu
   WorkingDirectory=/home/ubuntu/Health_Care_Predict_Group/backend
   ExecStart=/home/ubuntu/Health_Care_Predict_Group/backend/venv/bin/gunicorn -w 4 -b 0.0.0.0:5000 app:app
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

7. **Start the service**
   ```bash
   sudo systemctl start healthapp
   sudo systemctl enable healthapp
   ```

8. **Configure Nginx as reverse proxy**
   Edit `/etc/nginx/sites-available/default`:
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;

       location / {
           proxy_pass http://localhost:5000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

9. **Restart Nginx**
   ```bash
   sudo systemctl restart nginx
   ```

### Frontend on S3 + CloudFront:

1. Update API URL in script.js to point to your backend
2. Upload frontend folder to S3
3. Create CloudFront distribution
4. Access via CloudFront URL

---

## **Option C: Deploy on Docker (Professional)**

1. **Create Dockerfile** (in backend):
   ```dockerfile
   FROM python:3.9-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   RUN python train_model.py
   EXPOSE 5000
   CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
   ```

2. **Create docker-compose.yml** (in root):
   ```yaml
   version: '3'
   services:
     backend:
       build: ./backend
       ports:
         - "5000:5000"
     frontend:
       image: nginx:latest
       ports:
         - "80:80"
       volumes:
         - ./frontend:/usr/share/nginx/html
   ```

3. **Run with Docker**
   ```bash
   docker-compose up
   ```

---

## **Option D: Deploy on Render (Easiest)**

### Backend:

1. Push code to GitHub
2. Visit render.com
3. Create New > Web Service
4. Connect GitHub repo (backend folder)
5. Set Start Command: `gunicorn app:app`
6. Deploy (automatic)

### Frontend:

1. Create New > Static Site
2. Connect GitHub repo (frontend folder)
3. Build Command: (leave empty)
4. Publish Directory: `.`
5. Deploy

---

### **PART 4: POST-DEPLOYMENT TESTING**

1. **Test Backend API**
   ```bash
   curl -X POST https://your-backend-url/predict \
     -H "Content-Type: application/json" \
     -d '{
       "age": 45,
       "bmi": 28.5,
       "blood_pressure": 130,
       "cholesterol": 210,
       "smoking": 1,
       "diabetes": 0,
       "heart_disease": 0
     }'
   ```

2. **Test Frontend**
   - Visit your frontend URL
   - Fill form and submit
   - Verify results display correctly

3. **Check CORS**
   - Frontend should connect to backend without issues

---

### **PART 5: MONITORING & MAINTENANCE**

#### **Log Monitoring**
- Check backend logs regularly
- Monitor API response times
- Set up error alerts

#### **Model Updates**
- Retrain model with new data periodically:
  ```bash
  python train_model.py
  ```
- Restart backend after retraining

#### **Performance Optimization**
- Cache common predictions
- Use CDN for static files
- Monitor database queries (if added)

---

## **🔧 Troubleshooting**

### Issue: "API is offline" error
- Verify backend is running
- Check CORS settings in app.py
- Ensure port 5000 is open

### Issue: Model not found
- Run `python train_model.py` first
- Verify .pkl files exist in backend directory

### Issue: Frontend not connecting to API
- Update API_BASE_URL in script.js
- Check browser console for errors (F12)
- Verify CORS headers in backend

### Issue: High memory usage
- Reduce model complexity (DecisionTree instead of RandomForest)
- Implement model caching
- Use model quantization

---

## **📊 API Documentation**

### **Base URL**
```
http://localhost:5000
```

### **Endpoints**

#### **1. Health Check**
```
GET /health
```
Response:
```json
{
  "status": "healthy",
  "model_loaded": true
}
```

#### **2. Predict Risk**
```
POST /predict
Content-Type: application/json

{
  "patient_id": 1,
  "age": 45,
  "bmi": 28.5,
  "blood_pressure": 130,
  "cholesterol": 210,
  "smoking": 1,
  "diabetes": 0,
  "heart_disease": 0
}
```

Response:
```json
{
  "status": "success",
  "timestamp": "2026-02-26T12:00:00.000000",
  "patient_info": {...},
  "prediction": {
    "risk_level": "HIGH",
    "model_confidence": 87.5,
    "probabilities": {
      "Low": 5.2,
      "Medium": 7.3,
      "High": 87.5
    }
  },
  "recommendations": [...]
}
```

---

## **🎯 Next Steps**

1. ✅ Complete local setup
2. ✅ Train and test the model
3. ✅ Choose a deployment platform
4. ✅ Deploy backend and frontend
5. ✅ Add custom domain (optional)
6. ✅ Setup SSL/HTTPS
7. ✅ Monitor performance
8. ✅ Plan model updates

---

## **📞 Support**

For issues or questions:
1. Check the Troubleshooting section
2. Review API logs
3. Test with Postman/cURL
4. Check browser console (F12)

---

## **📝 License**

This project is open source and available for educational purposes.

---

**Happy Deploying! 🚀**
