# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import json
import random

# -> py manage.py runserver para runnear el server

# headers_request = 'https://www.carrefour.es/headers'

class Carrefour():
    
    def __init__(self, producto):
        self.producto = producto
        
    def scrapper(self):
        
        website = "https://www.carrefour.es/search-api/query/v1/search?query="+self.producto+"&lang=es"
        user_agent_list = [ 
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36', 
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36', 
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15', 
        ]
        for i in range(1,4): 
            user_agent = random.choice(user_agent_list)

        # a veces funciona, tienen antiBOT, el user agent puede ser no valido, o si detectan que no es un user-agent legitimo, la respuesta sera tipica de un antibot.
        print(user_agent)

        headers = {'User-Agent': user_agent}

        # res = requests.get(headers_request, headers=headers)
        res = requests.get(website, headers=headers)

        content = res.text
        # print(content)
        data = json.loads(content)
        # print(data['content']['docs'])

        carrefour = []

        for i in data['content']['docs']:
            carrefour.append({
                'producto': i['display_name'],
                'precio': i['active_price'],
                'image': i['image_path'],
                # 'marca': i['brand'],
                'url': "https://www.carrefour.es"+i['url']
            })

        return json.dumps(carrefour, indent=4)

