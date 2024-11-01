from sqlalchemy import Text, Column, Integer, BigInteger
from sqlalchemy import ForeignKey
from src.db.base import Base
from sqlalchemy.orm import relationship


class KPI(Base):
    __tablename__ = "kpi"

    page_id = Column(Integer, ForeignKey('pages.id'), primary_key=True)
    url = Column(Text, nullable=False)
    visits_num = Column(BigInteger, default=0, nullable=False)
    spent_time = Column(BigInteger, default=0, nullable=False)

    page = relationship("Page", back_populates="kpi")
