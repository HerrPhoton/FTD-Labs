from src.schemas.responses import DataResponse


class PostsResponse(DataResponse):
    data: dict = {"posts": list[dict]}
