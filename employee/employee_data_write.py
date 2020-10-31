import json 
import os
  
name = input()

os.chdir('../')
path = os.getcwd() + '/data/json/'
filename = 'employees.json'

print(path)
# function to add to JSON 
def write_json(data): 
    with open(path + filename,'w') as f: 
        json.dump(data, f) 

def init_json_file():
    init_data = {
        'EMPLOYEES':[]
    }
    with open(path + filename, 'w') as outfile:
        json.dump(init_data, outfile)

def update_data():
    with open(path + filename) as json_file: 
        data = json.load(json_file) 
      
        temp = data['EMPLOYEES'] 
  
        y = {
            'name': name,
            'token': 0,
            'hand_pay':0
        } 
    
        temp.append(y)
    write_json(data)
      
try:
    update_data()

except FileNotFoundError:
    init_json_file()
    update_data()
