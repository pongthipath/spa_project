import json
import os

name = input()

os.chdir('../')
path = os.getcwd() + '/spa_project/data/json/'
filename = 'rooms.json'

print(os.path.abspath(os.getcwd()))

def write_json(data): 
    with open(path + filename,'w') as f: 
        json.dump(data, f) 

with open(path + filename) as json_file:
    data = json.load(json_file)
    for p in data['ROOMS']:
        if(p['room_name'] == name):
            print(p)
    
    write_json(data)