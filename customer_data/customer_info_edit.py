import json
import os

path = os.path.abspath('../spa_project') + '/data/json/'
filename = 'customer_info.json'

def edit_treatment_customer_info_by_name(name, treatment):
    def write_json(data): 
        with open(path + filename,'w') as f: 
            json.dump(data, f) 

    with open(path + filename) as json_file:
        data = json.load(json_file)
        for p in data['CUSTOMERS']:
            if(p['fname'] == name):
                p['treatments'] = treatment
    
        write_json(data)

def edit_treatment_customer_info_by_id(id_c, treatment):
    def write_json(data): 
        with open(path + filename,'w') as f: 
            json.dump(data, f) 

    with open(path + filename) as json_file:
        data = json.load(json_file)
        for p in data['CUSTOMERS']:
            if(p['id'] == id_c):
                p['treatments'] = treatment
    
        write_json(data)

def de_customer_t_by_id(id_c, treatment):
    with open(path + filename) as json_file:
        data = json.load(json_file)
        json_list = list()
        all_list = list()
        e_list = list()
        l_list = list()
        for p in data['CUSTOMERS']:
            if(p['id'] == id_c):
                for t in p['treatments']:
                    for nt in treatment:
                        if(t['treatment'] == nt['treatment']):
                            if(int(t['amount']) >= int(nt['amount'])):
                                temp = int(t['amount']) - int(nt['amount'])
                                data = t['treatment'] + ':' + str(temp)
                                e_json ={
                                    'treatment': t['treatment'],
                                    'amount': str(temp)
                                }
                                json_list.append(e_json)
                                e_list.append(data)
                            if(int(t['amount']) < int(nt['amount'])):
                                temp_lack = int(nt['amount']) - int(t['amount'])
                                data_lack = t['treatment'] + ':' + str(temp_lack)
                                l_json = {
                                    'treatment': t['treatment'],
                                    'amount': '0'
                                }
                                json_list.append(l_json)
                                l_list.append(data_lack)

        all_list.append(e_list)
        all_list.append(l_list)
        all_list.append(json_list)
        return all_list

def de_customer_t_by_id_to_json(id_c, treatment):
    def write_json(data): 
        with open(path + filename,'w') as f: 
            json.dump(data, f) 

    with open(path + filename) as json_file:
        data = json.load(json_file)
        json_list = treatment
        old_list = list()
        for p in data['CUSTOMERS']:
            if(p['id'] == id_c):
                for t in p['treatments']:
                    old_list.append(t)
                    for nt in treatment:
                        if(t['treatment'] == nt['treatment']):
                            old_list.remove(t)

        for o in old_list:
            json_list.append(o)

        for l in data['CUSTOMERS']:
            if(l['id'] == id_c):
                l['treatments'] = json_list

        write_json(data)

def in_customer_t_by_id(name, treatment):
    def write_json(data): 
        with open(path + filename,'w') as f: 
            json.dump(data, f) 

    with open(path + filename) as json_file:
        data = json.load(json_file)
        json_list = list()
        old_list = list()

        for p in data['CUSTOMERS']:
            if(p['id'] == name):    
                for t in p['treatments']:
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

        for l in data['CUSTOMERS']:
            if(l['id'] == name):
                l['treatments'] = json_list
        
        write_json(data)