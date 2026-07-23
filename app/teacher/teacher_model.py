from database.student_database import Base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship

class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer , primary_key=True)
    teacher_name = Column(String)

    courses = relationship("Course", back_populates="teacher")