from fastapi import APIRouter, HTTPException , Depends
from app.schema.teacher_schema import TeacherReqSchema , TeacherResponceSchema
from sqlalchemy.orm import Session
from database.student_database import get_db
from app.service.teacher_service import create_teacher_service


teacher_router = APIRouter()

@teacher_router.post("/create/teacher",response_model= TeacherResponceSchema)
def create_teacher(body:TeacherReqSchema , db : Session = Depends(get_db)):
    return create_teacher_service(body,db)