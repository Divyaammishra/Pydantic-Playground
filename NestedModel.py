from pydantic import BaseModel

"""Nested Model in pydantic is useful, when you want to use a model as field or data-type in another model."""
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

print(employee1)

