from pydantic import BaseModel, Field, EmailStr, conint, constr
from typing import Dict, List, Optional

class Patient(BaseModel):
  name:str
  age:str
  weight:float
  married:bool = False # default value is false
  allergies:Optional[list[str]] = None # alergies is optional
  contact_details:Dict[str,str]
  
def insert_data(patient:Patient):
  print(patient.name)
  print(patient.age)
  print(patient.weight)
  print(patient.married)
  print(patient.allergies)
  print(patient.contact_details)
  print("Patient data inserted successfully in insert_data.")

patient_info = {
  "name":"praveen",
  "age":"30",
  "weight":70.5,
  "contact_details":{
    "email":"abc@gmail.com",
    "phone":"1234567890"
  }
}

patient1 = Patient(**patient_info)

insert_data(patient1)


# o/p:
'''
praveen
30
70.5
False
None
{'email': 'abc@gmail.com', 'phone': '1234567890'}
Patient data inserted successfully in insert_data.'''