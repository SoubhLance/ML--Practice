# def insert_patient_data(name,age):
#      print(name) #STR
#      print(age) #INT
#      print('inserted successfully to the database')



# insert_patient_data("Nilesh","thirty-two")

## To Fix that we are using the pydantic 

from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List, Dict, Optional

class Patient(BaseModel):
    name:str = Field(max_length=50)
    age:int = Field(gt=0,lt=120)
    email:EmailStr
    linedin:AnyUrl
    weight:float = Field(gt=0)
    married:bool
    allergies:Optional[List[str]]  = Field(max_length=5)
    contact_details: Dict[str,str]


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