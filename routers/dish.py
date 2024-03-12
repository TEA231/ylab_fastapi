from fastapi import APIRouter, Depends
from models.core import Dish
from models.shemas import *
from sqlalchemy.orm import Session
from models.database import get_db

router = APIRouter()

@router.get("/")
async def get_list_dish(db: Session = Depends(get_db)):
    return db.query(Dish).all()

@router.get("/{id_dish}")
async def get_dish(id_dish, db: Session = Depends(get_db)):
    return db.query(Dish).filter(Dish.id == id_dish).first()

@router.post("/")
async def add_dish(data: Dish_create, db: Session = Depends(get_db)):
    dish = Dish(name=data.name, price= data.price, submenu_id=data.submenu_id)
    db.add(dish) 
    db.commit()
    db.refresh(dish)    
    return dish

@router.put("/")
async def update_dish(data: Put_dish, db: Session = Depends(get_db)):
    dish = db.query(Dish).filter(Dish.id == data.id).first()
    dish.name = data.name
    dish.price = data.price
    db.commit()
    db.refresh(dish) 
    return dish

@router.delete("/")
async def delete_dish(data: Put_submenu, db: Session = Depends(get_db)):
    dish = db.query(Dish).filter(Dish.id == data.id).first()
    db.delete(dish)
    db.commit()
    return dish
