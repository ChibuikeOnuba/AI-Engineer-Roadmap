from typing import Optional
from pydantic import BaseModel


class model(BaseModel):
    title: str
    body: str
    conclusion: Optional[str] = None