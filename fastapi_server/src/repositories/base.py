from typing import Any, Generic, TypeVar

from src.db.base import Base
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):

    def __init__(self, model: type[ModelType], session: Session):
        self.model = model
        self.session = session

    async def get_by_id(self, id: int):
        return self.session.query(self.model).filter(self.model.id == id).first()

    async def get_by_field(self, field: str, value: Any):
        return self.session.query(self.model).filter(getattr(self.model, field) == value).first()

    async def create(self, obj_in: ModelType):
        self.session.add(obj_in)
        await self.session.commit()
        await self.session.refresh(obj_in)
        return obj_in
