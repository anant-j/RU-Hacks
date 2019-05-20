import requests
import json
import mapbox

import API_KEYS

class MapBoxAPI:
    def __init__(self, location):
        self.location = location
        self.API_KEY = API_KEYS.keys['MAPBOX_API_KEY']
        self.geocoder = mapbox.Geocoder(access_token = self.API_KEY)
    
    def get_postal_code(self):
        data =  self.geocoder.forward(self.location).json()
        data_ids = data['features'][0]['context']
        for ids in data_ids:
            if "postcode" in ids['id']:
                return "".join(ids['text'].split(" "))
        return None    

if __name__ == '__main__':
    m = MapBoxAPI("McMaster University")
    print(m.get_postal_code())