from pydantic import BaseModel, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Employee(BaseModel):
    name: str
    age: int = Field(gt=18, lt=60, strict=True, description='employee age should be greater than 18 and less than 60') #Data Validation, Strict will through the erro if data is invalid as Pydantic is smart to consider int in string format as int
    weight: float
    married: bool = False #False is default value here
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]   #In case if you don't want to share
    contact_details: Dict[str, str]
    linkedIn: AnyUrl #It is custome datatype to varify if the given data is valid or not - Data Validation


def insert_employee_data(employee: Employee): #Function
    print('name:', employee.name)
    print('age:', employee.age)
    print('weight:', employee.weight)
    print('married:', employee.married)
    print('allergies:', employee.allergies)
    print('contact_details:', employee.contact_details)
    print('status:', 'inserted')


employee_info = {'name': 'Divyam', 'age': 25, 'weight': 66, 'contact_details': {'email': 'divyam@example.com', 'phone': '1010101010'}, 'linkedIn': 'https://www.linkedin.com/in/mishra-divyam/'} #Act as databse

employee1 = Employee(**employee_info)

insert_employee_data(employee1)


    
    