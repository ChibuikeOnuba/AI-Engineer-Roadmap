from fastapi import FastAPI
from typing import Optional
import schema

app = FastAPI()

@app.get("/")

def index():
    return {"message": {"text": "Hello, World!"}}


@app.get("/intro")
def intro():
    return "This is a simple FastAPI application that returns a greeting message."

@app.get("/comment/{id}")
def comment(id: Optional[int], limit: int = 10):
    return {"commnent": {"id": id+limit, "text": "This is a comment."}}

@app.get("/blog")

def blog(limit: int =10, base: int=1, published: bool = False, sort: Optional[int] = None):

    if published:
        return {"blog": {f"This prints {limit+base} {published} number of blogs by default"}}
    else:
        return {"blog": {f"Limit is {limit}"}} 
    

# _____________________________POST REQUESTS_____________________________


# @app.post("/create")

# def create(title: str, body: Optional[str] = None):
#     return {'title': title, 'body': body}

# _________ The method above is outdated and improved using the Pydantic BaseModel (which creates a blueprint for the function)____________


@app.post("/create")

def create_blog(request: schema.model):
    return {request.title}