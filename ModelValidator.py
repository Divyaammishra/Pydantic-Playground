from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Employee(BaseModel):
    name: str
    age: int
    email: EmailStr
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    """Model Validator can be used when your validation is depend on the 2 or more field"""
    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 50 and 'emergency' not in model.contact_details:
            raise ValueError('Kindly specify emergency contact')
        return model
    
def update_employee_info(employee: Employee):
    print('name:', employee.name)
    print('age:', employee.age)
    print('email:', employee.email)
    print('weight:', employee.weight)
    print('allergies:', employee.allergies)
    print('contacts:', employee.contact_details)
    print('status:', 'Updated')

employee_info = {'name': 'Divyam', 'age': 25, 'email': 'xyz@google.com', 'weight': 66, 'married':False, 'allergies': ['none'], 'contact_details': {'Phone': '120142', 'emergency': '23708072'}}

employee1 = Employee(**employee_info)

update_employee_info(employee1)


    

    