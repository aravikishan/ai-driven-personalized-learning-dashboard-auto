from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List, Dict
from datetime import datetime
import sqlite3
import os

app = FastAPI()

# Database setup
DATABASE_URL = 'sqlite:///./test.db'

if not os.path.exists('./test.db'):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            preferences TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            content TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE progress (
            user_id INTEGER,
            course_id INTEGER,
            completion REAL,
            last_accessed DATETIME,
            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(course_id) REFERENCES courses(id)
        )
    ''')
    # Seed data
    cursor.execute("INSERT INTO users (name, email, preferences) VALUES ('John Doe', 'john@example.com', '{}')")
    cursor.execute("INSERT INTO courses (title, description, content) VALUES ('Python Basics', 'Learn the basics of Python.', '[\"Introduction\", \"Variables\", \"Loops\"]')")
    cursor.execute("INSERT INTO progress (user_id, course_id, completion, last_accessed) VALUES (1, 1, 0.5, ?)" , (datetime.now(),))
    conn.commit()
    conn.close()

# Static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Data models
class User(BaseModel):
    id: int
    name: str
    email: str
    preferences: Dict

class Course(BaseModel):
    id: int
    title: str
    description: str
    content: List[str]

class Progress(BaseModel):
    user_id: int
    course_id: int
    completion: float
    last_accessed: datetime

# API Endpoints
@app.get("/api/users/{user_id}/recommendations")
async def get_recommendations(user_id: int):
    # Mock recommendation logic
    return {"recommendations": ["Advanced Python", "Data Science with Python"]}

@app.get("/api/courses")
async def get_courses():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses")
    courses = cursor.fetchall()
    conn.close()
    return courses

@app.post("/api/users")
async def create_user(user: User):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email, preferences) VALUES (?, ?, ?)", (user.name, user.email, str(user.preferences)))
    conn.commit()
    conn.close()
    return {"message": "User created successfully"}

@app.get("/api/users/{user_id}/progress")
async def get_user_progress(user_id: int):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM progress WHERE user_id = ?", (user_id,))
    progress = cursor.fetchall()
    conn.close()
    return progress

# HTML Endpoints
@app.get("/", response_class=HTMLResponse)
async def dashboard(request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/courses", response_class=HTMLResponse)
async def courses(request):
    return templates.TemplateResponse("courses.html", {"request": request})

@app.get("/profile", response_class=HTMLResponse)
async def profile(request):
    return templates.TemplateResponse("profile.html", {"request": request})

@app.get("/analytics", response_class=HTMLResponse)
async def analytics(request):
    return templates.TemplateResponse("analytics.html", {"request": request})

@app.get("/settings", response_class=HTMLResponse)
async def settings(request):
    return templates.TemplateResponse("settings.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
