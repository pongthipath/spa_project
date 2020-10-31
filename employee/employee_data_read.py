import json
import os

name = input()

os.chdir('../')
path = os.getcwd() + '/data/json/'
filename = 'employees.json'

with open(path + filename) as json_file:
    data = json.load(json_file)
    for p in data['EMPLOYEES']:
        if(p['name'] == name):
            print(p)
