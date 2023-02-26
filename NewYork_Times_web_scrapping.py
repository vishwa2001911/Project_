# get NewYork Times artical list by using beautiful soup

from bs4 import BeautifulSoup as bf
import requests

def get_artical_list():
    
    artical_list = []
    try:
        url = requests.get("https://www.nytimes.com/").text
        soup = bf(url)
        
        for i in soup.find_all("section", class_="story-wrapper"):
            artical_list.append(i.find("h3", class_="indicate-hover").text)
            
    except:
        pass

    return artical_list


if __name__=="__main__":
    print(get_artical_list())
