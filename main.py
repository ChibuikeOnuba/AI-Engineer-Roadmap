from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def index():
    return {"message": {"text": "Hello, World!"}}


@app.get("/intro")
def intro():
    return "This is a simple FastAPI application that returns a greeting message."

@app.get("/comment/{id}")
def comment(id: int):
    return {"commnent": {"id": id, "text": "This is a comment."}}

@app.get("/blog")

def blog(limit: int=10, base: int=1):
    return {"blog": {f"This prints {limit+base} number of blogs by default"}}