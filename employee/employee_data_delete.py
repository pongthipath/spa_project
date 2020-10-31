import json
import os

name = input()

os.chdir('../')
path = os.getcwd() + '/spa_project/data/json/'
filename = 'employees.json'

print(os.path.abspath(os.getcwd()))

def write_json(data): 
    with open(path + filename,'w') as f: 
        json.dump(data, f) 

with open(path + filename) as json_file:
    data = json.load(json_file)
    for p in data['EMPLOYEES']:
        if(p['name'] == name):
            data['EMPLOYEES'].remove(p)
            print(p)
    
    write_json(data)