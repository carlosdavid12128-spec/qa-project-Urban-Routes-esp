
# Urban Routes - Pruebas Automatizadas (POM) 

Este proyecto contiene pruebas automatizadas para la aplicación web Urban Routes, específicamente para el flujo de pedir un taxi. Está desarrollado en Python utilizando el patrón Page Object Model (POM) y la librería Selenium para la automatización de pruebas en navegador.


## Estructura del proyecto

Arhivos y directorios principales

- data.py: Archivo encargado de manejar los datos del proyecto.

- main.py: Archivo en donde se desarrollan las pruebas automatizadas
## Tecnologias utilizadas

- Pycharm: Entorno de Desarrollo Integrado para trabajar con Python.

- Pytest: Framework para Python que permite la ejecución de pruebas automatizadas de manera simple, escalable y expresiva.

- Python: Lenguaje de programación principal del proyecto.

- Selenium WebDriver: Herramienta que permite la automatización de pruebas mediante el control de navegadores web.

- Assert: Confirma los resultados esperados en cada paso de la prueba.

- WebDriverWait: Herramienta de espera explícita que se usa en Selenium WebDriver para decirle al script que espere hasta que ocurra una condición específica antes de continuar.

- Expected Conditions (EC): Son condiciones predefinidas que se usan junto con WebDriverWait en Selenium para esperar hasta que algo específico ocurra en la página web.

- Google Chrome y ChromeDriver: Navegador y controlador utilizados para la ejecución de las pruebas.
## Explicacion de las pruebas 

- test_set_route: Verifica que la ruta de origen y destino se puede establecer correctamente.

- test_select_confort_rate: Comprueba la selección de la tarifa "Comfort"

- test_type_phone_number: CValida la autenticación con código SMS.

- test_payment_method: Añade y verifica un método de pago.

- test_message_for_driver: Envía un mensaje al conductor.

- test_slider_for_blanket: Activa la opción de cobija y pañuelo.

- test_counter_for_ice_cream: Incrementa el contador de helado.

- test_order_taxi_button: Solicita un taxi exitosamente.

- test_order_button:  Muestra los modales del contador y de la información del viaje.

IMPORTANTE

- Se recomienda cerrar todas las ventanas del navegador antes de ejecutar las pruebas para evitar conflictos.

- Asegúrate de actualizar la URL de Urban Routes data.py antes de ejecutar las pruebas.

## Estructura del archivo de prueba test_urban_routes.py

Imports utilizados

El código usa los siguientes imports:

```bash
from data import data

from selenium import webdriver

from selenium.webdriver import Keys

from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.chrome.service import Service

from data.data import phone_number, card_code, card_number, message_for_driver

from pages import urban_routes_page as urp

---

Carlos Flores, Cohorte 33, Sprint 8

```


