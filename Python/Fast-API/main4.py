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
    return {"message": "This is a simple API created using FASTAPI to demonstrate the CRUD functions"}


@app.get("/view")
def view_patients():
    data = load_data()
    return data
