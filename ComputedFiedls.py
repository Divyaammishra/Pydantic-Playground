from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Employee(BaseModel):
    name: str
    age: int
    email: EmailStr
    weight: float #KG
    height: float #M
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    """Computed Field is useful for values that are derived from other fields within the model"""
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi

    
def update_employee_info(employee: Employee):
    print('name:', employee.name)
    print('age:', employee.age)
    print('email:', employee.email)
    print('weight:', employee.weight)
    print('BMI:', employee.bmi)
    print('allergies:', employee.allergies)
    print('contacts:', employee.contact_details)
    print('status:', 'Updated')

employee_info = {'name': 'Divyam', 'age': 25, 'email': 'xyz@google.com', 'weight': 66, 'height': 1.70, 'married':False, 'allergies': ['none'], 'contact_details': {'Phone': '120142', 'emergency': '23708072'}}

employee1 = Employee(**employee_info)

update_employee_info(employee1)


    

    