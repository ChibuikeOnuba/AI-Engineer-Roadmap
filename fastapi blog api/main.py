
from fastapi import FastAPI
import models
from database import engine
from routers import blog, user



app = FastAPI()

# calling the database engine into the application
models.Base.metadata.create_all(engine)


@app.get('/')

def demo_page():
    return {'This is a demo page, got to http://127.0.0.1:8000/docs to use the interact with the FastAPI'}


# __________ ROUTER FUNCTION ____________________-
app.include_router(blog.router)
app.include_router(user.router)
