# Viewing the Data fetched from json

from fastapi import FastAPI, Path, HTTPException, Query
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
    # return {'error':'patient not found'}
    raise HTTPException(status_code=404,detail='Patient Not Found')  

@app.get('/sort')
def sort_patients(sort_by : str = Query(..., description='Sort on the basis of height, weight or bmi'), order : str = Query('asc',description = 'sort in ascening or desending order')):
    valid_field = ['height', 'weight', 'bmi']

    if sort_by not in valid_field:
        raise HTTPException(status_code="400",detail= f'Invalid Field please select from {valid_field}') 
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400,detail="Not a valid response pls select from asc or desc")
    
    data = load_data()
    sort_order =  True if order == 'desc' else False
    sorted_data = sorted(data.values(),key=lambda x: x.get(sort_by, 0),reverse=sort_order)

    return sorted_data