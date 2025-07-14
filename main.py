from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return 'Welcome to my first FastAPI app!'