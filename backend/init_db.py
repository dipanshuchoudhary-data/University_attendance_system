from database import engine, Base
from models import User, Timetable

print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Done.")
