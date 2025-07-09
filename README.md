# Log Dashboard

A simple full-stack application using **FastAPI**, **Redis**, and **AngularJS** that displays real-time log messages.

## 🔧 Tech Stack

- **Backend:** FastAPI, Redis
- **Frontend:** AngularJS
- **Others:** REST API, JSON, periodic polling with Angular `$interval`

## 🚀 Features

- Fetches messages from FastAPI backend
- Stores logs in Redis
- Displays logs on the frontend with auto-refresh

## 🛠️ How to Run

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload
