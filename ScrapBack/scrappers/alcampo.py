# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import json

# -> py manage.py runserver para runnear el server
# -> python manage.py runserver 0.0.0.0:9000 
# 0.0.0.0 para conectarlo con tu maquina virtual pon la direccion ip de tu equipo local para conectar.

class Alcampo():
    
    def __init__(self, producto):
        self.producto = producto
        
    def scrapper(self):
        website = "https://www.compraonline.alcampo.es/search?q="+self.producto
        res = requests.get(website)
        content = res.text
        soup = BeautifulSoup(content, 'html.parser')

        data = soup.find_all('script', attrs={"data-test": "initial-state-script"})

        # Extrae el contenido de la etiqueta <script>
        data = data[0]

        script_content = data.string



        # Limpia el contenido para asegurarte de que solo obtengas el JSON
        start_index = script_content.find('window.__INITIAL_STATE__=') + len('window.__INITIAL_STATE__=')
        json_str = script_content[start_index:]


        try:
            json_data = json.loads(json_str)
            # Accede a los datos relevantes dentro del objeto JSON
            json_content = json_data['data']
            # Ahora puedes trabajar con los datos según sea necesario
            # print(data)
            
        except json.JSONDecodeError as e:
            print("Error al decodificar JSON:", e)

        #hasta aqui funciona

        alcampo = []

        for i in json_content['products']['productEntities'].values():

            alcampo.append({
                # 'marca': i['brand'],
                'producto': i['name'],
                'disponible': i['available'],
                'precio': i['price']['current']['amount'],
                'precio_litro': i['price']['unit']['current']['amount'],
                'imagen': i['image']['src'],
                'url': 'https://www.compraonline.alcampo.es/products/'+i['retailerProductId']
            })
            
        return json.dumps(alcampo, indent=4)
