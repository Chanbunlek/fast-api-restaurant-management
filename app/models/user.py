from sqlalchemy import Column, Integer, String
from config.database import Base

class User(Base):
    __tablename__ = 'user'
    id=Column(Integer, primary_key=True)
    username=Column(String(25), default=False, unique=True)
    password=Column(String(25), default=False, unique=True)