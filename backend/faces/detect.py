import cv2


class FaceDetector:
    """
    Handles face detection using Haar Cascades.
    No recognition, no tracking.
    """

    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )

        if self.face_cascade.empty():
            raise RuntimeError("Failed to load Haar Cascade model")

    def detect(self, frame):
        """
        Detect faces in a single frame.

        Returns:
            List of (x, y, w, h)
        """
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5,
            minSize=(60, 60)
        )

        return faces
