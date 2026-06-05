# def insert_patient_data(name,age):
#      print(name) #STR
#      print(age) #INT
#      print('inserted successfully to the database')



# insert_patient_data("Nilesh","thirty-two")

## To Fix that we are using the pydantic 

from pydantic import BaseModel

class Patient(BaseModel):
    name:str
    age:int


def insert_patient_data(patient : Patient):

    print(patient.name)
    print(patient.age)

patient_info = {'name':'Soubhik','age':21}
patient_info1 = {'name':'Soubhik','age':'tyhirty'} ## Checking the Wrong output 

patient1 = Patient(**patient_info)
patient2 = Patient(**patient_info1) ## wrong


insert_patient_data(patient1)
insert_patient_data(patient2)  ## here inserting and then validation error 