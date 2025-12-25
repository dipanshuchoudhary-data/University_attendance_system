from fastapi import APIRouter,Depends
from models import Timetable
from database import SessionLocal
from deps import admin_required

router = APIRouter(prefix="/admin",tags=["admin"])

@router.post("/timetable")
def add_class(data:dict,user=Depends(admin_required)):
    db = SessionLocal()
    entry = Timetable(**data)
    db.add(entry)
    db.commit()

    return {"status":"Class added"}

@router.put("/timetable/{class_id}")
def edit_class(class_id:int,data:dict,user=Depends(admin_required)):
    db = SessionLocal()
    entry = db.query(Timetable).get(class_id)
    for key,value in data.items():
        setattr(entry,key,value)
    db.commit()
    return {"status":"Class updated"}

@router.get("/timetable")

def view_timetable(user=Depends(admin_required)):
    db = SessionLocal()
    return db.query(Timetable).all()