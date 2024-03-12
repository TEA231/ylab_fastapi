from pydantic import BaseModel

class Base_menu(BaseModel):
    name: str

class Base_submenu(BaseModel):
    name: str

class Base_dish(BaseModel):
    name: str
    price: int

class Put_dish(Base_dish):
    id: int

class Put_menu(Base_menu):
    id: int

class Put_submenu(Base_submenu):
    id: int

class Dish_create(Base_dish):
    submenu_id: int

    class Config:
        orm_mode = True

class Submenu_create(Base_submenu):
    menu_id: int

    class Config: 
        orm_mode = True

class Menu_create(Base_menu):
    submenus: list[Submenu_create] = []

    class Config:
        orm_mode = True
