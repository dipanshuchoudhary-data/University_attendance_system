import os
import numpy as np
from scipy.spatial.distance import cosine
from deepface import DeepFace


class FaceRecognizer:
    def __init__(self, embeddings_dir="data/embeddings", threshold=0.4):
        self.embeddings_dir = embeddings_dir
        self.threshold = threshold
        self.database = {}
        self._load_embeddings()

    def _load_embeddings(self):
        print("[INFO] Loading face embeddings...")

        for file in os.listdir(self.embeddings_dir):
            if file.endswith(".npy"):
                student_id = file.replace(".npy", "")
                path = os.path.join(self.embeddings_dir, file)
                self.database[student_id] = np.load(path)

        print("[INFO] Embeddings loaded")

    def recognize(self, face_img):
        try:
            rep = DeepFace.represent(
                img_path=face_img,
                model_name="Facenet",
                enforce_detection=False
            )
            embedding = rep[0]["embedding"]

        except Exception:
            return None, None

        best_match = None
        best_score = float("inf")

        for student_id, ref_embeddings in self.database.items():
            for ref_emb in ref_embeddings:
                dist = cosine(embedding, ref_emb)
                if dist < best_score:
                    best_score = dist
                    best_match = student_id

        if best_score < self.threshold:
            return best_match, round(1 - best_score, 2)

        return None, None
