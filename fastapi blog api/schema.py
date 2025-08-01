from typing import Optional
from pydantic import BaseModel


class model(BaseModel):
    id: int
    title: str
    body: str
    conclusion: Optional[str] = None

# ______________RESPONSE MODEL_____________________
class ShowBlog(model):
    title: str

    class Config():
        orm_mode = True