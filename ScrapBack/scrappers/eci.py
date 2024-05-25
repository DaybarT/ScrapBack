from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# -> py manage.py runserver para runnear el server

# options =  Options()
# options.headless =  True
# options.add_argument('--headless') 
#necesita javascript para cargarse

class ECI():
    
    def __init__(self, producto):
        self.producto = producto
        
    def scrapper(self):
        
        driver = webdriver.Chrome()

        website = "https://www.elcorteingles.es/supermercado/buscar/?term="+self.producto
        driver.get(website)
        time.sleep(5)
        html = driver.page_source

        # Cerrar el navegador
        driver.quit()

        soup = BeautifulSoup(html, 'html.parser')

        caja = soup.find('div',attrs={"data-page": "1"})


        productos = soup.find_all('div', attrs={"data-scope": "product"})
        eci = []

        for producto in productos:
            # Encuentra todos los enlaces dentro de cada producto
            links = producto.find_all('a', attrs={"data-event": "product_click"})
            
            for link in links:
                # Obtiene la URL del enlace
                redirecciones = link.get('href')
                url_to_buy = 'https://www.elcorteingles.es/' + redirecciones

                # Encuentra todas las imágenes dentro de cada enlace
                imgs = link.find_all('img')
                
                # Itera sobre las imágenes encontradas
                for img in imgs:
                    # Obtiene la URL de la imagen
                    imagen_src = img.get('src')

            # Obtiene el valor del atributo 'data-json' de cada elemento
            data_json = producto.get('data-json')
            
            # Parsea el JSON
            json_data = json.loads(data_json)

            # Extrae la información requerida del JSON
            product_id = json_data['id']
            product_name = json_data['name']
            product_price_final = json_data['price']['final']
            product_price_currency = json_data['price']['currency']

            objeto = {
                # "product_id": product_id,
                "product_name": product_name,
                "product_price_final": product_price_final,
                "url_to_buy": url_to_buy,
                "imagen_src": imagen_src
            }

            # Agrega el objeto al array
            eci.append(objeto)
            
        return json.dumps(eci, indent=4)