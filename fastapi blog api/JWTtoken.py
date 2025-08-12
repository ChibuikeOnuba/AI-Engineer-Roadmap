from jose import jwt, JWTError
import secrets, schema
from typing import Optional
from datetime import datetime, timedelta

secret_key = secrets.token_hex(32)
algorithm = "HS256"

def create_access_token(data:dict, expires_delta: Optional[timedelta] = None):
    payload = data.copy()

    if expires_delta:
        expire = datetime.utcnow()+expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    payload.update({"exp":expire})

    encoded_jwt = jwt.encode(payload, secret_key, algorithm=algorithm)
    return encoded_jwt


def verify_token(token:str, credentials_exception):
    try:
        payload = jwt.decode(token, secret_key, algorithms= [algorithm])
        email: str = payload.get('sub')
        if email is None:
            raise credentials_exception
        token_data = schema.TokenData(username=email)
    except JWTError:
        raise credentials_exception


