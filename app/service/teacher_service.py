from app.model.teacher_model import Teacher
from fastapi import HTTPException
from config.logger import logger

def create_teacher_service(body,db):
    try:
        crea_stu = Teacher(
            teacher_name = body.teacher_name
        )
        logger.info("Teacher Creating")
        db.add(crea_stu)
        db.commit()
        db.refresh(crea_stu)
        logger.info("Teacher Created Successfully")
    

        return crea_stu
    except Exception as e:
        logger.error(f"Teacher creation failed: {e}")