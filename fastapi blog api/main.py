from fastapi import FastAPI, Depends, Response, status, HTTPException
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

@app.post('/blog', status_code = status.HTTP_201_CREATED)

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

@app.get('/returnBlog')

def get_sinlge_blog(id, response:Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # _____ old method _____________
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {f'Blog with ID - {id} does not exist'}

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'Blog with ID - {id} does not exist')

    return blog



# _________________ DELETING FROM THE DATABASE _________________________

@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)

def delete(id, db: Session = Depends(get_db)):

    db.query(models.Blog).filter(models.Blog.id == 
                                 id).delete(synchronize_session=False)
    db.commit()
    
    return 'Done'