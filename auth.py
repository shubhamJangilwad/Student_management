from jose import jwt
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends


SECRET_KEY = "mysecretkey"

ALGORITHM = "HS256"


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def create_access_token(data):
    token = jwt.encode(
        data,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token

def get_current_user(
    token : str = Depends(oauth2_scheme)):
    payload = jwt.decode(
        token,
        SECRET_KEY,
        algorithms = [ALGORITHM]
    )

    return payload