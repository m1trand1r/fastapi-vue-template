from fastapi import (
    FastAPI,
)
from fastapi.middleware.cors import CORSMiddleware
from app.api.api_v1.api import api_router

import uvicorn

from app.core.config import settings


app = FastAPI(openapi_url=f"{settings.API_V1_STR}/openapi.json")
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router, prefix=settings.API_V1_STR)

# if __name__ == '__main__':
#     uvicorn.run(app=app, log_level='info')