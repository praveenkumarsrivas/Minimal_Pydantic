'''
if age ofthe patient is greater then 60 then it should be considered as senior citizen
and make sure in contact details it should have atleast one emergency contact details
'''

from pydantic import BaseModel, Field, EmailStr, conint, constr, field_validator, model_validator
from typing import Dict, List, Optional

class Patient(BaseModel):
  name:str
  email:EmailStr
  age:int
  weight:float
  contact_details:Dict[str,str]
  
  @model_validator(mode='after')
  def validate_emergency_contact(cls,model):
    if model.age>60 and "emergency" not in model.contact_details:
      raise ValueError("patient must have emergency contact, patient is above 60 age")
    return model
  
def update_patient_details(patient:Patient):
  name = patient.name
  email = patient.email
  age = patient.age
  weight = patient.weight
  contact_details = patient.contact_details
  print(name)
  print(email)
  print(age)
  print(weight)
  print(contact_details)
  
patient_info1 = {"name":"Ahem","email":"abc@def.com","age":80,"weight":80,"contact_details":{'emergency':'9876543212'}}
patient11 = Patient(**patient_info1)
update_patient_details(patient11)
  

print("\n===================== Not Having emergency contact=============\n")
patient_info = {"name":"Ahem","email":"abc@def.com","age":80,"weight":80,"contact_details":{'Mob':'9876543212'}}
patient1 = Patient(**patient_info)
update_patient_details(patient1)


#o/p:
'''
alue error, patient must have emergency contact, patient is above 60 age [type=value_error, input_value={'name': 'Ahem', 'email':...: {'Mob': '9876543212'}}, input_type=dict]
'''