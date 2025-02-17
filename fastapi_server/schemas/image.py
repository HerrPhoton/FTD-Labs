import base64

from pydantic import BaseModel, field_validator

from .base_responses import DataResponse


class Base64Image(BaseModel):
    base64_image: str

    @field_validator("base64_image", mode="before")
    def validate_base64_image(cls, value):

        if not value.startswith(("data:image/jpeg;base64,", "data:image/jpg;base64,", "data:image/png;base64,")):
            raise ValueError("base64_image must start with a valid base64 prefix,"
                             "e.g., 'data:image/jpeg;base64,' or 'data:image/png;base64,'")

        base64_data = value.split(",")[1]

        try:
            base64.b64decode(base64_data, validate=True)
            return value

        except (ValueError, base64.binascii.Error):
            raise ValueError("base64_image must be a valid base64-encoded string")


class ImageResponse(DataResponse[Base64Image]):
    data: Base64Image
