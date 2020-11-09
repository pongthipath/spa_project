import json
import os

path = os.path.abspath('../spa_project') + '/data/json/'
filename = 'rooms.json'

print(path)

def get_room_some(name):
    with open(path + filename) as json_file:
        data = json.load(json_file)
        for p in data['ROOMS']:
            if(p['name'] == name):
                return p

def get_room_all_name():

    with open(path + filename) as json_file:
        data = json.load(json_file)
        name_list = list()
        for p in data['ROOMS']:
            name_list.append(p['name'])
        return name_list

def get_room_all():

    with open(path + filename) as json_file:
        data = json.load(json_file)
        print(data['ROOMS'])
        return data['ROOMS']