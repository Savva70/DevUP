import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from src.config import settings
from src.routers.armor import router as armor_router
from src.routers.class_ import router as class_router
from src.routers.enchatmens import router as enchatmens_router
from src.routers.enemy import router as enemy_router
from src.routers.item import router as item_router
from src.routers.itemarmor import router as itemarmor_router
from src.routers.itemweapon import router as itemweapon_router
from src.routers.nps import router as nps_router
from src.routers.player import router as player_router
from src.routers.property import router as property_router
from src.routers.usable import router as usable_router
from src.routers.usableitem import router as usableitem_router
from src.routers.weapon import router as weapon_router

BASE_ROUTE_PATH = settings.BASE_ROUTE_PATH


app = FastAPI(
    openapi_url=f"{BASE_ROUTE_PATH}/openapi.json",
    docs_url=f"{BASE_ROUTE_PATH}/docs",
)

router = APIRouter(prefix=BASE_ROUTE_PATH)

router.include_router(router=item_router,prefix='/item', tags=['Item']) 
router.include_router(router= armor_router,prefix='/armor', tags=['armor'])
router.include_router(router= enchatmens_router,prefix='/enchatmens', tags=['enchatmens'])
router.include_router(router=enemy_router,prefix='/enemy', tags=['enemy'])
router.include_router(router=itemarmor_router,prefix='/itemarmor', tags=['itemarmor'])
router.include_router(router=itemweapon_router,prefix='/itemweapon', tags=['itemweapon'])
router.include_router(router=nps_router,prefix='/nps', tags=['nps'])
router.include_router(router=player_router,prefix='/player', tags=['player'])
router.include_router(router=property_router,prefix='/property', tags=['property'])
router.include_router(router=usableitem_router,prefix='/usableitem', tags=['usableitem'])
router.include_router(router=weapon_router,prefix='/weapon', tags=['weapon'])
router.include_router(router=class_router,prefix='/class', tags=['class'])

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='localhost',
        port=8000,
        reload=True,
    )

