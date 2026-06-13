## Field Validator

from pydantic import BaseModel,EmailStr,AnyUrl,Field, field_validator
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    name: str
    emsil: EmailStr
    age:int
    weight: float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains= ['hdfc.com','icici.com']
        domain_name=value.split('@')[-1]
        if domain_name not in valid_domains:
           raise ValueError('Not a Valid domain')

    @field_validator('name')
    @classmethod
    def Name_upper(cla,value):
        return value.upper()
    
    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')
    

def insert_patient_data(patient : Patient):

    print(patient.name)
    print(patient.age)

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print("Updated Records")

patient_info = {'name':'Soubhik','age':21}
patient_info1 = {'name':'Soubhik','age':'tyhirty'} ## Checking the Wrong output 
patient_info2 = {'name':'Soubhik','age':36}
patient_info3 = {'name':'Soubhik','age':36, 'weight':75.2,'married': True,'allergies':['pollen','dust'], 'contact_details':{'email':'abc@gmail.com','phone':'9852458769'}}

patient1 = Patient(**patient_info)
# patient2 = Patient(**patient_info1) ## wrong
patient3 = Patient(**patient_info2)
patient4 = Patient(**patient_info3)


insert_patient_data(patient1)
print("patient2 data is not valid")
# insert_patient_data(patient2)  ## here inserting and then validation error 
update_patient_data(patient3)
insert_patient_data(patient4)