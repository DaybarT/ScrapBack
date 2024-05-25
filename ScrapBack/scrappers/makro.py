from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# -> py manage.py runserver para runnear el server

class Makro():
    
    def __init__(self, producto):
        self.producto = producto
        
    def scrapper(self):
    
        options =  Options()
        options.headless =  True
        # options.add_argument('--headless') 
        #no necesita cargar javascript para recuperar los productos, pero si lo haces con headless recoge errores de la consola de JS, 
        #sin headless, tenemos un resultado mas limpio.

        driver = webdriver.Chrome(options=options)

        website = "https://tienda.makro.es/shop/search?q="+self.producto
        driver.get(website)
        time.sleep(5)
        html = driver.page_source

        # Imprimir el HTML o realizar otras operaciones con él


        # Cerrar el navegador
        driver.quit()

        soup = BeautifulSoup(html, 'html.parser')
        caja = soup.find('div',class_='mfcss_card-article-2--grid-container-flex')


        products = caja.find_all('div', class_='sd-articlecard') #recogemos las tarjetas de los productos

        makro = []

        for product in products:

            pictures_container1 = product.find('div', class_='image-container')

            pictures_container2 = pictures_container1.find('a', class_='image')
            pictures = pictures_container2.find('img').get('src')

            unity_price = product.find('div', class_='additional-price-info-row').text.strip()
            total_price = product.find('div', class_='price-display-main-row').text.strip()
            price_w_iva = product.find('div', class_='secondary-price-row').text.strip()
            url_content = product.find('a', class_='image').get('href')
            url = url_content.split('/', 6)

            name_product =product.find('a', class_='image').get('description')
            
            cleaned_unity_price = unity_price.replace("\u00a0", "").replace("\u20ac", "").replace("/", "").strip()
            cleaned_total_price = total_price.replace("\u00a0", "").replace("\u20ac", "").replace("/", "").strip()
            cleaned_price_w_iva = price_w_iva.replace("\u00a0", "").replace("\u20ac", "").replace("/", "").strip()

            cleaned_price_w_iva = ' '.join(reversed(cleaned_price_w_iva.split()))
            
            makro.append({
                "name_product": name_product,
                "unity_price": cleaned_unity_price,
                "total_price":cleaned_total_price,
                "price_w_iva":cleaned_price_w_iva,
                "image": pictures,
                "url": "https://tienda.makro.es" + '/'.join(url[:6])
            })

        return json.dumps(makro, indent=4)


