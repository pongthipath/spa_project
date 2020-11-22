import json
import os

path = os.path.abspath('../spa_project') + '/data/json/'
filename = 'treatments.json'


def get_treatment_some(name):
    with open(path + filename) as json_file:
        data = json.load(json_file)
        for p in data['TREATMENTS']:
            if(p['name'] == name):
                return p

def get_treatment_all_name():

    with open(path + filename) as json_file:
        data = json.load(json_file)
        name_list = list()
        for p in data['TREATMENTS']:
            name_list.append(p['name'])
        return name_list

def get_treatment_all():

    with open(path + filename) as json_file:
        data = json.load(json_file)
        return data['TREATMENTS']