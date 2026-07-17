from fastapi import APIRouter , Depends
from app.service.course_service import (create_course ,
                                    show_courses,
                                    get_one,
                                    update_course,
                                    delete_course) 
from database.student_database import get_db
from app.schema.course_schema import CourseReqCreate , CourseResponse
from sqlalchemy.orm import Session

Course_Router = APIRouter()


@Course_Router.post("/create/course" , response_model=CourseResponse)
def add_course(body : CourseReqCreate, db : Session = Depends(get_db)):
    return create_course(db,body)

@Course_Router.get("/show/courses")
def get_course(db : Session = Depends(get_db)):
    return show_courses(db)

@Course_Router.get("/get/course/{id}")
def get_course(id:int , db : Session = Depends(get_db)):
    return get_one(db,id)

@Course_Router.put("/update/course/{id}", response_model= CourseResponse)
def update_course_id(id : int, body : CourseReqCreate , db : Session = Depends(get_db)):
    return update_course(db , id, body)

@Course_Router.delete("/delete/course/{id}")
def delete_course_id(id:int , db : Session = Depends(get_db)):
    return delete_course(db, id)