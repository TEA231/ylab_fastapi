from fastapi import APIRouter, Depends
from models.core import Submenu, Dish
from models.shemas import *
from sqlalchemy.orm import Session
from models.database import get_db

router = APIRouter()

@router.get("/")
async def get_list_submenu(db: Session = Depends(get_db)):
    list_submenu = db.query(Submenu).all()
    for num, submenu in enumerate(list_submenu):
        list_submenu[num].q_dish = len(list_submenu[num].dishs)
    return list_submenu

@router.get("/{id_submenu}")
async def get_submenu(id_submenu, db: Session = Depends(get_db)):
    return db.query(Submenu).filter(Submenu.id == id_submenu).first()

@router.post("/")
async def add_submenu(data: Submenu_create, db: Session = Depends(get_db)):
    submenu = Submenu(name=data.name, menu_id=data.menu_id)
    db.add(submenu)
    db.commit()
    db.refresh(submenu)    
    return submenu

@router.put("/")
async def update_submenu(data: Put_submenu, db: Session = Depends(get_db)):
    submenu = db.query(Submenu).filter(Submenu.id == data.id).first()
    submenu.name = data.name
    db.commit()
    db.refresh(submenu) 
    return submenu 

@router.delete("/")
async def delete_submenu(data: Put_submenu, db: Session = Depends(get_db)):
    submenu = db.query(Submenu).filter(Submenu.id == data.id).first()
    db.delete(submenu)
    db.commit()
    return submenu
