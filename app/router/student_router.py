from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session 
from app.schema.student_schema import StudentReqCreate, StudentResponse
from database.student_database import get_db
from app.service.student_service import (create_student ,
                                     show_students,
                                     get_one ,
                                     update_student,
                                     delete_student)

Student_Router = APIRouter()


@Student_Router.post("/create/student", response_model= StudentResponse)
def add_student(body : StudentReqCreate, db : Session = Depends(get_db)):
    return create_student(db,body)

@Student_Router.get("/show/students")
def get_students(db : Session = Depends(get_db)):
    return show_students(db)

@Student_Router.get("/get/student/{id}")
def get_student(id:int , db : Session = Depends(get_db)):
    return get_one(db,id)

@Student_Router.put("/update/student/{id}", response_model= StudentResponse)
def update_student_id(id : int, body : StudentReqCreate , db : Session = Depends(get_db)):
    return update_student(db , id, body)

@Student_Router.delete("/delete/student/{id}")
def delete_student_id(id:int , db : Session = Depends(get_db)):
    return delete_student(db, id)