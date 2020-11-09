import json
import os

name = input()

os.chdir('../')
path = os.getcwd() + '/spa_project/data/json/'
filename = 'treatments.json'

print(os.path.abspath(os.getcwd()))

def write_json(data): 
    with open(path + filename,'w') as f: 
        json.dump(data, f) 

with open(path + filename) as json_file:
    data = json.load(json_file)
    for p in data['TREATMENTS']:
        if(p['name'] == name):
            print(p)
            print('Token: ')
            token = input()
            p['token'] = int(token)
            print(p)
    
    write_json(data)