import os

from sqlalchemy.orm import Session
from src.models.kpi import KPI
from src.core.config import settings
from src.models.pages import Page
from src.repositories.base import BaseRepository


class PageRepository(BaseRepository[Page]):

    def __init__(self, session: Session):
        super().__init__(Page, session)

    async def get_by_name(self, name: str):
        return await self.get_by_field("name", name)

    async def create_page(self, name: str):

        try:
            new_page = Page(name=name)
            self.session.add(new_page)
            await self.session.flush()

            new_kpi = KPI(page_id=new_page.id, url=os.path.join(settings.SITE_URL, new_page.name))

            self.session.add(new_kpi)
            await self.session.commit()

            await self.session.refresh(new_page)
            await self.session.refresh(new_kpi)

            return new_page, new_kpi

        except Exception as e:
            self.session.rollback()
            raise e
