import os

from sqlalchemy.orm import Session
from ..models.kpi import KPI
from ..core.config import settings
from ..models.pages import Page
from .base import BaseRepository


class PageRepository(BaseRepository[Page]):

    def __init__(self, session: Session):
        super().__init__(Page, session)

    def get_by_name(self, name: str):
        return self.get_by_field("name", name)

    def create_page(self, name: str):

        try:
            new_page = Page(name=name)
            self.session.add(new_page)
            self.session.flush()

            new_kpi = KPI(page_id=new_page.id, url=os.path.join(settings.SITE_URL, new_page.name))

            self.session.add(new_kpi)
            self.session.commit()

            self.session.refresh(new_page)
            self.session.refresh(new_kpi)

            return new_page, new_kpi

        except Exception as e:
            self.session.rollback()
            raise e
