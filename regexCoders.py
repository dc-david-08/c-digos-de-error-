import requests, json, re

def captureData(url):
    try:
        respuesta = requests.get(url).json()
        regexExpresion = "^[a-zA-Z]+$"
        regex = re.findall(respuesta, regexExpresion)
    except Exception as e:
        respuesta = None

