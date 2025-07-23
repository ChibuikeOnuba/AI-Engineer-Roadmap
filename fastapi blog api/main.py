from fastapi import FastAPI, Depends
import schema, models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# _________________ POSTING TO THE DATABASE _________________________

@app.post('/blog')

def create_blog(request:schema.model, db: Session = Depends(get_db)):
    new_blog =  models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog



# _________________ READING FROM THE DATABASE _________________________

@app.get('/blog')

def get_blog(db: Session = Depends(get_db)):
    db.get()
    return db
    
