from fastapi import Depends, Response, APIRouter, status
from src.db.base import get_session
from sqlalchemy.orm import scoped_session
from src.schemas.kpi import TimeSpentRequest
from src.models.pages import Page
from src.schemas.pages import PageBase, PageResponse
from src.schemas.responses import ErrorResponse
from src.repositories.pages import PageRepository

router = APIRouter(prefix="/pages", tags=["pages"])


@router.post("/",
             response_model=PageResponse,
             status_code=status.HTTP_201_CREATED,
             responses={
                 status.HTTP_201_CREATED: {
                     "model": PageResponse
                 },
                 status.HTTP_400_BAD_REQUEST: {
                     "model": ErrorResponse
                 },
                 status.HTTP_500_INTERNAL_SERVER_ERROR: {
                     "model": ErrorResponse
                 }
             })
async def create_page(request: PageBase, response: Response, session: scoped_session = Depends(get_session)):

    try:
        page_repo = PageRepository(session)

        if await page_repo.get_by_name(request.name):
            response.status_code = status.HTTP_400_BAD_REQUEST

            return ErrorResponse(status="error",
                                 error_code="PAGE_EXISTS",
                                 message=f"Page with name '{request.name}' already exists")

        new_page, _ = await page_repo.create_page(request.name)

        return PageResponse(status="success", data={"id": new_page.id, "name": new_page.name})

    except Exception as e:
        session.rollback()
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

        return ErrorResponse(status="error", error_code="CREATION_FAILED", message="Failed to create page", details=str(e))


@router.get("/{page_id}",
            response_model=PageResponse,
            status_code=status.HTTP_200_OK,
            responses={
                status.HTTP_200_OK: {
                    "model": PageResponse
                },
                status.HTTP_404_NOT_FOUND: {
                    "model": ErrorResponse
                }
            })
async def get_page(page_id: int, response: Response, session: scoped_session = Depends(get_session)):

    page = session.query(Page).filter(Page.id == page_id).first()

    if not page:
        response.status_code = status.HTTP_404_NOT_FOUND

        return ErrorResponse(status="error", error_code="PAGE_NOT_FOUND", message=f"Page with id {page_id} not found")

    return PageResponse(status="success", data={
        "id": page.id,
        "name": page.name,
    })


@router.post(
    "/{page_id}/update_time",
)
async def set_spent_time(page_id: int,
                         time_spent_request: TimeSpentRequest,
                         response: Response,
                         session: scoped_session = Depends(get_session)):
    pass


@router.get("/kpi")
async def pages_kpi(page_id: int, response: Response, session: scoped_session = Depends(get_session)):
    pass
