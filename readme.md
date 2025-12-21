# University Attendance System (Prototype)

A computer vision–based classroom attendance prototype that detects and recognizes students from a live camera feed and marks attendance **only after verified continuous presence**.  
The system is designed to prevent proxy attendance and reduce manual workload for faculty.

> ⚠️ This repository represents a **functional prototype**, not a production-ready system.

---

## Motivation

In many universities, biometric attendance systems are installed outside classrooms. This allows students to mark attendance without attending lectures, leading to proxy attendance and unethical practices.

This project addresses the problem by shifting attendance logic from **one-time authentication** to **time-based presence verification inside the classroom**.

---

## Core Idea

Attendance is **not marked at entry**.  
Attendance is marked **only when a student remains continuously present inside the classroom for a minimum duration**, verified using computer vision.

---

## Features (Prototype Scope)

- Live camera feed ingestion (mobile phone used as IP camera)
- Real-time face detection using OpenCV
- Face recognition using deep-learning embeddings (DeepFace / FaceNet)
- Continuous presence tracking with configurable time threshold
- Automatic attendance marking
- CSV-based attendance logging for auditability
- Modular and extensible code structure

---

## Tech Stack

- Python 3.10  
- OpenCV  
- DeepFace (FaceNet)  
- NumPy, SciPy  
- IP Webcam / Mobile Camera (prototype input)

---

## Project Structure

University_attendance_system/
├── camera/
│ └── stream.py
├── faces/
│ ├── detect.py
│ └── recognize.py
├── attendance/
│ ├── timer.py
│ └── attendance_log.py
├── data/
│ └── students/
│ ├── 100/
│ │ ├── img_01.jpg
│ │ └── img_02.jpg
│ └── 101/
│ └── img_01.jpg
├── enroll_student.py
├── main.py
└── README.md


---

## How It Works

1. **Camera Stream**  
   A live video stream is received from a phone acting as an IP camera.

2. **Face Detection**  
   Faces are detected in real time using OpenCV.

3. **Face Recognition**  
   Detected faces are matched against stored student photos.

4. **Presence Timer**  
   A timer tracks how long each recognized student remains present.

5. **Attendance Marking**  
   Attendance is marked only after the defined presence duration is reached.

6. **Audit Log**  
   Attendance records are saved in a CSV file.
