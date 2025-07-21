from database import Base
from sqlalchemy import String, integer, Column

class Blog(Base):
    id = Column(integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)


