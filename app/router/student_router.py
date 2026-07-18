from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session 
from app.schema.student_schema import StudentReqCreate, StudentResponse
from database.student_database import get_db
from app.service.student_service import (create_student ,
                                     show_students,
                                     get_one ,
                                     update_student,
                                     delete_student,
                                     get_stu_details_service,
                                     get_all_stu_service,
                                     get_stu_tea_cour_service,
                                     get_stu_cour_service,
                                     get_stu_del_exl_service)
from app.exports.excel import stu_cou_tech_excel_service
from app.exports.pdf import stu_cou_tech_pdf_service

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

@Student_Router.get("/get/stu/det/{id}")
def get_stu_details(id:int,db : Session = Depends(get_db)):
    return get_stu_details_service(id,db)

@Student_Router.get("/get/all/stu")
def get_all_stu(db: Session = Depends(get_db)):
    return get_all_stu_service(db)

@Student_Router.get("/get/stu/tea/cour")
def get_stu_tea_cour(db:Session = Depends(get_db)):
    return get_stu_tea_cour_service(db)

@Student_Router.get("/get/stu/cour{id}")
def get_stu_cour(id:int,db:Session = Depends(get_db)):
    print("Router called")
    return get_stu_cour_service(id,db)

@Student_Router.get("/stu/del/exl")
def get_stu_del_exl(db:Session = Depends(get_db)):
    return get_stu_del_exl_service(db)

@Student_Router.get("/get/stu/cou/tech/excel")
def get_stu_cou_tech_excel(db:Session = Depends(get_db)):
    return stu_cou_tech_excel_service(db)

@Student_Router.get("/get/stu/cou/tech/pdf")
def get_stu_cou_tech_pdf(db:Session = Depends(get_db)):
    return stu_cou_tech_pdf_service(db)
