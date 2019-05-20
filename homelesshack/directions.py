import requests
import json
import sys
import API_KEYS
import re

class Direction:
    def __init__(self, start, end):
        endpoint = "https://maps.googleapis.com/maps/api/directions/json?"
        api_key = API_KEYS.keys["GOOGLE_API_KEY"]
        self.origin = start.replace(" ", "+")
        self.destination = end.replace(" ", "+")

        nav_request = "origin={}&destination={}&mode=walking&key={}".format(
	        self.origin, self.destination, api_key)

        request = endpoint + nav_request
        response = requests.get(request).content.decode('utf-8')
        directions = json.loads(response)
        
        self.distance = directions["routes"][0]["legs"][0]["distance"]["text"]
        
        self.results = []
        for i in range(len(directions["routes"])):
            for x in directions["routes"][i]["legs"][0]["steps"]:
                self.results.append(x["html_instructions"])

    def print_distance(self):
            return self.distance
        
    def print_dirs(self):
        string = ""
        for i in self.results:
            string += re.sub('<[^<]+?>', ' ', i) + "\n"
        return string

if __name__ == "__main__":
    start = "229 Emerson St, Hamilton"
    end = "McMaster University"
    
    dic = Direction(start, end)
    print(dic.print_distance())
    print(dic.print_dirs())

