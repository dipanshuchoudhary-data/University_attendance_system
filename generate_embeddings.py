import os
import numpy as np
from deepface import DeepFace

STUDENTS_DIR = "data/students"
EMBEDDINGS_DIR = "data/embeddings"

os.makedirs(EMBEDDINGS_DIR, exist_ok=True)

print("[INFO] Generating embeddings...")

for student_id in os.listdir(STUDENTS_DIR):
    student_path = os.path.join(STUDENTS_DIR, student_id)
    if not os.path.isdir(student_path):
        continue

    embeddings = []

    for img_name in os.listdir(student_path):
        img_path = os.path.join(student_path, img_name)

        try:
            rep = DeepFace.represent(
                img_path=img_path,
                model_name="Facenet",
                enforce_detection=True
            )
            embeddings.append(rep[0]["embedding"])

        except Exception as e:
            print(f"[WARNING] Skipped {img_path}")

    if embeddings:
        emb_path = os.path.join(EMBEDDINGS_DIR, f"{student_id}.npy")
        np.save(emb_path, np.array(embeddings))
        print(f"[INFO] Saved embeddings for {student_id}")

print("[SUCCESS] Embedding generation completed")
