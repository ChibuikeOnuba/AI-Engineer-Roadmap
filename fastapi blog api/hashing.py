from passlib.context import CryptContext


hasher = CryptContext(schemes=["bcrypt"], deprecated="auto")
class Hash():
    def bcrypt(password):
        hashed_password = hasher.hash(password)
        return hashed_password
    
    def verify(plain_password, hashed_password):
        

        return hasher.verify(plain_password, hashed_password)