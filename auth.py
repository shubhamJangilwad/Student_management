from jose import jwt
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends , HTTPException
from datetime import datetime , timedelta
from jose import JWTError , ExpiredSignatureError 


SECRET_KEY = "mysecretkey"

ALGORITHM = "HS256"

current_time = datetime.utcnow()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def create_access_token(data):
    payload = data.copy()
    expire = current_time + timedelta(minutes= 30)
    payload.update(
        {
            "exp" : expire
        }
    )
    
    token = jwt.encode(
        data,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token

def get_current_user(
    token : str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms = [ALGORITHM]
        )

        return payload

    except ExpiredSignatureError:
        raise HTTPException(
            status_code= 401,
            detail= "Token Expired"
        )

    except JWTError:
        raise HTTPException(
            status_code= 401,
            detail= "Token Invalid"
        )