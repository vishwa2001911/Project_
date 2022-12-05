#import datetime as dt 
import ip_details
import requests

api_key = open('api_key.txt', 'r').read()



city_name = ip_details.get_ip_details.city()

url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
response = requests.get(url).json()

class weather:
    def __init__(self, response, url):

        self.url = url
        self.response = response
        
    def data():
        return response
        
    def clouds():
        return str(response["clouds"]["all"])+"%"
    
    def temp_kelvin_to_celcius(): 
        C = response["main"]["temp"]-273.15
        return f"{round(C, 1)}°C
    
    def humidity():
        return str(response["main"]["humidity"])+"%"
        
