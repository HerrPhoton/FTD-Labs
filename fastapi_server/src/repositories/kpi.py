from sqlalchemy.orm import Session
from src.models.kpi import KPI
from src.repositories.base import BaseRepository


class KPIRepository(BaseRepository[KPI]):

    def __init__(self, session: Session):
        super().__init__(KPI, session)

    async def get_by_page_id(self, page_id: int):
        return await self.get_by_field("page_id", page_id)

    async def update_spent_time(self, page_id: int, time: int):
        kpi = await self.get_by_page_id(page_id)

        if kpi:
            kpi.spent_time += time
            await self.session.commit()
            await self.session.refresh(kpi)

        return kpi
