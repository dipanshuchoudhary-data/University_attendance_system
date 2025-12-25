# University Attendance System

The **University Attendance System** is a computer vision–based classroom attendance application that detects and recognizes students from a live camera feed and marks attendance only after verified continuous presence. The system is designed to reduce proxy attendance and automate attendance management using AI-driven verification.

---

## Overview

The system captures a live classroom video stream, detects and recognizes student faces, tracks their continuous presence, and records attendance only when a predefined time threshold is satisfied. A FastAPI backend manages attendance data, APIs, and database persistence. A frontend interface is planned for future integration.

---

## Core Logic

- Attendance is not marked at entry.
- Attendance is marked only after continuous verified presence inside the classroom.
- Presence duration is configurable.
- Attendance records are stored and auditable.

---

## Features

- Live camera feed ingestion using IP camera
- Real-time face detection with OpenCV
- Face recognition using deep-learning embeddings (DeepFace / FaceNet)
- Continuous presence tracking with time thresholds
- Automatic attendance marking
- CSV-based attendance export
- FastAPI backend with REST APIs
- Database integration using SQLAlchemy
- Modular and extensible project structure
- Frontend integration planned

---

## Technology Stack

- **Language:** Python 3.10  
- **Computer Vision:** OpenCV  
- **Face Recognition:** DeepFace (FaceNet)  
- **Backend:** FastAPI  
- **Database:** SQLAlchemy (SQLite default, configurable)  
- **Data Processing:** NumPy, SciPy  
- **Camera Input:** IP Webcam / Mobile Camera  

---

## Project Structure


University_attendance_system/
├── backend/
│ ├── app/
│ │ ├── main.py
│ │ ├── database.py
│ │ ├── models.py
│ │ ├── schemas.py
│ │ └── routes/
│ │ ├── auth.py
│ │ └── attendance.py
│ └── requirements.txt
│
├── camera/
│ └── stream.py
│
├── faces/
│ ├── detect.py
│ └── recognize.py
│
├── attendance/
│ ├── timer.py
│ └── attendance_log.py
│
├── data/
│ └── students/
│
├── enroll_student.py
├── generate_embeddings.py
├── main.py
├── requirements.txt
└── README.md


---

## How the System Works

1. **Camera Stream**  
   A mobile phone acts as an IP camera and provides a live video stream.

2. **Face Detection**  
   Faces are detected in real time from each frame.

3. **Face Recognition**  
   Detected faces are matched with enrolled student images.

4. **Presence Tracking**  
   The system tracks how long each recognized student remains visible.

5. **Attendance Marking**  
   Attendance is recorded only after the presence threshold is reached.

6. **Backend Storage**  
   Attendance data is stored in the database and can be exported as CSV.

---

## Installation & Usage

### 1. Clone Repository
```bash
git clone https://github.com/dipanshuchoudhary-data/University_attendance_system.git
cd University_attendance_system

2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt
cd backend
pip install -r requirements.txt
cd ..

4. Configure Camera

Install an IP camera app on a mobile phone

Connect both devices to the same network

Update the stream URL in camera/stream.py

5. Run Backend
cd backend
uvicorn app.main:app --reload


API documentation:

http://localhost:8000/docs

6. Run Attendance System
python main.py

Database

Uses SQLite by default

Can be switched to PostgreSQL or MySQL

Configuration available in backend/app/database.py

Configuration

Presence time threshold

Camera stream URL

Database connection string

Future Enhancements

Web-based frontend dashboard

Faculty and admin role management

Real-time attendance visualization

Cloud deployment

Improved recognition accuracy

