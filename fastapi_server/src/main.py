from importlib import import_module

import uvicorn
from fastapi import FastAPI
from api.routes import __all__ as routes
from src.core.config import settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
)

for route in routes:
    app.include_router(import_module(route).router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("src.main:app", port=8080, reload=True)
