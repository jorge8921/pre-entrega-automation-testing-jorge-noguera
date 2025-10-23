# Pre-Entrega Automation Testing - Jorge Noguera

## Descripción
Este proyecto automatiza casos de prueba sobre el sitio [saucedemo.com](https://www.saucedemo.com) utilizando **Selenium WebDriver** y **Pytest**.  
Los escenarios incluyen:
- Login
- Navegación del inventario
- Carrito de compras

## Tecnologías Utilizadas
- Python 3.12
- Selenium WebDriver
- Pytest
- WebDriver Manager
- Pytest HTML Report

## Estructura del Proyecto
pre-entrega-automation-testing-jorge-noguera/
│
├── tests/
│ ├── test_login.py
│ ├── test_inventory.py
│ ├── test_cart.py
│
├── utils/
│ └── driver_factory.py
│
├── reports/
│ ├── reporte.html
│ └── screenshots/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md

## Instalación

pip install -r requirements.txt

## Ejecución de Pruebas

### Ejecutar todas las pruebas con reporte HTML:

python -m pytest


### Ejecutar un test específico:

python -m pytest tests/test_login.py

## Reportes

Los reportes HTML se guardan en la carpeta /reports/
Ejemplo: reports/reporte.html

Las capturas de errores se guardan en:
reports/screenshots/

Para acceder, desde CMD ejecuta el comando: start reports/reporte.html
## Casos de Prueba Incluidos
Test	            Descripción
test_login.py	    Login con credenciales válidas y validación de redirección
test_inventory.py	Validación de título, productos y elementos de interfaz
test_cart.py	    Agregar producto al carrito y validación del ítem agregado

## Comando para Generar Reporte Manual
pytest pre-entrega-final/test_saucedemo.py -v --html=reporte.html
