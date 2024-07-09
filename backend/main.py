from fastapi import FastAPI, Request, Depends, HTTPException, UploadFile, File
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import requests
import datetime
from fastapi.responses import PlainTextResponse
from io import StringIO
import json


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



def write_to_text(price, dtime):
    with open('pricelist.txt', 'a') as p:
        p.write("\n" + f'price : {price}, date : {dtime}')


def read_to_text(pricelist):
    with open('pricelist.txt', 'r') as f:
        content = f.read()
    print("\n" + pricelist + content)
    return content


def write_to_text_as_json(pricelist):
    filename = 'pricelist.txt'
    dict1 = {}
    with open(filename) as fh:
        for line in fh:
            command, description = line.strip().split(None, 1)
            dict1[command] = description.strip()
    out_file = open("pricelist.json", "w")
    json.dump(dict1, out_file, indent = 4, sort_keys= False)
    out_file.close()

  
def read_to_text_as_json(pricelist):
    with open('pricelist.json', 'r') as f:
        data = json.load(f)
    print(data)
    return data

@app.get("/price/usd/")
async def root():
    response = requests.get(url)
    response_json = response.json()
    response_usd_rate = response_json["bpi"]["USD"]["rate"]
    write_to_text(response_usd_rate, datetime.datetime.now())
    return {"message": response_usd_rate}

@app.get("/price/eur/")
async def root():
    response = requests.get(url)
    response_json = response.json()
    response_eur_rate = response_json["bpi"]["EUR"]["rate"]
    write_to_text(response_eur_rate, datetime.datetime.now())
    return {"message": response_eur_rate}

@app.get("/price/gbp/")
async def root():
    response = requests.get(url)
    response_json = response.json()
    response_gbp_rate = response_json["bpi"]["GBP"]["rate"]
    write_to_text(response_gbp_rate, datetime.datetime.now())
    return {"message": response_gbp_rate}

@app.get("/pricelist/")
async def pricelist():
    return read_to_text_as_json('pricelist.json')
