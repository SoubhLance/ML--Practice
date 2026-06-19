## Compute FIeld 


from pydantic import BaseModel,EmailStr,AnyUrl,Field, field_validator, model_validator
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    name: str
    emsil: EmailStr
    age:int
    weight: float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]
