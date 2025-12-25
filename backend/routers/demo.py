from fastapi import APIRouter

router = APIRouter(prefix="/demo", tags=["Demo"])

@router.post("/upload-face")
def upload_face():
    return {"status": "Face uploaded (demo only)"}
