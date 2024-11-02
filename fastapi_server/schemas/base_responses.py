from typing import Generic, TypeVar

from pydantic import BaseModel

T = TypeVar('T')


class ResponseBase(BaseModel):
    status: str
    message: str | None = None


class DataResponse(ResponseBase, Generic[T]):
    data: T


class ErrorResponse(ResponseBase):
    error_code: str
    details: str | None = None
