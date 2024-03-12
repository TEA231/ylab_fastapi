from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql://postgres:qwerty@localhost/postgres"

engine = create_engine(DATABASE_URL)
sessionlocal = sessionmaker(autocommit=False, bind=engine)
Base = declarative_base()

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:    
        db.close()
