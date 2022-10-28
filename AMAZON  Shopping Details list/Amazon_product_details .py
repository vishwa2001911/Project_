from selenium import webdriver
from bs4 import BeautifulSoup as bf
import requests
import csv



search_term = input("Input your search item :- ")
driver = webdriver.Chrome(executable_path="/home/vishwa/chromedriver")


# this  get_url(search_term) function create link to AMAZON site
def get_url(search_term):
    #url = f"https://www.amazon.com/s?k={product_name}"
    search_term_replace = search_term.replace(" ","+")
    
    return f"https://www.amazon.com/s?k={search_term_replace}"


driver.get(get_url(search_term))
soup = bf(driver.page_source, "html.parser")
driver.close()

f = open("AMAZON products details.csv","w", newline="")
row_1 = ("product_title","product_price","availability","ships_from","sold_by","return_policy","shipping_details","Product link")
writer = csv.writer(f)
writer.writerow(row_1)




driver_2= webdriver.Chrome(executable_path="/home/vishwa/chromedriver")
print("Pls wait your fils is creating......")

all_page_links = soup.find_all("a", class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")


def get_all_products_details():
    
    for sub_link in all_page_links:
        list_url_ = sub_link.attrs["href"]
        sub_url = f"https://www.amazon.com{list_url_}\n"
        driver_2.get(sub_url)
        soup_2 = bf(driver_2.page_source, "html.parser")

        product_title = soup_2.find("span", id="productTitle").text
        product_price = soup_2.find("span", class_="a-offscreen").text
        #try:
        #    product_price = soup_2.find("span", class_="a-offscreen").text
        #except:
        #    product_price = "deficult to provide"

        shipping_details = soup_2.find("span", class_="a-size-base a-color-secondary").text
        Delivery_date = soup_2.find("span", class_="a-text-bold").text
        availability = soup_2.find("div", id="availability").span.text
        #ratings = soup_2.find("span", class_="a-size-medium a-color-base").text
        #totle_price = soup_2.find("div", style="display: block;").find_all("span")[1].text
        ships_from = soup_2.find("div", class_="tabular-buybox-text a-spacing-none").span.text
        #sold_by = soup_2.find_all("span", class_="a-size-small")[11].text
        return_policy = soup_2.find("span", id="productSupportAndReturnPolicy-return-policy-celWidget").a.text
        row_2 = (product_title,product_price,availability,ships_from,return_policy,shipping_details,sub_url)
        writer.writerow(row_2)
    
    
    driver_2.close()

def get_top_10_products_details():
        
    for sub_link in all_page_links[0:10]:
        list_url_ = sub_link.attrs["href"]
        sub_url = f"https://www.amazon.com{list_url_}\n"
        driver_2.get(sub_url)
        soup_2 = bf(driver_2.page_source, "html.parser")

        product_title = soup_2.find("span", id="productTitle").text
        product_price = soup_2.find("span", class_="a-offscreen").text
        #try:
        #    product_price = soup_2.find("span", class_="a-offscreen").text
        #except:
        #    product_price = "deficult to provide"

        shipping_details = soup_2.find("span", class_="a-size-base a-color-secondary").text
        Delivery_date = soup_2.find("span", class_="a-text-bold").text
        availability = soup_2.find("div", id="availability").span.text
        #ratings = soup_2.find("span", class_="a-size-medium a-color-base").text
        #totle_price = soup_2.find("div", style="display: block;").find_all("span")[1].text
        ships_from = soup_2.find("div", class_="tabular-buybox-text a-spacing-none").span.text
        #sold_by = soup_2.find_all("span", class_="a-size-small")[11].text
        return_policy = soup_2.find("span", id="productSupportAndReturnPolicy-return-policy-celWidget").a.text
        row_2 = (product_title,product_price,availability,ships_from,return_policy,shipping_details,sub_url)
        writer.writerow(row_2)
    
    
    driver_2.close()


 
what_you_want = input("If you want all product links type 'all' if you want top to praducts details in list type  '10' :-  " ).lower()

try:
    if what_you_want == 'all':
        print("This will take more time...")
        get_all_products_details()
    elif what_you_want == '10':
        print("This will take more time...")
        get_top_10_products_details()
except:
    print("pls check what you enter ")

    
print("Your file is done.. ")
driver_2.close()


if __name__ == "__main__":
    get_url()
    
