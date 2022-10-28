import requests

accessKey = open("apiip_api_key.txt", 'r').read()
url = 'http://apiip.net/api/check?'+'&accessKey='+ accessKey
response = requests.get(url).json()

class get_ip_details:
    
    def __init__(self,url,response):
        
        self.url = url
        self.response = response
    
    def data():
        return response
    
    def latitude():
        return response["latitude"]
    
    def longitude():
        return response["longitude"]
    
    def city():
        return response['capital']
    
    def ip():
        return response["ip"]
    
    def country_name():
        return response["countryName"]
    
data()