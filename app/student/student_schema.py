from pydantic import BaseModel , ConfigDict

class StudentReqCreate(BaseModel):
    name : str
    age : int

class StudentResponse(BaseModel):
    id : int
    name : str
    age : int
    
    model_config = ConfigDict(from_attributes=True)



