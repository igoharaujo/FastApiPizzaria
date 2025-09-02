import os

from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

app = FastAPI()
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

from auth_routes import *
from order_routes import *

app.include_router(order_router)
app.include_router(auth_router)


#uvicorn main:app --reload