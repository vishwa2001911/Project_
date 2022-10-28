# This Program will create CSV file which Contain list of vacancises ublished by ptopjobs.lk website 

# example url " http://topjobs.lk/applicant/vacancybyfunctionalarea.jsp?FA=AGD "


from bs4 import BeautifulSoup as bf
import pandas as pd
import requests
import csv




def topjobs(url):
    link = requests.get(url).text

    soup = bf(link, 'lxml')

    f = open("jobs.csv","w", newline="")
    row_1 = ("Company_name","Post","Opening_date","Closing_date",f"Job_link:- {url}")
    writer = csv.writer(f)
    writer.writerow(row_1)

    d = soup.find('div', class_='cate-lister-view')
    date = d.table.find("tr", id="tr0")

    for num in range(0,19):
        row_2 = (d.table.find("tr", id=f"tr{num}").h1.text, d.table.find("tr", id=f"tr{num}").h2.text, date.find_all('td', width="14%")[0].text, date.find_all('td', width="14%")[1].text,None)
        writer.writerow(row_2)
        print('company name :- ', d.table.find("tr", id=f"tr{num}").h1.text)
        print('Post         :- ', d.table.find("tr", id=f"tr{num}").h2.text)
        print('Opening date :- ', date.find_all('td', width="14%")[0].text)
        print('Closing date :- ', date.find_all('td', width="14%")[1].text,"\n")

    f.close()
    

    
link1 = input("input your top jobs link:-")
 
if __name__ == '__main__':
  topjobs(link1)
