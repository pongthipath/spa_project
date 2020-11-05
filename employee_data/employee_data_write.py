import json 
import os

path = os.path.abspath('../spa_project') + '/data/json/'
filename = 'employees.json'

def add_new_employee(name):
    

    print(name)
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
                'name': str(name),
                'hand_pay':[]
            } 
    
            temp.append(y)
        write_json(data)
      
    try:
        update_data()

    except FileNotFoundError:
        init_json_file()
        update_data()

