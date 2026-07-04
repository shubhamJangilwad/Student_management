from pydantic import BaseModel , ConfigDict

class CourseCreate(BaseModel):
    course_name : str
   

class CourseResponse(BaseModel):
    id : int
    course_name : str
    student_id : int
    
    model_config = ConfigDict(from_attributes=True)