from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Menu(Base):
    __tablename__ = "menu"

    id=Column(Integer, primary_key=True)
    name=Column(String, nullable=False)
    
    submenus = relationship("Submenu", back_populates="menu_o")

class Submenu(Base):
    __tablename__ = "submenu"

    id=Column(Integer, primary_key=True)
    name=Column(String, nullable=False)
    menu_id=Column(Integer, ForeignKey("menu.id"))

    menu_o = relationship("Menu", back_populates="submenus")
    
    dishs = relationship("Dish", back_populates="submenu_o")

class Dish(Base):
    __tablename__ = "dish"

    id=Column(Integer, primary_key=True)
    name=Column(String, nullable=False)
    price=Column(Integer)
    submenu_id=Column(Integer, ForeignKey("submenu.id"))

    submenu_o = relationship("Submenu", back_populates="dishs")
