import json
import os

path = os.path.abspath('../spa_project') + '/data/json/'
filename = 'customer_info.json'

def edit_treatment_customer_info(name, treatment):
    def write_json(data): 
        with open(path + filename,'w') as f: 
            json.dump(data, f) 

    with open(path + filename) as json_file:
        data = json.load(json_file)
        for p in data['CUSTOMERS']:
            if(p['fname'] == name):
                p['treatment'] = treatment
    
        write_json(data)
