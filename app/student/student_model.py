from sqlalchemy import Column , Integer , String , ForeignKey 
from sqlalchemy.orm import relationship
from database.student_database import Base

class Student(Base):

    __tablename__ = "students"

    id = Column(Integer , primary_key=True)
    name = Column(String)
    age = Column(Integer)
    
    courses = relationship("Course", back_populates="student")


