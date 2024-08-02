# ScrapBack
Desarrollado en Python 3.12.3

Aplicación backend es para ser consumida por ScrapFront.

Esta aplicación ha sido desarrollada con el único propósito de aprender y experimentar con Python, Selenium, requests, BeautifulSoup y Django.

No está diseñada para su uso en producción ni ofrece garantías de estabilidad.

**Todos los scrapers utilizados en esta aplicación han sido desarrollados por mí para fines educativos.**
- Carrefour ha dejado de funcionar debido a que se ha restringido el acceso a los datos que intentaba recuperar.

## Descripción
Esta aplicación realiza peticiones a las páginas web de Makro, Carrefour, El Corte Inglés y Alcampo, recuperando productos de sus sitios. Los datos obtenidos se devuelven en formato JSON, los cuales son utilizados en ScrapFront.

## Setup

- Instalar Python 3.12.x como mínimo -> https://www.python.org/
- Descargar Webdriver compatible con tu version de **Google Chrome** : https://developer.chrome.com/docs/chromedriver/downloads?hl=es-419

Una vez tengamos todo instalado, en la carpeta del proyecto ejecutamos:
```sh
python manage.py migrate
```
Se nos migraran datos, se aplicaran cambios, etc...

### Compilación y reload activo
```sh
py manage.py runserver
```
```sh
py manage.py runserver 0.0.0.0:9000
```
