# FREE DATASET STORAGE: GitHub Guide

## Steps to Store Your Dataset on GitHub

1. **Install Git**
   - Download from: https://git-scm.com/download/win

2. **Create a GitHub Account**
   - Sign up at: https://github.com/signup

3. **Create a New Repository**
   - Go to https://github.com/new
   - Name it: `health-dataset` or similar

4. **Initialize Git in Your Project Folder**
   - Open terminal in your project directory:
     ```
     cd E:\Health_Care_Predict_Group
     git init
     ```

5. **Add Your Dataset File**
   - Place `healthcare_risk_classification_dataset.csv` in your project folder
   - Run:
     ```
     git add backend/healthcare_risk_classification_dataset.csv
     git commit -m "Add health risk dataset"
     ```

6. **Connect to GitHub Remote**
   - Get your repo URL (e.g., `https://github.com/yourusername/health-dataset.git`)
   - Run:
     ```
     git remote add origin <your-repo-url>
     git branch -M main
     git push -u origin main
     ```

7. **Verify Upload**
   - Visit your repo on GitHub and confirm the CSV file is present.

## Tips
- You can update the dataset anytime with `git add`, `git commit`, and `git push`.
- Share the repo link for easy access and collaboration.

---

For more details, see the official GitHub docs: https://docs.github.com/en/repositories/creating-and-managing-repositories
