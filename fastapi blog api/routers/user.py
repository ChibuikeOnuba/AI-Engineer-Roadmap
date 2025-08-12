from fastapi import APIRouter, HTTPException, status, Depends
import models, schema
from sqlalchemy.orm import Session
import database, models
from hashing import Hash
from repo import user
# from passlib.context import CryptContext //a class created for this.


get_db = database.get_db


router = APIRouter(
    prefix='/user',
    tags=['Users']
)


# ______________ CREATING A NEW USER _______________________

# hasher = CryptContext(schemes=["bcrypt"], deprecated="auto") //a class created for this.

@router.post('/', response_model=schema.ShowUser)
def create_user(request:schema.User,db: Session=Depends(get_db)):
    return user.create(request, db)


# ______________ GETTING A USER _______________________

@router.get('/{id}', response_model=schema.ShowUser)

def get_user(id:int, db: Session = Depends(get_db)):
    return user.get(id, db)

# ______________ DELETING A USER _______________________

@router.delete('/{id}')

def remove_user(id:str, db:Session=Depends(get_db)):
    return user.remove_user(id, db)