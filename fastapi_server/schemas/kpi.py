from pydantic import Field, BaseModel
from .base_responses import DataResponse


class KPIBase(BaseModel):
    time: int = Field(..., gt=0)


class KPIResponseData(BaseModel):
    time: int = Field(default=0, ge=0)
    visits: int = Field(default=0, ge=0)


class KPIResponse(DataResponse[KPIResponseData]):
    data: KPIResponseData
