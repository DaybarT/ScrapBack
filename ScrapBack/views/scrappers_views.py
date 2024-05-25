from django.http import JsonResponse,HttpResponse
from ..scrappers.alcampo import Alcampo
from ..scrappers.eci import ECI
from ..scrappers.makro import Makro
from ..scrappers.carrefour import Carrefour
import json
import threading
lock = threading.Lock()

class Scrappy():
   
    def makro(self, producto):
       instance = Makro(producto)
       makro = instance.scrapper()
       return HttpResponse(makro, content_type="application/json")
        
    def carrefour(self, producto):
       instance = Carrefour(producto)
       carrefour = instance.scrapper()
       return HttpResponse(carrefour, content_type="application/json")
    
    def alcampo(self, producto):
       instance = Alcampo(producto)
       alcampo = instance.scrapper()
       return HttpResponse(alcampo, content_type="application/json")
    
    def eci(self, producto):
       instance = ECI(producto)
       eci = instance.scrapper()
       return HttpResponse(eci, content_type="application/json")
    
    def all_scrappers(self, producto):
       
       with lock:
         makro_instance = Makro(producto)
         makro_data = makro_instance.scrapper()
         
         eci_instance = ECI(producto)
         eci_data = eci_instance.scrapper()
         
         alcampo_instance = Alcampo(producto)
         alcampo_data = alcampo_instance.scrapper()
         
         carrefour_instance = Carrefour(producto)
         carrefour_data = carrefour_instance.scrapper()
         
         #valora threading
         
         response = {
            "makro": json.loads(makro_data),
            "eci": json.loads(eci_data),
            "alcampo": json.loads(alcampo_data),
            "carrefour": json.loads(carrefour_data),
            
         }
         data = json.dumps(response, indent=4)
         return HttpResponse(data, content_type="application/json")
      