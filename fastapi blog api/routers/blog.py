from fastapi import APIRouter, HTTPException, status, Depends
import models, schema
from sqlalchemy.orm import Session
import database, models



router = APIRouter()

# _________________ POSTING TO THE DATABASE _________________________

@router.post('/blog', status_code = status.HTTP_201_CREATED, tags =['blog'])

def create_blog(request:schema.model, db: Session = Depends(database.get_db)):
    new_blog =  models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog