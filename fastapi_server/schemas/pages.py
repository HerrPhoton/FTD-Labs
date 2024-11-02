from pydantic import BaseModel
from .base_responses import DataResponse


class PageBase(BaseModel):
    name: str


class PageResponseData(BaseModel):
    id: int | None = None
    name: str = ""


class PageResponse(DataResponse[PageResponseData]):
    data: PageResponseData


class PageWithKPIData(BaseModel):
    id: int | None = None
    name: str = ""
    time: int = 0
    visits: int = 0


class PagesKPIResponse(DataResponse[PageWithKPIData]):
    data: list[PageWithKPIData]
