import json
import os

name = input()

os.chdir('../')
path = os.getcwd() + '/data/json/'
filename = 'treatments.json'

with open(path + filename) as json_file:
    data = json.load(json_file)
    for p in data['TREATMENTS']:
        if(p['treatment_name'] == name):
            print(p)