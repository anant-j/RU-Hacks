from bs4 import BeautifulSoup
import requests
import re

import MapBoxAPI
from directions import *

class FoodBanksCanadaScraper:
    def __init__(self, location):
        self.location = location

        m = MapBoxAPI.MapBoxAPI(self.location)
        
        self.post_code = m.get_postal_code()

        if self.post_code:
            self.page_URL = "https://www.foodbankscanada.ca/Utility-Pages/Find-a-Food-Bank.aspx?postalcode=" + self.post_code

        self.destination = None;

    def get_nearest_food_bank(self):
        if not self.post_code:
            return "Sorry, please try another monument near you."
    
        site = requests.get(self.page_URL).content
        soup = BeautifulSoup(site, 'html5lib')
        food_bank = str(soup.find("div", {'id':lambda x: x and x.startswith("details")}))
        food_bank = re.sub(r'[<]+([/]*[A-Z]*[a-z]*[0-9]*[ ]*[=]*["]*)*[/]*[>]+', "", food_bank)
        
        items = food_bank.split("\n")[1:]
        
        for item in range(len(items)):
            items[item] = re.sub(r'\xa0', " ", items[item])
        
        items[2] = items[2] + " " + items[3]
        thing = ['name', 'distance', 'address']
        dicts = {thing[i]:items[i] for i in range(3)}
        self.destination = dicts['name']
        return "The nearest food bank is called " + dicts['name'] + " and is located at " + dicts['address'] + ", and is at " + dicts['distance'] + " from your current location."
        
    def get_directions(self):
        dir = Direction(self.location, self.destination)
        string = "Directions:\n" + dir.print_dirs()
        string = string + "Link:\n" + "maps://www.google.com/maps/dir/" + self.location.replace(" ", "+") + "/" + self.destination.replace(" ", "+")
        return string
        
            
if __name__ == '__main__':
    a = FoodBanksCanadaScraper("Ryerson University")
    print(a.get_nearest_food_bank())
    print(a.get_directions())
    