from fastapi import APIRouter, HTTPException, status, Depends
import models, schema
from sqlalchemy.orm import Session
import database, models
from hashing import Hash
# from passlib.context import CryptContext //a class created for this.


get_db = database.get_db


router = APIRouter()


# ______________ CREATING A NEW USER _______________________

# hasher = CryptContext(schemes=["bcrypt"], deprecated="auto") //a class created for this.

@router.post('/user', response_model=schema.ShowUser, tags =['user'])
def create_user(request:schema.User,db: Session=Depends(get_db)):
    new_user = models.User(name = request.name, email = request.email, password = Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# ______________ GETTING A USER _______________________

@router.get('/user/{id}', response_model=schema.ShowUser, tags =['user'])

def get_user(id:int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with ID - {id} not found')

    return user