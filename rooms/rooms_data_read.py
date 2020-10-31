import json
import os

name = input()

os.chdir('../')
path = os.getcwd() + '/data/json/'
filename = 'rooms.json'

with open(path + filename) as json_file:
    data = json.load(json_file)
    for p in data['ROOMS']:
        if(p['room_name'] == name):
            print(p)