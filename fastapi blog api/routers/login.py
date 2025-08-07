from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import schema, database, models, hashing

router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')

def login(request:schema.login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='This email does not exist, please sign up')
    
    if not hashing.Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Password Incorrect')
    
    return {'status':f'Welcome back {user.name}'}