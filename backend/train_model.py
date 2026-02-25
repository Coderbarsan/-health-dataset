import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import os

# 1️⃣ Load Dataset
csv_path = os.path.join(os.path.dirname(__file__), "healthcare_risk_classification_dataset.csv")
df = pd.read_csv(csv_path)

print("First 5 rows:")
print(df.head())

# 2️⃣ Separate Features and Target
X = df.drop(["Risk_Level"], axis=1)
y = df["Risk_Level"]

# 3️⃣ Convert Target (Low/Medium/High → 0,1,2)
le = LabelEncoder()
y = le.fit_transform(y)

print("Target Classes:", le.classes_)

# 4️⃣ Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# 5️⃣ Hyperparameter Tuning with GridSearchCV
from sklearn.model_selection import GridSearchCV

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid,
                           cv=3, n_jobs=-1, verbose=2)
grid_search.fit(X_train, y_train)

best_rf_model = grid_search.best_estimator_
print("Best parameters:", grid_search.best_params_)

rf_pred = best_rf_model.predict(X_test)

print("\nRandom Forest Accuracy:", accuracy_score(y_test, rf_pred))
print("\nClassification Report (Random Forest):")
print(classification_report(y_test, rf_pred))

# 6️⃣ Save best model and label encoder
model_path = os.path.join(os.path.dirname(__file__), "rf_model.pkl")
encoder_path = os.path.join(os.path.dirname(__file__), "label_encoder.pkl")

joblib.dump(best_rf_model, model_path)
joblib.dump(le, encoder_path)

print(f"\nModel saved to {model_path}")
print(f"Label encoder saved to {encoder_path}")
