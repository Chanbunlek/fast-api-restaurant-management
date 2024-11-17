from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATA_BASE_URL = "postgresql://postgres:admin@localhost:8080/rsdb"

engine = create_engine(DATA_BASE_URL)
Base = declarative_base()
Session = sessionmaker(autoflush=False, autocommit=False, bind=engine)
