from fastapi import APIRouter, Depends
from models.core import *
from models.shemas import *
from sqlalchemy.orm import Session
from models.database import get_db

router = APIRouter()

@router.get("/")
async def get_list_menu(db: Session = Depends(get_db)):
    list_menu = db.query(Menu).all()
    
    for num, menu in enumerate(list_menu):
        list_menu[num].q_submenu = len(list_menu[num].submenus)
        list_menu[num].q_dish = sum([len(dsh) for dsh in [sb.dishs for sb in list_menu[num].submenus]])
    
    return list_menu

@router.get("/{id_menu}")
async def get_menu(id_menu, db: Session = Depends(get_db)):
    return db.query(Menu).filter(Menu.id == id_menu).first()

@router.post("/")
async def add_menu(data: Menu_create, db: Session = Depends(get_db)):
    menu = Menu(name=data.name)
    db.add(menu)
    db.commit()
    db.refresh(menu)    
    return menu

@router.put("/")
async def update_menu(data: Put_menu, db: Session = Depends(get_db)):
    menu = db.query(Menu).filter(Menu.id == data.id).first()
    menu.name = data.name
    db.commit()
    db.refresh(menu)
    return menu 

@router.delete("/")
async def delete_menu(data: Put_menu, db: Session = Depends(get_db)):
    menu = db.query(Menu).filter(Menu.id == data.id).first()
    db.delete(menu)
    db.commit()
    return menu
