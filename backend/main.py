from fastapi import FastAPI
from database import engine, Base
from models import User, Timetable
from routers import auth, admin, professor, demo

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Univerity Attendance System")

app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(professor.router)
app.include_router(demo.router)
