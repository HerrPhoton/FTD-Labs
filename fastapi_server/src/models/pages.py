from sqlalchemy import Text, Column, Integer
from src.db.base import Base
from sqlalchemy.orm import relationship


class Page(Base):
    __tablename__ = "pages"

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(Text, nullable=False)

    kpi = relationship("KPI", back_populates="page", uselist=False)
