# Viewing the Data fetched from json

from fastapi import FastAPI, Path
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
    return {"message": "This is a simple API created using FASTAPI to demonstrate the Read functions"}


@app.get("/view")
def view_patients():
    data = load_data()
    return data

@app.get("/patients/{patient_id}")
def view_patient(patient_id: str = Path(...,description="ID of the patient in the database",example='P001')):
    #loading all the patients
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    return {'error':'patient not found'}
 