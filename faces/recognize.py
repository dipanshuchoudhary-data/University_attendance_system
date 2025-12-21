import os
import numpy as np
from deepface import DeepFace
from scipy.spatial.distance import cosine


class FaceRecognizer:
    def __init__(self, students_dir="data/Students", threshold=0.4):
        self.students_dir = students_dir
        self.threshold = threshold
        self.database = {}  # student_id -> list of embeddings
        self._load_database()

    def _load_database(self):
        print("[INFO] Loading student face database...")

        for student_id in os.listdir(self.students_dir):
            student_path = os.path.join(self.students_dir, student_id)
            if not os.path.isdir(student_path):
                continue

            embeddings = []

            for img_name in os.listdir(student_path):
                img_path = os.path.join(student_path, img_name)

                try:
                    embedding = DeepFace.represent(
                        img_path=img_path,
                        model_name="Facenet",
                        enforce_detection=True
                    )[0]["embedding"]

                    embeddings.append(embedding)

                except Exception:
                    continue

            if embeddings:
                self.database[student_id] = embeddings
                print(f"[INFO] Loaded {len(embeddings)} images for student {student_id}")

        print("[INFO] Face database ready")

    def recognize(self, face_img):
        """
        face_img: cropped face (BGR image)
        Returns: (student_id, confidence) or (None, None)
        """
        try:
            embedding = DeepFace.represent(
                img_path=face_img,
                model_name="Facenet",
                enforce_detection=False
            )[0]["embedding"]

        except Exception:
            return None, None

        best_match = None
        best_score = float("inf")

        for student_id, embeddings in self.database.items():
            for ref_embedding in embeddings:
                dist = cosine(embedding, ref_embedding)

                if dist < best_score:
                    best_score = dist
                    best_match = student_id

        if best_score < self.threshold:
            confidence = round(1 - best_score, 2)
            return best_match, confidence

        return None, None
