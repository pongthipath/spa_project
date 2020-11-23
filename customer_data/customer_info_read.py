import json
import os

path = os.path.abspath('../spa_project') + '/data/json/'
filename = 'customer_info.json'


def get_customer_info_by_name(name):
    with open(path + filename) as json_file:
        data = json.load(json_file)
        for p in data['CUSTOMERS']:
            if(p['fname'] == name):
                return p

def get_customer_info_by_fname_list(name):
    with open(path + filename) as json_file:
        data = json.load(json_file)
        p_list = list()
        for p in data['CUSTOMERS']:
            if(p['fname'] == name):
                p_list.append(p)
        return p_list

def get_customer_info_by_sname_list(name):
    with open(path + filename) as json_file:
        data = json.load(json_file)
        p_list = list()
        for p in data['CUSTOMERS']:
            if(p['sname'] == name):
                p_list.append(p)
        return p_list

def get_customer_info_by_id_list(name):
    with open(path + filename) as json_file:
        data = json.load(json_file)
        p_list = list()
        for p in data['CUSTOMERS']:
            if(p['id'] == name):
                p_list.append(p)
        return p_list

def get_customer_info_by_id(id_c):
    with open(path + filename) as json_file:
        data = json.load(json_file)
        for p in data['CUSTOMERS']:
            if(p['id'] == id_c):
                return p

def get_customer_info_by_sur(sname):
    with open(path + filename) as json_file:
        data = json.load(json_file)
        for p in data['CUSTOMERS']:
            if(p['sname'] == sname):
                return p

def get_customer_info_all_name():

    with open(path + filename) as json_file:
        data = json.load(json_file)
        name_list = list()
        for p in data['CUSTOMERS']:
            name_list.append(p['fname'])
        return name_list

def get_customer_info_all_id():

    with open(path + filename) as json_file:
        data = json.load(json_file)
        id_list = list()
        for p in data['CUSTOMERS']:
            id_list.append(p['id'])
        return id_list

def get_customer_info_all():

    with open(path + filename) as json_file:
        data = json.load(json_file)
        return data['CUSTOMERS']