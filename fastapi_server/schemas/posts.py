from fastapi_server.schemas.base_responses import DataResponse


class PostsResponse(DataResponse):
    data: dict
