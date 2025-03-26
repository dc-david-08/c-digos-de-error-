import requests
import re

def captureData(url):
    try:
        respuesta = requests.get(url).text
        regexExpresion = r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?\"\s(\d{3})"
        regex = re.findall(regexExpresion, respuesta, re.MULTILINE)
        return regex
    except Exception as e:
        print(f"Error capturando datos: {e}")
        return None

def apiRequestData(data):
    JsonData = []
    if not data:
        print("No hay datos para procesar.")
        return

    URI = "http://ip-api.com/json/"
    ip_seen = set()

    for ip, code in data:
        if ip in ip_seen:
            continue  # Ya procesada

        ip_seen.add(ip)
        formatData = {"ip": ip, "code": code}

        try:
            response = requests.get(f"{URI}{ip}").json()
            formatData["country"] = response.get("country")
            formatData["city"] = response.get("city")
        except Exception as e:
            print(f"Error consultando API para {ip}: {e}")
            formatData["country"] = None
            formatData["city"] = None

        JsonData.append(formatData)

    # Imprime resultado final
    print("Datos recopilados:")
    for item in JsonData:
        print(item)

    return JsonData

# Ejecutar
resultado = captureData("https://raw.githubusercontent.com/elastic/examples/refs/heads/master/Common%20Data%20Formats/apache_logs/apache_logs")
apiRequestData(resultado)
