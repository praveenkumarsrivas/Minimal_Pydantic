# provide the discount on medicine if the employee is from hdfc or icici bank
# name should be in upper case

from pydantic import BaseModel, Field, validator, field_validator
from typing import Dict, List, Optional

class Patient(BaseModel):
  name:str
  age:int
  weight:float
  married:bool
  allergies:Optional[list[str]] = None # alergies is optional
  email:str
  
  @field_validator('email')
  @classmethod
  def validate_email(cls,value):
    if value.split("@")[-1] not in ['icici.com','hdfc.com']:
      raise ValueError("email domain should be icici.com or hdfc.com to get the discount")
    else:
      return value
    
  @field_validator('name')
  @classmethod
  def transform_name(cls,value):
    return value.upper()
  
def insert_data(patient:Patient):
  print(patient.name)
  print(patient.age)
  print(patient.weight)
  print(patient.married)
  print(patient.allergies)
  print(patient.email)
  print("Patient data inserted successfully in insert_data.")
  
  
patient_info = {
  "name":"praveen",
  "age":30,
  "weight":70.5,
  "married":True,
  "allergies":["pollen","dust"],
  "email":"hello@hdfc.com"
}
patient1 = Patient(**patient_info)
insert_data(patient1)

  