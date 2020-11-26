import json
import os
  

def add_booking(d, row, column, table):
    path = os.path.abspath('../spa_project') + '/data/booking/'
    filename = d + '.json'
    def write_json(data): 
        with open(path + filename,'w') as f: 
            json.dump(data, f)

    def init_json_file():
        r_list = list()
        for i in range(row):
            c_list = list()
            for j in range(column):
                empty_data = ''
                c_list.append(empty_data)
            r_list.append(c_list)

        init_data = {
            'BOOKING':r_list
        }
        with open(path + filename, 'w') as outfile:
            json.dump(init_data, outfile)

    def update_data():
        with open(path + filename) as json_file: 
            data = json.load(json_file)

            data['BOOKING'] = table
  
        write_json(data)
      
    try:
        update_data()

    except FileNotFoundError:
        init_json_file()
        update_data()