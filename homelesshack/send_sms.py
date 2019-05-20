from twilio.rest import Client
import API_KEYS

import FoodBanksCanadaScraper
import WeatherAPI
import shelter_Toronto

def send_sms(location, contact):
    
    lst = []
    
    account_sid = API_KEYS.keys['MY_ACCOUNT_SID']
    auth_token = API_KEYS.keys['MY_AUTH_TOKEN']
    
    f = FoodBanksCanadaScraper.FoodBanksCanadaScraper(location)
    food_bank = f.get_nearest_food_bank()
    food_dir = f.get_directions()
    
    w = WeatherAPI.WeatherAPIClass(location)
    weather = w.get_current_weather()
    
    s = shelter_Toronto.Shelter(location)
    shelter = s.find_nearest_shelter()
    shel_dir = s.print_direction()
    
    lst.append(shelter)
    lst.append(shel_dir)
    
    lst.append(food_bank)
    lst.append(food_dir)
    
    lst.append(weather)

    items = "\n".join(lst)

    client = Client(account_sid, auth_token)
    client.messages.create(
            to = contact,
            from_ = API_KEYS.keys['MY_TWILIO_NUMBER'],
            body=items
        )
