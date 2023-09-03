#from main import cas_no, name_substance, class_substance

# файл для консант 

API_URL = 'http://127.0.0.1:5000/'

search_options = [
    ('CAS_No', 'search_by_key'),
    ('Class', 'search_by_class'),
    ('Name', 'search_by_name')
]

def get_api_path_by_id(id):
    for option in search_options:
        if option[0] == id:
            return option[1]
    return ''