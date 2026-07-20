from fastapi import APIRouter , Depends
from app.schema.auth_schema import LoginRequest
from auth import create_access_token
from fastapi.security import OAuth2PasswordRequestForm


Login_Auth_Router = APIRouter()


@Login_Auth_Router.post("/login")
def login(form_data : OAuth2PasswordRequestForm = Depends()):
    if (form_data.username == "shubham" and form_data.password == "12345"):
        token = create_access_token(
            {
                "username":form_data.username
            }
        )
        return {
            "access_token" : token,
            "token_type" : "bearer"
        }
    return {
        "message" :"invalid username and password"
    }

