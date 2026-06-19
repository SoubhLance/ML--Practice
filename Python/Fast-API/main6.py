# making fully functional medical record API using FASTAPI --> pydantic (data validation) all endpoints incldong GET , PUT , POST ,PATCH , DELETE 

from fastapi import FastAPI, Path, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Optional
import json

app = FastAPI()


# ==========================
# Helper Functions
# ==========================

def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data


def save_data(data):
    with open("patients.json", "w") as f:
        json.dump(data, f, indent=4)


def calculate_bmi(height, weight):
    return round(weight / (height ** 2), 2)


# ==========================
# Pydantic Models
# ==========================

class Patient(BaseModel):
    id: str = Field(..., example="P001")
    name: str
    city: str
    age: int = Field(..., gt=0, lt=120)
    gender: str
    height: float = Field(..., gt=0)
    weight: float = Field(..., gt=0)


class PatientUpdate(BaseModel):
    name: Optional[str] = None
    city: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    height: Optional[float] = None
    weight: Optional[float] = None


# ==========================
# Basic Routes
# ==========================

@app.get("/")
def home():
    return {
        "message": "Medical Record API Working Successfully"
    }


@app.get("/about")
def about():
    return {
        "message": "CRUD Medical Record API built using FastAPI"
    }


# ==========================
# GET All Patients
# ==========================

@app.get("/view")
def view_patients():
    data = load_data()
    return data


# ==========================
# GET Single Patient
# ==========================

@app.get("/patients/{patient_id}")
def view_patient(
    patient_id: str = Path(
        ...,
        description="Patient ID",
        example="P001"
    )
):
    data = load_data()

    if patient_id in data:
        return data[patient_id]

    raise HTTPException(
        status_code=404,
        detail="Patient Not Found"
    )


# ==========================
# SORT Patients
# ==========================

@app.get("/sort")
def sort_patients(
    sort_by: str = Query(
        ...,
        description="height, weight, bmi"
    ),
    order: str = Query(
        "asc",
        description="asc or desc"
    )
):

    valid_fields = ["height", "weight", "bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Choose from {valid_fields}"
        )

    if order not in ["asc", "desc"]:
        raise HTTPException(
            status_code=400,
            detail="Order must be asc or desc"
        )

    data = load_data()

    reverse_order = True if order == "desc" else False

    sorted_data = sorted(
        data.values(),
        key=lambda x: x.get(sort_by, 0),
        reverse=reverse_order
    )

    return sorted_data


# ==========================
# CREATE Patient
# ==========================

@app.post("/create")
def create_patient(patient: Patient):

    data = load_data()

    if patient.id in data:
        raise HTTPException(
            status_code=400,
            detail="Patient Already Exists"
        )

    patient_dict = patient.model_dump()

    patient_dict["bmi"] = calculate_bmi(
        patient.height,
        patient.weight
    )

    data[patient.id] = patient_dict

    save_data(data)

    return {
        "message": "Patient Created Successfully",
        "patient": patient_dict
    }


# ==========================
# UPDATE Patient (PUT)
# ==========================

@app.put("/update/{patient_id}")
def update_patient(
    patient_id: str,
    patient: Patient
):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(
            status_code=404,
            detail="Patient Not Found"
        )

    patient_dict = patient.model_dump()

    patient_dict["bmi"] = calculate_bmi(
        patient.height,
        patient.weight
    )

    data[patient_id] = patient_dict

    save_data(data)

    return {
        "message": "Patient Updated Successfully",
        "patient": patient_dict
    }


# ==========================
# PATCH Patient
# ==========================

@app.patch("/patch/{patient_id}")
def patch_patient(
    patient_id: str,
    patient_update: PatientUpdate
):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(
            status_code=404,
            detail="Patient Not Found"
        )

    existing_patient = data[patient_id]

    update_data = patient_update.model_dump(
        exclude_unset=True
    )

    existing_patient.update(update_data)

    if (
        "height" in update_data
        or
        "weight" in update_data
    ):
        existing_patient["bmi"] = calculate_bmi(
            existing_patient["height"],
            existing_patient["weight"]
        )

    data[patient_id] = existing_patient

    save_data(data)

    return {
        "message": "Patient Partially Updated",
        "patient": existing_patient
    }


# ==========================
# DELETE Patient
# ==========================

@app.delete("/delete/{patient_id}")
def delete_patient(patient_id: str):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(
            status_code=404,
            detail="Patient Not Found"
        )

    deleted_patient = data.pop(patient_id)

    save_data(data)

    return {
        "message": "Patient Deleted Successfully",
        "deleted_patient": deleted_patient
    }