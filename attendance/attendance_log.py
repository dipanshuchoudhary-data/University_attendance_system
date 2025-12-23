import csv
import os
from datetime import datetime


LOG_FILE = "attendance/attendance.csv"


def log_attendance(student_id, class_id="CS101"):
    file_exists = os.path.exists(LOG_FILE)

    with open(LOG_FILE, mode="a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["student_id", "class_id", "timestamp"])

        writer.writerow([
            student_id,
            class_id,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ])
