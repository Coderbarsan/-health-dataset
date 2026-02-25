@echo off
REM Health Risk Prediction System - Quick Start Script (Windows)
REM This script sets up and starts the application

echo.
echo ========================================
echo  Health Risk Prediction System
echo  Quick Start Script (Windows)
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

echo [1/5] Creating virtual environment...
cd backend
if not exist venv (
    python -m venv venv
    echo Virtual environment created.
) else (
    echo Virtual environment already exists.
)

echo.
echo [2/5] Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo [3/5] Installing dependencies...
pip install -q -r requirements.txt
echo Dependencies installed.

echo.
echo [4/5] Training Machine Learning model...
python train_model.py
echo Model training complete.

echo.
echo [5/5] Starting Flask API server...
echo.
echo ========================================
echo  Backend API Server Starting
echo ========================================
echo.
echo API will be available at: http://localhost:5000
echo Press Ctrl+C to stop the server
echo.
echo In a new terminal, run this to start frontend:
echo   cd frontend
echo   python -m http.server 8000
echo.
echo Then visit: http://localhost:8000
echo ========================================
echo.

python app.py

pause
