from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def index():
    return {"message": {"text": "Hello, World!"}}


@app.get("/intro")
def intro():
    return "This is a simple FastAPI application that returns a greeting message."

@app.get("/comment/{id}")
def comment(id: str):
    return {"commnent": {"id": id, "text": "This is a comment."}}

@app.get("/blog")

def blog(name, base):
    return {"blog": {"title": "My First Blog", "content": "This is the content of my first blog."}}