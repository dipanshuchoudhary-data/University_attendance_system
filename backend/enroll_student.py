import os
import cv2
from camera.stream import CameraStream
from faces.detect import FaceDetector

STREAM_URL = "http://192.168.1.9:8080/video"
DATA_DIR = "data/Students"
REQUIRED_IMAGES = 10


def enroll_student(student_id: str):
    student_dir = os.path.join(DATA_DIR, student_id)
    os.makedirs(student_dir, exist_ok=True)

    camera = CameraStream(STREAM_URL).start()
    detector = FaceDetector()

    print(f"[INFO] Enrolling student: {student_id}")
    print("[INFO] Press 'c' to capture face, 'q' to quit")

    count = 0

    try:
        while True:
            frame = camera.read()

            # If stream drops, keep window responsive
            if frame is None:
                key = cv2.waitKey(30) & 0xFF
                if key == ord("q"):
                    break
                continue

            faces = detector.detect(frame)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.putText(
                frame,
                f"Captured: {count}/{REQUIRED_IMAGES}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            cv2.imshow("Enrollment - Face Capture", frame)
            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                print("[INFO] Enrollment aborted by user")
                break

            if key == ord("c") and len(faces) >= 1:
                # Select largest detected face
                faces = sorted(faces, key=lambda f: f[2] * f[3], reverse=True)
                x, y, w, h = faces[0]

                face_img = frame[y:y + h, x:x + w].copy()

                if face_img.size == 0:
                    print("[WARNING] Empty face crop detected. Skipping.")
                    continue

                img_path = os.path.join(student_dir, f"img_{count + 1:02d}.jpg")
                cv2.imwrite(img_path, face_img)

                count += 1
                print(f"[INFO] Captured image {count}/{REQUIRED_IMAGES}")

                if count >= REQUIRED_IMAGES:
                    print("[SUCCESS] Enrollment completed successfully")
                    break

    finally:
        camera.stop()
        cv2.destroyAllWindows()

    if count < REQUIRED_IMAGES:
        print("[WARNING] Enrollment incomplete")


if __name__ == "__main__":
    student_id = input("Enter Enrollment_number: ").strip()
    enroll_student(student_id)
