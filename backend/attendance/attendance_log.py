import csv
import os
from datetime import datetime

LOG_FILE = "attendance/attendance.csv"


def log_attendance(student_id, session):
    file_exists = os.path.exists(LOG_FILE)

    with open(LOG_FILE, mode="a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "student_id",
                "subject",
                "date",
                "start_time",
                "end_time",
                "timestamp"
            ])

        writer.writerow([
            student_id,
            session.subject,
            session.date,
            session.start_time,
            session.end_time,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ])
