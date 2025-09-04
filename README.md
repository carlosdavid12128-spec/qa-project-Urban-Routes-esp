Urban Routes - Pruebas Automatizadas (POM) Este proyecto contiene pruebas automatizadas para la aplicación web Urban Routes, específicamente para el flujo de pedir un taxi. Está desarrollado en Python utilizando el patrón Page Object Model (POM) y la librería Selenium para la automatización de pruebas en navegador.

📂 Estructura del Proyecto data.py Contiene datos estáticos y configuraciones necesarias para las pruebas (URLs, datos de prueba, etc.).

urban_routes_page.py Implementa la clase de la página principal siguiendo el patrón POM. Incluye los localizadores y métodos para interactuar con los elementos de la aplicación web Urban Routes.

test_urban_routes.py Contiene los casos de prueba automatizados. Verifica el flujo de pedir un taxi desde el inicio de sesión hasta la confirmación del viaje.

retrieve_code.py Contiene la lógica para recuperar el código de confirmación enviado al número de teléfono ingresado en la aplicación web.

⚙️ Requisitos Python 3.8+

Google Chrome y ChromeDriver (compatibles con tu versión de Chrome)

Librerías Python: selenium selenium pytest

🧩 Flujo probado Abrir la aplicación web Urban Routes.

Ingresar direcciones "Desde" y "Hasta"

Seleccionar la tarifa "Confort"

Ingresar número de teléfono.

Recuperar código de confirmación (mediante retrieve_code.py).

Ingresar código y acceder.

Ingresar los datos de la tarjeta bancaria de data.py

Agregar manta y pañuelos, y dos helados (sliders y contadores)

Solicitar un taxi

Validar que la solicitud sea exitosa.
