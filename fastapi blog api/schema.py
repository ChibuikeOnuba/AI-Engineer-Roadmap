from typing import Optional
from pydantic import BaseModel


class model(BaseModel):
    title: str
    body: str
    conclusion: Optional[str] = None

# ______________RESPONSE MODEL_____________________

    
class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str

    class Config():
        orm_mode = True 


class ShowBlog(BaseModel):
    id: int
    title: str
    body: str
    user: Optional[ShowUser]

    class Config():
        orm_mode = True 


class login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None