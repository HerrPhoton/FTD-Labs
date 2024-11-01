import requests
from fastapi import Response, APIRouter, status
from src.core.config import settings
from src.schemas.posts import PostsResponse
from src.schemas.responses import ErrorResponse

router = APIRouter(prefix="/posts", tags=["posts"])


@router.get("/",
            response_model=PostsResponse,
            status_code=status.HTTP_200_OK,
            responses={
                status.HTTP_200_OK: {
                    "model": PostsResponse
                },
                status.HTTP_500_INTERNAL_SERVER_ERROR: {
                    "model": ErrorResponse
                }
            })
async def posts(response: Response):

    try:
        response = requests.get(settings.POSTS_URL)
        response.raise_for_status()
        posts = response.json()

        return PostsResponse(status="success", data={"posts": posts})

    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

        return ErrorResponse(status="error", message="Error fetching posts", details=str(e))
