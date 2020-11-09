import json
import os

path = os.path.abspath('../spa_project') + '/data/json/'
filename = 'treatments.json'

def delete_this_treatment(name):
    def write_json(data): 
        with open(path + filename,'w') as f: 
            json.dump(data, f) 

    with open(path + filename) as json_file:
        data = json.load(json_file)
        for p in data['TREATMENTS']:
            if(p['name'] == name):
                data['TREATMENTS'].remove(p)
                print(p)
    
        write_json(data)