from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def index():
    return {"message": {"text": "Hello, World!"}}


@app.get("/intro")
def intro():
    return "This is a simple FastAPI application that returns a greeting message."

@app.get("/comment/{id}")
def intro(id: str):
    return id