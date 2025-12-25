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

