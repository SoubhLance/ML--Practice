# Viewing the Data fetched from json using path parameters

from fastapi import FastAPI
from pydantic import BaseModel
import json

app=FastAPI()

def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    
    return data

@app.get("/")
def hello():
    return {"message": "API WOrking CHeck the endPoints"}

@app.get("/about")
def about():
    return {"message": "This is a simple API created using FASTAPI to demonstrate the Read functions with paticular parameters to fetch data from json file"}


@app.get("/view")
def view_patients():
    data = load_data()
    return data
