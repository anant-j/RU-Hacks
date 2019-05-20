import requests
import json
import API_KEYS

class WeatherAPIClass:
    def __init__(self, location):
        self.API_KEY = API_KEYS.keys["OPENWEATHERAPI_SECRET_KEY"]
        self.cities_list = ["montreal", "toronto", "brampton", "mississauga", "hamilton"]
        
        self.location = location.lower()
        changed = False
        for l in self.cities_list:
            if l in self.location:
                self.location = l
                changed = True
                
        if not changed:
            self.location = False
        
        self.BASE_URL = "http://api.openweathermap.org/data/2.5/forecast?q="
        
    def get_current_weather_data(self):
        self.location = self.location.lower()
        
        weather_link = self.BASE_URL + self.location + ",ca?&appid=" + self.API_KEY

        response = requests.get(weather_link)
        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
    
    def get_current_weather(self):
        if self.location:           
            data = self.get_current_weather_data()
            
            temp = round(data['list'][0]['main']['temp'] - 273.15, 2)
            text = data['list'][0]['weather'][0]['main'].lower()
            
            verbs = self._get_verb(text)
                
            return "Current weather is " + str(temp) + " degrees Celsius and " + verbs + " " + text + "."
        
        return "You have entered an invalid city. Please choose from 'Toronto, Brampton, Mississauga, or Hamilton."
    # def send_data_to_twillio(self):
    #     data = self.
    #     return data
    #     #SEND DATA TO TWILLIO ONCE UPGRADED
    
    def _get_verb(self, text):

        if text in ['clear']:
            verbs = "it is"
        elif text in ['rain']:
            verbs = "there is"
        else:
            verbs = "there are"
            
        return verbs
if __name__ == '__main__':
    w = WeatherAPIClass("toronto")
    print(w.get_current_weather())    