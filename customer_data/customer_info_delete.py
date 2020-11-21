import json
import os

path = os.path.abspath('../spa_project') + '/data/json/'
filename = 'customer_info.json'

def delete_this_customer_info_by_id(id_c):
    def write_json(data): 
        with open(path + filename,'w') as f: 
            json.dump(data, f) 

    with open(path + filename) as json_file:
        data = json.load(json_file)
        for p in data['CUSTOMERS']:
            if(p['id'] == id_c):
                data['CUSTOMERS'].remove(p)
                print(p)
    
        write_json(data)

def delete_this_customer_info_by_name(name):
    def write_json(data): 
        with open(path + filename,'w') as f: 
            json.dump(data, f) 

    with open(path + filename) as json_file:
        data = json.load(json_file)
        for p in data['CUSTOMERS']:
            if(p['fname'] == name):
                data['CUSTOMERS'].remove(p)
                print(p)
    
        write_json(data)
