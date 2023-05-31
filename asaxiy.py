from bs4 import BeautifulSoup
import requests
from db import DB


db = DB('sovutgichlar.json')

def get_html(url):
    r = requests.get(url)
    return r.text

def get_href(html):
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find('div', class_="col-lg-9 col-md-12")
    products = div.find('div', class_="row custom-gutter mb-40")
    products_all_div = products.find_all('div', class_="col-6 col-xl-3 col-md-4")
    
    href_list = []
    for product in products_all_div:
        a = product.find('a')
        href = 'https://asaxiy.uz' + a.get('href')
        href_list.append(href)
    return href_list

def product_info(href_list:list):
    for href in href_list:
        html = get_html(href)
        soup = BeautifulSoup(html, 'html.parser')
        
        card_info = soup.find('div', class_="more__about-content")

        h1 = card_info.find('h1', class_="product-title").text
        brend = card_info.find('span', class_="text__content-name").text
        model = card_info.find('div', class_="text__content d-flex align-items-center mr-3").find('a').text.strip()
        priys = card_info.find('span', class_="price-box_new-price").text.strip()
        img = soup.find('div', class_="swiper-wrapper").find('img').get('src')

        db.add_data(h1, brend, model, priys, img)



html = get_html("https://asaxiy.uz/uz/product/bytovaya-tehnika/krupnaya-tehnika-dlya-kuhni/morozilniki")
# print(html)
href_list = get_href(html)
 
product_data = product_info(href_list)
# print(product_data)