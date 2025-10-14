import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
from src.config import settings

from src.routers.animal import router as animal_router


BASE_ROUTE_PATH = settings.BASE_ROUTE_PATH


app = FastAPI(
    openapi_url=f"{BASE_ROUTE_PATH}/openapi.json",
    docs_url=f"{BASE_ROUTE_PATH}/docs",
)

router = APIRouter(prefix=BASE_ROUTE_PATH)

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='localhost',
        port=8000,
        reload=True,
    )
    
router.include_router(animal_router, tags=['animal'])

app.include_router(router)