import json
import os

path = os.path.abspath('../spa_project') + '/data/json/'
filename = 'employees.json'

def reset_this_handPay(name, treatment):
    def write_json(data): 
        with open(path + filename,'w') as f: 
            json.dump(data, f) 

    with open(path + filename) as json_file:
        data = json.load(json_file)
        for p in data['EMPLOYEES']:
            if(p['name'] == name):
                p['hand_pay'] = treatment
    
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

def in_hp_employee(name, treatment):
    def write_json(data): 
        with open(path + filename,'w') as f: 
            json.dump(data, f) 

    with open(path + filename) as json_file:
        data = json.load(json_file)
        json_list = list()
        old_list = list()

        for p in data['EMPLOYEES']:
            if(p['name'] == name):    
                for t in p['hand_pay']:
                    old_list.append(t)
                    for nt in treatment:
                        if(t['treatment'] == nt['treatment']):
                            temp = int(t['amount']) + int(nt['amount'])
                            e_json ={
                                'treatment': t['treatment'],
                                'amount': str(temp)
                            }
                            json_list.append(e_json)
                            old_list.remove(t)

        for o in old_list:
            json_list.append(o)

        for l in data['EMPLOYEES']:
            if(l['name'] == name):
                l['hand_pay'] = json_list
        
        write_json(data)

def de_hp_employee(name, treatment):
    def write_json(data): 
        with open(path + filename,'w') as f: 
            json.dump(data, f) 

    with open(path + filename) as json_file:
        data = json.load(json_file)
        json_list = list()
        old_list = list()

        for p in data['EMPLOYEES']:
            if(p['name'] == name):    
                for t in p['hand_pay']:
                    old_list.append(t)
                    for nt in treatment:
                        if(t['treatment'] == nt['treatment']):
                            temp = int(nt['amount']) - int(t['amount'])
                            e_json ={
                                'treatment': t['treatment'],
                                'amount': str(temp)
                            }
                            json_list.append(e_json)
                            old_list.remove(t)

        for o in old_list:
            json_list.append(o)

        for l in data['EMPLOYEES']:
            if(l['name'] == name):
                l['hand_pay'] = json_list
        
        write_json(data)
                    