from app.model.student_model import Student
from app.model.course_model import Course
from fastapi import HTTPException

def create_student(db,body):

    db_student = Student(
        name = body.name,
        age = body.age
    )

    db.add(db_student)
    db.commit()

    return db_student

def show_students(db):
    shows_students = db.query(Student).all()
    return shows_students

def get_one(db,id):
    get_one_student = db.query(Student).filter(Student.id == id).first()
    return get_one_student

def update_student(db,id,body):
    update_student_by_id = db.query(Student).filter(Student.id == id).first()
    print("_____________________",update_student_by_id)
    update_student_by_id.name = body.name,
    update_student_by_id.age = body.age

    db.commit()
    return update_student_by_id

def delete_student(db,id):
    delete_stu_by_id = db.query(Student).filter(Student.id == id).first()

    if delete_stu_by_id is None:
        raise HTTPException(
            status_code= 404,
            detail= "Student not found"

        )
    db.delete(delete_stu_by_id)
    db.commit()
    return {
        "message" : "student deleted successfully"
    }

def get_stu_details_service(id,db):
    query = (
        db.query(
            Student.name,
            Course.course_name

        ).join(
            Course,
            Student.id == Course.student_id
        ).filter(Student.id == id)

    )

    result = query.all()

    print("________________________",result)
    responce = []

    for row in result:
        responce.append({
            "student_name":row.name,
            "course_name" : row.course_name
        })
    return responce
    