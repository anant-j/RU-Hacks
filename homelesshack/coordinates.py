import requests
import json
import sys
import API_KEYS

class Coord:
	def __init__(self, location):
		endpoint = "https://maps.googleapis.com/maps/api/geocode/json?"
		api_key = API_KEYS.keys["GOOGLE_API_KEY"]
		self.address = location.replace(" ", "+")

		nav_request = "address={}&key={}".format(
			self.address, api_key)

		request = endpoint + nav_request
		response = requests.get(request).content.decode('utf-8')
		result = json.loads(response)
		
		record = result["results"][0]["geometry"]["location"]
		self.lat = record["lat"]
		self.lng = record["lng"]

	def get_lat(self):
		return self.lat

	def get_lng(self):
		return self.lng

	def print_coord(self):
		string = str(self.lat) + "\n" + str(self.lng)

if __name__ == "__main__":
	location = "Toronro Public Library";

	place = Coord(location)
	print(place.print_coord())