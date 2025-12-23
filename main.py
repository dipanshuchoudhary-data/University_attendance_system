import cv2
from datetime import datetime
from camera.stream import CameraStream
from faces.detect import FaceDetector
from faces.recognize import FaceRecognizer
from attendance.timer import PresenceTimer
from attendance.attendance_log import log_attendance
from attendance.session import Class_Session
from attendance.schedule_loader import get_current_class



STREAM_URL = "http://192.168.1.9:8080/video"

FRAME_SIZE = (640, 480)
FRAME_SKIP = 3
RECOGNITION_INTERVAL = 10

PRESENCE_TIME_SEC = 30 



def main():
    camera = CameraStream(STREAM_URL).start()
    detector = FaceDetector()
    recognizer = FaceRecognizer()

    frame_count = 0
    recognition_cache = {}

    class_active = False
    timer = None
    current_session = None

    print("[SYSTEM] Waiting for scheduled class...")

    try:
        while True:
            frame = camera.read()
            if frame is None:
                continue

            frame = cv2.resize(frame, FRAME_SIZE)
            frame_count += 1

            # -----------------------------
            # KEYBOARD CONTROL
            # -----------------------------
            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break

            #  START
            if key == ord("s") and not class_active:
                scheduled = get_current_class()
                if scheduled:
                    current_session = Class_Session(
                        subject=scheduled["subject"],
                        start_time=scheduled["start_time"],
                        end_time=scheduled["end_time"]
                    )
                    timer = PresenceTimer(min_duration_sec=PRESENCE_TIME_SEC)
                    class_active = True
                    print(f"[CLASS STARTED] {current_session.subject}")
                else:
                    print("[INFO] No class scheduled at this time")

            #END
            if key == ord("e") and class_active:
                class_active = False
                timer = None
                print(f"[CLASS ENDED] {current_session.subject}")
                current_session = None

            # -----------------------------
            # AUTO-SCHEDULE CHECK
            # -----------------------------
            if not class_active:
                scheduled = get_current_class()
                if scheduled:
                    current_session = Class_Session(
                        subject=scheduled["subject"],
                        start_time=scheduled["start_time"],
                        end_time=scheduled["end_time"]
                    )
                    timer = PresenceTimer(min_duration_sec=PRESENCE_TIME_SEC)
                    class_active = True
                    print(f"[AUTO START] {current_session.subject}")


            status = "CLASS ACTIVE" if class_active else "NO ACTIVE CLASS"
            color = (0, 255, 0) if class_active else (0, 0, 255)

            cv2.putText(
                frame,
                status,
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                color,
                2
            )

            if current_session:
                cv2.putText(
                    frame,
                    current_session.subject,
                    (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (255, 255, 255),
                    2
                )

            # -----------------------------
            # SKIP FRAMES FOR PERFORMANCE
            # -----------------------------
            if frame_count % FRAME_SKIP != 0:
                cv2.imshow("Attendance System", frame)
                continue

            # -----------------------------
            # ATTENDANCE LOGIC
            # -----------------------------
            if class_active and timer:
                faces = detector.detect(frame)

                for (x, y, w, h) in faces:
                    face_img = frame[y:y + h, x:x + w]
                    face_key = (x // 20, y // 20, w // 20, h // 20)

                    student_id, confidence = None, None

                    if frame_count % RECOGNITION_INTERVAL == 0:
                        student_id, confidence = recognizer.recognize(face_img)
                        recognition_cache[face_key] = (student_id, confidence)
                    else:
                        student_id, confidence = recognition_cache.get(
                            face_key, (None, None)
                        )

                    label = "Unknown"
                    if student_id:
                        timer.update(student_id)
                        label = f"{student_id} ({confidence})"

                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv2.putText(
                        frame,
                        label,
                        (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.75,
                        (0, 255, 0),
                        2
                    )

                # -----------------------------
                # MARK ATTENDANCE
                # -----------------------------
                newly_marked = timer.check_attendance()
                for sid in newly_marked:
                    log_attendance(sid, current_session)
                    print(
                        f"[ATTENDANCE] {sid} marked present for {current_session.subject}"
                    )

            cv2.imshow("Attendance System", frame)

    finally:
        camera.stop()
        cv2.destroyAllWindows()
        print("[SYSTEM] Shutdown complete")


if __name__ == "__main__":
    main()
