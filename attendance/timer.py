import time


class PresenceTimer:
    def __init__(self, min_duration_sec=1800, grace_sec=5):
        """
        min_duration_sec: required presence time (e.g. 30 min = 1800 sec)
        grace_sec: allowed temporary face loss
        """
        self.min_duration = min_duration_sec
        self.grace_sec = grace_sec

        self.active = {}      # student_id -> last_seen_time
        self.start_time = {}  # student_id -> first_seen_time
        self.marked = set()   # students already marked present

    def update(self, student_id):
        now = time.time()

        if student_id not in self.start_time:
            self.start_time[student_id] = now

        self.active[student_id] = now

    def check_attendance(self):
        now = time.time()
        present_students = []

        for student_id in list(self.active.keys()):
            last_seen = self.active[student_id]

            # Remove if face disappeared beyond grace period
            if now - last_seen > self.grace_sec:
                self.active.pop(student_id, None)
                self.start_time.pop(student_id, None)
                continue

            duration = now - self.start_time.get(student_id, now)

            if duration >= self.min_duration and student_id not in self.marked:
                self.marked.add(student_id)
                present_students.append(student_id)

        return present_students
