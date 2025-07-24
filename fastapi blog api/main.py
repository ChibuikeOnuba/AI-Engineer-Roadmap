from fastapi import FastAPI, Depends
import schema, models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)

@app.get('/')

def demo_page():
    return {'This is a demo page, got to http://127.0.0.1:8000/docs to use the interact with the FastAPI'}

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

# query all blogs

@app.get('/blog')

def get_blog(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs
    

# query blogs from ID

@app.get('/blog/{id}')

def get_single_blog(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    return blog
