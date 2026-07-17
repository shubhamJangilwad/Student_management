from pydantic import BaseModel , ConfigDict

class CourseReqCreate(BaseModel):
    course_name : str
    student_id : int
    teacher_id : int
   

class CourseResponse(BaseModel):
    id : int
    course_name : str
    student_id : int
    teacher_id : int
    
    model_config = ConfigDict(from_attributes=True)