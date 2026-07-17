from pydantic import BaseModel , ConfigDict

class TeacherReqSchema(BaseModel):
    teacher_name : str


class TeacherResponceSchema(BaseModel):
    id : int
    teacher_name : str


    model_config = ConfigDict(from_attributes=True)