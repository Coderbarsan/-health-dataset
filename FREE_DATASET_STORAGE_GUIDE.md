# 📊 FREE DATASET STORAGE GUIDE

Your virtual environment is ready! Now learn how to store datasets for FREE using various platforms.

---

## 🎯 QUICK SUMMARY

**Your Current Setup**:
- ✅ Virtual environment: `e:\Health_Care_Predict_Group\backend\venv`
- ✅ Current dataset: Local CSV file (50 patients)
- ✅ Model trained: `rf_model.pkl` & `label_encoder.pkl`

**Next**: Store datasets in the cloud for FREE!

---

## 🔥 TOP 5 FREE DATASET STORAGE OPTIONS

### **1. GitHub (BEST - Recommended) ⭐⭐⭐⭐⭐**

**What**: Version control + free 100GB storage
**Best for**: Teams, code + data
**Cost**: FREE forever
**Limit**: Files up to 100 GB total per repo

**Setup Steps**:

```bash
# Step 1: Install Git (if not already)
# Download from: https://git-scm.com/download/win

# Step 2: Create GitHub account
# Visit: https://github.com/signup

# Step 3: Create new repository on GitHub website
# Name it: "health-dataset" or similar

# Step 4: Initialize git in your project
cd "e:\Health_Care_Predict_Group"
git init
git config user.name "Your Name"
git config user.email "your.email@gmail.com"

# Step 5: Add dataset
git add backend/healthcare_risk_classification_dataset.csv
git commit -m "Add healthcare dataset"

# Step 6: Push to GitHub
git remote add origin https://github.com/yourusername/health-dataset.git
git branch -M main
git push -u origin main
```

**Access Dataset in Code**:
```python
import pandas as pd
from urllib.request import urlopen

# Raw GitHub URL (Add ?raw=true)
url = "https://raw.githubusercontent.com/yourusername/health-dataset/main/backend/healthcare_risk_classification_dataset.csv"
df = pd.read_csv(url)
```

**Advantages**:
✅ Free forever
✅ Version control
✅ Easy to share
✅ GitHub Actions for automation
✅ Used by 90% of developers

---

### **2. Kaggle (Data Science Hub) ⭐⭐⭐⭐**

**What**: kaggle.com - Free data hosting for ML projects
**Best for**: Sharing public datasets
**Cost**: FREE
**Limit**: Unlimited files

**Setup Steps**:

```bash
# Step 1: Create Kaggle account
# Visit: https://www.kaggle.com/settings/account

# Step 2: Install Kaggle API
pip install kaggle

# Step 3: Download API key
# Account → Settings → API → Download kaggle.json
# Save to: C:\Users\[YourUsername]\.kaggle\kaggle.json

# Step 4: Create new dataset
# Visit: https://www.kaggle.com/datasets/create

# Step 5: Upload your CSV file
# Fill form and upload healthcare_risk_classification_dataset.csv

# Step 6: Make it public (optional)
# In dataset settings → Public
```

**Access Dataset in Code**:
```python
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

# Authenticate
api = KaggleApi()
api.authenticate()

# Download dataset
api.dataset_download_files('yourusername/health-risk-dataset', path='./data', unzip=True)

# Load
df = pd.read_csv('./data/healthcare_risk_classification_dataset.csv')
```

**Advantages**:
✅ Specifically for ML datasets
✅ Built-in version control
✅ Community engagement
✅ Easy sharing with URL
✅ Can be used in Kaggle competitions

---

### **3. Google Drive (Easy Integration) ⭐⭐⭐⭐**

**What**: Google Drive cloud storage
**Best for**: Simple file sharing
**Cost**: FREE (15GB initially)
**Limit**: 15GB free, $1.99/month for 100GB

**Setup Steps**:

```bash
# Step 1: Create Google Drive account
# Visit: https://drive.google.com

# Step 2: Upload CSV file
# Drag and drop healthcare_risk_classification_dataset.csv
# Right-click → Share → Anyone with link can view

# Step 3: Get shareable link
# Right-click file → Share → Copy link
# Example: https://drive.google.com/file/d/1abc123xyz/view?usp=sharing

# Step 4: Convert to direct download
# Replace: /file/d/{FILE_ID}/view
# With: /uc?export=download&id={FILE_ID}

# Step 5: Install gdown
pip install gdown
```

**Access Dataset in Code**:
```python
import pandas as pd
import gdown

# File ID from Google Drive link
file_id = "1abc123xyz"  # From your shareable link
url = f"https://drive.google.com/uc?export=download&id={file_id}"

# Download
gdown.download(url, 'healthcare_dataset.csv', quiet=False)

# Load
df = pd.read_csv('healthcare_dataset.csv')
```

**Advantages**:
✅ 15GB free
✅ Easy to share
✅ Works with Google Suite
✅ Automatic backups
✅ Can access from any device

---

### **4. AWS S3 (Scalable) ⭐⭐⭐**

**What**: Amazon Web Service cloud storage
**Best for**: Large datasets, production
**Cost**: FREE tier (5GB + bandwidth limits)
**Limit**: 5GB free first year, then $0.023/GB

**Setup Steps**:

```bash
# Step 1: Create AWS account
# Visit: https://aws.amazon.com

# Step 2: Create S3 bucket
# AWS Console → S3 → Create bucket → health-data-bucket

# Step 3: Install AWS CLI
pip install awscli

# Step 4: Configure AWS credentials
aws configure
# Enter your Access Key ID
# Enter your Secret Access Key
# Region: us-east-1
# Format: json

# Step 5: Upload dataset
aws s3 cp backend/healthcare_risk_classification_dataset.csv s3://health-data-bucket/

# Step 6: Make public (optional)
# S3 Console → Bucket → Permissions → Public Access
```

**Access Dataset in Code**:
```python
import pandas as pd
import boto3

# Create S3 client
s3 = boto3.client('s3')

# Download file
s3.download_file(
    'health-data-bucket',
    'healthcare_risk_classification_dataset.csv',
    'local_file.csv'
)

# Load
df = pd.read_csv('local_file.csv')
```

**Advantages**:
✅ Enterprise-level
✅ Highly scalable
✅ Good for large datasets
✅ Integration with other AWS services
✅ 5GB free first year

---

### **5. Zenodo (Academic) ⭐⭐⭐**

**What**: Zenodo.org - Free research data repository
**Best for**: Academic/research projects
**Cost**: FREE forever
**Limit**: Unlimited uploads (up to 50GB per file)

**Setup Steps**:

```bash
# Step 1: Create Zenodo account
# Visit: https://zenodo.org/signup

# Step 2: Create new upload
# Click "New Upload" button

# Step 3: Upload your CSV
# Drag healthcare_risk_classification_dataset.csv

# Step 4: Fill metadata
# Title: Healthcare Risk Classification Dataset
# Description: Your description
# License: Creative Commons

# Step 5: Publish
# Click Publish
# You get a DOI (Digital Object Identifier)
```

**Access Dataset in Code**:
```python
import pandas as pd
import requests

# Zenodo download URL
zenodo_url = "https://zenodo.org/record/YOUR_RECORD_ID/files/healthcare_risk_classification_dataset.csv"

df = pd.read_csv(zenodo_url)
```

**Advantages**:
✅ Free forever
✅ Citable with DOI
✅ Good for research
✅ Unlimited storage
✅ Open access

---

## 📊 COMPARISON TABLE

| Platform | Cost | Storage | Best For | Setup Time |
|----------|------|---------|----------|-----------|
| **GitHub** | FREE | 100GB | Code + Data | 5 min |
| **Kaggle** | FREE | Unlimited | ML Datasets | 10 min |
| **Google Drive** | FREE | 15GB | Simple Sharing | 3 min |
| **AWS S3** | FREE (5GB) | Scalable | Production | 15 min |
| **Zenodo** | FREE | Unlimited | Research | 8 min |

---

## 🚀 RECOMMENDED: GitHub + Kaggle COMBO

**Why This Works Best**:
1. **GitHub**: Store code + version history
2. **Kaggle**: Host large datasets, share with ML community
3. **Free forever**: Both platforms
4. **Easy to share**: One link per dataset

**Step-by-Step Setup**:

### **Step 1: Push Code to GitHub**
```bash
cd "e:\Health_Care_Predict_Group"
git init
git add .
git commit -m "Initial health risk prediction project"
git remote add origin https://github.com/yourusername/health-risk-prediction.git
git push -u origin main
```

### **Step 2: Upload Dataset to Kaggle**
1. Go to kaggle.com
2. Click "Create" → "Dataset"
3. Upload healthcare_risk_classification_dataset.csv
4. Make public
5. Get your dataset URL

### **Step 3: Update Code with Remote Dataset**

Edit [backend/train_model.py](../backend/train_model.py):

```python
# Old:
csv_path = os.path.join(os.path.dirname(__file__), "healthcare_risk_classification_dataset.csv")
df = pd.read_csv(csv_path)

# New (if using Kaggle):
import gdown
import os

DATASET_ID = "yourusername/health-risk-dataset"  # Your Kaggle dataset ID

# Download from Kaggle
if not os.path.exists("healthcare_risk_classification_dataset.csv"):
    os.system(f"kaggle datasets download -d {DATASET_ID}")
    import zipfile
    with zipfile.ZipFile(f'{DATASET_ID.split("/")[1]}.zip', 'r') as zip_ref:
        zip_ref.extractall()

csv_path = "healthcare_risk_classification_dataset.csv"
df = pd.read_csv(csv_path)
```

### **Step 4: Share Both Links**
- **Code**: `https://github.com/yourusername/health-risk-prediction`
- **Dataset**: `https://www.kaggle.com/datasets/yourusername/health-risk-dataset`

---

## 📈 SCALING: LARGE DATASETS (GB+ Size)

If you have large datasets (> 1GB):

**Option 1: Use Multiple Files**
```bash
# Split large CSV
split -l 10000 large_dataset.csv chunk_

# Upload chunks to GitHub/Kaggle
# In code, read and concatenate:
import pandas as pd
import glob

files = glob.glob('chunk_*')
df_list = [pd.read_csv(f) for f in files]
df = pd.concat(df_list, ignore_index=True)
```

**Option 2: Use Database**
```bash
# Use SQLite (free, no setup)
import sqlite3

# Create database
conn = sqlite3.connect('health_data.db')
df.to_sql('patients', conn, if_exists='replace')

# Later, read from database
df = pd.read_sql('SELECT * FROM patients', conn)

# Upload .db file (~1/3 size of CSV)
```

**Option 3: Use Parquet Format**
```bash
# Parquet is 50% smaller than CSV
import pandas as pd

df = pd.read_csv('large_dataset.csv')
df.to_parquet('health_data.parquet')  # Much smaller!

# Later, read back
df = pd.read_parquet('health_data.parquet')
```

---

## 🔄 UPDATING DATASETS

### **Update Dataset on GitHub**
```bash
cd "e:\Health_Care_Predict_Group"

# Make changes to CSV file

# Commit and push
git add backend/healthcare_risk_classification_dataset.csv
git commit -m "Update dataset with 10 new records"
git push origin main
```

### **Update Dataset on Kaggle**
1. Go to your dataset on Kaggle
2. Click "Edit Dataset"
3. Delete old files
4. Upload new CSV
5. Save

### **Load Latest from GitHub in Code**
```python
import pandas as pd
import requests
from io import StringIO

url = "https://raw.githubusercontent.com/yourusername/repo/main/backend/healthcare_risk_classification_dataset.csv"
response = requests.get(url)
df = pd.read_csv(StringIO(response.text))
```

---

## 🔒 PRIVACY & SENSITIVE DATA

**⚠️ Important**: Only upload **public, anonymized data**!

**Protect Sensitive Data**:
```python
# Remove personally identifiable information
df = df.drop(['Patient_Name', 'SSN', 'Phone', 'Email'], axis=1)

# Keep only: Age, BMI, BP, etc. (no personal info)

# Upload anonymized version only
df.to_csv('healthcare_risk_classification_dataset.csv', index=False)
```

---

## 💰 Cost Comparison (1 Year)

| Platform | 10GB | 50GB | 100GB |
|----------|------|------|-------|
| **GitHub** | FREE | FREE | FREE |
| **Kaggle** | FREE | FREE | FREE |
| **Google Drive** | FREE | $1.99/mo | FREE (100GB) |
| **AWS S3** | FREE | $1.15/mo | $2.30/mo |
| **Zenodo** | FREE | FREE | FREE |

**Winner**: GitHub + Kaggle (Both FREE forever!)

---

## ✅ YOUR SETUP CHECKLIST

After completing your setup:

- [ ] Virtual environment created and activated
- [ ] All dependencies installed
- [ ] ML model trained successfully
- [ ] Choose primary dataset storage (GitHub or Kaggle)
- [ ] Create account on chosen platform
- [ ] Upload dataset
- [ ] Get shareable dataset URL
- [ ] Update code to load from cloud (optional)
- [ ] Test loading data from cloud
- [ ] Share dataset with team

---

## 🎓 ADDITIONAL RESOURCES

**Learn Git:**
- https://github.com/git-tips/tips
- https://git-scm.com/book

**Kaggle API:**
- https://github.com/Kaggle/kaggle-api
- https://kaggle.com/docs/api

**AWS S3:**
- https://aws.amazon.com/s3/getting-started/
- https://docs.aws.amazon.com/s3/

**Google Drive API:**
- https://developers.google.com/drive
- https://github.com/iterative/gdown

---

## 📞 QUICK SUPPORT

| Problem | Solution |
|---------|----------|
| **Virtual env not activating** | Use full path: `e:\...\venv\Scripts\activate` |
| **Packages not installing** | Use complete pip path: `venv\Scripts\pip install` |
| **Can't upload large files** | Split into chunks or use Parquet format |
| **GitHub authentication failing** | Create personal access token at Settings → Developer |
| **Kaggle API key not found** | Ensure kaggle.json is in `C:\Users\YourName\.kaggle\` |

---

## 🚀 NEXT STEPS

1. **Choose your dataset storage platform**
   - Recommended: GitHub (for code) + Kaggle (for data)

2. **Create accounts** (takes 5 minutes each)

3. **Upload dataset**
   - GitHub: git push
   - Kaggle: Web upload

4. **Update your code** to load from cloud (optional but recommended)

5. **Share with your team**
   - GitHub link for code
   - Kaggle link for dataset

---

**Your Virtual Environment is Ready! 🎉**

Now you have:
✅ Isolated Python environment
✅ All packages installed
✅ ML model trained  
✅ Multiple free storage options

**Time to deploy!** 🚀

---

*Last Updated: February 2026*
*Status: Production Ready*
