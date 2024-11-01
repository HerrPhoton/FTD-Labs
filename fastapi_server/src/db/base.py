from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm import declarative_base
from src.core.config import settings

engine = create_engine(settings.db_url)
SessionLocal = scoped_session(sessionmaker(engine))
Base = declarative_base()


def get_session():
    session = SessionLocal()

    try:
        yield session

    finally:
        session.close()
