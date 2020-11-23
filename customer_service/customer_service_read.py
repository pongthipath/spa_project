import json
import os

def get_customer_service_info_by_name(name, d):
    path = os.path.abspath('../spa_project') + '/data/history/'
    filename = d + '.json'
    with open(path + filename) as json_file:
        data = json.load(json_file)
        for p in data['HISTORY']:
            if(p['fname'] == name):
                return p

def get_customer_service_info_by_fname_list(name, d):
    path = os.path.abspath('../spa_project') + '/data/history/'
    filename = d + '.json'
    with open(path + filename) as json_file:
        data = json.load(json_file)
        p_list = list()
        for p in data['HISTORY']:
            if(p['fname'] == name):
                p_list.append(p)
        return p_list

def get_customer_service_info_by_sname_list(name, d):
    path = os.path.abspath('../spa_project') + '/data/history/'
    filename = d + '.json'
    with open(path + filename) as json_file:
        data = json.load(json_file)
        p_list = list()
        for p in data['HISTORY']:
            if(p['sname'] == name):
                p_list.append(p)
        return p_list

def get_customer_service_info_by_id_list(name, d):
    path = os.path.abspath('../spa_project') + '/data/history/'
    filename = d + '.json'
    with open(path + filename) as json_file:
        data = json.load(json_file)
        p_list = list()
        for p in data['HISTORY']:
            if(p['id'] == name):
                p_list.append(p)
        return p_list

def get_customer_service_info_by_id(id_c, d):
    path = os.path.abspath('../spa_project') + '/data/history/'
    filename = d + '.json'
    with open(path + filename) as json_file:
        data = json.load(json_file)
        for p in data['HISTORY']:
            if(p['id'] == id_c):
                return p

def get_customer_service_info_by_sur(sname, d):
    path = os.path.abspath('../spa_project') + '/data/history/'
    filename = d + '.json'
    with open(path + filename) as json_file:
        data = json.load(json_file)
        for p in data['HISTORY']:
            if(p['sname'] == sname):
                return p

def get_customer_service_info_all_name(d):
    path = os.path.abspath('../spa_project') + '/data/history/'
    filename = d + '.json'
    with open(path + filename) as json_file:
        data = json.load(json_file)
        name_list = list()
        for p in data['HISTORY']:
            name_list.append(p['fname'])
        return name_list

def get_customer_service_info_all_id(d):
    path = os.path.abspath('../spa_project') + '/data/history/'
    filename = d + '.json'
    with open(path + filename) as json_file:
        data = json.load(json_file)
        id_list = list()
        for p in data['HISTORY']:
            id_list.append(p['id'])
        return id_list

def get_customer_service_info_all(d):
    path = os.path.abspath('../spa_project') + '/data/history/'
    filename = d + '.json'
    with open(path + filename) as json_file:
        data = json.load(json_file)
        return data['HISTORY']