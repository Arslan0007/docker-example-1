from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import requests
# from models import Base, User
# from schemas import UserSchema
# from database import engine, SessionLocal
# from sqlalchemy.orm import Session

# Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="MyApp",
    description="Hello API dev",
    version="0.1.0"
)

origins = [
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

url = "https://api.coindesk.com/v1/bpi/currentprice.json"


@app.get("/")
async def root():
    response = requests.get(url)
    response_json = response.json()
    response_usd_rate = response_json["bpi"]["USD"]["rate"]
    
    return {"message": response_usd_rate}

# new
# def get_db():
#     try:
#         db = SessionLocal()
#         yield db
#     finally:
#         db.close()
# # new
# @app.post("/adduser")
# async def add_user(request:UserSchema, db: Session = Depends(get_db)):
#     user = User(name=request.name, date=request.date)
#     db.add(user)
#     db.commit()
#     db.refresh(user)
#     return user
# # new for db
# @app.get("/user/{user_name}")
# async def get_users(user_name, db: Session = Depends(get_db)):
#     users = db.query(User).filter(User.name == user_name).first()
#     return users