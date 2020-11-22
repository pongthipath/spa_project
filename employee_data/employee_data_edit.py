import json
import os

path = os.path.abspath('../spa_project') + '/data/json/'
filename = 'employees.json'

def reset_this_handPay(name):
    def write_json(data): 
        with open(path + filename,'w') as f: 
            json.dump(data, f) 

    with open(path + filename) as json_file:
        data = json.load(json_file)
        for p in data['EMPLOYEES']:
            if(p['name'] == name):
                p['hand_pay'] = []
    
        write_json(data)

def increase_this_handPay(name, hp):
    def write_json(data): 
        with open(path + filename,'w') as f: 
            json.dump(data, f) 

    with open(path + filename) as json_file:
        data = json.load(json_file)
        for p in data['EMPLOYEES']:
            if(p['name'] == name):
                p['hand_pay'] = hp
    
        write_json(data)