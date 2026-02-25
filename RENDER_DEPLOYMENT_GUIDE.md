# Render.com Deployment Guide (Free, Lifetime)

## 1. Sign Up & Create New Web Service
- Go to https://render.com
- Sign up (free)
- Click "New" > "Web Service"

## 2. Connect Your GitHub Repo
- Authorize Render to access your GitHub
- Select your repo: `-health-dataset`

## 3. Configure Backend (Flask)
- Select root directory: `backend`
- Set build command: `pip install -r requirements.txt`
- Set start command: `python app.py` (or `gunicorn app:app` for production)
- Choose free plan

## 4. Configure Frontend (Static Site)
- Click "New" > "Static Site"
- Select root directory: `frontend`
- Set build command: (leave blank)
- Set publish directory: `frontend`
- Choose free plan

## 5. Set Environment Variables (if needed)
- Add any secrets (e.g., Supabase keys) in Render dashboard

## 6. Deploy
- Click "Deploy" for both services
- Wait for build and deployment to finish
- Access your live URLs (provided by Render)

## 7. Lifetime Validity
- Render's free tier is permanent for small projects
- No credit card required
- Backend may sleep after inactivity, but wakes on request

---

**Tips:**
- Update code by pushing to GitHub; Render auto-redeploys
- For custom domains, use Render's domain settings
- For API/backend, use Flask's CORS support (already enabled)
- For static frontend, all HTML/CSS/JS is supported

**Docs:**
- https://render.com/docs/deploy-flask
- https://render.com/docs/static-sites

If you need help with Render config, environment variables, or troubleshooting, let me know!
