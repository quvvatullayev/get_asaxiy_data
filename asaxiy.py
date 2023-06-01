from bs4 import BeautifulSoup
import requests
from db import DB


path = 'tkuv_mashenalar'
db = DB(f'uyuchun_texnikalar/{path}.json')

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
        names = card_info.find('div', class_="mb-3 d-flex flex-wrap")
        brend = names.find('span', class_="text__content-name").text
        model = names.find('div', class_="text__content d-flex align-items-center").find('span', class_="text__content-name").text
        priys = card_info.find('span', class_="price-box_new-price").text.strip()
        img = soup.find('div', class_="swiper-wrapper").find('img').get('src')

        db.add_data(h1, brend, model, priys, img)



url = "https://asaxiy.uz/uz/product/bytovaya-tehnika/tehnika-dlya-doma-2/shvejnye-mashiny-i-oborudovanie"
html = get_html(url)
# print(html)
href_list = get_href(html)
 
product_data = product_info(href_list)
# print(product_data)