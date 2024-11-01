from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .utils.db import Base, engine


def create_app():
    app = FastAPI(debug=True)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    return app
