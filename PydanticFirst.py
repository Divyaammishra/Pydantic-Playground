from pydantic import BaseModel
from typing import List, Dict

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]


def insert_patient_data(patient: Patient): #Function
    print('name:', patient.name)
    print('age:', patient.age)
    print('weight:', patient.weight)
    print('allergies:', patient.allergies)
    print('contact_details:', patient.contact_details)
    print('status:', 'inserted')


patient_info = {'name': 'Divyam', 'age': 25, 'weight': 66, 'married': False, 'allergies': ['none'], 'contact_details': {'email': 'divyam@example.com', 'phone': '1010101010'}} #Act as databse

patient1 = Patient(**patient_info)

insert_patient_data(patient1)


    
    