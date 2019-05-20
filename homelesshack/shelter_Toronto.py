import requests
import json
import sys
import copy
import API_KEYS

from directions import *
from coordinates import *

class Shelter:
	def __init__(self, location):
		self.start = location
		link = "https://www.toronto.ca/ext/open_data/catalog/data_set_files/SMIS_Daily_Occupancy_2018.json"
		f = requests.get(link).content.decode('utf-8')
		info = json.loads(f)
		self.shelterList = [];

		for i in range(107):
			shelter = info[i];
			self.shelterList.append(copy.deepcopy(shelter));

		self.end = None


	def print_all_shelters(self):
		for shelter in self.shelterList:
			#name
			print("Name: " + shelter["SHELTER_NAME"])
			#Address:
			print("Address: " + shelter["SHELTER_ADDRESS"])
			#City:
			print("CITY: " + shelter["SHELTER_CITY"])
			#State:
			print("State: " + shelter["SHELTER_PROVINCE"])
			#Post Code:
			print("Post Code: " + str(shelter["SHELTER_POSTAL_CODE"]))
			#capacity:
			print("Capacity: " + str(shelter["CAPACITY"]))
			print()


	def find_nearest_shelter(self):
		startPlace = Coord(self.start);
		startLAT = startPlace.get_lat();
		startLNG = startPlace.get_lng();

		minDistance = 100
		nearestSltAdd = None

		for i in self.shelterList:
			address = i["SHELTER_ADDRESS"] + "," + i["SHELTER_CITY"] + "," + i["SHELTER_PROVINCE"]
			place = Coord(address)
			sltLAT = place.get_lat()
			sltLNG = place.get_lng()
			distance = (sltLAT - startLAT)**2 + (sltLNG - startLNG)**2

			if(distance < minDistance):
				minDistance = distance
				nearestSltAdd = address
		self.end = nearestSltAdd
		string = "The nearest shelter is " + "\"" + self.end + "\""
		return string

	def print_direction(self):
		dir = Direction(self.start, self.end)
		string = "It's " + dir.print_distance() + " away from your current location.\n" + "Directions:\n" + dir.print_dirs()
		string = string + "Link:\n" + "maps://www.google.com/maps/dir/" + self.start.replace(" ", "+") + "/" + self.end.replace(" ", "+")
		return string



if __name__ == '__main__':
	s = Shelter("Eaton Center, Toronton, ON")
	#s.print_all_shelters()
	print(s.find_nearest_shelter())
	print(s.print_direction())

	

