import json
import os

path = os.path.abspath('../spa_project') + '/data/json/'
filename = 'employees.json'

def delete_this_employee(name):
    def write_json(data): 
        with open(path + filename,'w') as f: 
            json.dump(data, f) 

    with open(path + filename) as json_file:
        data = json.load(json_file)
        for p in data['EMPLOYEES']:
            if(p['name'] == name):
                data['EMPLOYEES'].remove(p)
    
        write_json(data)