import json
import os

path = os.path.abspath('../spa_project') + '/data/json/'
filename = 'rooms.json'

def delete_this_room(name):
    def write_json(data): 
        with open(path + filename,'w') as f: 
            json.dump(data, f) 

    with open(path + filename) as json_file:
        data = json.load(json_file)
        for p in data['ROOMS']:
            if(p['name'] == name):
                data['ROOMS'].remove(p)
                print(p)
    
        write_json(data)