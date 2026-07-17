from app.model.teacher_model import Teacher
from fastapi import HTTPException

def create_teacher_service(body,db):
    crea_stu = Teacher(
        teacher_name = body.teacher_name
    )

    db.add(crea_stu)
    db.commit()
    db.refresh(crea_stu)
   

    return crea_stu