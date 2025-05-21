def insert_patient_data(name,age):
  print(name)
  print(age)
  print("Patient data inserted successfully.")
  
insert_patient_data("John Doe", 30) # data inderted to db
insert_patient_data("Alok", "kumar") # gain data inserted but the data is not valid
print("\n======== Type Hunting=========\n")
# now we can do type hunting in function defination
def insert_patient_data_with_type_hunt(name:str,age:int):
  print(name)
  print(age)
  print("Patient data inserted successfully in insert_patient_data_with_type_hunt.")
  
insert_patient_data_with_type_hunt("John Doe", 30)
insert_patient_data_with_type_hunt("Alok", "kumar") # hence type hunting is also not safe as it is not providing any fallback/error if data is not valid
print("\n======== data validation manually=========\n")
# Now we will do the type validation manually
def inert_data_with_manual_validation(name,age):
  if type(name)==str and type(age)==int:
    print(name)
    print(age)
    print("Patient data inserted successfully in inert_data_with_manual_validation.")
  else: 
    raise TypeError("Invalid data type")

inert_data_with_manual_validation("Alok", "kumar") # hence we got the error
# But the type validation using manual is not extensible and not reusable

## hence we need pydantic to do the data validation and type validation
# Pydantic is a data validation and settings management library for Python, which uses Python type annotations to validate data.
# It allows you to define data models using Python classes, and automatically validates the data against the defined types.
# Pydantic is built on top of Python's type hints, which were introduced in Python 3.5. It provides a way to define data models using standard Python types, and then validates the data against those models.
# Pydantic is useful for data validation in web applications, APIs, and other scenarios where you need to ensure that the data being passed around is valid and conforms to a specific schema.
# Pydantic is a powerful library that can help you write cleaner, more maintainable code by enforcing data validation and type checking at runtime.
