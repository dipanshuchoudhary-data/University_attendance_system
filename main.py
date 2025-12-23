import cv2
from camera.stream import CameraStream
from faces.detect import FaceDetector
from faces.recognize import FaceRecognizer
from attendance.timer import PresenceTimer
from attendance.attendance_log import log_attendance


STREAM_URL = "http://192.168.1.9:8080/video"

timer = PresenceTimer(min_duration_sec=30)  # 30 sec for testing

def main():
    camera = CameraStream(STREAM_URL).start()
    detector = FaceDetector()
    recognizer = FaceRecognizer()

    try:
        while True:
            frame = camera.read()
            if frame is None:
                continue

            faces = detector.detect(frame)

            for (x, y, w, h) in faces:
                face_img = frame[y:y + h, x:x + w]

                student_id, confidence = recognizer.recognize(face_img)

                label = "Unknown"
                if student_id:
                    label = f"{student_id} ({confidence})"

                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(
                    frame,
                    label,
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2
                )

            cv2.imshow("Face Recognition", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    finally:
        camera.stop()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
