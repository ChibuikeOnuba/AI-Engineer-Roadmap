import models, schema, database
from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session

get_db = database.get_db

def create(request:schema.model, db: Session):
    new_blog =  models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def get_all(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs

def get_id(id:int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # _____ old method _____________
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {f'Blog with ID - {id} does not exist'}

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'Blog with ID - {id} does not exist')
    return blog

def delete(id:int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail=f'Blog with id {id} not found in Database')
    
    db.delete(blog)
    db.commit()
    return 'Deleted Successfully'

def update(id:int,request:schema.model, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with ID {id} not found")
    blog.title = request.title
    blog.body = request.body
    db.commit()
    db.refresh(blog)
    return blog
