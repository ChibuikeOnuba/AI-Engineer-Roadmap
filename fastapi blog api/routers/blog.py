from fastapi import APIRouter, HTTPException, status, Depends
import models, schema, Oauth
from sqlalchemy.orm import Session
import database, models
from typing import List
from repo import blog


get_db = database.get_db



router = APIRouter(
    tags=['Blogs'],
    prefix='/blog'
)

# ____________________________ POSTING TO THE DATABASE ____________________________________

@router.post('/', status_code = status.HTTP_201_CREATED, response_model=schema.ShowBlog)

def create_blog(request:schema.model, db: Session = Depends(get_db), current_user: schema.User=Depends(Oauth.get_current_user)):
    return blog.create(request,db)



# _____________________________ READING FROM THE DATABASE _____________________________________

# query all blogs
@router.get('/', response_model=List[schema.ShowBlog])

def get_blog(db: Session = Depends(get_db), current_user: schema.User=Depends(Oauth.get_current_user)):
    return blog.get_all(db)
    

# query blogs with ID
@router.get('/returnBlog/{id}', response_model=schema.ShowBlog)

def get_sinlge_blog(id, db: Session = Depends(get_db), current_user: schema.User=Depends(Oauth.get_current_user)):
    return blog.get_id(id, db)



# ____________________________ DELETING FROM THE DATABASE ____________________________________

@router.delete('/{id}')

def delete(id, db: Session = Depends(get_db), current_user: schema.User=Depends(Oauth.get_current_user)):
    return blog.delete(id, db)


# _________________________ UPDATING A RECORD ON THE DATABASE __________________________________

@router.put('/{id}', status_code=status.HTTP_200_OK)

def update(id, request:schema.model, db: Session = Depends(get_db), current_user: schema.User=Depends(Oauth.get_current_user)):
    return blog.update(id,request, db)
