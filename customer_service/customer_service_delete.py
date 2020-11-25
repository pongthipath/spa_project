import json
import os

def delete_customer_service_info_by_seq(name, d):
    path = os.path.abspath('../spa_project') + '/data/history/'
    filename = d + '.json'

    def write_json(data): 
        with open(path + filename,'w') as f: 
            json.dump(data, f) 

    with open(path + filename) as json_file:
        data = json.load(json_file)
        for p in data['HISTORY']:
            if(p['seq'] == name):
                data['HISTORY'].remove(p)

        write_json(data)