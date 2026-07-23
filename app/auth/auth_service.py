from app.auth.user_model import User
from fastapi import HTTPException
from auth import create_access_token




def create_user(body,db):
    try:
        creating_user = User(
            username = body.username,
            password = body.password
        )

        print("______________",creating_user.username)
        db.add(creating_user)
        db.commit()

        print("_______________",creating_user)
        return {
            "message" : "success"
        }

    except Exception as e:
        print(e)

def check_user(form_data,db):
    user = db.query(User).filter(User.username == form_data.username).first()

    if user is None:
        raise HTTPException(
            status_code= 401,
            detail= "UnAuthorized"
        )
    if user.password == form_data.password:
        token = create_access_token(
             {
                  "username":form_data.username
                  }
                )
        return {
                    "access_token" : token,
                    "token_type" : "bearer"
                }
    else:
        raise HTTPException(
            status_code= 401,
            detail= "Invalid credentials , UnAuthorized"
        )