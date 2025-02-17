from fastapi import APIRouter

from . import image, pages, posts

router = APIRouter()

router.include_router(pages.router)
router.include_router(posts.router)
router.include_router(image.router)
