from sqlalchemy import Text, Column, Integer, BigInteger
from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.orm import Session, relationship, sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.ext.declarative import declarative_base

from ..core.config import DATABASE_URL

engine = create_engine(DATABASE_URL)

Base = declarative_base()
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


def page_by_id(id: int, session: Session):
    return session.query(Page).filter(Page.id == id).first()


class Page(Base):
    __tablename__ = "pages"

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(Text, nullable=False)

    kpi = relationship("KPI", back_populates="page", uselist=False)


class KPI(Base):
    __tablename__ = "kpi"

    page_id = Column(Integer, ForeignKey('pages.id'), primary_key=True)
    url = Column(Text, nullable=False)
    visits_num = Column(BigInteger, default=0, nullable=False)
    spent_time = Column(BigInteger, default=0, nullable=False)

    page = relationship("Page", back_populates="kpi")
