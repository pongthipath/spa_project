import json
import os

def get_booking_table(d):
    path = os.path.abspath('../spa_project') + '/data/booking/'
    filename = d + '.json'
    with open(path + filename) as json_file:
        data = json.load(json_file)

        return data['BOOKING']