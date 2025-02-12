from fastapi import Depends, Response, APIRouter, status
from sqlalchemy.orm import scoped_session

from ...core.db import get_session
from ...schemas.kpi import KPIBase, KPIResponse, KPIResponseData
from ...schemas.pages import PageBase, PageResponse
from ...schemas.pages import PageWithKPIData, PageResponseData
from ...schemas.pages import PagesKPIResponse
from ...repositories.kpi import KPIRepository
from ...repositories.pages import PageRepository
from ...schemas.base_responses import ErrorResponse

router = APIRouter(prefix="/pages", tags=["pages"])


@router.post("/",
             response_model=None,
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
        page = page_repo.get_by_name(request.name)

        if page:
            response.status_code = status.HTTP_400_BAD_REQUEST

            return ErrorResponse(status="error",
                                 error_code="PAGE_EXISTS",
                                 message=f"Page with name '{request.name}' already exists")

        new_page, _ = page_repo.create_page(request.name)

        return PageResponse(status="success", data=PageResponseData(id=new_page.id, name=new_page.name))

    except Exception as e:
        session.rollback()
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

        return ErrorResponse(status="error", error_code="CREATION_FAILED", message="Failed to create page", details=str(e))


@router.get("/kpi",
            status_code=status.HTTP_200_OK,
            responses={
                status.HTTP_200_OK: {
                    "model": PagesKPIResponse
                },
                status.HTTP_500_INTERNAL_SERVER_ERROR: {
                    "model": ErrorResponse
                }
            })
async def pages_kpi(response: Response, session: scoped_session = Depends(get_session)):

    try:
        pages_repo = PageRepository(session)
        kpi_repo = KPIRepository(session)

        pages = pages_repo.get_all()

        data = []
        for page in pages:
            kpi = kpi_repo.get_by_page_id(page.id)

            if kpi:
                data.append(PageWithKPIData(id=page.id, name=page.name, time=kpi.spent_time, visits=kpi.visits_num))

        return PagesKPIResponse(status="success", data=data)

    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

        return ErrorResponse(status="error", error_code="GET_FAILED", message="Failed to get KPI of all pages", details=str(e))


@router.get("/{page_name}",
            response_model=None,
            status_code=status.HTTP_200_OK,
            responses={
                status.HTTP_200_OK: {
                    "model": PageResponse
                },
                status.HTTP_404_NOT_FOUND: {
                    "model": ErrorResponse
                }
            })
async def get_page(page_name: str, response: Response, session: scoped_session = Depends(get_session)):

    try:
        pages_repo = PageRepository(session)
        page = pages_repo.get_by_name(page_name)

        if not page:
            response.status_code = status.HTTP_404_NOT_FOUND

            return ErrorResponse(status="error", error_code="PAGE_NOT_FOUND", message=f"Page with name {page_name} not found")

        return PageResponse(status="success", data=PageResponseData(id=page.id, name=page.name))

    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

        return ErrorResponse(status="error", error_code="GET_FAILED", message="Failed to get page", details=str(e))


@router.put("/{page_name}/kpi",
            status_code=status.HTTP_200_OK,
            responses={
                status.HTTP_200_OK: {
                    "model": KPIResponse
                },
                status.HTTP_404_NOT_FOUND: {
                    "model": ErrorResponse
                },
                status.HTTP_500_INTERNAL_SERVER_ERROR: {
                    "model": ErrorResponse
                }
            })
async def update_kpi(page_name: str, kpi_request: KPIBase, response: Response, session: scoped_session = Depends(get_session)):

    try:
        kpi_repo = KPIRepository(session)
        kpi = kpi_repo.get_by_page_name(page_name)

        if kpi is None:
            response.status_code = status.HTTP_404_NOT_FOUND

            return ErrorResponse(status="error",
                                 error_code="PAGE_DOES_NOT_EXISTS",
                                 message=f"Page with name {page_name} does not exist")

        kpi = kpi_repo.update_visits_num(kpi.page_id)
        kpi = kpi_repo.update_spent_time(kpi.page_id, kpi_request.time)

        return KPIResponse(status="success", data=KPIResponseData(time=kpi.spent_time, visits=kpi.visits_num))

    except Exception as e:
        session.rollback()
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

        return ErrorResponse(status="error", error_code="UPDATE_FAILED", message="Failed to update time", details=str(e))
