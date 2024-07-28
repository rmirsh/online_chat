from fastapi import (
    APIRouter,
    Depends,
)

from core.config import settings


router = APIRouter(
    prefix=settings.api.v1.prefix,
    # dependencies=[Depends(http_bearer)],
)