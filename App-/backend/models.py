from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

dataBase = declarative_base()

#class user
class User(dataBase):
    __tablename__ = "Usuarios"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    
    expenses = relationship("Expense", back_populates="Owner") #gastos asociados a cada usuario
    
class Expense(dataBase):
    __tablename__ = "Gastos"
    id = Column(Integer, primary_key=True,index=True)
    amount = Column(Float)
    description = Column(String)
    date = Column(DateTime)
    user_id = Column(Integer, ForeignKey("Usuarios.id"))
    
    owner = relationship("Usuarios", back_populates="Gastos")