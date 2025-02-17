import cv2
from fastapi import Response, APIRouter, status

from ...schemas.image import Base64Image, ImageResponse
from ...utils.convert import image_to_base64, image_from_base64
from ...schemas.base_responses import ErrorResponse

router = APIRouter(prefix="/image", tags=["image"])


@router.post("/invert",
             response_model=None,
             status_code=status.HTTP_200_OK,
             responses={
                 status.HTTP_200_OK: {
                     "model": ImageResponse
                 },
                 status.HTTP_500_INTERNAL_SERVER_ERROR: {
                     "model": ErrorResponse
                 }
             })
async def invert_image(request: Base64Image, response: Response):

    try:
        image = image_from_base64(request.base64_image)
        inverted_image = cv2.bitwise_not(image)
        invert_image_base64 = image_to_base64(inverted_image)

        return ImageResponse(status="success", data=Base64Image(base64_image=invert_image_base64))

    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

        print(e)
        return ErrorResponse(status="error", error_code="PROCESSING_FAILED", message="Failed to invert image", details=str(e))
