import requests
import re

def captureData(url):
    try:
        respuesta = requests.get(url).text  # Obtiene el contenido como texto plano
        regexExpresion = r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?\"\s(\d{3})"
        regex = re.findall(regexExpresion, respuesta, re.MULTILINE)  # Busca todas las coincidencias
        return regex
    except Exception as e:
        print(f"Error capturando datos: {e}")
        return None

def apiRequestData(data):
    if not data:
        print("No hay datos para procesar.")
        return

    URI = "http://ip-api.com/json/"
    for ip, code in data:
        print(f"{ip}: {code}")  # Muestra IP y código HTTP
        try:
            response = requests.get(f"{URI}{ip}").json()  # Consulta API con la IP
            print(f"Ubicación de {ip}: {response.get('country')}, {response.get('city')}")
        except Exception as e:
            print(f"Error consultando API para {ip}: {e}")

# Ejecutar el proceso
resultado = captureData("https://raw.githubusercontent.com/elastic/examples/refs/heads/master/Common%20Data%20Formats/apache_logs/apache_logs")
apiRequestData(resultado)  # Procesa las IPs extraídas
