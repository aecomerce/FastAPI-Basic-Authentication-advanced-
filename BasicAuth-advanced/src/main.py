from typing import Annotated
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from hashed_password.HashPassword import pwd_context
from models.model_user import User
import secrets


app = FastAPI()
security = HTTPBasic()

# Храним только username и hashed_password
fake_users_db = []


def get_user_from_db(username: str):
    for user in fake_users_db:
        if secrets.compare_digest(user["username"], username):
            return user
    return None


def auth_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    user = get_user_from_db(credentials.username)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"}
        )
    if not pwd_context.verify(credentials.password, user["hashed_password"]):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"}
        )
    return user


@app.post("/register")
def register_user(user: User):
    if get_user_from_db(user.username):
        raise HTTPException(status_code=400, detail="User already exists")
    hashed_password = pwd_context.hash(user.password)
    db_object = {"username": user.username, "hashed_password": hashed_password}
    fake_users_db.append(db_object)
    return {"message": "User registered successfully"}


@app.get("/login")
def login_user(user: dict = Depends(auth_user)):
    return {"message": f"Welcome, {user['username']}!"}
