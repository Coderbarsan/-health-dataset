// Configuration
const API_BASE_URL = 'https://health-backend-nh6o.onrender.com';

// DOM Elements
const form = document.getElementById('predictionForm');
const resultsSection = document.getElementById('resultsSection');
const loadingSpinner = document.getElementById('loadingSpinner');
const errorMessage = document.getElementById('errorMessage');
const apiStatus = document.getElementById('apiStatus');
const statusText = document.getElementById('status-text');
const statusIndicator = document.getElementById('status-indicator');

// Check API status on page load
document.addEventListener('DOMContentLoaded', () => {
    checkAPIStatus();
    form.addEventListener('submit', handleFormSubmit);
});

// Check API Health
async function checkAPIStatus() {
    try {
        const response = await fetch(`${API_BASE_URL}/health`);
        if (response.ok) {
            apiStatus.textContent = 'Online';
            apiStatus.style.color = '#10b981';
            statusText.textContent = 'System Ready';
            statusIndicator.className = 'status-dot healthy';
        } else {
            setAPIError('API returned an error');
        }
    } catch (error) {
        setAPIError('API is offline');
        console.error('API Status Check Error:', error);
    }
}

// Set API Error Status
function setAPIError(message) {
    apiStatus.textContent = 'Offline';
    apiStatus.style.color = '#ef4444';
    statusText.textContent = message;
    statusIndicator.className = 'status-dot error';
}

// Handle Form Submission
async function handleFormSubmit(e) {
    e.preventDefault();

    // Hide previous results
    resultsSection.style.display = 'none';
    errorMessage.style.display = 'none';

    // Show loading spinner
    loadingSpinner.style.display = 'flex';

    // Get form data
    const formData = new FormData(form);
    const patientData = {
        patient_id: parseInt(formData.get('patient_id')),
        patient_name: formData.get('patient_name'),
        age: parseFloat(formData.get('age')),
        bmi: parseFloat(formData.get('bmi')),
        blood_pressure: parseFloat(formData.get('blood_pressure')),
        cholesterol: parseFloat(formData.get('cholesterol')),
        smoking: parseInt(formData.get('smoking')),
        diabetes: parseInt(formData.get('diabetes')),
        heart_disease: parseInt(formData.get('heart_disease'))
    };

    try {
        // Make API request to /predict
        const response = await fetch(`${API_BASE_URL}/predict`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(patientData)
        });
        if (!response.ok) {
            throw new Error('Failed to get prediction');
        }
        const result = await response.json();
        // Also store patient in DB
        await fetch(`${API_BASE_URL}/add_patient`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(patientData)
        });
        // Hide loading spinner
        loadingSpinner.style.display = 'none';
        // Display results
        displayResults(result, patientData);
        resultsSection.style.display = 'block';
        // Scroll to results
        setTimeout(() => {
            resultsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }, 100);
    } catch (error) {
        // Hide loading spinner
        loadingSpinner.style.display = 'none';
        // Display error message
        showError(`Error: ${error.message}. Please ensure the backend API is running.`);
        console.error('Prediction Error:', error);
    }
}

// Display Results
function displayResults(result, patientData) {
    // Update risk level
    const riskLevel = result.prediction.risk_level;
    const riskLevelElement = document.getElementById('riskLevel');
    const riskCard = document.getElementById('riskCard');

    riskLevelElement.textContent = riskLevel.toUpperCase();
    riskLevelElement.className = `risk-level ${riskLevel.toLowerCase()}`;

    // Update border color based on risk
    if (riskLevel === 'LOW') {
        riskCard.style.borderLeftColor = '#10b981';
    } else if (riskLevel === 'MEDIUM') {
        riskCard.style.borderLeftColor = '#f59e0b';
    } else {
        riskCard.style.borderLeftColor = '#ef4444';
    }

    // Update confidence
    document.getElementById('confidence').textContent =
        result.prediction.model_confidence.toFixed(1) + '%';

    // Update patient info
    document.getElementById('displayAge').textContent = patientData.age;
    document.getElementById('displayBMI').textContent = patientData.bmi.toFixed(1);
    document.getElementById('displayBP').textContent = patientData.blood_pressure;
    document.getElementById('displayCholesterol').textContent = patientData.cholesterol;

    // Display recommendations
    displayRecommendations(result.recommendations);

    // Display probability chart
    displayProbabilityChart(result.prediction.probabilities);
}

// Display Recommendations
function displayRecommendations(recommendations) {
    const container = document.getElementById('recommendations');
    container.innerHTML = '';

    recommendations.forEach(rec => {
        const div = document.createElement('div');
        div.className = 'recommendation-item';

        // Determine class based on severity
        if (rec.includes('[CRITICAL]')) {
            div.className += ' critical';
        } else if (rec.includes('[ALERT]')) {
            div.className += ' alert';
        } else if (rec.includes('[WARNING]')) {
            div.className += ' warning';
        } else if (rec.includes('[HEALTHY]')) {
            div.className += ' healthy';
        } else {
            div.className += ' info';
        }

        div.textContent = rec;
        container.appendChild(div);
    });
}

// Display Probability Chart
function displayProbabilityChart(probabilities) {
    const container = document.getElementById('probabilityChart');
    container.innerHTML = '';

    // Sort probabilities by key
    const sortedProbs = Object.entries(probabilities).sort();

    sortedProbs.forEach(([label, percentage]) => {
        const groupDiv = document.createElement('div');
        groupDiv.className = 'probability-bar-group';

        const labelDiv = document.createElement('div');
        labelDiv.className = 'probability-label';
        labelDiv.textContent = label;

        const containerDiv = document.createElement('div');
        containerDiv.className = 'probability-bar-container';

        const barDiv = document.createElement('div');
        barDiv.className = 'probability-bar';

        // Determine bar color based on label
        if (label.toLowerCase() === 'low') {
            barDiv.className += ' low';
        } else if (label.toLowerCase() === 'medium') {
            barDiv.className += ' medium';
        } else {
            barDiv.className += ' high';
        }

        barDiv.textContent = percentage.toFixed(1) + '%';
        barDiv.style.width = '0%';

        containerDiv.appendChild(barDiv);
        groupDiv.appendChild(labelDiv);
        groupDiv.appendChild(containerDiv);
        container.appendChild(groupDiv);

        // Animate bar
        setTimeout(() => {
            barDiv.style.width = percentage.toFixed(1) + '%';
        }, 100);
    });
}

// Show Error Message
function showError(message) {
    errorMessage.textContent = message;
    errorMessage.style.display = 'block';
    errorMessage.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// Scroll to Form
function scrollToForm() {
    const formSection = document.querySelector('.form-section');
    formSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
    form.reset();
    resultsSection.style.display = 'none';
}

// Form Validation
form.addEventListener('input', () => {
    const age = parseFloat(document.getElementById('age').value);
    const bmi = parseFloat(document.getElementById('bmi').value);
    const bp = parseFloat(document.getElementById('blood_pressure').value);

    // Show warnings for extreme values
    if (age < 0 || age > 120) {
        console.warn('Age value seems unusual');
    }
    if (bmi < 10 || bmi > 60) {
        console.warn('BMI value seems unusual');
    }
    if (bp < 70 || bp > 250) {
        console.warn('Blood Pressure value seems unusual');
    }
});

// Refresh API status every 30 seconds
setInterval(checkAPIStatus, 30000);
