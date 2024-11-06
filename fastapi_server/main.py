import uvicorn
from fastapi import FastAPI

from .core.db import init_db
from .api.routes import router
from .core.config import settings
from .core.middleware import setup_middleware

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION, servers=[{"url": "http://localhost:8080"}])

app.include_router(router)

setup_middleware()
init_db()

if __name__ == "__main__":
    uvicorn.run("fastapi_server.main:app", port=8080, reload=True)
