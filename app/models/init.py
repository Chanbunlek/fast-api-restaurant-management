from config.database import Base, engine
from models.user import User 

def init():
    Base.metadata.create_all(bind=engine)