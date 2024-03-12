from fastapi import FastAPI
from models import core
from models.database import engine
from routers.menu import router as router_menu
from routers.submenu import router as router_submenu
from routers.dish import router as router_dish

app = FastAPI()

app.include_router(
    router=router_menu,
    prefix="/menu",
    tags=["menu"],
)

app.include_router(
    router=router_submenu,
    prefix="/submenu",
    tags=["submenu"],
)

app.include_router(
    router=router_dish,
    prefix="/dish",
    tags=["dish"],  
)