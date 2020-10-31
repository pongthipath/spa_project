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
            print(p)
            print('Token: ')
            token = input()
            print('Hand_pay: ')
            hp = input()
            p['token'] = int(token)
            p['hand_pay'] = int(hp)
            print(p)
    
    write_json(data)