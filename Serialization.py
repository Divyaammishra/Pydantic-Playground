from pydantic import BaseModel

"""Exporting python model in dictionary and json"""
class Address(BaseModel):
    city: str
    state: str
    pincode: str

class Employee(BaseModel):
    name: str
    gender: str
    age: int
    address: Address


employee_address = {'city': 'varanasi', 'state': 'Uttar Pradesh', 'pincode': '1234'}
employee_address1 = Address(**employee_address)

employee_info = {'name': 'divyam', 'gender': 'male', 'age': 25, 'address': employee_address1}
employee1 = Employee(**employee_info)

#Exporting
export = employee1.model_dump() #exporting in dict
#export = employee1.model_dump(include=['name']) if you want to expo specific field
#export = employee1.model_dump(exclude=['name']) if you want exclude specific field

export2 = employee1.model_dump_json() #exporting in json

print(export)
print(type(export))

