from jose import jwt
import secrets
from typing import Optional
from datetime import datetime, timedelta

secret_key = secrets.token_hex(32)
algorithm = "HS256"
access_token_expiration_mins = 30

def create_access_token(data:dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow()+expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp":expire})

    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)

if __name__ == "__main__":
    print(secret_key)



