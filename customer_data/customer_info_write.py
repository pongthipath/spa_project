import json
import os
  
path = os.path.abspath('../spa_project') + '/data/json/'
filename = 'customer_info.json'

def add_new_customer(fname, sname, id_c, treatment):
    def write_json(data): 
        with open(path + filename,'w') as f: 
            json.dump(data, f)

    def init_json_file():
        init_data = {
            'CUSTOMERS':[]
        }
        with open(path + filename, 'w') as outfile:
            json.dump(init_data, outfile)

    def update_data():
        with open(path + filename) as json_file: 
            data = json.load(json_file)

            for c in data['CUSTOMERS']:
                if(c['id'] == id_c):
                    text_r = "มีไอดีนี้ในระบบแล้ว!"
                    return str(text_r)

                if(c['fname'] == fname and c['sname'] == sname):
                    text_r = "มีชื่อนี้ในระบบแล้ว!"
                    return str(text_r)

            treatment_list = list()
            for t in treatment:
                treatment_list.append(t)

            temp = data['CUSTOMERS'] 
  
            y = {
                'fname': fname,
                'sname': sname,
                'id': id_c,
                'treatment': treatment_list
            } 
    
            temp.append(y)
        write_json(data)
        return str(fname) + " " + str(sname) + " ถูกเพิ่มแล้ว!"
      
    try:
        message = update_data()
        return message

    except FileNotFoundError:
        init_json_file()
        update_data()