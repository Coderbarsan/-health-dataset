# 📱 QUICK REFERENCE CARD

## 🔑 Essential Commands (Copy & Paste Ready)

### Activate Virtual Environment

**Windows PowerShell:**
```powershell
& "e:\Health_Care_Predict_Group\backend\venv\Scripts\Activate.ps1"
```

**Windows Command Prompt (CMD):**
```cmd
e:\Health_Care_Predict_Group\backend\venv\Scripts\activate.bat
```

**Mac/Linux:**
```bash
source e:\Health_Care_Predict_Group/backend/venv/bin/activate
```

---

### Start Backend API

```powershell
& "e:\Health_Care_Predict_Group\backend\venv\Scripts\python" "e:\Health_Care_Predict_Group\backend\app.py"
```

**Then visit**: `http://localhost:5000`

---

### Start Frontend

```powershell
cd e:\Health_Care_Predict_Group\frontend
python -m http.server 8000
```

**Then visit**: `http://localhost:8000`

---

## 📊 Free Dataset Storage Commands

### GitHub Setup

```bash
cd e:\Health_Care_Predict_Group
git init
git config user.name "Your Name"
git config user.email "your@email.com"
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/health-app.git
git branch -M main
git push -u origin main
```

### Kaggle Setup

```powershell
pip install kaggle
# Download kaggle.json from https://www.kaggle.com/settings/account
# Save to: C:\Users\[YourUsername]\.kaggle\kaggle.json
kaggle datasets create -p .\backend\
```

### Google Drive Setup

```powershell
pip install gdown
# Upload CSV to Google Drive
# Get shareable link and extract file ID
gdown "https://drive.google.com/uc?export=download&id=FILE_ID"
```

---

## 🔧 Package Management

### Install New Package

```powershell
& "e:\Health_Care_Predict_Group\backend\venv\Scripts\pip" install package-name
```

### List Installed Packages

```powershell
& "e:\Health_Care_Predict_Group\backend\venv\Scripts\pip" list
```

### Update requirements.txt

```powershell
& "e:\Health_Care_Predict_Group\backend\venv\Scripts\pip" freeze > e:\Health_Care_Predict_Group\backend\requirements.txt
```

### Install from requirements.txt

```powershell
& "e:\Health_Care_Predict_Group\backend\venv\Scripts\pip" install -r e:\Health_Care_Predict_Group\backend\requirements.txt
```

---

## 🧠 ML Model Commands

### Train/Retrain Model

```powershell
& "e:\Health_Care_Predict_Group\backend\venv\Scripts\python" "e:\Health_Care_Predict_Group\backend\train_model.py"
```

### Test Model Loading

```powershell
& "e:\Health_Care_Predict_Group\backend\venv\Scripts\python" -c "import joblib; m=joblib.load('e:\Health_Care_Predict_Group\backend\rf_model.pkl'); print('✅ Model loaded')"
```

---

## 🌐 Deploy Commands

### Docker

```bash
docker-compose up --build
# Visit http://localhost
```

### Heroku

```bash
# Install: https://devcenter.heroku.com/articles/heroku-cli
heroku login
heroku create your-app-name
git push heroku main
heroku open
```

---

## 🚨 Troubleshooting Quick Fixes

### Clear Package Cache

```powershell
& "e:\Health_Care_Predict_Group\backend\venv\Scripts\pip" cache purge
```

### Reinstall All Packages

```powershell
& "e:\Health_Care_Predict_Group\backend\venv\Scripts\pip" install --force-reinstall -r "e:\Health_Care_Predict_Group\backend\requirements.txt"
```

### Kill Port 5000 (Windows)

```powershell
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### Remove Virtual Environment

```powershell
Remove-Item -Recurse -Force "e:\Health_Care_Predict_Group\backend\venv"
```

---

## 📋 File Paths

| Purpose | Path |
|---------|------|
| **Virtual Env** | `e:\Health_Care_Predict_Group\backend\venv` |
| **Python Executable** | `e:\Health_Care_Predict_Group\backend\venv\Scripts\python` |
| **Pip** | `e:\Health_Care_Predict_Group\backend\venv\Scripts\pip` |
| **Flask App** | `e:\Health_Care_Predict_Group\backend\app.py` |
| **Train Script** | `e:\Health_Care_Predict_Group\backend\train_model.py` |
| **Model File** | `e:\Health_Care_Predict_Group\backend\rf_model.pkl` |
| **Dataset** | `e:\Health_Care_Predict_Group\backend\healthcare_risk_classification_dataset.csv` |
| **Frontend** | `e:\Health_Care_Predict_Group\frontend\index.html` |

---

## 🎯 Common Workflows

### Test Full Application

```powershell
# Terminal 1: Start Backend
& "e:\Health_Care_Predict_Group\backend\venv\Scripts\python" "e:\Health_Care_Predict_Group\backend\app.py"

# Terminal 2: Start Frontend
cd e:\Health_Care_Predict_Group\frontend
python -m http.server 8000

# Browser: http://localhost:8000
```

### Deploy to Heroku

```powershell
git add .
git commit -m "Deploy updates"
git push heroku main
heroku logs --tail
```

### Use Cloud Dataset

```python
# In train_model.py or app.py:
import pandas as pd
import gdown  # or requests

# Option 1: Google Drive
url = "https://drive.google.com/uc?export=download&id=YOUR_FILE_ID"
df = pd.read_csv(gdown.download(url, quiet=False))

# Option 2: GitHub
url = "https://raw.githubusercontent.com/user/repo/main/file.csv"
df = pd.read_csv(url)

# Option 3: Kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()
api.dataset_download_files('user/dataset', path='.', unzip=True)
df = pd.read_csv('file.csv')
```

---

## 🔗 Important Links

- **GitHub**: https://github.com
- **Kaggle**: https://kaggle.com
- **Google Drive**: https://drive.google.com
- **AWS S3**: https://aws.amazon.com/s3
- **Heroku**: https://heroku.com
- **Docker**: https://docker.com
- **Python Docs**: https://docs.python.org/3
- **Flask Docs**: https://flask.palletsprojects.com

---

## 📚 Documentation Files

- **Setup & Virtual Env**: [VENV_SETUP_VERIFICATION.md](VENV_SETUP_VERIFICATION.md)
- **Cloud Storage**: [FREE_DATASET_STORAGE_GUIDE.md](FREE_DATASET_STORAGE_GUIDE.md)
- **Initial Setup**: [SETUP_GUIDE.md](SETUP_GUIDE.md)
- **Quick Start**: [QUICK_START.md](QUICK_START.md)
- **Deployment**: [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
- **Checklist**: [DEPLOYMENT_CHECKLIST.md](DEPLOYMENT_CHECKLIST.md)
- **Project Info**: [README.md](README.md)

---

## ⚡ One-Liner Shortcuts

**Run API:**
```powershell
& "e:\Health_Care_Predict_Group\backend\venv\Scripts\python" "e:\Health_Care_Predict_Group\backend\app.py"
```

**Run Frontend:**
```powershell
cd e:\Health_Care_Predict_Group\frontend; python -m http.server 8000
```

**Run Tests:**
```powershell
& "e:\Health_Care_Predict_Group\backend\venv\Scripts\python" "e:\Health_Care_Predict_Group\backend\train_model.py"
```

**Check Status:**
```powershell
& "e:\Health_Care_Predict_Group\backend\venv\Scripts\pip" list
```

---

**Keep this card open while developing!** 📌

Last updated: February 26, 2026
