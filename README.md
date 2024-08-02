# ScrapBack
Desarrollado en Python 3.12.3

Aplicación backend es para ser consumida por ScrapFront.

Esta aplicación ha sido desarrollada con el único propósito de aprender y experimentar con Python, Selenium, requests, BeautifulSoup y Django.

No está diseñada para su uso en producción ni ofrece garantías de estabilidad.

**Todos los scrapers utilizados en esta aplicación han sido desarrollados por mí para fines educativos.**

Para hacer funcionar alguno de los scrappers, necesitas descargar un webdriver de chrome compatible con tu actual navegador de chrome. en mi caso, uso chrome-headless-shell-win64.

Esta aplicacion hace peticiones a las paginas webs de makro, carrefour, el corte ingles y alcampo, devuelve JSONs que son aprovechados en un ScrapBack.

## Setup

- Instalar Python 3.12.x como mínimo -> https://www.python.org/
- Iniciar un proyecto con Django -> https://www.djangoproject.com/
- Instalar BeautifulSoup -> https://beautiful-soup-4.readthedocs.io/en/latest/
- Instalar Selenium -> https://www.selenium.dev/documentation/webdriver/getting_started/install_library/
- Descargar Webdriver compatible con **Google Chrome** : https://developer.chrome.com/docs/chromedriver/downloads?hl=es-419

Una vez tengamos todo instalado, en la carpeta del proyecto ejecutamos:
```sh
python manage.py migrate
```
Se nos migraran datos, se aplicaran cambios, etc...

# Compilación y reload activo
```sh
py manage.py runserver
```
