from typing import Optional
from pydantic import BaseModel


class model(BaseModel):
    id: int
    title: str
    body: str
    conclusion: Optional[str] = None

# ______________RESPONSE MODEL_____________________
class ShowBlog(BaseModel):
    title: str

    class Config():
        orm_mode = True 

    
class User(BaseModel):
    name: str
    email: str
    password: str