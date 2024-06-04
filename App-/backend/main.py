from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
import models, schemas, crud, deps, auth, database, currency
from datetime import datetime, timedelta 
from jose import JWTError, jwt
from typing import List


app = FastAPI()

database.init_db()

@app.post("/token", response_model=schemas.Token)
def login_for_access_token(db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = crud.get_user_by_username(db, username=form_data.username)
    if not user or not crud.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(deps.get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users/me/", response_model=schemas.User)
def read_users_me(current_user: schemas.User = Depends(deps.get_current_user)):
    return current_user

@app.post("/expenses/", response_model=schemas.Expense)
def create_expense(expense: schemas.ExpenseCreate, db: Session = Depends(deps.get_db), current_user: schemas.User = Depends(deps.get_current_user)):
    return crud.create_expense(db=db, expense=expense, user_id=current_user.id)

@app.get("/expenses/", response_model=List[schemas.Expense])
def read_expenses(skip: int = 0, limit: int = 10, db: Session = Depends(deps.get_db), current_user: schemas.User = Depends(deps.get_current_user)):
    expenses = crud.get_expenses(db=db, user_id=current_user.id)
    return expenses

@app.get("/currency/dollar_blue")
def read_dollar_blue_value():
    return {"dollar_blue_value": currency.get_dollar_blue_value()}


