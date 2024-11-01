from pydantic import BaseModel
from src.schemas.responses import DataResponse


class PageBase(BaseModel):
    name: str


class PageResponse(DataResponse):
    data: dict = {
        "id": int,
        "name": str,
    }
