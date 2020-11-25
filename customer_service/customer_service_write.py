import json
import os
import datetime

td = datetime.datetime.today()
now = datetime.datetime.now()

d = td.strftime("%d_%m_%Y")
dt = now.strftime("%H:%M:%S")

path = os.path.abspath('../spa_project') + '/data/history/'
filename = d + '.json'

def add_history(fname, sname, id_c, member, employee, rooms, service_time, treatment):
    def write_json(data): 
        with open(path + filename,'w') as f: 
            json.dump(data, f)

    def init_json_file():
        init_data = {
            'HISTORY':[]
        }
        with open(path + filename, 'w') as outfile:
            json.dump(init_data, outfile)

    def update_data():
        with open(path + filename) as json_file: 
            data = json.load(json_file)

            treatment_list = list()

            for t in treatment:
                treatment_list.append(t)

            temp = data['HISTORY'] 
  
            y = {
                'seq': str(len(temp)+1),
                'time': dt,
                'id': id_c,
                'fname': fname,
                'sname': sname,
                'member': member,
                'employee': employee,
                'room': rooms,
                'service_time': service_time,
                'treatments': treatment_list
            } 
    
            temp.append(y)
        write_json(data)
      
    try:
        update_data()

    except FileNotFoundError:
        init_json_file()
        update_data()