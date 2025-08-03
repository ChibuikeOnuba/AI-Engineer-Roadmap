from database import Base
from sqlalchemy import String, Integer, Column, DateTime
from sqlalchemy.sql import func

class Blog(Base):

    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)

    # To add a timestamp to the database record
    # created_at = Column(DateTime(timezone=True), server_default=func.now())

class User(Base):

    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)


