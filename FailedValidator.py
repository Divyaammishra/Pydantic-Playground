from pydantic import BaseModel, EmailStr, field_validator
from typing import List, Dict

class Employee(BaseModel):
    name: str
    age: int
    email: EmailStr
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    
    """field validator can be used when you want to valid data for specific domain, 
    like here we are validation email only for google and netflix. and it can be used when your 
    validation is depend on single field but when it is required we have to use model validator"""

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['google.com', 'netflix.com']

        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Invalid Email')
        
        return value

#Field Validator can be operate in 2 mode [before / after]
    @field_validator('age', mode='after')
    @classmethod
    def age_validator(cls, value):
        if 18 < value < 60:
            return value
        else:
            raise ValueError('Age should be between 18 to 60 ')

def update_employee_info(employee: Employee):
    print('name:', employee.name)
    print('age:', employee.age)
    print('email:', employee.email)
    print('weight:', employee.weight)
    print('allergies:', employee.allergies)
    print('contacts:', employee.contact_details)
    print('status:', 'Updated')

employee_info = {'name': 'Divyam', 'age': 25, 'email': 'xyz@google.com', 'weight': 66, 'married':False, 'allergies': ['none'], 'contact_details': {'Phone': '120142'}}

employee1 = Employee(**employee_info)

update_employee_info(employee1)
