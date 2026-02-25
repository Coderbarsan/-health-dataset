# 🚀 QUICK START GUIDE - Health Risk Prediction System

## 📋 Table of Contents
1. [Windows Quick Start](#windows-quick-start)
2. [macOS/Linux Quick Start](#macoslinus-quick-start)
3. [Docker Quick Start](#docker-quick-start)
4. [Development vs Production](#development-vs-production)

---

## 🪟 Windows Quick Start

### **Option 1: Automated (Recommended)**

1. **Open Command Prompt** in the project root
2. **Double-click** `quickstart.bat`
3. **Wait** for setup to complete (2-3 minutes)
4. **In a new Command Prompt**, run:
   ```bash
   cd frontend
   python -m http.server 8000
   ```
5. **Open browser** to `http://localhost:8000`

### **Option 2: Manual Setup**

```bash
# Step 1: Navigate to backend
cd backend

# Step 2: Create virtual environment
python -m venv venv
venv\Scripts\activate

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Train the model
python train_model.py

# Step 5: Start backend API
python app.py
```

**Backend URL**: `http://localhost:5000`

In a **new terminal**:
```bash
cd frontend
python -m http.server 8000
```

**Frontend URL**: `http://localhost:8000`

---

## 🍎 macOS/Linux Quick Start

```bash
# Step 1: Navigate to backend
cd backend

# Step 2: Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Train the model
python train_model.py

# Step 5: Start backend API
python app.py
```

**Backend URL**: `http://localhost:5000`

In a **new terminal**:
```bash
cd frontend
python3 -m http.server 8000
```

**Frontend URL**: `http://localhost:8000`

---

## 🐳 Docker Quick Start

### **Prerequisites**
- Docker installed ([Get Docker](https://www.docker.com/get-started))

### **Setup**

```bash
# Build and start all services
docker-compose up --build

# Wait for services to start (~30 seconds)
```

**Access Points**:
- Frontend: `http://localhost`
- Backend API: `http://localhost:5000`

### **Stop Services**
```bash
docker-compose down
```

### **View Logs**
```bash
docker-compose logs -f backend
docker-compose logs -f frontend
```

---

## 🔄 Development vs Production

### **Development Mode** ✨

**Use when**:
- Building and testing locally
- Making code changes
- Debugging issues

**Setup**:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python train_model.py
python app.py  # Development server
```

**Features**:
- Hot reload enabled
- Detailed error messages
- Debug mode active
- No performance optimization

### **Production Mode** 🚀

**Use when**:
- Deploying to server
- Real users accessing the app
- High-traffic scenarios

**Setup with Gunicorn**:
```bash
cd backend
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

**Better Performance**:
- Multiple worker processes
- Production-ready WSGI server
- Optimized caching
- Error logging

---

## 📊 Testing Your Setup

### **1. Test Backend API**

**Using curl** (Windows PowerShell or Linux/Mac):
```bash
curl -X POST http://localhost:5000/predict `
  -H "Content-Type: application/json" `
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

**Expected Response**:
```json
{
  "status": "success",
  "prediction": {
    "risk_level": "HIGH",
    "model_confidence": 87.5,
    ...
  }
}
```

**Using Postman**:
1. Download [Postman](https://www.postman.com/download/)
2. Create new POST request
3. URL: `http://localhost:5000/predict`
4. Body (JSON):
   ```json
   {
     "age": 35,
     "bmi": 25,
     "blood_pressure": 120,
     "cholesterol": 180,
     "smoking": 0,
     "diabetes": 0,
     "heart_disease": 0
   }
   ```
5. Send

### **2. Test Frontend**

1. Open `http://localhost:8000`
2. Should see beautiful form interface
3. Enter sample data
4. Click "Analyze Risk"
5. Should see prediction results

### **3. Check Logs**

**Backend Logs**:
```
 * Running on http://0.0.0.0:5000
```

**Browser Console Logs** (F12):
- Check for any errors
- Verify API request/response

---

## ⚡ Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: No module named 'flask'` | Run `pip install -r requirements.txt` |
| `Port 5000 already in use` | Change port in `app.py` or kill existing process |
| `API is offline` error in frontend | Ensure backend is running on `http://localhost:5000` |
| Blank/white frontend page | Check browser console (F12) for JavaScript errors |
| `Model not found` error | Run `python train_model.py` first |
| CORS errors | Ensure CORS is enabled in Flask app |

---

## 🎯 Next Steps

After successful local testing:

1. **Choose Deployment Platform**
   - Heroku (easiest)
   - AWS (most scalable)
   - Docker (most flexible)
   - Render.com (modern)

2. **Follow Deployment Guide**
   - See [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md)
   - Step-by-step instructions for each platform

3. **Customize**
   - Update colors/branding
   - Adjust model parameters
   - Add more health metrics

4. **Monitor**
   - Check logs
   - Monitor performance
   - Update model with new data

---

## 📚 File Descriptions

```
Health_Care_Predict_Group/
├── backend/
│   ├── app.py                    # Main Flask API
│   ├── train_model.py            # ML model training
│   ├── requirements.txt          # Python dependencies
│   ├── Dockerfile                # For Docker deployment
│   ├── Procfile                  # For Heroku deployment
│   └── .env.example              # Environment variables template
├── frontend/
│   ├── index.html               # Main UI file
│   ├── styles.css               # CSS styling
│   └── script.js                # Frontend logic
├── docker-compose.yml           # Complete Docker setup
├── nginx.conf                   # Nginx configuration
├── quickstart.bat               # Windows quick start
├── README.md                    # Project overview
├── QUICK_START.md              # This file
└── DEPLOYMENT_GUIDE.md         # Detailed deployment instructions
```

---

## 💡 Pro Tips

1. **Rename virtual environment folder** to hide it from git:
   ```bash
   echo venv/ > .gitignore
   ```

2. **Create `.env` file** for sensitive data:
   ```bash
   cp backend/.env.example backend/.env
   ```

3. **Use Postman collections** for API testing
   - Export curl commands as Postman collection
   - Share with team members

4. **Monitor with logs**:
   ```bash
   tail -f backend.log  # macOS/Linux
   Get-Content backend.log -Tail 10 -Wait  # Windows
   ```

5. **Auto-reload on code changes** (development):
   ```bash
   pip install python-dotenv
   # Then uncomment in app.py: app.run(debug=True)
   ```

---

## 🔒 Security Checklist

Before deployment:

- [ ] Set `DEBUG=False` in production
- [ ] Use HTTPS (SSL certificate)
- [ ] Implement rate limiting
- [ ] Add API key authentication
- [ ] Validate all inputs
- [ ] Use environment variables for secrets
- [ ] Enable CORS only for trusted domains
- [ ] Add logging and monitoring

---

## 📞 Need Help?

1. **Check Logs**: Review backend console output
2. **Browser DevTools**: Press F12 for frontend errors
3. **Test API**: Use curl or Postman
4. **Verify Files**: Ensure all files are in place
5. **Read DEPLOYMENT_GUIDE.md**: Comprehensive deployment help

---

**Ready to deploy? Follow [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md) next!** 🚀
