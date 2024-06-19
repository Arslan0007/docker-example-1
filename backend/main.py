from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import requests

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