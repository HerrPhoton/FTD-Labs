from sqlalchemy.orm import Session

from .base import BaseRepository
from ..models.kpi import KPI


class KPIRepository(BaseRepository[KPI]):

    def __init__(self, session: Session):
        super().__init__(KPI, session)

    def get_by_page_id(self, page_id: int):
        return self.get_by_field("page_id", page_id)

    def get_by_page_name(self, page_name: str):
        return self.session.query(KPI).join(KPI.page).filter_by(name=page_name).first()

    def update_spent_time(self, page_id: int, time: int):
        kpi = self.get_by_page_id(page_id)

        if kpi:
            kpi.spent_time += time
            self.session.commit()
            self.session.refresh(kpi)

        return kpi

    def update_visits_num(self, page_id: int):
        kpi = self.get_by_page_id(page_id)

        if kpi:
            kpi.visits_num += 1
            self.session.commit()
            self.session.refresh(kpi)

        return kpi
