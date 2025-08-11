from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import schema, database, models, hashing, JWTtoken
from datetime import datetime,timedelta

router = APIRouter(
    tags=['Authentication'],
    prefix='/login'
)

access_token_expiration_mins = 30

@router.post('/')

def login(request:schema.login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='This email does not exist, please sign up')
    
    if not hashing.Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Password Incorrect')
    
    access_token_expires = timedelta(minutes=access_token_expiration_mins)
    access_token = JWTtoken.create_access_token(data={'sub': user.email}, 
                                               expires_delta=access_token_expires)
    
    return {'access_token': access_token, 
            'token_type':'bearer'}