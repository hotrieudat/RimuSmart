from fastapi import APIRouter
from api.device import router as device_router

routers = APIRouter(prefix="/api/v1")
router_list = [device_router]

for router in router_list:
    routers.include_router(router)