from pydantic import Field, BaseModel


class TimeSpentRequest(BaseModel):
    time: int = Field(..., gt=0)
