from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import schema, database, models

router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')

def login(request:schema.login, db: Session = Depends(database.get_db)):
    log_req = db.query(models.User).filter(models.User.email == request.username).first()
    if not log_req:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='This email does not exist, please sign up')
    
    return {'status':f'Welcome back {log_req.name}',
            'details':log_req}