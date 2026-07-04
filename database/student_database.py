from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base 

DATABASE_URL = "postgresql://postgres:12345@localhost:5432/student_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit= False, 
    autoflush= False, #prepare data for send to the database 
    bind=engine) # session connection to the postgresql

def get_db(): # session creation
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()


Base = declarative_base()