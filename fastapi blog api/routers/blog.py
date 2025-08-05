from fastapi import APIRouter, HTTPException, status, Depends
import models, schema
from sqlalchemy.orm import Session
import database, models
from typing import List


get_db = database.get_db



router = APIRouter()

# _________________ POSTING TO THE DATABASE _________________________

@router.post('/blog', status_code = status.HTTP_201_CREATED, tags =['blog'])

def create_blog(request:schema.model, db: Session = Depends(get_db)):
    new_blog =  models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog



# _________________ READING FROM THE DATABASE _________________________

# query all blogs

@router.get('/blog', response_model=List[schema.ShowBlog], tags =['blog'])

def get_blog(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs
    

# query blogs with ID

@router.get('/returnBlog/{id}', response_model=schema.ShowBlog, tags =['blog'])

def get_sinlge_blog(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # _____ old method _____________
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {f'Blog with ID - {id} does not exist'}

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'Blog with ID - {id} does not exist')

    return blog



# _________________ DELETING FROM THE DATABASE _________________________

@router.delete('/blog/{id}', tags =['blog'])

def delete(id, db: Session = Depends(get_db)):

    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail=f'Blog with id {id} not found in Database')
    
    db.delete(blog)
    db.commit()
    return 'Done'


# ______________ UPDATING A RECORD ON THE DATABASE _______________________

@router.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags =['blog'])

def update(id, request:schema.model, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with ID {id} not found")
    blog.title = request.title
    blog.body = request.body
    db.commit()
    db.refresh(blog)
    return 'Done'
