from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import connector

class User(connector.Manager.Base):
    __tablename__ = 'Users'
    user_id = Column(Integer, Sequence('user_id'), primary_key=True)
    code = Column(String(10))
    name = Column(String(50))
    last = Column(String(50))
    password = Column(String(20))
