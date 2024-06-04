from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class ExpenseBase(BaseModel):
    amount: float
    description: str
    date: datetime
    
class ExpenseCreate(ExpenseBase):
    pass

class Expense(BaseModel):
    id: int
    user_id: int
    
    class Config: 
        orm_mode = True #habilita el modo orm para trabajar con base de datos (compatibilidad)
        
class UserBase(BaseModel):
    username: str
    email: str
    
class UserCreate(UserBase):
    password: str
    
class User(UserBase):
    id: int
    expense: List[Expense] = []
    
    class Config:
        orm_mode = True

from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        orm_mode = True
