from fastapi import APIRouter,Depends
from deps import professor_required

router = APIRouter(prefix="/professor",tags=["Professor"])

@router.post("/start-class")
def start_class(user=Depends(professor_required)):
    return {"status":"Class started"}

@router.post("/end-class")
def end_class(user=Depends(professor_required)):
    return {"status":"Class ended"}