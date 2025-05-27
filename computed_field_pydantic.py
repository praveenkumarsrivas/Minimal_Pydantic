# caluclate the bmi using weight and height, and that should be computed using the given data of patient

from pydantic import BaseModel, field_validator, model_validator,computed_field
from typing import List,Dict

class Patient(BaseModel):
  name:str
  age:int
  weight:float # in kgs
  height:float # in mts
  
  @computed_field
  def bmi(self) -> float:
    bmi = self.weight/self.height**2
    return bmi
  
def patient_details_update(patient:Patient):
  print("name:\t",patient.name)
  print("age:\t",patient.age)
  print("weight:\t",patient.weight)
  print("height:\t",patient.height)
  print("BMI:\t",patient.bmi)
  print("data updated")

patient_info = {"name":"Akshay","age":30,"weight":75,"height":1.76}

patient_obj = Patient(**patient_info)

patient_details_update(patient_obj)

#O/P:
'''
name:    Akshay
age:     30
weight:  75.0
height:  1.76
BMI:     24.212293388429753
data updated
'''