from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")

def index():
    return {"message": {"text": "Hello, World!"}}


@app.get("/intro")
def intro():
    return "This is a simple FastAPI application that returns a greeting message."

@app.get("/comment/{id}")
def comment(id: int=10, limit: int = 10):
    return {"commnent": {"id": id+limit, "text": "This is a comment."}}

@app.get("/blog")

def blog(limit: int =10, base: int=1, published: bool = False, sort: Optional[int] = None):

    if published:
        return {"blog": {f"This prints {limit+base} {published} number of blogs by default"}}
    else:
        return {"blog": {f"Limit is {limit}"}} 
    

# _____________________________POST REQUESTS_____________________________

class model(BaseModel):
    title: str
    content: str
    published: Optional[bool] = None


@app.post("/blog")

def create_blog(request: model):
    return {"message": f"Blog created successfully with a titke {request.title}!"}