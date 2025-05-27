from pydantic import BaseModel

class Patient(BaseModel):
  name:str
  age:int

def insert_patient_data(name:str,age:int):
  print(name)
  print(age)
  print("Patient data inserted successfully in insert_patient_data.")
  
patient_info = {"name":"praveen","age":30}

patient1 = Patient(**patient_info)

insert_patient_data(patient1.name, patient1.age)

print("\n======== passing it object of base model =========\n")
class Patient(BaseModel):
  name:str
  age:int

def insert_patient_data(patient:Patient):
  name = patient.name
  age = patient.age
  print(name)
  print(age)
  print("Patient data inserted successfully in insert_patient_data.")
  
patient_info1 = {"name":"praveen","age":30}

patient1 = Patient(**patient_info1)

insert_patient_data(patient1)

patient_info2 = {"name":"Kumar","age":"thirty"} # invalid data (  Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='thirty', input_type=str])

patient2 = Patient(**patient_info2)

insert_patient_data(patient2)