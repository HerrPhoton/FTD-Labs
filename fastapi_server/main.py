import uvicorn
from fastapi import FastAPI
from .api.routes import router
from .core.config import settings
from .db.base import Base, engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    servers=[{"url": "http://localhost:8080"}]
)

app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run("fastapi_server.main:app", port=8080, reload=True)
