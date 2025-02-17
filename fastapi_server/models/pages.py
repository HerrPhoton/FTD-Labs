from sqlalchemy import Text, Column, Integer
from sqlalchemy.orm import relationship

from ..core.db import Base


class Page(Base):
    __tablename__ = "pages"

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(Text, nullable=False, unique=True)

    kpi = relationship("KPI", back_populates="page", uselist=False)
