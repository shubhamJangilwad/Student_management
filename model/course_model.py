from sqlalchemy import Column   , Integer , String , ForeignKey
from sqlalchemy.orm import relationship
from database.student_database import Base 


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    course_name = Column(String)
    student_id = Column(Integer, ForeignKey("students.id")
)
    

    student = relationship("Student", back_populates="courses")