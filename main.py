from fastapi import FastAPI
from database.student_database import Base , engine
from app.router.student_router import Student_Router
from app.router.course_router import Course_Router

app = FastAPI()



Base.metadata.create_all(bind=engine)


app.include_router(Student_Router)
app.include_router(Course_Router)