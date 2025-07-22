from fastapi import FastAPI, Depends
import schema, models
from database import engine
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)

def blog_db():
    db = 


@app.post('/blog')

def create_blog(request:schema.model, db: Session = Depends(blog_db)):
    return db
