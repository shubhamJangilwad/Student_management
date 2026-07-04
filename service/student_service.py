from model.student_model import Student
from fastapi import HTTPException

def create_student(db,student_data):

    db_student = Student(
        name = student_data.name,
        age = student_data.age
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

def update_student(db,id,student):
    update_student_by_id = db.query(Student).filter(Student.id == id).first()
    print("_____________________",update_student_by_id)
    update_student_by_id.name = student.name,
    update_student_by_id.age = student.age

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