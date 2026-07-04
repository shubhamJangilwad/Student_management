from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session 
from schema.student_schema import StudentCreate, StudentResponse
from database.student_database import get_db
from service.student_service import (create_student ,
                                     show_students,
                                     get_one ,
                                     update_student,
                                     delete_student)

Student_Router = APIRouter()


@Student_Router.post("/create/student", response_model= StudentResponse)
def add_student(student : StudentCreate, db : Session = Depends(get_db)):
    return create_student(db,student)

@Student_Router.get("/show/students")
def get_students(db : Session = Depends(get_db)):
    return show_students(db)

@Student_Router.get("/get/student/{id}")
def get_student(id:int , db : Session = Depends(get_db)):
    return get_one(db,id)

@Student_Router.put("/update/student/{id}", response_model= StudentResponse)
def update_student_id(id : int, student : StudentCreate , db : Session = Depends(get_db)):
    return update_student(db , id, student)

@Student_Router.delete("/delete/student/{id}")
def delete_student_id(id:int , db : Session = Depends(get_db)):
    return delete_student(db, id)