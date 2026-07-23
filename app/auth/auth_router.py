from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session
from app.auth.auth_schema import LoginRequest
from auth import create_access_token
from app.auth.auth_service import create_user , check_user
from fastapi.security import OAuth2PasswordRequestForm
from database.student_database import get_db


Login_Auth_Router = APIRouter()


@Login_Auth_Router.post("/login")
def login(form_data : OAuth2PasswordRequestForm = Depends(),db : Session = Depends (get_db)):
    return check_user(form_data,db)
    # if (form_data.username == "shubham" 
    #     and 
    #     form_data.password == "12345"):
    #     token = create_access_token(
    #         {
    #             "username":form_data.username
    #         }
    #     )
    #     return {
    #         "access_token" : token,
    #         "token_type" : "bearer"
    #     }
    # return {
    #     "message" :"invalid username and password"
    # }


@Login_Auth_Router.post("/reg/user")
def register_user(body : LoginRequest , db : Session = Depends(get_db)):
    return create_user(body , db)
