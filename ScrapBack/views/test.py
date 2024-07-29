from django.http import JsonResponse,HttpResponse

class TestView():
    def get(self):
        return JsonResponse({"texto":"OK"})
    
    def test_alcampo(self):
        return JsonResponse({
            "producto": "MAHOU CLASICA Cervezas pack de 12 latas de 33 centilitros",
            "disponible": True,
            "precio": "6.79",
            "precio_litro": "1.71",
            "imagen": "https://www.compraonline.alcampo.es/images-v3/37ea0506-72ec-4543-93c8-a77bb916ec12/28369924-1272-4a22-8ee3-b90a4c5f8885/300x300.jpg",
            "url": "https://www.compraonline.alcampo.es/products/34870"
        })
    
    def test_eci(self):
        return JsonResponse({
            "product_name": "MAHOU CLASICA cerveza rubia original pack 12 latas 33 cl",
            "product_price_final": "8.64",
            "url_to_buy": "https://www.elcorteingles.es//supermercado/0110118600300364-mahou-clasica-cerveza-rubia-original-pack-12-latas-33-cl/",
            "imagen_src": "//sgfm.elcorteingles.es/SGFM/dctm/MEDIA03/202306/22/00118600300364____10__325x325.jpg"
        })
    
    def test_makro(self):
        return JsonResponse({"name_product": "Mahou cerveza cl\u00e1sica 25cl contiene 24 botellas",
        "unity_price": "0,41Unidad",
        "total_price": "9,95",
        "price_w_iva": "12,04 Incl. IVAIGIC",
        "image": "https://cdn.metro-group.com/es/es_pim_238030001001_01.png?format=jpg&quality=80&dpi=72&w=144&h=144",
        "url": "https://tienda.makro.es/shop/pv/BTY-X238072/0032/0021"})