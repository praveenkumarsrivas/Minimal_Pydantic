from pydantic import BaseModel, Field, EmailStr, conint, constr, AnyUrl
from typing import Dict, List, Optional,Annotated

# metadata fields can be apply using Annotated
class Patient(BaseModel):
  name:Annotated[str,Field(max_length=50,description="Name of the patient in 50 chars",titlle="Name of the patient")]
  email:EmailStr
  linkedin_url:AnyUrl
  age:Annotated[int, Field(gt=0,lt=120)]
  weight : Annotated[float,Field(gt=0)]
  married:Annotated[bool,Field(default=None,description="Is patient married?")]
  allergies:Annotated[list[str],Field(default=None,max_length=5,max_legth=5)]
  contact_details:Dict[str,str]
  
def insert_data(patient:Patient):
  print(patient.name)
  print(patient.email)
  print(patient.linkedin_url)
  print(patient.age)
  print(patient.weight)
  print(patient.married)
  print(patient.allergies)
  print(patient.contact_details)
  print("Patient data inserted successfully in insert_data.")

patient_info = {
  "name":"praveen",
  "email":"abc@gmail.com",
  "linkedin_url":"https://www.linkedin.com/in/1234",
  "age":30,
  "weight":70.5,
  "married":True,
  # "allergies":["pollen","dust"],
  "contact_details":{
    "phone":"1234567890"
  }
}

patient1 = Patient(**patient_info)

insert_data(patient1)

  
# output:
'''
praveen
abc@gmail.com
https://www.linkedin.com/in/1234
30
70.5
True
None
{'phone': '1234567890'}
Patient data inserted successfully in insert_data.
'''