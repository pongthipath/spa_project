import json
import os

def edit_seq_customer_service(d):
    path = os.path.abspath('../spa_project') + '/data/history/'
    filename = d + '.json'

    def write_json(data): 
        with open(path + filename,'w') as f: 
            json.dump(data, f) 

    with open(path + filename) as json_file:
        data = json.load(json_file)
        count = 1
        for p in data['HISTORY']:
            p['seq'] = str(count)
            count += 1

        write_json(data)