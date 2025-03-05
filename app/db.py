import os
import dotenv

dotenv.load_dotenv()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_NAME = os.getenv("POSTGRES_USERNAME")
DATABASE_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DATABASE_HOST = os.getenv("POSTGRES_HOSTNAME", "localhost")
DATABASE_URL = f"postgresql://{DATABASE_NAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:5432/postgres"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
