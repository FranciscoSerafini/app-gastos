from datetime import datetime, timedelta
from jose import JWTError, jwt

SECRET_KEY = "SECRET_KEY"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data:dict, expires_delta: timedelta = None):
    encode = data.copy()
    if expires_delta:
        expire = datetime.time() + expires_delta
    else:
        expire = datetime.timezoneaware() + timedelta(minutes=15)
    encode.update({"exp":expire})
    encode_jwt = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt

 