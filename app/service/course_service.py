from app.model.course_model import Course
from app.model.student_model import Student
from app.model.teacher_model import Teacher
from fastapi import HTTPException

def create_course(db,body):


    # creating_course = db.query(Student
    #                            ,Teacher).filter(Student.id == body.student_id,
    #                                             Teacher.id == body.teacher_id).first()

    # if creating_course is None :
    #      raise HTTPException(
    #          status_code= 404,
    #          detail= "Student Not found"
    #      )
      
    # else:
    db_course = Course(
    course_name = body.course_name,
    student_id = body.student_id,
    teacher_id = body.teacher_id

    )
    db.add(db_course)
    db.commit()

    return db_course

def show_courses(db):
    shows_courses = db.query(Course).all()
    return shows_courses

def get_one(db,id):
    get_one_course = db.query(Course).filter(Course.id == id).first()
    return get_one_course

def update_course(db,id,body):
    update_course_db = db.query(Course).filter(Course.id == id).first()
    print("_____________________",update_course_db)
    update_course_db.course_name = body.course_name

    db.commit()
    return update_course_db

def delete_course(db,id):
    course_d = db.query(Course).filter(Course.id == id).first()

    if course_d is None:
        raise HTTPException(
            status_code= 404,
            detail= "course not found"

        )
    db.delete(course_d)
    db.commit()
    return {
        "message" : "Course deleted successfully"
    }