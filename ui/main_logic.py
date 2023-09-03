import requests
from constants import API_URL
import json
from constants import get_api_path_by_id

def search_request(selected_option, value):
    
    apiPath = get_api_path_by_id(selected_option)
    if len(apiPath) > 0 and len(value) > 0:
        response = requests.get(API_URL + apiPath + '/' + value)
    else:
        return []  
    if response.status_code == 200:
        return json.loads(response.text)
    else: 
        return []
    

class Compound:
    def __init__(self, cas_no: str, name_substance: str, total_g: float, class_substance: str, location: str, descrip: str, molecular_weight: float, molecular_formula: str):
        self.cas_no = cas_no
        self.name_substance = name_substance
        self.total_g = total_g
        self.class_substance = class_substance
        self.location = location
        self.descrip = descrip
        self.molecular_weight = molecular_weight
        self.molecular_formula = molecular_formula

    def json(self):
        compound_dict = {
            "cas_no": self.cas_no,
            "name_substance": self.name_substance,
            "total_g": self.total_g,
            "class_substance": self.class_substance,
            "location": self.location,
            "descrip": self.descrip,
            "molecular_weight": self.molecular_weight,
            "molecular_formula": self.molecular_formula
        }
        return json.dumps(compound_dict)
    

# написать функцию, кторая примет на вход класс, если true - загрузилось requests.POST(API_URL + json_класс)

def upload_class_to_api(compound: Compound):
    json_data = compound.json()
    response = requests.post(API_URL + '/upload', json=json_data)
    print(json_data)
    if response.status_code == 200:
        return True
    else:
        return False
    
def upload_mass_to_api(cas_no, delta_g):
    response = requests.post(API_URL + '/update_mass', json=json.dumps({'cas_no': cas_no, 'delta_g': delta_g}))
    if response.status_code == 200:
        return True
    else:
        return False
    
def delete_to_api(cas_no):
    response = requests.delete(API_URL + f'/delete_by_key/{cas_no}')
    if response.status_code == 200:
        return True
    else:
        return False
    

    
