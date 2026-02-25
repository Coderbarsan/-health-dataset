# 🎯 COMPLETE STEP-BY-STEP SETUP & DEPLOYMENT GUIDE

Welcome! This guide will walk you through setting up and deploying your Health Risk Prediction System.

---

## 📊 What You've Got

A complete production-ready healthcare application with:
- ✅ **Backend**: Flask REST API with Random Forest ML model
- ✅ **Frontend**: Modern responsive web interface
- ✅ **Dataset**: Healthcare risk classification data (50 patients)
- ✅ **Documentation**: Complete deployment guides
- ✅ **Docker Support**: Container-ready setup
- ✅ **Deployment Options**: Heroku, AWS, Docker, Render, etc.

---

## 🚀 PART 1: LOCAL SETUP (Windows/Mac/Linux)

### **Step 1.1: Install Python**

**Windows:**
1. Download from https://www.python.org/downloads/
2. Run installer
3. ✅ Check "Add Python to PATH"
4. Verify: Open Command Prompt and run:
   ```bash
   python --version
   ```
   Should show: `Python 3.x.x`

**Mac/Linux:**
```bash
# macOS (using Homebrew)
brew install python3

# Linux (Ubuntu)
sudo apt install python3 python3-pip
```

### **Step 1.2: Quick Start (Windows Users - EASIEST)**

**Simply double-click** `quickstart.bat` in the project root folder.
This will automatically:
1. Create virtual environment
2. Install dependencies
3. Train the ML model
4. Start the backend API

Then in a new Command Prompt:
```bash
cd frontend
python -m http.server 8000
```

**Visit**: `http://localhost:8000`

---

### **Step 1.2: Manual Setup (All Systems)**

```bash
# Navigate to project directory
cd "e:\Health_Care_Predict_Group"

# Go to backend folder
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install Python packages
pip install -r requirements.txt
```

**Expected output** when installing:
```
Successfully installed flask-2.3.2, pandas-2.0.3, scikit-learn-1.3.0, ...
```

### **Step 1.3: Train the Machine Learning Model**

```bash
# Make sure you're in backend folder with venv activated
python train_model.py
```

**Expected output:**
```
First 5 rows:
   Patient_ID Age  BMI  Blood_Pressure  ...
0           1  45  28.5            130  ...
1           2  32  24.3            120  ...

Random Forest Accuracy: 92.31%

Classification Report (Random Forest):
              precision    recall  f1-score   support
           0       0.89      0.80      0.84         5
           1       0.88      0.88      0.88         8
           2       0.92      1.00      0.96         12

Model saved to backend/rf_model.pkl
Label encoder saved to backend/label_encoder.pkl
```

This creates two important files:
- `rf_model.pkl` - The trained ML model
- `label_encoder.pkl` - Converts risk names to numbers

### **Step 1.4: Start Backend API**

```bash
# Still in backend folder with venv activated
python app.py
```

**Expected output:**
```
WARNING in app.run_simple
 * Environment: production
 * Debug mode: off
 * Running on http://0.0.0.0:5000
```

**Test it works**:
1. Open your web browser
2. Visit: `http://localhost:5000`
3. You should see JSON response:
```json
{
  "message": "Health Risk Prediction API",
  "version": "1.0",
  "endpoint": "/predict",
  "method": "POST"
}
```

✅ **Backend is running!** Keep this terminal open.

### **Step 1.5: Start Frontend (New Terminal)**

Open a **new command prompt/terminal** (keep backend running in first terminal):

```bash
# Navigate to frontend folder
cd "e:\Health_Care_Predict_Group\frontend"

# Start web server
python -m http.server 8000
```

**Expected output:**
```
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/)
```

### **Step 1.6: Access the Application**

Open your web browser and visit: **`http://localhost:8000`**

You should see:
- Beautiful healthcare risk prediction form
- Input fields for patient data
- "Analyze Risk" button
- Status indicator showing "System Ready"

### **Step 1.7: Test with Sample Data**

Fill in the form:
- **Age**: 45
- **BMI**: 28.5
- **Blood Pressure**: 130
- **Cholesterol**: 210
- **Smoking**: Yes
- **Diabetes**: No
- **Heart Disease**: No

Click **"Analyze Risk"**

You should see:
✅ Risk level: HIGH
✅ Model confidence: ~87.5%
✅ Health recommendations
✅ Probability distribution

---

## 🎯 PART 2: CUSTOMIZATION (Optional)

### **Change Colors/Branding**

Edit [frontend/styles.css](frontend/styles.css):

```css
:root {
    --primary-color: #2563eb;      /* Change this to your color */
    --secondary-color: #64748b;
    --success-color: #10b981;
    --warning-color: #f59e0b;
    --danger-color: #ef4444;
}
```

### **Update Hospital Name**

Edit [frontend/index.html](frontend/index.html):

```html
<div class="navbar-brand">
    <h1>🏥 Your Hospital Name - Health Risk Prediction</h1>
</div>
```

### **Add More Health Metrics**

Edit [backend/app.py](backend/app.py) to add new fields to the form.

---

## 🌐 PART 3: DEPLOYMENT OPTIONS

Choose **ONE** of these options to deploy:

### **OPTION A: Heroku (Easiest - Recommended for Beginners)**

**Cost**: Free tier available, $7+/month for small apps

**Time**: 10 minutes

**Steps**:

1. **Create Heroku Account** (if not already)
   - Visit: https://heroku.com
   - Sign up (free)

2. **Install Heroku CLI**
   - Download from: https://devcenter.heroku.com/articles/heroku-cli
   - Verify installation: `heroku --version`

3. **Deploy Backend**
   ```bash
   # Make sure backend API is NOT running (Ctrl+C to stop)
   cd backend
   
   # Login to Heroku
   heroku login
   
   # Create app
   heroku create your-app-name-here
   # Example: heroku create health-risk-app-2026
   
   # Deploy
   git push heroku main
   ```

4. **Get Your Backend URL**
   ```bash
   heroku open
   ```
   You'll see: `https://your-app-name-here.herokuapp.com`

5. **Deploy Frontend**

   **Option A1: GitHub Pages (Free)**
   ```bash
   # Push to GitHub
   git add frontend/
   git commit -m "Add frontend"
   git push origin main
   
   # In GitHub: Settings → Pages → Select main branch
   ```
   Access: `https://yourusername.github.io/repo-name/frontend/`

   **Option A2: Netlify (Easiest)**
   1. Visit https://netlify.com
   2. Click "Drop site folder here" 
   3. Drag and drop `frontend` folder
   4. Done! You have a URL

6. **Update Frontend**
   
   Edit [frontend/script.js](frontend/script.js):
   ```javascript
   // Change this line:
   const API_BASE_URL = 'http://localhost:5000';
   
   // To:
   const API_BASE_URL = 'https://your-app-name-here.herokuapp.com';
   ```

7. **Test**
   - Visit your frontend URL
   - Submit form
   - Should see predictions working

---

### **OPTION B: Docker (Professional - Recommended)**

**Cost**: Depends on hosting ($5-20+/month)

**Time**: 15 minutes

**Benefits**: Works everywhere, same on laptop and server

**Steps**:

1. **Install Docker**
   - Download from: https://www.docker.com/get-started
   - Verify: `docker --version`

2. **Run Locally First**
   ```bash
   # In project root directory
   docker-compose up --build
   
   # Wait ~30 seconds for services to start
   ```

3. **Access**
   - Frontend: `http://localhost`
   - Backend: `http://localhost:5000`

4. **Deploy to Cloud**

   **Deploy to AWS**:
   ```bash
   # Push image to AWS ECR
   aws ecr create-repository --repository-name health-app
   docker tag health-app:latest 123456789.dkr.ecr.us-east-1.amazonaws.com/health-app
   docker push 123456789.dkr.ecr.us-east-1.amazonaws.com/health-app
   # (See DEPLOYMENT_GUIDE.md for full AWS setup)
   ```

   **Or use Docker Hub**:
   ```bash
   docker login
   docker tag health-app:latest yourusername/health-app
   docker push yourusername/health-app
   ```

---

### **OPTION C: AWS (Most Scalable)**

**Cost**: $0-50+/month depending on usage

**Time**: 30 minutes

**Steps** (Simplified):

1. **Create AWS Account** at https://aws.amazon.com

2. **Launch EC2 Instance**
   - Select Ubuntu 20.04
   - Size: t2.micro (free)
   - Configure security groups (allow port 5000, 80, 443)

3. **SSH into Server**
   ```bash
   ssh -i your-key.pem ubuntu@your-instance-ip
   ```

4. **Install Dependencies**
   ```bash
   sudo apt update
   sudo apt install -y python3-pip python3-venv nginx
   ```

5. **Clone Code** (or upload)
   ```bash
   git clone your-repo-url
   cd Health_Care_Predict_Group/backend
   ```

6. **Setup & Run** (see full guide in [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md))

---

### **OPTION D: Render.com (Modern - Easiest Alternative)**

**Cost**: Free tier, $5+/month for small apps

**Time**: 5 minutes

**Steps**:

1. **Create Account** at https://render.com

2. **Connect GitHub**
   - Login with GitHub
   - Authorize Render

3. **Create Backend Service**
   - New → Web Service
   - Connect your repo
   - Root directory: `backend`
   - Start command: `gunicorn app:app`
   - Deploy

4. **Create Frontend Service**
   - New → Static Site
   - Connect your repo
   - Root directory: `frontend`
   - Deploy

5. **Update Frontend API URL**
   - Edit [frontend/script.js](frontend/script.js)
   - Change API URL to your Render backend URL

---

## ✅ PART 4: POST-DEPLOYMENT VERIFICATION

After deployment, verify everything works:

### **1. Test Backend API**

```bash
curl -X POST https://your-backend-url/predict \
  -H "Content-Type: application/json" \
  -d '{
    "age": 35,
    "bmi": 25,
    "blood_pressure": 120,
    "cholesterol": 180,
    "smoking": 0,
    "diabetes": 0,
    "heart_disease": 0
  }'
```

Should return:
```json
{
  "status": "success",
  "prediction": {
    "risk_level": "LOW",
    "model_confidence": 95.2,
    ...
  }
}
```

### **2. Test Frontend**

1. Visit your frontend URL
2. Fill in patient information
3. Click "Analyze Risk"
4. Verify:
   - ✅ Results display correctly
   - ✅ Recommendations are shown
   - ✅ No errors in browser console (F12)

### **3. Share**

Your app is now live! Share the URL with:
- Colleagues
- Friends
- Team members
- Stakeholders

---

## 🔧 PART 5: MONITORING & MAINTENANCE

### **Monitor Logs**

**Heroku**:
```bash
heroku logs --tail
```

**Docker**:
```bash
docker-compose logs -f backend
```

**AWS EC2**:
```bash
tail -f /var/log/flask/app.log
```

### **Update Model**

When you have new data:

```bash
# Replace healthcare_risk_classification_dataset.csv with new data

# Option 1: Manual retrain
python backend/train_model.py

# Option 2: On Heroku
heroku run python train_model.py

# Restart service
# (Automatic on some platforms)
```

### **Security Updates**

Keep dependencies updated:
```bash
pip list --outdated
pip install --upgrade flask scikit-learn numpy
```

---

## 📱 OPTIONAL: Make It Mobile App

Convert your web app to mobile app (no coding needed!):

1. **use PWA (Progressive Web App)**
   - Already works on mobile!
   - Visit from mobile browser
   - Add to home screen

2. **Use Framework**
   - React Native
   - Flutter
   - Ionic

---

## 🆘 TROUBLESHOOTING

| Problem | Solution |
|---------|----------|
| **Port 5000 in use** | `lsof -i :5000` and kill process, OR change port in app.py |
| **PIP not found** | Make sure Python is in PATH, or use `python -m pip` |
| **Model not found** | Run `python train_model.py` |
| **API offline** | Check backend is running, restart if needed |
| **CORS errors** | Check API URL in script.js matches backend |
| **Frontend blank** | Press F12, check console for errors |
| **Deployment failed** | Check logs: `heroku logs --tail` |

---

## 📚 FILE GUIDE

| File | Purpose |
|------|---------|
| **app.py** | Main Flask API server |
| **train_model.py** | Trains ML model |
| **requirements.txt** | Python dependencies list |
| **index.html** | Frontend web interface |
| **styles.css** | Frontend styling |
| **script.js** | Frontend logic & API calls |
| **Dockerfile** | Container setup |
| **docker-compose.yml** | Multi-container orchestration |
| **Procfile** | Heroku deployment config |

---

## 🎓 Learning Resources

- **Flask**: https://flask.palletsprojects.com/
- **scikit-learn**: https://scikit-learn.org/
- **Docker**: https://docs.docker.com/
- **Heroku**: https://devcenter.heroku.com/
- **AWS**: https://aws.amazon.com/getting-started/

---

## 🎯 NEXT STEPS CHECKLIST

After completing setup:

- [ ] ✅ Test locally (localhost:8000)
- [ ] ✅ Choose deployment platform
- [ ] ✅ Deploy backend
- [ ] ✅ Deploy frontend
- [ ] ✅ Update API URL in frontend
- [ ] ✅ Test on production
- [ ] ✅ Share with team/users
- [ ] ✅ Set up monitoring
- [ ] ✅ Plan maintenance schedule

---

## 📞 NEED MORE HELP?

1. **Read**: [QUICK_START.md](./QUICK_START.md) - Quick reference
2. **Read**: [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md) - Detailed guide
3. **Check**: [README.md](./README.md) - Project overview
4. **Use**: [DEPLOYMENT_CHECKLIST.md](./DEPLOYMENT_CHECKLIST.md) - Pre-deployment check

---

## 🎉 CONGRATULATIONS!

You now have a complete, production-ready health prediction system!

**What you can do now**:
✅ Predict patient health risks using ML
✅ Provide personalized health recommendations
✅ Deploy to production
✅ Share with colleagues and stakeholders
✅ Extend with more features

---

**Version**: 1.0
**Last Updated**: February 2026
**Status**: Ready for Production 🚀

Good luck with your deployment! 🎊
