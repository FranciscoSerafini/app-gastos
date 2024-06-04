from sqlalchemy.orm import Session
import models, schemas
from passlib.context import CryptContext

#proceso de hashing -> toma la contraseña en texto plano y devuelve una contraseña encriptada
pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

#toma contraseña en texto plano y devuelve el hash
def get_password_hash(password):
    return pwd_context.hash(password)

#verificacion de contraseña
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

#creacion de un usuario
def create_user(db:Session, user: schemas.UserCreate):
    db_usuer = models.User (
        username = user.username,
        email= user.email,
        hashed_pass= get_password_hash(user.password)
    )
    db.add(db_usuer)
    db.commit()
    db.refresh(db_usuer)
    return db_usuer

def get_user_by_username(db:Session, username:str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_id(db:Session, id:int):
    return db.query(models.User).filter(models.User.id == id).first()

def create_expense(db:Session, expense: schemas.ExpenseCreate, userId:int):
    db_expense = models.Expense(userId == id, **expense.model_dump())
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

def get_expense(db:Session, user_id:int):
    return db.query(models.Expense).filter(models.Expense.id == user_id).first()

