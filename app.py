from flask import Flask, jsonify, request
import sqlite3
from reagent_stocktaking_db import*
import json

app = Flask(__name__)

create_table()
import_csv_data()

# SEARCH

@app.route('/')
def hello():
    return 'Hello API'

@app.route('/search_by_key/<string:cas_no>', methods=['GET'])
def search_by_key(cas_no):
    return jsonify(search_by_key_sql(cas_no))
    

@app.route('/search_by_class/<string:class_substance>', methods=['GET'])
def search_by_class_substance(class_substance):
    return jsonify(search_by_class_substance_sql(class_substance))

@app.route('/search_by_name/<string:name_substance>', methods=['GET'])
def search_by_name_substance(name_substance):
    return jsonify(search_by_name_substance_sql(name_substance))


# UPLOAD (ADD UPDATE)

@app.route('/upload', methods=['POST'])
def upload():
    data = json.loads(request.get_json())
    print(data['cas_no'])
    if data is None:
        return jsonify({'error': 'INVALID JSON'}), 400
    upload_sql(data)
    return 'OK', 200

@app.route('/update_mass', methods=['POST'])
def update_mass():
    data = json.loads(request.get_json())
    print(data['cas_no'])
    if data is None:
        return jsonify({'error': 'INVALID JSON'}), 400
    change_mass_by_cas_sql(data['cas_no'], data['delta_g'])
    return 'OK', 200

@app.route('/delete_by_key/<string:cas_no>', methods=['DELETE'])
def delete_by_key(cas_no):
    delete_record_by_key_sql(cas_no)
    return jsonify({'message': 'Record deleted successfully'})


    
